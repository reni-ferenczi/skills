# Parse

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 359 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Parse.h` | C++ | 350 |

## Overview

`Parse<T>` is a functor-based, extensible alternative to hand-writing `QString`-to-value conversions: the primary template is intentionally left undefined, and callers get a parser for a given `T` by using one of the specializations declared here (`int`, `unsigned int`, `float`, `double`, `bool`, `QString`, `const QString &`, and the `Int<Base, IntType>` wrapper) or by writing their own specialization alongside a new type, following the same convention. Every specialization exposes a `const` `operator()(const QString &)` that returns the parsed value or throws `ParseError` on failure, so generic code can treat `Parse<T>()(s)` uniformly regardless of `T`.

The numeric specializations route through two small helpers in `ParseInternals`: `parse_using_qlocale()` tries the `QLocale` conversion function first, then retries with the C locale before giving up (letting a file expressed in "C"-style numeric formatting parse correctly even under a different user locale), while `parse_using_qstring()` uses `QString`'s own base-aware conversion (used for non-base-10 integers, since `QLocale` has no concept of numeric base). `Int<Base, IntType>` exists so a base-N integer can be threaded through code that expects a plain integral type via its implicit conversion, while still using the base at parse time — the alternative being to pass the base explicitly to `Parse<int>`'s constructor.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::ParseError`](#gplatesutilsparseerror) | class | — | — | 0 | — |
| [`GPlatesUtils::ParseInternals::ParseWithLocale`](#gplatesutilsparseinternalsparsewithlocale) | class | — | — | 5 | — |
| [`GPlatesUtils::ParseInternals::ParseWithBase`](#gplatesutilsparseinternalsparsewithbase) | class | [`ParseWithLocale`](Parse.md) | — | 2 | — |
| [`GPlatesUtils::Parse<int>`](#gplatesutilsparseint) | struct | [`ParseInternals::ParseWithBase`](Parse.md) | `<>` | 0 | Template specialisation of Parse for int. |
| [`GPlatesUtils::Parse<unsigned int>`](#gplatesutilsparseunsigned-int) | struct | [`ParseInternals::ParseWithBase`](Parse.md) | `<>` | 0 | Template specialisation of Parse for unsigned int. |
| [`GPlatesUtils::Int`](#gplatesutilsint) | class | — | `<int Base, typename IntType = int>` | 0 | A wrapper around int to allow integers expressed in a base other than 10 to be parsed correctly. |
| [`GPlatesUtils::Parse<Int<Base, IntType> >`](#gplatesutilsparseintbase-inttype-) | struct | — | `<int Base, typename IntType>` | 0 | Template specialisation of Parse for Int\<Base, IntType\>. |
| [`GPlatesUtils::Parse<float>`](#gplatesutilsparsefloat) | struct | [`ParseInternals::ParseWithLocale`](Parse.md) | `<>` | 0 | Template specialisation of Parse for float. |
| [`GPlatesUtils::Parse<double>`](#gplatesutilsparsedouble) | struct | [`ParseInternals::ParseWithLocale`](Parse.md) | `<>` | 0 | Template specialisation of Parse for double. |
| [`GPlatesUtils::Parse<bool>`](#gplatesutilsparsebool) | struct | — | `<>` | 0 | Template specialisation of Parse for bool. |
| [`GPlatesUtils::Parse<const QString &>`](#gplatesutilsparseconst-qstring-) | struct | — | `<>` | 0 | Template specialisation of Parse for const QString &. |
| [`GPlatesUtils::Parse<QString>`](#gplatesutilsparseqstring) | struct | — | `<>` | 0 | Template specialisation of Parse for QString. |

## Members

### `GPlatesUtils::ParseError`

*None.*

### `GPlatesUtils::ParseInternals::ParseWithLocale`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `d_locale` | field | `QLocale` | protected | — |

### `GPlatesUtils::ParseInternals::ParseWithBase`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ParseWithBase( int base)` | constructor | `None` | protected | — |
| `d_base` | field | `int` | protected | — |

### `GPlatesUtils::Parse<int>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Parse( int base = 10)` | method | `None` | public | — |
| `operator()( const QString &s)` | operator | `int` | public | — |

### `GPlatesUtils::Parse<unsigned int>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Parse( int base = 10)` | method | `None` | public | — |
| `operator()( const QString &s)` | operator | `unsigned int` | public | — |

### `GPlatesUtils::Int`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Int( IntType value)` | constructor | `None` | public | — |
| `d_value` | field | `IntType` | private | — |

### `GPlatesUtils::Parse<Int<Base, IntType> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Parse()` | method | `None` | public | — |
| `operator()( const QString &s)` | operator | `Int<Base, IntType>` | public | — |
| `d_parse` | field | `Parse<IntType>` | private | — |

### `GPlatesUtils::Parse<float>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const QString &s)` | operator | `float` | public | — |

### `GPlatesUtils::Parse<double>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const QString &s)` | operator | `double` | public | — |

### `GPlatesUtils::Parse<bool>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const QString &s)` | operator | `bool` | public | — |

### `GPlatesUtils::Parse<const QString &>`

*None.*

### `GPlatesUtils::Parse<QString>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( const QString &s)` | operator | `QString` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_PARSE_H` | macro | `None` | — |
| `parse_using_qlocale( const QLocale &loc, const QString &s, FunctionType fn)` | function | `T` | — |
| `parse_using_qstring( const QString &s, FunctionType fn, int base)` | function | `T` | — |

## Notes

- `Parse<T>` is deliberately undefined for unspecialized `T`; using it without a matching specialization is a compile error, not a runtime one.
- `Parse<bool>` only recognizes the literal strings `"true"`/`"false"` (case-insensitive); anything else throws `ParseError`, so it does not accept `"1"`/`"0"` or other truthy forms.
- `Parse<int>`/`Parse<unsigned int>` only use `QLocale` for base 10; any other base always goes through `QString`'s conversion, since a non-decimal base combined with locale-specific digit grouping has no defined meaning in Qt5.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/XPath](XPath.md) | utils | 12 |
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 6 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 5 |
| [gui/CptColourPalette](../gui/CptColourPalette.md) | gui | 5 |
| [qt-widgets/ScalarField3DDepthLayersPage](../qt-widgets/ScalarField3DDepthLayersPage.md) | qt-widgets | 4 |
| [qt-widgets/TimeDependentRasterPage](../qt-widgets/TimeDependentRasterPage.md) | qt-widgets | 4 |
| [model/QualifiedXmlName](../model/QualifiedXmlName.md) | model | 3 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 2 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 2 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 2 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Parse.h
python scripts/gpq.py def GPlatesUtils::Parse<int> --body
python scripts/gpq.py uses Parse<int> --kind struct
python scripts/gpq.py hier Parse<int>
```
