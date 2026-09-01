# ArbitraryNodeProcessor

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1349 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ArbitraryNodeProcessor.h` | C++ | 55 |

## Overview

Abstract interface for processors that operate on XML data. The `execute` method applies processing logic to XML content held in a `QBuffer`. This base class defines the contract for concrete processors like `GsmlNodeProcessor` that extract and handle specific nodes from XML documents using XPath queries.

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

*None.*

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
