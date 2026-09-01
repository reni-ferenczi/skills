# GmlPoint

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 758 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlPoint.h` | C++ | 328 |
| `src/property-values/GmlPoint.cc` | C++ | 108 |

## Overview

[[[PROSE overview unit=property-values/GmlPoint tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlPoint`](#gplatespropertyvaluesgmlpoint) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:Point". |

## Members

### `GPlatesPropertyValues::GmlPoint`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlPoint>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlPoint\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlPoint>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlPoint\>. |
| `~GmlPoint()` | destructor | `None` | public | — |
| `GmlProperty` | enum | `None` | public | In GML 3.0, the whereabouts of a gml:Point can be specified using the "pos" property or the "coordinates" property. |
| `create_from_lon_lat( const std::pair<double/*lon*/, double/*lat*/> &gml_pos, GmlProperty gml_property_ = POS)` | method | `non_null_ptr_type` | public | Create a GmlPoint instance from a (longitude, latitude) coordinate duple. |
| `create_from_pos_2d( const std::pair<double, double> &pos_2d, GmlProperty gml_property_ = POS)` | method | `non_null_ptr_type` | public | Create a GmlPoint instance from a 2D coordinate duple. |
| `create( const GPlatesMaths::PointOnSphere &p, GmlProperty gml_property_ = POS)` | method | `non_null_ptr_type` | public | Create a GmlPoint instance from a GPlatesMaths::PointOnSphere instance. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GmlPoint::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `point` | field | `GPlatesMaths::PointOnSphere` | public | Access the GPlatesMaths::PointOnSphere which encodes the geometry of this instance. |
| `point_in_lat_lon()` | method | `GPlatesMaths::LatLonPoint` | public | Returns the point as a lat-lon point. |
| `point_2d` | field | `std::pair<double, double>` | public | Returns the point as a 2D (x,y) point. |
| `set_point( const GPlatesMaths::PointOnSphere &p)` | method | `void` | public | Set the point within this instance to p. |
| `gml_property()` | method | `GmlProperty` | public | — |
| `set_gml_property( GmlProperty gml_property_)` | method | `void` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlPoint( const std::pair<double, double> &point_2d_, GmlProperty gml_property_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlPoint( const GPlatesMaths::PointOnSphere &point_on_sphere_, GmlProperty gml_property_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlPoint( const GmlPoint &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_gml_property` | field | `GmlProperty` | private | — |
| `d_point_2d` | field | `boost::optional< std::pair<double, double> >` | private | One of these will always exist depending on how this instance was created. |
| `d_point_on_sphere` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `operator=` | field | `GmlPoint` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLPOINT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GmlPoint tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 13 |
| [property-values/GmlMultiPoint](GmlMultiPoint.md) | property-values | 12 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 8 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 6 |
| [property-values/GmlRectifiedGrid](GmlRectifiedGrid.md) | property-values | 6 |
| [app-logic/FlowlineGeometryPopulator](../app-logic/FlowlineGeometryPopulator.md) | app-logic | 4 |
| [app-logic/MotionPathGeometryPopulator](../app-logic/MotionPathGeometryPopulator.md) | app-logic | 3 |
| [app-logic/PalaeomagUtils](../app-logic/PalaeomagUtils.md) | app-logic | 3 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 3 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 3 |
| [feature-visitors/GeometryFinder](../feature-visitors/GeometryFinder.md) | feature-visitors | 3 |
| [feature-visitors/GeometryRotator](../feature-visitors/GeometryRotator.md) | feature-visitors | 3 |
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 3 |
| [property-values/GpmlFiniteRotation](GpmlFiniteRotation.md) | property-values | 3 |
| [qt-widgets/EditGeometryWidget](../qt-widgets/EditGeometryWidget.md) | qt-widgets | 3 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 2 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 2 |
| [app-logic/MotionPathUtils](../app-logic/MotionPathUtils.md) | app-logic | 2 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 2 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 2 |

*... and 35 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlPoint.h
python scripts/gpq.py def GPlatesPropertyValues::GmlPoint --body
python scripts/gpq.py uses GmlPoint --kind class
python scripts/gpq.py hier GmlPoint
```
