# WP-P0-GOV-002 unapproved RACI test-design scaffold

This document is a non-executable planning scaffold for the canonical
WP-P0-GOV-002 Test Case IDs. It does not approve a RACI meaning, role,
responsibility assignment, segregation rule, acceptance criterion, expected
result, test execution, Evidence package, RTM update, or Work Package status.

## 1. Document control

| Field | Value |
|---|---|
| Work Package | WP-P0-GOV-002 |
| Parent Issue | #4 |
| Deliverable | DEL-WP-P0-GOV-002-03 |
| Requirements | URS-GOV-001, URS-GOV-002 |
| Design references | DS-P0-GOV-002-FS, DS-P0-GOV-002-DS |
| CSV impact | High |
| Vault status | draft |
| Execution readiness | blocked |
| Protocol status | not_requested |
| Execution status | not_executable |
| Evidence status | not_created |
| RTM status | not_updated |

Current blockers:

- The requirement text and acceptance criteria are not approved.
- QA Reviewer, CSV Reviewer, and IT Owner are not assigned.
- The role directory, governed activity inventory, RACI semantics, matrix, and
  segregation-of-duties constraints are not approved.
- Intended-use and GxP-scope decisions from Issue #3 and system-boundary
  decisions from Issue #5 are not approved or reconciled.
- Applicable unit, integration, OQ, UAT, and PQ levels are TBD.

### Required reviewers

| Role | Assigned reviewer | Review status |
|---|---|---|
| QA Reviewer | TBD | not_requested |
| CSV Reviewer | TBD | not_requested |
| IT Owner | TBD | not_requested |

Business, Development, Validation, and IT Operations participation remains
TBD. Listing a function or role in this document does not assign a person,
authority, responsibility, or approval right.

## 2. Purpose and boundary

This partial deliverable makes the canonical RACI-oriented test, Evidence, and
RTM identifiers reviewable without deciding the RACI baseline that those tests
would later verify.

### Included

- A shared readiness gate for all four planned Test Case IDs.
- Placeholder data, role, environment, and configuration inputs.
- Candidate RACI-specific checks for normal, negative, authorization, and
  audit scenarios.
- A canonical Test Case to Evidence and RTM mapping.
- Review, deviation, and exit-decision questions.
- An explicit incomplete Definition of Done.

### Excluded

- Approval of URS-GOV-001, URS-GOV-002, acceptance criteria, FS, or DS.
- Approval or population of a role directory, activity inventory, RACI
  semantics, RACI matrix, or segregation-of-duties rule.
- Named person assignment, delegation, backup assignment, emergency access,
  permission grant, or approval authority.
- Final intended-use, GxP-scope, or system-boundary decisions.
- Implementation or configuration of a DocType, Workflow, Role Permission,
  Report, Print Format, Notification, Fixture, Patch, API, database, audit
  control, electronic signature, or runtime behavior.
- Selection of a validation environment or controlled data set.
- Test execution, result disposition, deviation closure, Evidence capture,
  Evidence review, or RTM update.
- WP approval, readiness transition, downstream authorization, or Issue #4
  closure.

### Deliverable status

| Deliverable | Canonical location | State after this change |
|---|---|---|
| DEL-WP-P0-GOV-002-01: FS/DS difference design | `validation_docs/design/WP-P0-GOV-002_FS_DS.md` | Existing decision input; not approved here |
| DEL-WP-P0-GOV-002-02: implementation PR / Fixture / Patch | `apps/governance/...` | Not implemented |
| DEL-WP-P0-GOV-002-03: test cases / OQ or UAT scripts | `validation_docs/test/TC-P0-GOV-002_*.md` | Partial planning scaffold only |
| DEL-WP-P0-GOV-002-04: execution Evidence | `validation_docs/evidence/WP-P0-GOV-002/` | Not created |
| DEL-WP-P0-GOV-002-05: RTM update / review record | `validation_docs/rtm/RTM_master.md` | Not updated |

The source names `apps/governance/fixtures/wp_p0_gov_002_*.json`,
`apps/governance/patches/wp_p0_gov_002_*.py`, and
`apps/governance/api/wp_p0_gov_002.py` as candidate locations. This document
does not create those paths or decide that a Fixture, Patch, or API is needed.

## 3. Source and scope references

