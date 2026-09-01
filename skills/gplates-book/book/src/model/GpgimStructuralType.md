# GpgimStructuralType

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 566 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimStructuralType.h` | C++ | 237 |

## Overview

[[[PROSE overview unit=model/GpgimStructuralType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=model/GpgimStructuralType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
