# GpgimEnumerationType

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1409 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimEnumerationType.h` | C++ | 128 |

## Overview

[[[PROSE overview unit=model/GpgimEnumerationType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::GpgimEnumerationType`](#gplatesmodelgpgimenumerationtype) | class | [`GpgimStructuralType`](GpgimStructuralType.md) | — | 0 | Information about a property enumeration (structural) type in the GPlates Geological Information Model (GPGIM). |

## Members

### `GPlatesModel::GpgimEnumerationType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpgimEnumerationType>` | public | A convenience typedef for a shared pointer to a non-const GpgimEnumerationType. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpgimEnumerationType>` | public | A convenience typedef for a shared pointer to a const GpgimEnumerationType. |
| `Content` | struct | `None` | public | A content of this enumeration containing allowed enumeration value and a description of that value. |
| `content_seq_type` | typedef | `std::vector<Content>` | public | Typdef for a sequence of Content objects. |
| `create( const GPlatesPropertyValues::StructuralType &structural_type, const QString &description, ContentForwardIter contents_begin, ContentForwardIter contents_end)` | method | `non_null_ptr_type` | public | Creates a GpgimEnumerationType. |
| `d_contents` | field | `content_seq_type` | private | The allowed content of this enumeration type. |
| `GpgimEnumerationType( const GPlatesPropertyValues::StructuralType &structural_type, const QString &description, ContentForwardIter contents_begin, ContentForwardIter contents_end)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_GPGIMENUMERATIONTYPE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/GpgimEnumerationType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/Gpgim](Gpgim.md) | model | 24 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 17 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 15 |
| [qt-widgets/EditEnumerationWidget](../qt-widgets/EditEnumerationWidget.md) | qt-widgets | 9 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 5 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 4 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 3 |
| [model/ModelUtils](ModelUtils.md) | model | 3 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 3 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 2 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 2 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/GpgimEnumerationType.h
python scripts/gpq.py def GPlatesModel::GpgimEnumerationType --body
python scripts/gpq.py uses GpgimEnumerationType --kind class
python scripts/gpq.py hier GpgimEnumerationType
```