- GitHub Issue #4 and the canonical WP-P0-GOV-002 Vault note.
- Existing `validation_docs/design/WP-P0-GOV-002_FS_DS.md`.
- Vault `10.2_WorkPackage台帳_正本`.
- Vault `10.4_依存関係マップ`.
- Vault `15.2_共通Definition_of_Done`.
- Issue #3 / WP-P0-GOV-001 intended-use and GxP-scope decision inputs.
- Issue #5 / WP-P0-GOV-003 system-inventory and system-boundary decision
  inputs.

WP-P0-GOV-002 has no prerequisite Work Package in the current dependency map.
Parallel drafting does not remove the blockers above and does not make this
test plan executable.

### Candidate target objects

The canonical source names the following candidates. Listing them does not
approve their implementation, RACI applicability, GxP classification, or test
scope:

- System Inventory.
- GxP Scope Matrix.
- RACI.
- Workflow candidate WP-P0-GOV-002-WF.
- Report candidate WP-P0-GOV-002-RPT.

Print Format and API remain N/A unless a later approved scope explicitly
requires them.

## 4. Shared execution-readiness gate

No planned Test Case may move from `not_executable` until every applicable gate
has an approved reference.

| Gate | Required input or decision | Approval reference | Status |
|---|---|---|---|
| Requirements | Approved URS-GOV-001 and URS-GOV-002 text | TBD | not_requested |
| Acceptance | Approved criterion and expected result for each Test Case | TBD | not_requested |
| Scope | Approved intended use, GxP scope, and system boundary | TBD | not_requested |
| Role directory | Approved role names, owners, definitions, and effective periods | TBD | not_requested |
| Activity inventory | Approved governed activities and lifecycle coverage | TBD | not_requested |
| RACI semantics | Approved R, A, C, and I meanings and cardinality rules | TBD | not_requested |
| RACI matrix | Approved assignments for each governed activity | TBD | not_requested |
| Segregation | Approved independence and prohibited-combination rules | TBD | not_requested |
| Delegation | Approved backup, temporary assignment, escalation, and emergency rules | TBD | not_requested |
| Design | Approved DS-P0-GOV-002-FS and DS-P0-GOV-002-DS baseline | TBD | not_requested |
| Test level | Approved unit/integration/OQ/UAT/PQ applicability | TBD | not_requested |
| Data | Approved test-data specification and provenance | TBD | not_requested |
| Users | Approved test identities, roles, and negative authorization matrix | TBD | not_requested |
| Environment | Qualified or otherwise approved environment and configuration | TBD | not_requested |
| Evidence | Approved capture, naming, storage, retention, and review method | TBD | not_requested |
| RTM | Approved traceability and Approval-column update method | TBD | not_requested |
| Reviewers | Assigned QA, CSV, and IT reviewers | TBD | not_requested |

## 5. Planned inputs

### Representative data

The canonical source requires representative PoC data but does not assign a
data-set identifier. The identifier therefore remains TBD; this document does
not invent, create, or approve one.

| Input attribute | Planned value | Status |
|---|---|---|
| Data-set identifier | TBD | not_requested |
| Version or checksum | TBD | not_requested |
| Data owner | TBD | not_requested |
| Approval reference | TBD | not_requested |
| Governed activity records | TBD | not_requested |
| Role-directory records | TBD | not_requested |
| RACI assignment records | TBD | not_requested |
| Invalid or prohibited combinations | TBD | not_requested |
| Delegation and effective-period records | TBD | not_requested |
| Expected-result source | TBD | not_requested |
| Reset or rollback method | TBD | not_requested |
| Personal or sensitive data assessment | TBD | not_requested |

### Candidate RACI semantics

These labels are references to the existing decision-input scaffold, not
approved meanings:

| Code | Candidate meaning | Approved meaning | Status |
|---|---|---|---|
| R | Performs or coordinates the activity | TBD | not_requested |
| A | Owns the outcome and approves completion | TBD | not_requested |
| C | Provides input before completion | TBD | not_requested |
| I | Receives information after a milestone | TBD | not_requested |

### Candidate organizational functions

No test user or authority is established here.

| Candidate function | Test identity | Applicable Test Case | Expected authorization | Status |
|---|---|---|---|---|
| Development | TBD | TBD | TBD | not_requested |
| Validation | TBD | TBD | TBD | not_requested |
| QA | TBD | TBD | TBD | not_requested |
| Business | TBD | TBD | TBD | not_requested |
| IT Operations | TBD | TBD | TBD | not_requested |

### Environment and configuration

