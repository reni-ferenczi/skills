# GsmlNodeProcessor

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1349 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlNodeProcessor.h` | C++ | 75 |
| `src/file-io/GsmlNodeProcessor.cc` | C++ | 58 |

## Overview

A processor that executes XQueries against GSML XML and delegates result handling to a callback. Constructed with a query string and a `Handler` callback (a `boost::function<void(QBuffer&)>`), `execute()` evaluates the query, extracts results, and invokes the handler on each matching element wrapped in a `QBuffer`. It inherits from `ArbitraryNodeProcessor`, supporting the processing pipeline used during GSML feature and property extraction.

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

*None.*

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
