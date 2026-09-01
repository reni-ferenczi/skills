# FeatureCollectionFileFormatConfigurations

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 796 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/FeatureCollectionFileFormatConfigurations.h` | C++ | 210 |
| `src/file-io/FeatureCollectionFileFormatConfigurations.cc` | C++ | 60 |

## Overview

This is where the concrete `file-io/FeatureCollectionFileFormatConfiguration`
subclasses live: `GMTConfiguration` for the write-only `WRITE_ONLY_XY_GMT`
format, and `OGRConfiguration` shared by the OGR-backed formats
(`OGRGMT`, `SHAPEFILE`, `GEOJSON`, `GEOPACKAGE`). Both are plain option
bags — a GMT header style on one side, a dateline-wrapping flag and an SRS
write-behaviour on the other — that `FeatureCollectionFileFormatRegistry`,
`OgrWriter`/`OgrReader` and the corresponding Qt configuration dialogs read
and write through the `dynamic_cast_configuration()`/`copy_cast_configuration()`
helpers from the base header.

`OGRConfiguration` also owns the original spatial reference system captured
when a file was read (`get_original_file_srs()`/`set_original_file_srs()`),
so a later write of the same feature collection can reproduce or override
the source SRS via `OgrSrsWriteBehaviour`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FeatureCollectionFileFormat::GMTConfiguration`](#gplatesfileiofeaturecollectionfileformatgmtconfiguration) | class | [`Configuration`](FeatureCollectionFileFormatConfiguration.md) | — | 0 | Configuration options for the write-only GMT format 'WRITE\_ONLY\_XY\_GMT'. |
| [`GPlatesFileIO::FeatureCollectionFileFormat::OGRConfiguration`](#gplatesfileiofeaturecollectionfileformatogrconfiguration) | class | [`Configuration`](FeatureCollectionFileFormatConfiguration.md) | — | 0 | Configuration options for OGR-supported file formats. |

## Members

### `GPlatesFileIO::FeatureCollectionFileFormat::GMTConfiguration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GMTConfiguration>` | public | — |
| `shared_ptr_type` | typedef | `boost::shared_ptr<GMTConfiguration>` | public | — |
| `GMTConfiguration( GPlatesFileIO::GMTFormatWriter::HeaderFormat header_format = GPlatesFileIO::GMTFormatWriter::PLATES4_STYLE_HEADER)` | constructor | `None` | public | Constructor. |
| `get_header_format()` | method | `GPlatesFileIO::GMTFormatWriter::HeaderFormat` | public | Returns the GMT header format. |
| `set_header_format( GPlatesFileIO::GMTFormatWriter::HeaderFormat header_format)` | method | `void` | public | Sets the GMT header format. |
| `d_header_format` | field | `GPlatesFileIO::GMTFormatWriter::HeaderFormat` | private | — |

### `GPlatesFileIO::FeatureCollectionFileFormat::OGRConfiguration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const OGRConfiguration>` | public | — |
| `shared_ptr_type` | typedef | `boost::shared_ptr<OGRConfiguration>` | public | — |
| `OgrSrsWriteBehaviour` | enum | `None` | public | — |
| `model_to_attribute_map_type` | typedef | `QMap<QString, QString>` | public | Typedef for a model-to-attribute mapping. |
| `OGRConfiguration( Format file_format, bool wrap_to_dateline)` | constructor | `None` | public | Constructor. |
| `get_wrap_to_dateline()` | method | `bool` | public | Returns dateline wrapping flag. |
| `set_wrap_to_dateline( bool wrap_to_dateline)` | method | `void` | public | Sets dateline wrapping flag. |
| `get_ogr_srs_write_behaviour()` | method | `OgrSrsWriteBehaviour` | public | — |
| `set_ogr_srs_write_behaviour( const OgrSrsWriteBehaviour &behaviour)` | method | `void` | public | — |
| `get_model_to_attribute_map` | field | `model_to_attribute_map_type` | public | Returns the model-to-attribute map. |
| `get_original_file_srs()` | method | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | get\_original\_file\_srs the original SRS of the OGR data source, if one was provided. |
| `set_original_file_srs( const GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type &srs)` | method | `void` | public | set\_original\_file\_srs Sets the original SRS of the OGR data source. |
| `FEATURE_COLLECTION_TAG` | field | `std::string` | private | The key string used when storing the model-to-attribute map as a tag in a FeatureCollectionHandle. |
| `d_wrap_to_dateline` | field | `bool` | private | — |
| `d_original_file_srs` | field | `boost::optional<GPlatesPropertyValues::SpatialReferenceSystem::non_null_ptr_to_const_type>` | private | d\_original\_file\_srs - The original SRS of the OGR data source, if one was provided. |
| `d_ogr_srs_write_behaviour` | field | `OgrSrsWriteBehaviour` | private | d\_ogr\_srs\_write\_behaviour - enum for controlling how the SRS is handled on output. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `FEATURE_COLLECTION_TAG` | variable | `std::string` | — |
| `GPLATES_FILE_IO_FEATURECOLLECTIONFILEFORMATCONFIGURATIONS_H` | macro | `None` | — |

## Notes

`OGRConfiguration::get_model_to_attribute_map()` is `static` and takes a
`FeatureCollectionHandle` rather than reading a member: despite living on
`OGRConfiguration`, the model-to-attribute map is *not* stored in the
configuration object. It is stored as a tag (keyed by
`FEATURE_COLLECTION_TAG`) directly on the feature collection, specifically so
the mapping survives the feature collection being detached from its
originating `File` and so it can be persisted separately (in a shapefile
mapping file) from the rest of the configuration, which is per-session and
not written to disk.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrWriter](OgrWriter.md) | file-io | 28 |
| [file-io/OgrFeatureCollectionWriter](OgrFeatureCollectionWriter.md) | file-io | 20 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 17 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 12 |
| [file-io/OgrReader](OgrReader.md) | file-io | 12 |
| [qt-widgets/GMTFileFormatConfigurationDialog](../qt-widgets/GMTFileFormatConfigurationDialog.md) | qt-widgets | 12 |
| [file-io/OgrGeometryExporter](OgrGeometryExporter.md) | file-io | 10 |
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](../qt-widgets/ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 10 |
| [file-io/GMTFormatWriter](GMTFormatWriter.md) | file-io | 5 |
| [file-io/PlatesRotationFileProxy](PlatesRotationFileProxy.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/FeatureCollectionFileFormatConfigurations.h
python scripts/gpq.py def GPlatesFileIO::FeatureCollectionFileFormat::OGRConfiguration --body
python scripts/gpq.py uses OGRConfiguration --kind class
python scripts/gpq.py hier OGRConfiguration
```
