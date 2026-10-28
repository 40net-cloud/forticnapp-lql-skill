# FortiCNAPP LQL Skill

This repository hosts a [Claude Code skill](https://docs.claude.com/en/docs/claude-code) for authoring **Lacework FortiCNAPP LQL queries and custom policies** — for example, turning compliance-standard controls (CIS Microsoft Azure Foundations Benchmark, CIS AWS Foundations, …) into FortiCNAPP violation policies.

The skill condenses the ~239-page FortiCNAPP LQL Reference Guide (~90K tokens raw) into a small always-loaded core plus grep-targeted reference files, so an LLM session pays only for what it actually needs (typically ~2K tokens instead of the full guide).

## Layout

```
skills/forticnapp-lql/
├── SKILL.md                        # hand-written core: query anatomy, policy
│                                   #   constraints, workflow, policy YAML template
├── guide-version.json              # source of truth: which guide version references/ is built from
└── references/                     # generated from the online docs
    ├── syntax.md                   # grammar, joins, policy-eval limits
    ├── query-types.md              # single / join / semi-join
    ├── operators.md                # all LQL operators
    ├── functions.md                # all LQL functions
    ├── examples.md                 # 15 worked example queries
    ├── datasources-index.md        # file -> service range map (generated)
    ├── datasources-aws-config-*.md # LW_CFG_AWS_*, alphabetical chunks (~6K tokens each)
    ├── datasources-aws-cloudtrail.md
    ├── datasources-azure-*.md      # LW_CFG_AZURE_*, chunked
    ├── datasources-gcp-config-*.md # LW_CFG_GCP_*, chunked
    ├── datasources-gcp-audit.md
    ├── datasources-oci.md          # LW_CFG_OCI_*
    ├── datasources-workload.md     # LW_HA_*/LW_HE_*
    ├── datasources-attackpath.md   # LW_APA_*
    └── datasources-entitlements.md # LW_CE_*
scripts/
└── generate_references.py          # regenerates references/ from docs.fortinet.com (run with uv)
.github/workflows/
└── refresh-lql-skill.yml           # weekly version check -> regenerate -> open PR
pyproject.toml                      # dependency set for the regenerate script
```

## Installation

**Claude Code plugin marketplace (recommended)** — updates arrive with `/plugin marketplace update`:

```
/plugin marketplace add 40net-cloud/forticnapp-lql-skill
/plugin install forticnapp-lql@forticnapp-lql-skill
```

**Release download** — grab `forticnapp-lql-<tag>.zip` from the [Releases](../../releases) page and unzip it into `~/.claude/skills/` (personal) or `<project>/.claude/skills/` (per project). The same zip can be uploaded in Claude.ai under Settings → Capabilities → Skills.

**Clone** — the skill auto-activates in any Claude Code session opened in this repo.

## Releasing

1. Bump `version` in `.claude-plugin/plugin.json`, commit.
2. `git tag vX.Y.Z && git push origin vX.Y.Z`

`.github/workflows/release.yml` fails if the tag and `plugin.json` version disagree, then publishes a GitHub release with the zip and tar.gz.

### Release information

- **Packaging:** the release assets contain only `skills/forticnapp-lql/` (the `forticnapp-lql/` folder sits at the archive root), so they work for `~/.claude/skills/`, project `.claude/skills/`, and the Claude.ai skill upload.
- **Marketplace manifests:** `.claude-plugin/plugin.json` describes the plugin and `.claude-plugin/marketplace.json` makes this repo its own marketplace (`source: "./"`; the plugin's skills are picked up from `skills/`). Keep `name` in both files in sync with the skill folder name.
- **Versioning:** the plugin version (`plugin.json`) is independent of the FortiCNAPP guide version (`skills/forticnapp-lql/guide-version.json`). Each release note states which guide version it was built from. Merging a weekly refresh PR does not publish a release; bump the version and tag when you want to ship it.
- **Other agents:** the skill is plain markdown (`SKILL.md` plus `references/`), so any tool that reads the Agent Skills format can use the release zip. Tools with their own rules-file formats (e.g. Cursor) would need a separate conversion.
- **Official directory:** the self-hosted marketplace works without approval. The plugin can also be submitted to Anthropic's plugin directory.
- **Disclaimer:** this is an unofficial, community project and is not affiliated with or endorsed by Fortinet. The reference files are derived from Fortinet's public documentation.
- **License:** no `LICENSE` file has been added yet. Add one before encouraging reuse, and check Fortinet's documentation terms for the generated reference content.

## Source of truth

The reference files are **generated** from the official HTML guide:

- Base URL: <https://docs.fortinet.com/document/forticnapp/latest/lql-reference/598361/lql-overview>
- The guide version the skill is built from lives in **`skills/forticnapp-lql/guide-version.json`**
  (`version` + `fetched` date). This is the single source of truth: `generate_references.py`
  rewrites it on every run, and the refresh workflow reads it to decide whether to regenerate.
  Each generated file also carries a provenance comment with its exact source URLs and fetch date.

The policy-wrapper section of `SKILL.md` additionally draws on [Create Policies with the CLI](https://docs.fortinet.com/document/lacework-forticnapp/latest/cli-reference/564847/create-policies-with-the-cli).

## Updating the skill

### Automated (GitHub Actions)

`.github/workflows/refresh-lql-skill.yml` runs every Monday. It compares the guide
version published on docs.fortinet.com with `skills/forticnapp-lql/guide-version.json`;
if they differ it regenerates the reference files (the script also rewrites
`guide-version.json`) and opens a pull request labelled `automation` with a review
checklist. Run it on demand from the **Actions** tab — use the **force** input to
regenerate even when the version is unchanged (catches content-only updates such as
new datasources).

The workflow never touches `SKILL.md` or `README.md`; those steps below stay
manual and are listed in the PR body.

### Manual

1. Regenerate the reference files. This needs [`uv`](https://docs.astral.sh/uv/) and `curl` on
   your `PATH`; `uv` resolves `beautifulsoup4` and `markdownify` automatically from
   `pyproject.toml` (also declared inline in the script via PEP 723), so there is no
   virtualenv to create or activate:

   ```sh
   uv run scripts/generate_references.py                  # detect + stamp the live guide version
   uv run scripts/generate_references.py --version 26.3   # or stamp an explicit version
   ```

   The script is also directly executable (`./scripts/generate_references.py`) thanks to
   its `uv run --script` shebang. `--print-remote-version` prints the version detected on
   docs.fortinet.com without regenerating anything. Every regeneration rewrites
   `skills/forticnapp-lql/guide-version.json` (`version` + `fetched` date) — commit it
   alongside the `references/` changes.

2. Review the script's output for `WARNING` lines — they mean the guide gained a new top-level datasource section or changed structure (add new sections to `DATASOURCE_GROUPS`; chunk filenames may change when services are added — that's expected), or that a known-errata patch in `fix_functions_errata` no longer matches (the guide fixed it upstream — drop that patch).

3. `git diff` the `references/` files. Most updates only add datasources and need nothing further. If the diff touches **syntax, operators, query types, or the policy-evaluation limitations**, update the hand-written `SKILL.md` to match (it summarizes those rules and is *not* regenerated).

4. Spot-check quality:
   - No raw `\_` escapes, `| --- |` table separators, or `[text](url)` links in the generated files (the cleaner should have handled them).
   - `grep -i -A5 '^### <SomeService>' skills/forticnapp-lql/references/datasources-azure-a-h.md` returns a sensible datasource list.
   - Example query YAML blocks in `examples.md` are intact.
   - `skills/forticnapp-lql/guide-version.json` shows the new `version` / `fetched` date.

## Maintenance notes

- **`SKILL.md` is hand-maintained** — never overwrite it with generated content. Keep it small (~2K tokens); anything bulky belongs in `references/`.
- **The datasource files are meant to be grepped**, not fully loaded (AWS config alone is ~32K tokens; the script splits each large section into ≤~6K-token chunks via `MAX_CHUNK_CHARS`). `SKILL.md` instructs the model accordingly; preserve that guidance when editing.
- **Known gap (by design):** the guide does not document the JSON schema inside `RESOURCE_CONFIG`. The skill's workflow tells the model to verify field names via the underlying cloud provider API (each datasource maps to a named API call), `lacework query show-source`/`preview-source`, or an explore query returning bare `RESOURCE_CONFIG`. Do not "fix" this by guessing schemas into the reference files.
- **Validating a change:** the cheapest end-to-end test is to open a Claude Code session in a scratch project containing the skill and ask it to draft a policy for one CIS control per provider, then check the chosen datasource names exist and the query respects the policy-evaluation constraints (`return distinct` + root-datasource-only columns when `array_to_rows` or MANY-cardinality joins are used).

## License

[License](/../../blob/main/LICENSE) © Fortinet Technologies. All rights reserved.
