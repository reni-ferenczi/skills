# RemappedColourPaletteParameters

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 38 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/RemappedColourPaletteParameters.h` | C++ | 324 |
| `src/presentation/RemappedColourPaletteParameters.cc` | C++ | 254 |

## Overview

`GPlatesPresentation::RemappedColourPaletteParameters` bundles a real-valued `GPlatesGui::RasterColourPalette` with an optional remapping of its input range, so that a layer can show the palette either over its natural (loaded or default) range or stretched/compressed to a range chosen by the user. It keeps the colour palette itself (loaded from a CPT file, a built-in `GPlatesGui::BuiltinColourPaletteType`, or auto-generated) separate from the palette *range*, tracking an unmapped `ColourPaletteInfo` and a mapped `ColourPaletteInfo` side by side; `get_colour_palette()` and `get_palette_range()` transparently return whichever one is current.

The class exists to back `RemappedColourPaletteWidget` and to be the piece of visual-layer state that widget edits — raster, scalar-field and reconstructed-scalar-coverage layers each keep one of these for their colour ramps. `set_deviation_from_mean()` records a "number of standard deviations" value that the widget uses to derive a mapped range from a scalar field's statistics (`[mean - deviation, mean + deviation]` for colour-by-scalar, `[-mean - deviation, mean + deviation]` for colour-by-gradient); this class only stores the parameter, it does not compute the mean itself.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::RemappedColourPaletteParameters`](#gplatespresentationremappedcolourpaletteparameters) | class | — | — | 0 | Manages a real-valued colour palette whose input range can be remapped. |

## Members

### `GPlatesPresentation::RemappedColourPaletteParameters`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DEFAULT_DEVIATION_FROM_MEAN` | field | `double` | public | — |
| `RemappedColourPaletteParameters( const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &default_colour_palette, const double &default_deviation_from_mean = DEFAULT_DEVIATION_FROM_MEAN)` | constructor | `None` | public | Constructor uses the specified default colour palette and deviation-from-mean parameter. |
| `get_colour_palette()` | method | `GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type` | public | Returns the colour palette - this is the mapped palette if mapping is currently used. |
| `get_palette_range` | field | `std::pair<double, double>` | public | Returns the palette range - this is the mapped range if mapping is currently used. |
| `get_colour_palette_filename()` | method | `QString` | public | Returns the filename of the CPT file from which the current colour palette was loaded. |
| `get_colour_palette_name()` | method | `QString` | public | Returns the name of the current colour palette. |
| `get_builtin_colour_palette_type()` | method | `boost::optional<GPlatesGui::BuiltinColourPaletteType>` | public | Returns the built-in colour palette type (if current palette was loaded via load\_builtin\_colour\_palette). |
| `set_builtin_colour_palette_parameters( const GPlatesGui::BuiltinColourPaletteType::Parameters &builtin_colour_palette_parameters)` | method | `void` | public | Sets the built-in colour palette parameters. |
| `use_default_colour_palette()` | method | `void` | public | Causes the current colour palette to be the auto-generated default palette, and sets the filename field to be the empty string. |
| `load_colour_palette( const QString &filename, GPlatesFileIO::ReadErrorAccumulation &read_errors, bool allow_integer_colour_palette = false)` | method | `bool` | public | Same as set\_colour\_palette but also loads the colour palette from the file filename. |
| `load_builtin_colour_palette( const GPlatesGui::BuiltinColourPaletteType &builtin_colour_palette_type)` | method | `void` | public | Similar to load\_colour\_palette except loads an built-in colour palette type. |
| `map_palette_range( double lower_bound, double upper_bound)` | method | `bool` | public | Remaps the value range of the colour palette (the palette colours remain unchanged). |
| `unmap_palette_range()` | method | `void` | public | Unmaps the current colour palette. |
| `is_palette_range_mapped()` | method | `bool` | public | Returns true if the palette range is currently mapped. |
| `set_deviation_from_mean( const double &deviation_from_mean)` | method | `void` | public | Sets the deviation-from-mean parameter (number of standard deviations). |
| `ColourPaletteInfo` | struct | `None` | private | — |
| `d_default_colour_palette_info` | field | `ColourPaletteInfo` | private | — |
| `d_colour_palette_filename` | field | `QString` | private | The filename the colour palette was loaded from. |
| `d_colour_palette_name` | field | `QString` | private | The name of the colour palette. |
| `d_builtin_colour_palette_type` | field | `boost::optional<GPlatesGui::BuiltinColourPaletteType>` | private | The built-in colour palette (if one is currently being used). |
| `d_builtin_colour_palette_parameters` | field | `GPlatesGui::BuiltinColourPaletteType::Parameters` | private | The built-in colour palette parameters. |
| `d_deviation_from_mean` | field | `double` | private | — |
| `d_unmapped_colour_palette_info` | field | `ColourPaletteInfo` | private | The unmapped palette loaded from the CPT file (or the default palette). |
| `d_mapped_colour_palette_info` | field | `ColourPaletteInfo` | private | The mapped palette (a mapped version of d\_unmapped\_colour\_palette\_info). |
| `d_is_currently_mapped` | field | `bool` | private | — |
| `set_colour_palette( const QString &filename, const QString &name, boost::optional<GPlatesGui::BuiltinColourPaletteType> builtin_colour_palette_type, const GPlatesGui::RasterColourPalette::non_null_ptr_to_const_type &colour_palette, const std::pair<double, double> &palette_range)` | method | `bool` | private | Sets the current colour palette to be one that has been loaded from a file. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_DEVIATION_FROM_MEAN` | variable | `double` | — |
| `GPLATES_PRESENTATION_REMAPPEDCOLOURPALETTEPARAMETERS_H` | macro | `None` | — |

## Notes

- Loading or switching the underlying colour palette (`load_colour_palette`, `load_builtin_colour_palette`, `use_default_colour_palette`) preserves an existing mapping by re-applying `map_palette_range()` with the previous mapped bounds to the new palette; if that re-mapping fails, the change is rolled back to the previous filename, name, built-in type and unmapped palette so the object never ends up with a mapped range that does not correspond to any palette.
- An integer (categorical) colour palette cannot be mapped: `map_palette_range()` fails and leaves the palette unmapped, and `load_colour_palette()` only allows loading an integer palette when the raster is integer-valued and no mapping is in effect.
- `map_palette_range()` nudges `lower_bound`/`upper_bound` apart by a relative `1e-6` when they compare equal, so the palette always has a non-zero range.
- `get_mapped_palette_range()` returns the most recently mapped range even when the palette is currently unmapped, so callers can restore a previous mapping without having to cache the bounds themselves.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 48 |
| [view-operations/ScalarField3DRenderParameters](../view-operations/ScalarField3DRenderParameters.md) | view-operations | 33 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 25 |
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 24 |
| [presentation/ReconstructScalarCoverageVisualLayerParams](ReconstructScalarCoverageVisualLayerParams.md) | presentation | 18 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 17 |
| [qt-widgets/RemappedColourPaletteWidget](../qt-widgets/RemappedColourPaletteWidget.md) | qt-widgets | 12 |
| [presentation/ScalarField3DVisualLayerParams](ScalarField3DVisualLayerParams.md) | presentation | 10 |
| [presentation/RasterVisualLayerParams](RasterVisualLayerParams.md) | presentation | 9 |
| [gui/MapRenderedGeometryCollectionPainter](../gui/MapRenderedGeometryCollectionPainter.md) | gui | 5 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 4 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/RemappedColourPaletteParameters.h
python scripts/gpq.py def GPlatesPresentation::RemappedColourPaletteParameters --body
python scripts/gpq.py uses RemappedColourPaletteParameters --kind class
python scripts/gpq.py hier RemappedColourPaletteParameters
```
