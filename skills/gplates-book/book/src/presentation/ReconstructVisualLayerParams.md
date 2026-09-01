# ReconstructVisualLayerParams

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 291 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/ReconstructVisualLayerParams.h` | C++ | 278 |
| `src/presentation/ReconstructVisualLayerParams.cc` | C++ | 306 |

## Overview

`ReconstructVisualLayerParams` holds the visual settings for a reconstruct
layer, covering three largely independent concerns: VGP (virtual geomagnetic
pole) visibility and time-window filtering, fill styling (polygon/polyline
fill, opacity and intensity, combined into a modulate colour the same way as
`RasterVisualLayerParams::get_modulate_colour()`), and topological
reconstruction display options (topology-reconstructed feature geometries,
strain accumulation and its display scale). `show_vgp()` is the one method
with real logic: given the current reconstruction time and a VGP's age, it
decides visibility according to `d_vgp_visibility_setting` —
`ALWAYS_VISIBLE`, a fixed `TIME_WINDOW` between `d_vgp_earliest_time` and
`d_vgp_latest_time`, or `DELTA_T_AROUND_AGE`, a window of `±d_vgp_delta_t`
centred on the VGP's own age.

The free `transcribe()` overload for `VGPVisibilitySetting` exists because the
enum is serialised by `Scribe` when saving sessions and projects; its comment
warns that any new enumerator must be added there too.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::ReconstructVisualLayerParams`](#gplatespresentationreconstructvisuallayerparams) | class | [`VisualLayerParams`](VisualLayerParams.md) | — | 0 | — |

## Members

### `GPlatesPresentation::ReconstructVisualLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructVisualLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructVisualLayerParams>` | public | — |
| `VGPVisibilitySetting` | enum | `None` | public | — |
| `create( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | method | `non_null_ptr_type` | public | — |
| `get_vgp_visibility_setting()` | method | `VGPVisibilitySetting` | public | — |
| `set_vgp_visibility_setting( VGPVisibilitySetting setting)` | method | `void` | public | — |
| `get_vgp_earliest_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | public | — |
| `set_vgp_earliest_time( const GPlatesPropertyValues::GeoTimeInstant &earliest_time)` | method | `void` | public | — |
| `get_vgp_latest_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | public | — |
| `set_vgp_latest_time( const GPlatesPropertyValues::GeoTimeInstant &latest_time)` | method | `void` | public | — |
| `get_vgp_delta_t()` | method | `double` | public | — |
| `set_vgp_delta_t( double vgp_delta_t)` | method | `void` | public | — |
| `get_vgp_draw_circular_error()` | method | `bool` | public | — |
| `set_vgp_draw_circular_error( bool draw)` | method | `void` | public | — |
| `show_vgp( double current_time, const boost::optional<double> &age)` | method | `bool` | public | — |
| `set_fill_polygons( bool fill)` | method | `void` | public | — |
| `get_fill_polygons()` | method | `bool` | public | — |
| `set_fill_polylines( bool fill)` | method | `void` | public | — |
| `get_fill_polylines()` | method | `bool` | public | — |
| `set_fill_opacity( const double &opacity)` | method | `void` | public | Sets the opacity of filled primitives. |
| `get_fill_opacity()` | method | `double` | public | Gets the opacity of filled primitives. |
| `set_fill_intensity( const double &intensity)` | method | `void` | public | Sets the intensity of filled primitives. |
| `get_fill_intensity()` | method | `double` | public | Gets the intensity of filled primitives. |
| `get_fill_modulate_colour()` | method | `GPlatesGui::Colour` | public | Returns the filled primitives modulate colour. |
| `set_show_topology_reconstructed_feature_geometries( bool show_topology_reconstructed_feature_geometries)` | method | `void` | public | Whether to show topology-reconstructed feature geometries. |
| `get_show_topology_reconstructed_feature_geometries()` | method | `bool` | public | — |
| `set_show_strain_accumulation( bool show_strain_accumulation)` | method | `void` | public | Whether to show strain accumulation at the points of deformed feature geometries. |
| `get_show_strain_accumulation()` | method | `bool` | public | — |
| `set_strain_accumulation_scale( const double &strain_accumulation_scale)` | method | `void` | public | — |
| `get_strain_accumulation_scale()` | method | `double` | public | — |
| `accept_visitor( ConstVisualLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in VirtualLayerParams base. |
| `accept_visitor( VisualLayerParamsVisitor &visitor)` | method | `void` | public | Override of virtual method in VirtualLayerParams base. |
| `ReconstructVisualLayerParams( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | constructor | `None` | protected | — |
| `INITIAL_VGP_DELTA_T` | field | `double` | private | — |
| `d_vgp_visibility_setting` | field | `VGPVisibilitySetting` | private | Enum indicating what sort of VGP visibility we have. |
| `d_vgp_earliest_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | Begin time used when the TIME\_WINDOW VGPVisibilitySetting is selected. |
| `d_vgp_latest_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | End time used when the TIME\_WINDOW VGPVisibilitySetting is selected. |
| `d_vgp_delta_t` | field | `GPlatesMaths::real_t` | private | Delta used for time window around VGP age. |
| `d_vgp_draw_circular_error` | field | `bool` | private | — |
| `d_fill_polygons` | field | `bool` | private | — |
| `d_fill_polylines` | field | `bool` | private | — |
| `d_fill_opacity` | field | `double` | private | The opacity of filled primitives in the range \[0,1\]. |
| `d_fill_intensity` | field | `double` | private | The intensity of filled primitives in the range \[0,1\]. |
| `d_show_topology_reconstructed_feature_geometries` | field | `bool` | private | — |
| `d_show_show_strain_accumulation` | field | `bool` | private | — |
| `d_strain_accumulation_scale` | field | `double` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `INITIAL_VGP_DELTA_T` | variable | `double` | — |
| `GPLATES_PRESENTATION_RECONSTRUCTVISUALLAYERPARAMS_H` | macro | `None` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, ReconstructVisualLayerParams::VGPVisibilitySetting &vgp_visibility_setting, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |

## Notes

Any new `VGPVisibilitySetting` enumerator must also be handled in the
`transcribe()` free function, per the comment on the enum, or saved
sessions/projects using it will not round-trip correctly. `d_fill_opacity`
and `d_fill_intensity` are documented as `[0,1]` but, as in
`RasterVisualLayerParams`, setters do not clamp them. `d_vgp_delta_t` is
stored as `GPlatesMaths::real_t` (a value with epsilon-tolerant comparisons)
even though the public getter/setter use `double`.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/SetVGPVisibilityDialog](../qt-widgets/SetVGPVisibilityDialog.md) | qt-widgets | 46 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 41 |
| [qt-widgets/ReconstructLayerOptionsWidget](../qt-widgets/ReconstructLayerOptionsWidget.md) | qt-widgets | 19 |
| [qt-widgets/SetTopologyReconstructionParametersDialog](../qt-widgets/SetTopologyReconstructionParametersDialog.md) | qt-widgets | 18 |
| [presentation/ReconstructionGeometryRenderer](ReconstructionGeometryRenderer.md) | presentation | 17 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 6 |
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 2 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/ReconstructVisualLayerParams.h
python scripts/gpq.py def GPlatesPresentation::ReconstructVisualLayerParams --body
python scripts/gpq.py uses ReconstructVisualLayerParams --kind class
python scripts/gpq.py hier ReconstructVisualLayerParams
```
