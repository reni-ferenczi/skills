# TranscribeArray

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1546 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeArray.h` | C++ | 265 |

## Overview

[[[PROSE overview unit=scribe/TranscribeArray tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBEARRAY_H` | macro | `None` | — |
| `transcribe_construct_data( Scribe &scribe, ConstructObject<T [N]> &array)` | function | `TranscribeResult` | We don't support using Scribe::load() and Scribe::save() (ie, ConstructObject) on \*multidimensional\* arrays because they do not support (non-default) constructors (can only be initialised explicitly using braces). |
| `transcribe_array_size( Scribe &scribe, T (&array)[N])` | function | `TranscribeResult` | — |
| `transcribe_impl( Scribe &scribe, T (&array)[N])` | function | `typename boost::enable_if< boost::is_array<T>, TranscribeResult >::type` | Implementation path when 'T' is an array. |
| `transcribe( Scribe &scribe, T (&array)[N], bool transcribed_construct_data)` | function | `TranscribeResult` | — |

## Notes

[[[PROSE notes unit=scribe/TranscribeArray tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeArray.h
```
