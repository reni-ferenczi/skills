# TypeTraits

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 472 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/TypeTraits.h` | C++ | 170 |

## Overview

`TypeTraits<T>` is a small, deliberately non-comprehensive compile-time type
traits facility, built before the project could rely on `<type_traits>` or a
full Boost.TypeTraits dependency. It classifies `T` as built-in, integral or
floating-point by checking membership in `boost::mpl::set` lists of the
concrete built-in types (`TypeTraitsInternals::built_in_types`,
`integral_types`, `floating_point_types`), with a partial specialisation of
`IsBuiltIn` for pointer types so any `T *` is treated as built-in.

The practically useful output is `TypeTraits<T>::argument_type`, computed via
`Select` as `T` when `T` is built-in and `const T &` otherwise — a standard
"pick a cheap parameter type" trick used by generic code that does not want to
pay for pass-by-reference on primitives or pay for pass-by-value on larger
objects.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::TypeTraitsInternals::built_in_types`](#gplatesutilstypetraitsinternalsbuilt_in_types) | typedef | — | — | 0 | — |
| [`GPlatesUtils::TypeTraitsInternals::IsBuiltIn`](#gplatesutilstypetraitsinternalsisbuiltin) | class | — | `<typename T>` | 0 | — |
| [`GPlatesUtils::TypeTraitsInternals::IsBuiltIn<T *>`](#gplatesutilstypetraitsinternalsisbuiltint-) | class | — | `<typename T>` | 0 | — |
| [`GPlatesUtils::TypeTraitsInternals::integral_types`](#gplatesutilstypetraitsinternalsintegral_types) | typedef | — | — | 0 | — |
| [`GPlatesUtils::TypeTraitsInternals::IsIntegral`](#gplatesutilstypetraitsinternalsisintegral) | class | — | `<typename T>` | 0 | — |
| [`GPlatesUtils::TypeTraitsInternals::floating_point_types`](#gplatesutilstypetraitsinternalsfloating_point_types) | typedef | — | — | 0 | — |
| [`GPlatesUtils::TypeTraitsInternals::IsFloatingPoint`](#gplatesutilstypetraitsinternalsisfloatingpoint) | class | — | `<typename T>` | 0 | — |
| [`GPlatesUtils::TypeTraits`](#gplatesutilstypetraits) | struct | — | `<typename T>` | 0 | Provides compile-time type information. |

## Members

### `GPlatesUtils::TypeTraitsInternals::built_in_types`

*None.*

### `GPlatesUtils::TypeTraitsInternals::IsBuiltIn`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `result_type` | typedef | `typename boost::mpl::has_key<built_in_types, T>::type` | private | — |
| `(anonymous enum)` | enum | `None` | public | — |

### `GPlatesUtils::TypeTraitsInternals::IsBuiltIn<T *>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |

### `GPlatesUtils::TypeTraitsInternals::integral_types`

*None.*

### `GPlatesUtils::TypeTraitsInternals::IsIntegral`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `result_type` | typedef | `typename boost::mpl::has_key<built_in_types, T>::type` | private | — |
| `(anonymous enum)` | enum | `None` | public | — |

### `GPlatesUtils::TypeTraitsInternals::floating_point_types`

*None.*

### `GPlatesUtils::TypeTraitsInternals::IsFloatingPoint`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `result_type` | typedef | `typename boost::mpl::has_key<floating_point_types, T>::type` | private | — |
| `(anonymous enum)` | enum | `None` | public | — |

### `GPlatesUtils::TypeTraits`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `argument_type` | typedef | `typename Select<is_built_in, T, const T &>::result` | public | Use argument\_type to pick a good type for arguments to functions. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_TYPETRAITS_H` | macro | `None` | — |

## Notes

The header's own comment warns that this is not a comprehensive traits
implementation: it only covers the fixed list of built-in scalar types plus
raw pointers, and gives incorrect results for implementation-specific or
compiler-extension types outside that list.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CptColourPalette](../gui/CptColourPalette.md) | gui | 11 |
| [gui/ColourRawRaster](../gui/ColourRawRaster.md) | gui | 6 |
| [qt-widgets/SelectionWidget](../qt-widgets/SelectionWidget.md) | qt-widgets | 5 |
| [maths/MathsUtils](../maths/MathsUtils.md) | maths | 4 |
| [gui/ColourPalette](../gui/ColourPalette.md) | gui | 3 |
| [gui/ColourPaletteAdapter](../gui/ColourPaletteAdapter.md) | gui | 3 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 2 |
| [gui/RasterColourPalette](../gui/RasterColourPalette.md) | gui | 2 |
| [property-values/ProxiedRasterResolver](../property-values/ProxiedRasterResolver.md) | property-values | 2 |
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 1 |
| [property-values/RawRasterUtils](../property-values/RawRasterUtils.md) | property-values | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/TypeTraits.h
python scripts/gpq.py def GPlatesUtils::TypeTraits --body
python scripts/gpq.py uses TypeTraits --kind struct
python scripts/gpq.py hier TypeTraits
```
