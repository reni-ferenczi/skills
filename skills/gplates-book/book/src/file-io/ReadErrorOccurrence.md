# ReadErrorOccurrence

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 672 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReadErrorOccurrence.h` | C++ | 293 |
| `src/file-io/ReadErrorOccurrence.cc` | C++ | 102 |

## Overview

This is the single record type that every GPlates file reader emits into a `ReadErrorAccumulation`, and its shape is dictated by two requirements that pull against each other. The reporting has to be uniform enough that one dialog can render errors from a PLATES rotation file, a shapefile, a GMT colour palette and an in-memory XML byte array side by side; but the readers themselves have wildly different notions of "where" a problem occurred and "what" the source even is. The answer here is to split an occurrence into four independent pieces — a `DataSource`, a `LocationInDataSource`, and two enum codes — and to keep the first two abstract.

`DataSource` and `LocationInDataSource` are pure-virtual stream-writers, deliberately minimal: a source can render itself as a short name, a full name and a format label, and a location can render itself, and that is the whole contract. `LocalFileDataSource` is the normal implementation, holding the filename and a `QFileInfo` so the short name is the basename and the full name the path; `GenericDataSource` covers sources that are not files at all — data received over the wire by `CommandServer`, or an in-memory buffer handed to `ArbitraryXmlReader` — by simply carrying the two strings it should print. `LineNumber` is the only location implementation in the tree, but the indirection means a reader for a format without line numbers (a raster band, a binary cache) can supply its own without touching the accumulation or the dialog. The `DataFormats::DataFormat` enum and its `data_format_to_str` mapping exist so that the format label is spelled consistently — the user sees "PLATES \"rotation\" format", not whatever each reader felt like writing.

The two enum codes are the other half of the design. `ReadErrorOccurrence` stores a `ReadErrors::Description` and a `ReadErrors::Result` — what went wrong and what GPlates did about it — and *never* a formatted message. Text is looked up at display time by `ReadErrorMessages`, from a table that pairs each code with a short and a full `QT_TR_NOOP` string, which is what keeps read-error text translatable and keeps the wording in one place instead of scattered through twenty readers. Adding a new failure mode therefore means adding an enumerator in `ReadErrors.h` *and* a row in `ReadErrorMessages.cc`; the header says so, and a missing row degrades to a placeholder string rather than a build error. The two `make_read_error_occurrence` overloads are the shorthand most readers actually call, wrapping the filename-plus-line-number and data-source-plus-line-number cases so a reader does not have to allocate the two `shared_ptr`s by hand.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::DataFormats::DataFormat`](#gplatesfileiodataformatsdataformat) | enum | — | — | 0 | — |
| [`GPlatesFileIO::DataSource`](#gplatesfileiodatasource) | struct | — | — | 2 | — |
| [`GPlatesFileIO::LocalFileDataSource`](#gplatesfileiolocalfiledatasource) | struct | [`DataSource`](ReadErrorOccurrence.md) | — | 0 | Use this DataSource derivation if the data source that triggered the read error is a local file. |
| [`GPlatesFileIO::GenericDataSource`](#gplatesfileiogenericdatasource) | struct | [`DataSource`](ReadErrorOccurrence.md) | — | 0 | This is a DataSource derivation that could be used for data sources other than local files. |
| [`GPlatesFileIO::LocationInDataSource`](#gplatesfileiolocationindatasource) | struct | — | — | 1 | — |
| [`GPlatesFileIO::LineNumber`](#gplatesfileiolinenumber) | struct | [`LocationInDataSource`](ReadErrorOccurrence.md) | — | 0 | Use this LocationInDataSource derivation if the data souurce that triggered the read error has a notion of line numbers. |
| [`GPlatesFileIO::ReadErrorOccurrence`](#gplatesfileioreaderroroccurrence) | struct | — | — | 0 | — |

## Members

### `GPlatesFileIO::DataFormats::DataFormat`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Gpml` | enumerator | `None` | — | — |
| `PlatesRotation` | enumerator | `None` | — | — |
| `PlatesLine` | enumerator | `None` | — | — |
| `Shapefile` | enumerator | `None` | — | — |
| `Gmap` | enumerator | `None` | — | — |
| `RasterImage` | enumerator | `None` | — | — |
| `ScalarField3D` | enumerator | `None` | — | — |
| `Cpt` | enumerator | `None` | — | — |
| `HellingerPick` | enumerator | `None` | — | — |
| `Unspecified` | enumerator | `None` | — | — |

### `GPlatesFileIO::DataSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~DataSource()` | destructor | `None` | public | — |
| `write_short_name( std::ostream &target)` | method | `void` | public | — |
| `write_full_name( std::ostream &target)` | method | `void` | public | — |
| `write_format( std::ostream &target)` | method | `void` | public | — |

### `GPlatesFileIO::LocalFileDataSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LocalFileDataSource( const QString &filename, DataFormats::DataFormat data_format)` | constructor | `None` | public | — |
| `write_short_name( std::ostream &target)` | method | `void` | public | — |
| `write_full_name( std::ostream &target)` | method | `void` | public | — |
| `write_format( std::ostream &target)` | method | `void` | public | — |
| `d_filename` | field | `QString` | private | — |
| `d_fileinfo` | field | `QFileInfo` | private | — |
| `d_data_format` | field | `DataFormats::DataFormat` | private | — |

### `GPlatesFileIO::GenericDataSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenericDataSource( DataFormats::DataFormat data_format, const std::string &short_name, const boost::optional<const std::string> &full_name = boost::none)` | constructor | `None` | public | GenericDataSource constructor. |
| `write_short_name( std::ostream &target)` | method | `void` | public | — |
| `write_full_name( std::ostream &target)` | method | `void` | public | — |
| `write_format( std::ostream &target)` | method | `void` | public | — |
| `d_data_format` | field | `DataFormats::DataFormat` | private | — |
| `d_short_name` | field | `std::string` | private | — |
| `d_full_name` | field | `std::string` | private | — |

### `GPlatesFileIO::LocationInDataSource`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~LocationInDataSource()` | destructor | `None` | public | — |
| `write( std::ostream &target)` | method | `void` | public | — |

### `GPlatesFileIO::LineNumber`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LineNumber( unsigned long line_num)` | constructor | `None` | public | — |
| `write( std::ostream &target)` | method | `void` | public | — |
| `d_line_num` | field | `unsigned long` | private | — |

### `GPlatesFileIO::ReadErrorOccurrence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ReadErrorOccurrence( boost::shared_ptr<DataSource> data_source, boost::shared_ptr<LocationInDataSource> location, ReadErrors::Description description, ReadErrors::Result result)` | constructor | `None` | public | Create a new ReadErrorOccurrence instance. |
| `write_short_name( std::ostream &target)` | method | `void` | public | — |
| `write_full_name( std::ostream &target)` | method | `void` | public | — |
| `d_data_source` | field | `boost::shared_ptr<DataSource>` | public | — |
| `d_location` | field | `boost::shared_ptr<LocationInDataSource>` | public | — |
| `d_description` | field | `ReadErrors::Description` | public | — |
| `d_result` | field | `ReadErrors::Result` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_READERROROCCURRENCE_H` | macro | `None` | — |
| `data_format_to_str( DataFormat data_format)` | function | `char` | — |
| `make_read_error_occurrence( const QString &filename, DataFormats::DataFormat data_format, unsigned long line_num, ReadErrors::Description description, ReadErrors::Result result)` | function | `ReadErrorOccurrence` | A convenience function to create a ReadErrorOccurrence for file read errors. |
| `make_read_error_occurrence( boost::shared_ptr<DataSource> data_source, unsigned long line_num, ReadErrors::Description description, ReadErrors::Result result)` | function | `ReadErrorOccurrence` | A convenience function to create a ReadErrorOccurrence for read errors from data sources that have line numbers. |

## Notes

Neither `d_data_source` nor `d_location` may be null — the constructor's Doxygen says so and nothing checks it, so a null slips through construction and crashes later in `write_short_name`, `write_full_name`, or in `ReadErrorUtils::group_read_errors_by_file`, which dereferences the data source. Both are `boost::shared_ptr`, so occurrences are cheap to copy and copies share one source object; a `LocalFileDataSource` created for one error is typically shared by every error from that file. That sharing is also why the source objects must be immutable in practice: they are captured at report time and read much later, potentially after the file has been closed or deleted.

The two `write_*` methods on `ReadErrorOccurrence` and the identically named ones on `DataSource` are not interchangeable, and the difference is load-bearing. `ReadErrorOccurrence::write_full_name` composes source, `":"`, location and format — the per-error line the dialog shows. `group_read_errors_by_file` deliberately calls `d_data_source->write_full_name` *alone*, without the location, and uses the resulting string as the map key; that is what makes all errors from one file group together instead of one group per line number. Any change to `LocalFileDataSource::write_full_name` therefore changes the grouping key, not just the displayed text.

`data_format_to_str` switches over `DataFormats::DataFormat` with no `default` and initialises its result to `NULL`. Adding an enumerator without adding a case returns a null `const char *` that is then streamed, so rely on the compiler's unhandled-enumerator warning here rather than on a runtime fallback. Note also that `GenericDataSource` copies its strings into `std::string` members while `LocalFileDataSource` keeps a `QString` plus a `QFileInfo`; the `QFileInfo` is constructed once at report time, so the short name reflects the path as it was when the error was recorded.

`ReadErrors::Severity` is not stored on an occurrence at all. Severity comes solely from which `ReadErrorAccumulation` vector the reader pushed into, so the same `Description`/`Result` pair can legitimately appear as a warning in one reader and a recoverable error in another.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesRotationFormatReader](PlatesRotationFormatReader.md) | file-io | 59 |
| [file-io/OgrReader](OgrReader.md) | file-io | 54 |
| [qt-widgets/ReadErrorAccumulationDialog](../qt-widgets/ReadErrorAccumulationDialog.md) | qt-widgets | 30 |
| [file-io/CptReader](CptReader.md) | file-io | 26 |
| [file-io/PlatesLineFormatReader](PlatesLineFormatReader.md) | file-io | 15 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 14 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 12 |
| [file-io/GmapReader](GmapReader.md) | file-io | 11 |
| [file-io/GpmlReaderUtils](GpmlReaderUtils.md) | file-io | 9 |
| [file-io/GdalUtils](GdalUtils.md) | file-io | 8 |
| [file-io/GpmlReader](GpmlReader.md) | file-io | 8 |
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 8 |
| [opengl/GLScalarField3DGenerator](../opengl/GLScalarField3DGenerator.md) | opengl | 7 |
| [file-io/HellingerReader](HellingerReader.md) | file-io | 6 |
| [file-io/RasterReader](RasterReader.md) | file-io | 4 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 4 |
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 4 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 4 |
| [file-io/GdalRasterReader](GdalRasterReader.md) | file-io | 2 |
| [file-io/ReadErrorAccumulation](ReadErrorAccumulation.md) | file-io | 2 |

*... and 6 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReadErrorOccurrence.h
python scripts/gpq.py def GPlatesFileIO::GenericDataSource --body
python scripts/gpq.py uses GenericDataSource --kind struct
python scripts/gpq.py hier GenericDataSource
```
