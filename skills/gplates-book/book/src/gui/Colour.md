# Colour

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 340 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Colour.h` | C++ | 701 |
| `src/gui/Colour.cc` | C++ | 571 |

## Overview

`Colour` is the value type the whole application passes around wherever a colour
is needed, and its entire design is dictated by one requirement: an array of
`Colour` must be handable to OpenGL directly as an array of four `GLfloat`s.
That is why the sole member is `GLfloat d_rgba[RGBA_SIZE]`, why the class
provides implicit `operator GLfloat*` / `operator const GLfloat*` conversions,
and why the header goes out of its way *not* to inherit from
`GPlatesUtils::QtStreamable` — even an empty base would push `sizeof(Colour)`
from 16 to 20 bytes, so the streaming operators are provided as free functions
instead. The same reasoning governs `rgba8_t`, which must stay exactly 4 bytes
and therefore also refuses multiple inheritance.

The two representations here are for two different worlds. `Colour` is the
floating-point form used by the painters (`GlobeRenderedGeometryLayerPainter`,
`MapRenderedGeometryLayerPainter`), by every colour palette, and by
`RenderedGeometryFactory`. `rgba8_t` is the packed 8-bit form used for raster and
texture data — it is an anonymous union over four named `uint8_t` components, a
`char[4]`, and both signed and unsigned 32-bit views, so the same four bytes can
be addressed whichever way the surrounding code finds convenient.
`convert_argb32_to_rgba8` and `convert_rgba8_to_argb32` bridge it to Qt: the
long comments there are worth reading before touching them, because
`QImage::Format_ARGB32` names a *32-bit integer* layout while `GL_RGBA` names a
*memory byte* layout, so the two are only the same thing on little-endian
machines. Both functions branch on `QSysInfo::ByteOrder` accordingly.

Everything else is conversion and blending helpers: to and from `QColor`, `QRgb`,
CMYK and HSV, plus `linearly_interpolate`, `modulate` and `pre_multiply_alpha`.
`HSVColour` exists mainly so that `linearly_interpolate` can be done in hue
space — its implementation is the only non-trivial arithmetic in the file,
handling the fact that hue is cyclic (it takes the shorter way round the wheel)
and that achromatic colours have a meaningless hue (it borrows the other
colour's hue rather than sweeping through the spectrum). CMYK and HSV
conversions largely delegate to `QColor`; the CMYK pair is a transcription of
the Boost.GIL algorithm, copied rather than depended on.

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

**`Colour::from_rgba8()` has its green and blue channels swapped.** The
implementation passes `rgba8.blue` into the constructor's `green` parameter and
`rgba8.green` into `blue`. There are currently no callers anywhere in the tree,
so the bug is dormant — but it is a live trap for anyone who reaches for the
obvious-looking inverse of `to_rgba8()`. Fix it, or convert via
`QColor::fromRgba` / `from_qrgb` instead.

**Nothing is clamped on construction.** The constructor's own comment says
out-of-range components are left alone because OpenGL clamps for itself, so a
`Colour` can legitimately hold negative or greater-than-one components. Clamping
happens only at the boundaries where it must: `operator QColor` runs each
component through the file-local `clamp_zero_one`, `to_cmyk` clamps explicitly
(with a comment saying why), and `float_to_uint8` saturates on the way to
`rgba8_t`. `linearly_interpolate`, `modulate` and `pre_multiply_alpha` do no
clamping and no range checking on `position` either — passing a position outside
`[0, 1]` extrapolates rather than clamping. In `linearly_interpolate(first,
second, position)`, position 0 yields `first` and position 1 yields `second`;
getting that backwards is an easy way to invert a palette by accident.

**Size is a contract, not an implementation detail.** `sizeof(Colour)` must stay
16 bytes and `sizeof(rgba8_t)` 4 bytes, because both are passed to OpenGL and to
raw stream reads/writes as arrays. Do not add virtual functions, base classes
(even empty ones) or members to either. Related: `output_pixels`/`input_pixels`
`reinterpret_cast` an `rgba8_t*` to `char*` and do a single raw block transfer —
profiling showed the per-pixel `operator<<` to be far slower — so any layout
change silently corrupts serialised raster data. The `GPlatesUtils::Endian::swap`
specialisation for `rgba8_t` is an intentionally empty function for the same
reason: the four bytes are already in memory order, so byte-swapping would be
wrong.

**`rgba8_t`'s default constructor leaves the components uninitialised**, which is
deliberate (bulk pixel buffers) and documented, but means a default-constructed
`rgba8_t` holds garbage. Note also that `operator==`/`operator!=` are non-const
member functions taking a non-const reference, so they will not compile against
`const rgba8_t` operands.

**Named colours are functions, not variables.** `get_black()` and friends are
generated by the `DEFINE_COLOUR` macro and each returns a function-local static —
explicitly to dodge the static initialisation order fiasco, since some of these
are used to initialise other translation units' statics (`MonochromeAgeColourPalette`
does exactly this). Keep that pattern for any colour you add. Be aware the names
follow the HTML/X11 convention: `get_green()` is (0, 0.5, 0) and `get_lime()` is
the pure (0, 1, 0).

Smaller points:

- `operator==` compares with `GPlatesMaths::are_almost_exactly_equal` on each
  component, not bitwise; `operator!=` comes free from
  `boost::equality_comparable`.
- `to_hsv()` normalises Qt's convention of returning hue `-1` for achromatic
  colours to `0`, so downstream code can assume hue is in `[0, 1]`.
- `from_cmyk()` discards alpha entirely — the result always has the constructor
  default of 1.0. The CMYK round trip is therefore lossy for translucent colours.
- The free `pre_multiply_alpha(rgba8_t)` and the static
  `Colour::pre_multiply_alpha(const Colour&)` do the same thing in different
  arithmetic; the 8-bit one avoids float conversion and integer division by 255
  using the `((x+1)*257)>>16` trick, which is approximate. Do not "clean it up"
  into a division without re-checking the rounding.
- `Colour` is transcribable for sessions and projects, and its `transcribe()`
  writes the raw `d_rgba` array under the tag `"rgba"` — that tag and the array
  length are part of the saved-file format.

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
