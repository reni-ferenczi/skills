# Endian

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1736 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Endian.h` | C++ | 382 |

## Overview

[[[PROSE overview unit=utils/Endian tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_ENDIAN_H` | macro | `None` | — |
| `swap( T &object)` | function | `void` | Swaps bytes in the data element to effectively switch/toggle endian-ness. |
| `swap( void *data)` | function | `void` | — |
| `swap( char &object)` | function | `void` | — |
| `swap( unsigned char &object)` | function | `void` | — |
| `swap( short &object)` | function | `void` | — |
| `swap( unsigned short &object)` | function | `void` | — |
| `swap( int &object)` | function | `void` | — |
| `swap( unsigned int &object)` | function | `void` | — |
| `swap( long &object)` | function | `void` | — |
| `swap( unsigned long &object)` | function | `void` | — |
| `swap( float &object)` | function | `void` | — |
| `swap( double &object)` | function | `void` | — |
| `swap( ForwardIteratorType begin, ForwardIteratorType end)` | function | `void` | — |
| `convert( T &object, QSysInfo::Endian endian)` | function | `void` | — |
| `convert( ForwardIteratorType begin, ForwardIteratorType end, QSysInfo::Endian endian)` | function | `void` | — |

## Notes

[[[PROSE notes unit=utils/Endian tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLScalarField3DGenerator](../opengl/GLScalarField3DGenerator.md) | opengl | 4 |
| [gui/ColourScaleGenerator](../gui/ColourScaleGenerator.md) | gui | 3 |
| [file-io/RasterFileCacheFormatReader](../file-io/RasterFileCacheFormatReader.md) | file-io | 2 |
| [file-io/ScalarField3DFileFormat](../file-io/ScalarField3DFileFormat.md) | file-io | 1 |
| [gui/Colour](../gui/Colour.md) | gui | 1 |
| [opengl/GLScalarField3D](../opengl/GLScalarField3D.md) | opengl | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Endian.h
```
