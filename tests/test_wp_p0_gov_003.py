"""Contract tests for the unapproved WP-P0-GOV-003 document scaffolds.

These tests inspect repository-document state only. They do not register a
system, approve a boundary, classify GxP impact or data, execute a validation
protocol, create Evidence, update the RTM, or approve the Work Package.
"""

from __future__ import annotations

import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESIGN_PATH = ROOT / "validation_docs/design/WP-P0-GOV-003_FS_DS.md"
PLAN_PATH = ROOT / "validation_docs/test/TC-P0-GOV-003_PLAN.md"

REQUIREMENT_IDS = {"URS-GOV-001", "URS-GOV-002"}
DESIGN_IDS = {"DS-P0-GOV-003-FS", "DS-P0-GOV-003-DS"}
CASE_KINDS = {
    "01": "FUNC",
    "02": "NEG",
    "03": "AUTH",
    "04": "AUDIT",
}
EVIDENCE_SUFFIXES = {
    "01": ("SCREEN", "DATA", "LOG", "RTM"),
    "02": ("SCREEN", "DATA", "LOG", "RTM"),
    "03": ("SCREEN", "AUTH", "AUDIT", "RTM"),
    "04": ("AUDIT", "ESIG", "APPROVAL", "RTM"),
}
TEST_CASE_IDS = {
    f"TC-P0-GOV-003-{case_number}-{case_kind}"
    for case_number, case_kind in CASE_KINDS.items()
}
EVIDENCE_TEST_CASE_IDS = {
    f"EVID-P0-GOV-003-{case_number}-{suffix}": (
        f"TC-P0-GOV-003-{case_number}-{CASE_KINDS[case_number]}"
    )
    for case_number, suffixes in EVIDENCE_SUFFIXES.items()
    for suffix in suffixes
}
EVIDENCE_IDS = set(EVIDENCE_TEST_CASE_IDS)
RTM_TEST_CASE_IDS = {
    f"RTM-P0-GOV-003-{case_number}": (
        f"TC-P0-GOV-003-{case_number}-{case_kind}"
    )
    for case_number, case_kind in CASE_KINDS.items()
}
RTM_ROW_IDS = set(RTM_TEST_CASE_IDS)

DESIGN_REVIEWER_STATES = {
    "QA Reviewer": ("TBD", "not_requested"),
    "CSV Reviewer": ("TBD", "not_requested"),
    "IT Owner": ("TBD", "not_requested"),
}
PLAN_ROLE_STATES = {
    "QA Reviewer": ("TBD", "not_requested"),
    "CSV Reviewer": ("TBD", "not_requested"),
    "IT Owner": ("TBD", "not_requested"),
    "Test Executor": ("TBD", "not_assigned"),
    "Evidence Reviewer": ("TBD", "not_assigned"),
    "RTM Reviewer": ("TBD", "not_assigned"),
}
DESIGN_PLACEHOLDER_TABLES = {
    "## 4. System Inventory record schema": 1,
    "## 6. Logical-boundary register schema": 1,
    "## 7. Interface and dependency register schema": 1,
    "## 8. Data-flow and record-boundary schema": 1,
}
DECISION_TABLES = {
    "## 5. System-boundary decision dimensions": (
        10,
        ("Decision", "Rationale"),
    ),
    "## 9. Environment and configuration boundary": (
        8,
        ("Decision", "Evidence or source", "Owner"),
    ),
    "## 10. Fit/Gap decision inputs": (
        11,
        ("Fit/Gap conclusion", "Design reference"),
    ),
}
TARGET_OBJECTS = {
    "System Inventory",
    "GxP Scope Matrix",
    "RACI",
    "WP-P0-GOV-003-WF",
    "WP-P0-GOV-003-RPT",
    "Print Format",
    "API",
}
DISCOVERY_CATEGORIES = {
    "Frappe / ERPNext platform",
    "Governance application or configuration",
    "Validation document repository",
    "Source repository and CI",
    "Identity and access services",
    "Runtime and infrastructure",
    "External integrations",
    "Operational tooling",
}

