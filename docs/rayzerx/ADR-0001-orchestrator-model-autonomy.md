# ADR-0001 — Orchestrator model autonomy and upstream-first integration

## Status

Accepted.

## Context

The RayzerX bootstrap initially described provider/model access as something that should be blocked until a central gateway existed. That framing is too restrictive for the intended RayzerX operating model.

The upstream project and its agent examples already have validated operational dynamics. RayzerX should not force those dynamics into a new rigid structure. The correct strategy is to fit RayzerX around the existing flow, then add orchestration, auditability, budgets, memory, and product experience on top.

## Decision

RayzerX agents may choose, switch, or call AI providers automatically when the orchestration policy allows it.

The orchestrator must support autonomous model selection because that is part of the product's core value. The control layer should observe, budget, audit, and route model usage; it should not remove the agent's ability to use the most appropriate IA for a task.

RayzerX will follow an **upstream-first integration strategy**:

1. Preserve the source project's working dynamics.
2. Identify which existing flow already solves part of RayzerX's need.
3. Add RayzerX context, policy, memory, UI, and audit around that flow.
4. Only replace internals when there is evidence of risk, missing capability, or scaling limit.

## Consequences

- The provider gateway is renamed conceptually to a **model autonomy controller**.
- Direct provider calls are not automatically forbidden.
- Model/provider switching is allowed when recorded and governed.
- The first local bootstrap remains deterministic only because no production credentials or budget were configured in this environment.
- Future implementations should prioritize wrapping the existing agent behavior before rewriting it.

## Guardrails

Autonomy does not mean absence of control. Production execution still requires:

- usage ledger;
- budget limits;
- secret handling;
- audit events;
- tenant/project isolation;
- sandboxing when generated code is executed;
- clear fallback behavior when a model/provider fails.
