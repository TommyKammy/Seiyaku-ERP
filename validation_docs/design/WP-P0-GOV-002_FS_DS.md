# WP-P0-GOV-002 FS/DS decision-input scaffold

> Status: **DRAFT / BLOCKED / NOT APPROVED**
>
> This document is a decision-input scaffold for Issue #4. It does not assign
> people, approve a RACI baseline, authorize implementation, or satisfy the
> Work Package acceptance criteria.

## 1. Document control

| Field | Value |
|---|---|
| Work Package | WP-P0-GOV-002 |
| Parent Issue | #4 |
| Vault status | draft |
| Execution readiness | blocked |
| CSV impact | High |
| Partial deliverable | DEL-WP-P0-GOV-002-01 |
| FS design ID | DS-P0-GOV-002-FS |
| DS design ID | DS-P0-GOV-002-DS |
| Approval state | not_requested |

Current blockers:

- The requirement text or acceptance criteria are not approved.
- QA Reviewer, CSV Reviewer, and IT Owner are not assigned.

### Required reviewers

| Role | Assigned reviewer | Review status |
|---|---|---|
| QA Reviewer | TBD | not_requested |
| CSV Reviewer | TBD | not_requested |
| IT Owner | TBD | not_requested |

### Source references

- GitHub Issue #4: WP-P0-GOV-002.
- URS-GOV-001 and URS-GOV-002 identifiers from the Issue/Vault source.
- Vault `10.2_WorkPackage台帳_正本`.
- Vault `10.4_依存関係マップ`.
- Vault `15.2_共通Definition_of_Done`.
- Issue #3 / WP-P0-GOV-001 intended-use and GxP-scope decision inputs.
- Issue #5 / WP-P0-GOV-003 system-inventory and system-boundary decision inputs.

Cross-Work-Package identifiers in this section are references only. This
document does not claim their deliverables or completion state.

## 2. Purpose and boundary of this draft

This partial deliverable provides a controlled place to collect the decisions
needed for the Development, Validation, QA, Business, and IT Operations RACI.
All assignments, approval authorities, segregation-of-duties controls, and
workflow permissions remain TBD until the named reviewers approve them.
This document does not create accounts, assign permissions, or grant authority.

### Included in this partial deliverable

- Candidate RACI terminology and decision questions.
- Empty role-directory and responsibility-matrix schemas.
- Candidate lifecycle activities requiring later scope confirmation.
- Questions for approval authority, delegation, escalation, and segregation of
  duties.
- Existing requirement, design, Test Case, Evidence, and RTM identifiers.
- Explicit review and exit gates for leaving the draft/blocked state.

### Excluded from this partial deliverable

- Named person assignments or approved organizational roles.
- An approved RACI matrix or responsibility baseline.
- Approval of URS-GOV-001, URS-GOV-002, or the Work Package acceptance
  criteria.
- Final intended-use, GxP-scope, or system-boundary decisions owned by Issues
  #3 and #5.
- Frappe or ERPNext application code.
- DocType, Workflow, Role Permission, fixture, patch, database, API, report, or
  notification implementation.
- Audit-trail, electronic-signature, reason-for-change, retention, or risk
  control design.
- Executed tests, generated Evidence, RTM approval, or acceptance claims.
- A change to the Work Package status, readiness, reviewer assignment, or
  closure state.

### Deferred Issue deliverables

The following Issue #4 deliverables are outside this partial change:

- DEL-WP-P0-GOV-002-02 — application, fixture, or patch implementation:
  NOT CREATED.
- DEL-WP-P0-GOV-002-03 — test protocol or OQ/UAT script: NOT CREATED.
- DEL-WP-P0-GOV-002-04 — executed Evidence package: NOT CREATED.
- DEL-WP-P0-GOV-002-05 — RTM update and review record: NOT UPDATED.

## 3. Candidate RACI semantics

The following meanings are decision inputs, not an approved project standard.
Reviewers must confirm or replace them before the matrix is populated.

