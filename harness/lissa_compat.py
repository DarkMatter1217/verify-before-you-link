"""Python versions of the parts of LiSSA (written in Java) that the harness needs.

The harness must send LiSSA's exact prompts (so the baseline is LiSSA's own prompt and RQ1's saved answers can be
looked up) and must score links exactly as LiSSA does. Each function names the LiSSA code it copies;
selftest.py and check_rq1.py compare the results with LiSSA's own files.
"""

import hashlib
import json
import pathlib
import re
import uuid

HARNESS = pathlib.Path(__file__).resolve().parent
ROOT = HARNESS.parent  # the repository folder
LISSA = ROOT / "LiSSA-RATLR-V2" / "lissa"
DATASETS = LISSA / "datasets" / "req2code"
PROJECTS = ("SMOS", "eTour_en", "iTrust")

# How LiSSA names the two artifact types in its prompt
SOURCE_TYPE = "requirement"
TARGET_TYPE = "source code"

# LiSSA's chain-of-thought prompt (REASON_WITH_NAME) with its system message, as in every requirements-to-code config
SYSTEM_MESSAGE = "Your job is to determine if there is a traceability link between two artifacts of a system."
COT_PROMPT = (
    "Below are two artifacts from the same software system. Is there a traceability link between (1) and (2)? "
    "Give your reasoning and then answer with 'yes' or 'no' enclosed in <trace> </trace>.\n"
    " (1) {source_type}: '''{source_content}''' \n (2) {target_type}: '''{target_content}''' "
)

# The Ollama settings of RQ1 (see ChatLanguageModelProvider.java); the seed is LiSSA's first seed
SEED = 133742243
NUM_CTX = 16384
NUM_PREDICT = 4096


# --- Artifacts -----------------------------------------------------------------------------------------------------


def read_artifact(path):
    """Reads a file as LiSSA does: as UTF-8, with Windows line endings ("\\r\\n") turned into "\\n".
    The bytes are decoded directly because Python's text mode would change other line endings too, which LiSSA does
    not. A byte-order mark at the start of a file is kept, as in LiSSA."""
    return path.read_bytes().decode("utf-8", errors="replace").replace("\r\n", "\n")


def load_artifacts(folder):
    """{file name: content}, sorted by file name, as LiSSA loads them."""
    files = sorted((p for p in pathlib.Path(folder).iterdir() if p.is_file()), key=lambda p: p.name)
    hidden = [p.name for p in files if p.name.startswith(".")]
    if hidden:
        # LiSSA would treat them as artifacts too; RQ1 refused to run with them, and so does the harness
        raise ValueError(f"hidden files in {folder}: {hidden}; delete them first")
    return {p.name: read_artifact(p) for p in files}


def link_id(file_name):
    """The ID LiSSA uses in trace links: the file name up to the first dot ("UC10E1.txt" -> "UC10E1")."""
    return file_name[: file_name.index(".")]


def load_gold(project):
    """The gold-standard links from answer.csv: one 'requirement,code' pair per line, no header."""
    lines = (DATASETS / project / "answer.csv").read_bytes().decode("utf-8").splitlines()
    return {tuple(line.split(",")[:2]) for line in lines if line}


# --- Prompts and cache keys ----------------------------------------------------------------------------------------


def fill(template, source_content, target_content, source_type=SOURCE_TYPE, target_type=TARGET_TYPE):
    """Puts the two artifacts into the prompt the same way, and in the same order, as LiSSA does."""
    return (
        template.replace("{source_type}", source_type)
        .replace("{source_content}", source_content)
        .replace("{target_type}", target_type)
        .replace("{target_content}", target_content)
    )


def messages_to_string(system, user):
    """The messages written out as text exactly as LiSSA's Java libraries print them.
    LiSSA computes the key under which it saves an answer from this text."""
    parts = [] if system is None else [f'SystemMessage {{ text = "{system}" }}']
    parts.append(f'UserMessage {{ name = null contents = [TextContent {{ text = "{user}" }}] }}')
    return "[" + ", ".join(parts) + "]"


def generate_key(text):
    """The key LiSSA saves an answer under: an ID computed from the text (as LiSSA's KeyGenerator does),
    after turning Windows line endings into "\\n"."""
    digest = hashlib.md5(text.replace("\r\n", "\n").encode("utf-8")).digest()
    return str(uuid.UUID(bytes=digest, version=3))


def message_key(system, user):
    return generate_key(messages_to_string(system, user))


# --- Answers -------------------------------------------------------------------------------------------------------

# Same matching as LiSSA's pattern: the tag must be on one line; upper and lower case count the same
_TRACE = re.compile(r"<trace>([^\n\r\u0085  ]*?)</trace>", re.IGNORECASE | re.ASCII)


def has_trace_tag(answer):
    return _TRACE.search(answer) is not None


def is_related_cot(answer):
    """LiSSA's rule: a link only if the first <trace>...</trace> on one line contains 'yes'.
    An answer without the tag counts as 'no'."""
    match = _TRACE.search(answer)
    return match is not None and "yes" in match.group().lower()


_LEADING_ANSWER = re.compile(r"\W*(yes|no)\b", re.IGNORECASE | re.ASCII)


def is_related_tolerant(answer):
    """Not LiSSA's rule: the <trace> answer if there is one, otherwise a 'yes' or 'no' at the start of
    the answer ("Yes, there is a traceability link ..."). Reported next to the strict rule, to separate what the model
    decided from whether it kept to the answer format."""
    if has_trace_tag(answer):
        return is_related_cot(answer)
    match = _LEADING_ANSWER.match(answer)
    return match is not None and match.group(1).lower() == "yes"


PARSERS = {"strict": is_related_cot, "tolerant": is_related_tolerant}


def lissa_cache_file(cache_dir, model, classifier="ReasoningClassifier"):
    """The file in which LiSSA saves a model's answers: '<classifier>_<model>.json', with ':' written as '__'."""
    return pathlib.Path(cache_dir) / f"{classifier}_{model}.json".replace(":", "__")


def read_lissa_cache(path):
    """A LiSSA answer file: {key: answer}. Answers are text; embeddings are lists of numbers stored as text."""
    return json.loads(pathlib.Path(path).read_bytes().decode("utf-8"))


# --- Metrics -------------------------------------------------------------------------------------------------------


def counts(predicted, gold):
    """True positives, false positives and false negatives, counted as LiSSA counts them."""
    tp = len(predicted & gold)
    return tp, len(predicted) - tp, len(gold) - tp


def scores(tp, fp, fn):
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0

    def f_beta(beta):
        denominator = beta**2 * precision + recall
        return (1 + beta**2) * precision * recall / denominator if denominator else 0.0

    return {"p": precision, "r": recall, "f1": f_beta(1), "f2": f_beta(2)}


def read_trace_links(path):
    """A LiSSA trace-link file: one 'requirement,code' pair per line, no header."""
    text = pathlib.Path(path).read_text(encoding="utf-8")
    return {tuple(line.split(",")) for line in text.splitlines() if line}


def model_tag(model):
    return model.removesuffix(":latest").replace(":", "-").replace("/", "-")
