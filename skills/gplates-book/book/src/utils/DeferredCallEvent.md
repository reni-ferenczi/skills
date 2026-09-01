# DeferredCallEvent

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 606 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/DeferredCallEvent.h` | C++ | 332 |
| `src/utils/DeferredCallEvent.cc` | C++ | 73 |

## Overview

[[[PROSE overview unit=utils/DeferredCallEvent tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/DeferredCallEvent tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
