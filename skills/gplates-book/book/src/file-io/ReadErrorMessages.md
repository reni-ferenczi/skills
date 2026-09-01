# ReadErrorMessages

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1318 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReadErrorMessages.h` | C++ | 63 |
| `src/file-io/ReadErrorMessages.cc` | C++ | 721 |

## Overview

`ReadErrorMessages` turns the `ReadErrors::Description` and `ReadErrors::Result`
enum codes used throughout the file readers into user-facing, translatable
text. Almost all of its 721-line `.cc` is two static tables,
`description_table` and `result_table` (sourced from the project's
`ReadErrorMessages` wiki page), each pairing an enum value with plain-`char*`
short and full message text. `get_short_description_as_string`,
`get_full_description_as_string` and `get_result_as_string` lazily build an
`std::map` from the matching table on first use — running each string through
`QObject::tr()` at that point, not at table-definition time, so Qt's
translation mechanism sees them — and cache the map in a function-local
`static` for subsequent lookups.

The code was, per its own header comment, refactored out of
`ReadErrorAccumulationDialog` specifically so the command-line (non-GUI)
build could format the same read-error messages without depending on that
Qt dialog; `CliFeatureCollectionFileIO` is the corresponding CLI-side
consumer.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::description_map_type`](#anonymousdescription_map_type) | typedef | — | — | 0 | Maps used for error text lookup. |
| [`(anonymous)::description_map_const_iterator`](#anonymousdescription_map_const_iterator) | typedef | — | — | 0 | — |
| [`(anonymous)::result_map_type`](#anonymousresult_map_type) | typedef | — | — | 0 | — |
| [`(anonymous)::result_map_const_iterator`](#anonymousresult_map_const_iterator) | typedef | — | — | 0 | — |
| [`(anonymous)::ReadErrorDescription`](#anonymousreaderrordescription) | struct | — | — | 0 | — |
| [`(anonymous)::ReadErrorResult`](#anonymousreaderrorresult) | struct | — | — | 0 | — |

## Members

### `(anonymous)::description_map_type`

*None.*

### `(anonymous)::description_map_const_iterator`

*None.*

### `(anonymous)::result_map_type`

*None.*

### `(anonymous)::result_map_const_iterator`

*None.*

### `(anonymous)::ReadErrorDescription`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `code` | field | `GPlatesFileIO::ReadErrors::Description` | public | — |
| `short_text` | field | `char` | public | — |
| `full_text` | field | `char` | public | — |

### `(anonymous)::ReadErrorResult`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `code` | field | `GPlatesFileIO::ReadErrors::Result` | public | — |
| `text` | field | `char` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NUM_ELEMS` | macro_function | `(sizeof(a) / sizeof((a)[0]))` | — |
| `description_table` | variable | `ReadErrorDescription` | This table is sourced from http://trac.gplates.org/wiki/ReadErrorMessages . |
| `result_table` | variable | `ReadErrorResult` | This table is sourced from http://trac.gplates.org/wiki/ReadErrorMessages . |
| `GPLATES_FILE_IO_READERRORMESSAGES_H` | macro | `None` | — |
| `get_short_description_as_string( ReadErrors::Description code)` | function | `QString` | Converts a ReadErrors::Description enum to a translated QString (short form). |
| `get_full_description_as_string( ReadErrors::Description code)` | function | `QString` | Converts a ReadErrors::Description enum to a translated QString (full text). |
| `get_result_as_string( ReadErrors::Result code)` | function | `QString` | Converts a ReadErrors::Result enum to a translated QString. |

## Notes

A code missing from its table is not an error: each lookup function falls
back to a fixed "not found" placeholder string rather than asserting or
throwing. Adding a new `ReadErrors::Description` or `ReadErrors::Result` value
means adding a row to the corresponding table here — the enum alone produces
no text.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReadErrorAccumulationDialog](../qt-widgets/ReadErrorAccumulationDialog.md) | qt-widgets | 9 |
| [cli/CliFeatureCollectionFileIO](../cli/CliFeatureCollectionFileIO.md) | cli | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReadErrorMessages.h
python scripts/gpq.py def (anonymous)::ReadErrorDescription --body
python scripts/gpq.py uses ReadErrorDescription --kind struct
python scripts/gpq.py hier ReadErrorDescription
```
