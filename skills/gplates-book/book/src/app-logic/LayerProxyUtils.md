# LayerProxyUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 840 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/LayerProxyUtils.h` | C++ | 800 |
| `src/app-logic/LayerProxyUtils.cc` | C++ | 320 |

## Overview

[[[PROSE overview unit=app-logic/LayerProxyUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::LayerProxyUtils::InputLayerProxy`](#gplatesapplogiclayerproxyutilsinputlayerproxy) | class | — | `<class LayerProxyType>` | 0 | A useful class for derived LayerProxy classes (or the base LayerProxy class) to use to keep track of changes to their input layer proxies. |
| [`GPlatesAppLogic::LayerProxyUtils::OptionalInputLayerProxy`](#gplatesapplogiclayerproxyutilsoptionalinputlayerproxy) | class | [`GPlatesUtils::SafeBool<OptionalInputLayerProxy<LayerProxyType> >`](../utils/SafeBool.md) | `<class LayerProxyType>` | 0 | A wrapper around InputLayerProxy to make it optional. |
| [`GPlatesAppLogic::LayerProxyUtils::InputLayerProxySequence`](#gplatesapplogiclayerproxyutilsinputlayerproxysequence) | class | — | `<class LayerProxyType>` | 0 | A convenience class that wraps a std::vector of InputLayerProxy and adds/removes input layer proxies. |
| [`GPlatesAppLogic::LayerProxyUtils::LayerProxyDerivedTypeFinder`](#gplatesapplogiclayerproxyutilslayerproxyderivedtypefinder) | class | [`LayerProxyVisitorBase< typename GPlatesUtils::CopyConst< LayerProxyDerivedType, LayerProxy>::type >`](LayerProxyVisitor.md) | `<class LayerProxyDerivedType>` | 0 | Template visitor class to find instances of a class derived from LayerProxy. |

## Members

### `GPlatesAppLogic::LayerProxyUtils::InputLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `layer_proxy_non_null_ptr_type` | typedef | `typename GPlatesGlobal::PointerTraits<LayerProxyType>::non_null_ptr_type` | public | Typedef for layer proxy non-null intrusive pointer. |
| `InputLayerProxy( const layer_proxy_non_null_ptr_type &input_layer_proxy, const subject_token_method_type &subject_token_method = &LayerProxyType::get_subject_token)` | constructor | `None` | public | — |
| `set_input_layer_proxy( const layer_proxy_non_null_ptr_type &input_layer_proxy)` | method | `void` | public | Sets a new input layer proxy wrapped by this object. |
| `is_up_to_date()` | method | `bool` | public | Returns true if the caller is up-to-date with respect to this input layer proxy. |
| `set_up_to_date()` | method | `void` | public | Makes the caller up-to-date with respect to this input layer proxy. |
| `d_input_layer_proxy` | field | `layer_proxy_non_null_ptr_type` | private | — |
| `d_subject_token_method` | field | `subject_token_method_type` | private | — |
| `d_input_layer_proxy_observer_token` | field | `GPlatesUtils::ObserverToken` | private | — |

### `GPlatesAppLogic::LayerProxyUtils::OptionalInputLayerProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `layer_proxy_non_null_ptr_type` | typedef | `typename GPlatesGlobal::PointerTraits<LayerProxyType>::non_null_ptr_type` | public | Typedef for layer proxy non-null intrusive pointer. |
| `OptionalInputLayerProxy()` | constructor | `None` | public | Default constructor stores no input layer proxy. |
| `OptionalInputLayerProxy( const layer_proxy_non_null_ptr_type &input_layer_proxy)` | constructor | `None` | public | Constructor to store an input layer proxy. |
| `boolean_test()` | method | `bool` | public | Use 'if (proxy)' to test if the wrapped input layer proxy is set (not boost::none). |
| `get_optional_input_layer_proxy()` | method | `boost::optional<layer_proxy_non_null_ptr_type>` | public | Returns the input layer proxy wrapped by this object as a boost::optional. |
| `set_input_layer_proxy( const boost::optional<layer_proxy_non_null_ptr_type> &optional_input_layer_proxy = boost::none)` | method | `void` | public | Sets a new input layer proxy wrapped by this object. |
| `is_up_to_date()` | method | `bool` | public | Returns true if the caller is up-to-date with respect to this input layer proxy. |
| `set_up_to_date()` | method | `void` | public | Makes the caller up-to-date with respect to this input layer proxy. |
| `d_optional_input_layer_proxy` | field | `boost::optional< InputLayerProxy<LayerProxyType> >` | private | — |
| `d_is_none_and_up_to_date` | field | `bool` | private | This flag is only used if d\_optional\_input\_layer\_proxy is boost::none in which case if it's false it means the input layer proxy has recently been set to none and is out-of-date because the client has not yet called set\_up\_to\_date. |

### `GPlatesAppLogic::LayerProxyUtils::InputLayerProxySequence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `layer_proxy_non_null_ptr_type` | typedef | `typename GPlatesGlobal::PointerTraits<LayerProxyType>::non_null_ptr_type` | public | Typedef for a non-null layer proxy pointer. |
| `layer_proxies_map_type` | typedef | `std::map< layer_proxy_non_null_ptr_type, InputLayerProxy<LayerProxyType> >` | public | Typedef for a mapping of layer proxies to their container InputLayerProxy objects. |
| `const_iterator` | typedef | `boost::transform_iterator< const InputLayerProxy<LayerProxyType> & (*)(const typename layer_proxies_map_type::value_type &), typename layer_proxies_map_type::const_iterator>` | public | Typedef for 'const' iterator over 'InputLayerProxy' input layer proxies. |
| `iterator` | typedef | `boost::transform_iterator< InputLayerProxy<LayerProxyType> & (*)(typename layer_proxies_map_type::value_type &), typename layer_proxies_map_type::iterator>` | public | Typedef for 'non-const' iterator over 'InputLayerProxy' input layer proxies. |
| `empty()` | method | `bool` | public | Return true if contains no input layer proxies. |
| `size()` | method | `unsigned int` | public | Return number of input layer proxies. |
| `begin()` | method | `const_iterator` | public | Get the begin 'const' iterator over the 'InputLayerProxy' input layer proxies. |
| `end()` | method | `const_iterator` | public | Get the end 'const' iterator over the 'InputLayerProxy' input layer proxies. |
| `set_input_layer_proxies( const std::vector<layer_proxy_non_null_ptr_type> &src_input_layer_proxies, const subject_token_method_type &subject_token_method = &LayerProxyType::get_subject_token)` | method | `bool` | public | Sets the input layer proxies. |
| `add_input_layer_proxy( const layer_proxy_non_null_ptr_type &input_layer_proxy, const subject_token_method_type &subject_token_method = &LayerProxyType::get_subject_token)` | method | `void` | public | Adds the specified input layer proxy to the sequence. |
| `remove_input_layer_proxy( const layer_proxy_non_null_ptr_type &input_layer_proxy)` | method | `void` | public | Removes the specified input layer proxy from the sequence. |
| `d_layer_proxies` | field | `layer_proxies_map_type` | private | — |

### `GPlatesAppLogic::LayerProxyUtils::LayerProxyDerivedTypeFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_class_type` | typedef | `LayerProxyVisitorBase< typename GPlatesUtils::CopyConst< LayerProxyDerivedType, LayerProxy>::type >` | public | Typedef for base class type. |
| `layer_proxy_derived_type` | typedef | `LayerProxyDerivedType` | public | Convenience typedef for the template parameter which is a type derived from LayerProxy. |
| `container_type` | typedef | `std::vector<layer_proxy_derived_type *>` | public | Convenience typedef for sequence of pointers to layer proxy derived type. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<layer_proxy_derived_type> &layer_proxy)` | method | `void` | public | — |
| `d_found_layer_proxies` | field | `container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_LAYERPROXYUTILS_H` | macro | `None` | — |
| `get_reconstructed_feature_geometries( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, std::vector<ReconstructHandle::type> &reconstruct_handles, const Reconstruction &reconstruction, bool include_topology_reconstructed_feature_geometries = true)` | function | `void` | Returns the reconstructed feature geometries from all active reconstruct layers in the specified reconstruction. |
| `get_resolved_topological_lines( std::vector<ResolvedTopologicalLine::non_null_ptr_type> &resolved_topological_lines, std::vector<ReconstructHandle::type> &reconstruct_handles, const Reconstruction &reconstruction)` | function | `void` | Returns the resolved topological lines from all active topological geometry layers in the specified reconstruction. |
| `find_dependent_topological_sections( std::set<GPlatesModel::FeatureId> &dependent_topological_sections, const Reconstruction &reconstruction)` | function | `void` | Returns the feature IDs of topological sections referenced for \*all\* times by all active topological layers (topological geometry and network) in the specified reconstruction. |
| `find_resolved_topological_sections( std::vector<ResolvedTopologicalSection::non_null_ptr_type> &resolved_topological_sections, const Reconstruction &reconstruction)` | function | `void` | Finds all sub-segments shared by \*all\* resolved topology boundaries and network boundaries in the specified reconstruction. |
| `find_reconstruct_layer_outputs_of_feature_collection( std::vector<GPlatesGlobal::PointerTraits<ReconstructLayerProxy>::non_null_ptr_type> &reconstruct_layer_outputs, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, const ReconstructGraph &reconstruct_graph)` | function | `void` | Returns the reconstruct layer outputs that reconstruct specified feature collection, and limited to active reconstruct layers in reconstruction. |
| `find_reconstruct_layer_outputs_of_feature( std::vector<GPlatesGlobal::PointerTraits<ReconstructLayerProxy>::non_null_ptr_type> &reconstruct_layer_outputs, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Reconstruction &reconstruction)` | function | `void` | Returns the reconstruct layer outputs that reconstructed the feature feature\_ref, and limited to active reconstruct layers in reconstruction. |
| `find_reconstructed_feature_geometries_of_feature( std::vector<ReconstructedFeatureGeometry::non_null_ptr_type> &reconstructed_feature_geometries, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const Reconstruction &reconstruction)` | function | `void` | Returns the reconstructed feature geometries, referencing the feature feature\_ref, and limited to those generated from all active reconstruct layers in reconstruction. |
| `get_layer_proxy_derived_type( LayerProxyPointer layer_proxy_ptr)` | function | `boost::optional<LayerProxyDerivedType *>` | — |
| `get_layer_proxy_derived_type_sequence( LayerProxyForwardIter layer_proxies_begin, LayerProxyForwardIter layer_proxies_end, ContainerOfLayerProxyDerivedType &layer_proxy_derived_type_seq)` | function | `bool` | — |

## Notes

[[[PROSE notes unit=app-logic/LayerProxyUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 181 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 95 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 91 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 89 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 86 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 85 |
| [app-logic/ScalarField3DLayerProxy](ScalarField3DLayerProxy.md) | app-logic | 79 |
| [app-logic/VelocityFieldCalculatorLayerProxy](VelocityFieldCalculatorLayerProxy.md) | app-logic | 78 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 78 |
| [app-logic/CoRegistrationLayerProxy](CoRegistrationLayerProxy.md) | app-logic | 54 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 52 |
| [app-logic/ReconstructGraph](ReconstructGraph.md) | app-logic | 49 |
| [app-logic/ScalarField3DLayerTask](ScalarField3DLayerTask.md) | app-logic | 46 |
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 43 |
| [app-logic/RasterLayerProxy](RasterLayerProxy.md) | app-logic | 40 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 40 |
| [presentation/VisualLayers](../presentation/VisualLayers.md) | presentation | 39 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 38 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 37 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 36 |

*... and 128 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/LayerProxyUtils.h
python scripts/gpq.py def GPlatesAppLogic::LayerProxyUtils::InputLayerProxySequence --body
python scripts/gpq.py uses InputLayerProxySequence --kind class
python scripts/gpq.py hier InputLayerProxySequence
```
