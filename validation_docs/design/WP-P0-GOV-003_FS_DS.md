# WP-P0-GOV-003 FS/DS decision-input scaffold

This document is an unapproved decision-input for the System Inventory and
system-boundary Work Package. It does not register a system, establish a
boundary, classify a component, approve a requirement, or authorize an
implementation.

## 1. Document control

| Field | Value |
|---|---|
| Work Package | WP-P0-GOV-003 |
| Parent Issue | #5 |
| Vault status | draft |
| Execution readiness | blocked |
| CSV impact | High |
| Partial deliverable | DEL-WP-P0-GOV-003-01 |
| FS design ID | DS-P0-GOV-003-FS |
| DS design ID | DS-P0-GOV-003-DS |
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

- GitHub Issue #5: WP-P0-GOV-003.
- URS-GOV-001 and URS-GOV-002 identifiers from the Issue/Vault source.
- Vault `10.2_WorkPackage台帳_正本`.
- Vault `10.4_依存関係マップ`.
- Vault `15.2_共通Definition_of_Done`.
- Issue #3 / WP-P0-GOV-001 intended-use and GxP-scope decision inputs.
- Issue #4 / WP-P0-GOV-002 RACI decision inputs.

Cross-Work-Package identifiers in this section are references only. This
document does not claim their deliverables, approval, or completion state.

## 2. Purpose and boundary of this draft

The purpose of this partial deliverable is to provide reviewable schemas and
decision questions for an eventual controlled System Inventory and approved
system boundary. Every substantive value remains TBD until the named roles are
assigned and the governing requirements and acceptance criteria are approved.

### Included in this partial deliverable

- Status semantics that distinguish candidate, proposed, approved, and retired
  inventory records.
- An empty System Inventory record schema.
- Candidate categories to consider during inventory discovery.
- Empty logical-boundary, interface, and data-flow register schemas.
- FS and DS decision questions.
- Planned traceability identifiers copied from the Issue/Vault source.
- Exit criteria and incomplete Definition of Done.

### Excluded from this partial deliverable

- Registration or approval of any system, component, interface, environment,
  supplier, owner, authoritative data source, or GxP classification.
- Approval of URS-GOV-001, URS-GOV-002, acceptance criteria, FS, or DS.
- A validated system-of-record designation.
- A production, validation, test, development, network, trust, security, or
  organizational boundary decision.
- Role Permission, Workflow, Custom Field, Print Format, Notification, Data
  Import, Report, retention, or audit configuration.
- Frappe or ERPNext application code, framework modification, DocType, fixture,
  patch, database migration, API, integration, secret, or credential.
- Test execution, Evidence creation, RTM update, or approval record.

### Deferred Issue deliverables

| Deliverable | Canonical location | State in this change |
|---|---|---|
| DEL-WP-P0-GOV-003-01: FS/DS difference design | `validation_docs/design/WP-P0-GOV-003_FS_DS.md` | Partial decision-input only |
| DEL-WP-P0-GOV-003-02: implementation PR / Fixture / Patch | `apps/governance/...` | Not implemented |
| DEL-WP-P0-GOV-003-03: test cases / OQ or UAT scripts | `validation_docs/test/TC-P0-GOV-003_*.md` | Not created |
| DEL-WP-P0-GOV-003-04: execution Evidence | `validation_docs/evidence/WP-P0-GOV-003/` | Not created |
| DEL-WP-P0-GOV-003-05: RTM update / review record | `validation_docs/rtm/RTM_master.md` | Not created |

The Issue/Vault source names
`apps/governance/fixtures/wp_p0_gov_003_*.json` and
`apps/governance/patches/wp_p0_gov_003_*.py` as candidate implementation
locations. This partial deliverable neither creates those paths nor determines
that a Fixture or Patch is required.

## 3. Inventory governance semantics

These candidate semantics require approval before use.

| Candidate lifecycle term | Candidate meaning | Permitted assertion in this draft |
|---|---|---|
| candidate | Discovered item awaiting scope and ownership review | The item has been proposed for review only |
| proposed | Draft record has required decision inputs | No proposed record exists in this document |
| approved | Authorized inventory baseline | Prohibited until required approvals are recorded |
| rejected | Reviewed item excluded with rationale | No exclusion decision exists in this document |
| retired | Previously approved item removed from service | No retirement decision exists in this document |

Control questions:

- What controlled identifier and naming convention applies?
- Who may create, review, approve, reject, change, and retire a record?
- Which status transitions require QA, CSV, Business, or IT approval?
- What effective date, review interval, and change-control reference are
  mandatory?
