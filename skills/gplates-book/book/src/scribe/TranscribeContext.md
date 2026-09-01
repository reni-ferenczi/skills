# TranscribeContext

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 46 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeContext.h` | C++ | 48 |

## Overview

`TranscribeContext<ObjectType>` is an empty template that callers specialise per `ObjectType` when transcribing that type needs information the archive itself does not carry. The default, unspecialised template holds nothing; a specialisation adds whatever extra state a `transcribe()` implementation needs but cannot reconstruct from the archived data alone — for example `TranscribeUtils::FilePath`'s specialisation carries the path of the project file currently being loaded, so relative file paths can be re-resolved against it rather than against where the project was originally saved.

The context object itself is never archived — it is constructed separately during loading (or saving) and made available to `Scribe` alongside the object being transcribed, for the cases where a constructor needs collaborators that the transcription format has no way to represent.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TranscribeContext`](#gplatesscribetranscribecontext) | class | — | `<typename ObjectType>` | 0 | The default transcribe context for object type 'ObjectType'. |

## Members

### `GPlatesScribe::TranscribeContext`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBECONTEXT_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 8 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 6 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 4 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 2 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 2 |
| [data-mining/CoRegConfigurationTable](../data-mining/CoRegConfigurationTable.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeContext.h
python scripts/gpq.py def GPlatesScribe::TranscribeContext --body
python scripts/gpq.py uses TranscribeContext --kind class
python scripts/gpq.py hier TranscribeContext
```