REQUIREMENT_PATTERN = r"\bURS-GOV-\d{3}\b"
DESIGN_PATTERN = r"\bDS-P0-GOV-\d{3}-(?:FS|DS)\b"
TEST_CASE_PATTERN = r"\bTC-P0-GOV-\d{3}-\d{2}-(?:FUNC|NEG|AUTH|AUDIT)\b"
EVIDENCE_PATTERN = (
    r"\bEVID-P0-GOV-\d{3}-\d{2}-"
    r"(?:SCREEN|DATA|LOG|RTM|AUTH|AUDIT|ESIG|APPROVAL)\b"
)
RTM_ROW_PATTERN = r"\bRTM-P0-GOV-\d{3}-\d{2}\b"


def extract_section(text: str, heading: str) -> str:
    """Return one Markdown section, stopping before a peer/parent heading."""

    matches = list(re.finditer(rf"(?m)^{re.escape(heading)}[ \t]*$", text))
    if len(matches) != 1:
        raise AssertionError(
            f"expected one {heading!r} heading, found {len(matches)}"
        )

    level = len(heading) - len(heading.lstrip("#"))
    start = matches[0].end()
    next_heading = re.search(rf"(?m)^#{{1,{level}}} ", text[start:])
    end = start + next_heading.start() if next_heading else len(text)
    return text[start:end]


def parse_markdown_table(section: str) -> tuple[list[str], list[dict[str, str]]]:
    """Parse the first Markdown table in a section with unique column names."""

    lines = section.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith("|") or index + 1 >= len(lines):
            continue
        if not re.fullmatch(r"\|(?:\s*:?-+:?\s*\|)+", lines[index + 1]):
            continue

        header = [cell.strip() for cell in line.strip("|").split("|")]
        if len(set(header)) != len(header):
            raise AssertionError(f"duplicate table columns: {header}")

        rows: list[dict[str, str]] = []
        for row_line in lines[index + 2 :]:
            if not row_line.startswith("|"):
                break
            cells = [cell.strip() for cell in row_line.strip("|").split("|")]
            if len(cells) != len(header):
                raise AssertionError(
                    f"table row has {len(cells)} cells; expected {len(header)}"
                )
            rows.append(dict(zip(header, cells)))
        return header, rows

    raise AssertionError("section does not contain a Markdown table")


def parse_two_column_table(section: str) -> dict[str, str]:
    header, rows = parse_markdown_table(section)
    if len(header) != 2:
        raise AssertionError(f"expected two table columns, found {header}")

    result: dict[str, str] = {}
    for row in rows:
        key, value = (row[column] for column in header)
        if key in result:
            raise AssertionError(f"duplicate table key: {key}")
        result[key] = value
    return result


