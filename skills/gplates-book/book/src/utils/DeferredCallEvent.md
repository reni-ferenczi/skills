# DeferredCallEvent

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 606 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/DeferredCallEvent.h` | C++ | 332 |
| `src/utils/DeferredCallEvent.cc` | C++ | 73 |

## Overview

This header lets code running on a background thread — most notably the
embedded Python interpreter driven by `PythonExecutionThread` — get a piece of
work executed on the Qt GUI thread, since Qt widgets and much of the
application state may only be touched there. Each concrete class wraps a
`boost::function<...>` callable as a `QEvent` (`AbstractDeferredCallEvent::TYPE`
is a custom event type registered once via `QEvent::registerEventType()`);
posting the event with `QApplication::postEvent(qApp, ...)` gets it delivered
and `execute()`d inside the GUI thread's event loop. `DeferredCallEvent` is
fire-and-forget; `BlockingDeferredCallEvent` and the templated
`DeferredCallWithResultEvent<ResultType>` additionally hold a `QMutex` and
`QWaitCondition` so the posting thread can block until `execute()` has run on
the GUI thread, and in the result-returning case retrieve the call's return
value afterwards.

`DeferCall<ResultType>::defer_call()` (and its `DeferCall<void>`
specialisation) is the entry point callers actually use: it checks whether it
is already running on the GUI thread — via `QThread::currentThread() ==
qApp->thread()` — and if so calls `deferred_call` directly rather than
posting an event at all, avoiding an unnecessary round trip and the risk of a
thread waiting on itself. The `DeferredCallWithResultEventInternals::traits`
machinery exists solely to let `ResultType` be a reference: since a
`boost::optional<ResultType&>` isn't meaningful the way a value type is, the
`traits_helper` partial specialisation stores a pointer instead when
`boost::is_reference<ResultType>::value` is true.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::AbstractDeferredCallEvent`](#gplatesutilsabstractdeferredcallevent) | class | `QEvent` | — | 3 | — |
| [`GPlatesUtils::DeferredCallEvent`](#gplatesutilsdeferredcallevent) | class | [`AbstractDeferredCallEvent`](DeferredCallEvent.md) | — | 0 | DeferredCallEvent is useful if you don't want to process something right now but you want to put it onto the event queue for later processing. |
| [`GPlatesUtils::BlockingDeferredCallEvent`](#gplatesutilsblockingdeferredcallevent) | class | [`AbstractDeferredCallEvent`](DeferredCallEvent.md) | — | 0 | This version provides facilities for blocking the calling thread until the execution has finished on the target thread. |
| [`GPlatesUtils::DeferredCallWithResultEventInternals::traits_helper`](#gplatesutilsdeferredcallwithresulteventinternalstraits_helper) | struct | — | `<typename ResultType, bool IsReference /* = false */>` | 0 | — |
| [`GPlatesUtils::DeferredCallWithResultEventInternals::traits_helper<ResultType, true>`](#gplatesutilsdeferredcallwithresulteventinternalstraits_helperresulttype-true) | struct | — | `<typename ResultType>` | 0 | — |
| [`GPlatesUtils::DeferredCallWithResultEventInternals::traits`](#gplatesutilsdeferredcallwithresulteventinternalstraits) | struct | — | `<typename ResultType>` | 0 | — |
| [`GPlatesUtils::DeferredCallWithResultEvent`](#gplatesutilsdeferredcallwithresultevent) | class | [`AbstractDeferredCallEvent`](DeferredCallEvent.md) | `<typename ResultType>` | 0 | The same idea as DeferredCallEvent above but this has facilities for returning the return value from the function call. |
| [`GPlatesUtils::DeferCall`](#gplatesutilsdefercall) | struct | — | `<typename ResultType = void>` | 0 | — |
| [`GPlatesUtils::DeferCall<void>`](#gplatesutilsdefercallvoid) | struct | — | `<>` | 0 | — |

## Members

### `GPlatesUtils::AbstractDeferredCallEvent`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TYPE` | field | `QEvent::Type` | public | — |
| `AbstractDeferredCallEvent()` | constructor | `None` | public | — |
| `execute()` | method | `void` | public | — |

### `GPlatesUtils::DeferredCallEvent`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `deferred_call_type` | typedef | `boost::function< void () >` | public | — |
| `DeferredCallEvent( const deferred_call_type &deferred_call)` | constructor | `None` | public | Constructs a DeferredCallEvent with the given deferred\_call. |
| `execute()` | method | `void` | public | Executes the stored deferred call. |
| `d_deferred_call` | field | `deferred_call_type` | private | — |

### `GPlatesUtils::BlockingDeferredCallEvent`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `deferred_call_type` | typedef | `DeferredCallEvent::deferred_call_type` | public | — |
| `BlockingDeferredCallEvent( const deferred_call_type &deferred_call, QMutex &mutex, QWaitCondition &condition)` | constructor | `None` | public | — |
| `execute()` | method | `void` | public | — |
| `d_deferred_call` | field | `deferred_call_type` | private | — |
| `d_mutex` | field | `QMutex` | private | — |
| `d_condition` | field | `QWaitCondition` | private | — |

### `GPlatesUtils::DeferredCallWithResultEventInternals::traits_helper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `storage_type` | typedef | `boost::optional<typename boost::remove_const<ResultType>::type>` | public | — |
| `result_to_storage( ResultType result)` | method | `storage_type` | public | — |

### `GPlatesUtils::DeferredCallWithResultEventInternals::traits_helper<ResultType, true>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `storage_type` | typedef | `typename boost::add_pointer<ResultType>::type` | public | — |
| `result_to_storage( ResultType result)` | method | `storage_type` | public | — |

### `GPlatesUtils::DeferredCallWithResultEventInternals::traits`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `storage_type` | typedef | `typename traits_helper< ResultType, boost::is_reference<ResultType>::value >::storage_type` | public | — |
| `result_to_storage( ResultType result)` | method | `storage_type` | public | — |

### `GPlatesUtils::DeferredCallWithResultEvent`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `deferred_call_type` | typedef | `boost::function< ResultType () >` | public | — |
| `storage_type` | typedef | `typename DeferredCallWithResultEventInternals::traits<ResultType>::storage_type` | public | — |
| `DeferredCallWithResultEvent( const deferred_call_type &deferred_call, QMutex &mutex, QWaitCondition &condition, storage_type &result)` | constructor | `None` | public | — |
| `execute()` | method | `void` | public | — |
| `d_deferred_call` | field | `deferred_call_type` | private | — |
| `d_mutex` | field | `QMutex` | private | — |
| `d_condition` | field | `QWaitCondition` | private | — |
| `d_result` | field | `storage_type` | private | — |

### `GPlatesUtils::DeferCall`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `defer_call( const typename DeferredCallWithResultEvent<ResultType>::deferred_call_type &deferred_call, bool blocking = false)` | method | `ResultType` | public | If called from a thread other than the GUI thread: Constructs a DeferredCallEvent with the given deferred\_call and posts it to the QApplication instance living in the main GUI thread. |

### `GPlatesUtils::DeferCall<void>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `defer_call( const DeferredCallEvent::deferred_call_type &deferred_call, bool blocking = false)` | method | `void` | public | If called from a thread other than the GUI thread: Constructs a DeferredCallEvent with the given deferred\_call and posts it to the QApplication instance living in the main GUI thread. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `TYPE` | variable | `QEvent::Type` | — |
| `GPLATES_UTILS_DEFERREDCALLEVENT_H` | macro | `None` | — |

## Notes

- If `deferred_call()` throws inside `BlockingDeferredCallEvent::execute()`
  (or the `DeferredCallWithResultEvent` equivalent), the mutex is never
  locked and `condition.wakeAll()` is never called, so the thread blocked in
  `defer_call()` waits forever. The source comment flags this directly: the
  called function is assumed not to throw.
- These classes only make sense for dispatching to the GUI thread: `defer_call()`
  is documented as unsuitable for running work on an arbitrary other thread —
  for that, construct and post an `AbstractDeferredCallEvent` subclass
  directly, with the receiver's `event()` handler living on the target
  thread.
- `QApplication::postEvent()` takes ownership of the heap-allocated event
  object; callers must not also delete it after posting.
- `DeferCall<ResultType>::defer_call()`'s `blocking` parameter is always
  ignored (it always blocks); only `DeferCall<void>::defer_call()` honours
  it, since a non-blocking call has no way to return a result at all.

## Used by

| Unit | Component | References |
|---|---|---|
| [api/DeferredApiCallImpl](../api/DeferredApiCallImpl.md) | api | 49 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 7 |
| [api/PythonRunner](../api/PythonRunner.md) | api | 6 |
| [gui/GPlatesQApplication](../gui/GPlatesQApplication.md) | gui | 5 |
| [api/PythonExecutionMonitor](../api/PythonExecutionMonitor.md) | api | 1 |
| [api/PythonExecutionThread](../api/PythonExecutionThread.md) | api | 1 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/DeferredCallEvent.h
python scripts/gpq.py def GPlatesUtils::DeferCall --body
python scripts/gpq.py uses DeferCall --kind struct
python scripts/gpq.py hier DeferCall
```
