# GpgimTemplateStructuralType

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 566 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimTemplateStructuralType.h` | C++ | 132 |

## Overview

`GpgimTemplateStructuralType` extends `GpgimStructuralType` to describe a GPGIM
structural type that is a template instantiation, such as `gpml:Array<gml:TimePeriod>`,
rather than a plain type like `gml:TimePeriod`. An uninstantiated template (the bare
`gpml:Array`) is still represented by a plain `GpgimStructuralType`; this subclass
exists only for the completed instantiation, which needs a value type in addition to
the structural type itself.

The class stores that value type in `d_value_type` and overrides
`get_instantiation_type()` to combine it with the inherited structural type into a
single `instantiation_type`. The two `create()` factories cover the two ways an
instantiation is built: from a structural type, value type and description directly,
or by instantiating an existing `GpgimStructuralType` with a value type, copying its
structural type and description across.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::GpgimTemplateStructuralType`](#gplatesmodelgpgimtemplatestructuraltype) | class | [`GpgimStructuralType`](GpgimStructuralType.md) | — | 0 | Information about a property \*template\* structural type in the GPlates Geological Information Model (GPGIM). |

## Members

### `GPlatesModel::GpgimTemplateStructuralType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpgimTemplateStructuralType>` | public | A convenience typedef for a shared pointer to a non-const GpgimTemplateStructuralType. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpgimTemplateStructuralType>` | public | A convenience typedef for a shared pointer to a const GpgimTemplateStructuralType. |
| `create( const GPlatesPropertyValues::StructuralType &structural_type, const GPlatesPropertyValues::StructuralType &value_type, const QString &description)` | method | `non_null_ptr_type` | public | Creates a GpgimTemplateStructuralType. |
| `create( const GpgimStructuralType &gpgim_structural_type, const GPlatesPropertyValues::StructuralType &value_type)` | method | `non_null_ptr_type` | public | Creates a GpgimTemplateStructuralType from a GpgimStructuralType and a value type. |
| `get_instantiation_type()` | method | `instantiation_type` | public | Returns the template's instantiation type (structural type plus value type). |
| `GpgimTemplateStructuralType( const GPlatesPropertyValues::StructuralType &structural_type, const GPlatesPropertyValues::StructuralType &value_type, const QString &description)` | constructor | `None` | protected | — |
| `GpgimTemplateStructuralType( const GpgimStructuralType &gpgim_structural_type, const GPlatesPropertyValues::StructuralType &value_type)` | constructor | `None` | protected | — |
| `d_value_type` | field | `GPlatesPropertyValues::StructuralType` | private | The value structural type. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_GPGIMTEMPLATESTRUCTURALTYPE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [model/Gpgim](Gpgim.md) | model | 10 |
| [model/ModelUtils](ModelUtils.md) | model | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/GpgimTemplateStructuralType.h
python scripts/gpq.py def GPlatesModel::GpgimTemplateStructuralType --body
python scripts/gpq.py uses GpgimTemplateStructuralType --kind class
python scripts/gpq.py hier GpgimTemplateStructuralType
```
