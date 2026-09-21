# v0.1.1 — Citation and provenance correction

This is primarily a citation and provenance correction release. It does not modify the mathematical proof code or the frozen theorem/audit artifacts, and it does not alter or replace the existing v0.1.0 tag or release.

## Citation and provenance correction

The manuscript and repository now cite two previously omitted records by Seth Douglas:

- *A rigorously characterized I3322 quantum wall and finite-dimensional nonattainment*, Zenodo v1.0.0, DOI [10.5281/zenodo.21782009](https://doi.org/10.5281/zenodo.21782009); and
- *The I3322 quantum value is attained spatially but not in finite dimension*, [arXiv:2609.05555](https://arxiv.org/abs/2609.05555).

The earlier v1.0.0 Zenodo record already contained the numerical candidate and matching picture. We have revised the manuscript to credit these antecedents explicitly and do not claim priority for either of them. The associated August proof claim was later withdrawn, while the numerical candidate and matching picture remained part of the public record. The contribution of the present manuscript is the proof developed here.

We thank Seth Douglas for bringing this omission to our attention.

## Scope

The substantive changes in v0.1.1 are the added citations, the clarified historical and priority attribution, aligned repository-level provenance language, refreshed release metadata, and the rebuilt public manuscript. No unrelated mathematical claim or proof-code change is included.

The repository release version is v0.1.1. The manuscript retains its existing internal edition number v0.1.2 because v0.1.1 was already used in the preserved pre-publication manuscript/build-QA history. The rebuilt title page identifies the repository release separately so that the two version namespaces remain unambiguous.

The final prerelease editorial pass removed unnecessarily defensive provenance wording and clarified that complete external expert human validation of the theorem has not yet occurred. Before that pass, the prerelease tag pointed to commit `b5cc876a7f2bd596309b27c15a07d2f381173c19`; v0.1.0 and the sealed theorem/audit artifacts remain unchanged.

## Next steps

Our immediate technical priority is a self-contained public replay package for the uniqueness/O6 computation, runnable from a clean checkout or directory without reliance on Git history, hidden local files, or undocumented intermediate artifacts, with clearly specified dependencies, explicit commands, expected outputs or certificates, and verification hashes or manifests.

We then plan to make the interval-arithmetic verification independently replayable, with its numerical assumptions, certified intervals, margins, and expected outputs stated explicitly. We will also audit the external premises individually, including the load-bearing use of certificate concavity and whether the finite-dimensional upper-bound component can be anchored to Pauwels's formally checked theorem where applicable.

These items are ongoing and are not part of v0.1.1.
