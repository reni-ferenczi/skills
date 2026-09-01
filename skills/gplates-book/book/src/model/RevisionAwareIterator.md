# RevisionAwareIterator

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 412 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/RevisionAwareIterator.h` | C++ | 477 |
| `src/model/RevisionAwareIterator.cc` | C++ | 41 |

## Overview

[[[PROSE overview unit=model/RevisionAwareIterator tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::RevisionAwareIteratorInternals::Traits`](#gplatesmodelrevisionawareiteratorinternalstraits) | struct | — | `<class HandleType>` | 0 | A helper traits class to differentiate between const and non-const Handles. |
| [`GPlatesModel::RevisionAwareIteratorInternals::Traits<const HandleType>`](#gplatesmodelrevisionawareiteratorinternalstraitsconst-handletype) | struct | — | `<class HandleType>` | 0 | — |
| [`GPlatesModel::RevisionAwareIterator`](#gplatesmodelrevisionawareiterator) | class | `boost::equivalent<RevisionAwareIterator<HandleType> >`<br>`boost::equality_comparable<RevisionAwareIterator<HandleType> >` | `<class HandleType>` | 0 | A revision-aware iterator to iterate over the container within a revisioning collection. |

## Members

### `GPlatesModel::RevisionAwareIteratorInternals::Traits`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value_type` | typedef | `typename HandleTraits<HandleType>::iterator_value_type` | public | — |
| `handle_weak_ref_type` | typedef | `typename HandleTraits<HandleType>::weak_ref` | public | — |

### `GPlatesModel::RevisionAwareIteratorInternals::Traits<const HandleType>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value_type` | typedef | `typename HandleTraits<HandleType>::const_iterator_value_type` | public | — |
| `handle_weak_ref_type` | typedef | `typename HandleTraits<HandleType>::const_weak_ref` | public | — |

### `GPlatesModel::RevisionAwareIterator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `handle_type` | typedef | `HandleType` | public | The type of Handle we are iterating over, e.g. |
| `this_type` | typedef | `RevisionAwareIterator<handle_type>` | public | The type of this class. |
| `revision_type` | typedef | `typename HandleTraits<handle_type>::revision_type` | public | The type of the Revision corresponding to the Handle. |
| `handle_weak_ref_type` | typedef | `typename RevisionAwareIteratorInternals::Traits<handle_type>::handle_weak_ref_type` | public | The type of a weak-ref to the Handle we're iterating over, with appropriate const-ness. |
| `index_type` | typedef | `container_size_type` | public | The type used to index the elements of the container. |
| `iterator_category` | alias | `std::bidirectional_iterator_tag` | public | Iterator typedefs. |
| `value_type` | alias | `typename RevisionAwareIteratorInternals::Traits<HandleType>::value_type` | public | Type returned by this iterator on dereference, with appropriate const-ness. |
| `difference_type` | alias | `std::ptrdiff_t` | public | — |
| `pointer` | alias | `void` | public | The 'pointer' inner type is set to void, because the dereference operator returns a temporary, and it is not desirable to take a pointer to a temporary. |
| `reference` | alias | `typename RevisionAwareIteratorInternals::Traits<HandleType>::value_type` | public | The 'reference' inner type is not a reference, because the dereference operator returns a temporary, and it is not desirable to take a reference to a temporary. |
| `RevisionAwareIterator()` | constructor | `None` | public | Default constructor. |
| `RevisionAwareIterator( handle_type &handle, index_type index_ = 0)` | constructor | `None` | public | Construct an iterator to iterate over the container inside handle, beginning at index. |
| `handle_weak_ref()` | method | `handle_weak_ref_type` | public | Return the pointer to the collection handle. |
| `index()` | method | `index_type` | public | Return the current index. |
| `operator*()` | operator | `value_type` | public | The dereference operator. |
| `operator++` | field | `RevisionAwareIterator` | public | The pre-increment operator. |
| `operator++(int)` | operator | `RevisionAwareIterator` | public | The post-increment operator. |
| `operator--` | field | `RevisionAwareIterator` | public | The pre-decrement operator. |
| `operator--(int)` | operator | `RevisionAwareIterator` | public | The post-decrement operator. |
| `is_still_valid()` | method | `bool` | public | Returns whether the underlying weak-ref to the Handle is valid, and if so whether the child of the Handle being pointed to is still in existence. |
| `current_element()` | method | `value_type` | private | Access the currently-indicated element. |
| `d_handle_weak_ref` | field | `handle_weak_ref_type` | private | A weak-ref to the Handle whose contents this Iterator iterates over. |
| `d_index` | field | `index_type` | private | This is the current index in the container. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_REVISIONAWAREITERATOR_H` | macro | `None` | — |
| `operator*()` | operator | `typename RevisionAwareIterator<HandleType>::value_type` | — |
| `operator++(int)` | operator | `RevisionAwareIterator<HandleType>` | — |
| `operator--(int)` | operator | `RevisionAwareIterator<HandleType>` | — |
| `operator<( const RevisionAwareIterator<HandleType> &lhs, const RevisionAwareIterator<HandleType> &rhs)` | operator | `bool` | — |

## Notes

[[[PROSE notes unit=model/RevisionAwareIterator tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 13 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 12 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 11 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 9 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 9 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 9 |
| [model/TopLevelPropertyRef](TopLevelPropertyRef.md) | model | 8 |
| [app-logic/LayerProxyUtils](../app-logic/LayerProxyUtils.md) | app-logic | 7 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 7 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](../app-logic/deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 7 |
| [app-logic/GeometryCookieCutter](../app-logic/GeometryCookieCutter.md) | app-logic | 5 |
| [gui/FeaturePropertyTableModel](../gui/FeaturePropertyTableModel.md) | gui | 5 |
| [gui/TopologySectionsContainer](../gui/TopologySectionsContainer.md) | gui | 5 |
| [app-logic/FlowlineGeometryPopulator](../app-logic/FlowlineGeometryPopulator.md) | app-logic | 4 |
| [app-logic/ReconstructMethodHalfStageRotation](../app-logic/ReconstructMethodHalfStageRotation.md) | app-logic | 4 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 4 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 4 |
| [gui/TopologySectionsTable](../gui/TopologySectionsTable.md) | gui | 4 |
| [qt-widgets/AgeModelManagerDialog](../qt-widgets/AgeModelManagerDialog.md) | qt-widgets | 4 |
| [app-logic/MotionPathGeometryPopulator](../app-logic/MotionPathGeometryPopulator.md) | app-logic | 3 |

*... and 34 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/RevisionAwareIterator.h
python scripts/gpq.py def GPlatesModel::RevisionAwareIterator --body
python scripts/gpq.py uses RevisionAwareIterator --kind class
python scripts/gpq.py hier RevisionAwareIterator
```
