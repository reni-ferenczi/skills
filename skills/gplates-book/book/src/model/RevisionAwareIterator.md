# RevisionAwareIterator

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 412 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/RevisionAwareIterator.h` | C++ | 477 |
| `src/model/RevisionAwareIterator.cc` | C++ | 41 |

## Overview

One iterator template serves all three levels of the feature store:
`FeatureStoreRootHandle` over its feature collections, `FeatureCollectionHandle` over its
features, and `FeatureHandle` over its top-level properties. `HandleTraits` supplies the
per-level revision type, weak-ref type and dereference type, and the
`RevisionAwareIteratorInternals::Traits` pair selects the const or non-const flavour, so
`RevisionAwareIterator<const FeatureHandle>` *is* `FeatureHandle::const_iterator` and a
non-const iterator converts implicitly to it. `BasicHandle::begin()` and `end()` hand these
out; nothing else constructs them directly.

The design point is what the iterator does *not* hold. It stores a `WeakReference` to the
handle and an integer index — never a pointer into the container — and re-reads
`handle->current_revision()` on every dereference, increment and decrement. That is the
"revision awareness": an iterator can never be left addressing a superseded revision, and
the index stays meaningful across edits because `BasicRevision::remove()` sets the child
slot to NULL instead of erasing it, so no other element ever shifts. The constructor and
`operator++` step over those NULL slots, so ordinary forward iteration never yields a hole
even in a container that has had children deleted.

Dereferencing a `FeatureHandle` iterator is the one special case, and it is why the `.cc`
file exists: a template specialisation of `current_element()` returns a
`TopLevelPropertyRef` proxy instead of a pointer. Assigning through that proxy routes into
`FeatureHandle::set`, which deep-clones the incoming property, bumps the revision id and
fires the modification notifications and `ChangesetHandle` bookkeeping. Without the proxy,
`*iter = property` would silently bypass all of it. The other two levels dereference to
plain `non_null_intrusive_ptr`s, as do const `FeatureHandle` iterators.

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

- **Nothing is checked for you.** `operator*`, `operator++`, `operator--` and the
  constructor all dereference `d_handle_weak_ref` unguarded. If the handle has been
  destroyed or deactivated you get undefined behaviour, not an exception. `is_still_valid()`
  is the explicit guard, checking both the weak-ref and that the child at the index still
  exists — call it when you have *held* an iterator across model edits. The header's advice
  not to call it during a plain iteration is about cost, not safety: forward iteration
  already skips NULL slots.
- **A default-constructed iterator is inert, not empty.** Its weak-ref is null and
  `d_index` is `INVALID_INDEX`, which is `container_size_type(-1)` — an unsigned `size_t`,
  so `SIZE_MAX`, not a negative number. It is not comparable to a real `end()` and must not
  be dereferenced or incremented.
- **Do not decrement `begin()`.** `operator--` pre-decrements before testing and only
  special-cases *arriving* at index 0. Decrementing from index 0 wraps the unsigned index to
  `SIZE_MAX` and then spins downwards; it does not terminate in any useful time.
- **`end()` is `container_size()`, not `size()`.** The revision keeps NULLed slots, so the
  number of slots exceeds the number of live children whenever anything has been removed.
  Do not compute an end iterator from `size()`, and do not treat the index as a position in
  a dense sequence.
- **Out-of-range construction is silently clamped.** The constructor caps `index_` at
  `container_size()`, so an oversized index yields `end()` rather than an error.
- **Ordering is only meaningful within one container.** `operator<` compares indices when
  both iterators reference the same handle and otherwise compares the weak-refs, i.e. the
  raw handle addresses. `boost::equivalent` then derives `operator==` from that ordering,
  so equality carries the same caveat.
- **The revision is never actually swapped in this version.**
  `BasicHandle::d_current_revision` is assigned only in the constructor and nowhere else;
  edits mutate the current revision in place and call `FeatureRevision::update_revision_id()`,
  whose declaration carries the FIXME "Remove this function once we actually create a new
  revision object when we modify a feature." So the per-operation re-read of
  `current_revision()` costs an indirection today without ever observing a change, and an
  iterator does **not** pin the state it was created against. Treat the revision-awareness
  as the scaffolding for the unfinished transaction/bubble-up scheme, and rely instead on
  the NULL-slot invariant for index stability.

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