| Code | Candidate meaning | Approval question | Status |
|---|---|---|---|
| R | Performs or coordinates the activity | May more than one role be Responsible? | TBD |
| A | Owns the outcome and approves completion | Must each activity have exactly one Accountable role? | TBD |
| C | Provides input before the decision or activity completes | Which consultations are mandatory and evidenced? | TBD |
| I | Receives information after a decision or activity milestone | Which notifications require retained proof? | TBD |

Questions that must be resolved:

- Whether every governed activity requires one and only one Accountable role.
- Whether a role may be both Responsible and Accountable for an activity.
- Which combinations require independent review or segregation of duties.
- Whether delegated or backup roles inherit accountability or only execution
  authority.
- What approval and recording rules apply to temporary assignments, absences,
  and emergency access.
- How conflicts between the RACI, SOPs, Workflow permissions, and actual
  organizational authority are resolved.

## 4. Role-directory schema

No person or approved role assignment is created by this table.

| Role group | Named role/person | Organization | Decision authority | Delegate/backup | Effective period | Approval reference | Status |
|---|---|---|---|---|---|---|---|
| Development | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |
| Validation | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |
| QA | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |
| Business | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |
| IT Operations | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |

Role-directory decisions:

- Canonical role names and organizational owners: TBD.
- Named reviewer and approver assignments: TBD.
- Minimum competence or training prerequisites: TBD.
- Delegate and backup rules: TBD.
- Effective dates and periodic-review interval: TBD.
- Joiner, mover, and leaver handling: TBD.

## 5. Candidate activity inventory

This list is a review checklist only. Inclusion in the approved RACI is TBD.

| Candidate activity | In scope? | Required decision output | Candidate stakeholders to consult | Status |
|---|---|---|---|---|
| Approve intended use and GxP scope | TBD | Approved scope baseline | Issue #3 reviewers | not_requested |
| Approve system inventory and boundary | TBD | Approved boundary baseline | Issue #5 reviewers | not_requested |
| Approve requirements and acceptance criteria | TBD | Approved requirement baseline | Business / QA / CSV | not_requested |
| Author and review FS/DS | TBD | Approved design baseline | Development / Validation / QA / CSV / IT Operations | not_requested |
| Configure or implement governed changes | TBD | Reviewed implementation record | Development / IT Operations | not_requested |
| Review source and configuration changes | TBD | Independent review record | Development / QA / CSV | not_requested |
| Plan and approve testing | TBD | Approved test protocol | Validation / QA / CSV / Business | not_requested |
| Execute and witness testing | TBD | Attributable execution record | Validation / Business / QA | not_requested |
| Review deviations and failed tests | TBD | Approved disposition | QA / CSV / Business / IT Operations | not_requested |
| Capture and review Evidence | TBD | Reviewed Evidence package | Validation / QA / CSV | not_requested |
| Update and approve RTM entries | TBD | Reviewed traceability record | Validation / QA / CSV | not_requested |
| Approve deployment or release readiness | TBD | Approved release decision | Business / QA / CSV / IT Operations | not_requested |
| Operate, monitor, and support the system | TBD | Controlled operation record | IT Operations / Business | not_requested |
| Approve controlled changes after release | TBD | Approved change record | Business / QA / CSV / IT Operations | not_requested |
| Review access and privileged activity | TBD | Periodic review record | IT Operations / QA / CSV | not_requested |
| Retire, archive, or migrate the system | TBD | Approved disposition record | Business / QA / CSV / IT Operations | not_requested |

## 6. RACI matrix schema

The matrix must remain unassigned until the role directory, activity scope, and
approval rules are reviewed. `TBD` means no responsibility has been granted.

| Activity ID | Activity | Development | Validation | QA | Business | IT Operations | Segregation constraint | Evidence/record | Approval status |
|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |

Matrix completion checks:

