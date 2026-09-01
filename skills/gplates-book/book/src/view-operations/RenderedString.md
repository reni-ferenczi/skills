# RenderedString

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1022 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedString.h` | C++ | 144 |

## Overview

[[[PROSE overview unit=view-operations/RenderedString tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedString`](#gplatesviewoperationsrenderedstring) | class | [`RenderedGeometryImpl`](RenderedGeometryImpl.md) | — | 0 | — |

## Members

### `GPlatesViewOperations::RenderedString`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderedString( const GPlatesMaths::PointOnSphere &point_on_sphere, const QString &string, const GPlatesGui::ColourProxy &colour, const GPlatesGui::ColourProxy &shadow_colour, int x_offset = 0, int y_offset = 0, const QFont &font = QFont())` | constructor | `None` | public | — |
| `accept_visitor( ConstRenderedGeometryVisitor& visitor)` | method | `void` | public | — |
| `test_proximity( const GPlatesMaths::ProximityCriteria &criteria)` | method | `GPlatesMaths::ProximityHitDetail::maybe_null_ptr_type` | public | — |
| `get_x_offset()` | method | `int` | public | — |
| `get_y_offset()` | method | `int` | public | — |
| `d_point_on_sphere` | field | `GPlatesMaths::PointOnSphere` | private | Location of text |
| `d_string` | field | `QString` | private | Text to display |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | Colour of text |
| `d_shadow_colour` | field | `GPlatesGui::ColourProxy` | private | Colour of shadow; set ColourProxy to boost::none if you do not want shadows |
| `d_x_offset` | field | `int` | private | Shifts the text d\_x\_offset pixels to the right of where it would otherwise be |
| `d_y_offset` | field | `int` | private | Shifts the text d\_y\_offset pixels above of where it would otherwise be |
| `d_font` | field | `QFont` | private | Font in which to display the text |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_RENDEREDSTRING_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=view-operations/RenderedString tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 3 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 3 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedString.h
python scripts/gpq.py def GPlatesViewOperations::RenderedString --body
python scripts/gpq.py uses RenderedString --kind class
python scripts/gpq.py hier RenderedString
```
