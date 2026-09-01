# ArbitraryNodeProcessor

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1349 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ArbitraryNodeProcessor.h` | C++ | 55 |

## Overview

[[[PROSE overview unit=file-io/ArbitraryNodeProcessor tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ArbitraryNodeProcessor`](#gplatesfileioarbitrarynodeprocessor) | class | — | — | 1 | — |

## Members

### `GPlatesFileIO::ArbitraryNodeProcessor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `execute( QBuffer& xml_data)` | method | `void` | public | — |
| `~ArbitraryNodeProcessor()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_ARBITRARYNODEPROCESSOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/ArbitraryNodeProcessor tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GsmlNodeProcessorFactory](GsmlNodeProcessorFactory.md) | file-io | 12 |
| [file-io/GsmlNodeProcessor](GsmlNodeProcessor.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ArbitraryNodeProcessor.h
python scripts/gpq.py def GPlatesFileIO::ArbitraryNodeProcessor --body
python scripts/gpq.py uses ArbitraryNodeProcessor --kind class
python scripts/gpq.py hier ArbitraryNodeProcessor
```
