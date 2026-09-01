# CallStackTracker

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 877 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/CallStackTracker.h` | C++ | 220 |
| `src/utils/CallStackTracker.cc` | C++ | 68 |

## Overview

A hand-rolled, opt-in call stack. `CallStack` is a Meyers singleton wrapping a
`std::vector<Trace>`, where a `Trace` is nothing but the `const char *` from
`__FILE__` and the `int` from `__LINE__`; `CallStackTracker` is the RAII wrapper
that pushes a `Trace` in its constructor and pops it in its destructor. There is
no platform stack walking here — a frame appears in the trace only because some
code explicitly created a tracker for it.

The reason this exists is that GPlates catches its exceptions at the very top of
the program, in `GPlatesGui::GPlatesQApplication`, by which time the real machine
stack between the throw site and the handler is gone. So
`GPlatesGlobal::Exception`'s constructor instantiates a `CallStackTracker` for
its own throw location and then immediately calls
`CallStack::instance().write_call_stack_trace()` into an `ostringstream`,
freezing the trace as a `std::string` member that the handler can print much
later. `GPlatesGlobal::Abort` in `src/global/GPlatesAssert.cc` does the same
thing before aborting. That is the whole design: capture at construction,
because capture at catch would be too late.

This also explains the size of the fan-in list below, which is misleading if you
read it as "these units track their call stack". `CallStack::Trace` is the type
of the first constructor argument of *every* exception derived from
`GPlatesGlobal::Exception`, and both `GPLATES_EXCEPTION_SOURCE`
(`src/global/GPlatesException.h`) and `GPLATES_ASSERTION_SOURCE`
(`src/global/GPlatesAssert.h`) expand to `CallStack::Trace(__FILE__, __LINE__)`.
Nearly all of those 185 units are simply throwing an exception or calling
`GPlatesGlobal::Assert`. Actual stack tracking — the `TRACK_CALL_STACK()` macro —
has exactly one live call site in the tree, `src/model/XmlNode.cc`. The comment
in `GPlatesQApplication.cc` is candid about why: this trace is far less
informative than a native debugger's, so debug builds deliberately do not catch
`GPlatesGlobal::Exception` at all and let the debugger keep the real stack.

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

- **Not thread safe.** The singleton is one process-wide `std::vector` with no
  mutex anywhere in the header or the `.cc`. Every `push`/`pop` from every thread
  hits the same vector, and a trace captured on one thread will contain frames
  pushed by another. Anything that constructs a `GPlatesGlobal::Exception` off
  the main thread is touching this shared state.
- **`pop()` is unchecked.** It calls `d_call_stack.pop_back()` with no emptiness
  test, so an unmatched pop is undefined behaviour. Never call `CallStack::push`
  or `pop` directly — go through `CallStackTracker` or `TRACK_CALL_STACK()` so
  the pairing is enforced by scope.
- **`CallStackTracker` is copyable.** It has no `boost::noncopyable` base and no
  deleted copy constructor, but the copy does not push. Copying one, or storing
  one anywhere other than a local variable, pops more times than it pushed. Stack
  locals only.
- **`Trace` stores the pointer, not the string.** It keeps the `const char *`
  verbatim with no copy, which is correct for `__FILE__` (a string literal with
  static storage) and a dangling pointer for anything else. Do not build a
  `Trace` from a temporary buffer or a `QString`'s data.
- **Iterators are invalidated by `push`.** The Doxygen warning against calling
  `push`/`pop` between `call_stack_begin()` and `call_stack_end()` is a real
  reallocation hazard, not a style rule.
- The destructor swallows every exception from `pop()`, so a corrupted stack
  fails silently rather than terminating.
- The capture cost is paid on *construction* of every GPlates exception, not on
  printing: `generate_call_stack_trace_string()` formats and allocates a string
  even for exceptions that are caught and discarded without their message ever
  being read.

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
