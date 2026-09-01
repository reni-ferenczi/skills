# ReconstructionGeometryExportImpl

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 101 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReconstructionGeometryExportImpl.h` | C++ | 508 |
| `src/file-io/ReconstructionGeometryExportImpl.cc` | C++ | 116 |

## Overview

[[[PROSE overview unit=file-io/ReconstructionGeometryExportImpl tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ReconstructionGeometryExportImpl::referenced_files_collection_type`](#gplatesfileioreconstructiongeometryexportimplreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |
| [`GPlatesFileIO::ReconstructionGeometryExportImpl::FeatureGeometryGroup`](#gplatesfileioreconstructiongeometryexportimplfeaturegeometrygroup) | struct | — | `<class ReconstructionGeometryType>` | 0 | Groups ReconstructedFeatureGeometry derived objects with their feature. |
| [`GPlatesFileIO::ReconstructionGeometryExportImpl::FeatureCollectionFeatureGroup`](#gplatesfileioreconstructiongeometryexportimplfeaturecollectionfeaturegroup) | struct | — | `<class ReconstructionGeometryType>` | 0 | Groups FeatureGeometryGroup objects with their feature collection. |
| [`GPlatesFileIO::ReconstructionGeometryExportImpl::feature_handle_to_collection_map_type`](#gplatesfileioreconstructiongeometryexportimplfeature_handle_to_collection_map_type) | typedef | — | — | 0 | Typedef for mapping from FeatureHandle to the feature collection file it came from and the order in which is occurs relative to other features in the feature collections. |
| [`GPlatesFileIO::ReconstructionGeometryExportImpl::ContainsSameFilePointerPredicate`](#gplatesfileioreconstructiongeometryexportimplcontainssamefilepointerpredicate) | class | — | `<class ReconstructionGeometryType>` | 0 | Predicate to determine if FeatureCollectionFeatureGroup object has specific file pointer. |
| [`GPlatesFileIO::ReconstructionGeometryExportImpl::SortByFeatureOrderInCollections`](#gplatesfileioreconstructiongeometryexportimplsortbyfeatureorderincollections) | class | — | `<class ReconstructionGeometryType>` | 0 | Compares feature handle pointers of two ReconstructionGeometry derived objects. |

## Members

### `GPlatesFileIO::ReconstructionGeometryExportImpl::referenced_files_collection_type`

*None.*

### `GPlatesFileIO::ReconstructionGeometryExportImpl::FeatureGeometryGroup`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureGeometryGroup( const GPlatesModel::FeatureHandle::const_weak_ref &_feature_ref)` | constructor | `None` | public | — |
| `feature_ref` | field | `GPlatesModel::FeatureHandle::const_weak_ref` | public | — |
| `recon_geoms` | field | `std::vector<const ReconstructionGeometryType *>` | public | — |

### `GPlatesFileIO::ReconstructionGeometryExportImpl::FeatureCollectionFeatureGroup`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureCollectionFeatureGroup( const GPlatesFileIO::File::Reference *file_ptr_)` | constructor | `None` | public | — |
| `file_ptr` | field | `GPlatesFileIO::File::Reference` | public | — |
| `feature_geometry_groups` | field | `std::list< FeatureGeometryGroup<ReconstructionGeometryType> >` | public | — |

### `GPlatesFileIO::ReconstructionGeometryExportImpl::feature_handle_to_collection_map_type`

*None.*

### `GPlatesFileIO::ReconstructionGeometryExportImpl::ContainsSameFilePointerPredicate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ContainsSameFilePointerPredicate(const GPlatesFileIO::File::Reference * file_ptr_)` | constructor | `None` | public | — |
| `operator()( const FeatureCollectionFeatureGroup<ReconstructionGeometryType>& elem)` | operator | `bool` | public | — |
| `file_ptr` | field | `GPlatesFileIO::File::Reference` | private | — |

### `GPlatesFileIO::ReconstructionGeometryExportImpl::SortByFeatureOrderInCollections`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SortByFeatureOrderInCollections( const feature_handle_to_collection_map_type &feature_handle_to_collection_map)` | constructor | `None` | public | Pointer-to-data-member determines which file offset (main or coverage) to use in comparison. |
| `operator()( const ReconstructionGeometryType *lhs_recon_geom, const ReconstructionGeometryType *rhs_recon_geom)` | operator | `bool` | public | — |
| `d_feature_handle_to_collection_map` | field | `feature_handle_to_collection_map_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_RECONSTRUCTIONGEOMETRYEXPORTIMPL_H` | macro | `None` | — |
| `DISABLE_MSVC_WARNING` | variable | `PUSH_MSVC_WARNINGS` | — |
| `populate_feature_handle_to_collection_map( feature_handle_to_collection_map_type &feature_handle_to_collection_map, const std::vector<const File::Reference *> &reconstructable_files)` | function | `void` | Populates mapping of feature handle to feature collection file. |
| `get_files_referenced_by_geometries( referenced_files_collection_type &referenced_files, const std::vector<const ReconstructionGeometryType *> &reconstruction_geometry_seq, const std::vector<const File::Reference *> &reconstructable_files, feature_handle_to_collection_map_type &feature_handle_to_collection_map)` | function | `void` | Returns a list of files that reference the ReconstructionGeometry derived objects. |
| `get_output_filenames( std::vector<QString> &output_filenames, const QString &output_filename, const std::list< FeatureCollectionFeatureGroup<ReconstructionGeometryType> > &grouped_features_seq, bool export_separate_output_directory_per_input_file)` | function | `void` | Creates an output filename for each entry in grouped\_features\_seq and stores in output\_filenames. |
| `build_flat_structure_filename( const QString &export_path, const QString &collection_filename, const QString &export_filename)` | function | `QString` | Builds filename as "\<export\_path\>/\<collection\_filename\>\_\<export\_filename\>". |
| `build_folder_structure_filename( const QString &export_path, const QString &collection_filename, const QString &export_filename)` | function | `QString` | Builds filename as "\<export\_path\>/\<collection\_filename\>/\<export\_filename\>". |
| `get_unique_list_of_referenced_files( referenced_files_collection_type &referenced_files, const std::vector<const ReconstructionGeometryType *> &reconstruction_geometry_seq, const feature_handle_to_collection_map_type &feature_handle_to_collection_map)` | function | `void` | Returns a unique list of files that reference the visible ReconstructionGeometry objects. |
| `group_reconstruction_geometries_with_their_feature( std::list< FeatureGeometryGroup<ReconstructionGeometryType> > &grouped_recon_geoms_seq, const std::vector<const ReconstructionGeometryType *> &reconstruction_geometry_seq, const feature_handle_to_collection_map_type &feature_to_collection_map)` | function | `void` | — |
| `group_feature_geom_groups_with_their_collection( const feature_handle_to_collection_map_type &feature_handle_to_collection_map, std::list< FeatureCollectionFeatureGroup<ReconstructionGeometryType> > &grouped_features_seq, const std::list< FeatureGeometryGroup<ReconstructionGeometryType> > &grouped_recon_geoms_seq)` | function | `void` | — |
| `get_output_filenames( std::vector<QString> &output_filenames, const QString &filename, const std::list< FeatureCollectionFeatureGroup<ReconstructionGeometryType> > &grouped_features_seq, bool export_separate_output_directory_per_input_file)` | function | `void` | — |

## Notes

[[[PROSE notes unit=file-io/ReconstructionGeometryExportImpl tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/MultiPointVectorFieldExport](MultiPointVectorFieldExport.md) | file-io | 26 |
| [file-io/ResolvedTopologicalGeometryExport](ResolvedTopologicalGeometryExport.md) | file-io | 22 |
| [file-io/DeformationExport](DeformationExport.md) | file-io | 16 |
| [file-io/ReconstructedScalarCoverageExport](ReconstructedScalarCoverageExport.md) | file-io | 16 |
| [file-io/OgrFormatReconstructedFeatureGeometryExport](OgrFormatReconstructedFeatureGeometryExport.md) | file-io | 12 |
| [file-io/ReconstructedFeatureGeometryExport](ReconstructedFeatureGeometryExport.md) | file-io | 10 |
| [file-io/ReconstructedFlowlineExport](ReconstructedFlowlineExport.md) | file-io | 10 |
| [file-io/ReconstructedMotionPathExport](ReconstructedMotionPathExport.md) | file-io | 10 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 9 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 8 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 7 |
| [file-io/GMTFormatDeformationExport](GMTFormatDeformationExport.md) | file-io | 6 |
| [file-io/GMTFormatFlowlineExport](GMTFormatFlowlineExport.md) | file-io | 6 |
| [file-io/GMTFormatMotionPathExport](GMTFormatMotionPathExport.md) | file-io | 6 |
| [file-io/GMTFormatMultiPointVectorFieldExport](GMTFormatMultiPointVectorFieldExport.md) | file-io | 6 |
| [file-io/GMTFormatReconstructedFeatureGeometryExport](GMTFormatReconstructedFeatureGeometryExport.md) | file-io | 6 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](GMTFormatReconstructedScalarCoverageExport.md) | file-io | 6 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 6 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](GpmlFormatMultiPointVectorFieldExport.md) | file-io | 6 |
| [file-io/OgrFormatFlowlineExport](OgrFormatFlowlineExport.md) | file-io | 6 |

*... and 8 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ReconstructionGeometryExportImpl.h
python scripts/gpq.py def GPlatesFileIO::ReconstructionGeometryExportImpl::SortByFeatureOrderInCollections --body
python scripts/gpq.py uses SortByFeatureOrderInCollections --kind class
python scripts/gpq.py hier SortByFeatureOrderInCollections
```
