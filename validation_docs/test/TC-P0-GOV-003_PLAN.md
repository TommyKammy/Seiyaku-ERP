# WP-P0-GOV-003 unapproved System Inventory and boundary test-design scaffold

This document is a non-executable planning scaffold for the four canonical
WP-P0-GOV-003 Test Case IDs. It does not register a system, establish or
approve a system boundary, assign an owner, classify GxP impact or data, approve
requirements or acceptance criteria, authorize an implementation, execute a
test, create Evidence, or update the RTM.

## 1. Document control

| Field | Value |
|---|---|
| Document status | draft |
| Readiness | blocked |
| Approval state | not_requested |
| Execution status | not_executable |
| Work Package | WP-P0-GOV-003 |
| GitHub Issue | #5 |
| Phase | P0 |
| Component | validation_docs |
| CSV impact | High |
| Requirements | URS-GOV-001, URS-GOV-002 |
| Design | DS-P0-GOV-003-FS, DS-P0-GOV-003-DS |
| Partial deliverable | DEL-WP-P0-GOV-003-03 |
| Canonical input reference | POC-GOVERNANCE-001 |
| Evidence status | not_created |
| RTM status | not_updated |

Current blockers:

- The requirement text and acceptance criteria are not approved.
- The intended use and GxP scope are not approved.
- QA Reviewer, CSV Reviewer, and IT Owner are not assigned.
- The System Inventory governance semantics, record granularity, ownership
  model, classifications, boundary dispositions, and approval workflow are not
  approved.
- Interface, data-flow, environment, configuration, and Fit/Gap decisions are
  not approved.
- Applicable unit, integration, OQ, UAT, and PQ levels are TBD.
- Detailed procedures, controlled input values, expected results, pass/fail
  rules, approved environment, and execution roles are TBD.

### Required reviewers and execution roles

| Role | Assigned person | Current status |
|---|---|---|
| QA Reviewer | TBD | not_requested |
| CSV Reviewer | TBD | not_requested |
| IT Owner | TBD | not_requested |
| Test Executor | TBD | not_assigned |
| Evidence Reviewer | TBD | not_assigned |
| RTM Reviewer | TBD | not_assigned |

Listing a function, role, or candidate operation in this document does not
assign a person, grant permission, establish segregation of duties, or authorize
test execution.

## 2. Purpose and boundary

The purpose of this partial deliverable is to make the future System Inventory
and system-boundary verification scope reviewable before implementation or test
execution. It converts the canonical Test Case, Evidence, and RTM identifiers
into prospective test designs while leaving every governance decision and
controlled value open for the named reviewers.

### Included

- Planning records for `TC-P0-GOV-003-01-FUNC`,
  `TC-P0-GOV-003-02-NEG`, `TC-P0-GOV-003-03-AUTH`, and
  `TC-P0-GOV-003-04-AUDIT`.
- Prospective checks for System Inventory, GxP Scope Matrix, RACI, the candidate
  workflow `WP-P0-GOV-003-WF`, and candidate report
  `WP-P0-GOV-003-RPT`.
- Review gates for inventory governance, logical boundary, interfaces,
  dependencies, data flows, records, environments, configuration, roles,
  Evidence, and RTM traceability.
- A manifest for the sixteen canonical Evidence IDs without creating evidence
  content or directories.
- Explicit separation between source-defined identifiers and unapproved
  implementation or validation decisions.

### Excluded

- Creating, approving, rejecting, changing, or retiring any inventory record.
- Deciding that a system, application, module, service, repository,
  infrastructure resource, identity service, integration, operational tool, or
  document store is inside or outside an approved boundary.
- Assigning Business, IT, QA/CSV, record, control, interface, data, or supplier
  ownership.
- Approving GxP impact, data classification, retention, electronic-record, or
  electronic-signature applicability.
- Selecting lifecycle status meanings, transition permissions, immutable
  fields, review intervals, or the approved inventory baseline.
- Implementing DocTypes, permissions, workflows, reports, fixtures, patches,
  APIs, runtime controls, migrations, integrations, or production changes.
- Creating test users, credentials, controlled data, Evidence, deviations,
  approvals, signatures, or RTM entries.
- Treating `POC-GOVERNANCE-001` as approved test data; the identifier is a
  canonical input reference only.

### Deliverable status

