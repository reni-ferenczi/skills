# ScribeBinaryArchiveReader

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 477 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeBinaryArchiveReader.h` | C++ | 120 |
| `src/scribe/ScribeBinaryArchiveReader.cc` | C++ | 370 |

## Overview

[[[PROSE overview unit=scribe/ScribeBinaryArchiveReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::BinaryArchiveReader`](#gplatesscribebinaryarchivereader) | class | [`ArchiveReader`](ScribeArchiveReader.md) | — | 0 | Binary scribe archiver reader. |

## Members

### `GPlatesScribe::BinaryArchiveReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<BinaryArchiveReader>` | public | Convenience typedefs for a shared pointer to a BinaryArchiveReader. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const BinaryArchiveReader>` | public | — |
| `create( QDataStream &input_stream)` | method | `non_null_ptr_type` | public | Create an archive reader that reads from the specified input stream. |
| `read_transcription()` | method | `Transcription::non_null_ptr_type` | public | Reads a Transcription from the archive. |
| `close()` | method | `void` | public | Close the archive. |
| `BinaryArchiveReader( QDataStream &input_stream)` | constructor | `None` | protected | — |
| `read_object_group( Transcription &transcription)` | method | `bool` | protected | — |
| `read( Transcription::CompositeObject &composite_object)` | method | `void` | protected | Read Transcription composite object. |
| `read_signed()` | method | `int` | protected | Write Transcription primitives to the archive. |
| `read_unsigned()` | method | `unsigned int` | protected | — |
| `read_float()` | method | `float` | protected | — |
| `read_double()` | method | `double` | protected | — |
| `read_string()` | method | `std::string` | protected | — |
| `d_input_stream` | field | `QDataStream` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEBINARYARCHIVEREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=scribe/ScribeBinaryArchiveReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 36 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 12 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeBinaryArchiveReader.h
python scripts/gpq.py def GPlatesScribe::BinaryArchiveReader --body
python scripts/gpq.py uses BinaryArchiveReader --kind class
python scripts/gpq.py hier BinaryArchiveReader
```
