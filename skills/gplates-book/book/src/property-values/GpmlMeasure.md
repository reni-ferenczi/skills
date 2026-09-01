# GpmlMeasure

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1053 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlMeasure.h` | C++ | 232 |
| `src/property-values/GpmlMeasure.cc` | C++ | 58 |

## Overview

[[[PROSE overview unit=property-values/GpmlMeasure tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlMeasure`](#gplatespropertyvaluesgpmlmeasure) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlMeasure`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlMeasure>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlMeasure\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlMeasure>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlMeasure\>. |
| `~GpmlMeasure()` | destructor | `None` | public | — |
| `create( const double &quantity, const std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue> & quantity_xml_attributes_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_quantity( const double &q)` | method | `void` | public | Set the quantity of this GpmlMeasure to q. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlMeasure( const double &quantity_, const std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue> & quantity_xml_attributes_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlMeasure( const GpmlMeasure &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `d_quantity` | field | `double` | private | — |
| `d_quantity_xml_attributes` | field | `std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue>` | private | — |
| `operator=` | field | `GpmlMeasure` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLMEASURE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlMeasure tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 5 |
| [qt-widgets/EditAngleWidget](../qt-widgets/EditAngleWidget.md) | qt-widgets | 3 |
| [app-logic/SmallCircleGeometryPopulator](../app-logic/SmallCircleGeometryPopulator.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [data-mining/PopulateShapeFileAttributesVisitor](../data-mining/PopulateShapeFileAttributesVisitor.md) | data-mining | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/ShapefileAttributeFinder](../feature-visitors/ShapefileAttributeFinder.md) | feature-visitors | 1 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [property-values/GpmlFiniteRotation](GpmlFiniteRotation.md) | property-values | 1 |
| [property-values/GpmlHotSpotTrailMark](GpmlHotSpotTrailMark.md) | property-values | 1 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 1 |
| [qt-widgets/SmallCircleWidget](../qt-widgets/SmallCircleWidget.md) | qt-widgets | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlMeasure.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlMeasure --body
python scripts/gpq.py uses GpmlMeasure --kind class
python scripts/gpq.py hier GpmlMeasure
```
