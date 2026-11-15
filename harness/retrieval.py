#!/usr/bin/env python3
"""LiSSA's retrieval step: the 20 code files most similar to each requirement, with rank and cosine similarity.

RQ2 and RQ3 must judge exactly the pairs LiSSA judged in RQ1, so this repeats LiSSA's retrieval exactly: whole files,
bge-m3 vectors, cosine similarity computed as LiSSA computes it, sorted from most to least similar (ties keep LiSSA's
order), top 20. The vectors come either from RQ1's saved LiSSA answers (same vectors, so the same pairs) or from
Ollama on this machine (for trying things out before RQ1's files are here; ties at rank 20 may then differ slightly).

    python3 harness/retrieval.py --from-ollama                               # compute with bge-m3 here
    python3 harness/retrieval.py --from-lissa-cache path/to/cache-local-r2c  # use RQ1's saved vectors

Writes harness/data/candidates-<source>.json: {project: {requirement file: [[code file, cosine], ...]}}.
"""

import argparse
import json
import pathlib
import sys
import urllib.request

import numpy as np

import lissa_compat as lc

EMBEDDING = "bge-m3"
EMBEDDING_NUM_CTX = 8192  # input limit of bge-m3, as in the RQ1 configs
TOP_K = 20
RQ1_EMBEDDING_SEED_DIR = "{project}-133742243"  # folder of RQ1's saved vectors (first seed)


def embed_with_ollama(url, text):
    """Sends the same embedding request as LiSSA's OllamaEmbeddingCreator."""
    body = {
        "model": EMBEDDING,
        "input": text,
        "truncate": True,
        "options": {"num_ctx": EMBEDDING_NUM_CTX, "num_batch": EMBEDDING_NUM_CTX},
    }
    request = urllib.request.Request(
        url.rstrip("/") + "/api/embed", json.dumps(body).encode(), {"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        vector = json.loads(response.read())["embeddings"][0]
    # LiSSA reads each number with single precision
    return np.asarray(vector, dtype=np.float64).astype(np.float32)


def embeddings_from_lissa_cache(cache_dir, contents):
    """LiSSA saves each vector under the key of the file's text, as a list of numbers."""
    cache = lc.read_lissa_cache(pathlib.Path(cache_dir) / f"OllamaEmbeddingCreator_{EMBEDDING}.json")
    vectors = {}
    for name, content in contents.items():
        stored = cache.get(lc.generate_key(content))
        if stored is None:
            raise KeyError(f"{name}: no embedding in {cache_dir}")
        vectors[name] = np.asarray(json.loads(stored), dtype=np.float64).astype(np.float32)
    return vectors


def cosine_like_java(query, element):
    """Cosine similarity computed step by step as LiSSA computes it, with the same number precision,
    so that ranks and ties come out the same."""
    dot = np.cumsum((query * element).astype(np.float64))[-1]
    norm_q = np.cumsum(query.astype(np.float64) ** 2)[-1]
    norm_e = np.cumsum(element.astype(np.float64) ** 2)[-1]
    return np.float32(dot / (np.sqrt(norm_q) * np.sqrt(norm_e)))


def top_k(query, targets, k=TOP_K):
    """The k most similar code files in LiSSA's order: by similarity, ties in file-name order."""
    scored = [(name, cosine_like_java(query, vector)) for name, vector in targets.items()]
    scored.sort(key=lambda item: -item[1])  # equal scores keep their order, as in LiSSA
    return [(name, float(score)) for name, score in scored[:k]]


def candidates_for_project(project, source):
    requirements = lc.load_artifacts(lc.DATASETS / project / "UC")
    code = lc.load_artifacts(lc.DATASETS / project / "CC")
    if source["kind"] == "lissa-cache":
        cache_dir = pathlib.Path(source["path"]) / RQ1_EMBEDDING_SEED_DIR.format(project=project)
        req_vectors = embeddings_from_lissa_cache(cache_dir, requirements)
        code_vectors = embeddings_from_lissa_cache(cache_dir, code)
    else:
        req_vectors, code_vectors = {}, {}
        for group, contents in ((req_vectors, requirements), (code_vectors, code)):
            for name, content in contents.items():
                group[name] = embed_with_ollama(source["url"], content)
                print(f"  embedded {project}/{name}", file=sys.stderr, end="\r")
    return {name: top_k(vector, code_vectors) for name, vector in req_vectors.items()}


def recall_at_k(project, candidates):
    gold = lc.load_gold(project)
    retrieved = {(lc.link_id(req), lc.link_id(code)) for req, ranked in candidates.items() for code, _ in ranked}
    return len(retrieved & gold) / len(gold)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--from-ollama", action="store_true", help="compute the embeddings with bge-m3 here")
    group.add_argument("--from-lissa-cache", metavar="CACHE_ROOT", help="RQ1's cache-local-r2c folder")
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434")
    parser.add_argument("--out", help="output file (default: harness/data/candidates-<source>.json)")
    args = parser.parse_args()

    if args.from_lissa_cache:
        source = {"kind": "lissa-cache", "path": str(pathlib.Path(args.from_lissa_cache).resolve())}
        name = "rq1"
    else:
        source = {"kind": "ollama", "url": args.ollama_url}
        name = "local"
    result = {"embedding": EMBEDDING, "top_k": TOP_K, "source": source, "projects": {}}
    for project in lc.PROJECTS:
        result["projects"][project] = candidates_for_project(project, source)
        print(f"{project}: recall@{TOP_K} = {recall_at_k(project, result['projects'][project]):.3f}", file=sys.stderr)

    out = pathlib.Path(args.out) if args.out else lc.HARNESS / "data" / f"candidates-{name}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=1) + "\n")
    print(f"Wrote {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
