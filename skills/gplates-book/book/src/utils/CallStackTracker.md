# CallStackTracker

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 877 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/CallStackTracker.h` | C++ | 220 |
| `src/utils/CallStackTracker.cc` | C++ | 68 |

## Overview

[[[PROSE overview unit=utils/CallStackTracker tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::CallStack`](#gplatesutilscallstack) | class | `boost::noncopyable` | — | 0 | This class is a singleton that keeps track of the call stack. |
| [`GPlatesUtils::CallStackTracker`](#gplatesutilscallstacktracker) | class | — | — | 0 | This class provides a means to track the call stack. |

## Members

### `GPlatesUtils::CallStack`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Trace` | class | `None` | public | Keeps track of the location of a specific trace in the call stack. |
| `trace_seq_type` | typedef | `std::vector<Trace>` | public | Typedef for a stack of CallStackElement objects. |
| `trace_const_iterator` | typedef | `trace_seq_type::const_iterator` | public | Typedef for iterator over const Trace objects. |
| `push( const Trace &)` | method | `void` | public | Start tracking a new stack trace . |
| `pop()` | method | `void` | public | Stop tracking matching stack trace from push. |
| `call_stack_begin()` | method | `trace_const_iterator` | public | Begin iterator of current call stack sequence. |
| `call_stack_end()` | method | `trace_const_iterator` | public | End iterator of current call stack sequence. |
| `write_call_stack_trace( std::ostream &output)` | method | `void` | public | Writes the call stack trace to output. |
| `CallStack()` | constructor | `None` | private | Constructor is private for singleton. |
| `d_call_stack` | field | `trace_seq_type` | private | — |

### `GPlatesUtils::CallStackTracker`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CallStackTracker( const CallStack::Trace &trace)` | constructor | `None` | public | — |
| `~CallStackTracker()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_CALLSTACKTRACKER_H` | macro | `None` | — |
| `CALL_STACK_MAGIC2` | macro_function | `GPlatesUtils::CallStackTracker call_stack_tracker##x(\ GPlatesUtils::CallStack::Trace(__FILE__, __LINE__));` | Do not invoke this macro directly. |
| `CALL_STACK_MAGIC1` | macro_function | `CALL_STACK_MAGIC2(x)` | Do not invoke this macro directly. |
| `TRACK_CALL_STACK` | macro_function | `CALL_STACK_MAGIC1(__LINE__)` | Track the call stack. |

## Notes

[[[PROSE notes unit=utils/CallStackTracker tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](../scribe/Scribe.md) | scribe | 129 |
| [scribe/ScribeExceptions](../scribe/ScribeExceptions.md) | scribe | 99 |
| [scribe/TranscribeUtils](../scribe/TranscribeUtils.md) | scribe | 61 |
| [scribe/ScribeInternalAccess](../scribe/ScribeInternalAccess.md) | scribe | 43 |
| [global/GPlatesAssert](../global/GPlatesAssert.md) | global | 30 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 29 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 27 |
| [utils/ConfigBundle](ConfigBundle.md) | utils | 24 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 20 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 19 |
| [maths/Rotation](../maths/Rotation.md) | maths | 18 |
| [global/GPlatesException](../global/GPlatesException.md) | global | 16 |
| [scribe/TranscribeDelegateProtocol](../scribe/TranscribeDelegateProtocol.md) | scribe | 16 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](../file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 14 |
| [scribe/ScribeLoadRefImpl](../scribe/ScribeLoadRefImpl.md) | scribe | 13 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 12 |
| [app-logic/ScalarField3DLayerTask](../app-logic/ScalarField3DLayerTask.md) | app-logic | 12 |
| [app-logic/VelocityFieldCalculatorLayerTask](../app-logic/VelocityFieldCalculatorLayerTask.md) | app-logic | 12 |
| [file-io/ExportTemplateFilenameSequence](../file-io/ExportTemplateFilenameSequence.md) | file-io | 12 |
| [opengl/GLRenderer](../opengl/GLRenderer.md) | opengl | 12 |

*... and 165 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/CallStackTracker.h
python scripts/gpq.py def GPlatesUtils::CallStack --body
python scripts/gpq.py uses CallStack --kind class
python scripts/gpq.py hier CallStack
```
