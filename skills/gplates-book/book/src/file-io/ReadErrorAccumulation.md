# ReadErrorAccumulation

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1264 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReadErrorAccumulation.h` | C++ | 154 |

## Overview

[[[PROSE overview unit=file-io/ReadErrorAccumulation tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ReadErrorAccumulation`](#gplatesfileioreaderroraccumulation) | struct | — | — | 0 | — |

## Members

### `GPlatesFileIO::ReadErrorAccumulation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_error_collection_type` | typedef | `std::vector<ReadErrorOccurrence>` | public | — |
| `read_error_collection_const_iterator` | typedef | `read_error_collection_type::const_iterator` | public | — |
| `size_type` | typedef | `read_error_collection_type::size_type` | public | — |
| `ReadErrorAccumulation()` | constructor | `None` | public | — |
| `d_warnings` | field | `read_error_collection_type` | public | A warning is the result of a problem which doesn't cause data loss (when the data is being loaded), but which the user should nevertheless be notified of. |
| `d_recoverable_errors` | field | `read_error_collection_type` | public | After a recoverable error, reading from file can continue, but some amount of data (a feature? a property of a feature? etc.) simply had to be discarded because it was hopelessly malformed. |
| `d_terminating_errors` | field | `read_error_collection_type` | public | After a terminating error, reading from file (or other data source) simply cannot continue. |
| `d_failures_to_begin` | field | `read_error_collection_type` | public | A failure to begin indicates a fatal error before the parser could access any data from the file, e.g. the file does not exist. |
| `is_empty()` | method | `bool` | public | Returns whether the ReadErrorAccumulation contains no errors or warnings. |
| `size()` | method | `size_type` | public | The combined size of all read error collections in this ReadErrorAccumulation. |
| `most_severe_error_type()` | method | `ReadErrors::Severity` | public | Returns the most severe type of warning/error found in this accumulation. |
| `clear()` | method | `void` | public | — |
| `accumulate( const ReadErrorAccumulation &errors)` | method | `void` | public | Appends warnings and errors of errors into 'this'. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_READERRORACCUMULATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/ReadErrorAccumulation tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 91 |
| [qt-widgets/ReadErrorAccumulationDialog](../qt-widgets/ReadErrorAccumulationDialog.md) | qt-widgets | 85 |
| [file-io/OgrReader](OgrReader.md) | file-io | 48 |
| [file-io/CptReader](CptReader.md) | file-io | 42 |
| [file-io/ReadErrorUtils](ReadErrorUtils.md) | file-io | 34 |
| [file-io/PlatesRotationFormatReader](PlatesRotationFormatReader.md) | file-io | 29 |
| [file-io/PlatesLineFormatReader](PlatesLineFormatReader.md) | file-io | 27 |
| [qt-widgets/TimeDependentRasterPage](../qt-widgets/TimeDependentRasterPage.md) | qt-widgets | 21 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 20 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 18 |
| [qt-widgets/ScalarField3DDepthLayersPage](../qt-widgets/ScalarField3DDepthLayersPage.md) | qt-widgets | 18 |
| [cli/CliFeatureCollectionFileIO](../cli/CliFeatureCollectionFileIO.md) | cli | 15 |
| [gui/ColourPaletteUtils](../gui/ColourPaletteUtils.md) | gui | 15 |
| [gui/TopologySectionsTable](../gui/TopologySectionsTable.md) | gui | 15 |
| [file-io/HellingerReader](HellingerReader.md) | file-io | 14 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 12 |
| [file-io/GpmlReaderUtils](GpmlReaderUtils.md) | file-io | 12 |
| [property-values/GmlFile](../property-values/GmlFile.md) | property-values | 11 |
| [file-io/ArbitraryXmlReader](ArbitraryXmlReader.md) | file-io | 10 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 10 |

*... and 88 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReadErrorAccumulation.h
python scripts/gpq.py def GPlatesFileIO::ReadErrorAccumulation --body
python scripts/gpq.py uses ReadErrorAccumulation --kind struct
python scripts/gpq.py hier ReadErrorAccumulation
```
