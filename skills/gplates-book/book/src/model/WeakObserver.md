# WeakObserver

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 544 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakObserver.h` | C++ | 551 |

## Overview

[[[PROSE overview unit=model/WeakObserver tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::WeakObserver`](#gplatesmodelweakobserver) | class | — | `<typename T>` | 16 | function mimics the functions intrusive\_ptr\_add\_ref and intrusive\_ptr\_release of the Boost intrusive\_ptr smart pointer. @par Substituting T for the actual publisher type, the functions should have the prototypes: @code inline ... |

## Members

### `GPlatesModel::WeakObserver`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `WeakObserver<T>` | public | This is a convenience typedef for this type. |
| `publisher_type` | typedef | `T` | public | This is the type of the publisher. |
| `WeakObserver()` | constructor | `None` | public | Default constructor. |
| `WeakObserver( publisher_type &publisher_)` | constructor | `None` | public | Constructor (note: not a copy-constructor). |
| `WeakObserver( const this_type &other)` | constructor | `None` | public | Copy-constructor. |
| `~WeakObserver()` | destructor | `None` | public | Virtual destructor. |
| `is_subscribed()` | method | `bool` | public | Return whether this WeakObserver instance is subscribed to a publisher. |
| `publisher_ptr()` | method | `publisher_type` | public | Return a pointer to the publisher-type. |
| `next_link_ptr()` | method | `this_type` | public | Return a pointer to the "next" weak observer instance in the chain. |
| `subscribe( publisher_type &publisher_)` | method | `void` | public | Subscribe this WeakObserver instance to publisher publisher\_. |
| `unsubscribe()` | method | `void` | public | Unsubscribe this WeakObserver instance from the publisher to which it is subscribed (if any). |
| `accept_weak_observer_visitor( WeakObserverVisitor<T> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `operator=` | field | `WeakObserver<T>` | protected | Copy-assign the value of other to this instance. |
| `swap( this_type &other)` | method | `void` | protected | Swap the value of this instance with the value of other. |
| `remove_from_subscriber_list_of_publisher( publisher_type &publisher_)` | method | `void` | protected | Remove this WeakObserver from the list of subscribers to the publisher. |
| `d_publisher_ptr` | field | `publisher_type` | private | If non-NULL, this points to the publisher instance to which this WeakObserver instance is subscribed. |
| `d_prev_link_ptr` | field | `this_type` | private | This points to the previous link in the doubly-linked list of weak observers of a particular publisher instance. |
| `d_next_link_ptr` | field | `this_type` | private | This points to the next link in the doubly-linked list of weak observers of a particular publisher instance. |
| `subscribe_to_publisher_unknown_whether_other_subscribers( publisher_type &publisher_)` | method | `void` | private | Subscribe this weak observer to publisher\_. |
| `subscribe_to_same_publisher_as_other_observer( const this_type &other)` | method | `void` | private | Subscribe this weak observer to the publisher to which other is subscribed. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_WEAKOBSERVER_H` | macro | `None` | — |
| `weak_observer_unsubscribe_forward( WeakObserverType *curr)` | function | `void` | Unsubscribe all weak observers from curr onwards (inclusive). |
| `swap( GPlatesModel::WeakObserver<T> &w1, GPlatesModel::WeakObserver<T> &w2)` | function | `void` | This is a template specialisation of the standard function swap. |

## Notes

[[[PROSE notes unit=model/WeakObserver tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyGeometryResolverLayerProxy](../app-logic/TopologyGeometryResolverLayerProxy.md) | app-logic | 103 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 102 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 92 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 88 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 88 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 74 |
| [opengl/GLRasterCoRegistration](../opengl/GLRasterCoRegistration.md) | opengl | 65 |
| [app-logic/TopologyNetworkResolverLayerProxy](../app-logic/TopologyNetworkResolverLayerProxy.md) | app-logic | 59 |
| [api/CoReg](../api/CoReg.md) | api | 57 |
| [app-logic/ReconstructScalarCoverageLayerProxy](../app-logic/ReconstructScalarCoverageLayerProxy.md) | app-logic | 43 |
| [app-logic/LayerProxyUtils](../app-logic/LayerProxyUtils.md) | app-logic | 42 |
| [model/ModelUtils](ModelUtils.md) | model | 40 |
| [app-logic/GeometryCookieCutter](../app-logic/GeometryCookieCutter.md) | app-logic | 39 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 39 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 39 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 37 |
| [app-logic/ReconstructUtils](../app-logic/ReconstructUtils.md) | app-logic | 36 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 35 |
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 34 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 34 |

*... and 216 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/WeakObserver.h
python scripts/gpq.py def GPlatesModel::WeakObserver --body
python scripts/gpq.py uses WeakObserver --kind class
python scripts/gpq.py hier WeakObserver
```
