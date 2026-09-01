# ColourScaleGenerator

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1035 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ColourScaleGenerator.h` | C++ | 95 |
| `src/gui/ColourScaleGenerator.cc` | C++ | 816 |

## Overview

[[[PROSE overview unit=gui/ColourScaleGenerator tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::round_up`](#anonymousround_up) | typedef | — | — | 0 | — |
| [`(anonymous)::round_down`](#anonymousround_down) | typedef | — | — | 0 | — |
| [`(anonymous)::ColourPaletteConverter`](#anonymouscolourpaletteconverter) | struct | — | `<typename KeyType>` | 0 | — |
| [`(anonymous)::ColourPaletteConverter<GPlatesMaths::Real>`](#anonymouscolourpaletteconvertergplatesmathsreal) | struct | — | `<>` | 0 | — |
| [`(anonymous)::ColourScaleGenerator`](#anonymouscolourscalegenerator) | class | `boost::static_visitor<bool>` | — | 0 | — |
| [`GPlatesGui::ColourScale::annotation_type`](#gplatesguicolourscaleannotation_type) | typedef | — | — | 0 | — |
| [`GPlatesGui::ColourScale::annotations_seq_type`](#gplatesguicolourscaleannotations_seq_type) | typedef | — | — | 0 | — |
| [`GPlatesGui::ColourScale::Annotations`](#gplatesguicolourscaleannotations) | struct | — | — | 0 | Contains a \*reference\* to the caller's sequence of annotations to write to, and the annotation height to be used. |

## Members

### `(anonymous)::round_up`

*None.*

### `(anonymous)::round_down`

*None.*

### `(anonymous)::ColourPaletteConverter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `GPlatesGui::StaticCastConverter<KeyType, double>` | public | — |

### `(anonymous)::ColourPaletteConverter<GPlatesMaths::Real>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `GPlatesGui::RealToBuiltInConverter<double>` | public | — |

### `(anonymous)::ColourScaleGenerator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CHECKERBOARD_GRID_SIZE` | field | `int` | public | Grid size of transparent checkerboard pattern. |
| `ColourScaleGenerator( QPixmap &colour_scale_pixmap, QPixmap &disabled_colour_scale_pixmap, int pixmap_width, int pixmap_height, boost::optional<double> use_log_scale, boost::optional<GPlatesGui::ColourScale::Annotations> annotations)` | constructor | `None` | public | — |
| `operator()( const GPlatesGui::RasterColourPalette::empty &)` | operator | `bool` | public | — |
| `operator()( const GPlatesUtils::non_null_intrusive_ptr<ColourPaletteType> &colour_palette)` | operator | `bool` | public | — |
| `RangeVisitor` | class | `None` | private | Extract the range of values covered by a colour palette, which is also returned, adapted into an integer colour palette. |
| `LinearInterpolator` | class | `None` | private | Interpolate linearly. |
| `LogInterpolator` | class | `None` | private | Interpolate such that colours are uniformly spaced in log space. |
| `d_colour_scale_pixmap` | field | `QPixmap` | private | — |
| `d_disabled_colour_scale_pixmap` | field | `QPixmap` | private | — |
| `d_pixmap_width` | field | `int` | private | — |
| `d_pixmap_height` | field | `int` | private | — |
| `d_use_log_scale` | field | `boost::optional<double>` | private | — |
| `d_annotations` | field | `boost::optional<GPlatesGui::ColourScale::Annotations>` | private | — |

### `GPlatesGui::ColourScale::annotation_type`

*None.*

### `GPlatesGui::ColourScale::annotations_seq_type`

*None.*

### `GPlatesGui::ColourScale::Annotations`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Annotations( annotations_seq_type &annotations_, int annotation_height_)` | constructor | `None` | public | — |
| `annotations` | field | `annotations_seq_type` | public | — |
| `annotation_height` | field | `int` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_double_value( double d)` | function | `double` | — |
| `get_double_value( GPlatesMaths::Real r)` | function | `double` | — |
| `calculate_linear_annotation_multiplier( double range, int max_rows)` | function | `double` | Calculates the number that the annotations should be a multiple of. |
| `fill_colour_scale( QPainter &painter, QPainter &disabled_painter, const InterpolatorType &interpolator, const GPlatesGui::ColourPalette<double>::non_null_ptr_type &adapted_colour_palette, int pixmap_width, int pixmap_height)` | function | `void` | — |
| `GPLATES_GUI_COLOURSCALEGENERATOR_H` | macro | `None` | — |
| `generate( const RasterColourPalette::non_null_ptr_to_const_type &colour_palette, QPixmap &colour_scale_pixmap, QPixmap &disabled_colour_scale_pixmap, int pixmap_width, int pixmap_height, boost::optional<double> use_log_scale = boost::none, boost::optional<Annotations> annotations = boost::none)` | function | `bool` | Generate a pixmap from a colour palette. |

## Notes

[[[PROSE notes unit=gui/ColourScaleGenerator tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ColourScaleWidget](../qt-widgets/ColourScaleWidget.md) | qt-widgets | 9 |
| [qt-widgets/ColourScaleButton](../qt-widgets/ColourScaleButton.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ColourScaleGenerator.h
python scripts/gpq.py def (anonymous)::ColourScaleGenerator --body
python scripts/gpq.py uses ColourScaleGenerator --kind class
python scripts/gpq.py hier ColourScaleGenerator
```
