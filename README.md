# Muhammad Basit Ali

**Software engineer working on AI agent security. I build open-source trust infrastructure for AI agents: who they are, what they may touch, and proof of what they did.**

In one sentence each: [Masoon Broker](https://basitalisandhu.github.io/masoon/masoon-broker.html) is a credential broker that keeps API keys out of AI agents and adds per-action approvals, a kill switch and a tamper-evident audit log (TypeScript; the commercial component, in private beta). [llm-agent-control-plane](https://github.com/basitalisandhu/llm-agent-control-plane) is a deterministic policy enforcement point for LLM agents, with no model on the decision path, evaluated on AgentDojo (Python, Apache-2.0). [ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents) is an open dataset of AI agent and LLM security incidents mapped to OWASP and MITRE ATLAS (CC BY 4.0). [agentic-semgrep-rules](https://github.com/basitalisandhu/agentic-semgrep-rules) is a Semgrep rule pack for insecure AI agent code (MIT). [agent-threat-model](https://github.com/basitalisandhu/agent-threat-model) is a CLI that turns a YAML description of an agent system into a STRIDE and OWASP Agentic threat model (Python, MIT). [agent-security-skills](https://github.com/basitalisandhu/agent-security-skills) is a Claude Code security plugin and skill pack for agent security reviews (MIT). [masoon](https://github.com/basitalisandhu/masoon) is the front door that ties them together, with a [docs site](https://basitalisandhu.github.io/masoon/) and a [machine-readable summary](https://basitalisandhu.github.io/masoon/llms.txt).

Most of that work ships under one umbrella, [Masoon](https://github.com/basitalisandhu/masoon) ([docs](https://basitalisandhu.github.io/masoon/)): a credential broker for AI agents, a deterministic policy layer for LLM agents, a public dataset of AI agent security incidents, and the tooling that turns the dataset into Semgrep rules, threat models and code reviews. It is for teams that run agents against real APIs, MCP servers and codebases and need least privilege, human approvals and an audit trail without putting another model in the loop.

## What I build

**Security Automation**
Controls that run in CI and at runtime without waiting for a human: Semgrep rule packs, reusable GitHub Actions security workflows, and brokers that issue credentials per action instead of per deployment.

**AI**
Agent tooling that makes security work measurable: evaluation harnesses on public benchmarks, structured datasets with schemas, and skills that fit into the editors and agents people already use.

**AI Security**
The core. Authorization, provenance and audit for LLM agents, built so that no model sits in the enforcement path and every decision can be replayed from the log.

## Start here if you are looking for

- **A credential broker for AI agents** that keeps API keys out of the agent and adds human approvals and a kill switch: [Masoon Broker](https://basitalisandhu.github.io/masoon/masoon-broker.html).
- **Prompt injection defence for tool-using LLM agents** that is deterministic and evaluated on AgentDojo: [llm-agent-control-plane](https://github.com/basitalisandhu/llm-agent-control-plane).
- **A dataset of AI agent security incidents** mapped to OWASP and MITRE ATLAS: [ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents) ([browse it](https://basitalisandhu.github.io/ai-agent-incidents/)).
- **Threat modeling for AI agents** from a YAML description, with STRIDE and OWASP Agentic output: [agent-threat-model](https://github.com/basitalisandhu/agent-threat-model).
- **Semgrep rules for AI agent code** and **a Claude Code security plugin**: [agentic-semgrep-rules](https://github.com/basitalisandhu/agentic-semgrep-rules) and [agent-security-skills](https://github.com/basitalisandhu/agent-security-skills).

## Featured

| Project | What it is |
|---|---|
| [Masoon Broker](https://basitalisandhu.github.io/masoon/masoon-broker.html) | Scoped, short-lived, per-action credentials for AI agents with human approvals, kill switch and hash-chained audit log. Commercial component, private beta. |
| [llm-agent-control-plane](https://github.com/basitalisandhu/llm-agent-control-plane) | Deterministic policy enforcement point for LLM agents (provenance + approval rules), evaluated on AgentDojo, with an 80-event incident dataset. Apache-2.0 / CC BY 4.0. |
| [ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents) | Open, structured dataset of publicly documented AI-agent security incidents: JSON + schema, mapped to OWASP and MITRE ATLAS, with a [browsable site](https://basitalisandhu.github.io/ai-agent-incidents/). |
| [agentic-semgrep-rules](https://github.com/basitalisandhu/agentic-semgrep-rules) | Semgrep rule pack for insecure agent code: unbounded tool permissions, eval of model output, SSRF through tool URLs, prompt interpolation, MCP servers without auth. |
| [agent-threat-model](https://github.com/basitalisandhu/agent-threat-model) | CLI that turns a YAML description of an agent system into a STRIDE + OWASP Agentic threat model, control checklist and Mermaid diagram. |
| [agent-security-skills](https://github.com/basitalisandhu/agent-security-skills) | Claude Code plugin and agentskills-compatible skill pack for agent security reviews: threat modelling, config audits, policy generation, incident lookup. |
| [masoon](https://github.com/basitalisandhu/masoon) | Platform overview and front door: architecture, components, design principles and roadmap, with a [docs site](https://basitalisandhu.github.io/masoon/). |

### Latest releases

<!-- RELEASES:START -->
| Project | Latest release | Published |
|---|---|---|
| [llm-agent-control-plane](https://github.com/basitalisandhu/llm-agent-control-plane) | no public release yet | |
| [ai-agent-incidents](https://github.com/basitalisandhu/ai-agent-incidents) | no public release yet | |
| [agentic-semgrep-rules](https://github.com/basitalisandhu/agentic-semgrep-rules) | no public release yet | |
| [agent-threat-model](https://github.com/basitalisandhu/agent-threat-model) | no public release yet | |
| [agent-security-skills](https://github.com/basitalisandhu/agent-security-skills) | no public release yet | |
| [masoon](https://github.com/basitalisandhu/masoon) | no public release yet | |
<!-- RELEASES:END -->

## Research

**AI as Weapon, Target, and Surface: A Threat Taxonomy and a Deterministic Control Plane for Securing LLM Agents** (2026). Code, policies, evaluation and the incident dataset live in [llm-agent-control-plane](https://github.com/basitalisandhu/llm-agent-control-plane).

## How I work

- **Deterministic controls over vibes.** Policy is code that returns the same answer for the same input. A model may advise; it never decides.
- **Evidence.** Hash-chained audit logs, tests, results on public benchmarks, and datasets anyone can inspect and challenge.
- **Practice what I preach.** CodeQL, OpenSSF Scorecard, a shared [security policy and CI baseline](https://github.com/basitalisandhu/.github), and docs that say what the code does not protect against.

## Now

Hardening `masoon-broker` and `llm-agent-control-plane` for people other than me, moving the incident dataset into its own repo with a browsable site, and publishing the Semgrep rule pack. After that: the threat-model CLI and the review skill pack. Open to conversations about agent safety and AI security engineering.

## Contact

- GitHub: [@basitalisandhu](https://github.com/basitalisandhu)
<!-- - LinkedIn: https://www.linkedin.com/in/<handle> -->
<!-- - X: https://x.com/<handle> -->
<!-- - Email: <address> -->

<p>
  <img src="https://github-readme-stats.vercel.app/api?username=basitalisandhu&show_icons=true&hide_border=true&theme=default" alt="GitHub stats" height="150" />
  <img src="https://streak-stats.demolab.com?user=basitalisandhu&hide_border=true&theme=default" alt="Contribution streak" height="150" />
</p>
