# RayzerX first local flow

The first flow proves the RayzerX operating model without pretending the platform is production-ready.

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
- We can add adapted agents behind the same contracts later.

## What this does not prove yet

- Real code generation.
- Paid model routing.
- Sandboxed code execution.
- Persistent workflow storage.
- Multi-tenant isolation.
- Production deployment.

Those belong to later phases after the contracts and gates are accepted.
