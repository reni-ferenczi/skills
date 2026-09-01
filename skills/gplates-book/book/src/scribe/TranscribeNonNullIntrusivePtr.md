# TranscribeNonNullIntrusivePtr

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 89 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeNonNullIntrusivePtr.h` | C++ | 130 |

## Overview

[[[PROSE overview unit=scribe/TranscribeNonNullIntrusivePtr tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/TranscribeNonNullIntrusivePtr tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
