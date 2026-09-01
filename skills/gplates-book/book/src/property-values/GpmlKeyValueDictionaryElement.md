# GpmlKeyValueDictionaryElement

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1297 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlKeyValueDictionaryElement.h` | C++ | 116 |
| `src/property-values/GpmlKeyValueDictionaryElement.cc` | C++ | 65 |

## Overview

`GpmlKeyValueDictionaryElement` is the single key/value pair type held in a `GpmlKeyValueDictionary`'s element vector: an `XsString` key, a `PropertyValue` (the value, of arbitrary property-value type), and the `StructuralType` that value is expected to have. Unlike the property values around it, it is a plain value type, not itself a `GPlatesModel::PropertyValue` — it is only ever stored inside a dictionary, never attached directly to a feature.

It derives from `GPlatesUtils::QtStreamable` purely to pick up `operator<<` support for `qDebug()`/`QTextStream` from the single `std::ostream` `operator<<` overload declared alongside the class.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlKeyValueDictionaryElement`](#gplatespropertyvaluesgpmlkeyvaluedictionaryelement) | class | [`GPlatesUtils::QtStreamable<GpmlKeyValueDictionaryElement>`](../utils/QtStreamable.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlKeyValueDictionaryElement`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GpmlKeyValueDictionaryElement( GPlatesPropertyValues::XsString::non_null_ptr_type key_, GPlatesModel::PropertyValue::non_null_ptr_type value_, const StructuralType &value_type_)` | constructor | `None` | public | — |
| `~GpmlKeyValueDictionaryElement()` | destructor | `None` | public | — |
| `deep_clone()` | method | `GpmlKeyValueDictionaryElement` | public | — |
| `key()` | method | `GPlatesPropertyValues::XsString::non_null_ptr_to_const_type` | public | — |
| `value()` | method | `GPlatesModel::PropertyValue::non_null_ptr_to_const_type` | public | — |
| `operator==( const GpmlKeyValueDictionaryElement &other)` | operator | `bool` | public | — |
| `d_key` | field | `XsString::non_null_ptr_type` | private | — |
| `d_value` | field | `GPlatesModel::PropertyValue::non_null_ptr_type` | private | — |
| `d_value_type` | field | `StructuralType` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator==( const GpmlKeyValueDictionaryElement &other)` | operator | `bool` | — |
| `GPLATES_PROPERTYVALUES_GPMLKEYVALUEDICTIONARYELEMENT_H` | macro | `None` | — |
| `operator<<` | variable | `std::ostream` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 4 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 4 |
| [feature-visitors/ShapefileAttributeFinder](../feature-visitors/ShapefileAttributeFinder.md) | feature-visitors | 3 |
| [qt-widgets/ShapefileAttributeViewerDialog](../qt-widgets/ShapefileAttributeViewerDialog.md) | qt-widgets | 3 |
| [data-mining/PopulateShapeFileAttributesVisitor](../data-mining/PopulateShapeFileAttributesVisitor.md) | data-mining | 2 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 2 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 2 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 2 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 2 |
| [qt-widgets/EditShapefileAttributesWidget](../qt-widgets/EditShapefileAttributesWidget.md) | qt-widgets | 2 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 2 |
| [api/PyFeature](../api/PyFeature.md) | api | 1 |
| [data-mining/CheckAttrTypeVisitor](../data-mining/CheckAttrTypeVisitor.md) | data-mining | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 1 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 1 |
| [property-values/GpmlKeyValueDictionary](GpmlKeyValueDictionary.md) | property-values | 1 |
| [unit-test/FeatureHandleTest](../unit-test/FeatureHandleTest.md) | unit-test | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlKeyValueDictionaryElement.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlKeyValueDictionaryElement --body
python scripts/gpq.py uses GpmlKeyValueDictionaryElement --kind class
python scripts/gpq.py hier GpmlKeyValueDictionaryElement
```
