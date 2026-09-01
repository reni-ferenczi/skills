# GpmlFormatDeformationExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlFormatDeformationExport.h` | C++ | 91 |
| `src/file-io/GpmlFormatDeformationExport.cc` | C++ | 417 |

## Overview

[[[PROSE overview unit=file-io/GpmlFormatDeformationExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::deformed_feature_geometry_seq_type`](#anonymousdeformed_feature_geometry_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of deformed feature geometries. |
| [`GPlatesFileIO::GpmlFormatDeformationExport::deformed_feature_geometry_group_type`](#gplatesfileiogpmlformatdeformationexportdeformed_feature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of TopologyReconstructedFeatureGeometry objects. |

## Members

### `(anonymous)::deformed_feature_geometry_seq_type`

*None.*

### `GPlatesFileIO::GpmlFormatDeformationExport::deformed_feature_geometry_group_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `insert_deformed_feature_geometry_into_feature_collection( GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, const GPlatesAppLogic::TopologyReconstructedFeatureGeometry *deformed_feature_geometry, boost::optional<GPlatesFileIO::DeformationExport::PrincipalStrainOptions> include_principal_strain, bool ...` | function | `void` | — |
| `GPLATES_FILE_IO_GPMLFORMATDEFORMATIONEXPORT_H` | macro | `None` | — |
| `export_deformation( const std::list<deformed_feature_geometry_group_type> &deformed_feature_geometry_group_seq, const QFileInfo& file_info, GPlatesModel::ModelInterface &model, boost::optional<DeformationExport::PrincipalStrainOptions> include_principal_strain, bool include_dilatation_strain, bool include_dilatation_st ...` | function | `void` | Exports TopologyReconstructedFeatureGeometry objects along with their deformation information. |

## Notes

[[[PROSE notes unit=file-io/GpmlFormatDeformationExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/DeformationExport](DeformationExport.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlFormatDeformationExport.h
python scripts/gpq.py def GPlatesFileIO::GpmlFormatDeformationExport::deformed_feature_geometry_group_type --body
python scripts/gpq.py uses deformed_feature_geometry_group_type --kind typedef
```
