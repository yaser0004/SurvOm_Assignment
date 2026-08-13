"""Turn a list of CheckResults into one Decision, by explicit precedence.

Pure function, no I/O, no hidden scoring. Evaluated in this exact order,
first match wins - copied into the generated README so the criteria are
public (report.render_criteria_markdown draws on this module's docstring
and rules.py, not the other way around):

1. single_cell_or_spatial FAIL -> REJECT (cell-resolved assay)
2. disease_relevance FAIL -> REJECT (no NAFLD-spectrum term anywhere)
3. library_strategy FAIL -> REJECT (no expression-profiling samples)
4. expression_data_availability FAIL -> REJECT (no downloadable expression data)
5. any WARN -> MANUAL_REVIEW
6. all STRONG conditions met -> STRONG_CANDIDATE
7. otherwise -> CANDIDATE, with unmet_strong naming each gap

Non-human organisms never trigger 1-4; they fall through to 7 with
"organism != Homo sapiens" in unmet_strong. Whether a CANDIDATE gets
downloaded is a curation decision made by a human later, never something
this function encodes.
"""

from __future__ import annotations

from geo_screen.models import CheckResult, Decision, Status, Verdict

REJECT_PRECEDENCE = (
    ("single_cell_or_spatial", "cell-resolved assay; not bulk transcriptomics"),
    ("disease_relevance", "no NAFLD-spectrum term in series or sample metadata"),
    ("library_strategy", "no expression-profiling samples"),
    ("expression_data_availability", "no downloadable expression data"),
)

STRONG_CHECK_IDS = (
    "source_tissue",
    "library_strategy",
    "disease_relevance",
    "sample_count",
    "expression_data_availability",
)


def classify(checks: list[CheckResult]) -> Verdict:
    by_id = {c.id: c for c in checks}

    for check_id, reason in REJECT_PRECEDENCE:
        check = by_id.get(check_id)
        if check and check.status is Status.FAIL:
            return Verdict(Decision.REJECT, (f"{check_id}: {reason} ({check.observed})",), ())

    warns = [c for c in checks if c.status is Status.WARN]
    if warns:
        reasons = tuple(f"{c.id}: {c.observed}" for c in warns)
        return Verdict(Decision.MANUAL_REVIEW, reasons, ())

    organism = by_id.get("organism_consistency")
    is_human = (
        organism is not None
        and organism.status is Status.PASS
        and organism.observed.startswith("Homo sapiens")
    )

    strong_met = {"organism == Homo sapiens": is_human}
    for check_id in STRONG_CHECK_IDS:
        check = by_id.get(check_id)
        strong_met[check_id] = check is not None and check.status is Status.PASS

    if all(strong_met.values()):
        return Verdict(Decision.STRONG_CANDIDATE, (), ())

    unmet = []
    for label, met in strong_met.items():
        if met:
            continue
        if label == "organism == Homo sapiens":
            unmet.append("organism != Homo sapiens — model system, not equivalent to human NAFLD")
        else:
            unmet.append(f"{label} not PASS")
    return Verdict(Decision.CANDIDATE, (), tuple(unmet))