- Each activity has a stable identifier linked to a controlled source.
- Every R/A/C/I entry refers to an approved role-directory entry.
- Accountability cardinality is checked against the approved RACI semantics.
- Prohibited or incompatible role combinations are documented.
- The responsible role has the authority, competence, and system access needed
  for the activity.
- The accountable role can approve or reject the result without an unresolved
  conflict of interest.
- Required consultation and notification produce the approved retained record.
- Workflow and Role Permission implementation, if later authorized, matches the
  approved matrix.

## 7. Segregation-of-duties decision inputs

No segregation rule is approved by this draft.

| Decision area | Question | Required owner/reviewer | Status |
|---|---|---|---|
| Requirement baseline | May the author approve the same requirement? | Business / QA / CSV | TBD |
| Design baseline | May the author approve the same FS/DS? | QA / CSV / IT Operations | TBD |
| Implementation review | What independence is required from the implementer? | Development / QA / CSV | TBD |
| Test protocol | May the protocol author be its final approver? | Validation / QA / CSV | TBD |
| Test execution | Which executions require a witness or independent reviewer? | Validation / QA / CSV | TBD |
| Evidence review | May the executor approve the Evidence package? | QA / CSV | TBD |
| Deviation disposition | Which roles may propose, approve, and close a deviation? | QA / CSV / Business | TBD |
| Access administration | May a privileged administrator approve their own access? | IT Operations / QA / CSV | TBD |
| Deployment | May the implementer authorize production deployment? | Business / QA / CSV / IT Operations | TBD |
| Emergency change | Which temporary combinations are allowed and how are they reviewed? | Business / QA / CSV / IT Operations | TBD |

## 8. FS decision questions

No functional behavior is approved by this draft.

- What is the canonical governed activity inventory?
- What are the canonical role names and organizational owners?
- Which role is Responsible, Accountable, Consulted, and Informed for each
  approved activity?
- Which activities require Business, QA, CSV, or IT Operations approval?
- Which responsibilities require independence or a prohibited combination?
- What delegation, backup, escalation, and dispute-resolution rules apply?
- Which RACI changes require change control, re-review, and re-approval?
- Which records demonstrate consultation, notification, and approval?
- Which intended-use, GxP-scope, and system-boundary decisions from Issues #3
  and #5 constrain the matrix?

## 9. DS decision questions

No implementation design is approved by this draft.

- Storage model for the approved RACI baseline: TBD.
- DocType and field model: TBD.
- Candidate Workflow identifier from Issue #4: WP-P0-GOV-002-WF —
  NOT IMPLEMENTED.
- Candidate Report identifier from Issue #4: WP-P0-GOV-002-RPT —
  NOT IMPLEMENTED.
- Workflow states, transitions, guards, and approval authority: TBD.
- Role Permission mapping and enforcement: TBD.
- Segregation-of-duties validation behavior: TBD.
- Audit trail and reason-for-change behavior: TBD.
- Electronic-signature applicability and semantics: TBD.
- Delegation and effective-period enforcement: TBD.
- Notification, escalation, and report behavior: TBD.
- Fixture, patch, and migration strategy: TBD.
- Integration and API behavior: TBD.
- Retention, archival, backup, and restore controls: TBD.
- Error handling and exception review: TBD.

## 10. Planned traceability inventory

All items in this section are identifiers from Issue #4. They are not evidence
of approval, execution, or acceptance.

### Requirements and design

- Requirements: URS-GOV-001, URS-GOV-002.
- Design: DS-P0-GOV-002-FS, DS-P0-GOV-002-DS.

### Planned Test Case IDs

- TC-P0-GOV-002-01-FUNC — NOT EXECUTED.
- TC-P0-GOV-002-02-NEG — NOT EXECUTED.
- TC-P0-GOV-002-03-AUTH — NOT EXECUTED.
- TC-P0-GOV-002-04-AUDIT — NOT EXECUTED.

### Planned Evidence IDs

