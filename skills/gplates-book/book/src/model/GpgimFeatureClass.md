# GpgimFeatureClass

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 890 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimFeatureClass.h` | C++ | 277 |
| `src/model/GpgimFeatureClass.cc` | C++ | 182 |

## Overview

`GpgimFeatureClass` represents one feature type's entry in the GPGIM — a
`FeatureType` name, a description, its own `GpgimProperty` definitions, an
optional default geometry property, and an optional parent class. Feature
classes form a single-inheritance tree (`Gpgim` builds and owns it), with
concrete, instantiable feature types at the leaves and abstract classes above
them; `does_inherit_from()` walks up via `get_parent_feature_class()` to test
membership anywhere in that chain.

Most query methods come in an "including ancestors" and an "excluding
ancestors" form: `get_feature_properties()` and `get_geometry_feature_properties()`
recurse up through `d_parent_feature_class` first and append this class's own
`d_feature_properties` after, so a derived feature class's own properties are
never confused with the accessor that returns only what it declares itself
(`get_feature_properties_excluding_ancestor_classes()`). The same override rule
applies to the default geometry property: `get_default_geometry_feature_property()`
returns this class's own default if it has one, and only falls back to the
parent's when it does not — a derived class's default geometry property takes
precedence.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::GpgimFeatureClass`](#gplatesmodelgpgimfeatureclass) | class | [`GPlatesUtils::ReferenceCount<GpgimFeatureClass>`](../utils/ReferenceCount.md) | — | 0 | Represents the class of feature in the GPlates Geological Information Model (GPGIM). |

## Members

### `GPlatesModel::GpgimFeatureClass`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpgimFeatureClass>` | public | A convenience typedef for a shared pointer to a non-const GpgimFeatureClass. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpgimFeatureClass>` | public | A convenience typedef for a shared pointer to a const GpgimFeatureClass. |
| `gpgim_property_seq_type` | typedef | `std::vector<GpgimProperty::non_null_ptr_to_const_type>` | public | Typedef for a sequence of GPGIM properties (definitions). |
| `create( const FeatureType &feature_type, const QString &feature_description, GpgimPropertyForwardIter gpgim_properties_begin, GpgimPropertyForwardIter gpgim_properties_end, boost::optional<GpgimProperty::non_null_ptr_to_const_type> default_geometry_property = boost::none, boost::optional<GpgimFeatureClass::non_null_ptr ...` | method | `non_null_ptr_type` | public | Creates a GpgimFeatureClass that (optionally) inherits from the specified parent feature class. feature class (but not its ancestor classes). feature class (but not its ancestor classes). |
| `get_feature_properties( gpgim_property_seq_type &feature_properties)` | method | `void` | public | Returns the GPGIM properties of this feature class (including ancestor feature classes). |
| `get_feature_properties( const GPlatesPropertyValues::StructuralType &property_type, boost::optional<gpgim_property_seq_type &> feature_properties = boost::none)` | method | `bool` | public | Convenience method returns the GPGIM property(s) of the specified property type. |
| `get_feature_property( const GPlatesModel::PropertyName &property_name)` | method | `boost::optional<GpgimProperty::non_null_ptr_to_const_type>` | public | Convenience method returns the GPGIM property of the specified property name. |
| `get_geometry_feature_properties( gpgim_property_seq_type &geometry_feature_properties)` | method | `bool` | public | Returns the GPGIM \*geometry\* properties of this feature class (including ancestor feature classes). |
| `get_default_geometry_feature_property()` | method | `boost::optional<GpgimProperty::non_null_ptr_to_const_type>` | public | Returns the default GPGIM property that represents a \*geometry\* property for this feature class. |
| `get_default_geometry_feature_property_excluding_ancestor_classes()` | method | `boost::optional<GpgimProperty::non_null_ptr_to_const_type>` | public | Same as get\_default\_geometry\_feature\_property but excludes ancestor feature classes. |
| `get_parent_feature_class()` | method | `boost::optional<GpgimFeatureClass::non_null_ptr_to_const_type>` | public | Returns the parent feature class that this feature class inherits from, or returns boost::none if this is the root class (ie, has no parent). |
| `does_inherit_from( const GPlatesModel::FeatureType &feature_type)` | method | `bool` | public | Returns true if this feature class inherits directly or indirectly from the specified feature type. |
| `d_feature_type` | field | `FeatureType` | private | The GPGIM feature type (string) of this feature class. |
| `d_feature_description` | field | `QString` | private | A short description of the feature type. |
| `d_feature_properties` | field | `gpgim_property_seq_type` | private | The GPGIM properties of this feature class. |
| `d_default_geometry_property` | field | `boost::optional<GpgimProperty::non_null_ptr_to_const_type>` | private | The optional default geometry property. |
| `d_parent_feature_class` | field | `boost::optional<GpgimFeatureClass::non_null_ptr_to_const_type>` | private | Optional parent feature class that 'this' feature class inherits from. |
| `GpgimFeatureClass( const FeatureType &feature_type, const QString &feature_description, GpgimPropertyForwardIter gpgim_properties_begin, GpgimPropertyForwardIter gpgim_properties_end, boost::optional<GpgimProperty::non_null_ptr_to_const_type> default_geometry_property, boost::optional<GpgimFeatureClass::non_null_ptr_to ...` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_GPGIMFEATURECLASS_H` | macro | `None` | — |

## Notes

- `create()` asserts (`GPlatesGlobal::PreconditionViolationError`) that
  `default_geometry_property`, when given, is actually one of the properties in
  `[gpgim_properties_begin, gpgim_properties_end)` — passing a property that
  belongs to a different feature class throws at construction.
- Overriding a default geometry property in a derived class silently shadows an
  ancestor's default rather than erroring; per the header comment this is not
  expected to occur if the GPGIM itself is designed correctly.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 70 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 39 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 30 |
| [model/Gpgim](Gpgim.md) | model | 25 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 14 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 6 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 6 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 5 |
| [qt-widgets/AddPropertyDialog](../qt-widgets/AddPropertyDialog.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/GpgimFeatureClass.h
python scripts/gpq.py def GPlatesModel::GpgimFeatureClass --body
python scripts/gpq.py uses GpgimFeatureClass --kind class
python scripts/gpq.py hier GpgimFeatureClass
```
