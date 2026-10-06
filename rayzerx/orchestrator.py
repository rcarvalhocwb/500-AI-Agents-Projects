"""Deterministic first RayzerX flow.

This local bootstrap is provider-free because no production credentials or
budget policy are configured in this environment. RayzerX product direction
allows autonomous model/provider selection by the orchestrator.
"""

from __future__ import annotations

import json
from pathlib import Path
from uuid import uuid4

from .contracts import (
    AgentRunResult,
    ArtifactRef,
    DecisionRecord,
    ExecutionContext,
    FlowReport,
    ReviewFinding,
    TaskBrief,
    UsageRecord,
)

FIRST_AGENT_SET = [
    "02-code-review-agent",
    "15-unit-test-generator",
    "16-documentation-writer",
    "19-competitive-analysis-agent",
    "20-multi-agent-debate",
]


def create_context(actor: str) -> ExecutionContext:
    return ExecutionContext(
        org_id="rayzerx",
        project_id="rayzerx-bootstrap",
        run_id=f"run-{uuid4()}",
        correlation_id=f"corr-{uuid4()}",
        actor=actor,
        capability_scope=[
            "plan",
            "research",
            "write_docs",
            "review",
            "run_local_checks",
        ],
    )


def run_first_flow(task: TaskBrief, output_dir: Path) -> FlowReport:
    context = create_context(task.requested_by)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = [
        _planner(task),
        _researcher(task),
        _tester(task),
        _reviewer(task),
        _documenter(task, output_dir),
    ]

    status = "passed"
    if any(result.status in {"failed", "blocked"} for result in results):
        status = "blocked"

    report = FlowReport(task=task, context=context, status=status, results=results)
    report_path = output_dir / f"{context.run_id}.json"
    report_path.write_text(
        json.dumps(report.to_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return report


def _local_usage(note: str) -> list[UsageRecord]:
    return [
        UsageRecord(
            provider="local",
            model="deterministic-bootstrap",
            note=note,
        )
    ]


def _planner(task: TaskBrief) -> AgentRunResult:
    steps = [
        "Lock contracts around the existing validated agent dynamics.",
        "Wrap the first safe source-agent set before rewriting internals.",
        "Allow model/provider autonomy when policy and budget are configured.",
        "Add sandboxing before generated code execution.",
        "Produce a human-readable handoff after each run.",
    ]
    return AgentRunResult(
        agent_role="planner",
        status="passed",
        summary="Plano inicial criado: " + " ".join(steps),
        decisions=[
            DecisionRecord(
                title="Use upstream-first integration",
                decision="Fit RayzerX around the source project's validated dynamics before replacing internals.",
                rationale="The existing project is already operational; RayzerX should add orchestration, audit, memory, and product experience around it.",
                impact="Model autonomy remains a core orchestrator capability and will be governed rather than blocked.",
            )
        ],
        usage=_local_usage("Planning used deterministic rules only."),
    )


def _researcher(task: TaskBrief) -> AgentRunResult:
    return AgentRunResult(
        agent_role="researcher",
        status="passed",
        summary=(
            "Primeiro conjunto recomendado: "
            + ", ".join(FIRST_AGENT_SET)
            + ". Esses agentes cobrem revisão, testes, documentação, pesquisa e decisão."
        ),
        artifacts=[
            ArtifactRef(
                kind="file",
                path="docs/rayzerx/agent-suitability-matrix.md",
                title="RayzerX agent suitability matrix",
            )
        ],
        usage=_local_usage("Research used the curated suitability matrix."),
    )


def _tester(task: TaskBrief) -> AgentRunResult:
    return AgentRunResult(
        agent_role="tester",
        status="passed",
        summary=(
            "Check local concluído: este bootstrap não depende de credenciais de produção, "
            "não executa código gerado por modelo e não faz deploy."
        ),
        findings=[
            ReviewFinding(
                severity="info",
                message="Production test execution harness still needs to be implemented.",
                recommendation="Add command allowlists and sandbox execution before running generated project code.",
            )
        ],
        usage=_local_usage("Testing used static bootstrap checks."),
    )


def _reviewer(task: TaskBrief) -> AgentRunResult:
    return AgentRunResult(
        agent_role="reviewer",
        status="passed",
        summary="Nenhum bloqueio para a fase bootstrap. A autonomia de IA foi registrada como requisito central.",
        findings=[
            ReviewFinding(
                severity="info",
                message="Model autonomy controller is not implemented yet.",
                recommendation="Allow model/provider switching in product design, but record provider, model, reason, cost, and outcome per run.",
            ),
            ReviewFinding(
                severity="medium",
                message="Sandbox policy is not implemented yet.",
                recommendation="Keep dangerous execution agents deferred until filesystem and process policies exist.",
            ),
        ],
        usage=_local_usage("Review used documented gates."),
    )


def _documenter(task: TaskBrief, output_dir: Path) -> AgentRunResult:
    handoff = output_dir / "latest-handoff.md"
    handoff.write_text(
        "\n".join(
            [
                "# RayzerX local flow handoff",
                "",
                f"Task: {task.title}",
                "",
                "Status: bootstrap flow executed locally without production IA credentials.",
                "",
                "Next implementation step:",
                "",
                "1. Add the model autonomy controller contract.",
                "2. Wrap `02-code-review-agent` while preserving its existing dynamics.",
                "3. Add tests for structured review findings.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return AgentRunResult(
        agent_role="documenter",
        status="passed",
        summary="Handoff local criado para orientar o próximo ciclo.",
        artifacts=[
            ArtifactRef(
                kind="report",
                path=str(handoff),
                title="RayzerX local flow handoff",
            )
        ],
        usage=_local_usage("Documentation used deterministic template output."),
    )
