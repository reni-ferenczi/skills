# ReadErrorAccumulation

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1264 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReadErrorAccumulation.h` | C++ | 154 |

## Overview

Every file reader in GPlates takes a `ReadErrorAccumulation &` as an out-parameter and reports problems into it rather than throwing. That is the central design decision this tiny struct encodes: loading a geological data file is expected to be partially successful, so a reader must be able to say "I skipped this feature and carried on" and still return a usable feature collection. The accumulation is the bucket those reports land in, and its four vectors are not a taxonomy of causes but a taxonomy of *consequences* — the Doxygen on each field spells out exactly what the reader is asserting by choosing it. A warning means nothing was lost; a recoverable error means some bounded chunk of data was discarded and reading continued; a terminating error means reading stopped part-way, so the collection is truncated; a failure to begin means the parser never got as far as the data, so nothing was loaded at all. Choosing the wrong vector is the main way to get this wrong, because downstream code branches on the distinction and the user is shown different text.

An accumulation aggregates across files as well as within one. A reader typically fills a local accumulation for the file it is parsing, and the caller folds it into a longer-lived one with `accumulate` — which is why the per-file "there can only be one terminating error" and "only one failure to begin" invariants in the Doxygen apply to a single file's worth of reporting, not to the accumulation itself, which may hold many. `GPlatesAppLogic::FeatureCollectionFileIO` is the usual funnel: after each load it calls `emit_handle_read_errors_signal`, which tests `is_empty()` and emits `handle_read_errors` only when there is something to say, so the errors dialog never pops up for a clean load. `most_severe_error_type` exists for exactly that consumer — it collapses the four vectors into a single `ReadErrors::Severity` so the window can decide how loudly to complain, and it is documented as being for `ViewportWindow::handle_read_errors()`.

The individual reports are `ReadErrorOccurrence` values, which carry a data source, a location and a pair of enum codes rather than a formatted message; `ReadErrorMessages` turns those codes into translated text at display time, and `ReadErrorUtils` regroups a collection by file or by error type for `ReadErrorAccumulationDialog`, which keeps its own accumulation and grows it across successive loads.

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

The four vectors are public fields with no accessors, and readers push onto them directly — there is no method that classifies an occurrence for you. Severity is decided entirely at the call site by which vector the reader chooses, so classification consistency across readers is a convention, not something the type enforces.

`accumulate` appends and never de-duplicates, so folding the same source accumulation in twice yields duplicate entries, and re-reading a file that keeps reporting the same problem grows the destination without bound. The long-lived accumulation inside `ReadErrorAccumulationDialog` is cleared explicitly rather than per-load, which is what makes it a running log across successive file loads.

Nothing here is copy-on-write or reference-counted at the accumulation level: `ReadErrorAccumulation` is a plain value with `std::vector` members, so copying one deep-copies the vectors. The elements are cheap to copy despite that, because `ReadErrorOccurrence` holds its data source and location behind `boost::shared_ptr`, so those objects are shared, not cloned — see the notes on `ReadErrorOccurrence` for what that implies about lifetimes.

There is no locking. An accumulation is intended to be filled by one reader on one thread and then handed on; `is_empty()`, `size()` and `most_severe_error_type()` all recompute from the four vectors on each call, so do not treat them as cached state while another thread might be appending.

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
