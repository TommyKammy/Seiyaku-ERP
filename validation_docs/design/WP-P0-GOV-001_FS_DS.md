---
work_package_id: WP-P0-GOV-001
deliverable_id: DEL-WP-P0-GOV-001-01
requirement_ids:
  - URS-GOV-001
  - URS-GOV-002
design_ids:
  - DS-P0-GOV-001-FS
  - DS-P0-GOV-001-DS
document_status: draft
approval_status: not_requested
scope_decision_status: undecided
readiness: blocked
csv_impact: High
reviewers:
  business_owner: TBD
  qa_reviewer: TBD
  csv_reviewer: TBD
  it_owner: TBD
---

# WP-P0-GOV-001 FS/DS decision-input scaffold

> [!warning]
> This is an unapproved decision-input scaffold. It does not define or approve
> the intended use, GxP scope, system boundary, RACI, control design, or
> validation acceptance criteria. Every substantive decision remains TBD until
> the assigned Business Owner, QA Reviewer, CSV Reviewer, and IT Owner complete
> the required review.

## 1. Document control

| Field | Value |
|---|---|
| Work Package | WP-P0-GOV-001 |
| Deliverable | DEL-WP-P0-GOV-001-01 |
| Requirement IDs | URS-GOV-001, URS-GOV-002 |
| Design IDs | DS-P0-GOV-001-FS, DS-P0-GOV-001-DS |
| CSV impact | High |
| Vault status | draft |
| Operational readiness | blocked |
| Approval status | not_requested |
| Intended-use decision | undecided |
| GxP-scope decision | undecided |

### Required reviewers

| Role | Assigned reviewer | Review status |
|---|---|---|
| Business Owner | TBD | not_requested |
| QA Reviewer | TBD | not_requested |
| CSV Reviewer | TBD | not_requested |
| IT Owner | TBD | not_requested |

### Source references

- Canonical WP:
  10_開発計画_WBS/WP/WP-P0-GOV-001_意図する使用・GxP対象範囲マトリクス.md
- Roadmap: 10_開発計画_WBS/10.1_開発ロードマップ_正本.md
- Work Package ledger:
  10_開発計画_WBS/10.2_WorkPackage台帳_正本.md
- Dependency map: 10_開発計画_WBS/10.4_依存関係マップ.md
- GitHub parent Issue:
  <https://github.com/TommyKammy/Seiyaku-ERP/issues/3>

## 2. Purpose and boundary of this draft

This draft creates a stable review surface for the human decisions required by
WP-P0-GOV-001. It records questions, identifiers, matrix columns, and exit
criteria without answering the questions or classifying any system object.

### Included in this partial deliverable

- Document-control metadata using existing canonical IDs.
- Intended-use decision-input questions.
- An empty GxP Scope Matrix schema.
- Planned traceability identifiers and review gates.
- Explicit open decisions and incomplete Definition of Done.

### Excluded from this partial deliverable

- An approved intended-use statement.
- Any in-scope or out-of-scope GxP classification.
- System-boundary or RACI decisions owned by Issues #4 and #5.
- Frappe or ERPNext application code.
- DocType, Workflow, Role Permission, fixture, patch, database, API, or report
  implementation.
- Audit-trail, electronic-signature, reason-for-change, retention, or risk
  control design.
- Executed tests, generated Evidence, RTM approval, or acceptance claims.
- A change to the Work Package status, readiness, reviewer assignment, or
  closure state.

## 3. Intended-use decision inputs

All response and decision fields must remain TBD until reviewers are assigned
and the requirement and acceptance baselines are approved.

| Decision input | Response | Decision owner | Review status |
|---|---|---|---|
| Product/system name and controlled version | TBD | Business Owner / IT Owner | not_requested |
| Intended users and operating organization | TBD | Business Owner | not_requested |
| Supported business processes | TBD | Business Owner | not_requested |
| Intended operating environment | TBD | IT Owner | not_requested |
| Records, data, calculations, or decisions produced | TBD | Business Owner / QA Reviewer | not_requested |
| Regulatory or quality decisions that may rely on the system | TBD | QA Reviewer / CSV Reviewer | not_requested |
| Upstream and downstream systems and interfaces | TBD | IT Owner | not_requested |
| Data ownership and authoritative source | TBD | Business Owner / IT Owner | not_requested |
| Failure consequences and patient/product/data risk | TBD | QA Reviewer / CSV Reviewer | not_requested |
| Retention, archival, and retrieval expectations | TBD | QA Reviewer / IT Owner | not_requested |
| Explicitly excluded uses | TBD | Business Owner / QA Reviewer | not_requested |
| Proposed system boundary | TBD | IT Owner / CSV Reviewer | not_requested |

## 4. GxP Scope Matrix schema

No classified row is present in this draft. Rows may be added only after the
intended-use baseline, Issue #4 RACI, Issue #5 system boundary, decision owners,
and acceptance criteria are available for review.

| Item ID | Business process | Object / DocType / report | Intended use | Regulated record or data | GxP relevance | Scope decision | Rationale | Business owner | QA / CSV reviewer | Requirement / RTM reference | Approval Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|

Allowed values and decision rules for the matrix are also TBD. This scaffold
must not be interpreted as establishing a controlled vocabulary or a final
classification method.

## 5. Candidate objects requiring later assessment

The canonical WP names the following candidates. Their intended use and GxP
classification are deliberately not recorded here:

- System Inventory
- GxP Scope Matrix
- RACI
- Workflow candidate WP-P0-GOV-001-WF
- Report candidate WP-P0-GOV-001-RPT

Print Format and API remain N/A unless a later approved scope explicitly adds
them. Listing a candidate is not an in-scope determination.

