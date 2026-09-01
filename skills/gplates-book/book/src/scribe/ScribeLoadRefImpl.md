# ScribeLoadRefImpl

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 349 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeLoadRefImpl.h` | C++ | 237 |

## Overview

The out-of-line implementation of `LoadRef<ObjectType>`, split out of `ScribeLoadRef.h` because it needs the full definition of `Scribe`, which would otherwise create a header cycle (`Scribe` also needs `LoadRef`). It defines the nested `TrackingDeleter`, the `boost::shared_ptr` deleter installed on `LoadRef::d_object`, along with the bodies of `LoadRef`'s constructor, `is_valid()`, `get()` and `untrack()`.

`TrackingDeleter` is where the "must check `is_valid()`" contract is actually enforced: its `operator()` asserts `is_valid_called`, via `GPlatesGlobal::Assert<Exceptions::ScribeTranscribeResultNotChecked>`, before the object is destroyed, and `get()` performs the same check before dereferencing. `is_valid()` marks the deleter as checked as a side effect of returning whether the reference is non-null. When `release` is true — meaning the `LoadRef` owns an object it allocated rather than merely referencing an existing one — the deleter also untracks the object (via `ScribeInternalAccess::untrack()`) before deleting it, covering both an unrelocated tracked object and one that was never trackable to begin with.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::LoadRef<ObjectType>::TrackingDeleter`](#gplatesscribeloadrefobjecttypetrackingdeleter) | struct | — | `<typename ObjectType>` | 0 | Define nested 'struct TrackingDeleter' here (ie, after class Scribe) to avoid cyclic dependency (since it makes a call to class Scribe and class Scribe calls 'LoadRef')... |

## Members

### `GPlatesScribe::LoadRef<ObjectType>::TrackingDeleter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TrackingDeleter( const GPlatesUtils::CallStack::Trace &transcribe_source_, Scribe *scribe_, bool release_)` | method | `None` | public | — |
| `operator()( ObjectType *object_ptr)` | operator | `void` | public | — |
| `transcribe_source` | field | `GPlatesUtils::CallStack::Trace` | public | — |
| `scribe` | field | `Scribe` | public | — |
| `is_valid_called` | field | `bool` | public | — |
| `release` | field | `bool` | public | — |
| `exception_thrown` | field | `bool` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBELOADREFIMPL_H` | macro | `None` | — |

## Notes

`TrackingDeleter::exception_thrown` guards against throwing a second exception while the first is already unwinding the stack through the deleter — the deleter is not supposed to throw, and a second exception during unwind would terminate the program with no diagnostic. It can only guard against exceptions thrown from within `LoadRef` itself (e.g. from `get()`); an exception thrown from unrelated code during unwind is not caught. `TrackingDeleter::operator()` swallows any exception thrown while untracking (`catch (...) {}`) before proceeding to `boost::checked_delete()`, so a failure in untracking never prevents the object from being freed. This header must be included wherever `LoadRef<ObjectType>` is actually constructed or dereferenced (i.e. together with `Scribe.h`), since `ScribeLoadRef.h` alone only declares the template.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 3 |
| [scribe/ScribeInternalUtilsImpl](ScribeInternalUtilsImpl.md) | scribe | 1 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 1 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeLoadRefImpl.h
python scripts/gpq.py def GPlatesScribe::LoadRef<ObjectType>::TrackingDeleter --body
python scripts/gpq.py uses LoadRef<ObjectType>::TrackingDeleter --kind struct
python scripts/gpq.py hier LoadRef<ObjectType>::TrackingDeleter
```
