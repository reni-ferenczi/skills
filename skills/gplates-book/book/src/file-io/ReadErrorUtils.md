# ReadErrorUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1460 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReadErrorUtils.h` | C++ | 77 |
| `src/file-io/ReadErrorUtils.cc` | C++ | 140 |

## Overview

[[[PROSE overview unit=file-io/ReadErrorUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/ReadErrorUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
