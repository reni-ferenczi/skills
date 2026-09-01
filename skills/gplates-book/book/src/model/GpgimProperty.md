# GpgimProperty

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 493 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimProperty.h` | C++ | 456 |
| `src/model/GpgimProperty.cc` | C++ | 86 |

## Overview

One `GpgimProperty` is one property definition from `gpgim.xml`. `Gpgim` parses
that file at startup into these objects and hands them to the
`GpgimFeatureClass`es that may carry them; from then on this object is the
authority on four questions the rest of GPlates keeps asking about a property:
what is it called (`PropertyName`), what structural types may its value have
(`GpgimStructuralType`, with one of them designated the default), how many times
may it appear on one feature (`MultiplicityType`), and may its value be wrapped
in a time-dependent wrapper — and if so which of `gpml:ConstantValue`,
`gpml:PiecewiseAggregation` and `gpml:IrregularSampling`. Because none of that
is compiled in, adding a property to the model is an edit to the GPGIM XML
rather than to C++.

The consumers split roughly in two. `ModelUtils` and the GPML readers use it to
decide what to build and whether to accept what they read — which structural
type to instantiate for a new property, whether to add or strip a time-dependent
wrapper, whether a property occurrence count is legal. The `qt-widgets` creation
and editing dialogs use it to populate themselves: `get_user_friendly_name` and
`get_property_description` are the label and the tooltip the user sees, and
`has_geometry_structural_type` is how a dialog tells a geometry property from an
ordinary one without enumerating type names itself.

The class is reference-counted via `GPlatesUtils::ReferenceCount` and normally
passed as `non_null_ptr_to_const_type`, because a single instance is shared by
every feature class that inherits the property. The setters and `clone` exist
for one specific pattern, used by `GpmlUpgradeReaderUtils`: to read a file
written by an older GPlates, it clones the affected `GpgimProperty`, renames the
clone to the old property name, and builds a reader against that altered copy of
the schema. That is the intended way to vary a definition — clone first, then
mutate.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::GpgimProperty`](#gplatesmodelgpgimproperty) | class | [`GPlatesUtils::ReferenceCount<GpgimProperty>`](../utils/ReferenceCount.md) | — | 0 | Defines a property of a feature in the GPlates Geological Information Model (GPGIM). |

## Members

### `GPlatesModel::GpgimProperty`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpgimProperty>` | public | A convenience typedef for a shared pointer to a non-const GpgimProperty. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpgimProperty>` | public | A convenience typedef for a shared pointer to a const GpgimProperty. |
| `structural_type_seq_type` | typedef | `std::vector<GpgimStructuralType::non_null_ptr_to_const_type>` | public | Typedef for a sequence of structural types. |
| `MultiplicityType` | enum | `None` | public | The number of times this property can occur in its parent feature. |
| `TimeDependentType` | enum | `None` | public | The ways in which a property can be made time-dependent. |
| `time_dependent_flags_type` | typedef | `std::bitset<NUM_TIME_DEPENDENT_TYPES>` | public | Typedef for a flag of time-dependent types. |
| `create( const PropertyName &property_name, const QString &user_friendly_name, const QString &property_description, MultiplicityType multiplicity, StructuralTypeForwardIter structural_types_begin, StructuralTypeForwardIter structural_types_end, unsigned int default_structural_type_index, time_dependent_flags_type time_d ...` | method | `non_null_ptr_type` | public | Creates a GpgimProperty. |
| `create( const PropertyName &property_name, const QString &user_friendly_name, const QString &property_description, MultiplicityType multiplicity, const GpgimStructuralType::non_null_ptr_to_const_type &structural_type, time_dependent_flags_type time_dependent_types)` | method | `non_null_ptr_type` | public | Creates a GpgimProperty. |
| `clone()` | method | `non_null_ptr_type` | public | Clones 'this' object. |
| `set_property_name( const PropertyName &property_name)` | method | `void` | public | Sets the property name. |
| `set_user_friendly_name( const QString &user_friendly_name)` | method | `void` | public | Sets the user friendly name. |
| `set_property_description( const QString &property_description)` | method | `void` | public | Sets the property description. |
| `get_default_structural_type()` | method | `GpgimStructuralType::non_null_ptr_to_const_type` | public | Returns the default structural type for this property. |
| `get_structural_type( const GPlatesPropertyValues::StructuralType &structural_type)` | method | `boost::optional<GpgimStructuralType::non_null_ptr_to_const_type>` | public | Convenience method returns the structural type of this property matching the specified type. |
| `has_geometry_structural_type()` | method | `bool` | public | Returns true if any of the structural types represents a geometry. |
| `set_structural_types( StructuralTypeForwardIter structural_types_begin, StructuralTypeForwardIter structural_types_end, unsigned int default_structural_type_index)` | method | `void` | public | Sets the structural types. |
| `get_multiplicity()` | method | `MultiplicityType` | public | Returns the number of allowed occurrences of this property in its parent feature. |
| `set_multiplicity( MultiplicityType multiplicity)` | method | `void` | public | Sets the property multiplicity. |
| `is_time_dependent()` | method | `bool` | public | Returns true if this property is time-dependent. |
| `set_time_dependent_types( const time_dependent_flags_type &time_dependent_types)` | method | `void` | public | Sets the allowed time-dependent types. |
| `d_property_name` | field | `PropertyName` | private | The name of this property. |
| `d_user_friendly_name` | field | `QString` | private | The user-friendly name of this property. |
| `d_property_description` | field | `QString` | private | The description of this property. |
| `d_multiplicity` | field | `MultiplicityType` | private | The number of allowed occurrences of this property in its parent feature. |
| `d_structural_types` | field | `structural_type_seq_type` | private | The allowed structural types for this property. |
| `d_has_geometry_structural_type` | field | `bool` | private | Do any of the structural types represent a geoemtry? |
| `d_time_dependent_types` | field | `time_dependent_flags_type` | private | The allowed time-dependent types, if any, for this property. |
| `set_default_structural_type( unsigned int default_structural_type_index)` | method | `void` | private | — |
| `set_has_geometry_structural_type()` | method | `void` | private | — |
| `GpgimProperty( const PropertyName &property_name, const QString &user_friendly_name, const QString &property_description, MultiplicityType multiplicity, StructuralTypeForwardIter structural_types_begin, StructuralTypeForwardIter structural_types_end, unsigned int default_structural_type_index, time_dependent_flags_type ...` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_GPGIMPROPERTY_H` | macro | `None` | — |

## Notes

The default structural type is not stored as an index. `set_default_structural_type`
physically moves the chosen entry to the front of `d_structural_types`, so
`get_structural_types()` does not return them in GPGIM XML order and index 0 is
always the default. `get_default_structural_type()` relies on this by simply
calling `front()` with no check. Two consequences: a structural-type index taken
from one `GpgimProperty` is meaningless against another, and `clone()` correctly
passes a default index of 0 rather than re-deriving one.

There must be at least one structural type. `set_default_structural_type`
asserts both non-emptiness and that the index is in range, throwing
`GPlatesGlobal::PreconditionViolationError`; the constructor and
`set_structural_types` are the only callers, so the invariant holds from
construction onward. `get_default_structural_type()` has no guard of its own and
would be undefined on an empty sequence.

`d_has_geometry_structural_type` is a cache, recomputed by
`set_has_geometry_structural_type()` from the structural types at construction
and again on every `set_structural_types`. Any future path that edits
`d_structural_types` without going through that setter would leave it stale.

Instances are shared, not owned, so mutating one through a `non_null_ptr_type`
changes the schema seen by every feature class that inherits it, including for
files already loaded. The usual holder type is `non_null_ptr_to_const_type`
precisely to prevent that; reach for `clone()` when you need a variant. The
reference count itself is atomic (`boost::detail::atomic_count`), but nothing
about the object's contents is synchronised — treat the GPGIM as read-only after
`Gpgim` has finished loading it.

`NUM_TIME_DEPENDENT_TYPES` is the sentinel that sizes `time_dependent_flags_type`,
so it must stay last in `TimeDependentType`. An all-zero bitset means the value
must not be wrapped at all, which is what `is_time_dependent()` tests.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/Gpgim](Gpgim.md) | model | 74 |
| [model/ModelUtils](ModelUtils.md) | model | 65 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 48 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 48 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 36 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 31 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 30 |
| [qt-widgets/CreateFeatureAddOrEditPropertyDialog](../qt-widgets/CreateFeatureAddOrEditPropertyDialog.md) | qt-widgets | 21 |
| [qt-widgets/AddPropertyDialog](../qt-widgets/AddPropertyDialog.md) | qt-widgets | 17 |
| [model/GpgimFeatureClass](GpgimFeatureClass.md) | model | 15 |
| [qt-widgets/ChoosePropertyWidget](../qt-widgets/ChoosePropertyWidget.md) | qt-widgets | 15 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 12 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 10 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 9 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 6 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 3 |
| [qt-widgets/ChangePropertyWidget](../qt-widgets/ChangePropertyWidget.md) | qt-widgets | 2 |
| [qt-widgets/ChangeFeatureTypeDialog](../qt-widgets/ChangeFeatureTypeDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditEnumerationWidget](../qt-widgets/EditEnumerationWidget.md) | qt-widgets | 1 |
| [qt-widgets/TopologyToolsWidget](../qt-widgets/TopologyToolsWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/GpgimProperty.h
python scripts/gpq.py def GPlatesModel::GpgimProperty --body
python scripts/gpq.py uses GpgimProperty --kind class
python scripts/gpq.py hier GpgimProperty
```
