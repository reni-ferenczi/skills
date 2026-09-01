# DeferredApiCall

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 1515 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/DeferredApiCall.h` | C++ | 161 |

## Overview

[[[PROSE overview unit=api/DeferredApiCall tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::DeferredApiCall::no_wrap`](#gplatesapideferredapicallno_wrap) | struct | — | — | 0 | A tag for use as a template parameter to ArgReferenceWrappings that indicates that the corresponding function parameter should not be given a reference wrapper when bound with the function for later execution. |
| [`GPlatesApi::DeferredApiCall::ref`](#gplatesapideferredapicallref) | struct | — | — | 0 | A tag for use as a template parameter to ArgReferenceWrappings that indicates that the corresponding function parameter should be given a non-const reference wrapper when bound with the function for later execution. |
| [`GPlatesApi::DeferredApiCall::cref`](#gplatesapideferredapicallcref) | struct | — | — | 0 | A tag for use as a template parameter to ArgReferenceWrappings that indicates that the corresponding function parameter should be given a const reference wrapper when bound with the function for later execution. |
| [`GPlatesApi::DeferredApiCall::ArgReferenceWrappings`](#gplatesapideferredapicallargreferencewrappings) | struct | — | `< typename A0 = no_wrap, typename A1 = no_wrap, typename A2 = no_wrap, typename A3 = no_wrap, typename A4 = no_wrap, typename A5 = no_wrap, typename A6 = no_wrap, typename A7 = no_wrap, typename A8 = no_wrap, typename A9 = no_wrap >` | 0 | — |

## Members

### `GPlatesApi::DeferredApiCall::no_wrap`

*None.*

### `GPlatesApi::DeferredApiCall::ref`

*None.*

### `GPlatesApi::DeferredApiCall::cref`

*None.*

### `GPlatesApi::DeferredApiCall::ArgReferenceWrappings`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `wrappings` | typedef | `boost::mpl::vector< A0, A1, A2, A3, A4, A5, A6, A7, A8, A9 >` | private | — |
| `get` | struct | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_DEFERREDAPICALL_H` | macro | `None` | — |
| `GPLATES_DEFERRED_API_CALL` | macro_function | `GPlatesApi::DeferredApiCallImpl::make_wrapper((F)).wrap<F>((A))` | For example, status\_message is a member function of ViewportWindow that interacts with QWidget objects. |

## Notes

[[[PROSE notes unit=api/DeferredApiCall tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 11 |
| [api/DeferredApiCallImpl](DeferredApiCallImpl.md) | api | 2 |
| [api/PyApplication](PyApplication.md) | api | 1 |

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `set_status_message` | function | — | `* GPLATES_DEFERRED_API_CALL(&GPlatesQtWidgets::ViewportWindow::status_message` |
| `set_status_message` | function | — | `* GPLATES_DEFERRED_API_CALL(&status_message` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/DeferredApiCall.h
python scripts/gpq.py def GPlatesApi::DeferredApiCall::ArgReferenceWrappings --body
python scripts/gpq.py uses ArgReferenceWrappings --kind struct
python scripts/gpq.py hier ArgReferenceWrappings
```
