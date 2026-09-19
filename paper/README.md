# Public manuscript v0.1.2

[Read the PDF](paper_v0_1_2.pdf). PDF SHA-256: `81b75cd3a720ab0e2953bdbd79f70c969af5fc48ab01caa75f4522b229f51f2f`.

The original sealed replay package `I3322_PAPER_V0_1_2.zip` has SHA-256 `1aa58a1d74f1aa130024196f4f537fcab293e7d78bab073d8432077348ee9905`. It contains the complete LaTeX/BibTeX source, PDF, build/render QA, replay wrapper and byte-preserved reproducibility archive. Because that embedded frozen provenance chain contains historical personal-email metadata in Git reflogs, the sealed replay package is retained privately rather than uploaded to the public GitHub Release. The readable source tree here and `paper_v0_1_2.pdf` are the public manuscript surfaces.

This is a metadata/declaration successor to v0.1.1: approved author/affiliation/email, PDF author/title metadata, the version label, and Funding/Competing interests declarations are finalized. Acknowledgements are deferred. **MATHEMATICAL CONTENT CHANGED: NO.** All other TeX/BibTeX files are byte-identical. The mathematical portions of the two edited files and every long numerical string are unchanged. No theorem, proof argument, external-premise scope, audit caveat or validation claim changed.

Author: Dehao Lin; School of Physics, Sun Yat-sen University, Guangzhou, China; lindh9@mail2.sysu.edu.cn. No ORCID is supplied and no AI system is an author. See [authorship](../AUTHORSHIP.md) and the unchanged [AI assistance disclosure](AI_ASSISTANCE_DISCLOSURE.md).

The new offline build exited 0 using pdfTeX 1.40.25 (TeX Live 2023/Debian), BibTeX and two final LaTeX passes. It has 33 pages, zero undefined references/citations, zero fatal LaTeX errors and no substantial overfull boxes. One 0.23207 pt overfull hbox is recorded; all 33 pages were visually reviewed without clipping or overlap. Exact long numerical strings were checked in both source and PDF.

## Build from the readable source tree

With CPython 3.10+, a local LaTeX engine and BibTeX, run from the repository root:

```sh
python -B paper/tools/build_paper.py --output ../i3322-paper-build/paper_v0_1_2.pdf
```

The byte-preserved helper disables shell escape and writes PDF/log outside this source tree. Its historical default filename is superseded by the explicit output above. It installs nothing. Byte-identical PDFs across toolchains are not promised. Full mathematical replay requires the privately retained sealed reviewer asset, as described in [REPRODUCE.md](../REPRODUCE.md).

The v0.1.1 package/PDF hashes are retained as historical build-QA provenance in [PROJECT_HISTORY.md](../docs/PROJECT_HISTORY.md). The historical ZIP is privacy-withheld; the old PDF may be retained privately. Those hashes are not the current public paper identity. Historical build notes inside old seals are not current build status. Owner-authored manuscript/prose is CC BY 4.0; embedded third-party and pre-existing frozen artifacts retain their existing notices/rights under the [license map](../LICENSE).
