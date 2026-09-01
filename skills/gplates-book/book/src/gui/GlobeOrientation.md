# GlobeOrientation

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 524 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GlobeOrientation.h` | C++ | 109 |

## Overview

[[[PROSE overview unit=gui/GlobeOrientation tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GlobeOrientation`](#gplatesguiglobeorientation) | class | — | — | 1 | This class is an abstract interface for globe orientations. |

## Members

### `GPlatesGui::GlobeOrientation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~GlobeOrientation()` | destructor | `None` | public | — |
| `rotation_axis` | field | `GPlatesMaths::UnitVector3D` | public | Return the axis of the accumulated rotation of the globe. |
| `rotation_angle` | field | `GPlatesMaths::real_t` | public | Return the angle of the accumulated rotation of the globe. |
| `orient_point( const GPlatesMaths::PointOnSphere &pos)` | method | `GPlatesMaths::PointOnSphere` | public | Apply the accumulated rotation of the globe to the supplied point. |
| `reverse_orient_point( const GPlatesMaths::PointOnSphere &pos)` | method | `GPlatesMaths::PointOnSphere` | public | Apply the reverse of the accumulated rotation of the globe to the supplied point. |
| `set_new_handle_at_pos( const GPlatesMaths::PointOnSphere &pos)` | method | `void` | public | Set a new handle at the given position. |
| `move_handle_to_pos( const GPlatesMaths::PointOnSphere &pos)` | method | `void` | public | Move the already-set handle to the given position, changing the orientation of the globe in the process. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_GLOBEORIENTATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/GlobeOrientation tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/SimpleGlobeOrientation](SimpleGlobeOrientation.md) | gui | 14 |
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GlobeOrientation.h
python scripts/gpq.py def GPlatesGui::GlobeOrientation --body
python scripts/gpq.py uses GlobeOrientation --kind class
python scripts/gpq.py hier GlobeOrientation
```