- EVID-P0-GOV-002-01-SCREEN, EVID-P0-GOV-002-01-DATA,
  EVID-P0-GOV-002-01-LOG, EVID-P0-GOV-002-01-RTM.
- EVID-P0-GOV-002-02-SCREEN, EVID-P0-GOV-002-02-DATA,
  EVID-P0-GOV-002-02-LOG, EVID-P0-GOV-002-02-RTM.
- EVID-P0-GOV-002-03-SCREEN, EVID-P0-GOV-002-03-AUTH,
  EVID-P0-GOV-002-03-AUDIT, EVID-P0-GOV-002-03-RTM.
- EVID-P0-GOV-002-04-AUDIT, EVID-P0-GOV-002-04-ESIG,
  EVID-P0-GOV-002-04-APPROVAL, EVID-P0-GOV-002-04-RTM.

Evidence status: PLANNED ONLY. No Evidence has been generated or reviewed.

### Planned RTM rows

- RTM-P0-GOV-002-01.
- RTM-P0-GOV-002-02.
- RTM-P0-GOV-002-03.
- RTM-P0-GOV-002-04.

RTM columns in scope for later controlled update: Requirement, Fit/Gap, FS, DS,
WP, Test Case, Evidence, and Approval.

RTM status: NOT UPDATED. This draft does not establish an approved requirement,
design, test, Evidence, or approval relationship.

## 11. Open decisions

| Decision | Required owner/reviewer | Status |
|---|---|---|
| Approve full URS-GOV-001 and URS-GOV-002 requirement text | Business / QA | TBD |
| Approve Work Package acceptance criteria and applicable test levels | QA / CSV | TBD |
| Assign QA Reviewer, CSV Reviewer, and IT Owner | TBD (governance owner must be identified) | TBD |
| Approve role-directory entries and authority | Business / QA / CSV / IT Operations | TBD |
| Approve RACI terminology and accountability cardinality | Business / QA / CSV | TBD |
| Approve governed activity inventory | Business / QA / CSV / IT Operations | TBD |
| Approve segregation-of-duties constraints | QA / CSV / IT Operations | TBD |
| Reconcile intended use and GxP scope from Issue #3 | Business / QA / CSV | TBD |
| Reconcile system inventory and boundary from Issue #5 | IT Operations / CSV | TBD |
| Approve FS/DS and RACI baseline | QA / CSV / IT Operations | TBD |

## 12. Exit criteria for this draft state

This document may leave draft/blocked status only when all applicable items are
complete and recorded:

- Full URS-GOV-001 and URS-GOV-002 text and acceptance criteria are approved.
- QA Reviewer, CSV Reviewer, and IT Owner are assigned.
- The role directory, activity inventory, RACI semantics, responsibility
  matrix, and segregation constraints are populated and reviewed.
- Issue #3 scope and Issue #5 boundary decisions are reconciled.
- Any Business, QA, CSV, and IT Operations approvals required by the approved
  matrix are recorded.
- Applicable FS/DS, Workflow, Role Permission, fixture, patch, test, Evidence,
  and RTM changes are separately authorized and reviewed.
- Critical and High findings are resolved.
- A controlled status/readiness change is approved outside this draft.

## 13. Incomplete Definition of Done

The following Work Package outcomes remain incomplete:

- Approved FS/DS and RACI baseline.
- Approved requirement and acceptance baseline.
- Named reviewers and approval records.
- Authorized application/configuration implementation.
- Reviewed fixture or patch, if applicable.
- Approved test protocol and applicable OQ/UAT/PQ scope.
- Executed FUNC, NEG, AUTH, and AUDIT tests.
- Reviewed Evidence package.
- Updated and approved RTM.
- Resolution of Critical and High findings.
- Satisfaction of the applicable common Definition of Done.
- Approval for downstream Work Packages to rely on the RACI.

Merging this partial document must not close Issue #4 or represent Validation,
QA, CSV, Business, or IT Operations approval.
