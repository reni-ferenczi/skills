# ScribeArchiveReader

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 477 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeArchiveReader.h` | C++ | 87 |

## Overview

[[[PROSE overview unit=scribe/ScribeArchiveReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::ArchiveReader`](#gplatesscribearchivereader) | class | [`GPlatesUtils::ReferenceCount<ArchiveReader>`](../utils/ReferenceCount.md) | — | 3 | Base class for all scribe archive readers. |

## Members

### `GPlatesScribe::ArchiveReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ArchiveReader>` | public | Convenience typedefs for a shared pointer to a ArchiveReader. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ArchiveReader>` | public | — |
| `~ArchiveReader()` | destructor | `None` | public | — |
| `read_transcription()` | method | `Transcription::non_null_ptr_type` | public | Reads a Transcription from the archive. |
| `close()` | method | `void` | public | Close the archive. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEARCHIVEREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=scribe/ScribeArchiveReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 66 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 18 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 11 |
| [scribe/ScribeBinaryArchiveReader](ScribeBinaryArchiveReader.md) | scribe | 4 |
| [scribe/ScribeTextArchiveReader](ScribeTextArchiveReader.md) | scribe | 4 |
| [scribe/ScribeXmlArchiveReader](ScribeXmlArchiveReader.md) | scribe | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeArchiveReader.h
python scripts/gpq.py def GPlatesScribe::ArchiveReader --body
python scripts/gpq.py uses ArchiveReader --kind class
python scripts/gpq.py hier ArchiveReader
```
