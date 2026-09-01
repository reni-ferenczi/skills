# TranscribeNonNullIntrusivePtr

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 89 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeNonNullIntrusivePtr.h` | C++ | 130 |

## Overview

This unit provides transcription support for `GPlatesUtils::non_null_intrusive_ptr<T, H>`, a non-null variant of Boost's `intrusive_ptr`. The transcribe functions delegate to the smart pointer protocol to serialize the pointed-to object as a shared owner. Two overloads handle the two usage modes: `transcribe()` for existing objects and `transcribe_construct_data()` for constructing from load data. Since the pointer is non-null, both paths must succeed in loading a valid pointer; null pointers are not supported and will cause transcription failure. The header resides in `TranscribeExternal` to avoid pulling `Scribe.h` into the `non_null_intrusive_ptr` utility header.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBENONNULLINTRUSIVEPTR_H` | macro | `None` | — |
| `transcribe( Scribe &scribe, GPlatesUtils::non_null_intrusive_ptr<T, H> &intrusive_ptr_object, bool transcribed_construct_data)` | function | `TranscribeResult` | — |
| `transcribe_construct_data( Scribe &scribe, ConstructObject< GPlatesUtils::non_null_intrusive_ptr<T, H> > &intrusive_ptr_object)` | function | `TranscribeResult` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/TranscribeExternal](TranscribeExternal.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeNonNullIntrusivePtr.h
```
