# XsInteger

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1105 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/XsInteger.h` | C++ | 190 |
| `src/property-values/XsInteger.cc` | C++ | 38 |

## Overview

A property value class wrapping a single `int`. `XsInteger` is a concrete type from the GPML/GML domain model representing XML Schema integer values in geological features. Like all property value types, it uses intrusive-pointer memory management, forbids stack allocation (constructor is protected), and implements the visitor pattern via `accept_visitor()` for feature traversal. Call `XsInteger::create()` to make an instance, then use `value()` and `set_value()` to read and modify the wrapped integer.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::XsInteger`](#gplatespropertyvaluesxsinteger) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::XsInteger`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<XsInteger>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<XsIntger\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const XsInteger>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const XsInteger\>. |
| `~XsInteger()` | destructor | `None` | public | — |
| `create( int value)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `value()` | method | `int` | public | Accesses the int contained within this XsInteger. |
| `set_value( const int &i)` | method | `void` | public | Set the int value contained within this XsInteger to i. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `XsInteger( int value_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `XsInteger( const XsInteger &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_value` | field | `int` | private | — |
| `operator=` | field | `XsInteger` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_XSINTEGER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 2 |
| [qt-widgets/EditIntegerWidget](../qt-widgets/EditIntegerWidget.md) | qt-widgets | 2 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 2 |
| [data-mining/CheckAttrTypeVisitor](../data-mining/CheckAttrTypeVisitor.md) | data-mining | 1 |
| [data-mining/PopulateShapeFileAttributesVisitor](../data-mining/PopulateShapeFileAttributesVisitor.md) | data-mining | 1 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/ShapefileAttributeFinder](../feature-visitors/ShapefileAttributeFinder.md) | feature-visitors | 1 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 1 |
| [file-io/OgrFormatFlowlineExport](../file-io/OgrFormatFlowlineExport.md) | file-io | 1 |
| [file-io/OgrFormatMotionPathExport](../file-io/OgrFormatMotionPathExport.md) | file-io | 1 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](../file-io/OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 1 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 1 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 1 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/XsInteger.h
python scripts/gpq.py def GPlatesPropertyValues::XsInteger --body
python scripts/gpq.py uses XsInteger --kind class
python scripts/gpq.py hier XsInteger
```
