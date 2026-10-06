# RayzerX first local flow

The first flow proves the RayzerX operating model without pretending the platform is production-ready. It is deterministic only for this bootstrap environment; the product direction allows automatic IA/model selection by the orchestrator.

## Flow

1. **Planner** converts a task brief into ordered steps.
2. **Researcher** maps the brief against the reusable source-agent inventory.
3. **Tester** runs deterministic local checks.
4. **Reviewer** inspects the run result for blockers and missing gates.
5. **Documenter** writes the handoff summary.

## Local command

```bash
python -m rayzerx.cli examples/rayzerx/software-task.json
```

The command writes a structured report to `tmp/rayzerx/runs/`.

## What this proves

- The team flow can be represented as structured data.
- The first execution can complete without model-provider credentials.
- We can wrap existing agents behind the same contracts later while preserving their validated flow.

## What this does not prove yet

- Real code generation.
- Automatic model/provider switching.
- Sandboxed code execution.
- Persistent workflow storage.
- Multi-tenant isolation.
- Production deployment.

Those belong to later phases after the contracts and gates are accepted.
