# ScalarField3DRenderParameters

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 93 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/ScalarField3DRenderParameters.h` | C++ | 513 |
| `src/view-operations/ScalarField3DRenderParameters.cc` | C++ | 425 |

## Overview

A plain value object holding every user-adjustable knob for 3D scalar field
visualisation, and the shared vocabulary between four subsystems that otherwise
have no business knowing about each other. `GPlatesQtWidgets::ScalarField3DLayerOptionsWidget`
writes it, `GPlatesPresentation::ScalarField3DVisualLayerParams` stores it by
value as the visual layer's persistent state,
`RenderedGeometryFactory::create_rendered_resolved_scalar_field_3d` copies it into
a `RenderedResolvedScalarField3D`, and `GPlatesOpenGL::GLScalarField3D` finally
turns the individual fields into GLSL uniforms for the ray-casting shaders. It
lives in `view-operations` rather than in `gui` or `opengl` because it is the one
piece all of them must agree on and none of them may depend on another for.

The nesting is not decoration — the nested structs are the units the renderer
actually consumes. `GLScalarField3D::render_isosurface` takes
`IsovalueParameters`, `DeviationWindowRenderOptions`, `DepthRestriction` and
`QualityPerformance` as separate arguments rather than the aggregate, so each
group corresponds to a coherent block of shader state. The four enums select
which of those blocks are live: `RenderMode` chooses isosurface versus cross
sections, and the two colour-mode enums decide whether the scalar palette, the
gradient palette or plain depth drives colouring — which is why both
`RemappedColourPaletteParameters` members are always present even though at most
one is in use at a time.

The other half of this file exists for session and project persistence. Every
nested struct is a `GPlatesScribe::Access` friend with its own `transcribe`, and
the four free `transcribe` overloads map the enums onto stable string ids through
`transcribe_enum_protocol`. The deliberate design here is graceful degradation:
each field is transcribed independently and, on failure, silently reset from a
static default-constructed instance, so a project written by a different GPlates
version loads with whatever it understood and defaults for the rest instead of
failing outright. `d_shader_test_variables` is not part of any of this — it is an
acknowledged development hook for poking arbitrary floats at the scalar field
shader.

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

- **Value semantics, no observers.** Copyable, no signals, no identity, no
  ownership of anything. Mutating a copy changes nothing;
  `ScalarField3DVisualLayerParams` is what actually notifies and triggers a
  redraw, so a setter called on a temporary is a silent no-op.
- **Adding an enumerator without updating `transcribe` breaks sessions.** The
  header says so at each enum, and it is enforced only by that comment: the
  `EnumValue` tables in the `.cc` are the complete wire vocabulary, and a value
  missing from a table cannot be written or read. The string ids are the format —
  renaming an *enumerator* is safe, changing its **string** is not, and neither is
  reordering, since the ids are matched by name. The trailing `NUM_*` sentinels
  are deliberately absent from the tables and must never be persisted.
- **Transcription never fails, which cuts both ways.** Every nested `transcribe`
  returns `TRANSCRIBE_SUCCESS` unconditionally and substitutes a value from a
  function-local `static const` default-constructed instance for any field it
  could not read. That is what makes old and new project files interoperate, but
  it also means a corrupt or renamed field is indistinguishable from an absent one
  and silently becomes the default. If you rename a transcribe key you will not
  get an error, you will get defaults.
- **Nothing here is validated.** The setters and the twelve-argument constructor
  assign straight through. No check that `min_depth_radius_restriction <=
  max_depth_radius_restriction`, that the opacities lie in [0,1], that
  `sampling_rate` or `bisection_iterations` are non-zero, or that `isovalue2`
  relates sensibly to `isovalue1`. Range enforcement lives entirely in the layer
  options widget; anything constructing these values programmatically inherits
  that responsibility.
- **`symmetric_deviation` is advisory.** The struct stores lower and upper
  deviations for both isovalues independently whatever the flag says; keeping them
  in step is the caller's job.
- **Default construction is not cheap.** The default constructor builds both
  colour palettes through `create_default_scalar_colour_palette_parameters` and
  `create_default_gradient_colour_palette_parameters`, each of which constructs a
  built-in palette and wraps it in a `RemappedColourPaletteParameters`. The nested
  structs' `transcribe` methods each hold a function-local static default instance
  for the same reason — do not default-construct one of these per frame.
- The header deliberately includes only `scribe/Transcribe.h`, not `Scribe.h`;
  keep the heavyweight include confined to the `.cc`.

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
