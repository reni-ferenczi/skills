# ReferenceCount

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1130 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/ReferenceCount.h` | C++ | 272 |

## Overview

The ownership model of nearly everything in GPlates. Almost every heap object
with a lifetime — property values, feature revisions, layer proxies, OpenGL
resources, scribe transcriptions — derives from this CRTP mixin and is passed
around as a `GPlatesUtils::non_null_intrusive_ptr`, which is why so many classes
carry the familiar `non_null_ptr_type` and `non_null_ptr_to_const_type` typedefs.
`intrusive_ptr_add_ref` and `intrusive_ptr_release` are free functions in
`GPlatesUtils` taking a `const ReferenceCount<Derived> *`, which is the hook both
`boost::intrusive_ptr` and `non_null_intrusive_ptr` find by argument-dependent
lookup for any derived type.

The curiously-recurring template parameter is not decoration. `intrusive_ptr_release`
`static_cast`s down to `Derived` and calls `boost::checked_delete` on *that*, so
the base needs no virtual destructor — and therefore no vtable pointer. The
comment on that function makes the trade explicit: a `ReferenceCount` object is
exactly one `atomic_count` wide, which matters when hundreds of thousands of
property values are alive. The `static_cast` is safe because the compiler knows
`Derived` statically and can apply any multiple-inheritance pointer fixups;
`checked_delete` is there to force a complete type so a non-trivial destructor
cannot be silently skipped.

The counter is `boost::detail::atomic_count` rather than a plain `long` — the
same primitive `boost::shared_ptr` uses, chosen because `boost::atomic` did not
exist before boost 1.53. The header records the measured cost of that choice: 32
instructions instead of about 5 on an Intel CPU circa 2013, roughly six times
slower to increment, and judged not to matter against the client code around it.
The two free helpers close the loop back the other way: `get_non_null_pointer` is
the intrusive equivalent of `enable_shared_from_this` — hand it a raw `this` and
get an owning pointer — and `make_shared_from_intrusive` produces a
`boost::shared_ptr` whose deleter is `intrusive_ptr_release`, so it joins the
existing count rather than starting a competing one, for the APIs that insist on
a `shared_ptr`.

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

- **The count starts at zero**, so a freshly `new`ed object is owned by nobody
  and must be handed to an intrusive pointer immediately. Hence the near-universal
  pattern in the derived classes: non-public constructors plus a static `create()`
  returning `non_null_ptr_type`. Calling `get_non_null_pointer(this)` from inside
  a constructor throws `IntrusivePointerZeroRefCountException` for exactly this
  reason.
- **If `Derived` is itself subclassed further, `Derived` must have a virtual
  destructor.** `intrusive_ptr_release` casts to the class named in the template
  argument, not to the most-derived class, so without one the object is destroyed
  as a `Derived` and the rest is silently leaked. This is the easiest way to get
  this wrong and it produces no diagnostic.
- **`boost::checked_delete<Derived>` needs the complete definition of `Derived`**
  wherever the intrusive pointer's destructor is instantiated. A forward
  declaration compiles until something actually releases a reference.
- **A derived copy constructor must reset the count, not copy it.** The base is
  `private boost::noncopyable`, which suppresses the compiler-generated copy
  constructor and forces each copyable derived class to write one that
  default-constructs the base — see `GPlatesModel::PropertyValue`'s copy
  constructor and the comment above it, which spells out that the clone must
  start at zero.
- **`increment_ref_count` and `decrement_ref_count` are public but off limits.**
  The Doxygen says so directly: calling them by hand alongside intrusive pointers
  desynchronises the count. They are public only because the free functions need
  them.
- **Atomic means the counter, not the object.** Two threads can share ownership
  safely, but nothing here synchronises access to the object's own state, and the
  final `delete` runs on whichever thread happens to drop the last reference.
  `get_reference_count()` is a bare atomic read — informative only, never a basis
  for a decision.
- The count is `mutable` and all three accessors are `const`, which is what makes
  `non_null_intrusive_ptr<const T>` and the pervasive
  `non_null_ptr_to_const_type` work.
- `make_shared_from_intrusive` deliberately shares ownership rather than
  duplicating it; the object dies when the *combined* count hits zero, whichever
  kind of pointer holds the last reference.
- The gcc 4.6 `-Wuninitialized` workaround near the top uses a bare
  `#pragma GCC diagnostic ignored` with no matching pop, so on that compiler it
  stays in effect for the rest of any translation unit that includes this header.

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
