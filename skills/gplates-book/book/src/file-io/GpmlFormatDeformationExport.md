# GpmlFormatDeformationExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlFormatDeformationExport.h` | C++ | 91 |
| `src/file-io/GpmlFormatDeformationExport.cc` | C++ | 417 |

## Overview

Exports deformation data from `TopologyReconstructedFeatureGeometry` objects to a GPML file. This module takes the per-point deformation information (strain, strain rates, and principal strains) computed during reconstruction and writes it into new GPML features structured as scalar coverage features. The exported features preserve the domain geometry and add scalar properties containing the requested deformation metrics—principal strain axes and magnitudes, dilatation strain, strain rate components, and strain rate style.

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

*None.*

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
