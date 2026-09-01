# Reconstruct

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 773 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/controls/Reconstruct.h` | C++ | 64 |
| `src/deprecated/controls/Reconstruct.cc` | C++ | 442 |

## Overview

[[[PROSE overview unit=deprecated/controls/Reconstruct tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`RotationsByPlate`](#rotationsbyplate) | typedef | — | — | 0 | — |
| [`status`](#status) | enum | — | — | 0 | — |

## Members

### `RotationsByPlate`

*None.*

### `status`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SUCCESSFUL` | enumerator | `None` | — | — |
| `CANNOT_BE_ROTATED` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `RIDOfGlobe` | variable | `rid_t` | FIXME: this should be placed somewhere "more official". |
| `ListContainsElem(const std::list< T > &l, const T &e)` | function | `bool` | A convenient alias for the operation of searching through a list for a particular element. |
| `CheckRotation(rid_t plate_id, real_t t, RotationsByPlate &rot_cache, std::list< rid_t > &cannot_be_rotated, const Data::RotationMap_type &histories)` | function | `enum status` | Check whether the plate described by plate\_id can be rotated to time t. |
| `PopulateRotatableData(const Data::DrawableMap_type *plates_to_draw, RotationsByPlate &rot_cache, const real_t &t)` | function | `void` | Given plates\_to\_draw (the collection of all plates to attempt to draw), populate rot\_cache (the collection of all plates which can be drawn) with the finite rotations which will rotate the plates to their positions at time t. |
| `WarpToTime(const fpdata_t &t)` | function | `void` | Warp the geological data to its position at time t. |
| `WarpToPresent()` | function | `void` | Warp the geological data to its position in the present-day (ie, at time 0.0 Ma). |
| `_GPLATES_CONTROLS_RECONSTRUCT_H_` | macro | `None` | — |
| `Time(const GPlatesGlobal::fpdata_t& time)` | function | `void` | Reconstruct the positions of the data at time time using the loaded rotation file. |
| `Present()` | function | `void` | Reset the construction back to the present day. |
| `Animation(const GPlatesGlobal::fpdata_t& start_time, const GPlatesGlobal::fpdata_t& end_time, const GPlatesGlobal::fpdata_t& time_delta, bool finish_on_end)` | function | `void` | Display an animation of the positions of the data as they move from time start\_time to time end\_time. start\_time and end\_time are measured in millions of years ago. |

## Notes

[[[PROSE notes unit=deprecated/controls/Reconstruct tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/deprecated/MainWindow](../../gui/deprecated/MainWindow.md) | gui | 7 |
| [deprecated/controls/File](File.md) | deprecated | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/controls/Reconstruct.h
python scripts/gpq.py def RotationsByPlate --body
python scripts/gpq.py uses RotationsByPlate --kind typedef
```
