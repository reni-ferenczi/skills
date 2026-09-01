# ReadErrorUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1460 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReadErrorUtils.h` | C++ | 77 |
| `src/file-io/ReadErrorUtils.cc` | C++ | 140 |

## Overview

`ReadErrorUtils` reshapes a flat `ReadErrorAccumulation::read_error_collection_type`
into forms convenient for reporting: `group_read_errors_by_file` buckets
errors by the source file's full name (via each error's `d_data_source`), and
`group_read_errors_by_type` buckets them by `ReadErrors::Description` code.
`build_summary_string` produces a single human-readable sentence — e.g.
"There were 2 failures, 1 warning" — counting `d_failures_to_begin` and
`d_terminating_errors` together as failures, plus recoverable errors and
warnings separately, with singular/plural wording handled explicitly for each
category. Both `ReadErrorAccumulationDialog` (GUI) and
`CliFeatureCollectionFileIO` (headless) use these to present the same error
accumulation consistently.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ReadErrorUtils::errors_by_file_map_type`](#gplatesfileioreaderrorutilserrors_by_file_map_type) | typedef | — | — | 0 | Map of Filename -\> Error collection for reporting all errors of a particular type for each file. |
| [`GPlatesFileIO::ReadErrorUtils::errors_by_file_map_const_iterator`](#gplatesfileioreaderrorutilserrors_by_file_map_const_iterator) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::ReadErrorUtils::errors_by_type_map_type`](#gplatesfileioreaderrorutilserrors_by_type_map_type) | typedef | — | — | 0 | Map of ReadErrors::Description -\> Error collection for reporting all errors of a particular type for each error code. |
| [`GPlatesFileIO::ReadErrorUtils::errors_by_type_map_const_iterator`](#gplatesfileioreaderrorutilserrors_by_type_map_const_iterator) | typedef | — | — | 0 | — |

## Members

### `GPlatesFileIO::ReadErrorUtils::errors_by_file_map_type`

*None.*

### `GPlatesFileIO::ReadErrorUtils::errors_by_file_map_const_iterator`

*None.*

### `GPlatesFileIO::ReadErrorUtils::errors_by_type_map_type`

*None.*

### `GPlatesFileIO::ReadErrorUtils::errors_by_type_map_const_iterator`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_READERRORUTILS_H` | macro | `None` | — |
| `build_summary_string( const ReadErrorAccumulation &read_errors)` | function | `QString` | Builds a string summarising the number of errors in each error category. |
| `group_read_errors_by_file( errors_by_file_map_type &errors_by_file, const ReadErrorAccumulation::read_error_collection_type &errors)` | function | `void` | Takes a read\_error\_collection\_type and creates a map of read\_error\_collection\_types, grouped by filename. |
| `group_read_errors_by_type( errors_by_type_map_type &errors_by_type, const ReadErrorAccumulation::read_error_collection_type &errors)` | function | `void` | Takes a read\_error\_collection\_type and creates a map of read\_error\_collection\_types, grouped by error type (the ReadErrors::Description enum). |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReadErrorAccumulationDialog](../qt-widgets/ReadErrorAccumulationDialog.md) | qt-widgets | 27 |
| [cli/CliFeatureCollectionFileIO](../cli/CliFeatureCollectionFileIO.md) | cli | 19 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReadErrorUtils.h
python scripts/gpq.py def GPlatesFileIO::ReadErrorUtils::errors_by_file_map_type --body
python scripts/gpq.py uses errors_by_file_map_type --kind typedef
```
