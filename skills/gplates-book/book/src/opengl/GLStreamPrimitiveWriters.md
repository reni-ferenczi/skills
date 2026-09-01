# GLStreamPrimitiveWriters

[Book TOC](../../TOC.md) · [opengl](../../components/opengl.md) · cluster Community 1044 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/opengl/GLStreamPrimitiveWriters.h` | C++ | 193 |

## Overview

[[[PROSE overview unit=opengl/GLStreamPrimitiveWriters tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=opengl/GLStreamPrimitiveWriters tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
