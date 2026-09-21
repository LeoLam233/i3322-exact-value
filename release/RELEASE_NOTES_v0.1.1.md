# v0.1.1 — Douglas citation and provenance correction

This is primarily a citation and provenance correction release. It does not modify the mathematical proof code or the frozen theorem/audit artifacts, and it does not alter or replace the existing v0.1.0 tag or release.

## Citation and provenance correction

The manuscript and repository now cite two previously omitted records by Seth Douglas:

- *A rigorously characterized I3322 quantum wall and finite-dimensional nonattainment*, Zenodo v1.0.0, DOI [10.5281/zenodo.21782009](https://doi.org/10.5281/zenodo.21782009), published 4 August 2026; and
- *The I3322 quantum value is attained spatially but not in finite dimension*, [arXiv:2609.05555](https://arxiv.org/abs/2609.05555).

The v1.0.0 Zenodo record contained the candidate constant and matching picture before the public release of this repository. The proof claims associated with that August release were subsequently withdrawn as proof claims; the numerical candidate was not thereby withdrawn. The present manuscript therefore does not claim priority for the earlier candidate or matching picture, and it does not treat the withdrawn proof attempt as having established the theorem claimed here. Its rigorous proof architecture and stated scope remain distinct.

We thank Seth Douglas for bringing this omission to our attention.

## Scope

The substantive changes in v0.1.1 are the added citations, the explicit historical/priority distinction above, aligned repository-level provenance language, refreshed release metadata, and the rebuilt public manuscript. No unrelated mathematical claim or proof-code change is included.

The repository release version is v0.1.1. The manuscript's pre-existing internal edition number remains v0.1.2 because v0.1.1 was already used in the preserved pre-publication manuscript/build-QA history; the rebuilt title page identifies this repository release explicitly so the two version namespaces are unambiguous.

## Next steps

The highest-priority technical follow-up is a self-contained public replay package for the uniqueness/O6 computation that runs from a clean checkout or directory without relying on Git history, hidden local files, or undocumented intermediate artifacts, with pinned or clearly specified dependencies, explicit commands, expected outputs or certificates, and verification hashes/manifests.

After that, we plan a more explicit independently replayable interval-arithmetic audit recording precision, rounding assumptions or mode, certified intervals, margins, and expected outputs. We will also audit each external premise and make every load-bearing use explicit, including where concavity of the relevant certificate is required, and investigate whether the finite-dimensional upper-bound component can be anchored to Pauwels's formally checked theorem where applicable rather than relying only on a single preprint source.

These follow-up tasks are not claimed as completed in v0.1.1, and no completion date is promised.
