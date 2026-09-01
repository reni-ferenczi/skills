# TopLevelPropertyRef

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 572 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/TopLevelPropertyRef.h` | C++ | 145 |
| `src/model/TopLevelPropertyRef.cc` | C++ | 105 |

## Overview

[[[PROSE overview unit=model/TopLevelPropertyRef tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::TopLevelPropertyRef`](#gplatesmodeltoplevelpropertyref) | class | [`GPlatesUtils::SafeBool<TopLevelPropertyRef>`](../utils/SafeBool.md) | — | 0 | Example usage: FeatureHandle::weak\_ref feature = ...; FeatureHandle::children\_iterator iter = feature-\>children\_begin(); TopLevelProperty::non\_null\_ptr\_to\_const\_type tlp = \*iter; // \*iter returns TopLevelPropertyRef, which can be converted ... |

## Members

### `GPlatesModel::TopLevelPropertyRef`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TopLevelPropertyRef( const HandleTraits<FeatureHandle>::iterator &iterator)` | constructor | `None` | public | — |
| `TopLevelPropertyRef( const TopLevelPropertyRef &other)` | constructor | `None` | public | — |
| `~TopLevelPropertyRef()` | destructor | `None` | public | — |
| `operator->()` | operator | `TopLevelProperty` | public | Undefined behaviour if index is invalid. |
| `get()` | method | `TopLevelProperty` | public | The same as operator-\>(). |
| `operator*` | field | `TopLevelProperty` | public | Undefined behaviour if index is invalid. |
| `operator=( GPlatesGlobal::PointerTraits<const TopLevelProperty>::non_null_ptr_type new_property)` | operator | `void` | public | Allows the TopLevelProperty to be changed. |
| `boolean_test()` | method | `bool` | public | operator bool() provided by SafeBool. |
| `pointer()` | method | `GPlatesGlobal::PointerTraits<const TopLevelProperty>::non_null_ptr_type` | private | Gets a pointer to the TopLevelProperty from the iterator. |
| `d_feature_ref` | field | `WeakReference<FeatureHandle>` | private | The feature that contains the TopLevelProperty of interest. |
| `d_index` | field | `container_size_type` | private | The index of the TopLevelProperty inside its parent feature. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator->()` | operator | `GPlatesModel::TopLevelProperty` | — |
| `operator=( GPlatesGlobal::PointerTraits<const TopLevelProperty>::non_null_ptr_type new_property)` | operator | `void` | — |
| `GPLATES_MODEL_TOPLEVELPROPERTYREF_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/TopLevelPropertyRef tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ChangeFeatureTypeDialog](../qt-widgets/ChangeFeatureTypeDialog.md) | qt-widgets | 10 |
| [qt-widgets/FeaturePropertiesDialog](../qt-widgets/FeaturePropertiesDialog.md) | qt-widgets | 8 |
| [qt-widgets/ChangePropertyWidget](../qt-widgets/ChangePropertyWidget.md) | qt-widgets | 5 |
| [qt-widgets/AddPropertyDialog](../qt-widgets/AddPropertyDialog.md) | qt-widgets | 4 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 3 |
| [model/RevisionAwareIterator](RevisionAwareIterator.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/TopLevelPropertyRef.h
python scripts/gpq.py def GPlatesModel::TopLevelPropertyRef --body
python scripts/gpq.py uses TopLevelPropertyRef --kind class
python scripts/gpq.py hier TopLevelPropertyRef
```
