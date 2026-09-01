# File

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 514 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/controls/File.h` | C++ | 64 |
| `src/deprecated/controls/File.cc` | C++ | 704 |

## Overview

Deprecated file I/O control functions for opening, loading, importing, and saving GPlates data files. The public interface provides `OpenData()` for native GPML files, `LoadRotation()` for PLATES rotation files, `ImportData()` for non-native formats, `SaveData()` to write GPML output, and `Quit()` to exit the application. Internal helpers include file-format detection based on extension and magic bytes, conversion functions between PLATES parser types and GPlates maths types, and a visitor for building drawable data maps from geological data.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::AddGeoDataToDrawableMap`](#anonymousaddgeodatatodrawablemap) | class | — | — | 0 | — |
| [`DataFormats::data_format`](#dataformatsdata_format) | enum | — | — | 0 | — |
| [`GPlatesControls::File::DataFormats::data_format`](#gplatescontrolsfiledataformatsdata_format) | enum | — | — | 0 | — |

## Members

### `(anonymous)::AddGeoDataToDrawableMap`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AddGeoDataToDrawableMap(Data::DrawableMap_type* map)` | constructor | `None` | public | — |
| `operator()(GeologicalData* data)` | operator | `void` | public | — |
| `_map` | field | `Data::DrawableMap_type` | private | — |

### `DataFormats::data_format`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ERROR` | enumerator | `None` | — | — |
| `UNKNOWN` | enumerator | `None` | — | — |
| `GPML` | enumerator | `None` | — | — |
| `PLATES` | enumerator | `None` | — | — |
| `NETCDF` | enumerator | `None` | — | — |

### `GPlatesControls::File::DataFormats::data_format`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `ConvertPlatesParserLatLonToMathsLatLon( const PlatesParser::LatLonPoint& point)` | function | `GPlatesMaths::LatLonPoint` | Remove this definition, since it is a duplicate of a function in PlatesPostParseTranslator. |
| `OpenFileErrorMessage(const std::string &fname, const char *fail_result_msg)` | function | `void` | — |
| `HandleGPMLFile(const std::string& filename)` | function | `void` | — |
| `ConvertDataGroupToDrawableDataMap(DataGroup* data)` | function | `void` | — |
| `HandlePLATESFile(const std::string& filename)` | function | `void` | — |
| `NATIVE_DATA_FORMAT_TESTS` | variable | `DataFormatTest` | — |
| `NONNATIVE_DATA_FORMAT_TESTS` | variable | `DataFormatTest` | — |
| `determineDataFormat(const std::string &filename, DataFormatTest *tests, size_t num_tests)` | function | `enum data_format` | — |
| `extensionMatches(const std::string &fname, const std::string &ext)` | function | `bool` | — |
| `magicMatches(const std::string &fname, const char *magic, int n)` | function | `bool` | — |
| `testGPML(const std::string &filename)` | function | `enum data_format` | — |
| `testPLATES(const std::string &filename)` | function | `enum data_format` | — |
| `ConvertPlatesParserAngleToGPlatesMathsAngle(const fpdata_t &pp_angle)` | function | `GPlatesMaths::real_t` | Ultimately, it should \*all\* go. |
| `ConvertPlatesParserLLPToGPlatesMathsPOS(PlatesParser::LatLonPoint pp_llp)` | function | `GPlatesMaths::PointOnSphere` | — |
| `ConvertPlatesParserFinRotToGPlatesMathsFinRot(const PlatesParser::FiniteRotation &pp_fin_rot)` | function | `GPlatesMaths::FiniteRotation` | — |
| `ConvertPlatesParserRotSeqToGPlatesMathsRotSeq(const PlatesParser::RotationSequence &pp_rot_seq)` | function | `GPlatesMaths::RotationSequence` | — |
| `ConvertPlatesRotationDataToRotationMap(const PlatesParser::PlatesRotationData &data)` | function | `void` | — |
| `_GPLATES_CONTROLS_FILE_H_` | macro | `None` | — |
| `OpenData(const std::string& filepath)` | function | `void` | Open a native GPlates data file. |
| `LoadRotation(const std::string& filepath)` | function | `void` | Load a PLATES rotation file. |
| `ImportData(const std::string &filepath)` | function | `void` | Import a non-native data file. |
| `SaveData(const std::string& filepath)` | function | `void` | Write the current data to a GPML file. |
| `Quit(const GPlatesGlobal::integer_t& exit_status)` | function | `void` | Exit GPlates. |

## Notes

The code contains marked TODOs indicating technical debt: `ConvertPlatesParserLatLonToMathsLatLon` is noted as a duplicate of a function in `PlatesPostParseTranslator`, and `ConvertPlatesParserAngleToGPlatesMathsAngle` should ultimately be removed. File I/O errors are presented to users via `Dialogs::ErrorMessage()` rather than propagated as exceptions.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/deprecated/MainWindow](../../gui/deprecated/MainWindow.md) | gui | 12 |
| [maths/deprecated/PolylineIntersections_test](../../maths/deprecated/PolylineIntersections_test.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/controls/File.h
python scripts/gpq.py def (anonymous)::AddGeoDataToDrawableMap --body
python scripts/gpq.py uses AddGeoDataToDrawableMap --kind class
python scripts/gpq.py hier AddGeoDataToDrawableMap
```
