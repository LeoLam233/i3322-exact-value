# i3322-exact-value

Proof-carrying research candidate, repository release v0.1.1, for external human review.

**Canonical repository:** https://github.com/LeoLam233/i3322-exact-value

**The frozen theorem characterizes the I3322 supremum over binary projective measurements on arbitrary finite-dimensional tensor products, with no fixed bound on local dimension.** It proves `S_t = s_*`, where `s_*` is the unique parameter in `I = (0.2508753845139765, 0.2508753855]` admitting an intrinsic full-state match. Equivalently, it is the unique zero of `Rcal(a(s))` on `I`, with the analytic residual defined in [the scalar definition](proof/SCALAR_DEFINITION.md).

The rigorous strict rational enclosure is:

```text
0.250875384513976535617336610945951298901321973971476246796391973158622991323050603025506260
  < S_t <
0.250875384513976535617336610945951298901321973971476707728748045068866376435770152964357102
```

Its exact width is `4.60932356071910243385112719549938850842E-52`. “Exact” refers to the structural unique-root characterization and certified enclosure; neither endpoint is the value and no elementary closed form is claimed. **There is no commuting=tensor equality or R2 claim.**

**Validation:** O1–O5 is CLOSED-PASS. O6 and the final integrated audit are OPEN-MINOR; the theorem survives with the genuine, unpatched, non-load-bearing M001 midpoint-helper defect. Source provenance is OPEN-MINOR, with complete R1 generation ancestry unresolved. **Complete external expert human validation of the theorem has not yet occurred, and journal peer review has not yet occurred.** See [limitations](LIMITATIONS.md) and [validation status](docs/VALIDATION_STATUS.md).

## v0.1.1 citation and provenance correction

This release corrects an omission in the original public manuscript and repository. Seth Douglas's [v1.0.0 Zenodo record](https://doi.org/10.5281/zenodo.21782009) contained the candidate constant and matching picture before this work was published; his later paper is [arXiv:2609.05555](https://arxiv.org/abs/2609.05555). The proof claims associated with the August v1.0.0 release were subsequently withdrawn as proof claims. The present manuscript therefore does not claim priority for those earlier observations, while its claimed rigorous theorem and proof architecture remain distinct. We thank Seth Douglas for bringing the missing citation and provenance issue to our attention.

## Start here

1. [Paper v0.1.2 (PDF)](paper/paper_v0_1_2.pdf) and [paper source/build guide](paper/README.md).
2. [Exact theorem and nonclaims](THEOREM.md).
3. [Skeptical audit entry point](AUDIT_ME_FIRST.md).
4. [Reproduce the checks](REPRODUCE.md).
5. [Authority and provenance](PROVENANCE.md).
6. [Project history and changing evidence status](docs/PROJECT_HISTORY.md).
7. [Human and AI contributions and responsibility](CONTRIBUTORS.md).

## Verify the candidate

From the repository root, with CPython 3.10 or later:

```sh
python -B tools/verify_hashes.py
python -B tools/verify_repository.py
```

For a Git checkout, add `--ignore-git` to the first command. A clone contains the readable sources and small helpers. Public GitHub Release assets are intentionally privacy-filtered; the canonical theorem seal and the original full replay paper package are not placed in the public Release because immutable nested Git reflogs contain an unrelated historical personal email address. Their SHA-256 identities remain published, and the byte-identical full reviewer package is retained privately for direct reviewer access. See [release assets](release/RELEASE_ASSETS.md) and [sealed-artifact privacy](release/SEALED_ARTIFACT_PRIVACY.md).

The [proof graph](proof/DEPENDENCY_GRAPH.md), [external premises](proof/EXTERNAL_PREMISES.md), and [machine/analytic boundary](proof/MACHINE_ANALYTIC_BOUNDARY.md) explain what replay establishes. Hashes authenticate bytes; they do not establish mathematical truth. Agreement among AI runs sharing external premises is not independent evidence.

**Author:** Dehao Lin; School of Physics, Sun Yat-sen University, Guangzhou, China; lindh9@mail2.sysu.edu.cn. [Authorship and declarations](AUTHORSHIP.md) are finalized; Funding and Competing interests appear in manuscript v0.1.2. Formal acknowledgements are deferred to a later manuscript revision. No AI system is an author.

Owner-authored code is MIT licensed; owner-authored manuscript/prose/documentation is CC BY 4.0. The [license map](LICENSE) and [third-party notices](THIRD_PARTY_NOTICES.md) explicitly exclude pre-existing frozen/sealed artifacts and third-party material from blanket grants.

Sealed historical archives retain inherited workstation/build paths under the owner-approved disclosure; their validation custody hashes are preserved. A later recursive privacy sweep also found a historical personal email in immutable Git reflogs inside some frozen archives; those affected archives are therefore withheld from the public GitHub Release rather than modified. See [sealed-artifact privacy](release/SEALED_ARTIFACT_PRIVACY.md). No arXiv submission or journal peer review is claimed by v0.1.1.
