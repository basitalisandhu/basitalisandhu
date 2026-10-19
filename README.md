# Muhammad Basit Ali

**AI agent security and cloud security engineer.** I build open-source tools for agent identities, MCP servers and Claude Code skills, and I publish the data behind them.

## Start here

- **[agent-off-switch](https://github.com/basitalisandhu/agent-off-switch)**: find every AI agent identity in Microsoft 365, AWS and GitHub, see what it can reach, and get an ordered runbook to switch it off. Offline on saved read-only exports; it prints commands and never runs them. Try it with `aos review examples/demo-tenant`.
- **[The state of public agent skills and MCP servers](https://github.com/basitalisandhu/agent-skills-state-2026)**: a study of 2,999 public skill, plugin and MCP repositories, with the dataset, method and scripts. It is re-run every month; see the [monthly index](https://github.com/basitalisandhu/agent-skills-state-2026#updated-monthly).
- **[skill-scan-gate](https://github.com/basitalisandhu/skill-scan-gate)**: a CI gate for Claude Code skills and plugins that fails the build on instruction-override text, exfiltration patterns, dangerous hooks and unpinned MCP servers, with SARIF for code scanning. On the [GitHub Marketplace](https://github.com/marketplace/actions/skill-scan-gate).
- **[claude-skills](https://github.com/basitalisandhu/claude-skills)**: every Claude Code skill I maintain in one repository, one marketplace and one install command.
- **[ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents)**: an open dataset of AI agent and LLM security incidents mapped to the OWASP LLM and Agentic Top 10 and MITRE ATLAS, with a [browsable site](https://basitalisandhu.github.io/ai-agent-incidents/).
- **[m365-governance-skills](https://github.com/basitalisandhu/m365-governance-skills)**: Claude Code skills for Microsoft 365 governance (Graph permission preflight, Entra ID posture, Intune baselines, access reviews) that read Graph exports offline.
- **[aws-security-skills](https://github.com/basitalisandhu/aws-security-skills)**: Claude Code skills for AWS security (account audit, SCP guardrails, IAM least privilege, Security Hub triage) that read saved aws CLI output offline.

## Latest writing

- [Agent identities are the new service accounts](https://basitalisandhu.github.io/posts/agent-identities-are-the-new-service-accounts/)
- [The state of public agent skills and MCP servers](https://basitalisandhu.github.io/posts/the-state-of-public-agent-skills-and-mcp-servers/)
- [Every Claude Code skill I maintain, in one repository](https://dev.to/basitalisandhu/every-claude-code-skill-i-maintain-in-one-repository-3pp9) (dev.to)
- All posts, and a page per project with install steps: [basitalisandhu.github.io](https://basitalisandhu.github.io/)

Everything below is open source and each repository stands on its own.

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
| [claude-code-tooling-skills](https://github.com/basitalisandhu/claude-code-tooling-skills) | Claude Code skills for keeping a Claude Code setup safe: review a third-party skill before installing it, lint skill descriptions, audit the context budget, build least-privilege permissions, test hooks. |
| [agent-identity-governance-skills](https://github.com/basitalisandhu/agent-identity-governance-skills) | Claude Code skills for agent identity governance: inventory the non-human identities agents run as, review permissions, recertify quarterly, catch expiring credentials, switch one off fast. |

## MCP tooling

| Repository | What it is |
|---|---|
| [dev-mcp-servers](https://github.com/basitalisandhu/dev-mcp-servers) | Ten small MCP servers for everyday development and security checks. |
| [mcp-server-template](https://github.com/basitalisandhu/mcp-server-template) | Secure MCP server template in TypeScript and Python, safe by default. |
| [mcp-tools-lint](https://github.com/basitalisandhu/mcp-tools-lint) | Lint MCP tool schemas and annotations before clients reject them. |
| [mcp-auth-doctor](https://github.com/basitalisandhu/mcp-auth-doctor) | Diagnose OAuth discovery problems on remote MCP servers. |
| [mcp-egress](https://github.com/basitalisandhu/mcp-egress) | Record every host an MCP server contacts, per tool, and fail CI on new ones. |
| [claude-mcp-allow](https://github.com/basitalisandhu/claude-mcp-allow) | Least-privilege Claude Code permission rules for MCP tools, generated from their annotations. |
| [agentdojo-mcp](https://github.com/basitalisandhu/agentdojo-mcp) | Run the AgentDojo benchmark's user and injection tasks against a real MCP server's tools. |
| [garak-mcp-probes](https://github.com/basitalisandhu/garak-mcp-probes) | Run garak against your own MCP servers, with detectors for denied tool calls, leaked canaries and runaway step counts. |
| [mcp-rc-check](https://github.com/basitalisandhu/mcp-rc-check) | MCP specification migration checker for the 2026-07-28 revision: flags removed, changed and deprecated constructs and writes a patch for mechanical fixes. |

## Security tooling

| Repository | What it is |
|---|---|
| [agent-off-switch](https://github.com/basitalisandhu/agent-off-switch) | Find every AI agent identity in Microsoft 365, AWS and GitHub, see what it can reach, and switch it off. Offline on saved exports. |
| [skill-scan-gate](https://github.com/basitalisandhu/skill-scan-gate) | CI gate for Claude Code skills and plugins, with SARIF output. GitHub Action and CLI. |
| [agent-threat-model](https://github.com/basitalisandhu/agent-threat-model) | Threat modeling for AI agents: describe the system in YAML, get a STRIDE and OWASP Agentic threat model. |
| [agent-config-audit](https://github.com/basitalisandhu/agent-config-audit) | Audit AI agent configuration files for security risks. |
| [agentic-semgrep-rules](https://github.com/basitalisandhu/agentic-semgrep-rules) | Semgrep rules for AI agent code in Python, TypeScript and JavaScript. |
| [security-actions](https://github.com/basitalisandhu/security-actions) | GitHub Actions for AI agent and supply chain security checks. |
| [cc-hooks](https://github.com/basitalisandhu/cc-hooks) | Typed Python SDK and offline test runner for Claude Code hooks. |
| [cc-plugin-lock](https://github.com/basitalisandhu/cc-plugin-lock) | Lock file for Claude Code plugins: pins plugins and skills to content hashes and verifies them before load. |
| [claude-perm-sim](https://github.com/basitalisandhu/claude-perm-sim) | Claude Code permission rule simulator: shows which rule decides a tool call and where a rule set is permissive. |
| [llms-txt-gen](https://github.com/basitalisandhu/llms-txt-gen) | Generate llms.txt for any docs site or repository. |
| [scp-guardrails](https://github.com/basitalisandhu/scp-guardrails) | Build AWS service control policies from a short spec and lint them for lockouts and statements that deny nothing. |
| [spotlighting](https://github.com/basitalisandhu/spotlighting) | Spotlighting for prompt injection defence in Python: mark untrusted text before it reaches a model. |

## Data and lists

| Repository | What it is |
|---|---|
| [ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents) | An open dataset of AI agent and LLM security incidents, with a [browsable site](https://basitalisandhu.github.io/ai-agent-incidents/). |
| [agent-skills-state-2026](https://github.com/basitalisandhu/agent-skills-state-2026) | Monthly study of public agent skill, plugin and MCP repositories: dataset, method, hand-checked precision and scripts. |
| [awesome-agent-security](https://github.com/basitalisandhu/awesome-agent-security) | Curated list of AI agent security tools, papers and datasets. |

Packages: published packages are listed at [github.com/basitalisandhu?tab=packages](https://github.com/basitalisandhu?tab=packages).

### Latest releases

<!-- RELEASES:START -->
| Project | Latest release | Published |
|---|---|---|
| [agent-off-switch](https://github.com/basitalisandhu/agent-off-switch) | [v0.1.1](https://github.com/basitalisandhu/agent-off-switch/releases/tag/v0.1.1) | 2026-10-18 |
| [agent-skills-state-2026](https://github.com/basitalisandhu/agent-skills-state-2026) | [v1.1.0](https://github.com/basitalisandhu/agent-skills-state-2026/releases/tag/v1.1.0) | 2026-10-16 |
| [skill-scan-gate](https://github.com/basitalisandhu/skill-scan-gate) | [v0.3.0](https://github.com/basitalisandhu/skill-scan-gate/releases/tag/v0.3.0) | 2026-10-13 |
| [claude-skills](https://github.com/basitalisandhu/claude-skills) | [v0.3.0](https://github.com/basitalisandhu/claude-skills/releases/tag/v0.3.0) | 2026-10-16 |
| [aws-security-skills](https://github.com/basitalisandhu/aws-security-skills) | [v0.4.1](https://github.com/basitalisandhu/aws-security-skills/releases/tag/v0.4.1) | 2026-10-18 |
| [repo-engineering-skills](https://github.com/basitalisandhu/repo-engineering-skills) | [v0.5.0](https://github.com/basitalisandhu/repo-engineering-skills/releases/tag/v0.5.0) | 2026-10-18 |
| [m365-governance-skills](https://github.com/basitalisandhu/m365-governance-skills) | [v0.5.1](https://github.com/basitalisandhu/m365-governance-skills/releases/tag/v0.5.1) | 2026-10-18 |
| [compliance-evidence-skills](https://github.com/basitalisandhu/compliance-evidence-skills) | [v0.5.0](https://github.com/basitalisandhu/compliance-evidence-skills/releases/tag/v0.5.0) | 2026-10-18 |
| [claude-dev-skills](https://github.com/basitalisandhu/claude-dev-skills) | [v0.3.1](https://github.com/basitalisandhu/claude-dev-skills/releases/tag/v0.3.1) | 2026-10-18 |
| [agent-security-skills](https://github.com/basitalisandhu/agent-security-skills) | [v0.5.0](https://github.com/basitalisandhu/agent-security-skills/releases/tag/v0.5.0) | 2026-10-18 |
| [ways-of-working-skills](https://github.com/basitalisandhu/ways-of-working-skills) | [v0.4.0](https://github.com/basitalisandhu/ways-of-working-skills/releases/tag/v0.4.0) | 2026-10-18 |
| [github-manager-skills](https://github.com/basitalisandhu/github-manager-skills) | [v0.3.1](https://github.com/basitalisandhu/github-manager-skills/releases/tag/v0.3.1) | 2026-10-18 |
| [mac-maintenance-skills](https://github.com/basitalisandhu/mac-maintenance-skills) | [v0.1.4](https://github.com/basitalisandhu/mac-maintenance-skills/releases/tag/v0.1.4) | 2026-10-18 |
| [claude-code-tooling-skills](https://github.com/basitalisandhu/claude-code-tooling-skills) | [v0.3.0](https://github.com/basitalisandhu/claude-code-tooling-skills/releases/tag/v0.3.0) | 2026-10-18 |
| [agent-identity-governance-skills](https://github.com/basitalisandhu/agent-identity-governance-skills) | [v0.2.0](https://github.com/basitalisandhu/agent-identity-governance-skills/releases/tag/v0.2.0) | 2026-10-18 |
| [dev-mcp-servers](https://github.com/basitalisandhu/dev-mcp-servers) | [v0.2.2](https://github.com/basitalisandhu/dev-mcp-servers/releases/tag/v0.2.2) | 2026-10-18 |
| [mcp-server-template](https://github.com/basitalisandhu/mcp-server-template) | [v0.2.1](https://github.com/basitalisandhu/mcp-server-template/releases/tag/v0.2.1) | 2026-10-18 |
| [mcp-tools-lint](https://github.com/basitalisandhu/mcp-tools-lint) | [v0.2.0](https://github.com/basitalisandhu/mcp-tools-lint/releases/tag/v0.2.0) | 2026-10-09 |
| [mcp-auth-doctor](https://github.com/basitalisandhu/mcp-auth-doctor) | [v0.3.0](https://github.com/basitalisandhu/mcp-auth-doctor/releases/tag/v0.3.0) | 2026-10-16 |
| [mcp-egress](https://github.com/basitalisandhu/mcp-egress) | [v0.1.1](https://github.com/basitalisandhu/mcp-egress/releases/tag/v0.1.1) | 2026-10-05 |
| [claude-mcp-allow](https://github.com/basitalisandhu/claude-mcp-allow) | [v0.3.0](https://github.com/basitalisandhu/claude-mcp-allow/releases/tag/v0.3.0) | 2026-10-16 |
| [mcp-rc-check](https://github.com/basitalisandhu/mcp-rc-check) | [v0.4.0](https://github.com/basitalisandhu/mcp-rc-check/releases/tag/v0.4.0) | 2026-10-16 |
| [agentdojo-mcp](https://github.com/basitalisandhu/agentdojo-mcp) | [v0.2.0](https://github.com/basitalisandhu/agentdojo-mcp/releases/tag/v0.2.0) | 2026-10-09 |
| [garak-mcp-probes](https://github.com/basitalisandhu/garak-mcp-probes) | [v0.1.0](https://github.com/basitalisandhu/garak-mcp-probes/releases/tag/v0.1.0) | 2026-10-05 |
| [agent-threat-model](https://github.com/basitalisandhu/agent-threat-model) | [v0.3.0](https://github.com/basitalisandhu/agent-threat-model/releases/tag/v0.3.0) | 2026-10-16 |
| [agent-config-audit](https://github.com/basitalisandhu/agent-config-audit) | [v0.3.0](https://github.com/basitalisandhu/agent-config-audit/releases/tag/v0.3.0) | 2026-10-16 |
| [agentic-semgrep-rules](https://github.com/basitalisandhu/agentic-semgrep-rules) | [v0.2.0](https://github.com/basitalisandhu/agentic-semgrep-rules/releases/tag/v0.2.0) | 2026-10-16 |
| [security-actions](https://github.com/basitalisandhu/security-actions) | [v0.2.0](https://github.com/basitalisandhu/security-actions/releases/tag/v0.2.0) | 2026-10-16 |
| [cc-hooks](https://github.com/basitalisandhu/cc-hooks) | [v0.1.2](https://github.com/basitalisandhu/cc-hooks/releases/tag/v0.1.2) | 2026-10-16 |
| [cc-plugin-lock](https://github.com/basitalisandhu/cc-plugin-lock) | [v0.3.0](https://github.com/basitalisandhu/cc-plugin-lock/releases/tag/v0.3.0) | 2026-10-16 |
| [claude-perm-sim](https://github.com/basitalisandhu/claude-perm-sim) | [v0.3.0](https://github.com/basitalisandhu/claude-perm-sim/releases/tag/v0.3.0) | 2026-10-16 |
| [llms-txt-gen](https://github.com/basitalisandhu/llms-txt-gen) | [v0.2.0](https://github.com/basitalisandhu/llms-txt-gen/releases/tag/v0.2.0) | 2026-10-09 |
| [scp-guardrails](https://github.com/basitalisandhu/scp-guardrails) | [v0.2.0](https://github.com/basitalisandhu/scp-guardrails/releases/tag/v0.2.0) | 2026-10-13 |
| [spotlighting](https://github.com/basitalisandhu/spotlighting) | [v0.3.0](https://github.com/basitalisandhu/spotlighting/releases/tag/v0.3.0) | 2026-10-16 |
| [ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents) | [v1.1.0](https://github.com/basitalisandhu/ai-agent-incidents/releases/tag/v1.1.0) | 2026-10-18 |
| [awesome-agent-security](https://github.com/basitalisandhu/awesome-agent-security) | [v0.1.0](https://github.com/basitalisandhu/awesome-agent-security/releases/tag/v0.1.0) | 2026-10-18 |
<!-- RELEASES:END -->

## Contact

- Questions, bugs and ideas: open an issue in that project's repository.
- Security problems: report them privately through the project's Security tab, as its `SECURITY.md` explains.
- Posts and project pages: [basitalisandhu.github.io](https://basitalisandhu.github.io/) ([RSS](https://basitalisandhu.github.io/feed.xml)).
