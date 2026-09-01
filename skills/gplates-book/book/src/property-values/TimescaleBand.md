# TimescaleBand

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 756 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/TimescaleBand.h` | C++ | 58 |

## Overview

[[[PROSE overview unit=property-values/TimescaleBand tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=property-values/TimescaleBand tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
