# non_null_intrusive_ptr

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1279 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/non_null_intrusive_ptr.h` | C++ | 305 |

## Overview

The ownership primitive of the whole codebase, and — with 321 units referencing
it and around 750 files declaring a `non_null_ptr_type` — the single most widely
depended-on type in `utils`. It is a verbatim fork of Boost's
`intrusive_ptr.hpp` (Peter Dimov's, under the Boost licence, which is why the
brace style and the ancient compiler workarounds in this file look nothing like
the rest of GPlates) with one change: the pointer can never be null. There is no
default constructor, no `reset()`, and every constructor either takes an
existing `non_null_intrusive_ptr` or a raw `T *` that it checks. Everything else
— the intrusive counting, the comparison operators, the pointer casts, the
`get_pointer()` hook for `boost::mem_fn` — is unmodified upstream code.

The point of the "non-null" part is that it moves a null check from every
dereference to a single point of construction. Because the invariant holds by
construction, `operator*` and `operator->` need no test, and a function taking a
`non_null_ptr_type` needs no precondition. Where a pointer is genuinely optional
the codebase wraps it in `boost::optional` rather than reaching for a nullable
pointer. The counterpart to `boost::intrusive_ptr` is kept live in both
directions: this header defines mixed `operator==` / `operator!=` against
`boost::intrusive_ptr`, and `get_intrusive_ptr()` converts one way.

Counting itself is not implemented here. The class relies on unqualified
`intrusive_ptr_add_ref(T *)` and `intrusive_ptr_release(T *)` found by ADL, and
in practice those come from `GPlatesUtils::ReferenceCount`, the CRTP base almost
every managed class derives from. That base holds a `boost::detail::atomic_count`
and, on the count reaching zero, `boost::checked_delete`s the pointer
`static_cast` back to the `Derived` template argument — which is precisely why
`ReferenceCount` needs no virtual destructor and costs no vtable pointer. The
companion `NullIntrusivePointerHandler` is the default `H` policy: its
`operator()` aborts in a `GPLATES_DEBUG` build so the offending stack is visible
in a debugger, and throws `NullNonNullIntrusivePointerException` otherwise. Read
those two headers alongside this one; none of the three makes sense alone.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::UnhandledNullPointerException`](#gplatesutilsunhandlednullpointerexception) | struct | — | — | 0 | This exception is thrown when the null\_handler\_type fails to handle a NULL pointer. |
| [`GPlatesUtils::non_null_intrusive_ptr`](#gplatesutilsnon_null_intrusive_ptr) | class | — | `<class T, class H = NullIntrusivePointerHandler>` | 0 | non\_null\_intrusive\_ptr A smart pointer that uses intrusive reference counting. |

## Members

### `GPlatesUtils::UnhandledNullPointerException`

*None.*

### `GPlatesUtils::non_null_intrusive_ptr`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type` | typedef | `non_null_intrusive_ptr` | private | — |
| `element_type` | typedef | `T` | public | — |
| `null_handler_type` | typedef | `H` | public | — |
| `non_null_intrusive_ptr(T * p, H const & handle_null = H(), bool add_ref = true)` | constructor | `None` | public | — |
| `non_null_intrusive_ptr(non_null_intrusive_ptr<U, I> const & rhs)` | constructor | `None` | public | — |
| `non_null_intrusive_ptr(non_null_intrusive_ptr const & rhs)` | constructor | `None` | public | — |
| `~non_null_intrusive_ptr()` | destructor | `None` | public | — |
| `get()` | method | `T` | public | — |
| `operator->()` | operator | `T` | public | — |
| `operator!()` | operator | `bool` | public | operator! is a Borland-specific workaround |
| `swap(non_null_intrusive_ptr & rhs)` | method | `void` | public | — |
| `p_` | field | `T` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NON_NULL_INTRUSIVE_PTR_HPP_INCLUDED` | macro | `None` | — |
| `operator==(non_null_intrusive_ptr<T, H> const & a, non_null_intrusive_ptr<U, I> const & b)` | operator | `bool` | — |
| `operator!=(non_null_intrusive_ptr<T, H> const & a, non_null_intrusive_ptr<U, I> const & b)` | operator | `bool` | — |
| `operator==(non_null_intrusive_ptr<T, H> const & a, boost::intrusive_ptr<U> const & b)` | operator | `bool` | — |
| `operator!=(non_null_intrusive_ptr<T, H> const & a, boost::intrusive_ptr<U> const & b)` | operator | `bool` | — |
| `operator==(boost::intrusive_ptr<T> const & a, non_null_intrusive_ptr<U, I> const & b)` | operator | `bool` | — |
| `operator!=(boost::intrusive_ptr<T> const & a, non_null_intrusive_ptr<U, I> const & b)` | operator | `bool` | — |
| `operator==(non_null_intrusive_ptr<T, H> const & a, T * b)` | operator | `bool` | — |
| `operator!=(non_null_intrusive_ptr<T, H> const & a, T * b)` | operator | `bool` | — |
| `operator==(T * a, non_null_intrusive_ptr<T, H> const & b)` | operator | `bool` | — |
| `operator!=(T * a, non_null_intrusive_ptr<T, H> const & b)` | operator | `bool` | — |
| `operator!=(non_null_intrusive_ptr<T, H> const & a, non_null_intrusive_ptr<T, H> const & b)` | operator | `bool` | Resolve the ambiguity between our op!= and the one in rel\_ops |
| `operator<(non_null_intrusive_ptr<T, H> const & a, non_null_intrusive_ptr<T, H> const & b)` | operator | `bool` | — |
| `swap(non_null_intrusive_ptr<T, H> & lhs, non_null_intrusive_ptr<T, H> & rhs)` | function | `void` | — |
| `get_intrusive_ptr(non_null_intrusive_ptr<T, H> const & p)` | function | `boost::intrusive_ptr<T>` | — |
| `get_pointer(non_null_intrusive_ptr<T, H> const & p)` | function | `T` | mem\_fn support |
| `static_pointer_cast(non_null_intrusive_ptr<U, H> const & p)` | function | `non_null_intrusive_ptr<T, H>` | — |
| `const_pointer_cast(non_null_intrusive_ptr<U, H> const & p)` | function | `non_null_intrusive_ptr<T, H>` | — |
| `dynamic_pointer_cast(non_null_intrusive_ptr<U, H> const & p)` | function | `non_null_intrusive_ptr<T, H>` | — |

## Notes

- **`dynamic_pointer_cast` cannot fail gracefully.** `dynamic_cast` returns null
  on a failed downcast, and that null goes straight into the raw-pointer
  constructor — which aborts in a debug build and throws
  `NullNonNullIntrusivePointerException` in a release build. It is not the
  optional-returning cast its name suggests. Test the type first, or go through
  `boost::intrusive_ptr` / a visitor.
- **The raw-pointer constructor is not `explicit`,** and both its other
  parameters are defaulted. Any `T *` in scope converts silently to an owning
  pointer, which is what makes `return non_null_ptr_type(new Foo(...))` read so
  cleanly but also means an accidental conversion compiles. Passing
  `add_ref = false` adopts the pointer *without* incrementing — correct only when
  you are transferring a count you already hold, and a leak or double-free
  otherwise.
- **The null-handling path is two-stage and the second stage is nearly dead
  code.** The constructor calls `handle_null()` and only throws
  `UnhandledNullPointerException` if that returns. The default
  `NullIntrusivePointerHandler` never returns, so in practice you see an abort
  (debug) or `NullNonNullIntrusivePointerException` (release);
  `UnhandledNullPointerException` is an empty `struct` outside the
  `GPlatesGlobal::Exception` hierarchy and is only reachable via a custom `H`.
- **The null tests inherited from Boost are vestigial.** `operator!`, the
  `unspecified_bool_type` conversion and the `p_ == 0` checks survive verbatim
  from `intrusive_ptr.hpp`, but the class invariant makes them constant. Code
  that tests a `non_null_intrusive_ptr` for truth is testing nothing; use
  `boost::optional<non_null_ptr_type>` where absence is a real state.
- **Reference cycles leak.** Intrusive counting has no weak-pointer counterpart
  here, and `boost::weak_ptr` does not work with it. The bridge, when you need
  one, is `GPlatesUtils::make_shared_from_intrusive()` in `ReferenceCount.h`,
  which yields a `boost::shared_ptr` sharing the same ownership.
- **You cannot make one of these to an unmanaged object.** Taking a pointer to
  `this` inside a constructor, or to a stack object, breaks the counting;
  `GPlatesUtils::get_non_null_pointer()` exists for the safe case and asserts
  `get_reference_count() != 0`, throwing
  `GPlatesGlobal::IntrusivePointerZeroRefCountException` otherwise.
- **Thread safety is exactly the counter's, no more.** `ReferenceCount` uses
  `boost::detail::atomic_count`, so copying and destroying pointers on different
  threads is safe; assigning to or swapping *the same pointer object* from two
  threads is not, and neither is the pointed-to object.
- **Ordering is by address.** `operator<` is `std::less<T *>`, which makes these
  usable as `std::map` keys but gives an order that varies between runs — never
  serialise or iterate in it expecting stability.
- **Treat the file as vendored.** It is a lightly patched copy of upstream Boost
  with its own header guard style, its own formatting and workarounds for
  compilers no longer in use. Keep edits surgical rather than modernising it; the
  policy-shaped behaviour belongs in `NullIntrusivePointerHandler` or
  `ReferenceCount` instead.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionGeometryUtils](../app-logic/ReconstructionGeometryUtils.md) | app-logic | 94 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 84 |
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 50 |
| [opengl/GLRenderer](../opengl/GLRenderer.md) | opengl | 50 |
| [app-logic/RasterLayerProxy](../app-logic/RasterLayerProxy.md) | app-logic | 46 |
| [model/Gpgim](../model/Gpgim.md) | model | 42 |
| [maths/GreatCircleArc](../maths/GreatCircleArc.md) | maths | 37 |
| [app-logic/ReconstructionGeometryVisitor](../app-logic/ReconstructionGeometryVisitor.md) | app-logic | 30 |
| [opengl/GLOffScreenContext](../opengl/GLOffScreenContext.md) | opengl | 29 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 28 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 28 |
| [gui/LayerPainter](../gui/LayerPainter.md) | gui | 27 |
| [maths/PolygonPartitioner](../maths/PolygonPartitioner.md) | maths | 23 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 21 |
| [file-io/RgbaRasterReader](../file-io/RgbaRasterReader.md) | file-io | 21 |
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 21 |
| [app-logic/TimeSpanUtils](../app-logic/TimeSpanUtils.md) | app-logic | 20 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 19 |
| [maths/FiniteRotation](../maths/FiniteRotation.md) | maths | 19 |
| [maths/PolygonOnSphere](../maths/PolygonOnSphere.md) | maths | 19 |

*... and 301 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/non_null_intrusive_ptr.h
python scripts/gpq.py def GPlatesUtils::non_null_intrusive_ptr --body
python scripts/gpq.py uses non_null_intrusive_ptr --kind class
python scripts/gpq.py hier non_null_intrusive_ptr
```
