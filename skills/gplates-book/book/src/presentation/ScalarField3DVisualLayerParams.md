# ScalarField3DVisualLayerParams

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 22 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/ScalarField3DVisualLayerParams.h` | C++ | 426 |
| `src/presentation/ScalarField3DVisualLayerParams.cc` | C++ | 201 |

## Overview

`GPlatesPresentation::ScalarField3DVisualLayerParams` is the `VisualLayerParams` for a scalar-field-3D layer: it wraps a `GPlatesViewOperations::ScalarField3DRenderParameters` (render mode, iso-surface and cross-section colour modes, isovalue and depth-restriction settings, two `RemappedColourPaletteParameters` for the scalar and gradient colour ramps) and forwards most of the get/set API straight through to it via `set_scalar_field_3d_render_parameters()` and the individual accessors.

Because several of those render parameters depend on statistics of the loaded scalar field (mean, standard deviation, depth range) rather than on anything the GUI can supply up front, `handle_layer_modified()` initialises the scalar and gradient colour palette ranges, the isovalue and the depth restriction lazily, the first time the underlying `GPlatesAppLogic::ScalarField3DLayerParams` reports that field data is ready. Each of the four `*_initialised_from_scalar_field` flags latches independently so that this happens exactly once per layer and does not clobber values the user has since changed by hand.

The constructor also determines, via `determine_if_surface_polygons_mask_supported()`, whether the active OpenGL context can support the "surface polygons mask" rendering feature, and disables it up front if not.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::ScalarField3DVisualLayerParams`](#gplatespresentationscalarfield3dvisuallayerparams) | class | [`VisualLayerParams`](VisualLayerParams.md) | — | 0 | — |

## Members

### `GPlatesPresentation::ScalarField3DVisualLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ScalarField3DVisualLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ScalarField3DVisualLayerParams>` | public | — |
| `create( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params, GPlatesPresentation::ViewState &view_state)` | method | `non_null_ptr_type` | public | — |
| `accept_visitor( ConstVisualLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in VirtualLayerParams base. |
| `accept_visitor( VisualLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in VirtualLayerParams base. |
| `handle_layer_modified( const GPlatesAppLogic::Layer &layer)` | method | `void` | public | Override of virtual method in VisualLayerParams base. |
| `set_scalar_field_3d_render_parameters( const GPlatesViewOperations::ScalarField3DRenderParameters &scalar_field_3d_render_parameters)` | method | `void` | public | Sets all parameters as a single ScalarField3DRenderParameters object for convenience. |
| `get_render_mode()` | method | `GPlatesViewOperations::ScalarField3DRenderParameters::RenderMode` | public | Returns the current render mode. |
| `set_render_mode( GPlatesViewOperations::ScalarField3DRenderParameters::RenderMode render_mode)` | method | `void` | public | Sets the current render mode. |
| `get_isosurface_deviation_window_mode()` | method | `GPlatesViewOperations::ScalarField3DRenderParameters::IsosurfaceDeviationWindowMode` | public | Returns the current iso-surface window deviation mode. |
| `set_isosurface_deviation_window_mode( GPlatesViewOperations::ScalarField3DRenderParameters::IsosurfaceDeviationWindowMode isosurface_deviation_window_mode)` | method | `void` | public | Sets the current iso-surface window deviation mode. |
| `get_isosurface_colour_mode()` | method | `GPlatesViewOperations::ScalarField3DRenderParameters::IsosurfaceColourMode` | public | Returns the current iso-surface colour mode. |
| `set_isosurface_colour_mode( GPlatesViewOperations::ScalarField3DRenderParameters::IsosurfaceColourMode isosurface_colour_mode)` | method | `void` | public | Sets the current iso-surface colour mode. |
| `get_cross_section_colour_mode()` | method | `GPlatesViewOperations::ScalarField3DRenderParameters::CrossSectionColourMode` | public | Returns the current cross-section colour mode. |
| `set_cross_section_colour_mode( GPlatesViewOperations::ScalarField3DRenderParameters::CrossSectionColourMode cross_section_colour_mode)` | method | `void` | public | Sets the current cross-section colour mode. |
| `create_default_scalar_colour_palette_parameters()` | method | `GPlatesPresentation::RemappedColourPaletteParameters` | public | The default scalar colour palette parameters. |
| `set_scalar_colour_palette_parameters( const GPlatesPresentation::RemappedColourPaletteParameters &scalar_colour_palette_parameters)` | method | `void` | public | Sets the current scalar colour palette. |
| `create_default_gradient_colour_palette_parameters()` | method | `GPlatesPresentation::RemappedColourPaletteParameters` | public | The default gradient colour palette parameters. |
| `set_gradient_colour_palette_parameters( const GPlatesPresentation::RemappedColourPaletteParameters &gradient_colour_palette_parameters)` | method | `void` | public | Sets the current gradient colour palette. |
| `set_isovalue_parameters( const GPlatesViewOperations::ScalarField3DRenderParameters::IsovalueParameters &isovalue_parameters)` | method | `void` | public | Sets the current isovalue parameters. |
| `set_deviation_window_render_options( const GPlatesViewOperations::ScalarField3DRenderParameters::DeviationWindowRenderOptions &deviation_window_render_options)` | method | `void` | public | — |
| `is_surface_polygons_mask_supported()` | method | `bool` | public | Returns whether the runtime graphics hardware can support surface polygons mask. |
| `set_surface_polygons_mask( GPlatesViewOperations::ScalarField3DRenderParameters::SurfacePolygonsMask surface_polygons_mask)` | method | `void` | public | — |
| `set_depth_restriction( const GPlatesViewOperations::ScalarField3DRenderParameters::DepthRestriction &depth_restriction)` | method | `void` | public | — |
| `set_quality_performance( const GPlatesViewOperations::ScalarField3DRenderParameters::QualityPerformance &quality_performance)` | method | `void` | public | — |
| `set_shader_test_variables( const std::vector<float> &shader_test_variables)` | method | `void` | public | Optional test variables to use during GLScalarField3D shader program development. |
| `ScalarField3DVisualLayerParams( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params, GPlatesPresentation::ViewState &view_state)` | constructor | `None` | protected | — |
| `d_scalar_field_3d_render_parameters` | field | `GPlatesViewOperations::ScalarField3DRenderParameters` | private | — |
| `d_is_surface_polygons_mask_supported` | field | `bool` | private | — |
| `d_scalar_colour_palette_parameters_initialised_from_scalar_field` | field | `bool` | private | — |
| `d_gradient_colour_palette_parameters_initialised_from_scalar_field` | field | `bool` | private | — |
| `d_isovalue_parameters_initialised_from_scalar_field` | field | `bool` | private | — |
| `d_depth_restriction_initialised_from_scalar_field` | field | `bool` | private | — |
| `disable_surface_polygons_mask_if_not_supported()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `determine_if_surface_polygons_mask_supported( ViewState &view_state)` | function | `bool` | Returns true if 3D scalar fields support 'surface polygons mask'. |
| `GPLATES_PRESENTATION_SCALARFIELD3DVISUALLAYERPARAMS_H` | macro | `None` | — |

## Notes

- `is_surface_polygons_mask_supported()` reflects a one-time OpenGL capability check made when the object was constructed (it queries the active `GPlatesOpenGL::GLContext`); it is not re-evaluated later, and `set_surface_polygons_mask()` is expected to respect it rather than force the feature on when unsupported.
- The scalar/gradient palette range, isovalue and depth-restriction initialisation in `handle_layer_modified()` only fires once per flag: once a value has been derived from the scalar field's statistics, later calls leave it alone even if the field is reloaded, so a changed field does not silently re-map a palette the user has already adjusted.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 151 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 19 |
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 5 |
| [presentation/ReconstructionGeometryRenderer](ReconstructionGeometryRenderer.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/ScalarField3DVisualLayerParams.h
python scripts/gpq.py def GPlatesPresentation::ScalarField3DVisualLayerParams --body
python scripts/gpq.py uses ScalarField3DVisualLayerParams --kind class
python scripts/gpq.py hier ScalarField3DVisualLayerParams
```
