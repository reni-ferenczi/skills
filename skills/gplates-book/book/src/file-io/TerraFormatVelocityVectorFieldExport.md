# TerraFormatVelocityVectorFieldExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 9 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/TerraFormatVelocityVectorFieldExport.h` | C++ | 70 |
| `src/file-io/TerraFormatVelocityVectorFieldExport.cc` | C++ | 229 |

## Overview

Exports reconstructed velocity vector fields to Terra text format, a data format used in geodynamic modelling. The namespace wraps `MultiPointVectorField` objects—which pair domain points on a sphere with velocity vectors—and writes them to a file with Terra parameters (grid dimensions `mt`, `nt`, `nd`, processor number, and reconstruction age). The export formats each domain point and its corresponding velocity as three double-precision components, writing them in a layout compatible with Terra's input expectations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::TerraFormatVelocityVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type`](#gplatesfileioterraformatvelocityvectorfieldexportanonymousmulti_point_vector_field_seq_type) | typedef | — | — | 0 | Convenience typedef for a sequence of MPVFs. |
| [`GPlatesFileIO::TerraFormatVelocityVectorFieldExport::velocity_vector_field_group_type`](#gplatesfileioterraformatvelocityvectorfieldexportvelocity_vector_field_group_type) | typedef | — | — | 0 | Typedef for a feature geometry group of MultiPointVectorField objects. |

## Members

### `GPlatesFileIO::TerraFormatVelocityVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type`

*None.*

### `GPlatesFileIO::TerraFormatVelocityVectorFieldExport::velocity_vector_field_group_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_terra_velocity_line( QTextStream &output_stream, const GPlatesMaths::Vector3D &velocity_vector)` | function | `void` | Outputs a velocity line to the Terra output consisting of velocity vector. |
| `print_terra_velocity_vector_field( QTextStream &output_stream, const GPlatesAppLogic::MultiPointVectorField &velocity_vector_field)` | function | `void` | Write the velocity vector field. |
| `GPLATES_FILE_IO_TERRAFORMATVELOCITYVECTORFIELDEXPORT_H` | macro | `None` | — |
| `export_velocity_vector_fields( const std::list<velocity_vector_field_group_type> &velocity_vector_field_group_seq, const QFileInfo& file_info, int terra_mt, int terra_nt, int terra_nd, int local_processor_number, int age)` | function | `void` | Exports MultiPointVectorField objects containing \*velocities\* to Terra text format. age is the reconstruction time rounded to an integer. |

## Notes

Velocity vectors are output with 16 decimal digits of precision and field width 19 characters. If a `MultiPointVectorField` has invalid or null codomain elements at a domain point, the exporter outputs a zero velocity for that point. The output file is opened in text mode for cross-platform line-ending handling. The helper functions `print_terra_velocity_line()` and `print_terra_velocity_vector_field()` are in an anonymous namespace and format the velocity data before streaming it to the output file; they are not meant for external use.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/MultiPointVectorFieldExport](MultiPointVectorFieldExport.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/TerraFormatVelocityVectorFieldExport.h
python scripts/gpq.py def GPlatesFileIO::TerraFormatVelocityVectorFieldExport::(anonymous)::multi_point_vector_field_seq_type --body
python scripts/gpq.py uses multi_point_vector_field_seq_type --kind typedef
```
