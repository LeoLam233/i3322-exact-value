# Minimal replay entry point

This directory contains only the repository wrapper, [replay.py](replay.py), and [exact frozen source locators](FROZEN_PATHS.md). The certificate algorithms remain inside the unchanged sealed private reviewer assets; privacy-filtered public Release assets do not contain the canonical theorem/replay seal. No rejected source code, historical numeric seed or certificate replacement is installed here.

Follow [REPRODUCE.md](../REPRODUCE.md) for repository checks, integration and full replay. The wrapper is a reviewer-only full replay entry point. It verifies the private reviewer manifest, extracts `I3322_PAPER_V0_1_2.zip` into a fresh external work directory, and invokes its original `tools/replay_frozen.py`, adding `--full` only when requested. The original wrapper selects its pinned clean closure and canonical components. Release-asset hashing does not turn the rejected artifact into a premise.

All helper acceptance checks raise explicitly on failure. Python `-B` prevents cache creation in the sealed repository; no optimization flag should be used for proof replay. The helpers are assembly infrastructure, not a new mathematical certificate implementation. Their checks do not patch M001, enlarge theorem scope, or replace an analytic proof.
