# GmlTimeInstant

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 997 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlTimeInstant.h` | C++ | 223 |
| `src/property-values/GmlTimeInstant.cc` | C++ | 78 |

## Overview

[[[PROSE overview unit=property-values/GmlTimeInstant tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlTimeInstant`](#gplatespropertyvaluesgmltimeinstant) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GmlTimeInstant`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlTimeInstant>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlTimeInstant\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlTimeInstant>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlTimeInstant\>. |
| `xml_attribute_map_type` | typedef | `std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue>` | public | Typedef for an XML attribute (name/value) map. |
| `~GmlTimeInstant()` | destructor | `None` | public | — |
| `create( const GeoTimeInstant &time_position_, const xml_attribute_map_type &time_position_xml_attributes_ = xml_attribute_map_type())` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GmlTimeInstant::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_time_position( const GeoTimeInstant &tp)` | method | `void` | public | Set the temporal position of this GmlTimeInstant to tp. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlTimeInstant( const GeoTimeInstant &time_position_, const xml_attribute_map_type & time_position_xml_attributes_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlTimeInstant( const GmlTimeInstant &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `d_time_position` | field | `GeoTimeInstant` | private | — |
| `d_time_position_xml_attributes` | field | `xml_attribute_map_type` | private | — |
| `operator=` | field | `GmlTimeInstant` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLTIMEINSTANT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GmlTimeInstant tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/GmlTimePeriod](GmlTimePeriod.md) | property-values | 16 |
| [property-values/GpmlTimeSample](GpmlTimeSample.md) | property-values | 7 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 5 |
| [feature-visitors/deprecated/GmlTimePeriodFinder](../feature-visitors/deprecated/GmlTimePeriodFinder.md) | feature-visitors | 4 |
| [qt-widgets/EditTimeInstantWidget](../qt-widgets/EditTimeInstantWidget.md) | qt-widgets | 3 |
| [file-io/PlatesLineFormatHeaderVisitor](../file-io/PlatesLineFormatHeaderVisitor.md) | file-io | 2 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 2 |
| [app-logic/FlowlineGeometryPopulator](../app-logic/FlowlineGeometryPopulator.md) | app-logic | 1 |
| [app-logic/MotionPathGeometryPopulator](../app-logic/MotionPathGeometryPopulator.md) | app-logic | 1 |
| [app-logic/PlateVelocityUtils](../app-logic/PlateVelocityUtils.md) | app-logic | 1 |
| [app-logic/ReconstructScalarCoverageLayerProxy](../app-logic/ReconstructScalarCoverageLayerProxy.md) | app-logic | 1 |
| [app-logic/ReconstructionFeatureProperties](../app-logic/ReconstructionFeatureProperties.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [data-mining/PopulateShapeFileAttributesVisitor](../data-mining/PopulateShapeFileAttributesVisitor.md) | data-mining | 1 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/ShapefileAttributeFinder](../feature-visitors/ShapefileAttributeFinder.md) | feature-visitors | 1 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatFlowlineExport](../file-io/GMTFormatFlowlineExport.md) | file-io | 1 |

*... and 19 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlTimeInstant.h
python scripts/gpq.py def GPlatesPropertyValues::GmlTimeInstant --body
python scripts/gpq.py uses GmlTimeInstant --kind class
python scripts/gpq.py hier GmlTimeInstant
```
