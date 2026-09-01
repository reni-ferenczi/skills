# File

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 222 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/File.h` | C++ | 263 |
| `src/file-io/File.cc` | C++ | 94 |

## Overview

This is the binding between a `GPlatesModel::FeatureCollectionHandle` and the file it came from or will be written to. It carries no I/O of its own; what it holds is the `FileInfo` (path, format) and an optional `FeatureCollectionFileFormat::Configuration` giving the read/write options for that particular file. Almost everything in the application that talks about "a loaded file" — `GPlatesAppLogic::FeatureCollectionFileState`, the readers and writers in `file-io`, the exporters, the CLI, the Python bindings — passes one of these two types around rather than a bare feature collection, which is why the fan-in is so wide.

The unit exists to solve a lifetime problem in two phases, and the split between `File` and the nested `File::Reference` is that solution rather than an interface/implementation split. A feature collection read off disk is not yet in the model, so someone must own it; `File` is that owner, holding a strong `FeatureCollectionHandle::non_null_ptr_type`. `Reference` holds only a `weak_ref` to the collection alongside the `FileInfo` and configuration, and it is what every consumer actually wants. Calling `add_feature_collection_to_model` pushes the handle onto `model->root()` and drops the internal `boost::optional`, so the model becomes the owner and the `File` wrapper has nothing left to do — the `Reference` it returns is the same object `get_reference()` was already handing out, and it stays valid after the `File` is destroyed. `FeatureCollectionFileState::add_file` follows exactly this shape: it takes a `File::non_null_ptr_type`, immediately calls `add_feature_collection_to_model`, and keeps only the `Reference`.

`create_file_reference` is the entry point for the other direction — a feature collection that is already in the model and just needs a filename and format attached, for instance when exporting. Both classes have private constructors and are created only through the static factories; `Reference` names `File` as a friend so `File`'s constructor can build the inner object.

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

`File` and `File::Reference` are separately reference-counted, and the `Reference` does *not* keep the feature collection alive — it stores only a `weak_ref`. Between `File::create_file` and `add_feature_collection_to_model` the owning `File` is the sole thing standing between the collection and destruction, so a caller that constructs a `File`, hands the `Reference` to a reader, and then lets the `File` go out of scope leaves the reader holding a dangling weak reference. After the transfer to the model, the collection's lifetime is the model's, and the `Reference`'s `weak_ref` goes invalid if the collection is later removed; callers must check the weak reference rather than assume it resolves. `FeatureCollectionFileState::FileSlotExtra` keeps a second `const_weak_ref` of its own purely to hang a model callback off, not to extend any lifetime.

`add_feature_collection_to_model` is idempotent: on a second call `d_feature_collection_handle` is already `boost::none` and it simply returns the existing `Reference`. Note that `create_file`'s defaults construct a fresh empty `FeatureCollectionHandle` and an empty `FileInfo`, which is the documented way to make an empty file for a reader to populate afterwards.

`set_file_info` on the `Reference` rewrites both the `FileInfo` and the file configuration in place — an existing `Reference` held elsewhere sees the change, which is the intended mechanism for "save as" but means the path is not an invariant of the object. A `file_configuration` of `boost::none` is not an error: it means "use whatever configuration is registered for this file's format", resolved by `FeatureCollectionFileFormatRegistry` at read or write time.

Neither class does any locking; adding to the model must happen on whatever thread owns the model.

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
