# ReconstructionGeometry

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1562 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGeometry.h` | C++ | 159 |

## Overview

This is the root of everything the reconstruction engine emits. A layer's output at one instant in geological time — reconstructed feature geometries, resolved topological boundaries, lines and networks, velocity fields, rasters, co-registration results — is always a `ReconstructionGeometry` subclass, so a `Reconstruction` and the renderers downstream of it can hold one heterogeneous sequence of `non_null_ptr_type` and recover the concrete type later. The base itself deliberately carries almost nothing: a reconstruction time and an optional reconstruct handle. Everything that distinguishes one kind of output from another lives in the derived class.

Recovering the concrete type is done by double dispatch rather than RTTI. The two pure-virtual `accept_visitor` overloads (const and non-const) are the whole polymorphic interface of this class, and `ReconstructionGeometryUtils` builds every downcast, property lookup and type filter on top of them. Making both overloads pure virtual is what forces a new derived class to be wired into `ReconstructionGeometryVisitorBase` before it can compile — the visitor list and the class hierarchy cannot silently drift apart.

The reconstruct handle is the other half of the design. `ReconstructHandle::type` is a 64-bit `GPlatesUtils::Counter64` handed out by `ReconstructHandle::get_next_reconstruct_handle()`; a producer takes one handle and stamps it on every geometry in a single batch of output. This matters because a `GPlatesModel::FeatureHandle` can be observed by many reconstruction geometries at once — several layers, several reconstruction times, some of them stale but still alive — so a client that needs a specific one (for example resolving a topological section back to the geometry produced for it) filters candidates by handle. `ReconstructHandle.h` deliberately offers no "current handle" accessor, so that one client cannot accidentally file its geometries into another client's group.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionGeometryVisitor`](#gplatesapplogicreconstructiongeometryvisitor) | typedef | — | — | 1 | Typedef for visitor over non-const ReconstructionGeometry objects. |
| [`GPlatesAppLogic::ConstReconstructionGeometryVisitor`](#gplatesapplogicconstreconstructiongeometryvisitor) | typedef | — | — | 13 | Typedef for visitor over const ReconstructionGeometry objects. |
| [`GPlatesAppLogic::ReconstructionGeometry`](#gplatesapplogicreconstructiongeometry) | class | [`GPlatesUtils::ReferenceCount<ReconstructionGeometry>`](../utils/ReferenceCount.md) | — | 15 | Classes derived from ReconstructionGeometry contain geometry that has been reconstructed to a particular geological time-instant. |

## Members

### `GPlatesAppLogic::ReconstructionGeometryVisitor`

*None.*

### `GPlatesAppLogic::ConstReconstructionGeometryVisitor`

*None.*

### `GPlatesAppLogic::ReconstructionGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructionGeometry>` | public | A convenience typedef for a shared pointer to a non-const ReconstructionGeometry. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructionGeometry>` | public | A convenience typedef for a shared pointer to a const ReconstructionGeometry. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ReconstructionGeometry>` | public | A convenience typedef for boost::intrusive\_ptr\<ReconstructionGeometry\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ReconstructionGeometry>` | public | A convenience typedef for boost::intrusive\_ptr\<const ReconstructionGeometry\>. |
| `~ReconstructionGeometry()` | destructor | `None` | public | — |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `ReconstructionGeometry( const double &reconstruction_time_, boost::optional<ReconstructHandle::type> reconstruct_handle_ = boost::none)` | constructor | `None` | protected | Construct a ReconstructionGeometry instance. |
| `d_reconstruction_time` | field | `double` | private | The reconstruction time of this reconstruction geometry. |
| `d_reconstruct_handle` | field | `boost::optional<ReconstructHandle::type>` | private | An optional reconstruct handle that can be used by clients to identify where this RG came from. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONGEOMETRY_H` | macro | `None` | — |

## Notes

The two visitor typedefs at the top of this header are a verbatim copy of the ones in `ReconstructionGeometryVisitor.h`, together with the forward declaration of `ReconstructionGeometryVisitorBase`, so that this header does not have to include the visitor header. If you change the visitor's template signature you must change it in both files.

A `ReconstructionGeometry` is immutable after construction: both fields are set in the protected constructor and there is no setter. It is a snapshot, valid for exactly one reconstruction time; when the time changes, clients do not mutate it but re-look it up, typically through `ReconstructionGeometryUtils::find_reconstruction_geometries_observing_feature`. Note the time is stored as a plain `double`, not a `GPlatesPropertyValues::GeoTimeInstant`.

Ownership is intrusive and shared with the whole hierarchy: the count lives in the single `GPlatesUtils::ReferenceCount<ReconstructionGeometry>` base, and `intrusive_ptr_release` `static_cast`s to `ReconstructionGeometry *` before deleting — which is only correct because the destructor declared here is virtual. Because the counter is a `boost::detail::atomic_count`, taking and dropping references is thread-safe even though nothing else here is; `ReconstructHandle::get_next_reconstruct_handle` in particular increments an unguarded function-local static, which its own comment flags as needing protection if GPlates ever becomes multi-threaded.

Instances must be owned by an intrusive pointer before anything visits them. Derived `accept_visitor` implementations obtain the pointer they hand to the visitor via `GPlatesUtils::get_non_null_pointer(this)`, which asserts a non-zero reference count and throws `IntrusivePointerZeroRefCountException` otherwise. That is why derived classes keep their constructors non-public and expose static `create()` functions instead — a stack-allocated reconstruction geometry would compile and then throw on first visit.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 65 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 48 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 34 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 29 |
| [app-logic/ResolvedSubSegmentRangeInSection](ResolvedSubSegmentRangeInSection.md) | app-logic | 28 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 22 |
| [app-logic/TopologyIntersections](TopologyIntersections.md) | app-logic | 21 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 20 |
| [gui/ColourProxy](../gui/ColourProxy.md) | gui | 20 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 18 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 17 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 16 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 15 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 15 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 15 |
| [gui/AddClickedGeometriesToFeatureTable](../gui/AddClickedGeometriesToFeatureTable.md) | gui | 14 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 14 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 13 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 12 |
| [view-operations/RenderedGeometryUtils](../view-operations/RenderedGeometryUtils.md) | view-operations | 12 |

*... and 98 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionGeometry.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionGeometry --body
python scripts/gpq.py uses ReconstructionGeometry --kind class
python scripts/gpq.py hier ReconstructionGeometry
```
