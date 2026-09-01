# ScribeTextArchiveReader

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 477 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeTextArchiveReader.h` | C++ | 133 |
| `src/scribe/ScribeTextArchiveReader.cc` | C++ | 365 |

## Overview

[[[PROSE overview unit=scribe/ScribeTextArchiveReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TextArchiveReader`](#gplatesscribetextarchivereader) | class | [`ArchiveReader`](ScribeArchiveReader.md) | — | 0 | Text scribe archiver reader. |

## Members

### `GPlatesScribe::TextArchiveReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TextArchiveReader>` | public | Convenience typedefs for a shared pointer to a TextArchiveReader. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TextArchiveReader>` | public | — |
| `create( std::istream &input_stream)` | method | `non_null_ptr_type` | public | Create an archive reader that reads from the specified input stream. |
| `read_transcription()` | method | `Transcription::non_null_ptr_type` | public | Reads a Transcription from the archive. |
| `close()` | method | `void` | public | Close the archive. |
| `TextArchiveReader( std::istream &input_stream)` | constructor | `None` | protected | — |
| `read_object_group( Transcription &transcription)` | method | `bool` | protected | — |
| `read( Transcription::CompositeObject &composite_object)` | method | `void` | protected | Read Transcription composite object. |
| `read()` | method | `ObjectType` | protected | Read Transcription primitives from the archive. |
| `d_input_stream` | field | `std::istream` | protected | — |
| `d_input_stream_flags_saver` | field | `boost::io::ios_flags_saver` | protected | Stream IO state savers to restore the stream state when finished. |
| `d_input_stream_precision_saver` | field | `boost::io::ios_precision_saver` | protected | — |
| `d_input_stream_locale_saver` | field | `boost::io::basic_ios_locale_saver<std::istream::char_type, std::istream::traits_type>` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBETEXTARCHIVEREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=scribe/ScribeTextArchiveReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 6 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeTextArchiveReader.h
python scripts/gpq.py def GPlatesScribe::TextArchiveReader --body
python scripts/gpq.py uses TextArchiveReader --kind class
python scripts/gpq.py hier TextArchiveReader
```
