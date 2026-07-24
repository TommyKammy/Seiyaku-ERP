"""Contract tests for the unapproved WP-P0-GOV-001 document scaffolds.

These tests verify repository-document state only. They do not execute a
validation protocol, inspect a runtime system, create Evidence, update the RTM,
or approve any Work Package decision.
"""

from __future__ import annotations

import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESIGN_PATH = ROOT / "validation_docs/design/WP-P0-GOV-001_FS_DS.md"
PLAN_PATH = ROOT / "validation_docs/test/TC-P0-GOV-001_PLAN.md"

REQUIREMENT_IDS = {"URS-GOV-001", "URS-GOV-002"}
DESIGN_IDS = {"DS-P0-GOV-001-FS", "DS-P0-GOV-001-DS"}
TEST_CASE_IDS = {
    "TC-P0-GOV-001-01-FUNC",
    "TC-P0-GOV-001-02-NEG",
    "TC-P0-GOV-001-03-AUTH",
    "TC-P0-GOV-001-04-AUDIT",
}
EVIDENCE_IDS = {
    "EVID-P0-GOV-001-01-SCREEN",
    "EVID-P0-GOV-001-01-DATA",
    "EVID-P0-GOV-001-01-LOG",
    "EVID-P0-GOV-001-01-RTM",
    "EVID-P0-GOV-001-02-SCREEN",
    "EVID-P0-GOV-001-02-DATA",
    "EVID-P0-GOV-001-02-LOG",
    "EVID-P0-GOV-001-02-RTM",
    "EVID-P0-GOV-001-03-SCREEN",
    "EVID-P0-GOV-001-03-AUTH",
    "EVID-P0-GOV-001-03-AUDIT",
    "EVID-P0-GOV-001-03-RTM",
    "EVID-P0-GOV-001-04-AUDIT",
    "EVID-P0-GOV-001-04-ESIG",
    "EVID-P0-GOV-001-04-APPROVAL",
    "EVID-P0-GOV-001-04-RTM",
}
RTM_ROW_IDS = {
    "RTM-P0-GOV-001-01",
    "RTM-P0-GOV-001-02",
    "RTM-P0-GOV-001-03",
    "RTM-P0-GOV-001-04",
}
RTM_TEST_CASE_IDS = {
    "RTM-P0-GOV-001-01": "TC-P0-GOV-001-01-FUNC",
    "RTM-P0-GOV-001-02": "TC-P0-GOV-001-02-NEG",
    "RTM-P0-GOV-001-03": "TC-P0-GOV-001-03-AUTH",
    "RTM-P0-GOV-001-04": "TC-P0-GOV-001-04-AUDIT",
}
EVIDENCE_TEST_CASE_IDS = {
    "EVID-P0-GOV-001-01-SCREEN": "TC-P0-GOV-001-01-FUNC",
    "EVID-P0-GOV-001-01-DATA": "TC-P0-GOV-001-01-FUNC",
    "EVID-P0-GOV-001-01-LOG": "TC-P0-GOV-001-01-FUNC",
    "EVID-P0-GOV-001-01-RTM": "TC-P0-GOV-001-01-FUNC",
    "EVID-P0-GOV-001-02-SCREEN": "TC-P0-GOV-001-02-NEG",
    "EVID-P0-GOV-001-02-DATA": "TC-P0-GOV-001-02-NEG",
    "EVID-P0-GOV-001-02-LOG": "TC-P0-GOV-001-02-NEG",
    "EVID-P0-GOV-001-02-RTM": "TC-P0-GOV-001-02-NEG",
    "EVID-P0-GOV-001-03-SCREEN": "TC-P0-GOV-001-03-AUTH",
    "EVID-P0-GOV-001-03-AUTH": "TC-P0-GOV-001-03-AUTH",
    "EVID-P0-GOV-001-03-AUDIT": "TC-P0-GOV-001-03-AUTH",
    "EVID-P0-GOV-001-03-RTM": "TC-P0-GOV-001-03-AUTH",
    "EVID-P0-GOV-001-04-AUDIT": "TC-P0-GOV-001-04-AUDIT",
    "EVID-P0-GOV-001-04-ESIG": "TC-P0-GOV-001-04-AUDIT",
    "EVID-P0-GOV-001-04-APPROVAL": "TC-P0-GOV-001-04-AUDIT",
    "EVID-P0-GOV-001-04-RTM": "TC-P0-GOV-001-04-AUDIT",
}
REVIEWER_STATES = {
    "Business Owner": ("TBD", "not_requested"),
    "QA Reviewer": ("TBD", "not_requested"),
    "CSV Reviewer": ("TBD", "not_requested"),
    "IT Owner": ("TBD", "not_requested"),
}
FRONTMATTER_REVIEWERS = {
    "business_owner": "TBD",
    "qa_reviewer": "TBD",
    "csv_reviewer": "TBD",
    "it_owner": "TBD",
}
INTENDED_USE_DECISION_INPUT_COUNT = 12
PROCEDURE_SECTION_ROW_COUNTS = {
    "## 7. TC-P0-GOV-001-01-FUNC planning schema": 13,
    "## 8. TC-P0-GOV-001-02-NEG planning schema": 13,
    "## 9. TC-P0-GOV-001-03-AUTH planning schema": 13,
    "## 10. TC-P0-GOV-001-04-AUDIT planning schema": 15,
}

