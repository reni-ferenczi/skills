# GMTFormatDeformationExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 110 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatDeformationExport.h` | C++ | 93 |
| `src/file-io/GMTFormatDeformationExport.cc` | C++ | 620 |

## Overview

Exports deformation and strain information calculated at reconstructed domain points to GMT format. Each output line records the position of a point on a deformed surface along with optional strain invariants and rates — principal strain (major and minor axes with orientation), dilatation strain, dilatation and second-invariant strain rates, and strain rate style. The exporter wraps `TopologyReconstructedFeatureGeometry` objects that pair domain positions with deformation data, writing them in the GMT xy-format with configurable coordinate conventions (longitude-latitude or latitude-longitude) and selectable strain output options.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GMTFormatDeformationExport::(anonymous)::deformed_feature_geometry_seq_type`](#gplatesfileiogmtformatdeformationexportanonymousdeformed_feature_geometry_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of deformed feature geometries. |
| [`GPlatesFileIO::GMTFormatDeformationExport::deformed_feature_geometry_group_type`](#gplatesfileiogmtformatdeformationexportdeformed_feature_geometry_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of TopologyReconstructedFeatureGeometry objects. |
| [`GPlatesFileIO::GMTFormatDeformationExport::referenced_files_collection_type`](#gplatesfileiogmtformatdeformationexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `GPlatesFileIO::GMTFormatDeformationExport::(anonymous)::deformed_feature_geometry_seq_type`

*None.*

### `GPlatesFileIO::GMTFormatDeformationExport::deformed_feature_geometry_group_type`

*None.*

### `GPlatesFileIO::GMTFormatDeformationExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_gmt_deformation_line( QTextStream &output_stream, const GPlatesMaths::PointOnSphere &domain_point, bool domain_point_lon_lat_format, boost::optional<const GPlatesAppLogic::DeformationStrain::StrainPrincipal &> principal_strain, boost::optional<const GPlatesFileIO::DeformationExport::PrincipalStrainOptions &> prin ...` | function | `void` | Outputs a deformation line to the GMT output consisting of position and optional strain rates. |
| `print_gmt_deformed_feature_geometry( QTextStream &output_stream, const GPlatesAppLogic::TopologyReconstructedFeatureGeometry &deformed_feature_geometry, bool domain_point_lon_lat_format, boost::optional<DeformationExport::PrincipalStrainOptions> include_principal_strain, bool include_dilatation_strain, bool include_dil ...` | function | `void` | Write the deformed feature geometry (positions and strain rates). |
| `GPLATES_FILE_IO_GMTFORMATDEFORMATIONEXPORT_H` | macro | `None` | — |
| `export_deformation( const std::list<deformed_feature_geometry_group_type> &velocity_vector_field_group_seq, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time, bool domain_poin ...` | function | `void` | Exports TopologyReconstructedFeatureGeometry objects. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/DeformationExport](DeformationExport.md) | file-io | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatDeformationExport.h
python scripts/gpq.py def GPlatesFileIO::GMTFormatDeformationExport::deformed_feature_geometry_group_type --body
python scripts/gpq.py uses deformed_feature_geometry_group_type --kind typedef
```
