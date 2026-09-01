# ScribeTextArchiveWriter

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 383 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeTextArchiveWriter.h` | C++ | 136 |
| `src/scribe/ScribeTextArchiveWriter.cc` | C++ | 390 |

## Overview

[[[PROSE overview unit=scribe/ScribeTextArchiveWriter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TextArchiveWriter`](#gplatesscribetextarchivewriter) | class | [`ArchiveWriter`](ScribeArchiveWriter.md) | — | 0 | Text scribe archiver writer. |

## Members

### `GPlatesScribe::TextArchiveWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TextArchiveWriter>` | public | Convenience typedefs for a shared pointer to a TextArchiveWriter. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TextArchiveWriter>` | public | — |
| `create( std::ostream &output_stream)` | method | `non_null_ptr_type` | public | Create an archive writer that writes to the specified output stream. |
| `write_transcription( const Transcription &transcription)` | method | `void` | public | Writes a Transcription to the archive. |
| `close()` | method | `void` | public | Close the archive. |
| `TextArchiveWriter( std::ostream &output_stream)` | constructor | `None` | protected | — |
| `write_object_group( const Transcription &transcription, Transcription::object_id_type start_object_id_in_group, unsigned int num_object_ids_in_group)` | method | `void` | protected | — |
| `write( const Transcription::CompositeObject &composite_object)` | method | `void` | protected | Write Transcription composite object. |
| `write( const Transcription::int32_type object)` | method | `void` | protected | Write Transcription primitives to the archive. |
| `write( const Transcription::uint32_type object)` | method | `void` | protected | — |
| `write( const float object)` | method | `void` | protected | — |
| `write( const double &object)` | method | `void` | protected | — |
| `write( const std::string &object)` | method | `void` | protected | — |
| `d_output_stream` | field | `std::ostream` | protected | — |
| `d_output_stream_flags_saver` | field | `boost::io::ios_flags_saver` | protected | Stream IO state savers to restore the stream state when finished. |
| `d_output_stream_precision_saver` | field | `boost::io::ios_precision_saver` | protected | — |
| `d_output_stream_locale_saver` | field | `boost::io::basic_ios_locale_saver<std::ostream::char_type, std::ostream::traits_type>` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBETEXTARCHIVEWRITER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=scribe/ScribeTextArchiveWriter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 6 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeTextArchiveWriter.h
python scripts/gpq.py def GPlatesScribe::TextArchiveWriter --body
python scripts/gpq.py uses TextArchiveWriter --kind class
python scripts/gpq.py hier TextArchiveWriter
```