| Deliverable | Status in this change |
|---|---|
| DEL-WP-P0-GOV-003-01: FS/DS difference design | existing unapproved scaffold |
| DEL-WP-P0-GOV-003-02: implementation / Fixture / Patch | not_started |
| DEL-WP-P0-GOV-003-03: test case / OQ or UAT script | partial planning scaffold |
| DEL-WP-P0-GOV-003-04: execution Evidence | not_created |
| DEL-WP-P0-GOV-003-05: RTM update / review record | not_updated |

The source names candidate implementation paths under `apps/governance`, but
this document does not create those paths or decide that a Fixture, Patch, API,
Print Format, or runtime customization is required.

## 3. Source and scope references

- Vault Work Package `WP-P0-GOV-003`: System Inventory and system-boundary
  registration.
- GitHub Issue #5.
- `validation_docs/design/WP-P0-GOV-003_FS_DS.md`.
- Requirements `URS-GOV-001` and `URS-GOV-002`.
- Designs `DS-P0-GOV-003-FS` and `DS-P0-GOV-003-DS`.
- Canonical dataset reference `POC-GOVERNANCE-001`.
- Retention classification `RET-GXP-LIFECYCLE`.

This Work Package has no prerequisite WP and may be drafted in parallel with
WP-P0-GOV-001 and WP-P0-GOV-002. Parallel drafting does not remove the blockers
above, reconcile unresolved scope or RACI decisions, or make this plan
executable.

### Candidate target objects

The canonical source names the following candidates. Their appearance here is
not an implementation decision or confirmation that they exist.

| Candidate object | Prospective verification concern | Approval state |
|---|---|---|
| System Inventory | identifiers, intended purpose, lifecycle, ownership, scope, classification, environment, supplier, boundary and approval references | TBD |
| GxP Scope Matrix | traceable and approved GxP scope decisions | TBD |
| RACI | approved ownership, accountability, review and segregation of duties | TBD |
| WP-P0-GOV-003-WF | approved state transitions, approvals, returns and cancellations | TBD |
| WP-P0-GOV-003-RPT | approved inventory, exception and review views | TBD |
| Print Format | applicable only if a later-approved scope requires output | N/A / TBD |
| API | applicable only if a later-approved scope requires external or automated processing | N/A / TBD |

### Candidate discovery categories

These categories are test-partition prompts only. They do not put an item
inside or outside the approved boundary.

| Candidate category | Planned review question |
|---|---|
| Frappe / ERPNext platform | Which relied-on platform capabilities are represented and traceable? |
| Governance application or configuration | Which governed custom or configured capabilities are represented? |
| Source repository and CI | Which repositories and controls affect a later-approved baseline? |
| Validation document repository | Which controlled record store is authoritative? |
| Runtime and infrastructure | Which services, hosts, databases, queues, caches, networks, and storage are relied upon? |
| Identity and access services | Which identity, authentication, authorization, and privileged-access services apply? |
| External integrations | Which upstream, downstream, or supplier-managed interfaces exist? |
| Operational tooling | Which monitoring, backup, restore, logging, and support tools affect control effectiveness? |

### Candidate test-user functions

The canonical source lists Manufacturing Operator (`製造作業者`), QC Analyst,
QA Reviewer, Warehouse Operator (`倉庫担当`), Accounting User (`経理担当`), and
IT Admin as representative test-user functions when applicable. These labels
are coverage prompts only. The approved RACI and permission design must decide
which functions are applicable, map each function to a controlled test role,
and identify authorized and unauthorized operations before test execution.
This list does not assign a user, grant access, or approve a role name.

## 4. Execution-readiness gates

No test step below may be executed until every applicable gate is approved and
linked to a controlled review record.

