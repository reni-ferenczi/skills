# GLStreamPrimitiveWriters

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1044 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStreamPrimitiveWriters.h` | C++ | 193 |

## Overview

Both classes implement the same informal, non-virtual `StreamWriter` interface
documented in the file's top comment (`write`, `count`, `remaining`), so
`GLStreamPrimitives` (the actual streaming logic, in the neighbouring unit)
can be templated on either one interchangeably rather than depending on a
concrete buffer type. `StreamElementType` stands for either a vertex
attribute type or an index type (`GLuint`/`GLushort`/`GLubyte`).

`GLStaticBufferStreamWriter` writes into a caller-supplied fixed-size raw
buffer — the intended use is a mapped vertex buffer object, where only write
access to memory is available and the total vertex/index count isn't known in
advance, so the caller streams until the buffer fills and then flushes it to
the GPU. `GLDynamicBufferStreamWriter` instead appends to a `std::vector`,
for the case where the data is generated once (e.g. building a static, reused
vertex buffer) and the final size isn't known up front either, but repeated
GPU uploads are not needed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesOpenGL::GLStaticBufferStreamWriter`](#gplatesopenglglstaticbufferstreamwriter) | class | — | `<typename StreamElementType>` | 0 | Stream writer class to write to a fixed size buffer. |
| [`GPlatesOpenGL::GLDynamicBufferStreamWriter`](#gplatesopenglgldynamicbufferstreamwriter) | class | — | `<typename StreamElementType>` | 0 | Stream writer class to write to a variable size buffer using a std::vector. |

## Members

### `GPlatesOpenGL::GLStaticBufferStreamWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLStaticBufferStreamWriter( StreamElementType *stream, unsigned int max_num_stream_elements, unsigned int initial_count = 0)` | constructor | `None` | public | Constructor. initial\_count can be used for vertices to indicate that a vertex buffer already has some vertices in it - then the vertex elements (indices) can be correctly offset from the start of the vertex buffer instead of the start of ... |
| `write( const StreamElementType &stream_element)` | method | `void` | public | Writes the specified stream element and increments write pointer to the next element. |
| `count()` | method | `unsigned int` | public | Returns the count of stream elements. |
| `remaining()` | method | `unsigned int` | public | Returns the number of stream elements that can still be written (that there is space for). |
| `d_stream` | field | `StreamElementType` | private | — |
| `d_max_num_stream_elements` | field | `unsigned int` | private | — |
| `d_initial_count` | field | `unsigned int` | private | — |
| `d_current_stream_element` | field | `StreamElementType` | private | — |

### `GPlatesOpenGL::GLDynamicBufferStreamWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GLDynamicBufferStreamWriter( std::vector<StreamElementType> &stream)` | constructor | `None` | public | — |
| `write( const StreamElementType &stream_element)` | method | `void` | public | Appends the specified stream element. |
| `count()` | method | `unsigned int` | public | Returns the number of stream elements in the 'std::vector' passed into constructor. |
| `remaining()` | method | `unsigned int` | public | Since a std::vector can grow arbitrarily large it's unlikely the limit will ever be reached so just return the maximum size of vector (don't bother subtracting off the number of elements currently in the vector - this function gets called ... |
| `d_stream` | field | `std::vector<StreamElementType>` | private | — |
| `d_max_stream_elements` | field | `unsigned int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_OPENGL_GLSTREAMPRIMITIVEWRITERS_H` | macro | `None` | — |

## Notes

- `GLStaticBufferStreamWriter` does no bounds checking on `write` — the caller
  must consult `remaining()` itself to avoid writing past
  `max_num_stream_elements`.
- `GLStaticBufferStreamWriter` neither owns nor reads the buffer it wraps; it
  only ever writes through the pointer, matching write-only mapped GPU
  memory.
- `GLDynamicBufferStreamWriter::remaining()` always returns the vector's
  `max_size()` rather than the true remaining capacity, since that limit is
  effectively unreachable in practice — it is not a precise "space left"
  count.

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLStreamPrimitives](GLStreamPrimitives.md) | opengl | 48 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/opengl/GLStreamPrimitiveWriters.h
python scripts/gpq.py def GPlatesOpenGL::GLStaticBufferStreamWriter --body
python scripts/gpq.py uses GLStaticBufferStreamWriter --kind class
python scripts/gpq.py hier GLStaticBufferStreamWriter
```
