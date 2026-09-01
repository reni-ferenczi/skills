# ReconstructionGeometryExportImpl

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 101 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ReconstructionGeometryExportImpl.h` | C++ | 508 |
| `src/file-io/ReconstructionGeometryExportImpl.cc` | C++ | 116 |

## Overview

Exporting reconstruction results is where two mismatched shapes have to be reconciled. App-logic hands the exporters a flat `std::vector` of `ReconstructionGeometry` pointers, in whatever order the reconstruction happened to produce them; the output formats want a *file*-shaped, *feature*-shaped hierarchy, because a shapefile or GMT file corresponds to one input feature collection and its records correspond to features. This header is the shared machinery that performs that regrouping, factored out of the roughly two dozen `*Export` units listed below so that every export format and every geometry type does it identically. It declares no exporter of its own — it is a private implementation namespace that the real exporters (`ReconstructedFeatureGeometryExport`, `ResolvedTopologicalGeometryExport`, `ReconstructedFlowlineExport`, `MultiPointVectorFieldExport` and the rest) include and call in a fixed sequence.

Everything is templated on `ReconstructionGeometryType` rather than written against the `ReconstructionGeometry` base, because the exporters need the concrete type — a `ReconstructedFeatureGeometry`, a `ResolvedTopologicalLine`, a `MultiPointVectorField` — all the way through to the format writer. The only thing this code needs from that type is the ability to recover its feature, which it gets through `GPlatesAppLogic::ReconstructionGeometryUtils::get_feature_handle_ptr` and `get_feature_ref`, so the templates work for any reconstruction-geometry class those utilities understand. `File::Reference` is the identity of an input file throughout; groups and referenced-file lists hold raw `const File::Reference *` and compare them by pointer.

The pipeline a caller runs is fixed and each step feeds the next. `get_files_referenced_by_geometries` builds the `feature_handle_to_collection_map_type` — the index from every feature handle in the active reconstructable files to its file plus a global ordinal — and from it derives the deduplicated list of files the exported geometries actually came from, which exporters write into the output as provenance. `group_reconstruction_geometries_with_their_feature` then uses that map's ordinals to sort, so the export order reproduces the order features appear in their collections rather than the order the reconstruction produced them; `group_feature_geom_groups_with_their_collection` regroups those per-feature groups under their file. `get_output_filenames` finally turns each group into an output path, either flat (`<collection>_<export>`) or one directory per input collection, which is what the export dialogs' "separate directory per input file" option selects.

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

Nothing here owns anything. The groups, the map and the referenced-file list all hold raw `const File::Reference *` and raw `const ReconstructionGeometryType *`, and `SortByFeatureOrderInCollections` holds a *reference* to the map. All of it is valid only for the duration of one export call, while the caller's files and reconstruction stay alive; none of these structures may outlive the export or be cached across reconstruction times. `feature_handle_to_collection_map_type` is keyed on raw `FeatureHandle *`, so it is likewise invalidated by anything that destroys features.

The map is also the only definition of export order, and it is built by walking `reconstructable_files` in the order given and assigning a single monotonically increasing `feature_order` *across* all files. Pass the files in a different order and the export order changes. Features whose collection weak-ref is invalid are skipped entirely, so they get no ordinal and no entry.

Silent drops are the norm on the read side too, and this is the behaviour most likely to surprise. `get_unique_list_of_referenced_files` and `group_reconstruction_geometries_with_their_feature` both `continue` past a geometry whose feature cannot be recovered or is absent from the map, and `group_feature_geom_groups_with_their_collection` skips any feature group not found in the map. A geometry reconstructed from a feature that is not in one of the `reconstructable_files` passed in therefore vanishes from the export with no error and no warning.

`SortByFeatureOrderInCollections` is used with `std::stable_sort`, deliberately — the comment says so — so that the relative order of several geometries belonging to the *same* feature is preserved. Do not switch it to `std::sort`. Its comparator has an ordering quirk worth knowing: geometries with no recoverable feature are compared by the `boost::optional` values themselves, and geometries missing from the map sort before those present, so unmapped entries cluster at the front of the sorted vector even though they are then skipped during grouping. The grouping loop relies on the sort having put same-feature geometries adjacent — it starts a new `FeatureGeometryGroup` only when the feature ref differs from the previous one, so a non-adjacent repeat of a feature would produce two groups for it.

`group_feature_geom_groups_with_their_collection` finds a collection's group with `std::find_if` over a `std::list`, which is linear per feature group; that is fine for a handful of loaded files but is quadratic in the number of *distinct* collections. It appends to `grouped_features_seq` without clearing it, as do the other output parameters here, so pass in empty containers.

`build_folder_structure_filename` has a side effect its sibling does not: it creates the `<export_path>/<collection>/` directory if missing and throws `ErrorOpeningFileForWritingException` when that fails. So `get_output_filenames` is not a pure name computation when `export_separate_output_directory_per_input_file` is true — calling it creates directories on disk and can throw. Collection names come from `QFileInfo::completeBaseName()` of the input file, so two input files with the same base name in different directories collide onto the same output path.

The MSVC pragmas at the top are load-bearing for the Windows build rather than incidental: warning 4503 (decorated name length exceeded) is disabled because of the deeply nested template instantiations these `std::list< FeatureGeometryGroup<...> >` types produce, and 4181 is suppressed around the Boost.Lambda includes used by the sort in `get_unique_list_of_referenced_files`.

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
