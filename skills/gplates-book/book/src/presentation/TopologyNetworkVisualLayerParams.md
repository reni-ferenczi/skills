# TopologyNetworkVisualLayerParams

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 149 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/TopologyNetworkVisualLayerParams.h` | C++ | 475 |
| `src/presentation/TopologyNetworkVisualLayerParams.cc` | C++ | 321 |

## Overview

[[[PROSE overview unit=presentation/TopologyNetworkVisualLayerParams tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::TopologyNetworkVisualLayerParams`](#gplatespresentationtopologynetworkvisuallayerparams) | class | [`VisualLayerParams`](VisualLayerParams.md) | — | 0 | — |

## Members

### `GPlatesPresentation::TopologyNetworkVisualLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopologyNetworkVisualLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopologyNetworkVisualLayerParams>` | public | — |
| `TriangulationColourMode` | enum | `None` | public | — |
| `TriangulationDrawMode` | enum | `None` | public | — |
| `create( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | method | `non_null_ptr_type` | public | — |
| `get_triangulation_colour_mode()` | method | `TriangulationColourMode` | public | — |
| `set_triangulation_colour_mode( TriangulationColourMode triangulation_colour_mode)` | method | `void` | public | — |
| `get_triangulation_draw_mode()` | method | `TriangulationDrawMode` | public | — |
| `set_triangulation_draw_mode( TriangulationDrawMode triangulation_draw_mode)` | method | `void` | public | — |
| `set_min_abs_dilatation( const double &min_abs_dilatation)` | method | `void` | public | Set min/max absolute dilatation strain rate (for colour blending). |
| `set_max_abs_dilatation( const double &max_abs_dilatation)` | method | `void` | public | — |
| `get_dilatation_colour_palette()` | method | `boost::optional<GPlatesGui::ColourPalette<double>::non_null_ptr_type>` | public | Return the dilatation colour palette. |
| `set_dilatation_colour_palette( const QString &filename, const GPlatesGui::ColourPalette<double>::non_null_ptr_type &colour_palette)` | method | `void` | public | Set the dilatation palette. |
| `use_default_dilatation_colour_palette()` | method | `void` | public | Use the default dilatation colour palette. |
| `set_min_abs_second_invariant( const double &min_abs_second_invariant)` | method | `void` | public | Set min/max absolute second invariant strain rate (for colour blending). |
| `set_max_abs_second_invariant( const double &max_abs_second_invariant)` | method | `void` | public | — |
| `get_second_invariant_colour_palette()` | method | `boost::optional<GPlatesGui::ColourPalette<double>::non_null_ptr_type>` | public | Return the second invariant colour palette. |
| `set_second_invariant_colour_palette( const QString &filename, const GPlatesGui::ColourPalette<double>::non_null_ptr_type &colour_palette)` | method | `void` | public | Set the second invariant palette. |
| `use_default_second_invariant_colour_palette()` | method | `void` | public | Use the default second invariant colour palette. |
| `set_min_strain_rate_style( const double &min_strain_rate_style)` | method | `void` | public | Set min/max strain rate style (for colour blending). |
| `set_max_strain_rate_style( const double &max_strain_rate_style)` | method | `void` | public | — |
| `get_strain_rate_style_colour_palette()` | method | `boost::optional<GPlatesGui::ColourPalette<double>::non_null_ptr_type>` | public | Return the strain rate style colour palette. |
| `set_strain_rate_style_colour_palette( const QString &filename, const GPlatesGui::ColourPalette<double>::non_null_ptr_type &colour_palette)` | method | `void` | public | Set the strain rate style palette. |
| `use_default_strain_rate_style_colour_palette()` | method | `void` | public | Use the default strain rate style colour palette. |
| `show_segment_velocity()` | method | `bool` | public | — |
| `set_show_segment_velocity( bool b)` | method | `void` | public | — |
| `get_fill_triangulation()` | method | `bool` | public | — |
| `set_fill_triangulation( bool b)` | method | `void` | public | — |
| `get_fill_rigid_blocks()` | method | `bool` | public | — |
| `set_fill_rigid_blocks( bool b)` | method | `void` | public | — |
| `set_fill_opacity( const double &opacity)` | method | `void` | public | Sets the opacity of filled triangulation and rigid blocks. |
| `get_fill_opacity()` | method | `double` | public | Gets the opacity of filled triangulation and rigid blocks. |
| `set_fill_intensity( const double &intensity)` | method | `void` | public | Sets the intensity of filled triangulation and rigid blocks. |
| `get_fill_intensity()` | method | `double` | public | Gets the intensity of filled triangulation and rigid blocks. |
| `get_fill_modulate_colour()` | method | `GPlatesGui::Colour` | public | Returns the filled primitives modulate colour. |
| `handle_layer_modified( const GPlatesAppLogic::Layer &layer)` | method | `void` | public | Override of virtual method in VisualLayerParams base. |
| `accept_visitor( ConstVisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( VisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `TopologyNetworkVisualLayerParams( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | constructor | `None` | protected | — |
| `d_triangulation_colour_mode` | field | `TriangulationColourMode` | private | — |
| `d_triangulation_draw_mode` | field | `TriangulationDrawMode` | private | — |
| `d_min_abs_dilatation` | field | `double` | private | Dilatation strain rate parameters. |
| `d_max_abs_dilatation` | field | `double` | private | — |
| `d_dilatation_colour_palette_filename` | field | `QString` | private | The dilatation colour palette filename (or empty if using default palette). |
| `d_dilatation_colour_palette` | field | `boost::optional<GPlatesGui::ColourPalette<double>::non_null_ptr_type>` | private | The dilatation colour palette, whether set explicitly as loaded from a file, or auto-generated. |
| `d_min_abs_second_invariant` | field | `double` | private | Second invariant strain rate parameters. |
| `d_max_abs_second_invariant` | field | `double` | private | — |
| `d_second_invariant_colour_palette_filename` | field | `QString` | private | The second invariant colour palette filename (or empty if using default palette). |
| `d_second_invariant_colour_palette` | field | `boost::optional<GPlatesGui::ColourPalette<double>::non_null_ptr_type>` | private | The second invariant colour palette, whether set explicitly as loaded from a file, or auto-generated. |
| `d_min_strain_rate_style` | field | `double` | private | Strain rate style parameters. |
| `d_max_strain_rate_style` | field | `double` | private | — |
| `d_strain_rate_style_colour_palette_filename` | field | `QString` | private | The strain rate style colour palette filename (or empty if using default palette). |
| `d_strain_rate_style_colour_palette` | field | `boost::optional<GPlatesGui::ColourPalette<double>::non_null_ptr_type>` | private | The strain rate style colour palette, whether set explicitly as loaded from a file, or auto-generated. |
| `d_show_segment_velocity` | field | `bool` | private | The various options to show or hide. |
| `d_fill_rigid_blocks` | field | `bool` | private | — |
| `d_fill_opacity` | field | `double` | private | The opacity of the filled triangulation and rigid blocks in the range \[0,1\]. |
| `d_fill_intensity` | field | `double` | private | The intensity of the filled triangulation and rigid blocks in the range \[0,1\]. |
| `create_default_dilatation_colour_palette()` | method | `void` | private | — |
| `create_default_second_invariant_colour_palette()` | method | `void` | private | — |
| `create_default_strain_rate_style_colour_palette()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_TOPOLOGYNETWORKVISUALLAYERPARAMS_H` | macro | `None` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, TopologyNetworkVisualLayerParams::TriangulationColourMode &triangulation_colour_mode, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | Transcribe for sessions/projects. |
| `transcribe( GPlatesScribe::Scribe &scribe, TopologyNetworkVisualLayerParams::TriangulationDrawMode &triangulation_draw_mode, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | — |

## Notes

[[[PROSE notes unit=presentation/TopologyNetworkVisualLayerParams tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 111 |
| [presentation/ReconstructionGeometryRenderer](ReconstructionGeometryRenderer.md) | presentation | 66 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 48 |
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 2 |
| [presentation/VisualLayer](VisualLayer.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/TopologyNetworkVisualLayerParams.h
python scripts/gpq.py def GPlatesPresentation::TopologyNetworkVisualLayerParams --body
python scripts/gpq.py uses TopologyNetworkVisualLayerParams --kind class
python scripts/gpq.py hier TopologyNetworkVisualLayerParams
```
