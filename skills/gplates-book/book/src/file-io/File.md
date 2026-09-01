# File

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 222 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/File.h` | C++ | 263 |
| `src/file-io/File.cc` | C++ | 94 |

## Overview

[[[PROSE overview unit=file-io/File tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::File`](#gplatesfileiofile) | class | [`GPlatesUtils::ReferenceCount<File>`](../utils/ReferenceCount.md) | — | 0 | A wrapper around a file that owns a feature collection (that has not been added to the model). |

## Members

### `GPlatesFileIO::File`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Reference` | class | `None` | public | Interface to get file information associated with a feature collection loaded from or saved to a file. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<File>` | public | A convenience typedef for a non-null intrusive pointer to a non-const File. |
| `create_file( const FileInfo &file_info = FileInfo(), const GPlatesModel::FeatureCollectionHandle::non_null_ptr_type & feature_collection = GPlatesModel::FeatureCollectionHandle::create(), boost::optional<FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type> file_configuration = boost::none)` | method | `File::non_null_ptr_type` | public | Create a File object with feature collection feature\_collection. |
| `create_file_reference( const FileInfo &file_info, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, boost::optional<FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type> file_configuration = boost::none)` | method | `File::Reference::non_null_ptr_type` | public | Create a Reference object with feature collection feature\_collection. |
| `add_feature_collection_to_model( GPlatesModel::ModelInterface &model)` | method | `Reference::non_null_ptr_type` | public | Adds the feature collection contained within to model. |
| `d_file` | field | `Reference::non_null_ptr_type` | private | — |
| `d_feature_collection_handle` | field | `boost::optional<GPlatesModel::FeatureCollectionHandle::non_null_ptr_type>` | private | The feature collection handle before it is added, if ever, to the model. |
| `File( const GPlatesModel::FeatureCollectionHandle::non_null_ptr_type &feature_collection, const FileInfo &file_info, boost::optional<FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type> file_configuration)` | constructor | `None` | private | Constructor. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_FILE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/File tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrFeatureCollectionWriter](OgrFeatureCollectionWriter.md) | file-io | 115 |
| [file-io/PlatesLineFormatReader](PlatesLineFormatReader.md) | file-io | 107 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 62 |
| [file-io/OgrReader](OgrReader.md) | file-io | 59 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 47 |
| [file-io/PlatesRotationFileProxy](PlatesRotationFileProxy.md) | file-io | 43 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 36 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 31 |
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 30 |
| [file-io/ReconstructionGeometryExportImpl](ReconstructionGeometryExportImpl.md) | file-io | 30 |
| [file-io/ResolvedTopologicalGeometryExport](ResolvedTopologicalGeometryExport.md) | file-io | 29 |
| [file-io/MultiPointVectorFieldExport](MultiPointVectorFieldExport.md) | file-io | 25 |
| [file-io/GmapReader](GmapReader.md) | file-io | 20 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 20 |
| [file-io/ReconstructedFeatureGeometryExport](ReconstructedFeatureGeometryExport.md) | file-io | 19 |
| [file-io/ReconstructedFlowlineExport](ReconstructedFlowlineExport.md) | file-io | 19 |
| [file-io/ReconstructedMotionPathExport](ReconstructedMotionPathExport.md) | file-io | 19 |
| [cli/CliFeatureCollectionFileIO](../cli/CliFeatureCollectionFileIO.md) | cli | 18 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 17 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 14 |

*... and 59 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/File.h
python scripts/gpq.py def GPlatesFileIO::File --body
python scripts/gpq.py uses File --kind class
python scripts/gpq.py hier File
```