| Attribute | Planned value | Status |
|---|---|---|
| Environment identifier | TBD | not_requested |
| Qualification or approval reference | TBD | not_requested |
| Application and framework version | TBD | not_requested |
| Configuration or fixture checksum | TBD | not_requested |
| Role Permission baseline | TBD | not_requested |
| Workflow baseline | TBD | not_requested |
| Time source and timezone | TBD | not_requested |
| Log and Audit Event source | TBD | not_requested |
| Electronic-signature configuration | TBD | not_requested |
| Cleanup or restoration method | TBD | not_requested |

## 6. Canonical Test Case inventory

The short acceptance-criterion labels and full Test Case IDs are kept
separate. None has an approved procedure or expected result.

| Acceptance label | Canonical Test Case ID | Planned perspective | Status |
|---|---|---|---|
| TC-P0-GOV-002-01 | TC-P0-GOV-002-01-FUNC | Prospective normal flow against a later-approved RACI baseline | not_executable |
| TC-P0-GOV-002-02 | TC-P0-GOV-002-02-NEG | Missing, invalid, duplicate, expired, or prohibited RACI data | not_executable |
| TC-P0-GOV-002-03 | TC-P0-GOV-002-03-AUTH | Unauthorized create, edit, approve, delete, export, or API operation | not_executable |
| TC-P0-GOV-002-04 | TC-P0-GOV-002-04-AUDIT | Reason for change, delegation, re-approval, signature, and traceability | not_executable |

## 7. TC-P0-GOV-002-01-FUNC planning schema

Canonical perspective: a representative normal flow that would use
later-approved RACI semantics, roles, activities, assignments, and target
configuration. None is approved by this document.

| Procedure field | Planned content | Status |
|---|---|---|
| Objective | TBD | not_requested |
| Preconditions | TBD | not_requested |
| Approved RACI baseline reference | TBD | not_requested |
| Authorized test role | TBD | not_requested |
| Input data and version | TBD | not_requested |
| Role-directory setup | TBD | not_requested |
| Governed activity setup | TBD | not_requested |
| RACI assignment setup | TBD | not_requested |
| Workflow or report setup | TBD | not_requested |
| Detailed steps | TBD | not_requested |
| Expected state and output | TBD | not_requested |
| Expected consultation or notification proof | TBD | not_requested |
| Audit expectation | TBD | not_requested |
| Pass/fail rule | TBD | not_requested |
| Cleanup | TBD | not_requested |

Planned Evidence location:
`validation_docs/evidence/WP-P0-GOV-002/TC-P0-GOV-002-01-FUNC/`.
No directory or Evidence is created by this change.

## 8. TC-P0-GOV-002-02-NEG planning schema

Canonical perspective: rejection or controlled hold for missing required
roles, invalid RACI codes, duplicate or conflicting assignments, absent
accountability, prohibited combinations, expired delegation, or invalid
state. The actual invalid-condition catalog and expected response remain TBD.

| Procedure field | Planned content | Status |
|---|---|---|
| Objective | TBD | not_requested |
| Preconditions | TBD | not_requested |
| Negative condition inventory | TBD | not_requested |
| Missing-role case | TBD | not_requested |
| Invalid-code case | TBD | not_requested |
| Cardinality-conflict case | TBD | not_requested |
| Segregation-conflict case | TBD | not_requested |
| Expired-delegation case | TBD | not_requested |
| Duplicate or stale record case | TBD | not_requested |
| Detailed steps | TBD | not_requested |
| Expected rejection or hold | TBD | not_requested |
| Expected message and Audit Event | TBD | not_requested |
| Pass/fail rule | TBD | not_requested |
| Cleanup | TBD | not_requested |

Planned Evidence location:
`validation_docs/evidence/WP-P0-GOV-002/TC-P0-GOV-002-02-NEG/`.
No directory or Evidence is created by this change.

## 9. TC-P0-GOV-002-03-AUTH planning schema

Canonical perspective: unauthorized creation, editing, approval, deletion,
export, cancellation, or API operation against a later-approved RACI baseline.
The role matrix, prohibited operations, and Audit Event contract remain TBD.

| Procedure field | Planned content | Status |
|---|---|---|
| Authorization matrix reference | TBD | not_requested |
| Segregation rule reference | TBD | not_requested |
| Prohibited operation inventory | TBD | not_requested |
| Unauthorized test identity | TBD | not_requested |
| Privileged or emergency identity | TBD | not_requested |
| Target record and state | TBD | not_requested |
| Detailed steps | TBD | not_requested |
| Expected denial point | TBD | not_requested |
| Expected user-facing message | TBD | not_requested |
| Expected Audit Event fields | TBD | not_requested |
| Expected absence of side effects | TBD | not_requested |
| Pass/fail rule | TBD | not_requested |
| Cleanup | TBD | not_requested |

