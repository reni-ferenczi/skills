# ScribeBinaryArchiveWriter

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 383 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeBinaryArchiveWriter.h` | C++ | 128 |
| `src/scribe/ScribeBinaryArchiveWriter.cc` | C++ | 390 |

## Overview

`BinaryArchiveWriter` is the `ArchiveWriter` implementation for the binary format, encoding a `Transcription` onto a `QDataStream` in the exact byte layout `BinaryArchiveReader` expects. Its constructor writes the archive header — the signature bytes (written unencoded, one `qint8` at a time, since the reader must confirm the signature before it can trust any varint decoding), the binary format version and the current `Scribe` version.

`write_transcription()` writes the object-tag-name table and the unique-string table, then walks the transcription's object ids. Unused ids are skipped and used ids are coalesced into contiguous runs, each written as a start id plus a count, so a densely populated transcription avoids repeating an id for every object. The primitive `write()` overloads encode integers as variable-length (varint) values, mirroring the reader's decoding scheme.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::BinaryArchiveWriter`](#gplatesscribebinaryarchivewriter) | class | [`ArchiveWriter`](ScribeArchiveWriter.md) | — | 0 | Binary scribe archiver writer. |

## Members

### `GPlatesScribe::BinaryArchiveWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<BinaryArchiveWriter>` | public | Convenience typedefs for a shared pointer to a BinaryArchiveWriter. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const BinaryArchiveWriter>` | public | — |
| `create( QDataStream &output_stream)` | method | `non_null_ptr_type` | public | Create an archive writer that writes to the specified output stream. |
| `write_transcription( const Transcription &transcription)` | method | `void` | public | Writes a Transcription to the archive. |
| `close()` | method | `void` | public | Close the archive. |
| `BinaryArchiveWriter( QDataStream &output_stream)` | constructor | `None` | protected | — |
| `write_object_group( const Transcription &transcription, Transcription::object_id_type start_object_id_in_group, unsigned int num_object_ids_in_group)` | method | `void` | protected | — |
| `write( const Transcription::CompositeObject &composite_object)` | method | `void` | protected | Write Transcription composite object. |
| `write( const qint32 object)` | method | `void` | protected | Write Transcription primitives to the archive. |
| `write( const quint32 object)` | method | `void` | protected | — |
| `write( const float object)` | method | `void` | protected | — |
| `write( const double &object)` | method | `void` | protected | — |
| `write( const std::string &object)` | method | `void` | protected | — |
| `d_output_stream` | field | `QDataStream` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEBINARYARCHIVEWRITER_H` | macro | `None` | — |

## Notes

Every write asserts `d_output_stream.status() == QDataStream::Ok`, so a failing output stream (for example, a full disk) is reported immediately via `Exceptions::ArchiveStreamError` rather than producing a silently truncated archive. `close()` is a no-op, since the binary format needs no trailing marker to be readable back; changing the object encoding or the contiguous-group scheme here must stay in lockstep with `BinaryArchiveReader` and, for a breaking change, bump `ArchiveCommon::BINARY_ARCHIVE_FORMAT_VERSION`.

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 6 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 3 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeBinaryArchiveWriter.h
python scripts/gpq.py def GPlatesScribe::BinaryArchiveWriter --body
python scripts/gpq.py uses BinaryArchiveWriter --kind class
python scripts/gpq.py hier BinaryArchiveWriter
```
