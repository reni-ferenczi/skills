# BasicRevision

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 376 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/BasicRevision.h` | C++ | 495 |

## Overview

`BasicRevision<HandleType>` factors out the child-collection bookkeeping shared by
every revision class in the model — `FeatureRevision`, `FeatureCollectionRevision`
and `FeatureStoreRootRevision` are all instantiations of this template over their
respective handle types, using `HandleTraits<HandleType>` to pick up the matching
`revision_type` and `child_type`. Inheritance is used rather than delegation here
specifically to keep the Revision classes' interfaces simple, even though the
header notes that delegation would normally be preferred.

Children are stored as `boost::intrusive_ptr` in a `std::vector`
(`collection_type`), indexed by position. A removed child leaves its slot as a
null pointer rather than shrinking the vector, so `container_size()` (the number
of slots) and `size()` (the number of live children) diverge once anything has
been removed — indices handed out earlier stay valid across removals. The
protected copy constructor taking a `child_predicate_type` supports revisioning
schemes that clone only a subset of children, via the internal
`BasicRevisionInternals::ChildPredicateAdapter` which bridges a predicate over
`non_null_intrusive_ptr` to the raw `intrusive_ptr` elements actually stored.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::BasicRevisionInternals::ChildPredicateAdapter`](#gplatesmodelbasicrevisioninternalschildpredicateadapter) | class | — | `<class PredicateType, class ChildType>` | 0 | Adapter functor that wraps around a child\_predicate\_type to make it work with intrusive\_ptr not just non\_null\_intrusive\_ptr. |
| [`GPlatesModel::BasicRevision`](#gplatesmodelbasicrevision) | class | — | `<class HandleType>` | 3 | BasicRevision contains functionality common to all Revision classes. |

## Members

### `GPlatesModel::BasicRevisionInternals::ChildPredicateAdapter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `argument_type` | typedef | `boost::intrusive_ptr<const ChildType>` | public | — |
| `ChildPredicateAdapter( const PredicateType &predicate)` | constructor | `None` | public | — |
| `operator()( const boost::intrusive_ptr<const ChildType> &child_ptr)` | operator | `bool` | public | — |
| `d_predicate` | field | `PredicateType` | private | — |

### `GPlatesModel::BasicRevision`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `handle_type` | typedef | `HandleType` | public | Typedef of the template parameter. |
| `this_type` | typedef | `BasicRevision<handle_type>` | public | The type of this class. |
| `revision_type` | typedef | `typename HandleTraits<handle_type>::revision_type` | public | The revision type associated with the handle type. |
| `child_type` | typedef | `typename HandleTraits<handle_type>::child_type` | public | The type of this type's child. |
| `collection_type` | typedef | `std::vector<boost::intrusive_ptr<child_type> >` | public | The type used to represent the collection of children of this revision. |
| `non_null_ptr_type` | typedef | `typename GPlatesGlobal::PointerTraits<revision_type>::non_null_ptr_type` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<FeatureRevision\>. |
| `non_null_ptr_to_const_type` | typedef | `typename GPlatesGlobal::PointerTraits<const revision_type>::non_null_ptr_type` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const FeatureRevision\>. |
| `~BasicRevision()` | destructor | `None` | public | Destructor. |
| `container_size()` | method | `container_size_type` | public | Returns the number of children-slots currently contained within this revision. |
| `size()` | method | `container_size_type` | public | Returns the number of children currently contained within this revision. |
| `operator[]( container_size_type index)` | operator | `boost::intrusive_ptr<const child_type>` | public | Accesses the child at index in the collection. |
| `get( container_size_type index)` | method | `boost::intrusive_ptr<const child_type>` | public | Accesses the child at index in the collection. |
| `has_element_at( container_size_type index)` | method | `bool` | public | Returns true if there is an element at position index in the underlying container. |
| `add( typename GPlatesGlobal::PointerTraits<child_type>::non_null_ptr_type new_child)` | method | `container_size_type` | public | Adds new\_child to the collection. |
| `remove( container_size_type index)` | method | `boost::intrusive_ptr<child_type>` | public | Removes and returns the child at index in the collection. |
| `set( container_size_type index, typename GPlatesGlobal::PointerTraits<child_type>::non_null_ptr_type new_child)` | method | `void` | public | Changes a child at a particular index into new\_child. |
| `child_predicate_type` | typedef | `boost::function<bool (const typename GPlatesGlobal::PointerTraits<const child_type>::non_null_ptr_type &)>` | protected | Typedef for a function that accepts a pointer to a child\_type and returns a boolean. |
| `BasicRevision()` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `BasicRevision( const this_type &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to be allow instantiation of this type on the stack. |
| `BasicRevision( const this_type &other, const child_predicate_type &clone_children_predicate)` | constructor | `None` | protected | This constructor should not be public, because we don't want to be allow instantiation of this type on the stack. |
| `operator=` | field | `this_type` | private | This should not be defined, because we don't want to be able to copy one of these objects. |
| `d_children` | field | `collection_type` | private | The collection of children possessed by this Revision. |
| `d_num_children` | field | `container_size_type` | private | The number of current children (i.e. the number of non-null slots in d\_children). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_BASICREVISION_H` | macro | `None` | — |
| `operator[]( container_size_type index)` | operator | `boost::intrusive_ptr<const typename BasicRevision<HandleType>::child_type>` | — |

## Notes

- All three constructors are protected and `operator=` is private and undefined:
  `BasicRevision` is meant to be instantiated only through a derived Revision
  class, never as a standalone object or copied via assignment.
- `remove()` and `set()` on an empty slot both adjust `d_num_children`, so callers
  do not need to track live-vs-empty counts themselves; `has_element_at()` is the
  correct way to distinguish a real child from a removed one at a given index.
- Indices from `add()` remain valid for the lifetime of the revision even after
  other children are removed, since removal nulls the slot instead of erasing it.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/FeatureRevision](FeatureRevision.md) | model | 19 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 10 |
| [model/RevisionAwareIterator](RevisionAwareIterator.md) | model | 7 |
| [model/FeatureCollectionRevision](FeatureCollectionRevision.md) | model | 5 |
| [model/FeatureStoreRootRevision](FeatureStoreRootRevision.md) | model | 5 |
| [qt-widgets/AssignReconstructionPlateIdsDialog](../qt-widgets/AssignReconstructionPlateIdsDialog.md) | qt-widgets | 4 |
| [model/ModelUtils](ModelUtils.md) | model | 2 |
| [qt-widgets/VisualLayersComboBox](../qt-widgets/VisualLayersComboBox.md) | qt-widgets | 2 |
| [model/TopLevelPropertyRef](TopLevelPropertyRef.md) | model | 1 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](../qt-widgets/CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 1 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/BasicRevision.h
python scripts/gpq.py def GPlatesModel::BasicRevision --body
python scripts/gpq.py uses BasicRevision --kind class
python scripts/gpq.py hier BasicRevision
```
