# Check the mathematics displayed by GitHub

The hosted check compares the equations on commit-pinned GitHub pages with the exact Markdown source. It covers every tracked Markdown page at browser widths of 1440 and 760 pixels, including inline notation and formulas in tables. It checks expression counts, MathML structure, relation symbols, equation labels and display geometry. The [content contract](math-contract.json) adds explicit text requirements for the headline bounds and repaired expressions.

The workflow uses an anonymous browser and read-only repository permissions. It runs for pull requests from this repository and can also be started manually from the Actions page. Each run retains its report, source inventory, captured HTML and screenshots as a temporary review artifact. A passing automated check still requires visual inspection of representative equations, tables and navigation.

## Run locally

Use Node.js 18 or later, Python 3.10 or later, Git and a Chromium-capable environment with access to the public GitHub pages. Install the dependencies outside the source checkout:

```bash
npm install --prefix /tmp/purification-render-deps playwright@1.56.1 mathjax-full@3.2.1
/tmp/purification-render-deps/node_modules/.bin/playwright install chromium

NODE_PATH=/tmp/purification-render-deps/node_modules \
node verification/hosted/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Stabilizer-Purification-Thresholds \
  --revision FULL_COMMIT_SHA \
  --contract verification/hosted/math-contract.json \
  --output /tmp/purification-render-evidence
```

Replace `FULL_COMMIT_SHA` with the full 40-character identity of the public revision being reviewed. Use a new empty evidence directory for each attempt. The inventory reads that commit's Git objects, so uncommitted edits are outside its scope. The content contract must match the expressions in the checked revision.

The output `hosted-report.json` binds the source commit and tree to the captured pages, viewports and evidence hashes. An exit status of zero means the structural checks passed; a nonzero status records a failed comparison or an unavailable capture route. A local TeX compilation alone does not establish what GitHub displays.

## Review scope

Read the source alongside the screenshots. Inspect the principal result, substantial proof displays, the learning bridge and milestone map, table alignment, and any repaired expression. The current source uses fenced `math` displays, protected inline math, upright trace notation, and explicit inequality commands to preserve the intended content in GitHub's renderer.

These checks concern the displayed mathematics of one repository revision. The [scientific verification suite](../README.md) and the analytical proofs establish the separate mathematical claims. Future renderer behavior and other browsers require their own observations.
