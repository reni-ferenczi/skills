# WeakObserver

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 544 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/WeakObserver.h` | C++ | 551 |

## Overview

`WeakObserver<T>` is the intrusive back-pointer that lets an object outside the model
hold on to a model handle without owning it. It is the common base of
`WeakReference` — the model's own handle-to-a-handle — and of every reconstruction
geometry that remembers which `FeatureHandle` it was produced from
(`ReconstructedFeatureGeometry`, `ResolvedTopologicalGeometry`,
`MultiPointVectorField` and the rest). It neither increments nor decrements the
publisher's reference count. Instead each observer *is* a link in a doubly-linked
list whose head and tail live in the publisher, so the publisher can find every
outstanding observer and detach them all when it dies; that is what makes a stale
`ReconstructedFeatureGeometry` report `is_valid() == false` instead of dereferencing
freed memory. The publisher half of the arrangement is `WeakObserverPublisher<H>`,
a base of `BasicHandle<HandleType>`, which keeps two independent chains — one for
`WeakObserver<H>` and one for `WeakObserver<const H>`.

The two halves are deliberately not coupled through a base class. `WeakObserver<T>`
reaches the publisher's head and tail pointers through two free functions,
`weak_observer_get_first` and `weak_observer_get_last`, resolved by
argument-dependent lookup in the publisher's own namespace, in the same style as
Boost's `intrusive_ptr_add_ref`. Any type can therefore become a publisher without
deriving from anything, as long as it supplies those two overloads;
`WeakObserverPublisher` is simply the implementation the model handles use. The
unused second parameter on both functions exists only to make the `WeakObserver<T>`
and `WeakObserver<const T>` overloads distinct, since the publisher keeps the two
chains separately.

Walking the chain is the publisher's job, not the observer's: `WeakObserverPublisher`
iterates with `next_link_ptr()` and calls the pure-virtual
`accept_weak_observer_visitor`, and that is the channel through which `BasicHandle`
delivers its modification, addition, deactivation, reactivation and
about-to-be-destroyed notifications (the visitors are in `WeakReferenceVisitors.h`).
You would touch this header only when adding a new kind of publisher or a new
observer — the latter means overriding `accept_weak_observer_visitor` and adding a
`visit_*` function to `WeakObserverVisitor`.

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

- **Nothrow is a hard requirement, not a nicety.** Every mutating operation here is
  pure pointer-splicing on built-in types: no allocation, no user code, nothing that
  can throw. The observers are the list nodes precisely so that subscribing and
  unsubscribing need no memory. `swap` is implemented naively as copy-construct plus
  two copy-assignments, which is only safe *because* all three are nothrow. If you
  add a member that allocates or a call that can throw, that reasoning collapses and
  a publisher's destructor can leave a half-spliced chain.
- **Never write your own loop over the chain.** Unsubscribing a link NULLs its own
  `next` and `prev` pointers, so a loop that reads `next_link_ptr()` *after*
  unsubscribing stops at the first element. Use `weak_observer_unsubscribe_forward`,
  which grabs the next pointer first; its Doxygen records that it was added after the
  same bug was found in several hand-rolled loops.
- **Ordering is not guaranteed.** New observers are appended at the tail, but
  copy-assignment and `swap` move links around, so notification order is arbitrary.
  Do not build behaviour on which observer is told first.
- `unsubscribe()` clears `d_publisher_ptr`; the destructor and the private
  `remove_from_subscriber_list_of_publisher` do not. That asymmetry is intentional
  (the destroyed object's pointer is never read again) but it means
  `is_subscribed()` is only meaningful on a live object.
- **Lifetime.** An observer never keeps its publisher alive. `WeakObserverPublisher`'s
  destructor unsubscribes both chains, so surviving observers see a NULL publisher
  afterwards. Note the ordering in `BasicHandle::~BasicHandle`: the
  about-to-be-destroyed notification is sent *first*, while `publisher_ptr()` is
  still non-NULL and the derived handle is already partway through destruction —
  a callback that dereferences the handle at that moment is on thin ice.
- The publisher's chain pointers are `mutable` and `first_const_weak_observer()` is
  a const member, so a const handle can still be observed; that is how
  `WeakObserver<const H>` works at all.
- The `std::swap` specialisation listed above is wrapped in `#if 0` in the header and
  is not compiled. The comment says it would be more useful on derived classes.
- `accept_weak_observer_visitor` is pure virtual, so `WeakObserver` itself is
  abstract, and the destructor is virtual only because of it.
- No synchronisation anywhere. Subscription, unsubscription and traversal must all
  happen on the same thread as the model mutation that triggers them.

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
