# MultiPointVectorField

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 540 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/MultiPointVectorField.h` | C++ | 465 |
| `src/app-logic/MultiPointVectorField.cc` | C++ | 64 |

## Overview

The `ReconstructionGeometry` that carries velocities. Where a
`ReconstructedFeatureGeometry` is one reconstructed geometry, a
`MultiPointVectorField` is a *sampled function*: a `MultiPointOnSphere` domain
paired with a parallel range of `CodomainElement`s, one per domain point, each
holding a `GPlatesMaths::Vector3D`, a `Reason` tag, an optional plate ID and a
maybe-null back-pointer to the `ReconstructionGeometry` that supplied the motion.
It is produced by `PlateVelocityUtils::solve_velocities_on_surfaces` (one field
per input velocity-domain geometry) and by the deformation path in
`TopologyReconstruct`, held by `VelocityFieldCalculatorLayerProxy`, drawn by
`ReconstructionGeometryRenderer`, and written out by the
`MultiPointVectorFieldExport` family in `file-io`.

The `Reason` enum is the part worth understanding. A single field may span several
independently-moving plates, so the velocity at each point is attributed
individually: the point may have been found in a reconstructed static polygon
(`InStaticPolygon`), in a resolved topological boundary (`InPlateBoundary`), in a
deforming region or a rigid block of a resolved topological network
(`InNetworkDeformingRegion`, `InNetworkRigidBlock`), in nothing at all
(`NotInAnyBoundaryOrNetwork`, which stores a zero vector rather than a null
element), or the domain point itself was reconstructed rather than tested against
surfaces (`ReconstructedDomainPoint`). Consumers use this both for colouring and
to decide what a vector means; `PlateVelocityUtils` also reads it back when
deciding whether smoothing applies near a boundary.

Construction is two-phase and deliberately so. `create_empty` pre-sizes the range
to `multi_point_ptr->number_of_points()` and fills it with `boost::none`; the
producer then walks the domain and the range in lockstep, assigning through the
non-const `begin()`/`end()` iterators. That is why the mutable iterator pair
exists on an otherwise read-only reconstruction geometry, and why an element may
legitimately still be null after the field has been published.

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

The load-bearing invariant is positional: the range has exactly as many elements
as the domain multi-point, and the i-th range element is the value at the i-th
domain point. Nothing enforces it after construction — the range is sized once in
the constructor and there is no `push_back` — so any code that iterates the domain
and the range together must advance both, and code that reorders or filters must
carry the index with it.

An element being `boost::none` means "no value assigned", which is not the same as
a zero vector; `NotInAnyBoundaryOrNetwork` is a real, assigned, zero-magnitude
sample. Readers must handle both.

The class is a `WeakObserver<FeatureHandle>`, so it does not keep its feature
alive: `is_valid()` and `feature_handle_ptr()` go null when the feature is
deleted, and `get_feature_ref()` then returns an invalid weak-ref rather than
throwing. `d_property_iterator` is an iterator into that feature's property list
and shares the same fate. The domain `MultiPointOnSphere` is the one thing held by
a counted pointer and always outlives the field.

`property()` is not guaranteed to point at a multi-point property. When called
from `solve_velocities_on_surfaces` the domain is produced by
`GeometryUtils::convert_geometry_to_multi_point` on the *reconstructed* geometry
of a `ReconstructedFeatureGeometry`, so the referenced property can hold a
polyline or polygon — the source flags this explicitly as "slightly dodgy". Do not
assume `property()` can be dereferenced back into `multi_point()`.

Also note the domain is the reconstructed position of the velocity domain, not the
present-day position. Assigning plate id zero to domain features is the documented
way to keep them fixed, and even that still moves under a non-zero anchored plate
id.

Constructors are protected so instances cannot be stack-allocated;
`get_non_null_pointer()` relies on that, since it hands out an intrusive reference
to `this`.

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
