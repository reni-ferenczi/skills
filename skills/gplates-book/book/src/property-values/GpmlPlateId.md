# GpmlPlateId

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1212 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlPlateId.h` | C++ | 194 |
| `src/property-values/GpmlPlateId.cc` | C++ | 38 |

## Overview

`GpmlPlateId` wraps an integer plate ID—a fundamental identifier used throughout GPlates for referring to tectonic plates. This is a simple but ubiquitous property value type used in countless places to specify which plate a feature belongs to or affects. The class is mutable: the plate ID can be changed after construction via `set_value()`, which updates the instance ID to reflect the modification. Instances must be created via the factory method and held in intrusive pointers. The wide use of this class (62+ units) reflects how central plate identification is to plate motion modeling.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlPlateId`](#gplatespropertyvaluesgpmlplateid) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlPlateId`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlPlateId>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlPlateId\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlPlateId>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlPlateId\>. |
| `~GpmlPlateId()` | destructor | `None` | public | — |
| `create( const GPlatesModel::integer_plate_id_type &value_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_value( const GPlatesModel::integer_plate_id_type &p)` | method | `void` | public | Set the plate id contained within this GpmlPlateId to p. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlPlateId( const GPlatesModel::integer_plate_id_type &value_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlPlateId( const GpmlPlateId &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_value` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `operator=` | field | `GpmlPlateId` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLPLATEID_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 3 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 2 |
| [app-logic/MotionPathUtils](../app-logic/MotionPathUtils.md) | app-logic | 2 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 2 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 2 |
| [qt-widgets/EditPlateIdWidget](../qt-widgets/EditPlateIdWidget.md) | qt-widgets | 2 |
| [app-logic/FlowlineGeometryPopulator](../app-logic/FlowlineGeometryPopulator.md) | app-logic | 1 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 1 |
| [app-logic/MotionPathGeometryPopulator](../app-logic/MotionPathGeometryPopulator.md) | app-logic | 1 |
| [app-logic/PalaeomagUtils](../app-logic/PalaeomagUtils.md) | app-logic | 1 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 1 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 1 |
| [app-logic/ReconstructMethodByPlateId](../app-logic/ReconstructMethodByPlateId.md) | app-logic | 1 |
| [app-logic/ReconstructMethodFlowline](../app-logic/ReconstructMethodFlowline.md) | app-logic | 1 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 1 |
| [app-logic/ReconstructMethodMotionPath](../app-logic/ReconstructMethodMotionPath.md) | app-logic | 1 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 1 |
| [app-logic/ReconstructionFeatureProperties](../app-logic/ReconstructionFeatureProperties.md) | app-logic | 1 |
| [app-logic/ReconstructionGraphPopulator](../app-logic/ReconstructionGraphPopulator.md) | app-logic | 1 |

*... and 62 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlPlateId.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlPlateId --body
python scripts/gpq.py uses GpmlPlateId --kind class
python scripts/gpq.py hier GpmlPlateId
```
