# ScribeBinaryArchiveReader

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 477 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeBinaryArchiveReader.h` | C++ | 120 |
| `src/scribe/ScribeBinaryArchiveReader.cc` | C++ | 370 |

## Overview

`BinaryArchiveReader` implements `ArchiveReader` for the binary archive format: it decodes a `Transcription` back out of a `QDataStream`, mirroring the layout `BinaryArchiveWriter` produces. Its constructor checks the archive signature byte-by-byte (deliberately not as a Qt string, since a corrupt stream's length prefix could be arbitrary), then validates that both the binary format version and the `Scribe` version the archive was written with are not newer than what this build supports.

Integers are decoded as Protocol-Buffers-style varints in `read_unsigned()`, with `read_signed()` layering a zigzag-style transform on top so small-magnitude negative values still encode in few bytes. `read_transcription()` reconstructs the object tags, the unique-string table, and then the objects themselves, which are stored on disk in contiguous id ranges (`read_object_group()`) so consecutive object ids don't each need their own id written out.

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

Every read helper asserts `d_input_stream.status() == QDataStream::Ok` and throws `Exceptions::ArchiveStreamError` on failure, so a truncated or corrupted archive fails fast rather than silently producing a partial `Transcription`. `close()` is a no-op here — the binary format needs no end-of-stream bookkeeping — which is why `read_transcription()` alone determines when the archive is exhausted (`read_object_group()` returns `false` once its group-size varint reads as zero).

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
