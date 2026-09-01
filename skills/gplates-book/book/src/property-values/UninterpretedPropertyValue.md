# UninterpretedPropertyValue

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1273 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/UninterpretedPropertyValue.h` | C++ | 178 |
| `src/property-values/UninterpretedPropertyValue.cc` | C++ | 39 |

## Overview

A property value that wraps an uninterpreted XML element node for properties that the parser could not deserialize as a known GPML type. It retains the raw XML element to preserve the data, allowing the property to be read without loss and potentially re-interpreted later or saved back to file unchanged. The wrapped element is immutable and accessed via `value()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::UninterpretedPropertyValue`](#gplatespropertyvaluesuninterpretedpropertyvalue) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements an uninterpreted PropertyValue. |

## Members

### `GPlatesPropertyValues::UninterpretedPropertyValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<UninterpretedPropertyValue>` | public | A convenience typedef for a shared pointer to a non-const UninterpretedPropertyValue. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const UninterpretedPropertyValue>` | public | A convenience typedef for a shared pointer to a const UninterpretedPropertyValue. |
| `~UninterpretedPropertyValue()` | destructor | `None` | public | — |
| `create( const GPlatesModel::XmlElementNode::non_null_ptr_to_const_type &value)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `UninterpretedPropertyValue( const GPlatesModel::XmlElementNode::non_null_ptr_to_const_type &value_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `UninterpretedPropertyValue( const UninterpretedPropertyValue &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_value` | field | `GPlatesModel::XmlElementNode::non_null_ptr_to_const_type` | private | — |
| `operator=` | field | `UninterpretedPropertyValue` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_UNINTERPRETEDPROPERTYVALUE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 3 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 1 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/UninterpretedPropertyValue.h
python scripts/gpq.py def GPlatesPropertyValues::UninterpretedPropertyValue --body
python scripts/gpq.py uses UninterpretedPropertyValue --kind class
python scripts/gpq.py hier UninterpretedPropertyValue
```
