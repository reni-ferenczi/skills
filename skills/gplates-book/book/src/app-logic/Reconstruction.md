# Reconstruction

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 928 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/Reconstruction.h` | C++ | 274 |
| `src/app-logic/Reconstruction.cc` | C++ | 84 |

## Overview

`Reconstruction` is the accumulated output of the layer reconstruct graph at one reconstruction time and anchor plate ID: it just holds the `LayerProxy` output of every currently active layer, plus the `ReconstructionLayerProxy` used as a fallback for layers not explicitly wired to a reconstruction-tree input. Callers pull results back out by asking `get_active_layer_outputs<LayerProxyDerivedType>()` for the layer proxies of a particular derived type and then querying that type's own interface — `Reconstruction` itself has no knowledge of what any given layer's output means.

`get_all_resolved_topological_sections()` and `get_all_resolved_topological_shared_sub_segments()` walk every active layer's output to assemble a global view of resolved topological sections, which is why the class caches the result: the first call computes and stores it, and `add_active_layer_output()` and `set_default_reconstruction_layer_output()` both invalidate that cache since either can change which layers contribute to it.

The two `create()` overloads differ only in the fallback reconstruction layer proxy: the one-argument-fewer overload supplies a bare `ReconstructionLayerProxy::create()` that reconstructs with identity rotations, letting callers get a valid, blank `Reconstruction` before any real rotation layer exists.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::Reconstruction`](#gplatesapplogicreconstruction) | class | [`GPlatesUtils::ReferenceCount<Reconstruction>`](../utils/ReferenceCount.md) | — | 0 | This class represents a plate-tectonic reconstruction at a particular geological time-instant. |

## Members

### `GPlatesAppLogic::Reconstruction`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<Reconstruction>` | public | A convenience typedef for a shared pointer to non-const Reconstruction. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const Reconstruction>` | public | A convenience typedef for a shared pointer to const Reconstruction. |
| `layer_output_seq_type` | typedef | `std::vector<LayerProxy::non_null_ptr_type>` | public | Typedef for a sequence of \*active\* layer outputs (in the form of layer proxies). |
| `create( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id, const ReconstructionLayerProxy::non_null_ptr_type &default_reconstruction_layer_proxy)` | method | `non_null_ptr_type` | public | Create a new blank Reconstruction instance with the default reconstruction tree as default\_reconstruction\_tree. |
| `create( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | method | `non_null_ptr_type` | public | Create a new blank Reconstruction instance with the default reconstruction layer output being one that returns empty reconstruction trees (ie, returns identity rotations for all plates). |
| `add_active_layer_output( const LayerProxy::non_null_ptr_type &layer_proxy)` | method | `void` | public | Adds the output of an \*active\* layer to this reconstruction. |
| `get_active_layer_outputs( std::vector<typename LayerProxyDerivedType::non_null_ptr_type> &filtered_active_layer_outputs)` | method | `bool` | public | Returns the sequence of \*active\* layer outputs, for this reconstruction, that are of the specified type 'LayerProxyDerivedType'. |
| `get_anchor_plate_id()` | method | `GPlatesModel::integer_plate_id_type` | public | Returns the anchor plate id used for all reconstruction trees and all reconstructed geometries. |
| `get_default_reconstruction_layer_output()` | method | `ReconstructionLayerProxy::non_null_ptr_type` | public | Returns the reconstruction layer proxy used to reconstruct layers that are not explicitly connected to an input reconstruction layer. |
| `set_default_reconstruction_layer_output( const ReconstructionLayerProxy::non_null_ptr_type &reconstruction_layer_proxy)` | method | `void` | public | Sets the reconstruction layer proxy used to reconstruct layers that are not explicitly connected to an input reconstruction layer. |
| `get_all_resolved_topological_sections` | field | `std::vector<ResolvedTopologicalSection::non_null_ptr_type>` | public | Finds all resolved topological sections (sub-segments shared by resolved topology boundaries and network boundaries) from ALL layer outputs in this reconstruction. |
| `get_all_resolved_topological_shared_sub_segments` | field | `TopologyUtils::resolved_topological_boundaries_networks_to_shared_sub_segments_map_type` | public | A different representation of find\_resolved\_topological\_sections. |
| `d_reconstruction_time` | field | `GPlatesMaths::Real` | private | The reconstruction time at which all reconstructions are performed. |
| `d_anchor_plate_id` | field | `GPlatesModel::integer_plate_id_type` | private | The anchor plate id used for all reconstructions. |
| `d_default_reconstruction_layer_proxy` | field | `ReconstructionLayerProxy::non_null_ptr_type` | private | The reconstruction layer proxy used to reconstruct layers that are not explicitly connected to an input reconstruction layer. |
| `d_active_layer_outputs` | field | `layer_output_seq_type` | private | The sequence of active layer outputs. |
| `d_all_resolved_topological_sections` | field | `boost::optional<std::vector<ResolvedTopologicalSection::non_null_ptr_type>>` | private | Resolved topological sections from ALL layer outputs in this reconstruction (cached when calling get\_all\_resolved\_topological\_sections). |
| `d_all_resolved_topological_shared_sub_segments` | field | `boost::optional<TopologyUtils::resolved_topological_boundaries_networks_to_shared_sub_segments_map_type>` | private | Resolved topological shared sub-segments from ALL layer outputs in this reconstruction (cached when calling get\_all\_resolved\_topological\_shared\_sub\_segments). |
| `Reconstruction( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id, const ReconstructionLayerProxy::non_null_ptr_type &default_reconstruction_layer_proxy)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `Reconstruction( const double &reconstruction_time, GPlatesModel::integer_plate_id_type anchor_plate_id)` | constructor | `None` | private | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTION_H` | macro | `None` | — |

## Notes

The resolved-topological-sections cache is lazily populated and only invalidated by `add_active_layer_output` and `set_default_reconstruction_layer_output`; code that mutates `d_active_layer_outputs` through any other means would leave the cache stale.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 8 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 7 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 6 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 5 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 5 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 5 |
| [cli/CliReconstructCommand](../cli/CliReconstructCommand.md) | cli | 5 |
| [cli/CliAssignPlateIdsCommand](../cli/CliAssignPlateIdsCommand.md) | cli | 4 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 4 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 3 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 2 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 2 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 2 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 2 |
| [gui/ExportCoRegistrationAnimationStrategy](../gui/ExportCoRegistrationAnimationStrategy.md) | gui | 2 |
| [gui/ExportStageRotationAnimationStrategy](../gui/ExportStageRotationAnimationStrategy.md) | gui | 2 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 2 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 2 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 2 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 2 |

*... and 27 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/Reconstruction.h
python scripts/gpq.py def GPlatesAppLogic::Reconstruction --body
python scripts/gpq.py uses Reconstruction --kind class
python scripts/gpq.py hier Reconstruction
```