- How are duplicate, superseded, orphaned, or expired records handled?
- Which fields are immutable after approval?
- What constitutes the approved inventory baseline?

## 4. System Inventory record schema

The row below is a placeholder schema, not an inventory registration.

| System ID | System name | Intended purpose | Lifecycle state | Business owner | IT owner | QA/CSV owner | GxP impact | Data classification | Environments | Supplier | Boundary reference | Approval reference | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |

Required inventory decisions:

- Canonical system and component granularity: TBD.
- Relationship between a system, application, module, service, repository,
  infrastructure resource, and document repository: TBD.
- Required ownership roles and segregation-of-duties constraints: TBD.
- GxP impact classification method and permitted values: TBD.
- Data classification and record-retention attributes: TBD.
- Supplier, version, support, and end-of-life attributes: TBD.
- Environment and deployment-instance representation: TBD.
- Periodic review and reconciliation process: TBD.
- Inventory export, exception report, and approval-record requirements: TBD.

### Candidate discovery categories

The following categories are prompts for discovery only. They do not place any
item inside or outside the approved boundary.

| Candidate category | Discovery question | Inclusion decision | Owner | Status |
|---|---|---|---|---|
| Frappe / ERPNext platform | Which platform capabilities are used or relied upon? | TBD | TBD | not_requested |
| Governance application or configuration | Which custom or configured governance capabilities exist? | TBD | TBD | not_requested |
| Source repository and CI | Which repositories and controls affect the governed baseline? | TBD | TBD | not_requested |
| Validation document repository | Which document store is authoritative for controlled records? | TBD | TBD | not_requested |
| Runtime and infrastructure | Which services, hosts, databases, queues, caches, and storage are relied upon? | TBD | TBD | not_requested |
| Identity and access services | Which identity, authentication, authorization, and privileged-access services apply? | TBD | TBD | not_requested |
| External integrations | Which upstream, downstream, or supplier-managed interfaces exist? | TBD | TBD | not_requested |
| Operational tooling | Which monitoring, backup, restore, logging, and support tools affect control effectiveness? | TBD | TBD | not_requested |

## 5. System-boundary decision dimensions

No boundary is established by this section.

| Dimension | Decision question | Decision | Rationale | Required reviewer | Status |
|---|---|---|---|---|---|
| Functional | Which intended functions are governed? | TBD | TBD | QA Reviewer / CSV Reviewer | not_requested |
| Application | Which applications, modules, and configurations are included? | TBD | TBD | IT Owner / CSV Reviewer | not_requested |
| Data | Which records, metadata, attachments, logs, and derived outputs are included? | TBD | TBD | QA Reviewer / IT Owner | not_requested |
| Integration | Which inbound and outbound interfaces cross the boundary? | TBD | TBD | IT Owner / CSV Reviewer | not_requested |
| Infrastructure | Which compute, database, storage, queue, cache, and network services are relied upon? | TBD | TBD | IT Owner | not_requested |
| Identity and trust | Which identity providers, service accounts, certificates, and trust zones apply? | TBD | TBD | IT Owner / QA Reviewer | not_requested |
| Organizational | Which teams, suppliers, and support responsibilities are included? | TBD | TBD | QA Reviewer / IT Owner | not_requested |
| Lifecycle | Which development, test, validation, production-like, archival, and retirement states apply? | TBD | TBD | CSV Reviewer / IT Owner | not_requested |
| Geographic | Which sites, regions, legal entities, and data locations apply? | TBD | TBD | QA Reviewer / IT Owner | not_requested |
| Temporal | Which effective dates, transition periods, and historical baselines apply? | TBD | TBD | QA Reviewer / CSV Reviewer | not_requested |

Boundary-control questions:

- What is explicitly in scope, out of scope, shared, or externally managed?
- Which excluded item can still affect a GxP record or control?
- Where does responsibility transfer at each boundary crossing?
- Which controls are inherited, shared, or supplied?
- Which boundary changes require impact assessment, revalidation, or
  re-approval?
- What authoritative diagram and register represent the approved boundary?
- How are discrepancies among inventory, configuration, architecture, RTM, and
  operational reality detected and resolved?

## 6. Logical-boundary register schema

The row below is a placeholder schema, not a boundary decision.

| Boundary item ID | Candidate item | Item type | Proposed disposition | Rationale | Control owner | GxP relevance | Source reference | Approval reference | Status |
|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |

Permitted disposition values and their semantics remain TBD. In particular,
this draft does not authorize `in_scope`, `out_of_scope`, `shared`, or
`external` as approved classifications.

## 7. Interface and dependency register schema

The row below is a placeholder schema, not an interface registration.

| Interface ID | Source | Destination | Direction | Purpose | Data or event | Protocol or mechanism | Frequency | Authentication | Failure handling | Record owner | Boundary crossing | GxP relevance | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |

Interface decisions:

- Authoritative producer and consumer: TBD.
- Data ownership and reconciliation responsibility: TBD.
- Message, file, API, event, and manual-transfer controls: TBD.
- Authentication, authorization, certificate, and secret ownership: TBD.
- Retry, timeout, idempotency, duplicate, ordering, and partial-failure rules:
  TBD.
- Audit, monitoring, alerting, exception review, and retention requirements:
  TBD.
- Supplier or external-service assurance and service-level expectations: TBD.

## 8. Data-flow and record-boundary schema

The row below is a placeholder schema, not a data-flow registration.

| Flow ID | Record or data class | Origin | Transformation | Destination | Authoritative source | Integrity control | Retention | Personal or sensitive data | GxP relevance | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | not_requested |

Data-boundary decisions:

- Canonical record and authoritative-source designations: TBD.
- Master, transactional, derived, audit, configuration, and attachment data
  classification: TBD.
- Data residency, backup, restore, archival, and disposal rules: TBD.
- Clock, timestamp, locale, and time-zone controls: TBD.
- Import, export, migration, reconciliation, and manual-correction controls:
  TBD.
- Electronic-record and electronic-signature applicability: TBD.

## 9. Environment and configuration boundary

No environment or configuration baseline is approved by this draft.

| Decision area | Question | Decision | Evidence or source | Owner | Status |
|---|---|---|---|---|---|
| Environment classes | Which environment types exist and what is each intended use? | TBD | TBD | TBD | not_requested |
| Instance identity | How is each deployed instance uniquely identified? | TBD | TBD | TBD | not_requested |
| Version baseline | Which application, framework, dependency, and configuration versions are controlled? | TBD | TBD | TBD | not_requested |
| Configuration scope | Which settings, fixtures, patches, environment variables, and feature flags are governed? | TBD | TBD | TBD | not_requested |
| Promotion | How is an approved baseline promoted between environments? | TBD | TBD | TBD | not_requested |
| Drift detection | How is unauthorized or unexplained drift detected and dispositioned? | TBD | TBD | TBD | not_requested |
| Backup and restore | Which components and records require verified backup and restore? | TBD | TBD | TBD | not_requested |
| Monitoring | Which health, security, audit, and business-control signals are monitored? | TBD | TBD | TBD | not_requested |

## 10. Fit/Gap decision inputs

The Issue/Vault source states that ERPNext standard is out of scope while the
conditions, GxP scope, and responsibility boundary for using Frappe/ERPNext must
be documented. This draft records no Fit/Gap conclusion.

| Candidate area | Decision question | Fit/Gap conclusion | Design reference | Status |
|---|---|---|---|---|
| System Inventory | Is a standard or configured record model suitable? | TBD | TBD | not_requested |
| GxP Scope Matrix | What controlled relationship to Issue #3 is required? | TBD | TBD | not_requested |
| RACI | What controlled relationship to Issue #4 is required? | TBD | TBD | not_requested |
| Role Permission | Which approved inventory or boundary operations require enforcement? | TBD | TBD | not_requested |
| Workflow | Are WP-P0-GOV-003-WF states and approvals required? | TBD | TBD | not_requested |
| Custom Field | Which approved attributes cannot be represented without extension? | TBD | TBD | not_requested |
| Notification | Which controlled events require notification or escalation? | TBD | TBD | not_requested |
| Data Import | Is controlled inventory import permitted and how is it reconciled? | TBD | TBD | not_requested |
| Report | Is WP-P0-GOV-003-RPT required for baseline, exception, or review reporting? | TBD | TBD | not_requested |
| Audit and reason for change | Which changes require immutable history and rationale? | TBD | TBD | not_requested |
| Electronic signature | Which approvals, if any, require an electronic signature? | TBD | TBD | not_requested |

WP-P0-GOV-003-WF and WP-P0-GOV-003-RPT are candidate identifiers copied from
the Issue/Vault source. Neither object is implemented or approved here.
Print Format and API are N/A in the current source unless a later approved
scope explicitly requires them.

## 11. FS decision questions

No functional behavior is approved by this draft.