REQUIREMENT_PATTERN = (
    r"\bURS-GOV-\d{3}(?:[-_][A-Za-z0-9]+)*\b"
)
DESIGN_PATTERN = r"\bDS-P0-GOV-001-[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*\b"
TEST_CASE_PATTERN = (
    r"\bTC-P0-GOV-001-\d{2}-[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*\b"
)
EVIDENCE_PATTERN = (
    r"\bEVID-P0-GOV-001-\d{2}-"
    r"[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*\b"
)
RTM_ROW_PATTERN = (
    r"\bRTM-P0-GOV-001-\d{2}(?:[-_][A-Za-z0-9]+)*\b"
)


def extract_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        raise AssertionError("design document must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise AssertionError("design document frontmatter is not terminated")
    return text[4:end]


def parse_unique_frontmatter_values(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in extract_frontmatter(text).splitlines():
        if not line or line[0].isspace():
            continue
        key, separator, value = line.partition(":")
        if not separator:
            continue
        if key in values:
            raise AssertionError(f"duplicate frontmatter key: {key}")
        values[key] = value.strip()
    return values


def parse_unique_frontmatter_mapping(text: str, parent_key: str) -> dict[str, str]:
    lines = extract_frontmatter(text).splitlines()
    parent = f"{parent_key}:"
    if lines.count(parent) != 1:
        raise AssertionError(f"frontmatter key must occur exactly once: {parent_key}")

    values: dict[str, str] = {}
    parent_index = lines.index(parent)
    for line in lines[parent_index + 1 :]:
        if not line or not line[0].isspace():
            break
        key, separator, value = line.strip().partition(":")
        if not separator:
            raise AssertionError(f"invalid nested frontmatter value: {line}")
        if key in values:
            raise AssertionError(f"duplicate nested frontmatter key: {key}")
        values[key] = value.strip()
    return values


def extract_section(text: str, heading: str) -> str:
    if text.splitlines().count(heading) != 1:
        raise AssertionError(f"section heading must occur exactly once: {heading}")
    marker = f"{heading}\n"
    start = text.find(marker)
    if start == -1:
        raise AssertionError(f"missing section: {heading}")
    content_start = start + len(marker)
    heading_level = len(heading) - len(heading.lstrip("#"))
    if heading_level == 0 or not heading.startswith(f"{'#' * heading_level} "):
        raise AssertionError(f"invalid Markdown heading: {heading}")
    next_heading = re.search(
        rf"(?m)^#{{1,{heading_level}}} ", text[content_start:]
    )
    if next_heading is None:
        return text[content_start:]
    return text[content_start : content_start + next_heading.start()]


def parse_unique_two_column_table(section: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in section.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 2 or cells[0] in {"Field", "---"}:
            continue
        key, value = cells
        if key in values:
            raise AssertionError(f"duplicate table key: {key}")
        values[key] = value
    return values


def parse_markdown_table(section: str) -> tuple[list[str], list[dict[str, str]]]:
    table_lines = [
        line.strip() for line in section.splitlines() if line.strip().startswith("|")
    ]
    if len(table_lines) < 2:
        raise AssertionError("section must contain a Markdown table")

    def cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip("|").split("|")]

    header = cells(table_lines[0])
    separator = cells(table_lines[1])
    if len(header) != len(separator) or not all(
        re.fullmatch(r":?-{3,}:?", cell) for cell in separator
    ):
        raise AssertionError("invalid Markdown table header")
    if len(set(header)) != len(header):
        raise AssertionError("duplicate Markdown table header")

    rows: list[dict[str, str]] = []
    for line in table_lines[2:]:
        row = cells(line)
        if len(row) != len(header):
            raise AssertionError("Markdown table row has an unexpected column count")
        rows.append(dict(zip(header, row, strict=True)))
    return header, rows


class WP001DocumentContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.design = DESIGN_PATH.read_text(encoding="utf-8")
        cls.plan = PLAN_PATH.read_text(encoding="utf-8")

    def test_design_remains_an_unapproved_blocked_decision_input(self) -> None:
        frontmatter = parse_unique_frontmatter_values(self.design)
        expected_frontmatter = {
            "work_package_id": "WP-P0-GOV-001",
            "deliverable_id": "DEL-WP-P0-GOV-001-01",
            "document_status": "draft",
            "approval_status": "not_requested",
            "scope_decision_status": "undecided",
            "readiness": "blocked",
            "csv_impact": "High",
        }
        for key, expected_value in expected_frontmatter.items():
            self.assertEqual(frontmatter.get(key), expected_value)

        document_control = extract_section(self.design, "## 1. Document control")
        document_control_values = parse_unique_two_column_table(document_control)
        expected_document_control = {
            "Vault status": "draft",
            "Operational readiness": "blocked",
            "Approval status": "not_requested",
            "Intended-use decision": "undecided",
            "GxP-scope decision": "undecided",
        }
        for key, expected_value in expected_document_control.items():
            self.assertEqual(document_control_values.get(key), expected_value)

        decision_inputs = extract_section(
            self.design, "## 3. Intended-use decision inputs"
        )
        decision_header, decision_rows = parse_markdown_table(decision_inputs)
        self.assertEqual(
            decision_header,
            ["Decision input", "Response", "Decision owner", "Review status"],
        )
        self.assertEqual(len(decision_rows), INTENDED_USE_DECISION_INPUT_COUNT)
        self.assertEqual(
            len({row["Decision input"] for row in decision_rows}),
            INTENDED_USE_DECISION_INPUT_COUNT,
        )
        self.assertEqual(
            Counter(
                (row["Response"], row["Review status"]) for row in decision_rows
            ),
            Counter(
                {("TBD", "not_requested"): INTENDED_USE_DECISION_INPUT_COUNT}
            ),
        )

        self.assertIn(
            "The Work Package and Issue must remain draft/blocked and must not be closed by\n"
            "this document-only change.",
            self.design,
        )
        self.assertIn("RTM status for every row: NOT UPDATED.", self.design)

    def test_design_contains_only_the_canonical_planned_identifiers(self) -> None:
        self.assertSetEqual(
            set(re.findall(REQUIREMENT_PATTERN, self.design)), REQUIREMENT_IDS
        )
        self.assertSetEqual(set(re.findall(DESIGN_PATTERN, self.design)), DESIGN_IDS)
        self.assertSetEqual(
            set(re.findall(TEST_CASE_PATTERN, self.design)), TEST_CASE_IDS
        )
        self.assertSetEqual(
            set(re.findall(EVIDENCE_PATTERN, self.design)), EVIDENCE_IDS
        )
        self.assertSetEqual(
            set(re.findall(RTM_ROW_PATTERN, self.design)), RTM_ROW_IDS
        )

    def test_design_scope_matrix_has_no_classified_rows(self) -> None:
        scope_matrix = extract_section(
            self.design, "## 4. GxP Scope Matrix schema"
        )
        header, rows = parse_markdown_table(scope_matrix)
        self.assertIn("Scope decision", header)
        self.assertIn("Approval Evidence", header)
        self.assertEqual(rows, [])

    def test_required_reviewers_remain_unassigned(self) -> None:
        self.assertEqual(
            parse_unique_frontmatter_mapping(self.design, "reviewers"),
            FRONTMATTER_REVIEWERS,
        )
        for document in (self.design, self.plan):
            reviewer_section = extract_section(document, "### Required reviewers")
            _, reviewer_rows = parse_markdown_table(reviewer_section)
            self.assertEqual(len(reviewer_rows), len(REVIEWER_STATES))
            actual_reviewer_states = {
                row["Role"]: (row["Assigned reviewer"], row["Review status"])
                for row in reviewer_rows
            }
            self.assertEqual(actual_reviewer_states, REVIEWER_STATES)

    def test_plan_remains_non_executable_and_unapproved(self) -> None:
        document_control = extract_section(self.plan, "## 1. Document control")
        document_control_values = parse_unique_two_column_table(document_control)
        expected_values = {
            "Work Package": "WP-P0-GOV-001",
            "Parent Issue": "#3",
            "Deliverable": "DEL-WP-P0-GOV-001-03",
            "Vault status": "draft",
            "Execution readiness": "blocked",
            "Protocol status": "not_requested",
            "Execution status": "not_executable",
            "Evidence status": "not_created",
            "RTM status": "not_updated",
        }
        for key, expected_value in expected_values.items():
            self.assertEqual(document_control_values.get(key), expected_value)
        self.assertIn(
            "Issue #3 and WP-P0-GOV-001 must remain open, draft, and blocked.",
            self.plan,
        )
        self.assertIn(
            "planning scaffold must not represent test execution, Validation, QA, CSV,\n"
            "Business, or IT approval.",
            self.plan,
        )

    def test_plan_procedure_schemas_remain_unapproved(self) -> None:
        for heading, expected_row_count in PROCEDURE_SECTION_ROW_COUNTS.items():
            with self.subTest(heading=heading):
                procedure = extract_section(self.plan, heading)
                header, rows = parse_markdown_table(procedure)
                self.assertEqual(
                    header,
                    ["Procedure field", "Planned content", "Status"],
                )
                self.assertEqual(len(rows), expected_row_count)
                self.assertEqual(
                    len({row["Procedure field"] for row in rows}),
                    expected_row_count,
                )
                self.assertEqual(
                    Counter(
                        (row["Planned content"], row["Status"]) for row in rows
                    ),
                    Counter({("TBD", "not_requested"): expected_row_count}),
                )

    def test_plan_canonical_inventory_has_one_entry_per_identifier(self) -> None:
        inventory = extract_section(
            self.plan, "## 6. Canonical Test Case inventory"
        )
        self.assertEqual(
            Counter(re.findall(TEST_CASE_PATTERN, inventory)),
            Counter({identifier: 1 for identifier in TEST_CASE_IDS}),
        )
        _, inventory_rows = parse_markdown_table(inventory)
        self.assertEqual(len(inventory_rows), len(TEST_CASE_IDS))
        actual_execution_states = {
            row["Planned Test Case ID"]: row["Execution status"]
            for row in inventory_rows
        }
        expected_execution_states = {
            identifier: "not_executable" for identifier in TEST_CASE_IDS
        }
        self.assertEqual(actual_execution_states, expected_execution_states)

        manifest = extract_section(self.plan, "## 11. Evidence manifest schema")
        self.assertEqual(
            Counter(re.findall(EVIDENCE_PATTERN, manifest)),
            Counter({identifier: 1 for identifier in EVIDENCE_IDS}),
        )
        _, manifest_rows = parse_markdown_table(manifest)
        self.assertEqual(len(manifest_rows), len(EVIDENCE_IDS))
        actual_evidence_states = {
            row["Planned Evidence ID"]: (row["Test Case ID"], row["Status"])
            for row in manifest_rows
        }
        expected_evidence_states = {
            identifier: (EVIDENCE_TEST_CASE_IDS[identifier], "not_created")
            for identifier in EVIDENCE_IDS
        }
        self.assertEqual(actual_evidence_states, expected_evidence_states)

        traceability = extract_section(self.plan, "## 12. Planned traceability")
        _, traceability_rows = parse_markdown_table(traceability)
        expected_traceability_states = {
            identifier: (
                RTM_TEST_CASE_IDS[identifier],
                "not_executed",
                "not_requested",
                "not_updated",
            )
            for identifier in RTM_ROW_IDS
        }
        self.assertEqual(len(traceability_rows), len(RTM_ROW_IDS))
        actual_traceability_states = {
            row["RTM row"]: (
                row["Test Case"],
                row["Execution"],
                row["Evidence review"],
                row["RTM update"],
            )
            for row in traceability_rows
        }
        self.assertEqual(
            actual_traceability_states,
            expected_traceability_states,
        )

    def test_plan_full_identifier_sets_match_the_design_contract(self) -> None:
        self.assertSetEqual(
            set(re.findall(REQUIREMENT_PATTERN, self.plan)), REQUIREMENT_IDS
        )
        self.assertSetEqual(set(re.findall(DESIGN_PATTERN, self.plan)), DESIGN_IDS)
        self.assertSetEqual(set(re.findall(TEST_CASE_PATTERN, self.plan)), TEST_CASE_IDS)
        self.assertSetEqual(set(re.findall(EVIDENCE_PATTERN, self.plan)), EVIDENCE_IDS)
        self.assertSetEqual(set(re.findall(RTM_ROW_PATTERN, self.plan)), RTM_ROW_IDS)


if __name__ == "__main__":
    unittest.main()
