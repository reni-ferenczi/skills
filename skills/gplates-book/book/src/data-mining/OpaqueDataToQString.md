# OpaqueDataToQString

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1241 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/OpaqueDataToQString.h` | C++ | 98 |

## Overview

`ConvertOpaqueDataToString` is a Boost visitor that converts `OpaqueData` to `QString` for display in UI tables and other text representations. It handles multiple data kinds: empty data becomes `"NaN"`, booleans become `"true"` or `"false"`, numeric types are converted via `QString::number()`, strings are returned as-is, and single characters are wrapped in `QString`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::ConvertOpaqueDataToString`](#gplatesdataminingconvertopaquedatatostring) | class | `boost::static_visitor<QString>` | — | 0 | — |

## Members

### `GPlatesDataMining::ConvertOpaqueDataToString`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const empty_data_type)` | operator | `QString` | public | — |
| `operator()( const bool b)` | operator | `QString` | public | — |
| `operator()( const Type data)` | operator | `QString` | public | — |
| `operator()( const QString& str)` | operator | `QString` | public | — |
| `operator()( const char c)` | operator | `QString` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_OPAQUEDATAVISITORS_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/DataAssociationDataTableTest](../unit-test/DataAssociationDataTableTest.md) | unit-test | 4 |
| [data-mining/DataTable](DataTable.md) | data-mining | 3 |
| [api/PyFeature](../api/PyFeature.md) | api | 2 |
| [data-mining/VoteReducer](VoteReducer.md) | data-mining | 2 |
| [qt-widgets/CoRegistrationResultTableDialog](../qt-widgets/CoRegistrationResultTableDialog.md) | qt-widgets | 2 |
| [api/CoReg](../api/CoReg.md) | api | 1 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/OpaqueDataToQString.h
python scripts/gpq.py def GPlatesDataMining::ConvertOpaqueDataToString --body
python scripts/gpq.py uses ConvertOpaqueDataToString --kind class
python scripts/gpq.py hier ConvertOpaqueDataToString
```
