# ScribeInternalUtilsImpl

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 28 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeInternalUtilsImpl.h` | C++ | 88 |

## Overview

This file provides template method implementations for `TranscribeOwningPointerTemplate`, which handles serialization of objects owned by pointers. The save path creates a `SaveConstructObject` wrapper and transcribes it; the load path constructs the object on the heap via `LoadConstructObjectOnHeap`, transcribes into it, then releases ownership to the owning pointer. This separation of construction and transcription is necessary because the scribe system must handle both the creation and the value-loading phases independently.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEINTERNALUTILSIMPL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 1 |
| [scribe/ScribeExportRegistry](ScribeExportRegistry.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeInternalUtilsImpl.h
```
