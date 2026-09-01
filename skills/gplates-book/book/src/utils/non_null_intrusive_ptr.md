# non_null_intrusive_ptr

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1279 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/non_null_intrusive_ptr.h` | C++ | 305 |

## Overview

[[[PROSE overview unit=utils/non_null_intrusive_ptr tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/non_null_intrusive_ptr tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
