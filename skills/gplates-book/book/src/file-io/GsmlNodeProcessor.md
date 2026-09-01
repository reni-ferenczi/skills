# GsmlNodeProcessor

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1349 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlNodeProcessor.h` | C++ | 75 |
| `src/file-io/GsmlNodeProcessor.cc` | C++ | 58 |

## Overview

[[[PROSE overview unit=file-io/GsmlNodeProcessor tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GsmlNodeProcessor`](#gplatesfileiogsmlnodeprocessor) | class | [`ArbitraryNodeProcessor`](ArbitraryNodeProcessor.md) | — | 0 | — |

## Members

### `GPlatesFileIO::GsmlNodeProcessor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Handler` | typedef | `boost::function<void(QBuffer&)>` | public | — |
| `GsmlNodeProcessor( const QString& query_str, Handler handler)` | constructor | `None` | public | — |
| `execute( QBuffer& xml_data)` | method | `void` | public | — |
| `get_query_string()` | method | `QString` | public | — |
| `d_query` | field | `QXmlQuery` | protected | — |
| `d_query_str` | field | `QString` | protected | — |
| `d_handler` | field | `Handler` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GSMLNODEPROCESSOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GsmlNodeProcessor tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GsmlNodeProcessorFactory](GsmlNodeProcessorFactory.md) | file-io | 8 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GsmlNodeProcessor.h
python scripts/gpq.py def GPlatesFileIO::GsmlNodeProcessor --body
python scripts/gpq.py uses GsmlNodeProcessor --kind class
python scripts/gpq.py hier GsmlNodeProcessor
```
