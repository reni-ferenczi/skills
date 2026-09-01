# GpmlPropertyDelegate

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1103 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlPropertyDelegate.h` | C++ | 203 |
| `src/property-values/GpmlPropertyDelegate.cc` | C++ | 38 |

## Overview

`GpmlPropertyDelegate` is a `GPlatesModel::PropertyValue` that points at a property on a *different* feature, rather than holding a value itself: it stores the target's `GPlatesModel::FeatureId`, the `GPlatesModel::PropertyName` of the property to read on that feature, and the expected `StructuralType` of that property's value. It is how GPML topology geometry — `GpmlTopologicalLineSection`, `GpmlTopologicalPoint`, `GpmlTopologicalNetwork` — refers to the source features that supply its boundary or section geometry, since a topology is defined in terms of other features' geometry rather than owning coordinates directly.

The value type is fixed at construction and has no setter, since resolving a delegate depends on the referenced property actually having that type. `print_to()` renders the delegate as `<feature-id>:<aliased-property-name>` for diagnostic output.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlPropertyDelegate`](#gplatespropertyvaluesgpmlpropertydelegate) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlPropertyDelegate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlPropertyDelegate>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlPropertyDelegate\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlPropertyDelegate>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlPropertyDelegate\>. |
| `~GpmlPropertyDelegate()` | destructor | `None` | public | — |
| `create( const GPlatesModel::FeatureId &feature_, const GPlatesModel::PropertyName &property_name_, const StructuralType &value_type_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlPropertyDelegate( const GPlatesModel::FeatureId &feature_, const GPlatesModel::PropertyName &property_name_, const StructuralType &value_type_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlPropertyDelegate( const GpmlPropertyDelegate &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_feature` | field | `GPlatesModel::FeatureId` | private | — |
| `d_property_name` | field | `GPlatesModel::PropertyName` | private | — |
| `d_value_type` | field | `StructuralType` | private | — |
| `operator=` | field | `GpmlPropertyDelegate` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLPROPERTYDELEGATE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/GpmlTopologicalLineSection](GpmlTopologicalLineSection.md) | property-values | 9 |
| [property-values/GpmlTopologicalPoint](GpmlTopologicalPoint.md) | property-values | 9 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 2 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 2 |
| [property-values/GpmlTopologicalNetwork](GpmlTopologicalNetwork.md) | property-values | 2 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlPropertyDelegate.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlPropertyDelegate --body
python scripts/gpq.py uses GpmlPropertyDelegate --kind class
python scripts/gpq.py hier GpmlPropertyDelegate
```
