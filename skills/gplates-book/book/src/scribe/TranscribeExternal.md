# TranscribeExternal

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 89 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeExternal.h` | C++ | 58 |

## Overview

This is an umbrella header that aggregates transcription support for external libraries into one include point. It includes `TranscribeBoost`, `TranscribeQt`, and `TranscribeStd`, which provide the specializations of `transcribe()` for Boost, Qt, and standard library types respectively. As a special case, it also includes `TranscribeNonNullIntrusivePtr` — which handles `GPlatesUtils::non_null_intrusive_ptr`, a utility based on Boost's intrusive_ptr. The umbrella design avoids forcing heavyweight `Scribe.h` includes into external library headers (which can't be modified) and centralizes the external type support.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBEEXTERNAL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeExternal.h
```
