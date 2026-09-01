# ScribeLoadRef

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 349 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeLoadRef.h` | C++ | 192 |

## Overview

[[[PROSE overview unit=scribe/ScribeLoadRef tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::LoadRef`](#gplatesscribeloadref) | class | — | `<typename ObjectType>` | 0 | A shared reference to an object loaded from an archive using Scribe::load() or a reference to an object using Scribe::load\_reference(). |

## Members

### `GPlatesScribe::LoadRef`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LoadRef()` | constructor | `None` | public | A NULL reference (no object referenced). |
| `is_valid()` | method | `bool` | public | Return whether this reference is valid to be dereferenced, or whether it's a NULL reference. |
| `get` | field | `ObjectType` | public | Get the referenced object. |
| `operator->()` | operator | `ObjectType` | public | Indirection operator. |
| `TrackingDeleter` | struct | `None` | private | Custom boost::shared\_ptr deleter that untracks the object if it's still being tracked. |
| `LoadRef( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe, ObjectType *object, bool release)` | constructor | `None` | private | Successful transcribe - object should be non-null. |
| `untrack( Scribe *scribe, ObjectType *object, bool discard)` | method | `void` | private | Used by TrackingDeleter to get friend access to ScribeInternalAccess. |
| `d_object` | field | `boost::shared_ptr<ObjectType>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBELOADREF_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=scribe/ScribeLoadRef tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 70 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 56 |
| [scribe/TranscriptionScribeContext](TranscriptionScribeContext.md) | scribe | 21 |
| [scribe/TranscribeBoost](TranscribeBoost.md) | scribe | 14 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 14 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 8 |
| [gui/BuiltinColourPalettes](../gui/BuiltinColourPalettes.md) | gui | 7 |
| [scribe/TranscribeMappingProtocol](TranscribeMappingProtocol.md) | scribe | 7 |
| [scribe/TranscribeSequenceProtocol](TranscribeSequenceProtocol.md) | scribe | 5 |
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 3 |
| [model/TranscribeStringContentTypeGenerator](../model/TranscribeStringContentTypeGenerator.md) | model | 2 |
| [scribe/ScribeLoadRefImpl](ScribeLoadRefImpl.md) | scribe | 2 |
| [scribe/TranscribeNonNullIntrusivePtr](TranscribeNonNullIntrusivePtr.md) | scribe | 2 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 1 |
| [scribe/ScribeExceptions](ScribeExceptions.md) | scribe | 1 |
| [scribe/ScribeInternalAccess](ScribeInternalAccess.md) | scribe | 1 |
| [scribe/ScribeTextArchiveReader](ScribeTextArchiveReader.md) | scribe | 1 |
| [scribe/TranscribeArray](TranscribeArray.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeLoadRef.h
python scripts/gpq.py def GPlatesScribe::LoadRef --body
python scripts/gpq.py uses LoadRef --kind class
python scripts/gpq.py hier LoadRef
```
