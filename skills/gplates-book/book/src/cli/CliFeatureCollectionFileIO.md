# CliFeatureCollectionFileIO

[Book TOC](../../TOC.md) · [cli](../../components/cli.md) · cluster Community 200 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/cli/CliFeatureCollectionFileIO.h` | C++ | 239 |
| `src/cli/CliFeatureCollectionFileIO.cc` | C++ | 392 |

## Overview

[[[PROSE overview unit=cli/CliFeatureCollectionFileIO tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCli::FeatureCollectionFileIO`](#gplatesclifeaturecollectionfileio) | class | — | — | 0 | This is a replacement for the FeatureCollectionFileIO in namespace GPlatesAppLogic in that it doesn't require a FeatureCollectionFileState. |

## Members

### `GPlatesCli::FeatureCollectionFileIO`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `feature_collection_file_seq_type` | typedef | `std::vector<GPlatesFileIO::File::Reference::non_null_ptr_type>` | public | Typedef for a sequence of files each containing a feature collection. |
| `FeatureCollectionFileIO( GPlatesModel::ModelInterface &model, const boost::program_options::variables_map &command_line_variables)` | constructor | `None` | public | model will be used to create feature collections and command\_line\_variables will be used to search for filenames specified on the command-line. |
| `load_files( const std::string &option_name, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | method | `feature_collection_file_seq_type` | public | Load feature collection files using filenames specified via the command-line option option\_name. |
| `extract_feature_collections( std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref> &feature_collections, FeatureCollectionFileIO::feature_collection_file_seq_type &files)` | method | `void` | public | Extracts the feature collections from their containing File objects. |
| `report_load_file_errors( const GPlatesFileIO::ReadErrorAccumulation &read_errors)` | method | `void` | public | Reports any file read errors accumulated into read\_errors. |
| `save_file( const GPlatesFileIO::FileInfo &file_info, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Write the feature collection associated to a file described by file\_info. |
| `SAVE_FILE_TYPE_GPML` | field | `std::string` | public | Values specified by user on command-line for the save file type. |
| `SAVE_FILE_TYPE_GPMLZ` | field | `std::string` | public | — |
| `SAVE_FILE_TYPE_PLATES_LINE` | field | `std::string` | public | — |
| `SAVE_FILE_TYPE_PLATES_ROTATION` | field | `std::string` | public | — |
| `SAVE_FILE_TYPE_SHAPEFILE` | field | `std::string` | public | — |
| `SAVE_FILE_TYPE_GMT` | field | `std::string` | public | — |
| `SAVE_FILE_TYPE_GMAP` | field | `std::string` | public | — |
| `get_save_file_format( const std::string &save_file_type)` | method | `GPlatesFileIO::FeatureCollectionFileFormat::Format` | public | Returns the save filename by changing the extension of file\_info using the save file format of save\_file\_format. |
| `get_save_file_info( const QString &filename_no_extension, GPlatesFileIO::FeatureCollectionFileFormat::Format save_file_format)` | method | `GPlatesFileIO::FileInfo` | public | Returns the save filename by appending the filename extension determined by save\_file\_format to filename\_no\_extension. |
| `get_save_file_info( const QString &filename_no_extension, const std::string &save_file_type)` | method | `GPlatesFileIO::FileInfo` | public | Returns the save filename by appending the filename extension determined by save\_file\_type to filename\_no\_extension. |
| `get_save_file_info( const GPlatesFileIO::FileInfo &file_info, GPlatesFileIO::FeatureCollectionFileFormat::Format save_file_format, const QString &filename_prefix = "", const QString &filename_suffix = "")` | method | `GPlatesFileIO::FileInfo` | public | Returns the save filename by changing the extension of file\_info using the save file format of save\_file\_format. |
| `get_save_file_info( const GPlatesFileIO::FileInfo &file_info, const std::string &save_file_type, const QString &filename_prefix = "", const QString &filename_suffix = "")` | method | `GPlatesFileIO::FileInfo` | public | Returns the save filename by changing the extension of file\_info using the save file format of save\_file\_format. |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | Used to create feature collections when loading files. |
| `d_file_format_registry` | field | `GPlatesFileIO::FeatureCollectionFileFormat::Registry` | private | A registry of the file formats for reading/writing feature collections. |
| `d_command_line_variables` | field | `boost::program_options::variables_map` | private | The command-line variables are stored here. |
| `load_feature_collections( const std::vector<std::string> &filenames, feature_collection_file_seq_type &files, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | method | `void` | private | — |
| `report_load_file_error_by_collection_type( const QString &error_header, const GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors)` | method | `void` | private | — |
| `report_load_file_error_by_file( const GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors)` | method | `void` | private | — |
| `report_load_file_error_by_error_type( const GPlatesFileIO::ReadErrorAccumulation::read_error_collection_type &errors)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `remove_filename_extension( const QString &filename)` | function | `QString` | Removes filename extension. |
| `prepend_filename_prefix( QString &filename, const QString &filename_prefix)` | function | `void` | — |
| `append_filename_suffix( QString &filename, const QString &filename_suffix)` | function | `void` | — |
| `append_filename_extension( QString &filename, const QString &filename_extension)` | function | `void` | — |
| `SAVE_FILE_TYPE_GPML` | variable | `std::string` | — |
| `SAVE_FILE_TYPE_GPMLZ` | variable | `std::string` | — |
| `SAVE_FILE_TYPE_PLATES_LINE` | variable | `std::string` | — |
| `SAVE_FILE_TYPE_PLATES_ROTATION` | variable | `std::string` | — |
| `SAVE_FILE_TYPE_SHAPEFILE` | variable | `std::string` | — |
| `SAVE_FILE_TYPE_GMT` | variable | `std::string` | — |
| `SAVE_FILE_TYPE_GMAP` | variable | `std::string` | — |
| `GPLATES_CLI_CLILOADFEATURECOLLECTIONS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=cli/CliFeatureCollectionFileIO tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [cli/CliAssignPlateIdsCommand](CliAssignPlateIdsCommand.md) | cli | 45 |
| [cli/CliReconstructCommand](CliReconstructCommand.md) | cli | 28 |
| [cli/CliConvertFileFormatCommand](CliConvertFileFormatCommand.md) | cli | 27 |
| [cli/CliRelativeTotalRotation](CliRelativeTotalRotation.md) | cli | 10 |
| [cli/CliStageRotationCommand](CliStageRotationCommand.md) | cli | 10 |
| [cli/CliEquivalentTotalRotation](CliEquivalentTotalRotation.md) | cli | 9 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/cli/CliFeatureCollectionFileIO.h
python scripts/gpq.py def GPlatesCli::FeatureCollectionFileIO --body
python scripts/gpq.py uses FeatureCollectionFileIO --kind class
python scripts/gpq.py hier FeatureCollectionFileIO
```
