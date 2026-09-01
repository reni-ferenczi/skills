# ReadErrorOccurrence

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 672 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReadErrorOccurrence.h` | C++ | 293 |
| `src/file-io/ReadErrorOccurrence.cc` | C++ | 102 |

## Overview

[[[PROSE overview unit=file-io/ReadErrorOccurrence tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/ReadErrorOccurrence tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