- What is the authoritative purpose of the System Inventory?
- What qualifies as one system, component, instance, interface, and data flow?
- What is the approved scope and relationship to Issues #3 and #4?
- Which inventory fields are mandatory for each lifecycle state?
- Who may propose, review, approve, change, retire, and periodically review a
  record?
- Which inventory or boundary events require Workflow, notification,
  escalation, exception review, or report output?
- What duplicate, completeness, referential-integrity, and stale-record rules
  apply?
- Which changes require reason, impact assessment, re-approval, RTM update, or
  revalidation?
- Which audit, electronic-record, electronic-signature, and retention controls
  apply?
- Which normal, negative, authorization, and audit scenarios are approved?

## 12. DS decision questions

No implementation design is approved by this draft.

- Storage model for the approved inventory and boundary baseline: TBD.
- DocType and field model: TBD.
- Identifier, naming, uniqueness, and cardinality rules: TBD.
- Candidate Workflow WP-P0-GOV-003-WF states, transitions, guards, and
  approvers: TBD and NOT IMPLEMENTED.
- Candidate Report WP-P0-GOV-003-RPT columns, filters, exceptions, and access:
  TBD and NOT IMPLEMENTED.
- Role Permission and segregation-of-duties enforcement: TBD.
- Validation, duplicate detection, relationship integrity, and stale-record
  behavior: TBD.
- Audit trail, versioning, reason-for-change, and electronic-signature behavior:
  TBD.
- Interface, retry, idempotency, reconciliation, and error handling: TBD.
- Retention, archival, backup, restore, and deletion controls: TBD.
- Fixture, patch, migration, rollback, and baseline strategy: TBD.
- Monitoring, alerting, periodic review, and exception handling: TBD.
- Test-data, Evidence, and RTM linkage implementation: TBD.

## 13. Planned traceability inventory

These identifiers are planned references copied from the Issue/Vault source.
Listing them does not mean that the associated test was approved or executed,
that Evidence exists, or that the RTM was updated.

### Requirements and design

- Requirements: URS-GOV-001, URS-GOV-002.
- Design: DS-P0-GOV-003-FS, DS-P0-GOV-003-DS.

### Planned Test Case IDs

- TC-P0-GOV-003-01-FUNC.
- TC-P0-GOV-003-02-NEG.
- TC-P0-GOV-003-03-AUTH.
- TC-P0-GOV-003-04-AUDIT.

### Unapproved acceptance-criteria mapping

The Issue/Vault source states the following acceptance-criterion shorthand.
This table only maps those statements to their planned full Test Case IDs; it
does not approve an acceptance criterion or test protocol.

| Acceptance criterion | Planned Test Case ID | Unapproved criterion summary | Status |
|---|---|---|---|
| TC-P0-GOV-003-01 | TC-P0-GOV-003-01-FUNC | Representative normal flow, state, output, and notification behavior | TBD |
| TC-P0-GOV-003-02 | TC-P0-GOV-003-02-NEG | Missing, invalid, duplicate, cancellation, and return behavior | TBD |
| TC-P0-GOV-003-03 | TC-P0-GOV-003-03-AUTH | Unauthorized create, edit, approve, delete, and export behavior plus Audit Event | TBD |
| TC-P0-GOV-003-04 | TC-P0-GOV-003-04-AUDIT | Reason for change, re-approval, and RTM/Evidence-update behavior | TBD |

### Planned Evidence IDs

- EVID-P0-GOV-003-01-SCREEN.
- EVID-P0-GOV-003-01-DATA.
- EVID-P0-GOV-003-01-LOG.
- EVID-P0-GOV-003-01-RTM.
- EVID-P0-GOV-003-02-SCREEN.
- EVID-P0-GOV-003-02-DATA.
- EVID-P0-GOV-003-02-LOG.
- EVID-P0-GOV-003-02-RTM.
- EVID-P0-GOV-003-03-SCREEN.
- EVID-P0-GOV-003-03-AUTH.
- EVID-P0-GOV-003-03-AUDIT.
- EVID-P0-GOV-003-03-RTM.
- EVID-P0-GOV-003-04-AUDIT.
- EVID-P0-GOV-003-04-ESIG.
- EVID-P0-GOV-003-04-APPROVAL.
- EVID-P0-GOV-003-04-RTM.

### Planned RTM rows

- RTM-P0-GOV-003-01.
- RTM-P0-GOV-003-02.
- RTM-P0-GOV-003-03.
- RTM-P0-GOV-003-04.

