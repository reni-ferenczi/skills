# TranscribeArray

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1546 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeArray.h` | C++ | 265 |

## Overview

This unit provides transcription support for native C++ static arrays, including multidimensional ones. It recursively handles arrays of arrays by using `boost::enable_if` to branch: when the element type `T` is itself an array, it recurses; when `T` is a scalar, it uses `ConstructObject` semantics for saving and `LoadRef` for loading. The array size is treated as part of the serialized format and validated on load; if the source code changes the array size, loading old archives will fail. Arrays use the same sequence protocol as `std::vector`, making them compatible with other container types during transcription.

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

Multidimensional arrays cannot be constructed via `ConstructObject` (only initialized via brace syntax), but you can transcribe arrays of non-default-constructable items as long as the array itself is already allocated. Changing an array's compile-time size in source code breaks compatibility with previously saved archives; there is no version migration path short of storing arrays in a container class and manually reconstructing the serialization logic.

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
