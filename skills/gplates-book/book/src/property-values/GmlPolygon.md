# GmlPolygon

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1154 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlPolygon.h` | C++ | 209 |
| `src/property-values/GmlPolygon.cc` | C++ | 50 |

## Overview

`GmlPolygon` is the `GPlatesModel::PropertyValue` for `gml:Polygon`. It is a
thin, immutable-geometry wrapper around a `GPlatesMaths::PolygonOnSphere`,
held by `internal_polygon_type` (a `non_null_intrusive_ptr` to a const
polygon) — the same shape as `GmlMultiPoint` and `GmlPoint` use for their own
maths geometry, since none of these classes have anything left to add on top
of the underlying `PropertyValue` machinery besides the geometry itself and
`get_structural_type()`/`accept_visitor()` boilerplate.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlPolygon`](#gplatespropertyvaluesgmlpolygon) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:Polygon". |

## Members

### `GPlatesPropertyValues::GmlPolygon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlPolygon>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlPolygon\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlPolygon>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlPolygon\>. |
| `internal_polygon_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::PolygonOnSphere>` | public | A convenience typedef for the internal polygon representation. |
| `~GmlPolygon()` | destructor | `None` | public | — |
| `create( const internal_polygon_type &polygon_)` | method | `non_null_ptr_type` | public | Create a GmlPolygon instance which contains a copy of polygon\_. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `polygon()` | method | `internal_polygon_type` | public | Access the GPlatesMaths::PolygonOnSphere which encodes the geometry of this instance. |
| `set_polygon( const internal_polygon_type &p)` | method | `void` | public | Set the polygon within this instance to p. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlPolygon( const internal_polygon_type &polygon_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlPolygon( const GmlPolygon &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_polygon` | field | `internal_polygon_type` | private | — |
| `operator=` | field | `GmlPolygon` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLPOLYGON_H` | macro | `None` | — |

## Notes

- `polygon()` deliberately has no non-`const` overload: the header notes the
  contained `PolygonOnSphere` must not be modified in place, and callers who
  need a different polygon must build one and call `set_polygon()` instead.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 3 |
| [feature-visitors/GeometryFinder](../feature-visitors/GeometryFinder.md) | feature-visitors | 3 |
| [feature-visitors/GeometryRotator](../feature-visitors/GeometryRotator.md) | feature-visitors | 3 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 3 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 2 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 2 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 2 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 2 |
| [feature-visitors/GeometrySetter](../feature-visitors/GeometrySetter.md) | feature-visitors | 2 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 2 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 2 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 2 |
| [file-io/PlatesLineFormatWriter](../file-io/PlatesLineFormatWriter.md) | file-io | 2 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 1 |
| [app-logic/ReconstructMethodFlowline](../app-logic/ReconstructMethodFlowline.md) | app-logic | 1 |
| [app-logic/ReconstructMethodMotionPath](../app-logic/ReconstructMethodMotionPath.md) | app-logic | 1 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 1 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 1 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 1 |

*... and 14 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlPolygon.h
python scripts/gpq.py def GPlatesPropertyValues::GmlPolygon --body
python scripts/gpq.py uses GmlPolygon --kind class
python scripts/gpq.py hier GmlPolygon
```
