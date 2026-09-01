# ReconstructScalarCoverageVisualLayerParams

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 245 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/ReconstructScalarCoverageVisualLayerParams.h` | C++ | 164 |
| `src/presentation/ReconstructScalarCoverageVisualLayerParams.cc` | C++ | 235 |

## Overview

`ReconstructScalarCoverageVisualLayerParams` holds the visual settings for a
reconstruct-scalar-coverage layer, but unlike the single-raster
`RasterVisualLayerParams`, a scalar coverage can expose several scalar types
at once (for example temperature and depth), so it keeps one
`RemappedColourPaletteParameters` per `ValueObjectType` in
`d_colour_palette_parameters_map`. Scalar type queries
(`get_current_scalar_type()`, `get_scalar_types()`) delegate straight through
to the app-logic `GPlatesAppLogic::ReconstructScalarCoverageLayerParams`,
obtained via a `dynamic_cast` on `get_layer_params()`; the "current" colour
palette accessors are thin wrappers that look up the palette for whatever
scalar type is currently selected.

Palette creation is deliberately lazy: `get_colour_palette_parameters()`
creates and caches a palette for a scalar type only the first time it is
asked for, since computing the statistics needed to auto-map a palette's
range can require reconstructing the coverage's full history. `handle_layer_modified()`
does not pre-create palettes for newly discovered scalar types — it only
prunes entries whose scalar type no longer exists, on the assumption that a
change in the underlying data does not by itself invalidate an already-chosen
colour palette; only an explicit `set_colour_palette_parameters()` call does
that.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::ReconstructScalarCoverageVisualLayerParams`](#gplatespresentationreconstructscalarcoveragevisuallayerparams) | class | [`VisualLayerParams`](VisualLayerParams.md) | — | 0 | — |

## Members

### `GPlatesPresentation::ReconstructScalarCoverageVisualLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructScalarCoverageVisualLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructScalarCoverageVisualLayerParams>` | public | — |
| `create( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | method | `non_null_ptr_type` | public | — |
| `get_current_colour_palette_parameters` | field | `RemappedColourPaletteParameters` | public | Gets, and creates if necessary, the current colour palette (associated with the current scalar type). |
| `set_current_colour_palette_parameters( const RemappedColourPaletteParameters &colour_palette_parameters)` | method | `void` | public | Sets the current colour palette (associated with the current scalar type). |
| `create_default_colour_palette_parameters()` | method | `GPlatesPresentation::RemappedColourPaletteParameters` | public | The default colour palette parameters. |
| `get_colour_palette_parameters` | field | `RemappedColourPaletteParameters` | public | Gets, and creates if necessary, the colour palette associated with the specified scalar type. |
| `set_colour_palette_parameters( const GPlatesPropertyValues::ValueObjectType &scalar_type, const RemappedColourPaletteParameters &colour_palette_parameters)` | method | `void` | public | Sets the colour palette associated with the specified scalar type. |
| `get_current_scalar_type` | field | `GPlatesPropertyValues::ValueObjectType` | public | Returns the currently selected scalar type. |
| `get_scalar_types( std::vector<GPlatesPropertyValues::ValueObjectType> &scalar_types)` | method | `void` | public | Returns the list of scalar types available in the scalar coverage features. |
| `accept_visitor( ConstVisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( VisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `handle_layer_modified( const GPlatesAppLogic::Layer &layer)` | method | `void` | public | — |
| `ReconstructScalarCoverageVisualLayerParams( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | constructor | `None` | protected | — |
| `colour_palette_parameters_map_type` | typedef | `std::map<GPlatesPropertyValues::ValueObjectType, RemappedColourPaletteParameters>` | private | Typedef for map from scalar type to colour palette parameters. |
| `d_colour_palette_parameters_map` | field | `colour_palette_parameters_map_type` | private | The colour palette(s) for this layer, whether set explicitly as loaded from a file, or auto-generated. |
| `create_colour_palette_parameters( const GPlatesPropertyValues::ValueObjectType &scalar_type)` | method | `RemappedColourPaletteParameters` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_RECONSTRUCTSCALARCOVERAGEVISUALLAYERPARAMS_H` | macro | `None` | — |

## Notes

`d_colour_palette_parameters_map` is `mutable` precisely because
`get_colour_palette_parameters()` (a `const` accessor) creates and inserts a
palette on first access rather than requiring the caller to pre-populate it.
`get_current_scalar_type()`, `get_scalar_types()` and
`create_colour_palette_parameters()` all assert (via `GPlatesGlobal::Assert<AssertionFailureException>`)
that the underlying `LayerParams` really is a `ReconstructScalarCoverageLayerParams`
— calling this class on the wrong kind of layer is a programming error, not a
recoverable condition.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) | qt-widgets | 44 |
| [qt-widgets/RasterLayerOptionsWidget](../qt-widgets/RasterLayerOptionsWidget.md) | qt-widgets | 11 |
| [presentation/ReconstructionGeometryRenderer](ReconstructionGeometryRenderer.md) | presentation | 4 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 3 |
| [app-logic/ReconstructScalarCoverageLayerParams](../app-logic/ReconstructScalarCoverageLayerParams.md) | app-logic | 2 |
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 2 |
| [gui/ExportRasterAnimationStrategy](../gui/ExportRasterAnimationStrategy.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/ReconstructScalarCoverageVisualLayerParams.h
python scripts/gpq.py def GPlatesPresentation::ReconstructScalarCoverageVisualLayerParams --body
python scripts/gpq.py uses ReconstructScalarCoverageVisualLayerParams --kind class
python scripts/gpq.py hier ReconstructScalarCoverageVisualLayerParams
```
