# ResolvedRaster

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1249 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedRaster.h` | C++ | 192 |
| `src/app-logic/ResolvedRaster.cc` | C++ | 73 |

## Overview

[[[PROSE overview unit=app-logic/ResolvedRaster tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedRaster`](#gplatesapplogicresolvedraster) | class | [`ReconstructionGeometry`](ReconstructionGeometry.md)<br>[`GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>`](../model/WeakObserver.md) | — | 0 | A type of ReconstructionGeometry representing a raster. |

## Members

### `GPlatesAppLogic::ResolvedRaster`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedRaster>` | public | A convenience typedef for a shared pointer to a non-const ResolvedRaster. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedRaster>` | public | A convenience typedef for a shared pointer to a non-const ResolvedRaster. |
| `WeakObserverType` | typedef | `GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>` | public | A convenience typedef for the WeakObserver base class of this class. |
| `create( GPlatesModel::FeatureHandle &feature_handle, const double &reconstruction_time, const RasterLayerProxy::non_null_ptr_type &raster_layer_proxy, const std::vector<ReconstructLayerProxy::non_null_ptr_type> &reconstructed_polygons_layer_proxies, const boost::optional<RasterLayerProxy::non_null_ptr_type> &age_grid_r ...` | method | `non_null_ptr_type` | public | Create a ResolvedRaster. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `ResolvedRaster( GPlatesModel::FeatureHandle &feature_handle, const double &reconstruction_time, const RasterLayerProxy::non_null_ptr_type &raster_layer_proxy, const std::vector<ReconstructLayerProxy::non_null_ptr_type> &reconstructed_polygons_layer_proxies, const boost::optional<RasterLayerProxy::non_null_ptr_type> &ag ...` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_raster_layer_proxy` | field | `RasterLayerProxy::non_null_ptr_type` | private | The raster layer proxy. |
| `d_reconstructed_polygons_layer_proxies` | field | `std::vector<ReconstructLayerProxy::non_null_ptr_type>` | private | The optional reconstructed polygons layer proxies. |
| `d_age_grid_raster_layer_proxy` | field | `boost::optional<RasterLayerProxy::non_null_ptr_type>` | private | The optional age grid layer proxy. |
| `d_normal_map_raster_layer_proxy` | field | `boost::optional<RasterLayerProxy::non_null_ptr_type>` | private | The optional normal map layer proxy. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDRASTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ResolvedRaster tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 29 |
| [canvas-tools/AdjustFittedPoleEstimate](../canvas-tools/AdjustFittedPoleEstimate.md) | canvas-tools | 19 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 18 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 14 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 9 |
| [canvas-tools/CreateSmallCircle](../canvas-tools/CreateSmallCircle.md) | canvas-tools | 4 |
| [view-operations/DeleteVertexGeometryOperation](../view-operations/DeleteVertexGeometryOperation.md) | view-operations | 2 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 2 |
| [app-logic/RasterLayerProxy](RasterLayerProxy.md) | app-logic | 1 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 1 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 1 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 1 |
| [view-operations/AddPointGeometryOperation](../view-operations/AddPointGeometryOperation.md) | view-operations | 1 |
| [view-operations/RenderedResolvedRaster](../view-operations/RenderedResolvedRaster.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedRaster.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedRaster --body
python scripts/gpq.py uses ResolvedRaster --kind class
python scripts/gpq.py hier ResolvedRaster
```
