# MultiPointVectorField

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 540 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/MultiPointVectorField.h` | C++ | 465 |
| `src/app-logic/MultiPointVectorField.cc` | C++ | 64 |

## Overview

[[[PROSE overview unit=app-logic/MultiPointVectorField tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::MultiPointVectorField`](#gplatesapplogicmultipointvectorfield) | class | [`ReconstructionGeometry`](ReconstructionGeometry.md)<br>[`GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>`](../model/WeakObserver.md) | — | 0 | This class represents a 3-D vector field over a multi-point domain. |

## Members

### `GPlatesAppLogic::MultiPointVectorField`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<MultiPointVectorField>` | public | A convenience typedef for a non-null shared pointer to a non-const MultiPointVectorField. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const MultiPointVectorField>` | public | A convenience typedef for a non-null shared pointer to a const MultiPointVectorField. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<MultiPointVectorField>` | public | A convenience typedef for boost::intrusive\_ptr\<MultiPointVectorField\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const MultiPointVectorField>` | public | A convenience typedef for boost::intrusive\_ptr\<const MultiPointVectorField\>. |
| `WeakObserverType` | typedef | `GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>` | public | A convenience typedef for the WeakObserver base class of this class. |
| `multi_point_ptr_type` | typedef | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | public | A convenience typedef for a non-null shared pointer to a non-const MultiPointOnSphere. |
| `CodomainElement` | struct | `None` | public | This class represents an element of the codomain -- primarily a 3-D vector, plus some other information. |
| `codomain_type` | typedef | `std::vector< boost::optional<CodomainElement> >` | public | A convenience typedef for the codomain type. |
| `create_empty( const double &reconstruction_time_, const multi_point_ptr_type &multi_point_ptr, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator_, boost::optional<ReconstructHandle::type> reconstruct_handle_ = boost::none)` | method | `non_null_ptr_type` | public | Create a MultiPointVectorField instance which is sampled over the supplied multi-point domain. |
| `~MultiPointVectorField()` | destructor | `None` | public | — |
| `get_non_null_pointer_to_const()` | method | `non_null_ptr_to_const_type` | public | Get a non-null pointer to a const MultiPointVectorField which points to this instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_type` | public | Get a non-null pointer to a MultiPointVectorField which points to this instance. |
| `references( const GPlatesModel::FeatureHandle &that_feature_handle)` | method | `bool` | public | Return whether this RFG references that\_feature\_handle. |
| `feature_handle_ptr()` | method | `GPlatesModel::FeatureHandle` | public | Return the pointer to the FeatureHandle. |
| `is_valid()` | method | `bool` | public | Return whether this pointer is valid to be dereferenced (to obtain a FeatureHandle). |
| `get_feature_ref()` | method | `GPlatesModel::FeatureHandle::weak_ref` | public | Return a weak-ref to the \*domain\* feature used for the domain of the vector field. |
| `property()` | method | `GPlatesModel::FeatureHandle::iterator` | public | Access the feature property which contained the reconstructed geometry. |
| `multi_point()` | method | `multi_point_ptr_type` | public | Access the MultiPointOnSphere which is the domain of the 3-D vector field. |
| `domain_size()` | method | `codomain_type::size_type` | public | Return the number of points in the domain. |
| `begin()` | method | `codomain_type::const_iterator` | public | Return a "begin" const-iterator for the elements in the range. |
| `end()` | method | `codomain_type::const_iterator` | public | Return an "end" const-iterator for the elements in the range. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `MultiPointVectorField( const double &reconstruction_time_, const multi_point_ptr_type &multi_point_ptr, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator_, boost::optional<ReconstructHandle::type> reconstruct_handle_)` | constructor | `None` | protected | Instantiate a MultiPointVectorField which is sampled over the supplied multi-point domain. |
| `d_multi_point_ptr` | field | `multi_point_ptr_type` | private | The multi-point domain over which the 3-D vector field is sampled. |
| `d_property_iterator` | field | `GPlatesModel::FeatureHandle::iterator` | private | This is an iterator to the (multi-point-valued) property from which this MPVF was derived. |
| `d_range` | field | `codomain_type` | private | The range (a set of codomain elements) of the multi-point domain. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_MULTIPOINTVECTORFIELD_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/MultiPointVectorField tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 112 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 106 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 98 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 45 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 42 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 40 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 38 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 37 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 33 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 31 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 26 |
| [file-io/GMTFormatMultiPointVectorFieldExport](../file-io/GMTFormatMultiPointVectorFieldExport.md) | file-io | 26 |
| [file-io/CitcomsFormatVelocityVectorFieldExport](../file-io/CitcomsFormatVelocityVectorFieldExport.md) | file-io | 24 |
| [file-io/TerraFormatVelocityVectorFieldExport](../file-io/TerraFormatVelocityVectorFieldExport.md) | file-io | 24 |
| [file-io/MultiPointVectorFieldExport](../file-io/MultiPointVectorFieldExport.md) | file-io | 23 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 21 |
| [app-logic/ResolvedVertexSourceInfo](ResolvedVertexSourceInfo.md) | app-logic | 18 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 17 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 16 |
| [app-logic/ReconstructMethodRegistry](ReconstructMethodRegistry.md) | app-logic | 15 |

*... and 29 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/MultiPointVectorField.h
python scripts/gpq.py def GPlatesAppLogic::MultiPointVectorField --body
python scripts/gpq.py uses MultiPointVectorField --kind class
python scripts/gpq.py hier MultiPointVectorField
```
