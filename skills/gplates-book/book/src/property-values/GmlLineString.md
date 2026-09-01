# GmlLineString

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1153 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlLineString.h` | C++ | 209 |
| `src/property-values/GmlLineString.cc` | C++ | 53 |

## Overview

`GmlLineString` is the `PropertyValue` for `gml:LineString`: it wraps a
`GPlatesMaths::PolylineOnSphere` (held via `internal_polyline_type`, a
`non_null_intrusive_ptr<const PolylineOnSphere>`) so an open, non-closed line-shaped
geometry can be attached to a feature property. It is one of several
geometry-property-value wrappers in this component (alongside `GmlPoint`,
`GmlPolygon`, `GmlOrientableCurve` and similar), each pairing one `GPlatesMaths`
geometry type with the GML element name it corresponds to.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlLineString`](#gplatespropertyvaluesgmllinestring) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:LineString". |

## Members

### `GPlatesPropertyValues::GmlLineString`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlLineString>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlLineString\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlLineString>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlLineString\>. |
| `internal_polyline_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::PolylineOnSphere>` | public | A convenience typedef for the internal polyline representation. |
| `~GmlLineString()` | destructor | `None` | public | — |
| `create( const internal_polyline_type &polyline_)` | method | `non_null_ptr_type` | public | Create a GmlLineString instance which contains a copy of polyline\_. |
| `clone()` | method | `GmlLineString::non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GmlLineString::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `polyline()` | method | `internal_polyline_type` | public | Access the GPlatesMaths::PolylineOnSphere which encodes the geometry of this instance. |
| `set_polyline( const internal_polyline_type &p)` | method | `void` | public | Set the polyline within this instance to p. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlLineString( const internal_polyline_type &polyline_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlLineString( const GmlLineString &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_polyline` | field | `internal_polyline_type` | private | — |
| `operator=` | field | `GmlLineString` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLLINESTRING_H` | macro | `None` | — |

## Notes

`polyline()` deliberately returns only a pointer-to-const: the contained
`PolylineOnSphere` must never be mutated in place, since `PolylineOnSphere` is shared
(reference-counted) and possibly aliased elsewhere. To change the geometry, replace it
wholesale via `set_polyline()`, which also calls `update_instance_id()`.

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/GmlOrientableCurve](GmlOrientableCurve.md) | property-values | 7 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 5 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 3 |
| [feature-visitors/GeometryFinder](../feature-visitors/GeometryFinder.md) | feature-visitors | 3 |
| [feature-visitors/GeometryRotator](../feature-visitors/GeometryRotator.md) | feature-visitors | 3 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 3 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 2 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 2 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 2 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 2 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 2 |
| [feature-visitors/GeometrySetter](../feature-visitors/GeometrySetter.md) | feature-visitors | 2 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 2 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 2 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 2 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 2 |
| [file-io/PlatesLineFormatWriter](../file-io/PlatesLineFormatWriter.md) | file-io | 2 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 2 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 2 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 1 |

*... and 16 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlLineString.h
python scripts/gpq.py def GPlatesPropertyValues::GmlLineString --body
python scripts/gpq.py uses GmlLineString --kind class
python scripts/gpq.py hier GmlLineString
```
