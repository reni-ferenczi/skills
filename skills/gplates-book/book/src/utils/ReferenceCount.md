# ReferenceCount

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1130 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ReferenceCount.h` | C++ | 272 |

## Overview

[[[PROSE overview unit=utils/ReferenceCount tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::ReferenceCount`](#gplatesutilsreferencecount) | class | `boost::noncopyable` | `<class Derived>` | 366 | Allows incrementing, decrementing and retrieving a reference count. |

## Members

### `GPlatesUtils::ReferenceCount`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReferenceCount()` | constructor | `None` | public | Constructor. |
| `increment_ref_count()` | method | `void` | public | Increment the reference-count of this instance. |
| `decrement_ref_count()` | method | `long` | public | Decrement the reference-count of this instance, and return the new reference-count. |
| `get_reference_count()` | method | `long` | public | Returns the current reference count. |
| `ref_count_type` | typedef | `boost::detail::atomic_count` | private | The type used to store the reference-count of an instance of this class. |
| `d_ref_count` | field | `ref_count_type` | private | The reference-count of this instance by intrusive-pointers. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_REFERENCECOUNT_H` | macro | `None` | — |
| `intrusive_ptr_add_ref( const ReferenceCount<Derived> *p)` | function | `void` | — |
| `intrusive_ptr_release( const ReferenceCount<Derived> *p)` | function | `void` | — |
| `get_non_null_pointer( U *reference_count_derived)` | function | `GPlatesUtils::non_null_intrusive_ptr<U>` | — |
| `make_shared_from_intrusive( U *reference_count_derived)` | function | `boost::shared_ptr<U>` | — |
| `make_shared_from_intrusive( const GPlatesUtils::non_null_intrusive_ptr<U> &non_null_ptr)` | function | `boost::shared_ptr<U>` | — |

## Notes

[[[PROSE notes unit=utils/ReferenceCount tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/ScribeInternalUtils](../scribe/ScribeInternalUtils.md) | scribe | 13 |
| [utils/StringSet](StringSet.md) | utils | 13 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 6 |
| [model/FeatureRevision](../model/FeatureRevision.md) | model | 6 |
| [opengl/GLOffScreenContext](../opengl/GLOffScreenContext.md) | opengl | 6 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 6 |
| [app-logic/LayerParams](../app-logic/LayerParams.md) | app-logic | 5 |
| [opengl/GLStateSetKeys](../opengl/GLStateSetKeys.md) | opengl | 5 |
| [presentation/Session](../presentation/Session.md) | presentation | 5 |
| [scribe/ScribeArchiveReader](../scribe/ScribeArchiveReader.md) | scribe | 5 |
| [scribe/ScribeArchiveWriter](../scribe/ScribeArchiveWriter.md) | scribe | 5 |
| [scribe/Transcription](../scribe/Transcription.md) | scribe | 5 |
| [app-logic/CoRegistrationData](../app-logic/CoRegistrationData.md) | app-logic | 4 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 4 |
| [model/PropertyValue](../model/PropertyValue.md) | model | 4 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 4 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 4 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 4 |
| [utils/non_null_intrusive_ptr](non_null_intrusive_ptr.md) | utils | 4 |
| [app-logic/ScalarCoverageEvolution](../app-logic/ScalarCoverageEvolution.md) | app-logic | 3 |

*... and 136 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/ReferenceCount.h
python scripts/gpq.py def GPlatesUtils::ReferenceCount --body
python scripts/gpq.py uses ReferenceCount --kind class
python scripts/gpq.py hier ReferenceCount
```
