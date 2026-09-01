# RenderedGeometryUtils

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 167 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/RenderedGeometryUtils.h` | C++ | 330 |
| `src/view-operations/RenderedGeometryUtils.cc` | C++ | 502 |

## Overview

[[[PROSE overview unit=view-operations/RenderedGeometryUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::RenderedGeometryUtils::(anonymous)::CountNonEmptyRenderedGeometries`](#gplatesviewoperationsrenderedgeometryutilsanonymouscountnonemptyrenderedgeometries) | class | — | — | 0 | Increments count for every non-empty RenderedGeometryLayer. |
| [`GPlatesViewOperations::RenderedGeometryUtils::(anonymous)::CollectReconstructionGeometries`](#gplatesviewoperationsrenderedgeometryutilsanonymouscollectreconstructiongeometries) | class | [`ConstRenderedGeometryVisitor`](RenderedGeometryVisitor.md) | — | 0 | Retrieves any ReconstructionGeometry objects from RenderedGeometryLayer. |
| [`GPlatesViewOperations::RenderedGeometryUtils::reconstruction_geom_seq_type`](#gplatesviewoperationsrenderedgeometryutilsreconstruction_geom_seq_type) | typedef | — | — | 0 | Typedef for sequence of ReconstructionGeometry objects. |
| [`GPlatesViewOperations::RenderedGeometryUtils::VisitFunctionOnRenderedGeometryLayers`](#gplatesviewoperationsrenderedgeometryutilsvisitfunctiononrenderedgeometrylayers) | class | [`RenderedGeometryCollectionVisitor<>`](RenderedGeometryCollectionVisitor.md) | — | 0 | Visits a RenderedGeometryCollection and calls a user-specified function, class method or functor on each RenderedGeometryLayer object contained within. |
| [`GPlatesViewOperations::RenderedGeometryUtils::ConstVisitFunctionOnRenderedGeometryLayers`](#gplatesviewoperationsrenderedgeometryutilsconstvisitfunctiononrenderedgeometrylayers) | class | [`ConstRenderedGeometryCollectionVisitor<>`](RenderedGeometryCollectionVisitor.md) | — | 0 | Visits a RenderedGeometryCollection and calls a user-specified function, class method or functor on each RenderedGeometryLayer object contained within. |

## Members

### `GPlatesViewOperations::RenderedGeometryUtils::(anonymous)::CountNonEmptyRenderedGeometries`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CountNonEmptyRenderedGeometries()` | constructor | `None` | public | — |
| `operator()( const RenderedGeometryLayer &rendered_geom_layer)` | operator | `void` | public | — |
| `get_count()` | method | `unsigned int` | public | — |
| `d_count` | field | `unsigned int` | private | — |

### `GPlatesViewOperations::RenderedGeometryUtils::(anonymous)::CollectReconstructionGeometries`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CollectReconstructionGeometries( reconstruction_geom_seq_type &reconstruction_geom_seq)` | constructor | `None` | public | — |
| `operator()( const RenderedGeometryLayer &rendered_geom_layer)` | operator | `void` | public | — |
| `visit_rendered_reconstruction_geometry( const RenderedReconstructionGeometry &rendered_recon_geom)` | method | `void` | public | — |
| `visit_rendered_multi_reconstruction_geometry( const RenderedMultiReconstructionGeometry &rendered_multi_recon_geom)` | method | `void` | public | — |
| `d_reconstruction_geom_seq` | field | `reconstruction_geom_seq_type` | private | — |

### `GPlatesViewOperations::RenderedGeometryUtils::reconstruction_geom_seq_type`

*None.*

### `GPlatesViewOperations::RenderedGeometryUtils::VisitFunctionOnRenderedGeometryLayers`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `rendered_geometry_layer_function_type` | typedef | `boost::function<void (RenderedGeometryLayer &)>` | public | A function to call when visiting each RenderedGeometryLayer. |
| `VisitFunctionOnRenderedGeometryLayers( rendered_geometry_layer_function_type rendered_geom_layer_function, RenderedGeometryCollection::main_layers_update_type main_layers = RenderedGeometryCollection::ALL_MAIN_LAYERS, bool only_if_main_layer_active = true)` | constructor | `None` | public | Specify the main layers in which rendered\_geom\_layer\_function will be called on the RenderedGeometryLayer objects in the collection. each RenderedGeometryLayer. |
| `call_function( RenderedGeometryCollection &rendered_geom_collection)` | method | `void` | public | — |
| `visit_main_rendered_layer( RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_layer_type)` | method | `bool` | private | — |
| `visit_rendered_geometry_layer( RenderedGeometryLayer &rendered_geometry_layer)` | method | `bool` | private | — |
| `d_rendered_geom_layer_function` | field | `rendered_geometry_layer_function_type` | private | — |
| `d_main_layers` | field | `RenderedGeometryCollection::main_layers_update_type` | private | — |
| `d_only_if_main_layer_active` | field | `bool` | private | — |

### `GPlatesViewOperations::RenderedGeometryUtils::ConstVisitFunctionOnRenderedGeometryLayers`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `rendered_geometry_layer_function_type` | typedef | `boost::function<void (const RenderedGeometryLayer &)>` | public | A function to call when visiting each RenderedGeometryLayer. |
| `ConstVisitFunctionOnRenderedGeometryLayers( rendered_geometry_layer_function_type rendered_geom_layer_function, RenderedGeometryCollection::main_layers_update_type main_layers = RenderedGeometryCollection::ALL_MAIN_LAYERS, bool only_if_main_layer_active = true)` | constructor | `None` | public | Specify the main layers in which rendered\_geom\_layer\_function will be called on the RenderedGeometryLayer objects in the collection. each RenderedGeometryLayer. |
| `call_function( const RenderedGeometryCollection &rendered_geom_collection)` | method | `void` | public | — |
| `visit_main_rendered_layer( const RenderedGeometryCollection &rendered_geometry_collection, RenderedGeometryCollection::MainLayerType main_layer_type)` | method | `bool` | private | — |
| `visit_rendered_geometry_layer( const RenderedGeometryLayer &rendered_geometry_layer)` | method | `bool` | private | — |
| `d_rendered_geom_layer_function` | field | `rendered_geometry_layer_function_type` | private | — |
| `d_main_layers` | field | `RenderedGeometryCollection::main_layers_update_type` | private | — |
| `d_only_if_main_layer_active` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `remove_duplicates( reconstruction_geom_seq_type &reconstruction_geom_seq)` | function | `void` | Removes duplicate ReconstructionGeometry objects from an unsorted sequence. |
| `GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYCOLLECTIONUTILS_H` | macro | `None` | — |
| `get_num_active_non_empty_layers( const RenderedGeometryCollection &rendered_geom_collection, RenderedGeometryCollection::MainLayerType main_layer_type, bool only_if_main_layer_active = true)` | function | `unsigned int` | Returns number of RenderedGeometryLayer objects that are not empty. |
| `get_num_active_non_empty_layers( const RenderedGeometryCollection &rendered_geom_collection, RenderedGeometryCollection::main_layers_update_type main_layers = RenderedGeometryCollection::ALL_MAIN_LAYERS, bool only_if_main_layer_active = true)` | function | `unsigned int` | Returns number of RenderedGeometryLayer objects that are not empty. |
| `activate_rendered_geometry_layers( RenderedGeometryCollection &rendered_geom_collection, RenderedGeometryCollection::MainLayerType main_layer_type, bool only_if_main_layer_active = true)` | function | `void` | Activate all RenderedGeometryLayer objects in the specified main layer. |
| `activate_rendered_geometry_layers( RenderedGeometryCollection &rendered_geom_collection, RenderedGeometryCollection::main_layers_update_type main_layers = RenderedGeometryCollection::ALL_MAIN_LAYERS, bool only_if_main_layer_active = true)` | function | `void` | Activate all RenderedGeometryLayer objects in the specified main layers. |
| `deactivate_rendered_geometry_layers( RenderedGeometryCollection &rendered_geom_collection, RenderedGeometryCollection::MainLayerType main_layer_type, bool only_if_main_layer_active = true)` | function | `void` | Deactivate all RenderedGeometryLayer objects in the specified main layer. |
| `deactivate_rendered_geometry_layers( RenderedGeometryCollection &rendered_geom_collection, RenderedGeometryCollection::main_layers_update_type main_layers = RenderedGeometryCollection::ALL_MAIN_LAYERS, bool only_if_main_layer_active = true)` | function | `void` | Deactivate all RenderedGeometryLayer objects in the specified main layers. |
| `get_unique_reconstruction_geometries( reconstruction_geom_seq_type &reconstruction_geom_seq, const RenderedGeometryCollection &rendered_geom_collection, RenderedGeometryCollection::MainLayerType main_layer_type, bool only_if_main_layer_active = true)` | function | `bool` | Collects any ReconstructionGeometry objects contained in RenderedReconstructionGeometry and RenderedMultiReconstructionGeometry objects in the specified main layer. |
| `get_unique_reconstruction_geometries( reconstruction_geom_seq_type &reconstruction_geom_seq, const RenderedGeometryCollection &rendered_geom_collection, RenderedGeometryCollection::main_layers_update_type main_layers = RenderedGeometryCollection::ALL_MAIN_LAYERS, bool only_if_main_layer_active = true)` | function | `bool` | Collects any ReconstructionGeometry objects contained in RenderedReconstructionGeometry and RenderedMultiReconstructionGeometry objects in the specified main layers. |
| `get_unique_reconstruction_geometries( reconstruction_geom_seq_type &reconstruction_geom_seq, const GPlatesViewOperations::sorted_rendered_geometry_proximity_hits_type & sorted_rendered_geometry_hits)` | function | `bool` | Collects any ReconstructionGeometry objects contained in the results of a proximity test. |
| `get_unique_reconstruction_geometries_observing_feature( reconstruction_geom_seq_type &reconstruction_geometries_observing_feature, const RenderedGeometryCollection &rendered_geom_collection, const GPlatesAppLogic::ReconstructionGeometry &reconstruction_geometry, boost::optional<const std::vector<GPlatesAppLogic::Recons ...` | function | `bool` | Finds the ReconstructionGeometry objects that were generated from the same geometry property as reconstruction\_geometry and that were optionally reconstructed using reconstruct\_handles and that are from the reconstruction layer in ... |
| `get_unique_reconstruction_geometries_observing_feature( reconstruction_geom_seq_type &reconstruction_geometries_observing_feature, const RenderedGeometryCollection &rendered_geom_collection, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, boost::optional<const std::vector<GPlatesAppLogic::ReconstructHandle::t ...` | function | `bool` | Finds the ReconstructionGeometry objects from feature feature\_ref and that were optionally reconstructed using reconstruct\_handles and that are from the reconstruction layer in rendered\_geom\_collection. |
| `get_unique_reconstruction_geometries_observing_feature( reconstruction_geom_seq_type &reconstruction_geometries_observing_feature, const RenderedGeometryCollection &rendered_geom_collection, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureHandle::iterator &geometry_property_iterator ...` | function | `bool` | Finds the ReconstructionGeometry objects that were generated from the geometry property geometry\_property\_iterator in feature feature\_ref and that were optionally reconstructed using reconstruct\_handles and that are from the reconstruction ... |

## Notes

[[[PROSE notes unit=view-operations/RenderedGeometryUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/VisibleReconstructionGeometryExport](VisibleReconstructionGeometryExport.md) | view-operations | 13 |
| [gui/AddClickedGeometriesToFeatureTable](../gui/AddClickedGeometriesToFeatureTable.md) | gui | 7 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 7 |
| [view-operations/RenderedGeometryProximity](RenderedGeometryProximity.md) | view-operations | 7 |
| [gui/GeometryFocusHighlight](../gui/GeometryFocusHighlight.md) | gui | 5 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](../gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 4 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 4 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 4 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 4 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 1 |
| [canvas-tools/ClickGeometry](../canvas-tools/ClickGeometry.md) | canvas-tools | 1 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 1 |
| [gui/GlobeRenderedGeometryCollectionPainter](../gui/GlobeRenderedGeometryCollectionPainter.md) | gui | 1 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryCollectionPainter](../gui/MapRenderedGeometryCollectionPainter.md) | gui | 1 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 1 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 1 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/RenderedGeometryUtils.h
python scripts/gpq.py def GPlatesViewOperations::RenderedGeometryUtils::(anonymous)::CollectReconstructionGeometries --body
python scripts/gpq.py uses CollectReconstructionGeometries --kind class
python scripts/gpq.py hier CollectReconstructionGeometries
```
