# TopologyGeometryVisualLayerParams

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 1047 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/TopologyGeometryVisualLayerParams.h` | C++ | 157 |

## Overview

`GPlatesPresentation::TopologyGeometryVisualLayerParams` is the `VisualLayerParams` for a resolved-topological-geometry layer (topological lines and polygons, as opposed to the topological-network layer covered by `TopologyNetworkVisualLayerParams`). It holds the small set of display options specific to that layer type — whether resolved polygons are filled, and the opacity/intensity/modulate colour of that fill — leaving everything else (colouring by feature, symbolisation, etc.) to the shared machinery in the `VisualLayerParams` base.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::TopologyGeometryVisualLayerParams`](#gplatespresentationtopologygeometryvisuallayerparams) | class | [`VisualLayerParams`](VisualLayerParams.md) | — | 0 | — |

## Members

### `GPlatesPresentation::TopologyGeometryVisualLayerParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopologyGeometryVisualLayerParams>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopologyGeometryVisualLayerParams>` | public | — |
| `create( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | method | `non_null_ptr_type` | public | — |
| `set_fill_polygons( bool fill)` | method | `void` | public | — |
| `get_fill_polygons()` | method | `bool` | public | — |
| `set_fill_opacity( const double &opacity)` | method | `void` | public | Sets the opacity of filled primitives. |
| `get_fill_opacity()` | method | `double` | public | Gets the opacity of filled primitives. |
| `set_fill_intensity( const double &intensity)` | method | `void` | public | Sets the intensity of filled primitives. |
| `get_fill_intensity()` | method | `double` | public | Gets the intensity of filled primitives. |
| `get_fill_modulate_colour()` | method | `GPlatesGui::Colour` | public | Returns the filled primitives modulate colour. |
| `accept_visitor( ConstVisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( VisualLayerParamsVisitor &visitor)` | method | `void` | public | — |
| `TopologyGeometryVisualLayerParams( GPlatesAppLogic::LayerParams::non_null_ptr_type layer_params)` | constructor | `None` | protected | — |
| `d_fill_polygons` | field | `bool` | private | — |
| `d_fill_opacity` | field | `double` | private | The opacity of filled primitives in the range \[0,1\]. |
| `d_fill_intensity` | field | `double` | private | The intensity of filled primitives in the range \[0,1\]. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_TOPOLOGYGEOMETRYVISUALLAYERPARAMS_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](../qt-widgets/TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 15 |
| [presentation/ReconstructionGeometryRenderer](ReconstructionGeometryRenderer.md) | presentation | 2 |
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 2 |
| [presentation/TranscribeSession](TranscribeSession.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/TopologyGeometryVisualLayerParams.h
python scripts/gpq.py def GPlatesPresentation::TopologyGeometryVisualLayerParams --body
python scripts/gpq.py uses TopologyGeometryVisualLayerParams --kind class
python scripts/gpq.py hier TopologyGeometryVisualLayerParams
```