| Gate | Required approved input | Current state |
|---|---|---|
| G01 | URS-GOV-001 and URS-GOV-002 text | blocked |
| G02 | acceptance criteria and pass/fail rules | blocked |
| G03 | intended use and GxP scope | blocked |
| G04 | approved QA, CSV, Business, IT, executor, and reviewer assignments | blocked |
| G05 | System Inventory identifier, granularity, field and lifecycle semantics | blocked |
| G06 | ownership, approval, segregation-of-duties and immutable-field rules | blocked |
| G07 | logical-boundary dimensions, permitted dispositions and rationales | blocked |
| G08 | interface, dependency, failure, reconciliation and supplier controls | blocked |
| G09 | record/data classifications, authoritative sources, integrity and retention controls | blocked |
| G10 | environment, version, configuration, promotion, drift, backup and monitoring boundary | blocked |
| G11 | Fit/Gap decision and approved FS/DS baseline | blocked |
| G12 | applicable test levels and detailed controlled procedures | blocked |
| G13 | approved environment, release/configuration baseline and rollback isolation | blocked |
| G14 | controlled `POC-GOVERNANCE-001` input values and expected outputs | blocked |
| G15 | authorized test users with approved least-privilege roles | blocked |
| G16 | Evidence repositories, naming, metadata, integrity and retention controls | blocked |
| G17 | RTM rows and review/update procedure | blocked |
| G18 | deviation handling, defect severity and exit criteria | blocked |

Readiness may change only through the applicable human review and approval
process. Completing this document or merging its PR does not satisfy a gate.

## 5. Prospective coverage model

### Inventory record fields

Future approved test data must identify expected results for, at minimum:

- System ID and controlled naming convention.
- System name and intended purpose.
- Lifecycle state and status.
- Business owner, IT owner, and QA/CSV owner.
- GxP impact and data classification.
- Environments and supplier.
- Boundary reference and approval reference.
- Effective date, review interval, change-control reference, version/support
  metadata, and retirement attributes when later approved as required.

No value for these fields is asserted by this document.

### Candidate lifecycle semantics

The FS/DS lists `candidate`, `proposed`, `approved`, `rejected`, and `retired`
as decision inputs. Their meanings, permitted transitions, approvers, required
reasons, and immutable fields require approval before testing. In particular,
this plan does not assert that an approved inventory baseline exists.

### Boundary partitions

Future procedures should partition approved examples across functional,
application, data, integration, infrastructure, identity/trust,
organizational, lifecycle, geographic, and temporal dimensions. For each item,
the controlled input must supply the later-approved disposition, rationale,
control owner, GxP relevance, source reference, approval reference, and
expected status.

The illustrative words `in_scope`, `out_of_scope`, `shared`, and `external`
remain unauthorized classifications until their meanings are approved.

### Interface and dependency partitions

Future controlled inputs should cover source, destination, direction, purpose,
data/event, protocol/mechanism, frequency, authentication, failure handling,
record owner, boundary crossing, GxP relevance, producer/consumer authority,
reconciliation, retry, timeout, idempotency, duplicate, ordering,
partial-failure, monitoring, alerting and retention expectations.

### Data-flow and record partitions

Future controlled inputs should cover record/data class, origin,
transformation, destination, authoritative source, integrity control,
retention, personal/sensitive data, GxP relevance, data residency, backup,
restore, archival, disposal, timestamp/locale controls, import, export,
migration, reconciliation and manual correction.

### Environment and configuration partitions

Future controlled inputs should cover environment classes and intended use,
instance identity, application/framework/dependency/configuration versions,
settings, fixtures, patches, environment variables, feature flags, promotion,
drift detection, backup/restore, monitoring and disposition of discrepancies.

## 6. Common prospective preconditions and result rules

### Preconditions

Every future executable Test Case must:

1. Reference the approved versions of all G01-G18 inputs that apply.
2. Identify the approved environment, build, configuration, data reset or
   isolation method, and execution timestamp.
3. Identify the executor and independent reviewer.
4. Identify the approved user/role, expected permissions and prohibited
   operations for each actor.
5. Version and checksum the controlled `POC-GOVERNANCE-001` input extract.
6. Define exact steps, expected field values, statuses, transitions,
   notifications, reports, logs and audit records.
7. Link the Test Case, Evidence IDs, requirement, design, WP and RTM row.
8. Define objective pass/fail rules before execution.

### Planned result classification

- `PASS`: every approved expected result is observed, Evidence is complete and
  integrity-checked, no unresolved Critical/High deviation exists, and the
  independent review is recorded.
- `FAIL`: any approved expected result is not observed, a prohibited operation
  succeeds, required Evidence is missing or compromised, or traceability is
  incomplete.
- `BLOCKED`: a gate or controlled prerequisite is missing, the environment or
  data does not match its approved baseline, or execution cannot proceed
  without making an unapproved decision.
