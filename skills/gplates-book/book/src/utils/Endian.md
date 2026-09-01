# Endian

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1736 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Endian.h` | C++ | 382 |

## Overview

`Endian` provides fast endianness conversion functions for basic types and sequences, optimized for processing large raster arrays. It offers `swap()` functions to reverse byte order in place, and `convert()` functions to swap only when the input data's endianness differs from the runtime system.

The implementation uses size-based dispatch through template specialization: types of the same byte size (1, 2, 4, 8) are handled identically using bitwise operations. All functions are inline to enable inlining in the hot path. Qt provides similar functions but is slower; this module was created to speed up CPU-intensive raster conversions. Custom types can be supported by specializing `swap()` for the struct or class.

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

The unspecialized `swap<T>()` template is intentionally undefined; code using unsupported types will not compile. Byte-swapping is in-place and modifies the argument; no copy is made. The `convert()` function is symmetric: the same call converts from system endian to the specified endian or vice versa. Custom types must specialize `swap()` within the `GPlatesUtils::Endian` namespace, recursively swapping member fields of basic types; the header documents the required pattern.

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
