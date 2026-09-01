# MultiPointVectorFieldExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 6 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/MultiPointVectorFieldExport.h` | C++ | 253 |
| `src/file-io/MultiPointVectorFieldExport.cc` | C++ | 488 |

## Overview

This unit is the format-agnostic entry point for exporting velocity fields computed
on a multi-point domain. Each of its four functions takes a sequence of
`GPlatesAppLogic::MultiPointVectorField` objects plus the export options for one
target format, and groups or splits them into output files as requested (a single
combined file, one file per input feature collection, or both) before handing the
actual per-vector formatting off to a dedicated writer: `GpmlFormatMultiPointVectorFieldExport`,
`GMTFormatMultiPointVectorFieldExport`, `TerraFormatVelocityVectorFieldExport`, or
`CitcomsFormatVelocityVectorFieldExport`.

The GMT, Terra and CitcomS variants exist because those simulation codes each expect
a different velocity representation and file-naming convention: GMT allows a choice
of vector encoding (`GMTVelocityVectorFormatType`) plus optional stride and scaling,
while Terra and CitcomS match output files to input velocity-domain (mesh) files by
substituting placeholders in filename templates, since a single reconstruction can
produce one velocity field per mesh processor or diamond cap.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::MultiPointVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type`](#gplatesfileiomultipointvectorfieldexportanonymousmulti_point_vector_field_seq_type) | typedef | — | — | 0 | Typedef for a sequence of MultiPointVectorField objects. |
| [`GPlatesFileIO::MultiPointVectorFieldExport::(anonymous)::grouped_features_seq_type`](#gplatesfileiomultipointvectorfieldexportanonymousgrouped_features_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureCollectionFeatureGroup objects. |
| [`GPlatesFileIO::MultiPointVectorFieldExport::GMTVelocityVectorFormatType`](#gplatesfileiomultipointvectorfieldexportgmtvelocityvectorformattype) | enum | — | — | 0 | How to write out each velocity vector to GMT format. |

## Members

### `GPlatesFileIO::MultiPointVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type`

*None.*

### `GPlatesFileIO::MultiPointVectorFieldExport::(anonymous)::grouped_features_seq_type`

*None.*

### `GPlatesFileIO::MultiPointVectorFieldExport::GMTVelocityVectorFormatType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GMT_VELOCITY_VECTOR_3D` | enumerator | `None` | — | — |
| `GMT_VELOCITY_VECTOR_COLAT_LON` | enumerator | `None` | — | — |
| `GMT_VELOCITY_VECTOR_ANGLE_MAGNITUDE` | enumerator | `None` | — | — |
| `GMT_VELOCITY_VECTOR_AZIMUTH_MAGNITUDE` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_MULTIPOINTVECTORFIELDEXPORT_H` | macro | `None` | — |
| `export_velocity_vector_fields_to_gpml_format( const QString &filename, const std::vector<const GPlatesAppLogic::MultiPointVectorField *> &velocity_vector_field_seq, GPlatesModel::ModelInterface &model, const std::vector<const File::Reference *> &active_files, const GPlatesModel::integer_plate_id_type &reconstruction_an ...` | function | `void` | Exports MultiPointVectorField objects containing \*velocities\* to the GPML file format. |
| `export_velocity_vector_fields_to_gmt_format( const QString &filename, const std::vector<const GPlatesAppLogic::MultiPointVectorField *> &velocity_vector_field_seq, const std::vector<const File::Reference *> &active_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstru ...` | function | `void` | Exports MultiPointVectorField objects containing \*velocities\* to the GMT file format. |
| `export_velocity_vector_fields_to_terra_text_format( const QString &velocity_domain_file_name_template, const QString &velocity_export_file_name_template, const QString &velocity_domain_mt_place_holder, const QString &velocity_domain_nt_place_holder, const QString &velocity_domain_nd_place_holder, const QString &velocit ...` | function | `void` | Exports MultiPointVectorField objects containing \*velocities\* to the Terra text file format. |
| `export_velocity_vector_fields_to_citcoms_global_format( const QString &velocity_domain_file_name_template, const QString &velocity_export_file_name_template, const QString &velocity_domain_density_place_holder, const QString &velocity_domain_cap_number_place_holder, const QString &velocity_export_cap_number_place_holde ...` | function | `void` | Exports MultiPointVectorField objects containing \*velocities\* to the CitcomS global file format. |

## Notes

- The GPML export always writes velocities in colat/lon format, regardless of the
  GMT-only `GMTVelocityVectorFormatType` choice, which only affects the GMT writer.
- The Terra and CitcomS exporters silently skip any velocity field whose domain file
  name does not match the supplied template placeholders; there must be exactly one
  occurrence of each required placeholder in the template or matching fails.
- All four functions throw `ErrorOpeningFileForWritingException` if an output file
  cannot be written.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatMultiPointVectorFieldExport](GMTFormatMultiPointVectorFieldExport.md) | file-io | 23 |
| [qt-widgets/ExportVelocityOptionsWidget](../qt-widgets/ExportVelocityOptionsWidget.md) | qt-widgets | 23 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 14 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 8 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 3 |
| [file-io/CitcomsFormatVelocityVectorFieldExport](CitcomsFormatVelocityVectorFieldExport.md) | file-io | 2 |
| [file-io/TerraFormatVelocityVectorFieldExport](TerraFormatVelocityVectorFieldExport.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/MultiPointVectorFieldExport.h
python scripts/gpq.py def GPlatesFileIO::MultiPointVectorFieldExport::GMTVelocityVectorFormatType --body
python scripts/gpq.py uses GMTVelocityVectorFormatType --kind enum
```
