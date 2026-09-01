# TimescaleName

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 756 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/TimescaleName.h` | C++ | 59 |

## Overview

[[[PROSE overview unit=property-values/TimescaleName tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=property-values/TimescaleName tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
