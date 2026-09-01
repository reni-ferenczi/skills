# DependentTopologicalSectionLayers

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 480 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/DependentTopologicalSectionLayers.h` | C++ | 184 |
| `src/app-logic/DependentTopologicalSectionLayers.cc` | C++ | 272 |

## Overview

`DependentTopologicalSectionLayers` is a helper embedded in topology-resolving layer
proxies (`TopologyGeometryResolverLayerProxy`, `TopologyNetworkResolverLayerProxy`, and
others that consume resolved topologies such as `ScalarField3DLayerProxy`,
`VelocityFieldCalculatorLayerProxy`) to avoid recomputing resolved topologies whenever
an unrelated section layer changes. Topological features reference their sections
(reconstructed geometries via `ReconstructLayerProxy`, or resolved lines via
`TopologyGeometryResolverLayerProxy`) indirectly by feature ID, so a layer holding many
candidate section layers cannot tell which of them actually matter without scanning
feature references; this class does that scan once via
`set_topological_section_feature_ids()` and caches the resulting *dependency* subset
so that `update_topological_section_layer()` can cheaply answer "does this particular
section layer's update actually affect my resolved topologies" without a full rescan.

Both the reconstructed-geometry and resolved-line cases are handled by the same
private template methods (`set_dependency_topological_section_layers()`,
`update_topological_section_layer()`, `get_dependent_topological_section_layers()`),
parameterised on the layer proxy type, with the public overloads simply forwarding to
the corresponding `d_dependency_*_layers` set and `d_*_layers` full list.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::DependentTopologicalSectionLayers`](#gplatesapplogicdependenttopologicalsectionlayers) | class | — | — | 0 | Keeps track of which layers actually contribute topological sections to resolved topologies in a resolved topology layer. |

## Members

### `GPlatesAppLogic::DependentTopologicalSectionLayers`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~DependentTopologicalSectionLayers()` | destructor | `None` | public | — |
| `set_topological_section_feature_ids( const std::vector<GPlatesModel::FeatureHandle::weak_ref> &topological_features, boost::optional<TopologyGeometry::Type> topology_geometry_type = boost::none)` | method | `void` | public | Sets the topological section feature IDs referenced by the topological features for \*all\* times. |
| `set_topological_section_layers( const std::vector<ReconstructLayerProxy::non_null_ptr_type> &all_layers)` | method | `bool` | public | Set the \*reconstructed geometry\* topological section layers. |
| `set_topological_section_layers( const std::vector<GPlatesGlobal::PointerTraits<TopologyGeometryResolverLayerProxy>::non_null_ptr_type> &all_layers)` | method | `bool` | public | Set the \*resolved line\* topological section layers. |
| `update_topological_section_layer( const ReconstructLayerProxy::non_null_ptr_type &layer)` | method | `bool` | public | Call when the specified \*reconstructed geometry\* topological layer has changed (been updated). |
| `update_topological_section_layer( const GPlatesGlobal::PointerTraits<TopologyGeometryResolverLayerProxy>::non_null_ptr_type &layer)` | method | `bool` | public | Call when the specified \*resolved line\* topological layer has changed (been updated). |
| `get_dependent_topological_section_layers( std::vector<ReconstructLayerProxy::non_null_ptr_type> &dependent_layers)` | method | `void` | public | Get the \*reconstructed geometry\* topological layers that the topological features depend on. |
| `get_dependent_topological_section_layers( std::vector<GPlatesGlobal::PointerTraits<TopologyGeometryResolverLayerProxy>::non_null_ptr_type> &dependent_layers)` | method | `void` | public | Get the \*reconstructed geometry\* topological layers that the topological features depend on. |
| `d_reconstructed_geometry_layers` | field | `std::vector<ReconstructLayerProxy::non_null_ptr_type>` | private | All topological section layers (even ones that don't contribute to resolved topologies). |
| `d_resolved_line_layers` | field | `std::vector<GPlatesGlobal::PointerTraits<TopologyGeometryResolverLayerProxy>::non_null_ptr_type>` | private | — |
| `d_dependency_reconstructed_geometry_layers` | field | `std::set<ReconstructLayerProxy *>` | private | Unique list of dependency topological section layers that contribute to resolved topologies. |
| `d_dependency_resolved_line_layers` | field | `std::set<TopologyGeometryResolverLayerProxy *>` | private | — |
| `d_feature_ids` | field | `std::set<GPlatesModel::FeatureId>` | private | Unique list of topological section feature IDs that contribute to resolved topologies. |
| `set_dependency_topological_section_layers( const std::vector<typename LayerProxyType::non_null_ptr_type> &all_layers, std::set<LayerProxyType *> &layers)` | method | `bool` | private | — |
| `update_topological_section_layer( const typename LayerProxyType::non_null_ptr_type &layer, std::set<LayerProxyType *> &layers)` | method | `bool` | private | — |
| `get_dependent_topological_section_layers( std::vector<typename LayerProxyType::non_null_ptr_type> &dependent_layers, const std::set<LayerProxyType *> &layers)` | method | `void` | private | — |
| `topologies_depend_on_layer( const ReconstructLayerProxy::non_null_ptr_type &layer)` | method | `bool` | private | Checks if any topology depends on any of the specified topological section layer. |
| `topologies_depend_on_layer( const GPlatesGlobal::PointerTraits<TopologyGeometryResolverLayerProxy>::non_null_ptr_type &layer)` | method | `bool` | private | — |
| `topologies_depend_on_features( const std::vector<GPlatesModel::FeatureHandle::weak_ref> &features)` | method | `bool` | private | Checks if any topology depends on any of the specified topological section features. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_DEPENDENTTOPOLOGICALSECTIONLAYERS_H` | macro | `None` | — |

## Notes

`set_topological_section_feature_ids()` must be called (typically whenever the
topological features themselves change) before `update_topological_section_layer()`
results are meaningful, since the dependency sets are derived from the feature IDs
captured at that call — they are not automatically kept in sync with the topological
features afterward. The class holds raw, non-owning pointers in
`d_dependency_reconstructed_geometry_layers`/`d_dependency_resolved_line_layers`; the
owning references are the `non_null_ptr_type` vectors (`d_reconstructed_geometry_layers`,
`d_resolved_line_layers`), which must be kept up to date via `set_topological_section_layers()`
whenever the candidate layer set changes.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 22 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 21 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 20 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 15 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 10 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 9 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 8 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 6 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 6 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 4 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 3 |
| [app-logic/AssignPlateIds](AssignPlateIds.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/DependentTopologicalSectionLayers.h
python scripts/gpq.py def GPlatesAppLogic::DependentTopologicalSectionLayers --body
python scripts/gpq.py uses DependentTopologicalSectionLayers --kind class
python scripts/gpq.py hier DependentTopologicalSectionLayers
```
