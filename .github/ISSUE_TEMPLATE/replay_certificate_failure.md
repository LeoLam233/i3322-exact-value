---
name: "Replay or certificate failure"
about: "Report a reproducible verification failure"
title: "[replay] "
labels: ""
assignees: ""
---

Please provide a precise location and evidence. A general statement such as "the proof is wrong" without an identifiable step or supporting evidence cannot be investigated.

## Artifact and exact failure location
Release/tag, archive filename and SHA-256, extracted root, certificate/member identifier, stage and failing predicate:

## Reproduction
Exact command, interpreter/tool versions, operating system, fresh-extraction steps and exit code:

## Expected and actual result
Provide a minimal relevant log excerpt and expected result. State whether manifests passed and whether any file was changed. Remove private paths or secrets from newly supplied logs.

## Certificate evidence
For an arithmetic issue, include exact rational input/output and the containment or bound that fails. Identify whether the input occurs on the submitted proof path or is a synthetic helper case.

