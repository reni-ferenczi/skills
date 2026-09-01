# GpgimEnumerationType

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1409 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimEnumerationType.h` | C++ | 128 |

## Overview

`GpgimEnumerationType` extends `GpgimStructuralType` with the extra data an
enumeration structural type needs: the set of allowed enumeration values,
each paired with its own description in a `Content` struct. Where
`GpgimStructuralType` alone is enough to describe a plain structural type such
as `gml:Point`, an enumeration type (e.g. a `gpml:` enumeration property) also
has to enumerate and document its legal values, and `d_contents` is that list.

Like its base class it is created only through `create()`, which forwards a
`ContentForwardIter` range into `d_contents` — callers pass begin/end iterators
over whatever container holds the enumeration's `Content` values rather than a
fixed container type. Readers such as `GpmlOutputVisitor` and the property-edit
widgets (`EditEnumerationWidget`, `CreateFeatureDialog`) use `get_contents()` to
populate combo boxes and to validate a property's value against the GPGIM.

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

*None.*

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
