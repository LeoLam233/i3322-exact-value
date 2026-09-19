# Sol O6: reproducible arithmetic failure

**REJECTED — NOT THEOREM AUTHORITY.**

| Evidence | SHA-256 |
|---|---|
| Clean Sol recertification, asset 06 | `e4521901d521d3c4c93e04784a2e178ca410896ee291e5a899e82db27ed85a95` |
| Rejecting hostile arithmetic audit, asset 07 | `01ee95689ac0991962161a2398b414269e830a3a08abaabdc11b0fab5d1473a0` |

The proof was a clean recertification attempt. Its own README claimed PASS, and the hostile audit reran the unmodified one-command replay successfully. Those claims remain frozen historical evidence, not the current acceptance status.

The decisive finding **F001** is a false square-root enclosure. At precision 180, the integer square-root step produces a scaled integer that may have 181 digits. Scaling it back with ordinary nearest-context Decimal arithmetic can move the intended lower bound upward or the upper bound downward. For `dec_sqrt_bounds(2)`, both returned endpoints equal `b` although exact rational arithmetic gives `b² > 2`. The same containment failure occurs on actual full-parameter multiplier-discriminant inputs. The audit reports eight of nine tests failing. This is an exact breach of the enclosure specification, not a judgment about too few displayed digits.

A separate rounding finding, named **M001 in the rejected audit**, concerns direct nearest-rounded powers, sums, quotients and derivative radii in `local_certificate.py`. Exact rational substitution shows a sufficient phase-derivative upper bound and a reported radius falling below their defining expressions. This rejected-branch M001 is distinct from the surviving Astra branch's midpoint-helper M001; finding identifiers are local to their audit.

The rejected audit also records minor centered-domain and malformed-tree issues. Its root receipt's width and placement can be arithmetically correct while its enclosure remains unproved. Diagnostic recomputations were explicitly conditional and were not accepted as a replacement proof.

The arithmetic foundation feeds coefficient generation and local/global interval stages. A reproduced PASS cannot make inward-rounded intervals outward. The audit found no second matching parameter and did not establish that O6 itself is false; it established that this submitted proof does not rigorously certify its load-bearing claims.

Sources: asset 06 `build/I3322_O6_CLEAN_RECERTIFICATION/README.md` and `src/interval.py`; asset 07 `AUDIT_VERDICT.md`, `IMPLEMENTATION_AUDIT.md`, `ROOT_AUDIT.md`, `FINDINGS.json` and its exact arithmetic probes. This assembly does not patch or rerun the rejected branch and never consumes its root or PASS as canonical evidence.
