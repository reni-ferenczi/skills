# SmartNodeLinkedList

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 127 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/SmartNodeLinkedList.h` | C++ | 405 |

## Overview

[[[PROSE overview unit=utils/SmartNodeLinkedList tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/SmartNodeLinkedList tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
