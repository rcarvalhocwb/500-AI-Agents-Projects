# RayzerX upstream-first integration plan

## Goal

Turn this MIT-licensed agent catalog into a RayzerX-compatible starting point by fitting RayzerX around the project’s already validated dynamics: plan, build, test, review, document, and report.

This repository should be treated as the reusable agent-pattern inventory and operational reference. The RayzerX product layer should add orchestration, context, memory, governance, model autonomy, deployment controls, and persistence on top.

## Phase 0 — Repository hygiene

- Keep upstream attribution and MIT license intact.
- Keep `origin` pointed to the RayzerX fork and `upstream` pointed to the original repository.
- Ignore local build artifacts and dependency folders.
- Work from feature branches before merging to `main`.

Acceptance:

- `git status` only shows intentional source changes.
- Existing React atlas still builds.

## Phase 1 — Agent inventory and selection

Create a RayzerX suitability matrix for each existing `agents/*` example:

| Dimension | Required decision |
| --- | --- |
| Product fit | Keep, adapt later, or exclude |
| Runtime risk | Safe, needs sandbox, external integration risk, or not approved |
| Dependency health | Installable, conflict, outdated, or unknown |
| Data boundary | Local-only, provider call, third-party service, or PII-sensitive |
| RayzerX role | Planner, builder, reviewer, tester, documenter, researcher, support, or memory |

Initial keep/adapt candidates:

- `02-code-review-agent`
- `15-unit-test-generator`
- `16-documentation-writer`
- `19-competitive-analysis-agent`
- `20-multi-agent-debate`

Initial defer/exclude candidates:

- `08-data-analysis-agent` until dangerous-code execution is sandboxed.
- `13-customer-support-agent` until tenant-safe memory and real ticket escalation exist.
- `21-pii-sanitization-agent` until external privacy boundary is approved.

## Phase 2 — RayzerX contracts around the existing flow

Define minimal contracts before wrapping or extending code:

- `TaskBrief`
- `AgentRunRequest`
- `AgentRunResult`
- `ArtifactRef`
- `ReviewFinding`
- `UsageRecord`
- `DecisionRecord`

Each contract should include organization/project/run identifiers, correlation ID, actor, deadline, idempotency key, and capability scope.

## Phase 3 — Model autonomy controller

Add a controller that lets the orchestrator choose, switch, and call IA providers automatically while preserving traceability:

- Model routing by task type, agent role, cost, quality, latency, and availability.
- API key lookup through secret broker.
- Usage ledger per run.
- Budget fail-closed behavior.
- Provider-independent request/response shape.
- Audit trail showing which IA was selected and why.

Direct provider calls are not automatically forbidden. They must be either wrapped, observed, or approved by policy so RayzerX can track usage, cost, and outcomes without breaking useful existing dynamics.

## Phase 4 — First runnable vertical slice

Build one end-to-end flow:

1. `planner` turns a task brief into steps.
2. `builder` prepares changes in a sandboxed repository workspace.
3. `tester` runs allowed test commands.
4. `reviewer` reviews the diff.
5. `documenter` writes a handoff summary.

For this fork, Phase 4 can start as a local CLI or API prototype before production deployment.

Acceptance:

- A sample task produces a structured run report.
- The build/test command is deterministic and auditable.
- Model/provider switching is recorded and budget-aware.

## Phase 5 — Production hardening

- Persistent workflow state.
- Tenant separation.
- Audit event stream.
- Runtime policy engine for tools.
- Deployment pipeline.
- Monitoring and failure recovery.

## Immediate next files to create

- `docs/rayzerx/agent-suitability-matrix.md`
- `docs/rayzerx/contracts.md`
- `docs/rayzerx/first-flow.md`
- `rayzerx/` implementation folder once the contracts are accepted.
