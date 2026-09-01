# SmartNodeLinkedList

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 127 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/SmartNodeLinkedList.h` | C++ | 405 |

## Overview

An intrusive, circular, doubly-linked list. Unlike `std::list`, the list does not
allocate its nodes: a `Node` is embedded directly in whatever object wants to be
a list member, and the node's destructor calls `splice_self_out()`, so an object
leaves every list it is in simply by being destroyed. That single property is
what the rest of the tree buys this header for — a container whose membership is
maintained by the members themselves, with no removal bookkeeping at the owner's
end and no risk of a stale entry outliving the thing it points at. The sentinel
is a by-value member of the list, so an empty list costs no heap allocation at
all, and a `Node` is fully usable on its own without a `SmartNodeLinkedList`
around it — the class only adds the sentinel, `begin()`/`end()` and `append()`.

The second reason it exists is splice semantics. An iterator here is nothing but
a `Node *`, so moving a node between lists neither invalidates iterators to other
nodes nor detaches an iterator from the node it names — it follows the node into
its new list. `GPlatesUtils::ObjectCache` says so explicitly at its
`object_seq_type` typedef: it uses this list rather than `std::list` because the
effect of `std::list::splice` on iterators is not agreed between the SGI
documentation and the standard. The two free `splice()` overloads exploit the
same property: they move a node from one list to another given only iterators or
a node reference, never the list objects, because a node does not know or need
which list it is in.

The users divide along those two lines. `GPlatesUtils::ObjectCache` and
`GPlatesUtils::IdStringSet` (whose back-reference list assumes the same owner
manages both the `Node` and the back-ref it holds) want the splice behaviour;
`GPlatesScribe::Scribe` and `GPlatesMaths::DateLineWrapper` keep lists of object
ids and polygon vertices that are cheaply re-ordered and re-spliced; the OpenGL
classes that dominate the fan-in reach it indirectly through `ObjectCache`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::SmartNodeLinkedList`](#gplatesutilssmartnodelinkedlist) | class | `boost::noncopyable` | `<typename T>` | 0 | A doubly-linked list of "smart" nodes -- that is, nodes which are able to manage themselves. |

## Members

### `GPlatesUtils::SmartNodeLinkedList`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `element_type` | typedef | `T` | public | — |
| `Node` | class | `None` | public | — |
| `NodeIterator` | class | `None` | public | Iterator over the list. 'ElementNodeQualifiedType' can be either 'element\_type' or 'const element\_type'. |
| `const_iterator` | typedef | `NodeIterator<typename boost::add_const<element_type>::type>` | public | Typedef for a const iterator. |
| `iterator` | typedef | `NodeIterator<element_type>` | public | Typedef for a non-const iterator. |
| `SmartNodeLinkedList( const element_type &null_elem_for_sentinel = element_type())` | constructor | `None` | public | Construct a new SmartNodeLinkedList, using null\_elem\_for\_sentinel as the element contained in the sentinel node. |
| `clear()` | method | `void` | public | Clears the list. |
| `empty()` | method | `bool` | public | — |
| `begin()` | method | `const_iterator` | public | — |
| `end()` | method | `const_iterator` | public | — |
| `append( Node &new_node)` | method | `void` | public | — |
| `d_sentinel` | field | `Node` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_SMARTNODELINKEDLIST_H` | macro | `None` | — |
| `splice( typename SmartNodeLinkedList<T>::iterator where_to_insert_into_destination_list, typename SmartNodeLinkedList<T>::iterator where_to_remove_from_source_list)` | function | `void` | This is equivalent to std::list::splice except there's no need to specify the list objects themselves (as only the list node objects are required). |
| `splice( typename SmartNodeLinkedList<T>::iterator where_to_insert_into_destination_list, typename SmartNodeLinkedList<T>::Node &node_to_remove_from_source_list)` | function | `void` | Same as the other overload of splice except directly referencing the node from source list. |

## Notes

- **The list owns nothing but its sentinel.** Nodes are owned by whoever embeds
  or allocates them; the list neither creates nor destroys them. Destroying a
  `SmartNodeLinkedList` destroys only `d_sentinel`, which splices the sentinel
  out and leaves the member nodes linked to each other in a headless ring.
- **`clear()` is not "empty and forget".** It splices the sentinel out and does
  nothing else, so afterwards the former members are still chained together,
  merely unreachable from this list. It is a detach, not a destruction, and the
  nodes must still be disposed of by their owners.
- **A node is never in two lists.** `splice_self_before()` unlinks first if
  `has_neighbours()`, so appending a node that is already elsewhere silently
  removes it from that other list. There is no way to ask a node which list it
  belongs to.
- **Invariant: an unlinked node points at itself.** Both `d_prev_ptr` and
  `d_next_ptr` equal `this` when the node is out of a list, which is what makes
  `splice_self_out()` a safe no-op and what `empty()` tests via the sentinel.
- **Iteration is circular, with no bounds check.** `end()` is the sentinel;
  incrementing it wraps to `begin()` and decrementing `begin()` reaches the
  sentinel again, so a loop that misses its termination condition spins forever
  rather than walking off the end.
- **Copying is deliberately partial.** The list itself is non-copyable; `Node`'s
  copy-constructor copies only the element and gives the new node no neighbours,
  and copy-assignment is declared private and left undefined. Take care with
  containers that copy their elements — the copy will not be in any list.
- **No `size()`, no thread safety.** Counting means walking, and every mutation
  is a plain pointer write with no synchronisation; two threads splicing nodes
  in the same list will corrupt it.
- **Superseded in principle.** The header's own note says that since the boost
  minimum was raised to 1.35 this should be `boost::intrusive::list` with
  `auto_unlink` hooks, which is exactly the `splice_self_out()`-in-the-destructor
  behaviour. Prefer that for new code rather than extending this class.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 172 |
| [unit-test/SmartNodeLinkedListTest](../unit-test/SmartNodeLinkedListTest.md) | unit-test | 83 |
| [maths/DateLineWrapper](../maths/DateLineWrapper.md) | maths | 77 |
| [scribe/Scribe](../scribe/Scribe.md) | scribe | 73 |
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 64 |
| [utils/SmartNodeLinkedList_test](SmartNodeLinkedList_test.md) | utils | 40 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 33 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 28 |
| [opengl/GLScalarFieldDepthLayersSource](../opengl/GLScalarFieldDepthLayersSource.md) | opengl | 27 |
| [qt-widgets/GlobeAndMapWidget](../qt-widgets/GlobeAndMapWidget.md) | qt-widgets | 27 |
| [opengl/GLFrameBufferObject](../opengl/GLFrameBufferObject.md) | opengl | 25 |
| [qt-widgets/ReconstructionViewWidget](../qt-widgets/ReconstructionViewWidget.md) | qt-widgets | 23 |
| [opengl/GLDataRasterSource](../opengl/GLDataRasterSource.md) | opengl | 21 |
| [opengl/GLProgramObject](../opengl/GLProgramObject.md) | opengl | 16 |
| [model/XmlNode](../model/XmlNode.md) | model | 13 |
| [opengl/GLTextureUtils](../opengl/GLTextureUtils.md) | opengl | 12 |
| [utils/IdStringSet](IdStringSet.md) | utils | 12 |
| [opengl/GLFilledPolygonsGlobeView](../opengl/GLFilledPolygonsGlobeView.md) | opengl | 11 |
| [opengl/GLMultiResolutionRasterMapView](../opengl/GLMultiResolutionRasterMapView.md) | opengl | 10 |
| [opengl/GLVisualRasterSource](../opengl/GLVisualRasterSource.md) | opengl | 9 |

*... and 32 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/SmartNodeLinkedList.h
python scripts/gpq.py def GPlatesUtils::SmartNodeLinkedList --body
python scripts/gpq.py uses SmartNodeLinkedList --kind class
python scripts/gpq.py hier SmartNodeLinkedList
```