- `NOT RUN`: the approved procedure has not been executed.

All four Test Cases are `NOT RUN` and `blocked` in this scaffold.

## 7. Planned Test Cases

### TC-P0-GOV-003-01-FUNC — prospective normal-flow verification

Objective: verify that a later-approved System Inventory and boundary workflow
handles the approved representative inputs and produces the exact approved
state, notification, report and traceability results.

Planned procedure outline:

1. Confirm the approved versions of requirements, acceptance criteria, FS/DS,
   workflow, report, permissions and `POC-GOVERNANCE-001`.
2. Load only the approved representative records into the approved isolated
   environment.
3. As each approved role, perform the approved create, review, return, revise,
   approve, reject, cancel or retire operations that apply.
4. Verify the exact inventory fields, ownership references, classifications,
   boundary references, statuses, effective dates and approval records.
5. Verify the approved boundary, interface, dependency, data-flow,
   environment/configuration and discrepancy representations.
6. Verify approved notifications, exception/review report outputs and any
   later-approved export.
7. Capture the four assigned Evidence items and reconcile the RTM row.

Expected-result placeholders:

- Only later-approved values and transitions are accepted.
- Required approvals and segregation of duties are enforced.
- The inventory, boundary registers, report and audit history agree with the
  approved expected results.
- Records and outputs are traceable to `RTM-P0-GOV-003-01`.

These placeholders are not executable expectations. Detailed input values and
expected outputs remain TBD pending approval.

### TC-P0-GOV-003-02-NEG — prospective negative and consistency verification

Objective: verify later-approved rejection or hold behavior without inventing
validation rules.

Candidate partitions to disposition during test review:

- Missing fields later approved as mandatory.
- Values outside later-approved domains or formats.
- Duplicate controlled identifiers or records.
- Invalid, skipped, or stale lifecycle transitions.
- Expired review, approval, supplier, support, or configuration references.
- Orphaned ownership, boundary, interface, dependency, data-flow, environment,
  configuration, Evidence or RTM references.
- Conflicting inventory, boundary, architecture, configuration, report, RTM or
  operational-state values.
- Unknown source/destination, missing authentication, duplicate or out-of-order
  transfers, timeouts, retries and partial failures.
- Unauthorized or unexplained configuration drift.
- Return or cancellation without a later-approved reason and route.

For each approved partition, the executable procedure must define the exact
input, expected rejection or hold point, user-visible result, persisted state,
audit/log result, cleanup and pass/fail rule. This scaffold does not assert
which candidates are invalid or what rejection behavior is required.

Traceability target: `RTM-P0-GOV-003-02`.

### TC-P0-GOV-003-03-AUTH — prospective authorization-boundary verification

Objective: verify that each later-approved unauthorized actor is denied the
specified operation and that the denial is recorded as required.

Candidate operation matrix:

| Operation | Authorized role | Unauthorized role | Expected denial point | Required audit fields |
|---|---|---|---|---|
| Create | TBD | TBD | TBD | user, role, operation, target, reason |
| Edit | TBD | TBD | TBD | user, role, operation, target, reason |
| Submit for review | TBD | TBD | TBD | user, role, operation, target, reason |
| Approve or reject | TBD | TBD | TBD | user, role, operation, target, reason |
| Return or cancel | TBD | TBD | TBD | user, role, operation, target, reason |
| Delete | TBD | TBD | TBD | user, role, operation, target, reason |
| View or export | TBD | TBD | TBD | user, role, operation, target, reason |
| API or automated operation | N/A / TBD | N/A / TBD | N/A / TBD | N/A / TBD |

No row grants or denies a permission. The approved RACI, role-permission model,
segregation-of-duties rules and API applicability must supply every value
before execution.

The future procedure must verify denial before prohibited persistence or
approval, absence of unintended side effects, the exact later-approved
user-facing response, and the required Audit Event. It must not use production
credentials or privileged access outside the approved test environment.

Traceability target: `RTM-P0-GOV-003-03`.

### TC-P0-GOV-003-04-AUDIT — prospective change and audit verification

Objective: verify the later-approved reason-for-change, reapproval, electronic
signature, post-signature lock and audit-review controls that are actually
applicable to the approved scope.

Candidate sequence for later approval:

