# GpgimStructuralType

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 566 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimStructuralType.h` | C++ | 237 |

## Overview

`GpgimStructuralType` describes one property structural type — the GPML/GML
value shape a property can hold, such as `gml:Point` or `gpml:Array` — as
recorded in the GPGIM. It pairs a `GPlatesPropertyValues::StructuralType` name
with a human-readable description and a flag for whether the type represents
geometry (used to recognise `gml:Point`, `gpml:TopologicalNetwork` and similar
types uniformly). `GpgimProperty` and `Gpgim` hold these to describe what
values a GPGIM property definition accepts.

Some structural types are templates — `gpml:Array` needs a value type before it
names a concrete instantiation, as in `gpml:Array<gml:TimePeriod>` — so
`get_instantiation_type()` returns an `InstantiationType` pairing the structural
type with an optional value type, and is virtual so the derived
`GpgimTemplateStructuralType` can override it to supply that value type.
`GpgimEnumerationType` is the other subclass, adding the allowed enumeration
values for `gpml:` enumeration types. Both derive from `ReferenceCount` and are
constructed only through the protected constructor plus each class's own
`create()`, kept off the stack like other reference-counted model objects.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::GpgimStructuralType`](#gplatesmodelgpgimstructuraltype) | class | [`GPlatesUtils::ReferenceCount<GpgimStructuralType>`](../utils/ReferenceCount.md) | — | 2 | Information about a property structural type in the GPlates Geological Information Model (GPGIM). |

## Members

### `GPlatesModel::GpgimStructuralType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpgimStructuralType>` | public | A convenience typedef for a shared pointer to a non-const GpgimStructuralType. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpgimStructuralType>` | public | A convenience typedef for a shared pointer to a const GpgimStructuralType. |
| `InstantiationType` | class | `None` | public | The instantiation type is the structural type of the property and an optional value type (only used if structural type is a template such as 'gpml:Array'). |
| `instantiation_type` | typedef | `InstantiationType` | public | — |
| `create( const GPlatesPropertyValues::StructuralType &structural_type, const QString &description, bool is_geometry_structural_type_ = false)` | method | `non_null_ptr_type` | public | Creates a GpgimStructuralType. |
| `~GpgimStructuralType()` | destructor | `None` | public | Virtual destructor since GpgimEnumerationType is sub-class and GPlatesUtils::dynamic\_pointer\_cast is used. |
| `is_geometry_structural_type()` | method | `bool` | public | Returns true if the structural type represents a geometry. |
| `get_instantiation_type()` | method | `instantiation_type` | public | Returns the instantiation type. |
| `GpgimStructuralType( const GPlatesPropertyValues::StructuralType &structural_type, const QString &description, bool is_geometry_structural_type_ = false)` | constructor | `None` | protected | — |
| `d_structural_type` | field | `GPlatesPropertyValues::StructuralType` | private | The structural type. |
| `d_description` | field | `QString` | private | The description of the structural type. |
| `d_is_geometry_structural_type` | field | `bool` | private | Is a geometry? |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_GPGIMSTRUCTURALTYPE_H` | macro | `None` | — |

## Notes

- The destructor is virtual specifically because `GpgimEnumerationType` (and
  `GpgimTemplateStructuralType`) subclass it and code uses
  `GPlatesUtils::dynamic_pointer_cast` on `non_null_ptr_type` values — omitting
  virtuality here would make that cast undefined behaviour on destruction.
- `get_instantiation_type()`'s base implementation assumes no value type; only
  override it when the structural type is genuinely a template, as
  `GpgimTemplateStructuralType` does.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/Gpgim](Gpgim.md) | model | 15 |
| [model/GpgimProperty](GpgimProperty.md) | model | 11 |
| [model/GpgimTemplateStructuralType](GpgimTemplateStructuralType.md) | model | 8 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 8 |
| [qt-widgets/CreateFeatureAddOrEditPropertyDialog](../qt-widgets/CreateFeatureAddOrEditPropertyDialog.md) | qt-widgets | 7 |
| [model/ModelUtils](ModelUtils.md) | model | 6 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 4 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 3 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 3 |
| [model/GpgimEnumerationType](GpgimEnumerationType.md) | model | 3 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 2 |
| [qt-widgets/AddPropertyDialog](../qt-widgets/AddPropertyDialog.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/GpgimStructuralType.h
python scripts/gpq.py def GPlatesModel::GpgimStructuralType --body
python scripts/gpq.py uses GpgimStructuralType --kind class
python scripts/gpq.py hier GpgimStructuralType
```
