# TimescaleBand

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 756 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/TimescaleBand.h` | C++ | 58 |

## Overview

`TimescaleBand` is a `GPlatesModel::StringContentTypeGenerator<TimescaleBandFactory>` instantiation for the interned names of geological timescale bands (its own Doxygen comment gives "Devonian" as an example). `TimescaleBandFactory` is never instantiated; it exists only to bind `StringContentTypeGenerator` to the dedicated `GPlatesUtils::StringSet` returned by `GPlatesModel::StringSetSingletons::timescale_band_instance()`, so every `TimescaleBand` string is interned separately from other string-typedef families such as `TextContent` or `ValueObjectType`.

`GpmlAge` is by far the heaviest consumer, using `TimescaleBand` to name the timescale a geological age is expressed against.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::TimescaleBandFactory`](#gplatespropertyvaluestimescalebandfactory) | class | — | — | 0 | — |
| [`GPlatesPropertyValues::TimescaleBand`](#gplatespropertyvaluestimescaleband) | typedef | — | — | 0 | StringSetSingleton typedef for the names of bands within a timescale - e.g. |

## Members

### `GPlatesPropertyValues::TimescaleBandFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TimescaleBandFactory()` | constructor | `None` | private | — |

### `GPlatesPropertyValues::TimescaleBand`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_TIMESCALEBAND_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/GpmlAge](GpmlAge.md) | property-values | 28 |
| [qt-widgets/EditAgeWidget](../qt-widgets/EditAgeWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/TimescaleBand.h
python scripts/gpq.py def GPlatesPropertyValues::TimescaleBandFactory --body
python scripts/gpq.py uses TimescaleBandFactory --kind class
python scripts/gpq.py hier TimescaleBandFactory
```
