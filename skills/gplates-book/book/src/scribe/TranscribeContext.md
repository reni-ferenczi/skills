# TranscribeContext

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 46 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeContext.h` | C++ | 48 |

## Overview

[[[PROSE overview unit=scribe/TranscribeContext tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/TranscribeContext tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
