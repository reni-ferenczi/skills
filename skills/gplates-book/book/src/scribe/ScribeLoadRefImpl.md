# ScribeLoadRefImpl

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 349 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeLoadRefImpl.h` | C++ | 237 |

## Overview

[[[PROSE overview unit=scribe/ScribeLoadRefImpl tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/ScribeLoadRefImpl tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
