# RayzerX agent suitability matrix

This matrix is the first operating filter for turning demo agents into RayzerX building blocks.

Legend:

- **Keep now**: good candidate for the first vertical slice.
- **Adapt later**: useful, but needs more platform work first.
- **Defer**: do not wire into RayzerX until a risk or dependency gap is closed.

| Agent | RayzerX role | Decision | Main blocker before production |
| --- | --- | --- | --- |
| `01-web-research-agent` | Research | Adapt later | Dependency conflict around LangGraph/LangChain versions; needs source/audit policy |
| `02-code-review-agent` | Reviewer | Keep now | Needs model gateway, structured findings, and deterministic tests |
| `03-pdf-qa-agent` | Knowledge/RAG | Adapt later | Needs persistent isolated indexes per tenant/project |
| `04-sql-database-agent` | Data tool | Adapt later | Must keep read-only defaults and never expose core DB credentials |
| `05-email-drafting-agent` | Communications | Defer | External email workflows need recipient approval and send boundaries |
| `06-news-summarizer-agent` | Research | Adapt later | Needs source freshness, citations, and scheduled retrieval policy |
| `07-github-issue-triage-agent` | Project ops | Adapt later | Currently suggests changes; production needs controlled GitHub write policy |
| `08-data-analysis-agent` | Data analysis | Defer | Dangerous code execution must be sandboxed before use |
| `09-social-media-agent` | Marketing | Defer | External publishing requires account approvals and review gates |
| `10-meeting-notes-agent` | Documentation | Adapt later | Needs input/source boundary and storage policy |
| `11-stock-research-agent` | Finance research | Defer | Financial output needs source verification and explicit non-advisory framing |
| `12-content-creation-agent` | Content | Adapt later | Needs brand policy and review workflow |
| `13-customer-support-agent` | Support/memory | Defer | Tenant-safe memory and real escalation integration are missing |
| `14-travel-planning-agent` | Planning | Defer | Not core to initial RayzerX software-company flow |
| `15-unit-test-generator` | Tester | Keep now | Needs test execution harness, coverage goal, and sandboxed file writes |
| `16-documentation-writer` | Documenter | Keep now | Needs path allowlist and review before writing project docs |
| `17-recipe-agent` | Consumer assistant | Defer | Not core to initial RayzerX flow |
| `18-job-application-agent` | HR workflow | Defer | Handles personal data; requires privacy and submission controls |
| `19-competitive-analysis-agent` | Market research | Keep now | Needs real retrieval, citations, and source confidence |
| `20-multi-agent-debate` | Decision support | Keep now | Needs structured decision records and persistence |
| `21-pii-sanitization-agent` | Privacy guard | Defer | Sends data to external sanitizer; privacy boundary must be approved |

## First implementation set

Start with these five adapters:

1. `02-code-review-agent`
2. `15-unit-test-generator`
3. `16-documentation-writer`
4. `19-competitive-analysis-agent`
5. `20-multi-agent-debate`

They map directly to the RayzerX build loop: review, test, document, research, and decide.

## First exclusion rule

Any agent that runs model-generated code, sends personal data to an external service, writes to arbitrary paths, or performs external account actions is excluded from the first runnable slice.
