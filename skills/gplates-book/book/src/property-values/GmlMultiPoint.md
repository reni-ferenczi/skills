# GmlMultiPoint

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 620 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlMultiPoint.h` | C++ | 257 |
| `src/property-values/GmlMultiPoint.cc` | C++ | 101 |

## Overview

[[[PROSE overview unit=property-values/GmlMultiPoint tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlMultiPoint`](#gplatespropertyvaluesgmlmultipoint) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:MultiPoint". |

## Members

### `GPlatesPropertyValues::GmlMultiPoint`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlMultiPoint>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlMultiPoint\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlMultiPoint>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlMultiPoint\>. |
| `internal_multipoint_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GPlatesMaths::MultiPointOnSphere>` | public | A convenience typedef for the internal multipoint representation. |
| `~GmlMultiPoint()` | destructor | `None` | public | — |
| `create( const internal_multipoint_type &multipoint_)` | method | `non_null_ptr_type` | public | Create a GmlMultiPoint instance which contains a copy of multipoint\_. |
| `create( const internal_multipoint_type &multipoint_, const std::vector<GmlPoint::GmlProperty> &gml_properties_)` | method | `non_null_ptr_type` | public | Create a GmlMultiPoint instance which contains a copy of multipoint\_. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GmlMultiPoint::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `multipoint()` | method | `internal_multipoint_type` | public | Access the GPlatesMaths::MultiPointOnSphere which encodes the geometry of this instance. |
| `set_multipoint( const internal_multipoint_type &p)` | method | `void` | public | Set the GPlatesMaths::MultiPointOnSphere within this instance to p. |
| `set_gml_properties( const std::vector<GmlPoint::GmlProperty> &gml_properties_)` | method | `void` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlMultiPoint( const internal_multipoint_type &multipoint_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlMultiPoint( const internal_multipoint_type &multipoint_, const std::vector<GmlPoint::GmlProperty> &gml_properties_)` | constructor | `None` | protected | — |
| `GmlMultiPoint( const GmlMultiPoint &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `fill_gml_properties()` | method | `void` | private | Fills d\_gml\_properties with d\_multipoint.size() of GmlPoint::POS. |
| `d_multipoint` | field | `internal_multipoint_type` | private | — |
| `d_gml_properties` | field | `std::vector<GmlPoint::GmlProperty>` | private | It's not the nicest OO, but this vector must be of the same size as d\_multipoint. |
| `operator=` | field | `GmlMultiPoint` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLMULTIPOINT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GmlMultiPoint tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/FlowlineGeometryPopulator](../app-logic/FlowlineGeometryPopulator.md) | app-logic | 6 |
| [app-logic/MotionPathGeometryPopulator](../app-logic/MotionPathGeometryPopulator.md) | app-logic | 5 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 3 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 3 |
| [feature-visitors/GeometryFinder](../feature-visitors/GeometryFinder.md) | feature-visitors | 3 |
| [feature-visitors/GeometryRotator](../feature-visitors/GeometryRotator.md) | feature-visitors | 3 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 2 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 2 |
| [app-logic/MotionPathUtils](../app-logic/MotionPathUtils.md) | app-logic | 2 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 2 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 2 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 2 |
| [app-logic/ReconstructMethodFlowline](../app-logic/ReconstructMethodFlowline.md) | app-logic | 2 |
| [app-logic/ReconstructMethodMotionPath](../app-logic/ReconstructMethodMotionPath.md) | app-logic | 2 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 2 |
| [feature-visitors/GeometrySetter](../feature-visitors/GeometrySetter.md) | feature-visitors | 2 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 2 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 2 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 2 |

*... and 27 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlMultiPoint.h
python scripts/gpq.py def GPlatesPropertyValues::GmlMultiPoint --body
python scripts/gpq.py uses GmlMultiPoint --kind class
python scripts/gpq.py hier GmlMultiPoint
```
