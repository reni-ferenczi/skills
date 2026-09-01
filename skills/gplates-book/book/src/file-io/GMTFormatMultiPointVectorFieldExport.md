# GMTFormatMultiPointVectorFieldExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 272 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GMTFormatMultiPointVectorFieldExport.h` | C++ | 97 |
| `src/file-io/GMTFormatMultiPointVectorFieldExport.cc` | C++ | 425 |

## Overview

Exports velocity vector fields to GMT format. The exporter writes `MultiPointVectorField` objects (collections of velocities sampled at multiple points) to a GMT file with selectable output options: domain points (spatial positions where velocities were calculated), velocity vectors in user-chosen format, and associated plate IDs. Velocity magnitudes can be scaled and output filtered by stride to control density. Output includes GMT headers with reconstruction metadata, and coordinates follow GMT xy-format conventions.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GMTFormatMultiPointVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type`](#gplatesfileiogmtformatmultipointvectorfieldexportanonymousmulti_point_vector_field_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of MPVFs. |
| [`GPlatesFileIO::GMTFormatMultiPointVectorFieldExport::multi_point_vector_field_group_type`](#gplatesfileiogmtformatmultipointvectorfieldexportmulti_point_vector_field_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of MultiPointVectorField objects. |
| [`GPlatesFileIO::GMTFormatMultiPointVectorFieldExport::referenced_files_collection_type`](#gplatesfileiogmtformatmultipointvectorfieldexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |

## Members

### `GPlatesFileIO::GMTFormatMultiPointVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type`

*None.*

### `GPlatesFileIO::GMTFormatMultiPointVectorFieldExport::multi_point_vector_field_group_type`

*None.*

### `GPlatesFileIO::GMTFormatMultiPointVectorFieldExport::referenced_files_collection_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_global_header_lines( std::vector<QString>& header_lines, const referenced_files_collection_type &referenced_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time)` | function | `void` | Prints GMT format header at top of the exported file containing information about the reconstruction that is not per-feature information. |
| `print_gmt_velocity_line( QTextStream &output_stream, const GPlatesMaths::PointOnSphere &domain_point, const GPlatesMaths::Vector3D &velocity_vector, GPlatesModel::integer_plate_id_type plate_id, MultiPointVectorFieldExport::GMTVelocityVectorFormatType velocity_vector_format, bool domain_point_lon_lat_format, bool inclu ...` | function | `void` | Outputs a velocity line to the GMT output consisting of velocity and optionally position and plate id. |
| `print_gmt_velocity_vector_field( QTextStream &output_stream, const GPlatesAppLogic::MultiPointVectorField &velocity_vector_field, MultiPointVectorFieldExport::GMTVelocityVectorFormatType velocity_vector_format, double velocity_scale, unsigned int &velocity_vector_index, unsigned int velocity_stride, bool domain_point_l ...` | function | `void` | Write the velocity vector field and optionally its domain positions and plate ids. |
| `GPLATES_FILE_IO_GMTFORMATMULTIPOINTVECTORFIELDEXPORT_H` | macro | `None` | — |
| `export_velocity_vector_fields( const std::list<multi_point_vector_field_group_type> &velocity_vector_field_group_seq, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const double &reconstruction_time, MultiP ...` | function | `void` | Exports MultiPointVectorField objects containing \*velocities\*. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/MultiPointVectorFieldExport](MultiPointVectorFieldExport.md) | file-io | 8 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GMTFormatMultiPointVectorFieldExport.h
python scripts/gpq.py def GPlatesFileIO::GMTFormatMultiPointVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type --body
python scripts/gpq.py uses multi_point_vector_field_seq_type --kind typedef
```
