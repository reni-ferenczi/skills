# IntrusiveSinglyLinkedList

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 837 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/IntrusiveSinglyLinkedList.h` | C++ | 348 |

## Overview

[[[PROSE overview unit=utils/IntrusiveSinglyLinkedList tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/IntrusiveSinglyLinkedList tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
