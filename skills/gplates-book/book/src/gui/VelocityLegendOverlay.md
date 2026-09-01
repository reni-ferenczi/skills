# VelocityLegendOverlay

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1205 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/VelocityLegendOverlay.h` | C++ | 69 |
| `src/gui/VelocityLegendOverlay.cc` | C++ | 501 |

## Overview

[[[PROSE overview unit=gui/VelocityLegendOverlay tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::VelocityLegendOverlay`](#gplatesguivelocitylegendoverlay) | class | — | — | 0 | TextOverlay is responsible for painting the text overlay onto the globe or map, in a manner specified by TextOverlaySettings. |

## Members

### `GPlatesGui::VelocityLegendOverlay`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VelocityLegendOverlay()` | constructor | `None` | public | — |
| `paint( GPlatesOpenGL::GLRenderer &renderer, const VelocityLegendOverlaySettings &settings, int paint_device_width, int paint_device_height, float scale)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `BOX_MARGIN` | variable | `double` | BOX\_MARGIN - Fraction of window size used as margin around arrow. |
| `MIN_MARGIN` | variable | `int` | MIN\_MARGIN - minimum margin in pixels |
| `scale_font( const QFont &font, float scale)` | function | `QFont` | Returns a scaled version of the specified font. |
| `get_scale_from_uppermost_velocity_layer( const GPlatesPresentation::ViewState &view_state)` | function | `boost::optional<double>` | get\_scale\_from\_uppermost\_velocity\_layer the scale factor (i.e. the length of an arrow representing 2cm/yr) of the last velocity layer we come across in the layers collection, i.e. the uppermost velocity layer. |
| `get_scale_from_selected_layer( const boost::weak_ptr<GPlatesPresentation::VisualLayer> &selected_visual_layer)` | function | `boost::optional<double>` | — |
| `reduce_to_fit( double &length, double &scale, const double max_width)` | function | `void` | reduce\_to\_fit until |
| `increase_to_fit( double &length, double &scale, const double max_width)` | function | `void` | — |
| `render( GPlatesOpenGL::GLRenderer &renderer, const GPlatesGui::VelocityLegendOverlaySettings &settings, float x, float y, double legend_width, double legend_height, int legend_margin, const QString &text, int text_width, double arrow_length, double arrow_height, double arrow_angle, float scale)` | function | `void` | — |
| `GPLATES_GUI_VELOCITYLEGENDOVERLAY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/VelocityLegendOverlay tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GlobeCanvas](../qt-widgets/GlobeCanvas.md) | qt-widgets | 3 |
| [qt-widgets/MapCanvas](../qt-widgets/MapCanvas.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/VelocityLegendOverlay.h
python scripts/gpq.py def GPlatesGui::VelocityLegendOverlay --body
python scripts/gpq.py uses VelocityLegendOverlay --kind class
python scripts/gpq.py hier VelocityLegendOverlay
```
