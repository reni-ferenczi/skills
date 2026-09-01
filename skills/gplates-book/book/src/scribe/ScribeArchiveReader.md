# ScribeArchiveReader

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 477 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeArchiveReader.h` | C++ | 87 |

## Overview

`ArchiveReader` is the abstract interface that lets the rest of `GPlatesScribe` load a `Transcription` without caring whether it came from a text, binary or XML archive. `ScribeBinaryArchiveReader`, `ScribeTextArchiveReader` and `ScribeXmlArchiveReader` each implement `read_transcription()` and `close()` against their own on-disk layout (whose shared constants live in `ArchiveCommon`), and callers such as `ProjectSession` and `InternalSession` hold only this base type.

An archive can contain more than one transcription written back to back, so `read_transcription()` is meant to be called repeatedly until the caller has consumed everything it expects.

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

Call `close()` only after reading every transcription the archive contains; a partial read followed by `close()` can throw, since some archive types use it to verify the stream reached its end. `close()` is never called from the destructor, so a caller that skips it deliberately (to abandon a partial read) will not get that end-of-archive check.

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
