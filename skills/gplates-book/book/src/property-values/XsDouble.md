# XsDouble

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1158 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/XsDouble.h` | C++ | 191 |
| `src/property-values/XsDouble.cc` | C++ | 38 |

## Overview

`XsDouble` is the `GPlatesModel::PropertyValue` wrapping a bare `double`, corresponding to the XML Schema `xsi:double` type (its `get_structural_type()` returns `StructuralType::create_xsi("double")`). It is the standard property-value representation for a scalar numeric quantity read from or written to GPML, and is registered with the visitor dispatch machinery via `DECLARE_PROPERTY_VALUE_FINDER(GPlatesPropertyValues::XsDouble, visit_xs_double)`, so `GPlatesFeatureVisitors::get_property_value()` and both `FeatureVisitor`/`ConstFeatureVisitor` hierarchies can find and visit it like any other property value.

Construction goes only through the `create()` factory, which returns a `non_null_ptr_type`; the constructors are protected so instances always live behind an intrusive-pointer and can never be created on the stack.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::XsDouble`](#gplatespropertyvaluesxsdouble) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::XsDouble`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<XsDouble>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<XsIntger\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const XsDouble>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const XsDouble\>. |
| `~XsDouble()` | destructor | `None` | public | — |
| `create( double value)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `value()` | method | `double` | public | Accesses the double contained within this XsDouble. |
| `set_value( const double &d)` | method | `void` | public | Set the double value contained within this XsDouble to d. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `XsDouble( double value_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `XsDouble( const XsDouble &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_value` | field | `double` | private | — |
| `operator=` | field | `XsDouble` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_XSDOUBLE_H` | macro | `None` | — |

## Notes

`set_value()` calls the inherited `update_instance_id()`, so mutating an `XsDouble` in place changes its identity for the purposes of clone-tracking (a clone otherwise shares its instance id with the object it was cloned from). `clone()` and `deep_clone()` are equivalent here since a `double` has no nested property values to recursively clone.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 13 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [qt-widgets/EditDoubleWidget](../qt-widgets/EditDoubleWidget.md) | qt-widgets | 3 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 2 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 2 |
| [app-logic/PalaeomagUtils](../app-logic/PalaeomagUtils.md) | app-logic | 1 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](../app-logic/ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 1 |
| [app-logic/ReconstructionFeatureProperties](../app-logic/ReconstructionFeatureProperties.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 1 |
| [data-mining/CheckAttrTypeVisitor](../data-mining/CheckAttrTypeVisitor.md) | data-mining | 1 |
| [data-mining/PopulateShapeFileAttributesVisitor](../data-mining/PopulateShapeFileAttributesVisitor.md) | data-mining | 1 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [feature-visitors/ShapefileAttributeFinder](../feature-visitors/ShapefileAttributeFinder.md) | feature-visitors | 1 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |

*... and 13 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/XsDouble.h
python scripts/gpq.py def GPlatesPropertyValues::XsDouble --body
python scripts/gpq.py uses XsDouble --kind class
python scripts/gpq.py hier XsDouble
```
