# IntrusiveSinglyLinkedList

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 837 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/IntrusiveSinglyLinkedList.h` | C++ | 348 |

## Overview

`IntrusiveSinglyLinkedList` is a low-level linked list for cases where a
`std::list` is too heavy: an element becomes part of the list by inheriting
publicly from `IntrusiveSinglyLinkedList<ElementNodeType>::Node`, which adds
only a single `mutable` next-pointer, and the list itself stores nothing but
a head pointer. Because the "next" pointer lives inside the element rather
than in a separate node allocation, the list never allocates — `push_front`
and `pop_front` just relink an existing object, and the client retains
ownership and is responsible for the elements' memory throughout.

Copying or assigning a list does not copy elements: both copies share
(tail-share) the same underlying chain, which the header calls out as a
deliberate feature for traversing directed-acyclic-graph structures, where
each node's list of ancestors can share a common tail with its siblings'
lists instead of duplicating it. An `ElementNodeType` that must belong to
more than one such list at once inherits from `Node` multiple times, once
per list, disambiguated with a distinct `NodeTag` type parameter for each —
`push_front`, `pop_front` and the iterator's increment all use a
tag-qualified `tagged_base_node_type` typedef to pick the right base when an
element has more than one `Node` base.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::IntrusiveSinglyLinkedList`](#gplatesutilsintrusivesinglylinkedlist) | class | — | `<class ElementNodeType, class NodeTag = void>` | 0 | Template parameter ElementNodeType must inherit publicly from IntrusiveSinglyLinkedList\<ElementNodeType\>::Node. |

## Members

### `GPlatesUtils::IntrusiveSinglyLinkedList`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Node` | class | `None` | public | The template parameter ElementNodeType must inherit publicly from this class. |
| `Iterator` | class | `None` | public | Iterator over the list. 'ElementNodeQualifiedType' can be either 'ElementNodeType' or 'const ElementNodeType'. |
| `iterator` | typedef | `Iterator<ElementNodeType>` | public | Typedef for iterator. |
| `const_iterator` | typedef | `Iterator< typename boost::add_const<ElementNodeType>::type >` | public | Typedef for const iterator. |
| `IntrusiveSinglyLinkedList()` | constructor | `None` | public | — |
| `IntrusiveSinglyLinkedList( const IntrusiveSinglyLinkedList &other_list)` | constructor | `None` | public | Copy constructor. |
| `clear()` | method | `void` | public | Clears the list. |
| `empty()` | method | `bool` | public | — |
| `push_front( ElementNodeType *const node)` | method | `void` | public | Adds the specified element to the front of the list. |
| `pop_front()` | method | `void` | public | Removes the element at the front of the list. |
| `begin()` | method | `iterator` | public | — |
| `end()` | method | `iterator` | public | — |
| `d_list` | field | `ElementNodeType` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_INTRUSIVESINGLYLINKEDLIST_H` | macro | `None` | — |

## Notes

Calling `front()`, `pop_front()` or dereferencing/incrementing `end()` on an
empty list is undefined behaviour (a likely crash) — the class does no bounds
checking. `clear()` and `pop_front()` only detach elements; they never
destroy or free them, since the client owns the elements' memory. The header
itself notes that now the project's minimum Boost version is 1.35 or higher,
`boost::intrusive::slist` should be used instead of this class for new code.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/Profile](Profile.md) | utils | 57 |
| [opengl/GLStateSetStore](../opengl/GLStateSetStore.md) | opengl | 47 |
| [scribe/ScribeVoidCastRegistry](../scribe/ScribeVoidCastRegistry.md) | scribe | 42 |
| [utils/LatLonAreaSampling](LatLonAreaSampling.md) | utils | 40 |
| [scribe/TranscribeStd](../scribe/TranscribeStd.md) | scribe | 33 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 26 |
| [utils/ObjectCache](ObjectCache.md) | utils | 16 |
| [scribe/TranscribeQt](../scribe/TranscribeQt.md) | scribe | 15 |
| [utils/ObjectPool](ObjectPool.md) | utils | 9 |
| [scribe/Scribe](../scribe/Scribe.md) | scribe | 7 |
| [scribe/TranscribeSequenceProtocol](../scribe/TranscribeSequenceProtocol.md) | scribe | 7 |
| [maths/CubeQuadTreePartitionUtils](../maths/CubeQuadTreePartitionUtils.md) | maths | 6 |
| [opengl/GLFilledPolygonsGlobeView](../opengl/GLFilledPolygonsGlobeView.md) | opengl | 6 |
| [app-logic/ReconstructionGraphBuilder](../app-logic/ReconstructionGraphBuilder.md) | app-logic | 4 |
| [maths/CubeQuadTreePartition](../maths/CubeQuadTreePartition.md) | maths | 4 |
| [opengl/GLVertexArrayObject](../opengl/GLVertexArrayObject.md) | opengl | 4 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 4 |
| [maths/CubeQuadTree](../maths/CubeQuadTree.md) | maths | 2 |
| [opengl/GLStateSets](../opengl/GLStateSets.md) | opengl | 2 |
| [scribe/TranscribeBoost](../scribe/TranscribeBoost.md) | scribe | 2 |

*... and 8 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/IntrusiveSinglyLinkedList.h
python scripts/gpq.py def GPlatesUtils::IntrusiveSinglyLinkedList --body
python scripts/gpq.py uses IntrusiveSinglyLinkedList --kind class
python scripts/gpq.py hier IntrusiveSinglyLinkedList
```