Planned Evidence location:
`validation_docs/evidence/WP-P0-GOV-002/TC-P0-GOV-002-03-AUTH/`.
No account, permission, role assignment, authority, role-directory record, or
Evidence is created by this change.

## 10. TC-P0-GOV-002-04-AUDIT planning schema

Canonical perspective: controlled amendment of a later-approved RACI baseline,
including reason for change, delegation history, re-approval, applicable
electronic signature, post-signature locking, and RTM/Evidence linkage. The
applicable controls and expected values remain TBD.

| Procedure field | Planned content | Status |
|---|---|---|
| Approved baseline reference | TBD | not_requested |
| GxP-critical field inventory | TBD | not_requested |
| Change-control reference | TBD | not_requested |
| Amendment and reason | TBD | not_requested |
| Old/new value expectation | TBD | not_requested |
| Delegation or effective-period expectation | TBD | not_requested |
| Re-approval path | TBD | not_requested |
| Electronic-signature applicability | TBD | not_requested |
| Re-authentication and signature meaning | TBD | not_requested |
| Signature-target hash expectation | TBD | not_requested |
| Post-signature lock expectation | TBD | not_requested |
| Audit Event expectation | TBD | not_requested |
| RTM and Evidence update expectation | TBD | not_requested |
| Detailed steps | TBD | not_requested |
| Pass/fail rule | TBD | not_requested |
| Cleanup | TBD | not_requested |

Planned Evidence location:
`validation_docs/evidence/WP-P0-GOV-002/TC-P0-GOV-002-04-AUDIT/`.
No directory or Evidence is created by this change.

## 11. Evidence manifest schema

Every Evidence ID below remains planned only.

The canonical source names a common candidate attachment set: `README.md`,
input data, screen or report output, logs, an RTM diff, and a review record. It
names `RET-GXP-LIFECYCLE` as the source retention classification. These are
source references only: applicability, required format, approved storage and
retention controls, reviewer assignment, and integrity method remain TBD. This
document does not create an Evidence package or approve the retention
classification.

| Test Case ID | Planned Evidence ID | Artifact type | Producer | Reviewer | Retention | Integrity reference | Status |
|---|---|---|---|---|---|---|---|
| TC-P0-GOV-002-01-FUNC | EVID-P0-GOV-002-01-SCREEN | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-01-FUNC | EVID-P0-GOV-002-01-DATA | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-01-FUNC | EVID-P0-GOV-002-01-LOG | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-01-FUNC | EVID-P0-GOV-002-01-RTM | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-02-NEG | EVID-P0-GOV-002-02-SCREEN | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-02-NEG | EVID-P0-GOV-002-02-DATA | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-02-NEG | EVID-P0-GOV-002-02-LOG | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-02-NEG | EVID-P0-GOV-002-02-RTM | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-03-AUTH | EVID-P0-GOV-002-03-SCREEN | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-03-AUTH | EVID-P0-GOV-002-03-AUTH | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-03-AUTH | EVID-P0-GOV-002-03-AUDIT | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-03-AUTH | EVID-P0-GOV-002-03-RTM | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-04-AUDIT | EVID-P0-GOV-002-04-AUDIT | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-04-AUDIT | EVID-P0-GOV-002-04-ESIG | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-04-AUDIT | EVID-P0-GOV-002-04-APPROVAL | TBD | TBD | TBD | TBD | TBD | not_created |
| TC-P0-GOV-002-04-AUDIT | EVID-P0-GOV-002-04-RTM | TBD | TBD | TBD | TBD | TBD | not_created |

## 12. Planned traceability

No traceability relationship is approved or written to the RTM by this
document.

