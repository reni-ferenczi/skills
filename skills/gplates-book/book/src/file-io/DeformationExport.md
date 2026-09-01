# DeformationExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 110 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/DeformationExport.h` | C++ | 197 |
| `src/file-io/DeformationExport.cc` | C++ | 285 |

## Overview

`DeformationExport` writes the per-point deformation data carried by `TopologyReconstructedFeatureGeometry` objects — the output of topological network reconstruction — to either GPML (`export_deformation_to_gpml_format`) or GMT (`export_deformation_to_gmt_format`) format. Both functions share the same set of optional scalar fields: principal strain or stretch (angle/azimuth plus major/minor axis, controlled by `PrincipalStrainOptions`), dilatation strain, dilatation strain rate, second-invariant strain rate, and strain-rate style, each independently switchable so callers only pay for the scalars they need. `PrincipalStrainOptions` also converts a raw `DeformationStrain::StrainPrincipal` into the angle-or-azimuth convention the caller asked for via `get_principal_angle_or_azimuth_in_degrees`.

Both exporters share the same output-grouping options — a single combined file (`export_single_output_file`), one file per input feature collection (`export_per_input_file`, optionally into per-file directories) — and either combination can be requested at once, in which case both a combined file and the per-file breakdown are written. `export_deformation_to_gmt_format` additionally controls whether domain points are written longitude-then-latitude (GMT's default) or latitude-then-longitude.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::DeformationExport::(anonymous)::deformed_feature_geometry_seq_type`](#gplatesfileiodeformationexportanonymousdeformed_feature_geometry_seq_type) | typedef | — | — | 0 | Typedef for a sequence of TopologyReconstructedFeatureGeometry objects. |
| [`GPlatesFileIO::DeformationExport::(anonymous)::grouped_features_seq_type`](#gplatesfileiodeformationexportanonymousgrouped_features_seq_type) | typedef | — | — | 0 | Typedef for a sequence of FeatureCollectionFeatureGroup objects. |
| [`GPlatesFileIO::DeformationExport::PrincipalStrainOptions`](#gplatesfileiodeformationexportprincipalstrainoptions) | struct | — | — | 0 | Options for exporting principal strain/stretch. |

## Members

### `GPlatesFileIO::DeformationExport::(anonymous)::deformed_feature_geometry_seq_type`

*None.*

### `GPlatesFileIO::DeformationExport::(anonymous)::grouped_features_seq_type`

*None.*

### `GPlatesFileIO::DeformationExport::PrincipalStrainOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OutputType` | enum | `None` | public | — |
| `FormatType` | enum | `None` | public | — |
| `PrincipalStrainOptions( OutputType output_, FormatType format_)` | constructor | `None` | public | — |
| `get_principal_angle_or_azimuth_in_degrees( const GPlatesAppLogic::DeformationStrain::StrainPrincipal &principal_strain)` | method | `double` | public | Returns the angle or azimuth from the specified principal strain. |
| `output` | field | `OutputType` | public | — |
| `format` | field | `FormatType` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_DEFORMATIONEXPORT_H` | macro | `None` | — |
| `export_deformation_to_gpml_format( const QString &filename, const std::vector<const GPlatesAppLogic::TopologyReconstructedFeatureGeometry *> &deformed_feature_geometry_seq, GPlatesModel::ModelInterface &model, const std::vector<const File::Reference *> &active_files, boost::optional<PrincipalStrainOptions> include_prin ...` | function | `void` | Exports TopologyReconstructedFeatureGeometry objects containing deformation information to the GPML file format. |
| `export_deformation_to_gmt_format( const QString &filename, const std::vector<const GPlatesAppLogic::TopologyReconstructedFeatureGeometry *> &deformed_feature_geometry_seq, const std::vector<const File::Reference *> &active_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &r ...` | function | `void` | Exports TopologyReconstructedFeatureGeometry objects containing deformation information to the GMT file format. |

## Notes

- Both entry points throw `ErrorOpeningFileForWritingException` if the target file cannot be opened.
- `PrincipalStrainOptions::OutputType` is `STRAIN` (extension positive, compression negative) or `STRETCH` (`1.0 + strain`, plottable directly as an ellipse) — the two are not interchangeable without conversion, and the exported property name (`PrincipalStrain*` vs `PrincipalStretch*`) changes to match.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlFormatDeformationExport](GpmlFormatDeformationExport.md) | file-io | 66 |
| [file-io/GMTFormatDeformationExport](GMTFormatDeformationExport.md) | file-io | 34 |
| [gui/ExportDeformationAnimationStrategy](../gui/ExportDeformationAnimationStrategy.md) | gui | 22 |
| [file-io/ExportTemplateFilenameSequenceImpl](ExportTemplateFilenameSequenceImpl.md) | file-io | 18 |
| [gui/ExportAnimationRegistry](../gui/ExportAnimationRegistry.md) | gui | 16 |
| [qt-widgets/ExportDeformationOptionsWidget](../qt-widgets/ExportDeformationOptionsWidget.md) | qt-widgets | 16 |
| [unit-test/FilterTest](../unit-test/FilterTest.md) | unit-test | 2 |
| [file-io/GMTFormatHeader](GMTFormatHeader.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/DeformationExport.h
python scripts/gpq.py def GPlatesFileIO::DeformationExport::PrincipalStrainOptions --body
python scripts/gpq.py uses PrincipalStrainOptions --kind struct
python scripts/gpq.py hier PrincipalStrainOptions
```
