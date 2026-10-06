# RayzerX contracts

These contracts define the first stable boundary for adapting demo agents into a RayzerX build flow. They are intentionally small so the first vertical slice can run locally before paid model calls, cloud state, or production deployment are added.

## Design rules

- Every run must be traceable by organization, project, run, and correlation identifiers.
- Every agent must receive an explicit capability scope.
- Every result must report status, artifacts, findings, decisions, and usage.
- Model/provider calls are not allowed until the provider gateway and budget controls exist.
- Agents may not write outside approved project paths.

## Core records

| Contract | Purpose |
| --- | --- |
| `TaskBrief` | Captures the user's requested work and acceptance criteria. |
| `ExecutionContext` | Carries traceability, actor, deadline, idempotency, and capability scope. |
| `AgentRunRequest` | Sends a role-specific instruction to an agent adapter. |
| `AgentRunResult` | Returns structured output from an agent adapter. |
| `ArtifactRef` | Points to a file, URL, report, diff, or generated asset. |
| `ReviewFinding` | Records reviewer/tester findings with severity and location. |
| `UsageRecord` | Records provider/runtime usage. First slice only records local runtime usage. |
| `DecisionRecord` | Captures structured decisions and why they were made. |

## Status values

- `pending`
- `running`
- `passed`
- `failed`
- `blocked`

## Capability scopes

The first local flow supports these capability strings:

- `plan`
- `research`
- `write_docs`
- `review`
- `run_local_checks`

Additional capabilities require a policy update before implementation.

## First flow contract

The first runnable flow accepts a task brief and produces:

- implementation plan
- research notes
- local check result
- review findings
- documentation handoff
- final run report

No external model call is performed in this phase.
