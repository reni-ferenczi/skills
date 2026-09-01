# VelocityLegendOverlaySettings

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 305 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/VelocityLegendOverlaySettings.h` | C++ | 326 |
| `src/gui/VelocityLegendOverlaySettings.cc` | C++ | 102 |

## Overview

`VelocityLegendOverlaySettings` is a plain value object holding everything
`GPlatesGui::VelocityLegendOverlay` needs to draw the on-globe velocity-scale
legend: text font and colour, arrow colour, optional background colour and
opacity, screen anchor corner (`Anchor`) with a pixel offset, and the arrow's
angle and length. `ConfigureVelocityLegendOverlayDialog` edits an instance of
this class directly; `VelocityLegendOverlay` reads it back when painting.

The `ArrowLengthType` enum captures the one real design choice the settings
encode: whether the legend keeps the velocity scale (`DYNAMIC_ARROW_LENGTH`,
arrow length changes with zoom to preserve a fixed cm/yr scale) or the arrow's
on-screen length (`MAXIMUM_ARROW_LENGTH`, the scale snaps to round multiples
of 2/5/10/20 cm/yr as the view zooms to keep the arrow a roughly constant
size) fixed as the user zooms. `d_selected_velocity_layer` records which
`VisualLayer` the legend currently reflects, since a document can have more
than one velocity layer and the overlay only shows one at a time.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::VelocityLegendOverlaySettings`](#gplatesguivelocitylegendoverlaysettings) | class | — | — | 0 | — |

## Members

### `GPlatesGui::VelocityLegendOverlaySettings`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Anchor` | enum | `None` | public | — |
| `ArrowLengthType` | enum | `None` | public | — |
| `VelocityLegendOverlaySettings()` | constructor | `None` | public | Constructs a VelocityLegendOverlaySettings with default values. |
| `set_scale_text_font( const QFont &font)` | method | `void` | public | — |
| `set_scale_text_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `set_arrow_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `set_background_colour( const GPlatesGui::Colour &colour)` | method | `void` | public | — |
| `get_anchor()` | method | `Anchor` | public | — |
| `set_anchor( Anchor anchor)` | method | `void` | public | — |
| `get_x_offset()` | method | `int` | public | — |
| `set_x_offset( int x_offset)` | method | `void` | public | — |
| `get_y_offset()` | method | `int` | public | — |
| `set_y_offset( int y_offset)` | method | `void` | public | — |
| `is_enabled()` | method | `bool` | public | — |
| `set_enabled( bool enabled)` | method | `void` | public | — |
| `get_arrow_length()` | method | `int` | public | — |
| `set_arrow_length( int length)` | method | `void` | public | — |
| `get_arrow_angle()` | method | `int` | public | — |
| `set_arrow_angle( int angle)` | method | `void` | public | — |
| `get_arrow_scale()` | method | `double` | public | — |
| `set_arrow_scale( double scale)` | method | `void` | public | — |
| `get_background_opacity()` | method | `double` | public | — |
| `set_background_opacity( double opacity)` | method | `void` | public | — |
| `background_enabled()` | method | `bool` | public | — |
| `set_background_enabled( bool enabled)` | method | `void` | public | — |
| `get_arrow_length_type()` | method | `ArrowLengthType` | public | — |
| `set_arrow_length_type( ArrowLengthType type)` | method | `void` | public | — |
| `get_selected_velocity_layer()` | method | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | public | — |
| `set_selected_velocity_layer( boost::weak_ptr<GPlatesPresentation::VisualLayer> layer)` | method | `void` | public | — |
| `DEFAULT_SCALE_TEXT_COLOUR` | field | `GPlatesGui::Colour` | public | — |
| `DEFAULT_ARROW_COLOUR` | field | `GPlatesGui::Colour` | public | — |
| `DEFAULT_BACKGROUND_COLOUR` | field | `GPlatesGui::Colour` | public | — |
| `DEFAULT_ANCHOR` | field | `Anchor` | public | — |
| `DEFAULT_X_OFFSET` | field | `int` | public | — |
| `DEFAULT_Y_OFFSET` | field | `int` | public | — |
| `DEFAULT_ARROW_LENGTH` | field | `int` | public | — |
| `DEFAULT_ARROW_ANGLE` | field | `int` | public | — |
| `DEFAULT_ARROW_SCALE` | field | `double` | public | — |
| `DEFAULT_BACKGROUND_OPACITY` | field | `double` | public | — |
| `DEFAULT_IS_ENABLED` | field | `bool` | public | — |
| `DEFAULT_BACKGROUND_ENABLED` | field | `bool` | public | — |
| `d_scale_text_font` | field | `QFont` | private | — |
| `d_scale_text_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_arrow_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_background_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_anchor` | field | `Anchor` | private | — |
| `d_x_offset` | field | `int` | private | — |
| `d_y_offset` | field | `int` | private | — |
| `d_arrow_length` | field | `int` | private | d\_arrow\_length - in pixels |
| `d_arrow_angle` | field | `int` | private | d\_arrow\_angle- angle of velocity arrow. |
| `d_scale` | field | `double` | private | d\_scale Velocity scale (cm / yr) provided by user. |
| `d_background_opacity` | field | `double` | private | — |
| `d_is_enabled` | field | `bool` | private | — |
| `d_background_enabled` | field | `bool` | private | — |
| `d_arrow_length_type` | field | `ArrowLengthType` | private | — |
| `d_selected_velocity_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | d\_selected\_velocity\_layer - the velocity layer selected in the UI's combo-box. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_SCALE_TEXT_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `DEFAULT_ARROW_COLOUR` | variable | `GPlatesGui::Colour` | — |
| `DEFAULT_BACKGROUND_COLOUR` | variable | `GPlatesGui::Colour` | A tasteful semi-transparent blue. |
| `DEFAULT_ANCHOR` | variable | `GPlatesGui::VelocityLegendOverlaySettings::Anchor` | — |
| `DEFAULT_X_OFFSET` | variable | `int` | — |
| `DEFAULT_Y_OFFSET` | variable | `int` | — |
| `DEFAULT_ARROW_LENGTH` | variable | `int` | — |
| `DEFAULT_ARROW_ANGLE` | variable | `int` | — |
| `DEFAULT_ARROW_SCALE` | variable | `double` | — |
| `DEFAULT_BACKGROUND_OPACITY` | variable | `double` | — |
| `DEFAULT_IS_ENABLED` | variable | `bool` | — |
| `DEFAULT_BACKGROUND_ENABLED` | variable | `bool` | — |
| `get_default_font()` | function | `QFont` | — |
| `GPLATES_GUI_VELOCITYLEGENDOVERLAYSETTINGS_H` | macro | `None` | — |

## Notes

- `get_selected_velocity_layer()` is a `boost::weak_ptr`; the default
  constructor leaves it empty and does not attempt to auto-select an existing
  velocity layer, so callers must check it before use and expect it to be
  expired if the referenced `VisualLayer` was since removed.
- The default scale-text font is not a fixed size: `get_default_font()`
  scales the application's default `QFont` point size by 1.5, so it tracks
  whatever font the rest of the application is using.
- The legend is disabled (`DEFAULT_IS_ENABLED == false`) and the background
  fill enabled by default (`DEFAULT_BACKGROUND_ENABLED == true`); the two
  flags are independent, so a caller can show the arrow/text without the
  background box or vice versa.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ConfigureVelocityLegendOverlayDialog](../qt-widgets/ConfigureVelocityLegendOverlayDialog.md) | qt-widgets | 36 |
| [gui/VelocityLegendOverlay](VelocityLegendOverlay.md) | gui | 20 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/VelocityLegendOverlaySettings.h
python scripts/gpq.py def GPlatesGui::VelocityLegendOverlaySettings --body
python scripts/gpq.py uses VelocityLegendOverlaySettings --kind class
python scripts/gpq.py hier VelocityLegendOverlaySettings
```
