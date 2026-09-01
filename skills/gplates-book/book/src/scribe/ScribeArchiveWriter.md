# ScribeArchiveWriter

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 383 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeArchiveWriter.h` | C++ | 82 |

## Overview

[[[PROSE overview unit=scribe/ScribeArchiveWriter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::ArchiveWriter`](#gplatesscribearchivewriter) | class | [`GPlatesUtils::ReferenceCount<ArchiveWriter>`](../utils/ReferenceCount.md) | — | 3 | Base class for all scribe archive writers. |

## Members

### `GPlatesScribe::ArchiveWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ArchiveWriter>` | public | Convenience typedefs for a shared pointer to a ArchiveWriter. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ArchiveWriter>` | public | — |
| `~ArchiveWriter()` | destructor | `None` | public | — |
| `write_transcription( const Transcription &transcription)` | method | `void` | public | Writes a Transcription to the archive. |
| `close()` | method | `void` | public | Close the archive. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEARCHIVEWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=scribe/ScribeArchiveWriter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 16 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 7 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 3 |
| [scribe/ScribeBinaryArchiveWriter](ScribeBinaryArchiveWriter.md) | scribe | 2 |
| [scribe/ScribeTextArchiveWriter](ScribeTextArchiveWriter.md) | scribe | 2 |
| [scribe/ScribeXmlArchiveWriter](ScribeXmlArchiveWriter.md) | scribe | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeArchiveWriter.h
python scripts/gpq.py def GPlatesScribe::ArchiveWriter --body
python scripts/gpq.py uses ArchiveWriter --kind class
python scripts/gpq.py hier ArchiveWriter
```
