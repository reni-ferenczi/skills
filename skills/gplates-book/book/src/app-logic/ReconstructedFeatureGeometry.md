# ReconstructedFeatureGeometry

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 84 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructedFeatureGeometry.h` | C++ | 515 |
| `src/app-logic/ReconstructedFeatureGeometry.cc` | C++ | 165 |

## Overview

The RFG is the workhorse output of the reconstruction pipeline: one geometry-valued property of one feature, carried to one geological time. It has two identities at once. As a `ReconstructionGeometry` it flows downstream into `Reconstruction`, the renderers and the exporters. As a `GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>` it is threaded onto the observer chain of the feature it came from, without owning or keeping that feature alive — which is what lets `ReconstructionGeometryFinder` walk in the other direction, from a feature to every reconstruction geometry currently observing it, and what makes `references()`, `is_valid()` and `feature_handle_ptr()` cheap and non-throwing.

Besides the geometry it carries its own provenance: the `ReconstructionTree` it was reconstructed with, a `ReconstructionTreeCreator` that can rebuild the equivalent tree at any other time using the same anchor plate and rotation features, and an iterator to the feature property the geometry came from. The cached reconstruction plate ID and time of formation are there because colouring by plate ID and colouring by age read them on every frame, and because a user clicking a geometry wants them; the plate ID is optional because a feature may be "reconstructed" with the identity rotation when it has no reconstruction plate ID, or by a method that is not plate-ID based at all.

The main design point is the pair of `create()` overloads. One is handed geometry that has already been reconstructed. The other is handed the *resolved* geometry — unreconstructed, but with any time-dependent geometry property already looked up at the reconstruction time — together with a `ReconstructMethodFiniteRotation`, and defers the transform until `reconstructed_geometry()` is first called, caching the result. That deferral is not a micro-optimisation: it keeps the rigid rotation visible to clients that would rather not materialise rotated geometry at all. `ReconstructLayerProxy` inserts the unrotated geometry plus its rotation into a spatial partition and rotates only the centroid; `GLReconstructedStaticPolygonMeshes` and `GLRasterCoRegistration` build present-day polygon meshes once and rotate them on the GPU, skipping any RFG that cannot offer a finite rotation; `LayerOutputRenderer` groups geometries by transform. A third, protected constructor initialises neither the geometry nor the transform and exists solely for `TopologyReconstructedFeatureGeometry`, whose deforming geometry cannot be expressed as a single rotation and which overrides `reconstructed_geometry()` instead.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructedFeatureGeometry`](#gplatesapplogicreconstructedfeaturegeometry) | class | [`ReconstructionGeometry`](ReconstructionGeometry.md)<br>[`GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>`](../model/WeakObserver.md) | — | 5 | — |

## Members

### `GPlatesAppLogic::ReconstructedFeatureGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructedFeatureGeometry>` | public | Typedef for a non-null shared pointer to a non-const ReconstructedFeatureGeometry. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructedFeatureGeometry>` | public | Typedef for a non-null shared pointer to a const ReconstructedFeatureGeometry. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ReconstructedFeatureGeometry>` | public | Typedef for boost::intrusive\_ptr\<ReconstructedFeatureGeometry\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ReconstructedFeatureGeometry>` | public | Typedef for boost::intrusive\_ptr\<const ReconstructedFeatureGeometry\>. |
| `WeakObserverType` | typedef | `GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>` | public | Typedef for the WeakObserver base class of this class. |
| `geometry_ptr_type` | typedef | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Typedef for a non-null shared pointer to a non-const GeometryOnSphere. |
| `point_seq_type` | typedef | `std::vector<GPlatesMaths::PointOnSphere>` | public | Typedef for a sequence of points. |
| `FiniteRotationReconstruction` | class | `None` | public | Used to obtain a resolved geometry and its finite rotation transform (reconstruction). |
| `create( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator_, GPlatesModel::FeatureHandle &feature_handle_, const GPlatesModel::FeatureHandle::iterator &property_iterator_, const geometry_ptr_type &reconstructed_geometry_, boost::optio ...` | method | `non_null_ptr_type` | public | Create a ReconstructedFeatureGeometry instance from a \*reconstructed\* geometry with an optional reconstruction plate ID and an optional time of formation. |
| `create( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator_, GPlatesModel::FeatureHandle &feature_handle_, const GPlatesModel::FeatureHandle::iterator &property_iterator_, // NOTE: This is the *unreconstructed* geometry... const geome ...` | method | `non_null_ptr_type` | public | Create a ReconstructedFeatureGeometry instance from an \*unreconstructed\* geometry and a reconstruction transform (specific to the particular reconstruct method). |
| `~ReconstructedFeatureGeometry()` | destructor | `None` | public | — |
| `get_non_null_pointer_to_const()` | method | `non_null_ptr_to_const_type` | public | Get a non-null pointer to a const ReconstructedFeatureGeometry which points to this instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_type` | public | Get a non-null pointer to a ReconstructedFeatureGeometry which points to this instance. |
| `get_reconstruction_tree()` | method | `ReconstructionTree::non_null_ptr_to_const_type` | public | Access the ReconstructionTree that was used to reconstruct this ReconstructionGeometry. |
| `get_reconstruction_tree_creator()` | method | `ReconstructionTreeCreator` | public | Gets the reconstruction tree creator that uses the same anchor plate and reconstruction features as used to create the tree returned by get\_reconstruction\_tree. |
| `references( const GPlatesModel::FeatureHandle &that_feature_handle)` | method | `bool` | public | Return whether this RFG references that\_feature\_handle. |
| `feature_handle_ptr()` | method | `GPlatesModel::FeatureHandle` | public | Return the pointer to the FeatureHandle. |
| `is_valid()` | method | `bool` | public | Return whether this pointer is valid to be dereferenced (to obtain a FeatureHandle). |
| `get_feature_ref()` | method | `GPlatesModel::FeatureHandle::weak_ref` | public | Return a weak-ref to the feature whose reconstructed geometry this RFG contains, or an invalid weak-ref, if this pointer is not valid to be dereferenced. |
| `property()` | method | `GPlatesModel::FeatureHandle::iterator` | public | Access the feature property which contained the reconstructed geometry. |
| `reconstructed_geometry()` | method | `geometry_ptr_type` | public | Returns the reconstructed geometry. |
| `get_reconstruct_method_type()` | method | `boost::optional<ReconstructMethod::Type>` | public | The reconstruct method type used to generate this RFG. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `ReconstructedFeatureGeometry( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator_, GPlatesModel::FeatureHandle &feature_handle_, GPlatesModel::FeatureHandle::iterator property_iterator_, const geometry_ptr_type &reconstructed_geometry ...` | constructor | `None` | protected | — |
| `ReconstructedFeatureGeometry( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator_, GPlatesModel::FeatureHandle &feature_handle_, GPlatesModel::FeatureHandle::iterator property_iterator_, // NOTE: This is the *unreconstructed* geometry ...` | constructor | `None` | protected | — |
| `ReconstructedFeatureGeometry( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator_, GPlatesModel::FeatureHandle &feature_handle_, GPlatesModel::FeatureHandle::iterator property_iterator_, boost::optional<ReconstructMethod::Type> recons ...` | constructor | `None` | protected | Used by derived class TopologyReconstructedFeatureGeometry. |
| `d_reconstruction_tree` | field | `ReconstructionTree::non_null_ptr_to_const_type` | private | The reconstruction tree used to reconstruct us. |
| `d_reconstruction_tree_creator` | field | `ReconstructionTreeCreator` | private | Used to create reconstruction trees similar that the tree used to reconstruction 'this' reconstruction geometry (the only difference being the reconstruction time). |
| `d_property_iterator` | field | `GPlatesModel::FeatureHandle::iterator` | private | This is an iterator to the (geometry-valued) property from which this RFG was derived. |
| `d_reconstructed_geometry` | field | `boost::optional<geometry_ptr_type>` | private | The reconstructed feature geometry. |
| `d_finite_rotation_reconstruction` | field | `boost::optional<FiniteRotationReconstruction>` | private | The optional finite rotation transform (and resolved geometry). |
| `d_reconstruct_method_type` | field | `boost::optional<ReconstructMethod::Type>` | private | The reconstruct method type used to generate this RFG. |
| `d_reconstruction_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | The cached reconstruction plate ID, if it exists. |
| `d_time_of_formation` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | The cached time of formation of the feature, if it exists. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTEDFEATUREGEOMETRY_H` | macro | `None` | — |

## Notes

**The core invariant.** Of the two public constructors, exactly one of `d_reconstructed_geometry` and `d_finite_rotation_reconstruction` is always initialised; `reconstructed_geometry()` relies on that and asserts (`AssertionFailureException`) if it finds neither. The third, protected constructor breaks the invariant deliberately and is only sound because `TopologyReconstructedFeatureGeometry` overrides `reconstructed_geometry()` and never reaches the base implementation. If you add another subclass through that constructor, you must override the method too.

**Resolved is not reconstructed.** `FiniteRotationReconstruction::get_resolved_geometry()` returns the geometry *before* the rotation is applied — present-day geometry when the property is constant in time, the looked-up value when it is time-dependent. Only `get_reconstructed_geometry()` (or the RFG's own `reconstructed_geometry()`) applies the transform. The two are the same type, so confusing them compiles.

**`finite_rotation_reconstruction()` returning `boost::none` is ambiguous.** It means either that the reconstruction genuinely is not a finite rotation, or merely that this RFG was created from already-reconstructed geometry when it could have been created the other way. Callers must handle `none` rather than treat it as "not rigid": `ReconstructLayerProxy` falls back to the reconstructed geometry, the OpenGL paths skip the geometry entirely.

**Caching and constness.** `d_reconstructed_geometry` is `mutable` and filled on the first call to the const `reconstructed_geometry()`. The first call therefore does the geometry transform, and concurrent first calls on the same instance are not safe.

**Weak observation.** The feature is not owned. If its `FeatureHandle` is destroyed, this RFG is unsubscribed and `feature_handle_ptr()` becomes NULL — check `is_valid()`, or use `get_feature_ref()`, which returns an invalid weak-ref in that case. The stored property iterator is not validated here either; callers should test `is_still_valid()` on it, as `ReconstructionGeometryUtils::get_geometry_property_iterator` does.

**Time comes from the tree.** All three constructors pass `reconstruction_tree_->get_reconstruction_time()` up to the `ReconstructionGeometry` base, so an RFG's reconstruction time cannot disagree with the tree that produced it.

**Ownership before visiting.** `get_non_null_pointer()`, `get_non_null_pointer_to_const()` and hence both `accept_visitor` overloads require the instance to already be held by an intrusive pointer; on a zero reference count they throw `IntrusivePointerZeroRefCountException`. Constructing an RFG anywhere but through `create()` is unsupported for this reason.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GeometryUtils](GeometryUtils.md) | app-logic | 118 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 43 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 40 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 40 |
| [app-logic/FlowlineGeometryPopulator](FlowlineGeometryPopulator.md) | app-logic | 36 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 30 |
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 29 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 26 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 26 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 26 |
| [app-logic/ResolvedTriangulationNetwork](ResolvedTriangulationNetwork.md) | app-logic | 23 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 23 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 22 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 21 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 21 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 21 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 20 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 20 |
| [app-logic/MotionPathGeometryPopulator](MotionPathGeometryPopulator.md) | app-logic | 18 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 18 |

*... and 96 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructedFeatureGeometry.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructedFeatureGeometry --body
python scripts/gpq.py uses ReconstructedFeatureGeometry --kind class
python scripts/gpq.py hier ReconstructedFeatureGeometry
```
