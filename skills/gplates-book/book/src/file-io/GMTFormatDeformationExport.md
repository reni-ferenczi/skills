# GMTFormatDeformationExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 110 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatDeformationExport.h` | C++ | 93 |
| `src/file-io/GMTFormatDeformationExport.cc` | C++ | 620 |

## Overview

[[[PROSE overview unit=file-io/GMTFormatDeformationExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=file-io/GMTFormatDeformationExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
