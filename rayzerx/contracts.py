"""Typed contracts for the first RayzerX local execution flow."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Literal
from uuid import uuid4

RunStatus = Literal["pending", "running", "passed", "failed", "blocked"]
FindingSeverity = Literal["info", "low", "medium", "high", "critical"]
ArtifactKind = Literal["file", "url", "report", "diff", "log"]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class TaskBrief:
    title: str
    description: str
    requested_by: str
    acceptance_criteria: list[str]
    constraints: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ExecutionContext:
    org_id: str
    project_id: str
    run_id: str
    correlation_id: str
    actor: str
    capability_scope: list[str]
    deadline_utc: str | None = None
    idempotency_key: str = field(default_factory=lambda: str(uuid4()))
    created_at: str = field(default_factory=utc_now)


@dataclass(frozen=True)
class AgentRunRequest:
    agent_role: str
    instruction: str
    task: TaskBrief
    context: ExecutionContext


@dataclass(frozen=True)
class ArtifactRef:
    kind: ArtifactKind
    path: str
    title: str
    description: str = ""


@dataclass(frozen=True)
class ReviewFinding:
    severity: FindingSeverity
    message: str
    location: str = ""
    recommendation: str = ""


@dataclass(frozen=True)
class UsageRecord:
    provider: str
    model: str
    input_units: int = 0
    output_units: int = 0
    cost_estimate_usd: float = 0.0
    note: str = ""


@dataclass(frozen=True)
class DecisionRecord:
    title: str
    decision: str
    rationale: str
    impact: str


@dataclass(frozen=True)
class AgentRunResult:
    agent_role: str
    status: RunStatus
    summary: str
    artifacts: list[ArtifactRef] = field(default_factory=list)
    findings: list[ReviewFinding] = field(default_factory=list)
    decisions: list[DecisionRecord] = field(default_factory=list)
    usage: list[UsageRecord] = field(default_factory=list)


@dataclass(frozen=True)
class FlowReport:
    task: TaskBrief
    context: ExecutionContext
    status: RunStatus
    results: list[AgentRunResult]
    created_at: str = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def load_task_brief(path: Path) -> TaskBrief:
    import json

    data = json.loads(path.read_text(encoding="utf-8"))
    return TaskBrief(
        title=data["title"],
        description=data["description"],
        requested_by=data.get("requested_by", "unknown"),
        acceptance_criteria=list(data.get("acceptance_criteria", [])),
        constraints=list(data.get("constraints", [])),
    )
