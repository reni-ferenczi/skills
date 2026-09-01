# Colour

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 340 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Colour.h` | C++ | 701 |
| `src/gui/Colour.cc` | C++ | 571 |

## Overview

[[[PROSE overview unit=gui/Colour tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::HSVColour`](#gplatesguihsvcolour) | struct | — | — | 0 | — |
| [`GPlatesGui::CMYKColour`](#gplatesguicmykcolour) | struct | — | — | 0 | — |
| [`GPlatesGui::rgba8_t`](#gplatesguirgba8_t) | struct | [`GPlatesUtils::QtStreamable<rgba8_t>`](../utils/QtStreamable.md) | — | 0 | — |
| [`GPlatesGui::Colour`](#gplatesguicolour) | class | `boost::equality_comparable<Colour>` | — | 0 | — |

## Members

### `GPlatesGui::HSVColour`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `h` | field | `double` | public | Hue \*/ |
| `s` | field | `double` | public | Saturation \*/ |
| `v` | field | `double` | public | Value \*/ |
| `a` | field | `double` | public | Alpha \*/ |
| `HSVColour( double h_, double s_, double v_, double a_ = 1.0)` | constructor | `None` | public | — |
| `linearly_interpolate( const HSVColour &first, const HSVColour &second, const double &position)` | method | `HSVColour` | public | Linearly interpolate between two colours. interpreted as where the returned colour lies in the range between the first colour and the second colour. |

### `GPlatesGui::CMYKColour`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `c` | field | `double` | public | Cyan \*/ |
| `m` | field | `double` | public | Magenta \*/ |
| `y` | field | `double` | public | Yellow \*/ |
| `k` | field | `double` | public | Black \*/ |
| `CMYKColour( double c_, double m_, double y_, double k_)` | constructor | `None` | public | — |

### `GPlatesGui::rgba8_t`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NUM_COMPONENTS` | field | `int` | public | NOTE: Be careful \*not\* to multiply inherit in order to avoid bloating sizeof(rgba8\_t) due to multiple inheritance (even from empty base class). sizeof(rgba\_t) should remain at 4 bytes. |
| `(anonymous)` | union | `None` | public | — |
| `rgba8_t()` | constructor | `None` | public | This DOES NOT initialise any of the components. |
| `rgba8_t( boost::uint8_t red_, boost::uint8_t green_, boost::uint8_t blue_, boost::uint8_t alpha_)` | constructor | `None` | public | — |
| `operator==( const rgba8_t &other)` | operator | `bool` | public | — |
| `operator!=( const rgba8_t &other)` | operator | `bool` | public | — |

### `GPlatesGui::Colour`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_black` | field | `Colour` | public | These functions are defined in colour.cc with macro. |
| `get_white` | field | `Colour` | public | — |
| `get_red` | field | `Colour` | public | — |
| `get_green` | field | `Colour` | public | — |
| `get_blue` | field | `Colour` | public | — |
| `get_grey` | field | `Colour` | public | — |
| `get_silver` | field | `Colour` | public | — |
| `get_maroon` | field | `Colour` | public | — |
| `get_purple` | field | `Colour` | public | — |
| `get_fuchsia` | field | `Colour` | public | — |
| `get_lime` | field | `Colour` | public | — |
| `get_olive` | field | `Colour` | public | — |
| `get_yellow` | field | `Colour` | public | — |
| `get_navy` | field | `Colour` | public | — |
| `get_teal` | field | `Colour` | public | — |
| `get_aqua` | field | `Colour` | public | — |
| `(anonymous enum)` | enum | `None` | public | Indices of the respective colour componets. |
| `Colour( const GLfloat &red = 0.0, const GLfloat &green = 0.0, const GLfloat &blue = 0.0, const GLfloat &alpha = 1.0)` | constructor | `None` | public | Construct a colour with the given red, green and blue components. |
| `Colour( const QColor &qcolor)` | constructor | `None` | public | Construct a Colour from its QColor equivalent. |
| `Colour( const Colour &colour)` | constructor | `None` | public | — |
| `red()` | method | `GLfloat` | public | Accessor methods |
| `green()` | method | `GLfloat` | public | — |
| `blue()` | method | `GLfloat` | public | — |
| `alpha()` | method | `GLfloat` | public | — |
| `linearly_interpolate( const Colour &first, const Colour &second, const double &position)` | method | `Colour` | public | Linearly interpolate between two colours. interpreted as where the returned colour lies in the range between the first colour and the second colour. |
| `linearly_interpolate( const Colour &first, const Colour &second, const Colour &third, const double &interp_first, const double &interp_second)` | method | `Colour` | public | Linearly interpolate between three colours. |
| `modulate( const Colour &first, const Colour &second)` | method | `Colour` | public | Modulate/multiply two colours (including alpha channel). |
| `pre_multiply_alpha( const Colour &colour)` | method | `Colour` | public | Return a colour with the RGB components multiplied by the alpha component. |
| `from_cmyk( const CMYKColour &cmyk)` | method | `Colour` | public | Converts a CMYK colour to a Colour (which is RGBA). |
| `to_cmyk( const Colour &colour)` | method | `CMYKColour` | public | Converts a Colour (which is RGBA) to CMYK. |
| `from_hsv( const HSVColour &hsv)` | method | `Colour` | public | Converts a HSV colour to a Colour (which is RGBA). |
| `to_hsv( const Colour &colour)` | method | `HSVColour` | public | Converts a Colour (which is RGBA) to HSV. |
| `from_rgba8( const rgba8_t &rgba8)` | method | `Colour` | public | Converts an RGBA colour with 8-bit integer components to a Colour (which uses floating-point values internally). |
| `to_rgba8( const Colour &colour)` | method | `rgba8_t` | public | Converts a Colour (which uses floating-point values internally) to an RGBA colour with 8-bit integer components. |
| `from_qrgb( const QRgb &rgba)` | method | `Colour` | public | Converts a QRgb to a Colour, preserving the alpha component. |
| `to_qrgb( const Colour &colour)` | method | `QRgb` | public | Converts a Colour to a QRgb, preserving the alpha component. |
| `d_rgba` | field | `GLfloat` | private | The storage space for the colour components. |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFINE_COLOUR` | macro_function | `const GPlatesGui::Colour & \ GPlatesGui::Colour::get_##colour_name() \ { \ static const GPlatesGui::Colour colour_name(r, g, b); \ return colour_name; \ }` | Define a function (eg, "get\_black()") that creates a local static colour object and returns it. |
| `clamp_zero_one( qreal value)` | function | `qreal` | — |
| `operator <<( QDebug dbg, const Colour &c)` | operator | `QDebug` | — |
| `FLOAT_TO_UINT8` | variable | `GLfloat` | The parentheses around min/max are to prevent the windows min/max macros from stuffing numeric\_limits' min/max. |
| `UINT8_MAX_VALUE` | variable | `boost::uint8_t` | — |
| `float_to_uint8( GLfloat f)` | function | `boost::uint8_t` | — |
| `GPLATES_GUI_COLOUR_H` | macro | `None` | — |
| `convert_argb32_to_rgba8( const boost::uint32_t *argb32_pixels, rgba8_t *rgba8_pixels, unsigned int num_pixels)` | function | `void` | Convert an array of pixels from the 32-bit integer format 0xAARRGGBB to the 4 x 8-byte (R,G,B,A) format (ie, the rgba8\_t type). |
| `convert_rgba8_to_argb32( const rgba8_t *rgba8_pixels, boost::uint32_t *argb32_pixels, unsigned int num_pixels)` | function | `void` | Convert an array of pixels from the 4 x 8-bit (R,G,B,A) format (ie, the rgba8\_t type) to the 32-bit integer format 0xAARRGGBB. |
| `output_pixels( QDataStream &out, const rgba8_t *rgba8_pixels, unsigned int num_pixels)` | function | `void` | Writes an array of rgba8\_t pixels to the output stream. |
| `input_pixels( QDataStream &in, rgba8_t *rgba8_pixels, unsigned int num_pixels)` | function | `void` | Read to array of rgba8\_t pixels from the input stream. |
| `pre_multiply_alpha( rgba8_t rgba8_color)` | function | `rgba8_t` | Return a colour with the RGB components multiplied by the alpha component. |
| `operator<<` | variable | `std::ostream` | — |
| `operator <<` | variable | `QTextStream` | Gives us: QTextStream text\_stream(device); text\_stream \<\< p; |
| `swap( GPlatesGui::rgba8_t &colour)` | function | `void` | — |

## Notes

[[[PROSE notes unit=gui/Colour tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapRenderedGeometryLayerPainter](MapRenderedGeometryLayerPainter.md) | gui | 256 |
| [gui/GlobeRenderedGeometryLayerPainter](GlobeRenderedGeometryLayerPainter.md) | gui | 196 |
| [gui/Palette](Palette.md) | gui | 136 |
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 109 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 106 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 103 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 101 |
| [unit-test/MipmapperTest](../unit-test/MipmapperTest.md) | unit-test | 89 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 88 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 88 |
| [qt-widgets/ExportVelocityOptionsWidget](../qt-widgets/ExportVelocityOptionsWidget.md) | qt-widgets | 82 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 81 |
| [view-operations/RenderedGeometryParameters](../view-operations/RenderedGeometryParameters.md) | view-operations | 71 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 62 |
| [gui/BuiltinColourPalettes](BuiltinColourPalettes.md) | gui | 60 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 60 |
| [gui/PlateIdColourPalettes](PlateIdColourPalettes.md) | gui | 57 |
| [qt-widgets/HellingerConfigurationWidget](../qt-widgets/HellingerConfigurationWidget.md) | qt-widgets | 56 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 55 |
| [gui/deprecated/MainWindow](deprecated/MainWindow.md) | gui | 53 |

*... and 213 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/Colour.h
python scripts/gpq.py def GPlatesGui::Colour --body
python scripts/gpq.py uses Colour --kind class
python scripts/gpq.py hier Colour
```
