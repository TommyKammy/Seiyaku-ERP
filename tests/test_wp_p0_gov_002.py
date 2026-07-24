"""Contract tests for the unapproved WP-P0-GOV-002 document scaffolds.

These tests inspect repository-document state only. They do not execute a
validation protocol, assign a responsibility, create Evidence, update the RTM,
or approve any Work Package decision.
"""

from __future__ import annotations

import re
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESIGN_PATH = ROOT / "validation_docs/design/WP-P0-GOV-002_FS_DS.md"
PLAN_PATH = ROOT / "validation_docs/test/TC-P0-GOV-002_PLAN.md"

REQUIREMENT_IDS = {"URS-GOV-001", "URS-GOV-002"}
DESIGN_IDS = {"DS-P0-GOV-002-FS", "DS-P0-GOV-002-DS"}
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
    f"TC-P0-GOV-002-{case_number}-{case_kind}"
    for case_number, case_kind in CASE_KINDS.items()
}
EVIDENCE_TEST_CASE_IDS = {
    f"EVID-P0-GOV-002-{case_number}-{suffix}": (
        f"TC-P0-GOV-002-{case_number}-{CASE_KINDS[case_number]}"
    )
    for case_number, suffixes in EVIDENCE_SUFFIXES.items()
    for suffix in suffixes
}
EVIDENCE_IDS = set(EVIDENCE_TEST_CASE_IDS)
RTM_TEST_CASE_IDS = {
    f"RTM-P0-GOV-002-{case_number}": (
        f"TC-P0-GOV-002-{case_number}-{case_kind}"
    )
    for case_number, case_kind in CASE_KINDS.items()
}
RTM_ROW_IDS = set(RTM_TEST_CASE_IDS)

