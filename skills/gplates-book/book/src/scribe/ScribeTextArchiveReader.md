# ScribeTextArchiveReader

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 477 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeTextArchiveReader.h` | C++ | 133 |
| `src/scribe/ScribeTextArchiveReader.cc` | C++ | 365 |

## Overview

`TextArchiveReader` is the `ArchiveReader` implementation that parses the human-readable text archive format written by `TextArchiveWriter`, reconstructing a `Transcription` from an `std::istream`. On construction it imbues the stream with the classic "C" locale and skips leading whitespace, so parsing is unaffected by the application's global locale, then validates the archive signature and checks that both the text-archive format version and the Scribe version that wrote the archive are not newer than what this build supports.

`read_transcription()` replays the archive's structure back into a fresh `Transcription`: the object tag names, the pool of unique strings, and then the objects themselves, read in contiguous id-ranged groups (`read_object_group()`) so the archive does not need to spell out every object id individually. Each object's leading type code selects which `Transcription::add_*` call reconstructs it, and a composite object's child keys and child object ids are read recursively via the protected `read(Transcription::CompositeObject &)` overload. The primitive-reading `read<ObjectType>()` template has explicit specialisations for `float`, `double` and `std::string` because those need special handling beyond `operator>>`: floats and doubles must recognise the writer's textual infinity/NaN tokens, and strings are stored length-prefixed rather than whitespace-delimited.

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

The `d_input_stream_*_saver` members are `boost::io` state savers, not tracking data — their sole job is to restore the stream's original flags, precision and locale when the reader is destroyed, since the constructor changes all three. Any malformed or truncated archive data — a bad signature, an unreadable primitive, a stream that runs out mid-read — surfaces as an exception (`Exceptions::InvalidArchiveSignature`, `Exceptions::UnsupportedVersion` or `Exceptions::ArchiveStreamError`) rather than a silently wrong `Transcription`. This class must stay format-compatible with `TextArchiveWriter`: the object type codes, the infinity/NaN sentinel strings, and the length-prefixed string encoding are shared conventions (`ArchiveCommon`) between the two, so changing one without the other breaks round-tripping.

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