## 6. FS decision questions

### 6.1 Functional boundary

- Which approved business processes are supported?
- Which activities remain manual or outside the system?
- Which object is the authoritative record for each approved process?
- Which reports, exports, notifications, or interfaces are required?
- Which lifecycle states and transitions are needed?

Decision: TBD.

### 6.2 Roles and approval

- Which role creates, reviews, approves, rejects, amends, or cancels a record?
- Which actions require segregation of duties?
- Which approval is a business approval, QA approval, or CSV approval?
- Which permissions are explicitly denied?

Decision: TBD. Issue #4 is the authoritative dependency for the RACI baseline.

### 6.3 System boundary

- Which applications, integrations, storage locations, and manual controls are
  inside the controlled boundary?
- Which system owns each master-data and transactional-data element?
- Which interface transfers regulated data?
- Which external services or infrastructure require supplier assessment?

Decision: TBD. Issue #5 is the authoritative dependency for the inventory and
boundary baseline.

## 7. DS decision questions

No implementation design is approved by this draft.

- DocType and field model: TBD.
- Workflow states, transitions, and guards: TBD.
- Role Permissions and segregation of duties: TBD.
- Audit trail and reason-for-change behavior: TBD.
- Electronic-signature applicability and semantics: TBD.
- Notification and report behavior: TBD.
- Data migration, patch, and fixture strategy: TBD.
- Integration and API behavior: TBD.
- Retention, archival, backup, and restore controls: TBD.
- Error handling and exception review: TBD.

## 8. Planned traceability inventory

The following IDs are copied from the canonical WP for planning. This section
does not assert that traceability relationships are approved, tests are
executed, Evidence exists, or RTM rows are complete.

### Requirements and design

- URS-GOV-001
- URS-GOV-002
- DS-P0-GOV-001-FS
- DS-P0-GOV-001-DS

### Planned Test Case IDs

- TC-P0-GOV-001-01-FUNC
- TC-P0-GOV-001-02-NEG
- TC-P0-GOV-001-03-AUTH
- TC-P0-GOV-001-04-AUDIT

Test status for every ID: NOT EXECUTED. Acceptance and expected results remain
unapproved.

### Planned Evidence IDs

- EVID-P0-GOV-001-01-SCREEN
- EVID-P0-GOV-001-01-DATA
- EVID-P0-GOV-001-01-LOG
- EVID-P0-GOV-001-01-RTM
- EVID-P0-GOV-001-02-SCREEN
- EVID-P0-GOV-001-02-DATA
- EVID-P0-GOV-001-02-LOG
- EVID-P0-GOV-001-02-RTM
- EVID-P0-GOV-001-03-SCREEN
- EVID-P0-GOV-001-03-AUTH
- EVID-P0-GOV-001-03-AUDIT
- EVID-P0-GOV-001-03-RTM
- EVID-P0-GOV-001-04-AUDIT
- EVID-P0-GOV-001-04-ESIG
- EVID-P0-GOV-001-04-APPROVAL
- EVID-P0-GOV-001-04-RTM

Evidence status for every ID: PLANNED ONLY. No execution Evidence or approval
record is created by this partial deliverable.

### Planned RTM rows

- RTM-P0-GOV-001-01
- RTM-P0-GOV-001-02
- RTM-P0-GOV-001-03
- RTM-P0-GOV-001-04

RTM status for every row: NOT UPDATED. The future baseline must cover the
Requirement, Fit/Gap, FS, DS, WP, Test Case, Evidence, and Approval columns.

## 9. Open decisions

| Decision | Required owner/reviewer | Status |
|---|---|---|
| Approve full URS-GOV-001 and URS-GOV-002 requirement text | Business Owner / QA Reviewer | TBD |
| Approve WP acceptance criteria and applicable test levels | QA Reviewer / CSV Reviewer | TBD |
| Assign named reviewers | Project governance | TBD |
| Approve intended-use statement | Business Owner / QA Reviewer | TBD |
| Approve GxP classification method and values | QA Reviewer / CSV Reviewer | TBD |
| Reconcile RACI from Issue #4 | Business Owner / QA Reviewer / IT Owner | TBD |
| Reconcile system inventory and boundary from Issue #5 | IT Owner / CSV Reviewer | TBD |
| Approve FS/DS baseline | QA Reviewer / CSV Reviewer / IT Owner | TBD |

## 10. Exit criteria for this draft state

This document can leave the decision-input state only when:

- URS-GOV-001 and URS-GOV-002 full text and acceptance criteria are approved.
- Named Business Owner, QA Reviewer, CSV Reviewer, and IT Owner are assigned.
- The intended-use statement is reviewed and approved.
- Issue #4 provides the approved RACI baseline.
- Issue #5 provides the approved inventory and system-boundary baseline.
- Scope-matrix rules and classifications are reviewed and approved.
- Applicable test levels and expected results are approved.
- RTM and Evidence handling are reviewed under the canonical conventions.

## 11. Incomplete Definition of Done

This partial deliverable satisfies only the creation of a reviewable
DEL-WP-P0-GOV-001-01 scaffold. The following remain incomplete:

- FS/DS content review and approval.
- GxP Scope Matrix population and approval.
- Fixture, patch, application, and configuration implementation.
- Test protocols, test execution, and accepted results.
- Evidence capture and Evidence review.
- RTM update and Approval fields.
- Resolution of Critical or High findings.
- QA, CSV, Business Owner, and IT Owner approvals.
- Readiness transition and downstream-work authorization.

The Work Package and Issue must remain draft/blocked and must not be closed by
this document-only change.