REVIEWER_STATES = {
    "QA Reviewer": ("TBD", "not_requested"),
    "CSV Reviewer": ("TBD", "not_requested"),
    "IT Owner": ("TBD", "not_requested"),
}
READINESS_GATES = {
    "Requirements",
    "Acceptance",
    "Scope",
    "Role directory",
    "Activity inventory",
    "RACI semantics",
    "RACI matrix",
    "Segregation",
    "Delegation",
    "Design",
    "Test level",
    "Data",
    "Users",
    "Environment",
    "Evidence",
    "RTM",
    "Reviewers",
}
REPRESENTATIVE_INPUTS = {
    "Data-set identifier",
    "Version or checksum",
    "Data owner",
    "Approval reference",
    "Governed activity records",
    "Role-directory records",
    "RACI assignment records",
    "Invalid or prohibited combinations",
    "Delegation and effective-period records",
    "Expected-result source",
    "Reset or rollback method",
    "Personal or sensitive data assessment",
}
ORGANIZATIONAL_FUNCTIONS = {
    "Development",
    "Validation",
    "QA",
    "Business",
    "IT Operations",
}
ENVIRONMENT_ATTRIBUTES = {
    "Environment identifier",
    "Qualification or approval reference",
    "Application and framework version",
    "Configuration or fixture checksum",
    "Role Permission baseline",
    "Workflow baseline",
    "Time source and timezone",
    "Log and Audit Event source",
    "Electronic-signature configuration",
    "Cleanup or restoration method",
}
PROCEDURE_SECTION_ROW_COUNTS = {
    "## 7. TC-P0-GOV-002-01-FUNC planning schema": 15,
    "## 8. TC-P0-GOV-002-02-NEG planning schema": 14,
    "## 9. TC-P0-GOV-002-03-AUTH planning schema": 13,
    "## 10. TC-P0-GOV-002-04-AUDIT planning schema": 16,
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

    matches = list(
        re.finditer(rf"(?m)^{re.escape(heading)}[ \t]*$", text)
    )
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
        if not re.fullmatch(
            r"\|(?:\s*:?-+:?\s*\|)+", lines[index + 1]
        ):
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


class WP002DocumentContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.design = DESIGN_PATH.read_text(encoding="utf-8")
        cls.plan = PLAN_PATH.read_text(encoding="utf-8")

    def assert_reviewers_unassigned(self, text: str) -> None:
        reviewers = extract_section(text, "### Required reviewers")
        header, rows = parse_markdown_table(reviewers)
        self.assertEqual(
            header, ["Role", "Assigned reviewer", "Review status"]
        )
        self.assertEqual(len(rows), len(REVIEWER_STATES))
        self.assertEqual(
            {
                row["Role"]: (
                    row["Assigned reviewer"],
                    row["Review status"],
                )
                for row in rows
            },
            REVIEWER_STATES,
        )

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
        expected = {
            "Work Package": "WP-P0-GOV-002",
            "Parent Issue": "#4",
            "Vault status": "draft",
            "Execution readiness": "blocked",
            "CSV impact": "High",
            "Partial deliverable": "DEL-WP-P0-GOV-002-01",
            "FS design ID": "DS-P0-GOV-002-FS",
            "DS design ID": "DS-P0-GOV-002-DS",
            "Approval state": "not_requested",
        }
        self.assertEqual(control, expected)
        self.assertIn("Status: **DRAFT / BLOCKED / NOT APPROVED**", self.design)
        self.assertIn(
            "Merging this partial document must not close Issue #4 or represent "
            "Validation,\nQA, CSV, Business, or IT Operations approval.",
            self.design,
        )
        self.assert_reviewers_unassigned(self.design)

    def test_design_raci_semantics_and_assignments_remain_unapproved(self) -> None:
        semantics = extract_section(
            self.design, "## 3. Candidate RACI semantics"
        )
        header, rows = parse_markdown_table(semantics)
        self.assertEqual(
            header, ["Code", "Candidate meaning", "Approval question", "Status"]
        )
        self.assertEqual({row["Code"] for row in rows}, {"R", "A", "C", "I"})
        self.assertEqual(
            Counter(row["Status"] for row in rows), Counter({"TBD": 4})
        )

        role_directory = extract_section(
            self.design, "## 4. Role-directory schema"
        )
        _, role_rows = parse_markdown_table(role_directory)
        self.assertEqual(len(role_rows), 5)
        self.assertEqual(
            {row["Role group"] for row in role_rows},
            {"Development", "Validation", "QA", "Business", "IT Operations"},
        )
        for row in role_rows:
            for field in (
                "Named role/person",
                "Organization",
                "Decision authority",
                "Delegate/backup",
                "Effective period",
                "Approval reference",
            ):
                self.assertEqual(row[field], "TBD")
            self.assertEqual(row["Status"], "not_requested")

        activities = extract_section(
            self.design, "## 5. Candidate activity inventory"
        )
        _, activity_rows = parse_markdown_table(activities)
        self.assertEqual(len(activity_rows), 16)
        self.assertEqual(
            len({row["Candidate activity"] for row in activity_rows}), 16
        )
        self.assertEqual(
            Counter(
                (row["In scope?"], row["Status"]) for row in activity_rows
            ),
            Counter({("TBD", "not_requested"): 16}),
        )

        matrix = extract_section(self.design, "## 6. RACI matrix schema")
        _, matrix_rows = parse_markdown_table(matrix)
        self.assertEqual(len(matrix_rows), 1)
        matrix_row = matrix_rows[0]
        self.assertEqual(matrix_row["Approval status"], "not_requested")
        self.assertEqual(
            {value for key, value in matrix_row.items() if key != "Approval status"},
            {"TBD"},
        )

        segregation = extract_section(
            self.design, "## 7. Segregation-of-duties decision inputs"
        )
        _, segregation_rows = parse_markdown_table(segregation)
        self.assertEqual(len(segregation_rows), 10)
        self.assertEqual(
            Counter(row["Status"] for row in segregation_rows),
            Counter({"TBD": 10}),
        )

        open_decisions = extract_section(self.design, "## 11. Open decisions")
        _, decision_rows = parse_markdown_table(open_decisions)
        self.assertEqual(len(decision_rows), 10)
        self.assertEqual(
            Counter(row["Status"] for row in decision_rows),
            Counter({"TBD": 10}),
        )

    def test_design_contains_only_canonical_planned_identifiers(self) -> None:
        self.assert_identifier_sets(self.design)

    def test_plan_remains_non_executable_and_unapproved(self) -> None:
        control = parse_two_column_table(
            extract_section(self.plan, "## 1. Document control")
        )
        expected = {
            "Work Package": "WP-P0-GOV-002",
            "Parent Issue": "#4",
            "Deliverable": "DEL-WP-P0-GOV-002-03",
            "Requirements": "URS-GOV-001, URS-GOV-002",
            "Design references": "DS-P0-GOV-002-FS, DS-P0-GOV-002-DS",
            "CSV impact": "High",
            "Vault status": "draft",
            "Execution readiness": "blocked",
            "Protocol status": "not_requested",
            "Execution status": "not_executable",
            "Evidence status": "not_created",
            "RTM status": "not_updated",
        }
        self.assertEqual(control, expected)
        self.assertIn(
            "Issue #4 and WP-P0-GOV-002 must remain open, draft, and blocked.",
            self.plan,
        )
        self.assertIn(
            "scaffold is not Validation Evidence, QA/CSV approval, a "
            "responsibility\nassignment, or Work Package completion.",
            self.plan,
        )
        self.assert_reviewers_unassigned(self.plan)

    def test_plan_readiness_and_inputs_remain_placeholders(self) -> None:
        readiness = extract_section(
            self.plan, "## 4. Shared execution-readiness gate"
        )
        header, rows = parse_markdown_table(readiness)
        self.assertEqual(
            header,
            ["Gate", "Required input or decision", "Approval reference", "Status"],
        )
        self.assertEqual(len(rows), 17)
        self.assertEqual(
            Counter(
                (row["Approval reference"], row["Status"]) for row in rows
            ),
            Counter({("TBD", "not_requested"): 17}),
        )
        self.assertEqual({row["Gate"] for row in rows}, READINESS_GATES)

        placeholder_tables = {
            "### Representative data": (
                "Input attribute",
                REPRESENTATIVE_INPUTS,
                ("Planned value",),
            ),
            "### Candidate organizational functions": (
                "Candidate function",
                ORGANIZATIONAL_FUNCTIONS,
                ("Test identity", "Applicable Test Case", "Expected authorization"),
            ),
            "### Environment and configuration": (
                "Attribute",
                ENVIRONMENT_ATTRIBUTES,
                ("Planned value",),
            ),
        }
        for heading, (
            identifier_column,
            expected_identifiers,
            placeholder_columns,
        ) in placeholder_tables.items():
            with self.subTest(heading=heading):
                _, placeholder_rows = parse_markdown_table(
                    extract_section(self.plan, heading)
                )
                self.assertEqual(
                    len(placeholder_rows), len(expected_identifiers)
                )
                self.assertEqual(
                    {row[identifier_column] for row in placeholder_rows},
                    expected_identifiers,
                )
                for row in placeholder_rows:
                    for placeholder_column in placeholder_columns:
                        self.assertEqual(row[placeholder_column], "TBD")
                    self.assertEqual(row["Status"], "not_requested")

        semantics = extract_section(
            self.plan, "### Candidate RACI semantics"
        )
        _, semantics_rows = parse_markdown_table(semantics)
        self.assertEqual({row["Code"] for row in semantics_rows}, {"R", "A", "C", "I"})
        self.assertEqual(
            Counter(
                (row["Approved meaning"], row["Status"])
                for row in semantics_rows
            ),
            Counter({("TBD", "not_requested"): 4}),
        )

    def test_plan_procedure_schemas_remain_unapproved(self) -> None:
        for heading, expected_count in PROCEDURE_SECTION_ROW_COUNTS.items():
            with self.subTest(heading=heading):
                header, rows = parse_markdown_table(
                    extract_section(self.plan, heading)
                )
                self.assertEqual(
                    header, ["Procedure field", "Planned content", "Status"]
                )
                self.assertEqual(len(rows), expected_count)
                self.assertEqual(
                    len({row["Procedure field"] for row in rows}),
                    expected_count,
                )
                self.assertEqual(
                    Counter(
                        (row["Planned content"], row["Status"]) for row in rows
                    ),
                    Counter({("TBD", "not_requested"): expected_count}),
                )

    def test_plan_inventory_evidence_and_traceability_are_unexecuted(self) -> None:
        inventory = extract_section(
            self.plan, "## 6. Canonical Test Case inventory"
        )
        _, inventory_rows = parse_markdown_table(inventory)
        self.assertEqual(len(inventory_rows), len(TEST_CASE_IDS))
        self.assertEqual(
            {
                row["Canonical Test Case ID"]: row["Status"]
                for row in inventory_rows
            },
            {identifier: "not_executable" for identifier in TEST_CASE_IDS},
        )
        self.assertEqual(
            Counter(re.findall(TEST_CASE_PATTERN, inventory)),
            Counter({identifier: 1 for identifier in TEST_CASE_IDS}),
        )

        manifest = extract_section(
            self.plan, "## 11. Evidence manifest schema"
        )
        _, manifest_rows = parse_markdown_table(manifest)
        self.assertEqual(len(manifest_rows), len(EVIDENCE_IDS))
        actual_evidence_mapping = {
            row["Planned Evidence ID"]: row["Test Case ID"]
            for row in manifest_rows
        }
        self.assertEqual(actual_evidence_mapping, EVIDENCE_TEST_CASE_IDS)
        for row in manifest_rows:
            for field in (
                "Artifact type",
                "Producer",
                "Reviewer",
                "Retention",
                "Integrity reference",
            ):
                self.assertEqual(row[field], "TBD")
            self.assertEqual(row["Status"], "not_created")

        traceability = extract_section(
            self.plan, "## 12. Planned traceability"
        )
        _, traceability_rows = parse_markdown_table(traceability)
        self.assertEqual(len(traceability_rows), len(RTM_ROW_IDS))
        actual_traceability = {
            row["RTM row"]: (
                row["Test Case"],
                row["Execution"],
                row["Evidence review"],
                row["RTM update"],
            )
            for row in traceability_rows
        }
        expected_traceability = {
            rtm_row: (
                test_case,
                "not_executed",
                "not_requested",
                "not_updated",
            )
            for rtm_row, test_case in RTM_TEST_CASE_IDS.items()
        }
        self.assertEqual(actual_traceability, expected_traceability)

    def test_plan_contains_only_canonical_planned_identifiers(self) -> None:
        self.assert_identifier_sets(self.plan)


if __name__ == "__main__":
    unittest.main()
