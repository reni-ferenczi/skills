# TimescaleName

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 756 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/TimescaleName.h` | C++ | 59 |

## Overview

A `StringContentTypeGenerator` typedef for timescale names (e.g., ICC2012, GTS2004) used in the `GpmlAge` property value. The `TimescaleNameFactory` provides access to a singleton string set of valid timescale identifiers, leveraging the `StringSetSingletons` infrastructure to ensure a single, deduplicated pool of timescale name strings across the application.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::TimescaleNameFactory`](#gplatespropertyvaluestimescalenamefactory) | class | — | — | 0 | — |
| [`GPlatesPropertyValues::TimescaleName`](#gplatespropertyvaluestimescalename) | typedef | — | — | 0 | StringSetSingleton typedef for common names of timescales e.g. |

## Members

### `GPlatesPropertyValues::TimescaleNameFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TimescaleNameFactory()` | constructor | `None` | private | — |

### `GPlatesPropertyValues::TimescaleName`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_TIMESCALENAME_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/GpmlAge](GpmlAge.md) | property-values | 12 |
| [qt-widgets/EditAgeWidget](../qt-widgets/EditAgeWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/TimescaleName.h
python scripts/gpq.py def GPlatesPropertyValues::TimescaleNameFactory --body
python scripts/gpq.py uses TimescaleNameFactory --kind class
python scripts/gpq.py hier TimescaleNameFactory
```
