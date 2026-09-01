# FeatureCollectionFileFormatRegistry

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 474 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/FeatureCollectionFileFormatRegistry.h` | C++ | 360 |
| `src/file-io/FeatureCollectionFileFormatRegistry.cc` | C++ | 976 |

## Overview

[[[PROSE overview unit=file-io/FeatureCollectionFileFormatRegistry tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FeatureCollectionFileFormat::(anonymous)::FileMagic`](#gplatesfileiofeaturecollectionfileformatanonymousfilemagic) | enum | — | — | 0 | — |
| [`GPlatesFileIO::FeatureCollectionFileFormat::Registry`](#gplatesfileiofeaturecollectionfileformatregistry) | class | `boost::noncopyable` | — | 0 | Stores information concerning feature collection file formats and reading/writing to/from them. |

## Members

### `GPlatesFileIO::FeatureCollectionFileFormat::(anonymous)::FileMagic`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FILE_MAGIC_UNKNOWN` | enumerator | `None` | — | — |
| `FILE_MAGIC_XML` | enumerator | `None` | — | — |
| `FILE_MAGIC_GZIP` | enumerator | `None` | — | — |

### `GPlatesFileIO::FeatureCollectionFileFormat::Registry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `is_file_format_function_type` | typedef | `boost::function<bool (const QFileInfo&, const QString &)>` | public | Convenience typedef for a function that determines if a specified file format is recognised. |
| `read_feature_collection_function_type` | typedef | `boost::function< void ( File::Reference &, ReadErrorAccumulation &, bool &)>` | public | Convenience typedef for a function that reads a feature collection from a file. |
| `create_feature_collection_writer_function_type` | typedef | `boost::function< boost::shared_ptr<GPlatesModel::ConstFeatureVisitor> ( File::Reference &)>` | public | Convenience typedef for a function that creates a feature visitor that writes features to a file. |
| `Registry( bool register_default_file_formats_ = true)` | constructor | `None` | public | Constructor. |
| `register_default_file_formats()` | method | `void` | public | Registers information about the default feature collection file formats. |
| `register_file_format( Format file_format, const QString &short_description, const std::vector<QString> &filename_extensions, const classifications_type &feature_classification, const is_file_format_function_type &is_file_format_function, const boost::optional<read_feature_collection_function_type> &read_feature_collect ...` | method | `void` | public | Stores information about the given file\_format. |
| `unregister_file_format( Format file_format)` | method | `void` | public | Unregisters the specified file format. |
| `get_registered_file_formats()` | method | `std::vector<Format>` | public | Returns a list of all registered file formats. |
| `get_short_description` | field | `QString` | public | Returns a short description of the specified file\_format. |
| `get_primary_filename_extension( Format file_format)` | method | `QString` | public | Returns the primary filename extension associated with file\_format. |
| `get_all_filename_extensions_for_format` | field | `std::vector<QString>` | public | Returns the primary and alternative filename extensions associated with file\_format. |
| `get_all_filename_extensions( std::vector<QString> &filename_extensions)` | method | `void` | public | Returns the primary and alternative filename extensions associated with all registered file formats. |
| `get_feature_classification( Format file_format)` | method | `classifications_type` | public | Returns the classification of features that the specified file format can read/write. |
| `get_file_format( const QFileInfo& file_info)` | method | `boost::optional<Format>` | public | Determine the feature collection file format of the file described by file\_info. |
| `does_file_format_support_reading( Format file_format)` | method | `bool` | public | Returns true if the specified file format supports \*reading\* feature collections from files. |
| `does_file_format_support_writing( Format file_format)` | method | `bool` | public | Returns true if the specified file format supports \*writing\* feature collections to files. |
| `read_feature_collection( File::Reference &file_ref, ReadErrorAccumulation &read_errors, boost::optional<bool &> contains_unsaved_changes = boost::none)` | method | `void` | public | Reads features from file file\_ref into the file's feature collection. to one or more features after reading from file (eg, to conform to GPGIM). |
| `write_feature_collection( File::Reference &file_ref)` | method | `void` | public | Writes features to the specified file file\_ref. |
| `get_default_configuration` | field | `boost::optional<Configuration::shared_ptr_to_const_type>` | public | Returns the default configuration options for the specified file format. |
| `set_default_configuration( Format file_format, const Configuration::shared_ptr_to_const_type &default_configuration)` | method | `void` | public | Sets the default configuration options for the specified file format. |
| `FileFormatInfo` | struct | `None` | private | — |
| `file_format_info_map_type` | typedef | `std::map<Format, FileFormatInfo>` | private | — |
| `d_file_format_info_map` | field | `file_format_info_map_type` | private | Stores a struct of information for each file format. |
| `get_file_format_info` | field | `FileFormatInfo` | private | Returns file format info for specified file format, otherwise throws FileFormatNotSupportedException. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `identify_gpml_or_gpmlz_by_magic_number( const QFileInfo& file_info)` | function | `boost::optional<FileMagic>` | Returns file type (or FILE\_MAGIC\_UNKNOWN if not recognised), or boost::none if unable to open file for reading. |
| `FILE_FORMAT_EXT_GPML` | variable | `QString` | Filename extensions for the various file formats. |
| `FILE_FORMAT_EXT_GPMLZ` | variable | `QString` | — |
| `FILE_FORMAT_EXT_GPMLZ_ALTERNATIVE` | variable | `QString` | — |
| `FILE_FORMAT_EXT_PLATES4_LINE` | variable | `QString` | — |
| `FILE_FORMAT_EXT_PLATES4_LINE_ALTERNATIVE` | variable | `QString` | — |
| `FILE_FORMAT_EXT_PLATES4_ROTATION` | variable | `QString` | — |
| `FILE_FORMAT_EXT_GPLATES_ROTATION` | variable | `QString` | — |
| `FILE_FORMAT_EXT_SHAPEFILE` | variable | `QString` | — |
| `FILE_FORMAT_EXT_OGRGMT` | variable | `QString` | — |
| `FILE_FORMAT_EXT_GEOJSON` | variable | `QString` | — |
| `FILE_FORMAT_EXT_GEOJSON_ALTERNATIVE` | variable | `QString` | — |
| `FILE_FORMAT_EXT_GEOPACKAGE` | variable | `QString` | — |
| `FILE_FORMAT_EXT_WRITE_ONLY_XY_GMT` | variable | `QString` | — |
| `FILE_FORMAT_EXT_GMAP` | variable | `QString` | — |
| `FILE_FORMAT_EXT_GSML` | variable | `QString` | — |
| `file_name_ends_with( const QFileInfo &file_info, const QString &suffix)` | function | `bool` | Returns true if the filename of file\_info ends with suffix. |
| `is_gpml_format_file( const QFileInfo &file_info, const QString &filename_extension)` | function | `bool` | — |
| `is_gpmlz_format_file( const QFileInfo &file_info, const QString &filename_extension)` | function | `bool` | — |
| `ogr_read_feature_collection( File::Reference &file_ref, const Registry &file_format_registry, Format file_format, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | function | `void` | Reads an OGR-supported feature collection. |
| `gplates_rotation_read_feature_collection( File::Reference &file_ref, const Registry &file_format_registry, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | function | `void` | Reads a GPlates rotation (".grot") feature collection. |
| `gsml_read_feature_collection( File::Reference &file_ref, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | function | `void` | Reads a GSML feature collection. |
| `create_gpml_feature_collection_writer( File::Reference &file_ref)` | function | `boost::shared_ptr<GPlatesModel::ConstFeatureVisitor>` | Creates a GPML feature visitor writer. |
| `create_gpmlz_feature_collection_writer( File::Reference &file_ref)` | function | `boost::shared_ptr<GPlatesModel::ConstFeatureVisitor>` | Creates a GPMLZ feature visitor writer. |
| `create_plates_line_feature_collection_writer( File::Reference &file_ref)` | function | `boost::shared_ptr<GPlatesModel::ConstFeatureVisitor>` | Creates a PLATES4\_LINE feature visitor writer. |
| `create_plates_rotation_feature_collection_writer( File::Reference &file_ref)` | function | `boost::shared_ptr<GPlatesModel::ConstFeatureVisitor>` | Creates a PLATES4\_ROTATION feature visitor writer. |
| `create_gplates_rotation_feature_collection_writer( File::Reference &file_ref)` | function | `boost::shared_ptr<GPlatesModel::ConstFeatureVisitor>` | Creates a GPlates rotation (".grot") file writer. |
| `create_ogr_feature_collection_writer( File::Reference &file_ref, const Registry &file_format_registry, Format file_format)` | function | `boost::shared_ptr<GPlatesModel::ConstFeatureVisitor>` | Creates a feature visitor writer for OGR-supported file formats. |
| `create_write_only_xy_gmt_feature_collection_writer( File::Reference &file_ref, const Registry &file_format_registry)` | function | `boost::shared_ptr<GPlatesModel::ConstFeatureVisitor>` | Creates a feature visitor writer for the old write-only ".xy" GMT format. |
| `GPLATES_FILE_IO_FEATURECOLLECTIONFILEFORMATREGISTRY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/FeatureCollectionFileFormatRegistry tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrReader](OgrReader.md) | file-io | 39 |
| [cli/CliFeatureCollectionFileIO](../cli/CliFeatureCollectionFileIO.md) | cli | 35 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 14 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 9 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 6 |
| [unit-test/GenerateVelocityDomainCitcomsTest](../unit-test/GenerateVelocityDomainCitcomsTest.md) | unit-test | 6 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 5 |
| [file-io/ReconstructedFeatureGeometryExport](ReconstructedFeatureGeometryExport.md) | file-io | 4 |
| [file-io/ReconstructedFlowlineExport](ReconstructedFlowlineExport.md) | file-io | 4 |
| [file-io/ReconstructedMotionPathExport](ReconstructedMotionPathExport.md) | file-io | 4 |
| [file-io/ResolvedTopologicalGeometryExport](ResolvedTopologicalGeometryExport.md) | file-io | 4 |
| [qt-widgets/ManageFeatureCollectionsActionWidget](../qt-widgets/ManageFeatureCollectionsActionWidget.md) | qt-widgets | 4 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 3 |
| [cli/CliAssignPlateIdsCommand](../cli/CliAssignPlateIdsCommand.md) | cli | 3 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 3 |
| [file-io/OgrFeatureCollectionWriter](OgrFeatureCollectionWriter.md) | file-io | 3 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 3 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 2 |
| [cli/CliConvertFileFormatCommand](../cli/CliConvertFileFormatCommand.md) | cli | 2 |
| [cli/CliReconstructCommand](../cli/CliReconstructCommand.md) | cli | 2 |

*... and 15 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/FeatureCollectionFileFormatRegistry.h
python scripts/gpq.py def GPlatesFileIO::FeatureCollectionFileFormat::Registry --body
python scripts/gpq.py uses Registry --kind class
python scripts/gpq.py hier Registry
```