class WP003DocumentContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.design = DESIGN_PATH.read_text(encoding="utf-8")
        cls.plan = PLAN_PATH.read_text(encoding="utf-8")

    def assert_identifier_sets(self, text: str) -> None:
        self.assertSetEqual(
            set(re.findall(REQUIREMENT_PATTERN, text)), REQUIREMENT_IDS
        )
        self.assertSetEqual(set(re.findall(DESIGN_PATTERN, text)), DESIGN_IDS)
        self.assertSetEqual(
            set(re.findall(TEST_CASE_PATTERN, text)), TEST_CASE_IDS
        )
        self.assertSetEqual(
            set(re.findall(EVIDENCE_PATTERN, text)), EVIDENCE_IDS
        )
        self.assertSetEqual(
            set(re.findall(RTM_ROW_PATTERN, text)), RTM_ROW_IDS
        )

    def test_design_remains_a_blocked_unapproved_partial_deliverable(self) -> None:
        control = parse_two_column_table(
            extract_section(self.design, "## 1. Document control")
        )
        self.assertEqual(
            control,
            {
                "Work Package": "WP-P0-GOV-003",
                "Parent Issue": "#5",
                "Vault status": "draft",
                "Execution readiness": "blocked",
                "CSV impact": "High",
                "Partial deliverable": "DEL-WP-P0-GOV-003-01",
                "FS design ID": "DS-P0-GOV-003-FS",
                "DS design ID": "DS-P0-GOV-003-DS",
                "Approval state": "not_requested",
            },
        )
        self.assertIn(
            "does not register a system, establish a\nboundary, classify a "
            "component, approve a requirement, or authorize an\nimplementation",
            self.design,
        )

        header, rows = parse_markdown_table(
            extract_section(self.design, "### Required reviewers")
        )
        self.assertEqual(
            header, ["Role", "Assigned reviewer", "Review status"]
        )
        self.assertEqual(
            {
                row["Role"]: (
                    row["Assigned reviewer"],
                    row["Review status"],
                )
                for row in rows
            },
            DESIGN_REVIEWER_STATES,
        )
        self.assertEqual(len(rows), len(DESIGN_REVIEWER_STATES))

    def test_design_inventory_and_boundary_registers_remain_empty(self) -> None:
        for heading, expected_count in DESIGN_PLACEHOLDER_TABLES.items():
            with self.subTest(heading=heading):
                _, rows = parse_markdown_table(
                    extract_section(self.design, heading)
                )
                self.assertEqual(len(rows), expected_count)
                for row in rows:
                    self.assertEqual(row["Status"], "not_requested")
                    self.assertEqual(
                        {
                            value
                            for field, value in row.items()
                            if field != "Status"
                        },
                        {"TBD"},
                    )

        dimensions = extract_section(
            self.design, "## 5. System-boundary decision dimensions"
        )
        _, dimension_rows = parse_markdown_table(dimensions)
        self.assertEqual(len(dimension_rows), 10)
        self.assertEqual(
            {row["Dimension"] for row in dimension_rows},
            {
                "Functional",
                "Application",
                "Data",
                "Integration",
                "Infrastructure",
                "Identity and trust",
                "Organizational",
                "Lifecycle",
                "Geographic",
                "Temporal",
            },
        )

    def test_design_decisions_and_identifiers_remain_unapproved(self) -> None:
        for heading, (expected_count, placeholder_fields) in DECISION_TABLES.items():
            with self.subTest(heading=heading):
                _, rows = parse_markdown_table(
                    extract_section(self.design, heading)
                )
                self.assertEqual(len(rows), expected_count)
                for row in rows:
                    for field in placeholder_fields:
                        self.assertEqual(row[field], "TBD")
                    self.assertEqual(row["Status"], "not_requested")

        _, decision_rows = parse_markdown_table(
            extract_section(self.design, "## 14. Open decisions")
        )
        self.assertEqual(len(decision_rows), 11)
        self.assertEqual(
            Counter(row["Status"] for row in decision_rows),
            Counter({"TBD": 11}),
        )
        self.assert_identifier_sets(self.design)

    def test_plan_remains_non_executable_and_unapproved(self) -> None:
        control = parse_two_column_table(
            extract_section(self.plan, "## 1. Document control")
        )
        self.assertEqual(
            control,
            {
                "Document status": "draft",
                "Readiness": "blocked",
                "Approval state": "not_requested",
                "Execution status": "not_executable",
                "Work Package": "WP-P0-GOV-003",
                "GitHub Issue": "#5",
                "Phase": "P0",
                "Component": "validation_docs",
                "CSV impact": "High",
                "Requirements": "URS-GOV-001, URS-GOV-002",
                "Design": "DS-P0-GOV-003-FS, DS-P0-GOV-003-DS",
                "Partial deliverable": "DEL-WP-P0-GOV-003-03",
                "Canonical input reference": "POC-GOVERNANCE-001",
                "Evidence status": "not_created",
                "RTM status": "not_updated",
            },
        )
        self.assertIn(
            "All four Test Cases are `NOT RUN` and `blocked` in this scaffold.",
            self.plan,
        )
        self.assertIn(
            "does not register a system, establish or\napprove a system "
            "boundary, assign an owner, classify GxP impact or data",
            self.plan,
        )

        header, rows = parse_markdown_table(
            extract_section(
                self.plan, "### Required reviewers and execution roles"
            )
        )
        self.assertEqual(
            header, ["Role", "Assigned person", "Current status"]
        )
        self.assertEqual(
            {
                row["Role"]: (
                    row["Assigned person"],
                    row["Current status"],
                )
                for row in rows
            },
            PLAN_ROLE_STATES,
        )
        self.assertEqual(len(rows), len(PLAN_ROLE_STATES))

    def test_plan_readiness_and_candidate_inputs_remain_placeholders(self) -> None:
        header, readiness_rows = parse_markdown_table(
            extract_section(self.plan, "## 4. Execution-readiness gates")
        )
        self.assertEqual(
            header, ["Gate", "Required approved input", "Current state"]
        )
        self.assertEqual(
            {row["Gate"] for row in readiness_rows},
            {f"G{number:02d}" for number in range(1, 19)},
        )
        self.assertEqual(
            Counter(row["Current state"] for row in readiness_rows),
            Counter({"blocked": 18}),
        )

        _, target_rows = parse_markdown_table(
            extract_section(self.plan, "### Candidate target objects")
        )
        self.assertEqual(len(target_rows), len(TARGET_OBJECTS))
        self.assertEqual(
            {row["Candidate object"] for row in target_rows}, TARGET_OBJECTS
        )
        self.assertEqual(
            Counter(row["Approval state"] for row in target_rows),
            Counter({"TBD": 5, "N/A / TBD": 2}),
        )

        _, discovery_rows = parse_markdown_table(
            extract_section(self.plan, "### Candidate discovery categories")
        )
        self.assertEqual(len(discovery_rows), len(DISCOVERY_CATEGORIES))
        self.assertEqual(
            {row["Candidate category"] for row in discovery_rows},
            DISCOVERY_CATEGORIES,
        )

        boundary = extract_section(self.plan, "### Boundary partitions")
        self.assertIn(
            "remain unauthorized classifications until their meanings are "
            "approved",
            boundary,
        )

    def test_plan_procedure_models_do_not_claim_approved_results(self) -> None:
        procedure_headings = (
            "### TC-P0-GOV-003-01-FUNC — prospective normal-flow verification",
            "### TC-P0-GOV-003-02-NEG — prospective negative and "
            "consistency verification",
            "### TC-P0-GOV-003-03-AUTH — prospective "
            "authorization-boundary verification",
            "### TC-P0-GOV-003-04-AUDIT — prospective change and audit verification",
        )
        for heading in procedure_headings:
            with self.subTest(heading=heading):
                section = extract_section(self.plan, heading)
                self.assertRegex(
                    section,
                    r"(?i)(later-approved|approved versions|remain TBD|placeholder)",
                )

        _, authorization_rows = parse_markdown_table(
            extract_section(self.plan, procedure_headings[2])
        )
        self.assertEqual(len(authorization_rows), 8)
        for row in authorization_rows:
            for field in (
                "Authorized role",
                "Unauthorized role",
                "Expected denial point",
            ):
                self.assertIn(row[field], {"TBD", "N/A / TBD"})

    def test_plan_evidence_and_traceability_are_uncreated(self) -> None:
        manifest = extract_section(self.plan, "## 8. Evidence manifest")
        _, manifest_rows = parse_markdown_table(manifest)
        self.assertEqual(len(manifest_rows), len(EVIDENCE_IDS))
        self.assertEqual(
            {
                row["Evidence ID"]: row["Test Case"]
                for row in manifest_rows
            },
            EVIDENCE_TEST_CASE_IDS,
        )
        self.assertEqual(
            Counter(row["Status"] for row in manifest_rows),
            Counter({"not_created": len(EVIDENCE_IDS)}),
        )
        self.assertEqual(
            Counter(re.findall(EVIDENCE_PATTERN, manifest)),
            Counter({identifier: 1 for identifier in EVIDENCE_IDS}),
        )

        _, traceability_rows = parse_markdown_table(
            extract_section(self.plan, "## 9. Planned traceability")
        )
        self.assertEqual(len(traceability_rows), len(RTM_ROW_IDS))
        self.assertEqual(
            {
                row["RTM row"]: (
                    row["Requirement"],
                    row["Design"],
                    row["Test Case"],
                    row["Current state"],
                )
                for row in traceability_rows
            },
            {
                rtm_row: (
                    "URS-GOV-001, URS-GOV-002",
                    "DS-P0-GOV-003-FS, DS-P0-GOV-003-DS",
                    test_case,
                    "not_updated",
                )
                for rtm_row, test_case in RTM_TEST_CASE_IDS.items()
            },
        )

    def test_plan_contains_only_canonical_planned_identifiers(self) -> None:
        self.assert_identifier_sets(self.plan)


if __name__ == "__main__":
    unittest.main()
