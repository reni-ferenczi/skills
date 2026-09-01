# FeatureWeakRefSequence

[Book TOC](../../../TOC.md) · [gui](../../../components/gui.md) · cluster Community 1080 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/deprecated/FeatureWeakRefSequence.h` | C++ | 163 |

## Overview

[[[PROSE overview unit=gui/deprecated/FeatureWeakRefSequence tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::FeatureWeakRefSequence`](#gplatesguifeatureweakrefsequence) | class | `QObject`<br>[`GPlatesUtils::ReferenceCount<FeatureWeakRefSequence>`](../../utils/ReferenceCount.md) | — | 0 | This class is used for a sequence of feature weak-refs in the GUI. |

## Members

### `GPlatesGui::FeatureWeakRefSequence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<FeatureWeakRefSequence, GPlatesUtils::NullIntrusivePointerHandler>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<FeatureWeakRefSequence, GPlatesUtils::NullIntrusivePointerHandler\>. |
| `sequence_type` | typedef | `std::vector<GPlatesModel::FeatureHandle::weak_ref>` | public | The type used to contain the sequence of feature weak-refs. |
| `size_type` | typedef | `sequence_type::size_type` | public | The type used for the size of the sequence of feature weak-refs. |
| `const_iterator` | typedef | `sequence_type::const_iterator` | public | The type used to const-iterate over the sequence of feature weak-refs. |
| `~FeatureWeakRefSequence()` | destructor | `None` | public | — |
| `create()` | method | `non_null_ptr_type` | public | Create a new FeatureWeakRefSequence instance. |
| `size()` | method | `size_type` | public | — |
| `begin()` | method | `const_iterator` | public | — |
| `end()` | method | `const_iterator` | public | — |
| `at(size_type index)` | method | `GPlatesModel::FeatureHandle::weak_ref` | public | — |
| `clear()` | method | `void` | public | — |
| `push_back( const GPlatesModel::FeatureHandle::weak_ref &new_elem)` | method | `void` | public | — |
| `d_sequence` | field | `sequence_type` | private | The sequence of feature weak-refs. |
| `FeatureWeakRefSequence()` | constructor | `None` | private | Construct a FeatureWeakRefSequence instance. |
| `FeatureWeakRefSequence( const FeatureWeakRefSequence &)` | constructor | `None` | private | This constructor should never be defined, because we don't want/need to allow copy-construction. |
| `operator=` | field | `FeatureWeakRefSequence` | private | This operator should never be defined, because we don't want/need to allow copy-assignment. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_FEATUREWEAKREFSEQUENCE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/deprecated/FeatureWeakRefSequence tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/deprecated/FeatureWeakRefSequence.h
python scripts/gpq.py def GPlatesGui::FeatureWeakRefSequence --body
python scripts/gpq.py uses FeatureWeakRefSequence --kind class
python scripts/gpq.py hier FeatureWeakRefSequence
```
