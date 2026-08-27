# FortiCNAPP LQL Skill

This repository hosts a [Claude Code skill](https://docs.claude.com/en/docs/claude-code) for authoring **Lacework FortiCNAPP LQL queries and custom policies** — for example, turning compliance-standard controls (CIS Microsoft Azure Foundations Benchmark, CIS AWS Foundations, …) into FortiCNAPP violation policies.

The skill condenses the ~239-page FortiCNAPP LQL Reference Guide (~90K tokens raw) into a small always-loaded core plus grep-targeted reference files, so an LLM session pays only for what it actually needs (typically ~2K tokens instead of the full guide).

## Layout

```
.claude/skills/forticnapp-lql/
├── SKILL.md                        # hand-written core: query anatomy, policy
│                                   #   constraints, workflow, policy YAML template
└── references/                     # generated from the online docs
    ├── syntax.md                   # grammar, joins, operators, policy-eval limits
    ├── functions.md                # all LQL functions
    ├── examples.md                 # 15 worked example queries
    ├── datasources-aws.md          # LW_CFG_AWS_* + CloudTrail (grep, don't read!)
    ├── datasources-azure.md        # LW_CFG_AZURE_* (Resource Graph + Azure AD)
    ├── datasources-gcp.md          # LW_CFG_GCP_* + audit log activity
    ├── datasources-oci.md          # LW_CFG_OCI_*
    └── datasources-agent-k8s.md    # LW_HA_*/LW_HE_*/LW_APA_*/LW_CE_* with fields
scripts/
└── generate_references.py          # regenerates references/ from docs.fortinet.com
FortiCNAPP-LQL_Reference_Guide.pdf  # offline fallback copy of the guide (26.2)
```

The skill auto-activates in any Claude Code session opened in this repo. To use it in other projects, copy `.claude/skills/forticnapp-lql/` into that project's `.claude/skills/`, or into `~/.claude/skills/` to make it personal/global.

## Source of truth

The reference files are **generated** from the official HTML guide:

- Base URL: <https://docs.fortinet.com/document/forticnapp/latest/lql-reference/598361/lql-overview>
- Current generation: guide version **26.2**, fetched **2026-08-26** (each file carries a provenance comment with its exact source URLs and fetch date).

The policy-wrapper section of `SKILL.md` additionally draws on [Create Policies with the CLI](https://docs.fortinet.com/document/lacework-forticnapp/latest/cli-reference/564847/create-policies-with-the-cli).

The local PDF is a point-in-time offline copy; the HTML guide is the source of truth for updates (Fortinet updates it roughly monthly per its change log — mostly new datasources).

## Updating the skill

1. Regenerate the reference files (needs Python 3 with `beautifulsoup4` and `markdownify`, plus `curl`):

   ```sh
   pip install beautifulsoup4 markdownify
   python3 scripts/generate_references.py --version 26.3   # stamp the new guide version
   ```

2. Review the script's output for `WARNING` lines — they mean the guide gained a new top-level datasource section or changed structure; add new sections to `DATASOURCE_GROUPS` in the script.

3. `git diff` the `references/` files. Most updates only add datasources and need nothing further. If the diff touches **syntax, operators, query types, or the policy-evaluation limitations**, update the hand-written `SKILL.md` to match (it summarizes those rules and is *not* regenerated).

4. Spot-check quality:
   - No raw `\_` escapes, `| --- |` table separators, or `[text](url)` links in the generated files (the cleaner should have handled them).
   - `grep -i -A5 '^### <SomeService>' .claude/skills/forticnapp-lql/references/datasources-azure.md` returns a sensible datasource list.
   - Example query YAML blocks in `examples.md` are intact.

5. Optionally refresh the offline PDF and update the version/date in this README.

## Maintenance notes

- **`SKILL.md` is hand-maintained** — never overwrite it with generated content. Keep it small (~2K tokens); anything bulky belongs in `references/`.
- **The datasource files are meant to be grepped**, not fully loaded (`datasources-aws.md` alone is ~32K tokens). `SKILL.md` instructs the model accordingly; preserve that guidance when editing.
- **Known gap (by design):** the guide does not document the JSON schema inside `RESOURCE_CONFIG`. The skill's workflow tells the model to verify field names via the underlying cloud provider API (each datasource maps to a named API call), `lacework query show-source`/`preview-source`, or an explore query returning bare `RESOURCE_CONFIG`. Do not "fix" this by guessing schemas into the reference files.
- **Validating a change:** the cheapest end-to-end test is to open a Claude Code session in a scratch project containing the skill and ask it to draft a policy for one CIS control per provider, then check the chosen datasource names exist and the query respects the policy-evaluation constraints (`return distinct` + root-datasource-only columns when `array_to_rows` or MANY-cardinality joins are used).
