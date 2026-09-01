# VelocityLegendOverlay

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1205 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/VelocityLegendOverlay.h` | C++ | 69 |
| `src/gui/VelocityLegendOverlay.cc` | C++ | 501 |

## Overview

Paints a scale arrow legend on the globe or map to indicate the visual scale of velocity vectors. The `paint()` method renders the legend onto the OpenGL viewport using a `GLRenderer`, constrained by `VelocityLegendOverlaySettings` and scaled to the viewport dimensions.

The supporting free functions calculate the arrow scale factor from velocity layers via `get_scale_from_uppermost_velocity_layer()`, adjust font sizes via `scale_font()`, and dynamically resize the legend to fit the available space with `reduce_to_fit()` and `increase_to_fit()`.

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

*None.*

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
