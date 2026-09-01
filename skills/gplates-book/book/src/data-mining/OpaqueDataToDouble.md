# OpaqueDataToDouble

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 1259 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/OpaqueDataToDouble.h` | C++ | 89 |

## Overview

`ConvertOpaqueDataToDouble` is a Boost visitor that extracts numeric values from `OpaqueData` (a variant type holding different data kinds). It provides overloads for `int`, `double`, `float`, and `unsigned` types that wrap the value in `boost::optional<double>`, and a template fallback that returns `boost::none` for non-numeric types. This enables safe conversion of opaque data to numerical form for aggregation operations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::ConvertOpaqueDataToDouble`](#gplatesdataminingconvertopaquedatatodouble) | class | `boost::static_visitor<boost::optional<double> >` | — | 0 | — |

## Members

### `GPlatesDataMining::ConvertOpaqueDataToDouble`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const type)` | operator | `boost::optional<double>` | public | — |
| `operator()( const int data)` | operator | `boost::optional<double>` | public | — |
| `operator()( const double data)` | operator | `boost::optional<double>` | public | — |
| `operator()( const float data)` | operator | `boost::optional<double>` | public | — |
| `operator()( const unsigned data)` | operator | `boost::optional<double>` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_OPAQUEDATATODOUBLE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [api/PyFeature](../api/PyFeature.md) | api | 2 |
| [data-mining/DataMiningUtils](DataMiningUtils.md) | data-mining | 2 |
| [data-mining/MinReducer](MinReducer.md) | data-mining | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/OpaqueDataToDouble.h
python scripts/gpq.py def GPlatesDataMining::ConvertOpaqueDataToDouble --body
python scripts/gpq.py uses ConvertOpaqueDataToDouble --kind class
python scripts/gpq.py hier ConvertOpaqueDataToDouble
```
