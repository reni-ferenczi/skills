# CitcomsFormatVelocityVectorFieldExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1367 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/CitcomsFormatVelocityVectorFieldExport.h` | C++ | 76 |
| `src/file-io/CitcomsFormatVelocityVectorFieldExport.cc` | C++ | 307 |

## Overview

[[[PROSE overview unit=file-io/CitcomsFormatVelocityVectorFieldExport tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::CitcomsFormatVelocityVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type`](#gplatesfileiocitcomsformatvelocityvectorfieldexportanonymousmulti_point_vector_field_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of MPVFs. |
| [`GPlatesFileIO::CitcomsFormatVelocityVectorFieldExport::velocity_vector_field_group_type`](#gplatesfileiocitcomsformatvelocityvectorfieldexportvelocity_vector_field_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of MultiPointVectorField objects. |

## Members

### `GPlatesFileIO::CitcomsFormatVelocityVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type`

*None.*

### `GPlatesFileIO::CitcomsFormatVelocityVectorFieldExport::velocity_vector_field_group_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_citcoms_velocity_line( QTextStream &output_stream, const GPlatesMaths::PointOnSphere &domain_point, const GPlatesMaths::Vector3D &velocity_vector)` | function | `void` | Outputs a velocity line to the CitcomS output consisting of velocity vector. |
| `print_citcoms_gmt_velocity_line( QTextStream &gmt_output_stream, const GPlatesMaths::PointOnSphere &domain_point, const GPlatesMaths::Vector3D &velocity_vector)` | function | `void` | Outputs a velocity line to the CitcomS-compatible GMT output consisting of a domain point as lat/lon and velocity azimuth and magnitude. |
| `print_citcoms_velocity_vector_field( QTextStream &output_stream, boost::optional<QTextStream> &gmt_output_stream, const GPlatesAppLogic::MultiPointVectorField &velocity_vector_field, double gmt_velocity_scale, unsigned int &velocity_vector_index, unsigned int gmt_velocity_stride)` | function | `void` | Write the velocity vector field. |
| `GPLATES_FILE_IO_CITCOMSFORMATVELOCITYVECTORFIELDEXPORT_H` | macro | `None` | — |
| `export_global_velocity_vector_fields( const std::list<velocity_vector_field_group_type> &velocity_vector_field_group_seq, const QFileInfo& file_info, int age, bool include_gmt_export, double gmt_velocity_scale, unsigned int gmt_velocity_stride)` | function | `void` | Exports MultiPointVectorField objects containing \*velocities\* to CitcomS global format. age is the reconstruction time rounded to an integer. |

## Notes

[[[PROSE notes unit=file-io/CitcomsFormatVelocityVectorFieldExport tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/MultiPointVectorFieldExport](MultiPointVectorFieldExport.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/CitcomsFormatVelocityVectorFieldExport.h
python scripts/gpq.py def GPlatesFileIO::CitcomsFormatVelocityVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type --body
python scripts/gpq.py uses multi_point_vector_field_seq_type --kind typedef
```
