# Muhammad Basit Ali

I am a cloud security and AI agent security engineer. I build tooling for AWS guardrails, Microsoft 365 governance, MCP servers and Claude Code skills. Everything below is open source and each repository stands on its own.

## Claude Code skill packs

| Repository | What it is |
|---|---|
| [claude-skills](https://github.com/basitalisandhu/claude-skills) | Every skill I maintain, in one repository: 87 skills in 13 plugins from the packs below, one marketplace, one install script, synced daily. |
| [ways-of-working-skills](https://github.com/basitalisandhu/ways-of-working-skills) | Claude Code skills for ways of working: change requests from a Terraform plan, an action ledger across meeting notes, exception and risk registers, RFC lint, a decision log, weekly status notes, a private 1:1 ledger and focus time from a calendar export. |
| [aws-security-skills](https://github.com/basitalisandhu/aws-security-skills) | AWS security skills for Claude Code: account audit, SCP guardrails, blast-radius landing zones, IAM least privilege, Security Hub triage. |
| [repo-engineering-skills](https://github.com/basitalisandhu/repo-engineering-skills) | Repository engineering skills for Claude Code: docs checked against the code, audits where every finding cites a line, agent context files that say only what code cannot. |
| [m365-governance-skills](https://github.com/basitalisandhu/m365-governance-skills) | Microsoft 365 governance skills for Claude Code: Entra ID posture review, Intune baseline check, Graph permission preflight, Teams and group sprawl, access review pack. |
| [compliance-evidence-skills](https://github.com/basitalisandhu/compliance-evidence-skills) | Compliance evidence skills for Claude Code: integrity-checked evidence packs from GitHub, AWS and Microsoft 365 exports, mapped to ISO 27001 and SOC 2, with narratives that cite evidence or say not assessable. |
| [claude-dev-skills](https://github.com/basitalisandhu/claude-dev-skills) | Claude Code skills for everyday development: code review, refactoring, debugging, CI and containers, data and APIs, documentation and security basics. |
| [agent-security-skills](https://github.com/basitalisandhu/agent-security-skills) | Claude Code security plugin and agent skills for securing LLM agents: threat modelling, configuration audits, prompt injection review, MCP server review, incident lookup. |
| [github-manager-skills](https://github.com/basitalisandhu/github-manager-skills) | Claude Code skills for engineering managers that compute from exported GitHub data: stuck-PR and review-queue digest, iteration report, blameless postmortem timeline. |
| [mac-maintenance-skills](https://github.com/basitalisandhu/mac-maintenance-skills) | Claude Code skills for cleaning up and speeding up a Mac: read-only survey first, safe tier removes only what programs recreate, leftovers and duplicate finders. |

## MCP tooling

| Repository | What it is |
|---|---|
| [dev-mcp-servers](https://github.com/basitalisandhu/dev-mcp-servers) | Ten small MCP servers for everyday development and security checks. |
| [mcp-server-template](https://github.com/basitalisandhu/mcp-server-template) | Secure MCP server template in TypeScript and Python, safe by default. |
| [mcp-tools-lint](https://github.com/basitalisandhu/mcp-tools-lint) | Lint MCP tool schemas and annotations before clients reject them. |
| [mcp-auth-doctor](https://github.com/basitalisandhu/mcp-auth-doctor) | Diagnose OAuth discovery problems on remote MCP servers. |
| [mcp-egress](https://github.com/basitalisandhu/mcp-egress) | Record every host an MCP server contacts, per tool, and fail CI on new ones. |
| [claude-mcp-allow](https://github.com/basitalisandhu/claude-mcp-allow) | Least-privilege Claude Code permission rules for MCP tools, generated from their annotations. |

## Security tooling

| Repository | What it is |
|---|---|
| [agent-threat-model](https://github.com/basitalisandhu/agent-threat-model) | Threat modeling for AI agents: describe the system in YAML, get a STRIDE and OWASP Agentic threat model. |
| [agent-config-audit](https://github.com/basitalisandhu/agent-config-audit) | Audit AI agent configuration files for security risks. |
| [agentic-semgrep-rules](https://github.com/basitalisandhu/agentic-semgrep-rules) | Semgrep rules for AI agent code in Python, TypeScript and JavaScript. |
| [security-actions](https://github.com/basitalisandhu/security-actions) | GitHub Actions for AI agent and supply chain security checks. |
| [cc-hooks](https://github.com/basitalisandhu/cc-hooks) | Typed Python SDK and offline test runner for Claude Code hooks. |
| [cc-plugin-lock](https://github.com/basitalisandhu/cc-plugin-lock) | Lock file for Claude Code plugins: pins plugins and skills to content hashes and verifies them before load. |
| [claude-perm-sim](https://github.com/basitalisandhu/claude-perm-sim) | Claude Code permission rule simulator: shows which rule decides a tool call and where a rule set is permissive. |
| [llms-txt-gen](https://github.com/basitalisandhu/llms-txt-gen) | Generate llms.txt for any docs site or repository. |

## Data and lists

| Repository | What it is |
|---|---|
| [ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents) | An open dataset of AI agent and LLM security incidents, with a [browsable site](https://basitalisandhu.github.io/ai-agent-incidents/). |
| [awesome-agent-security](https://github.com/basitalisandhu/awesome-agent-security) | Curated list of AI agent security tools, papers and datasets. |

Packages: published packages are listed at [github.com/basitalisandhu?tab=packages](https://github.com/basitalisandhu?tab=packages).

### Latest releases

<!-- RELEASES:START -->
| Project | Latest release | Published |
|---|---|---|
| [aws-security-skills](https://github.com/basitalisandhu/aws-security-skills) | [v0.3.0](https://github.com/basitalisandhu/aws-security-skills/releases/tag/v0.3.0) | 2026-10-05 |
| [repo-engineering-skills](https://github.com/basitalisandhu/repo-engineering-skills) | [v0.3.1](https://github.com/basitalisandhu/repo-engineering-skills/releases/tag/v0.3.1) | 2026-10-05 |
| [m365-governance-skills](https://github.com/basitalisandhu/m365-governance-skills) | [v0.3.0](https://github.com/basitalisandhu/m365-governance-skills/releases/tag/v0.3.0) | 2026-10-05 |
| [compliance-evidence-skills](https://github.com/basitalisandhu/compliance-evidence-skills) | [v0.1.2](https://github.com/basitalisandhu/compliance-evidence-skills/releases/tag/v0.1.2) | 2026-10-05 |
| [claude-dev-skills](https://github.com/basitalisandhu/claude-dev-skills) | [v0.1.2](https://github.com/basitalisandhu/claude-dev-skills/releases/tag/v0.1.2) | 2026-10-05 |
| [agent-security-skills](https://github.com/basitalisandhu/agent-security-skills) | [v0.2.0](https://github.com/basitalisandhu/agent-security-skills/releases/tag/v0.2.0) | 2026-10-05 |
| [dev-mcp-servers](https://github.com/basitalisandhu/dev-mcp-servers) | [v0.1.1](https://github.com/basitalisandhu/dev-mcp-servers/releases/tag/v0.1.1) | 2026-10-05 |
| [mcp-server-template](https://github.com/basitalisandhu/mcp-server-template) | [v0.1.1](https://github.com/basitalisandhu/mcp-server-template/releases/tag/v0.1.1) | 2026-10-05 |
| [mcp-tools-lint](https://github.com/basitalisandhu/mcp-tools-lint) | [v0.1.1](https://github.com/basitalisandhu/mcp-tools-lint/releases/tag/v0.1.1) | 2026-10-05 |
| [mcp-auth-doctor](https://github.com/basitalisandhu/mcp-auth-doctor) | [v0.1.1](https://github.com/basitalisandhu/mcp-auth-doctor/releases/tag/v0.1.1) | 2026-10-05 |
| [mcp-egress](https://github.com/basitalisandhu/mcp-egress) | [v0.1.1](https://github.com/basitalisandhu/mcp-egress/releases/tag/v0.1.1) | 2026-10-05 |
| [claude-mcp-allow](https://github.com/basitalisandhu/claude-mcp-allow) | [v0.1.1](https://github.com/basitalisandhu/claude-mcp-allow/releases/tag/v0.1.1) | 2026-10-05 |
| [agent-threat-model](https://github.com/basitalisandhu/agent-threat-model) | [v0.1.1](https://github.com/basitalisandhu/agent-threat-model/releases/tag/v0.1.1) | 2026-10-05 |
| [agent-config-audit](https://github.com/basitalisandhu/agent-config-audit) | [v0.1.1](https://github.com/basitalisandhu/agent-config-audit/releases/tag/v0.1.1) | 2026-10-05 |
| [agentic-semgrep-rules](https://github.com/basitalisandhu/agentic-semgrep-rules) | [v0.1.0](https://github.com/basitalisandhu/agentic-semgrep-rules/releases/tag/v0.1.0) | 2026-10-04 |
| [security-actions](https://github.com/basitalisandhu/security-actions) | [v0.1.0](https://github.com/basitalisandhu/security-actions/releases/tag/v0.1.0) | 2026-10-04 |
| [cc-hooks](https://github.com/basitalisandhu/cc-hooks) | [v0.1.1](https://github.com/basitalisandhu/cc-hooks/releases/tag/v0.1.1) | 2026-10-05 |
| [cc-plugin-lock](https://github.com/basitalisandhu/cc-plugin-lock) | [v0.1.0](https://github.com/basitalisandhu/cc-plugin-lock/releases/tag/v0.1.0) | 2026-10-04 |
| [claude-perm-sim](https://github.com/basitalisandhu/claude-perm-sim) | [v0.1.0](https://github.com/basitalisandhu/claude-perm-sim/releases/tag/v0.1.0) | 2026-10-04 |
| [llms-txt-gen](https://github.com/basitalisandhu/llms-txt-gen) | [v0.1.1](https://github.com/basitalisandhu/llms-txt-gen/releases/tag/v0.1.1) | 2026-10-05 |
| [ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents) | no public release yet | |
| [awesome-agent-security](https://github.com/basitalisandhu/awesome-agent-security) | no public release yet | |
<!-- RELEASES:END -->

## Contact

- GitHub: [@basitalisandhu](https://github.com/basitalisandhu)
- Questions about a project: open an issue in that project's repository.
