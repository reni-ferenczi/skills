# ScribeOptions

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 28 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeOptions.h` | C++ | 54 |

## Overview

[[[PROSE overview unit=scribe/ScribeOptions tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEOPTIONS_H` | macro | `None` | — |
| `TRACK` | variable | `unsigned int` | Objects are \*not\* tracked by default - use this option to request tracking on an object... |
| `EXCLUSIVE_OWNER` | variable | `unsigned int` | A pointer can optionally specify that it exclusively owns the pointed-to object (only applies to pointers)... |
| `SHARED_OWNER` | variable | `unsigned int` | A pointer can optionally specify that it shares ownership of the pointed-to object with other pointers (only applies to pointers)... |

## Notes

[[[PROSE notes unit=scribe/ScribeOptions tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 162 |
| [scribe/Scribe](Scribe.md) | scribe | 16 |
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 6 |
| [scribe/TranscribeBoost](TranscribeBoost.md) | scribe | 4 |
| [scribe/TranscribeArray](TranscribeArray.md) | scribe | 3 |
| [scribe/TranscribeMappingProtocol](TranscribeMappingProtocol.md) | scribe | 2 |
| [scribe/TranscribeSequenceProtocol](TranscribeSequenceProtocol.md) | scribe | 2 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 2 |
| [scribe/ScribeInternalAccess](ScribeInternalAccess.md) | scribe | 1 |
| [scribe/ScribeInternalUtils](ScribeInternalUtils.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeOptions.h
```