1. Establish an approved record and its linked inventory/boundary baseline.
2. Request a change to a field later classified as GxP-important.
3. Verify capture of old value, new value, reason, user, timestamp, target
   record ID and related requirement.
4. Exercise the later-approved return, correction and reapproval path.
5. If electronic signature is approved as applicable, verify reauthentication,
   signature meaning, signed-object hash, signer identity and post-signature
   lock.
6. Verify the approved audit review, Evidence linkage and RTM update.

Applicability, exact fields, signature controls, locking behavior, reviewers and
expected results are TBD. This plan does not classify a field as GxP-important
or declare an electronic signature required.

Traceability target: `RTM-P0-GOV-003-04`.

## 8. Evidence manifest

The paths and identifiers below are reservations from the canonical source.
No directory or Evidence content is created by this scaffold.

| Test Case | Evidence ID | Planned content | Status |
|---|---|---|---|
| TC-P0-GOV-003-01-FUNC | EVID-P0-GOV-003-01-SCREEN | approved screen/report capture | not_created |
| TC-P0-GOV-003-01-FUNC | EVID-P0-GOV-003-01-DATA | controlled input and result data | not_created |
| TC-P0-GOV-003-01-FUNC | EVID-P0-GOV-003-01-LOG | execution and application logs | not_created |
| TC-P0-GOV-003-01-FUNC | EVID-P0-GOV-003-01-RTM | RTM diff and review record | not_created |
| TC-P0-GOV-003-02-NEG | EVID-P0-GOV-003-02-SCREEN | rejection/hold capture | not_created |
| TC-P0-GOV-003-02-NEG | EVID-P0-GOV-003-02-DATA | negative input and persisted-state data | not_created |
| TC-P0-GOV-003-02-NEG | EVID-P0-GOV-003-02-LOG | validation and exception logs | not_created |
| TC-P0-GOV-003-02-NEG | EVID-P0-GOV-003-02-RTM | RTM diff and review record | not_created |
| TC-P0-GOV-003-03-AUTH | EVID-P0-GOV-003-03-SCREEN | denial capture | not_created |
| TC-P0-GOV-003-03-AUTH | EVID-P0-GOV-003-03-AUTH | approved permission matrix and results | not_created |
| TC-P0-GOV-003-03-AUTH | EVID-P0-GOV-003-03-AUDIT | authorization-denial audit records | not_created |
| TC-P0-GOV-003-03-AUTH | EVID-P0-GOV-003-03-RTM | RTM diff and review record | not_created |
| TC-P0-GOV-003-04-AUDIT | EVID-P0-GOV-003-04-AUDIT | change and audit records | not_created |
| TC-P0-GOV-003-04-AUDIT | EVID-P0-GOV-003-04-ESIG | applicable electronic-signature records | not_created |
| TC-P0-GOV-003-04-AUDIT | EVID-P0-GOV-003-04-APPROVAL | return/reapproval review records | not_created |
| TC-P0-GOV-003-04-AUDIT | EVID-P0-GOV-003-04-RTM | RTM diff and review record | not_created |

Planned canonical folder pattern:

- `validation_docs/evidence/WP-P0-GOV-003/TC-P0-GOV-003-01-FUNC/`
- `validation_docs/evidence/WP-P0-GOV-003/TC-P0-GOV-003-02-NEG/`
- `validation_docs/evidence/WP-P0-GOV-003/TC-P0-GOV-003-03-AUTH/`
- `validation_docs/evidence/WP-P0-GOV-003/TC-P0-GOV-003-04-AUDIT/`

Each future Evidence package must include `README.md`, controlled input data,
screen or report captures, logs, the RTM diff and a review record as applicable.
The approved procedure must define provenance, timestamps, hashes or equivalent
integrity controls, reviewer, disposition and `RET-GXP-LIFECYCLE` retention.

## 9. Planned traceability