| Requirement | Design | Work Package | Test Case | RTM row | Execution | Evidence review | RTM update |
|---|---|---|---|---|---|---|---|
| URS-GOV-001 / URS-GOV-002 | DS-P0-GOV-002-FS / DS-P0-GOV-002-DS | WP-P0-GOV-002 | TC-P0-GOV-002-01-FUNC | RTM-P0-GOV-002-01 | not_executed | not_requested | not_updated |
| URS-GOV-001 / URS-GOV-002 | DS-P0-GOV-002-FS / DS-P0-GOV-002-DS | WP-P0-GOV-002 | TC-P0-GOV-002-02-NEG | RTM-P0-GOV-002-02 | not_executed | not_requested | not_updated |
| URS-GOV-001 / URS-GOV-002 | DS-P0-GOV-002-FS / DS-P0-GOV-002-DS | WP-P0-GOV-002 | TC-P0-GOV-002-03-AUTH | RTM-P0-GOV-002-03 | not_executed | not_requested | not_updated |
| URS-GOV-001 / URS-GOV-002 | DS-P0-GOV-002-FS / DS-P0-GOV-002-DS | WP-P0-GOV-002 | TC-P0-GOV-002-04-AUDIT | RTM-P0-GOV-002-04 | not_executed | not_requested | not_updated |

The planned RTM columns are Requirement, Fit/Gap, FS, DS, WP, Test Case,
Evidence, and Approval. `validation_docs/rtm/RTM_master.md` is not created or
updated by this change.

## 13. Review and approval questions

| Decision | Required owner or reviewer | Status |
|---|---|---|
| Approve full URS-GOV-001 and URS-GOV-002 text | Business / QA | TBD |
| Approve each acceptance criterion and expected result | Business / QA / CSV | TBD |
| Assign named reviewers and test participants | Project governance | TBD |
| Approve intended-use, GxP-scope, and system-boundary baselines | Business / QA / CSV / IT | TBD |
| Approve canonical role directory and activity inventory | Business / QA / CSV / IT | TBD |
| Approve RACI meanings, cardinality rules, and assignment matrix | Business / QA / CSV / IT | TBD |
| Approve segregation, delegation, backup, and emergency rules | Business / QA / CSV / IT | TBD |
| Approve test-data specification and provenance | Business / QA | TBD |
| Approve test level and protocol classification | QA / CSV | TBD |
| Approve authorization and negative-test matrix | QA / CSV / IT | TBD |
| Approve Evidence capture and retention method | QA / CSV / IT | TBD |
| Approve deviation and defect disposition process | QA / CSV | TBD |
| Approve RTM update and review method | QA / CSV | TBD |
| Authorize execution | QA / CSV / IT | TBD |

## 14. Deviation and result-disposition questions

No deviation, defect, result, or disposition record exists.

- What identifier and workflow apply to a test deviation?
- Who may pause, resume, repeat, invalidate, or accept a test run?
- How are pre-execution protocol changes distinguished from deviations?
- How are screenshots, logs, data extracts, and timestamps linked to one run?
- How is an invalid run preserved without being misrepresented as Evidence?
- Which failures are Critical or High, and who approves their disposition?
- When is regression, re-execution, impact assessment, or revalidation needed?
- How are RACI conflicts, authorization defects, deviations, Evidence, and RTM
  rows linked?

## 15. Exit criteria for this planning state

This scaffold can leave `not_executable` only when:

- Every shared readiness gate has an approved reference.
- Each procedure has approved inputs, steps, expected results, and pass/fail
  rules.
- Applicable test levels and execution order are approved.
- Test data, identities, roles, environment, and configuration are controlled.
- Evidence capture, integrity, retention, and review instructions are approved.
- Deviation and result-disposition instructions are approved.
- Named reviewers authorize execution under the applicable change control.

Execution must occur in a separate authorized activity. Editing this file or
merging its PR does not authorize execution.

## 16. Incomplete Definition of Done

The following items remain incomplete after this partial deliverable:

- Approved URS, acceptance criteria, FS, and DS.
- Approved intended-use, GxP-scope, and system-boundary baselines.
- Approved role directory, activity inventory, RACI semantics, RACI matrix,
  segregation constraints, delegation, and escalation rules.
- Named QA Reviewer, CSV Reviewer, IT Owner, and applicable Business,
  Development, Validation, and IT Operations participants.
- Authorized implementation or configuration changes.
- Approved detailed procedures, expected results, and pass/fail rules.
- Approved unit/integration/OQ/UAT/PQ applicability.
- Qualified or approved environment and controlled test data.
- Test execution and result disposition.
- Evidence capture, review, integrity verification, and retention.
- RTM and Approval-column update.
- Critical and High finding resolution.
- Controlled readiness transition and downstream authorization.

Issue #4 and WP-P0-GOV-002 must remain open, draft, and blocked. This planning
scaffold is not Validation Evidence, QA/CSV approval, a responsibility
assignment, or Work Package completion.
