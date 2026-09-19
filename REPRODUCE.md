# Reproduce and inspect the result

Use **CPython 3.10 or later**, with Python optimization disabled. The public repository supports complete static/source inspection and verification of the privacy-filtered public Release. Full frozen replay additionally requires the byte-identical **private full reviewer asset package**, because the canonical theorem seal and replay-paper package contain immutable historical Git reflogs with an unrelated personal email address and are not uploaded publicly.

## Public verification

From the repository root:

```sh
python -B tools/verify_hashes.py --ignore-git
python -B tools/verify_repository.py
```

If running from a ZIP extraction rather than a Git checkout, `--ignore-git` may be omitted.

After extracting `I3322_GITHUB_V0_1_0_PUBLIC_RELEASE_ASSETS.zip` beside the repository:

```sh
python -B tools/verify_release_assets.py \
  --assets-dir ../I3322_GITHUB_V0_1_0_PUBLIC_RELEASE_ASSETS
```

This checks the complete public asset inventory against `release/SHA256SUMS`. It does **not** claim to replay the privately retained canonical theorem seal.

## Build the public manuscript from readable source

```sh
python -B paper/tools/build_paper.py --output ../i3322-paper-build/paper_v0_1_2.pdf
```

The published PDF SHA-256 is `81b75cd3a720ab0e2953bdbd79f70c969af5fc48ab01caa75f4522b229f51f2f`. Byte-identical PDFs across LaTeX toolchains are not promised.

## Full frozen replay for reviewers

The owner retains the byte-identical earlier full reviewer asset tree/ZIP. Its outer ZIP SHA-256 is:

```text
93ac17e3d1471a8d74f5f88f9029b9852c2d221f70b13ecd6fb00bc606d28598
```

That package contains the canonical theorem archive `01_FINAL_CLEAN_EXACT_VALUE_CLOSURE_e592.zip` and the complete `I3322_PAPER_V0_1_2.zip`. Before replay, verify the extracted tree against `release/PRIVATE_REVIEW_SHA256SUMS`:

```sh
python -B tools/verify_release_assets.py \
  --assets-dir ../I3322_GITHUB_V0_1_0_RELEASE_ASSETS \
  --private-review
```

Then run:

```sh
python -B machine/replay.py \
  --assets-dir ../I3322_GITHUB_V0_1_0_RELEASE_ASSETS \
  --work-dir ../i3322-integration-replay

python -B machine/replay.py \
  --assets-dir ../I3322_GITHUB_V0_1_0_RELEASE_ASSETS \
  --full \
  --work-dir ../i3322-full-replay
```

The work directory must be fresh and outside repository/assets. Full mode executes integration, integration mutations, R0, R1, O1–O5 and the surviving O6 branch; the rejected Sol branch is never consumed as proof authority. The historical 107,716,343-operation observer audit is authenticated in the record but is not rerun by this wrapper.

The privacy withholding is a transport/publication decision only. The original theorem, certificate and audit hashes are unchanged. See [sealed-artifact privacy](release/SEALED_ARTIFACT_PRIVACY.md), [machine/analytic boundary](proof/MACHINE_ANALYTIC_BOUNDARY.md), and [limitations](LIMITATIONS.md).
