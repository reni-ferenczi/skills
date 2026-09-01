# ScribeOptions

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 28 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeOptions.h` | C++ | 54 |

## Overview

Defines the bit-flag constants passed as the `options` argument of `Scribe::transcribe()` and related calls: `TRACK`, `EXCLUSIVE_OWNER` and `SHARED_OWNER`. They are combined with bitwise OR, as in `GPlatesScribe::EXCLUSIVE_OWNER | GPlatesScribe::TRACK`, to tell the Scribe how to treat a particular object during transcription. `TRACK` requests that an object be tracked (untracked is the default) so it can later be relocated or shared via reference; `EXCLUSIVE_OWNER` and `SHARED_OWNER` apply only to pointers and declare whether the pointer owns the pointed-to object outright or shares that ownership with other pointers.

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

*None.*

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