| RTM row | Requirement | Design | Test Case | Evidence set | Current state |
|---|---|---|---|---|---|
| RTM-P0-GOV-003-01 | URS-GOV-001, URS-GOV-002 | DS-P0-GOV-003-FS, DS-P0-GOV-003-DS | TC-P0-GOV-003-01-FUNC | EVID-P0-GOV-003-01-* | not_updated |
| RTM-P0-GOV-003-02 | URS-GOV-001, URS-GOV-002 | DS-P0-GOV-003-FS, DS-P0-GOV-003-DS | TC-P0-GOV-003-02-NEG | EVID-P0-GOV-003-02-* | not_updated |
| RTM-P0-GOV-003-03 | URS-GOV-001, URS-GOV-002 | DS-P0-GOV-003-FS, DS-P0-GOV-003-DS | TC-P0-GOV-003-03-AUTH | EVID-P0-GOV-003-03-* | not_updated |
| RTM-P0-GOV-003-04 | URS-GOV-001, URS-GOV-002 | DS-P0-GOV-003-FS, DS-P0-GOV-003-DS | TC-P0-GOV-003-04-AUDIT | EVID-P0-GOV-003-04-* | not_updated |

This is a planned mapping only. It does not modify
`validation_docs/rtm/RTM_master.md`, attest coverage, or approve any
requirement, design, Test Case, Evidence, result or RTM row.

## 10. Review questions before executable authoring

Reviewers must resolve at least:

1. What is the approved intended use and GxP boundary?
2. What constitutes a system versus an application, component, service,
   repository, infrastructure resource or document store?
3. Which inventory fields, lifecycle statuses, transitions and approvals are
   required, and which fields become immutable?
4. What roles own, create, review, approve, reject, change and retire records?
5. What boundary dimensions and disposition vocabulary are approved?
6. Which interfaces, dependencies, records, data flows, environments,
   configurations, suppliers and inherited controls are in scope?
7. How are duplicates, superseded, orphaned, expired, inconsistent or drifting
   items detected and dispositioned?
8. Which functions can Frappe/ERPNext support by configuration and which gaps
   need later-approved custom controls?
9. Which test levels apply, and what controlled inputs, exact steps, expected
   results and pass/fail rules are required?
10. Which audit, reason-for-change, electronic-signature, reapproval, lock,
    Evidence integrity, retention and RTM controls apply?

Answers must be approved in their controlled source. Editing this scaffold is
not a substitute for approval.

## 11. Deviation and defect handling

- Any difference from an approved procedure, environment, configuration, data
  or expected result must be recorded under the approved deviation process.
- Severity, impact, containment, retest, regression and closure criteria remain
  TBD until approved.
- A Critical or High deviation must not be self-dispositioned by the executor
  or this automation.
- Evidence must preserve the original observation and approved disposition;
  it must not be rewritten to make a result appear conforming.
- A blocked or failed execution must not be reported as validated or complete.

## 12. Exit criteria for this planning state

This scaffold may leave `draft` / `blocked` only when:

- G01-G18 are resolved or formally marked not applicable by authorized
  reviewers with rationale.
- Each Test Case has approved versioned prerequisites, detailed steps, exact
  expected results and objective pass/fail rules.
- Test users, environment, configuration, controlled data, isolation, cleanup,
  executor and independent reviewer are approved and available.
- Evidence capture, integrity, retention, review and RTM update methods are
  approved.
- QA Reviewer, CSV Reviewer and IT Owner record the required reviews.

Merging this planning document does not meet these criteria.

## 13. Incomplete Definition of Done

The following remain incomplete:

- Approval of URS-GOV-001, URS-GOV-002 and acceptance criteria.
- Approval of intended use, GxP scope, RACI, System Inventory governance,
  record granularity, lifecycle, ownership, classifications and boundaries.
- Approval of interface, dependency, data-flow, record, environment,
  configuration, Fit/Gap, FS/DS and implementation decisions.
- Assignment and approval of QA, CSV, IT, executor and reviewer roles.
- Approval of test levels, detailed procedures, controlled inputs, expected
  results and pass/fail rules.
- Preparation and approval of the test environment, configuration baseline,
  test users and controlled `POC-GOVERNANCE-001` data.
- Implementation, review and approval of any required DocType, permission,
  workflow, report, Fixture, Patch, API or custom control.
- Execution of all four Test Cases and disposition of deviations or defects.
- Creation, integrity verification, independent review and retention of all
  sixteen Evidence items.
- Update and approval of `RTM-P0-GOV-003-01` through
  `RTM-P0-GOV-003-04`.
- Resolution of all Critical/High findings.
- Authorized readiness transition and WP validation or completion.

This partial deliverable must not be used to approve or close
WP-P0-GOV-003.
