# ScalarField3DRenderParameters

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 93 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/ScalarField3DRenderParameters.h` | C++ | 513 |
| `src/view-operations/ScalarField3DRenderParameters.cc` | C++ | 425 |

## Overview

[[[PROSE overview unit=view-operations/ScalarField3DRenderParameters tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::ScalarField3DRenderParameters`](#gplatesviewoperationsscalarfield3drenderparameters) | class | — | — | 0 | — |

## Members

### `GPlatesViewOperations::ScalarField3DRenderParameters`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RenderMode` | enum | `None` | public | The scalar field rendering mode. |
| `IsosurfaceDeviationWindowMode` | enum | `None` | public | The isosurface deviation window mode. |
| `IsosurfaceColourMode` | enum | `None` | public | The isosurface colouring mode. |
| `CrossSectionColourMode` | enum | `None` | public | The cross-sections colouring mode. |
| `IsovalueParameters` | struct | `None` | public | Isovalue(s) and associated deviation windows. |
| `DeviationWindowRenderOptions` | struct | `None` | public | Deviation window render options. |
| `SurfacePolygonsMask` | struct | `None` | public | Surface polygons mask parameters. |
| `DepthRestriction` | struct | `None` | public | Restricting depth range visualised for scalar field. |
| `QualityPerformance` | struct | `None` | public | Parameters affecting quality/performance trade-off. |
| `ScalarField3DRenderParameters()` | constructor | `None` | public | — |
| `ScalarField3DRenderParameters( RenderMode render_mode, IsosurfaceDeviationWindowMode isosurface_deviation_window_mode, IsosurfaceColourMode isosurface_colour_mode, CrossSectionColourMode cross_section_colour_mode, const GPlatesPresentation::RemappedColourPaletteParameters &scalar_colour_palette_parameters, const GPlate ...` | constructor | `None` | public | — |
| `get_render_mode()` | method | `RenderMode` | public | — |
| `set_render_mode( RenderMode render_mode)` | method | `void` | public | — |
| `get_isosurface_deviation_window_mode()` | method | `IsosurfaceDeviationWindowMode` | public | — |
| `set_isosurface_deviation_window_mode( IsosurfaceDeviationWindowMode isosurface_deviation_window_mode)` | method | `void` | public | — |
| `get_isosurface_colour_mode()` | method | `IsosurfaceColourMode` | public | — |
| `set_isosurface_colour_mode( IsosurfaceColourMode isosurface_colour_mode)` | method | `void` | public | — |
| `get_cross_section_colour_mode()` | method | `CrossSectionColourMode` | public | — |
| `set_cross_section_colour_mode( CrossSectionColourMode cross_section_colour_mode)` | method | `void` | public | — |
| `create_default_scalar_colour_palette_parameters()` | method | `GPlatesPresentation::RemappedColourPaletteParameters` | public | The default scalar colour palette parameters. |
| `set_scalar_colour_palette_parameters( const GPlatesPresentation::RemappedColourPaletteParameters &scalar_colour_palette_parameters)` | method | `void` | public | — |
| `create_default_gradient_colour_palette_parameters()` | method | `GPlatesPresentation::RemappedColourPaletteParameters` | public | The default gradient colour palette parameters. |
| `set_gradient_colour_palette_parameters( const GPlatesPresentation::RemappedColourPaletteParameters &gradient_colour_palette_parameters)` | method | `void` | public | — |
| `set_isovalue_parameters( const IsovalueParameters &isovalue_parameters)` | method | `void` | public | — |
| `set_deviation_window_render_options( const DeviationWindowRenderOptions &deviation_window_render_options)` | method | `void` | public | — |
| `set_surface_polygons_mask( const SurfacePolygonsMask &surface_polygons_mask)` | method | `void` | public | — |
| `set_depth_restriction( const DepthRestriction &depth_restriction)` | method | `void` | public | — |
| `set_quality_performance( const QualityPerformance &quality_performance)` | method | `void` | public | — |
| `set_shader_test_variables( const std::vector<float> &shader_test_variables)` | method | `void` | public | — |
| `d_render_mode` | field | `RenderMode` | private | — |
| `d_isosurface_deviation_window_mode` | field | `IsosurfaceDeviationWindowMode` | private | — |
| `d_isosurface_colour_mode` | field | `IsosurfaceColourMode` | private | — |
| `d_cross_section_colour_mode` | field | `CrossSectionColourMode` | private | — |
| `d_scalar_colour_palette_parameters` | field | `GPlatesPresentation::RemappedColourPaletteParameters` | private | The colour palette used to colour by scalar value. |
| `d_gradient_colour_palette_parameters` | field | `GPlatesPresentation::RemappedColourPaletteParameters` | private | The colour palette used to colour by gradient magnitude. |
| `d_isovalue_parameters` | field | `IsovalueParameters` | private | — |
| `d_deviation_window_render_options` | field | `DeviationWindowRenderOptions` | private | — |
| `d_surface_polygons_mask` | field | `SurfacePolygonsMask` | private | — |
| `d_depth_restriction` | field | `DepthRestriction` | private | — |
| `d_quality_performance` | field | `QualityPerformance` | private | — |
| `d_shader_test_variables` | field | `std::vector<float>` | private | Used during test/development of the scalar field shader program. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEW_OPERATIONS_SCALARFIELD3DRENDERPARAMETERS_H` | macro | `None` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, ScalarField3DRenderParameters::RenderMode &render_mode, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `transcribe( GPlatesScribe::Scribe &scribe, ScalarField3DRenderParameters::IsosurfaceDeviationWindowMode &isosurface_deviation_window_mode, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `transcribe( GPlatesScribe::Scribe &scribe, ScalarField3DRenderParameters::IsosurfaceColourMode &isosurface_colour_mode, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `transcribe( GPlatesScribe::Scribe &scribe, ScalarField3DRenderParameters::CrossSectionColourMode &cross_section_colour_mode, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

[[[PROSE notes unit=view-operations/ScalarField3DRenderParameters tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ScalarField3DLayerOptionsWidget](../qt-widgets/ScalarField3DLayerOptionsWidget.md) | qt-widgets | 340 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 190 |
| [presentation/ScalarField3DVisualLayerParams](../presentation/ScalarField3DVisualLayerParams.md) | presentation | 72 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 30 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 18 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 9 |
| [view-operations/RenderedResolvedScalarField3D](RenderedResolvedScalarField3D.md) | view-operations | 4 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 3 |
| [view-operations/RenderedGeometryFactory](RenderedGeometryFactory.md) | view-operations | 3 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/ScalarField3DRenderParameters.h
python scripts/gpq.py def GPlatesViewOperations::ScalarField3DRenderParameters --body
python scripts/gpq.py uses ScalarField3DRenderParameters --kind class
python scripts/gpq.py hier ScalarField3DRenderParameters
```