The planned RTM columns are Requirement, Fit/Gap, FS, DS, WP, Test Case,
Evidence, and Approval. `validation_docs/rtm/RTM_master.md` is not created or
updated by this partial deliverable.

### Deferred test-input references

The Issue/Vault source names `POC-GOVERNANCE-001` as a representative PoC data
set and lists 製造作業者, QC Analyst, QA Reviewer, 倉庫担当, 経理担当, and
IT Admin as candidate test-user roles where applicable. This document does
not create or approve that data set, create a user, assign a role, grant a
permission, or decide which role is applicable. Test-data content, role
mapping, authorization expectations, and environment remain TBD.

## 14. Open decisions

| Decision | Required owner/reviewer | Status |
|---|---|---|
| Approve full URS-GOV-001 and URS-GOV-002 requirement text | Business Owner / QA Reviewer | TBD |
| Approve WP acceptance criteria and applicable test levels | QA Reviewer / CSV Reviewer | TBD |
| Assign named reviewers | Project governance | TBD |
| Approve inventory purpose, granularity, and record schema | QA Reviewer / CSV Reviewer / IT Owner | TBD |
| Approve system and component inventory baseline | QA Reviewer / CSV Reviewer / IT Owner | TBD |
| Approve functional, application, data, integration, infrastructure, trust, organizational, lifecycle, geographic, and temporal boundaries | QA Reviewer / CSV Reviewer / IT Owner | TBD |
| Reconcile intended-use and GxP scope with Issue #3 | Business Owner / QA Reviewer / CSV Reviewer | TBD |
| Reconcile accountability and ownership with Issue #4 | QA Reviewer / IT Owner | TBD |
| Approve interface, dependency, and authoritative-data-source registers | QA Reviewer / CSV Reviewer / IT Owner | TBD |
| Approve Fit/Gap conclusions and implementation scope | QA Reviewer / CSV Reviewer / IT Owner | TBD |
| Approve FS/DS baseline | QA Reviewer / CSV Reviewer / IT Owner | TBD |

## 15. Dependencies and execution constraints

The Vault dependency map states that WP-P0-GOV-003 has no prerequisite Work
Package and may run in parallel when the common ID, branch, and RTM rules are
followed. That scheduling statement does not approve this Work Package, remove
its blockers, or establish that Issues #3 and #4 are complete.

- Prerequisite Work Package: none in the current Vault dependency map.
- Related parallel decision inputs: Issue #3 / WP-P0-GOV-001 and Issue #4 /
  WP-P0-GOV-002.
- Required reconciliation: intended-use and GxP scope from Issue #3, and
  accountability and ownership from Issue #4.
- Current blockers: requirement or acceptance criteria not approved; QA
  Reviewer, CSV Reviewer, and IT Owner not assigned.
- Implementation constraint: no inventory value, boundary disposition, or
  runtime control may be inferred merely because parallel drafting is allowed.

## 16. Exit criteria for this draft state

This draft can leave `not_requested` only after:

- URS-GOV-001, URS-GOV-002, and the acceptance criteria are approved.
- QA Reviewer, CSV Reviewer, and IT Owner are assigned.
- The inventory semantics, record schema, boundary dimensions, and register
  schemas are reviewed.
- Approved inventory and boundary values are supplied by authorized owners.
- Issues #3 and #4 are reconciled without asserting their completion.
- Fit/Gap and implementation decisions are approved.
- FS and DS are reviewed and approved under the applicable change-control
  process.
- Applicable test levels, protocols, Evidence expectations, retention, and RTM
  updates are approved.

Only then may a separately authorized change implement or configure DocTypes,
Workflow, Report, Role Permission, fixtures, patches, database changes, APIs,
integrations, audit controls, or runtime behavior.

## 17. Incomplete Definition of Done

The following Work Package outcomes remain incomplete:

- Approved requirement, acceptance, inventory, boundary, FS, and DS baselines.
- Named reviewers and approval records.
- Approved System Inventory, GxP Scope Matrix, and RACI relationships.
- Authorized application or configuration implementation.
- Reviewed fixture or patch, if applicable.
- Approved test protocol and applicable OQ/UAT/PQ scope.
- Executed FUNC, NEG, AUTH, and AUDIT tests.
- Reviewed Evidence package.
- Updated and approved RTM.
- Resolution of Critical and High findings.
- Satisfaction of the applicable common Definition of Done.
- Approval for downstream Work Packages to rely on the inventory or boundary.

Merging this partial document must not close Issue #5 or represent system
registration, boundary approval, Validation, QA, CSV, Business, or IT approval.
