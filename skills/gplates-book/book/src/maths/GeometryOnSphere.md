# GeometryOnSphere

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1560 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/GeometryOnSphere.h` | C++ | 112 |

## Overview

This header is the root of the geometry hierarchy that the rest of GPlates passes
around. Its four subclasses cover every shape the application can hold on the
globe, and almost all code outside `src/maths` deals with them through
`GeometryOnSphere::non_null_ptr_to_const_type` rather than the concrete types —
that is why the fan-in below is so wide. The design commitment visible in this
file is that geometries are *immutable, heap-allocated and shared*: the only
pointer typedefs declared here are to `const`, the reference-count base is
`boost::noncopyable`, and there is no mutating operation anywhere in the base.
Reconstructing a feature therefore never edits a geometry in place; it builds a
new one and hands out a new pointer.

Because the base is deliberately thin, recovering the concrete type is done by
double dispatch through `ConstGeometryOnSphereVisitor` (`accept_visitor`), not
by `dynamic_cast`. That visitor is the extension point almost everything uses —
`GPlatesFeatureVisitors::GeometryTypeFinder`, the exporters in `file-io`, the
renderers — so a new geometry kind is a change to two files, not to every
consumer.

The two proximity entry points are the other half of the interface, and they sit
on the geometry rather than in a free function because only the geometry knows
its own vertices and great-circle-arc segments. A hit returns a
`ProximityHitDetail` subclass carrying the closeness value and, for vertex
tests, the index of the vertex that was hit, which is what the canvas tools need
in order to know *what* the user clicked, not merely *that* they clicked
something. The header's own class comment claims the class declares pure
virtuals "for cloning"; it does not, and given the immutability above it does
not need to.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::GeometryOnSphere`](#gplatesmathsgeometryonsphere) | class | [`GPlatesUtils::ReferenceCount<GeometryOnSphere>`](../utils/ReferenceCount.md) | — | 4 | This class is the abstract base of all geometries on the sphere. |

## Members

### `GPlatesMaths::GeometryOnSphere`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GeometryOnSphere>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GeometryOnSphere\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const GeometryOnSphere>` | public | A convenience typedef for boost::intrusive\_ptr\<const GeometryOnSphere\>. |
| `~GeometryOnSphere()` | destructor | `None` | public | — |
| `test_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | Test for a proximity hit. |
| `test_vertex_proximity( const ProximityCriteria &criteria)` | method | `ProximityHitDetail::maybe_null_ptr_type` | public | Test for a proximity hit, but only on the vertices of the geometry. |
| `accept_visitor( ConstGeometryOnSphereVisitor &visitor)` | method | `void` | public | Accept a ConstGeometryOnSphereVisitor instance. |
| `get_non_null_pointer()` | method | `non_null_ptr_to_const_type` | public | Return this instance as a non-null pointer. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_GEOMETRYONSPHERE_H` | macro | `None` | — |

## Notes

- **`get_non_null_pointer()` throws on an unowned instance.** It forwards to
  `GPlatesUtils::get_non_null_pointer`, which asserts that the reference count is
  already non-zero and otherwise throws
  `GPlatesGlobal::IntrusivePointerZeroRefCountException`. Calling it from inside
  a constructor, or on a geometry that no intrusive pointer owns yet, is a
  run-time failure rather than a compile error.
- **The virtual destructor is load-bearing.** `ReferenceCount` is used through
  the curiously recurring template pattern with `GeometryOnSphere` as the
  `Derived` parameter, so `intrusive_ptr_release` `checked_delete`s the object
  through a `const GeometryOnSphere *`. Without the virtual destructor here, the
  concrete subclass destructors would never run.
- **Reference counting is thread-safe; the geometries are not "thread-safe" in
  any wider sense.** `ReferenceCount` stores a `boost::detail::atomic_count`, so
  copying pointers across threads is fine. Since the objects are immutable and
  only ever handed out as `const`, concurrent readers are safe too.
- **Adding a geometry type fails silently in existing visitors.** The `visit_*`
  functions on `ConstGeometryOnSphereVisitor` have empty bodies rather than being
  pure virtual, so a new subclass plus a new `visit_*` will compile everywhere
  and simply be ignored by every visitor that was not updated. If you add a fifth
  geometry, audit the `ConstGeometryOnSphereVisitor` subclasses by hand.
- `test_proximity` and `test_vertex_proximity` signal "no hit" by returning a
  null `ProximityHitDetail::maybe_null_ptr_type` (`ProximityHitDetail::null`),
  not by throwing — callers must check.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 43 |
| [utils/GeometryCreationUtils](../utils/GeometryCreationUtils.md) | utils | 36 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 33 |
| [maths/GeometryDistance](GeometryDistance.md) | maths | 31 |
| [canvas-tools/CanvasTool](../canvas-tools/CanvasTool.md) | canvas-tools | 30 |
| [maths/PolygonPartitioner](PolygonPartitioner.md) | maths | 29 |
| [maths/PolygonMesh](PolygonMesh.md) | maths | 26 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 22 |
| [feature-visitors/GeometryTypeFinder](../feature-visitors/GeometryTypeFinder.md) | feature-visitors | 21 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 20 |
| [file-io/OgrGeometryExporter](../file-io/OgrGeometryExporter.md) | file-io | 20 |
| [maths/PolygonFan](PolygonFan.md) | maths | 20 |
| [maths/GeometryInterpolation](GeometryInterpolation.md) | maths | 19 |
| [file-io/PlatesLineFormatWriter](../file-io/PlatesLineFormatWriter.md) | file-io | 18 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 17 |
| [app-logic/GeometryCookieCutter](../app-logic/GeometryCookieCutter.md) | app-logic | 16 |
| [canvas-tools/MeasureDistanceState](../canvas-tools/MeasureDistanceState.md) | canvas-tools | 16 |
| [file-io/PlatesLineFormatGeometryExporter](../file-io/PlatesLineFormatGeometryExporter.md) | file-io | 14 |
| [maths/PointOnSphere](PointOnSphere.md) | maths | 14 |
| [app-logic/ResolvedSubSegmentRangeInSection](../app-logic/ResolvedSubSegmentRangeInSection.md) | app-logic | 13 |

*... and 130 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/GeometryOnSphere.h
python scripts/gpq.py def GPlatesMaths::GeometryOnSphere --body
python scripts/gpq.py uses GeometryOnSphere --kind class
python scripts/gpq.py hier GeometryOnSphere
```
