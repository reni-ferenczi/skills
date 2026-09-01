# GpmlOnePointFiveOutputVisitor

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 745 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/GpmlOnePointFiveOutputVisitor.h` | C++ | 138 |
| `src/file-io/deprecated/GpmlOnePointFiveOutputVisitor.cc` | C++ | 359 |

## Overview

[[[PROSE overview unit=file-io/deprecated/GpmlOnePointFiveOutputVisitor tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GpmlOnePointFiveOutputVisitor`](#gplatesfileiogpmlonepointfiveoutputvisitor) | class | [`GPlatesModel::ConstFeatureVisitor`](../../model/FeatureVisitor.md) | — | 0 | — |

## Members

### `GPlatesFileIO::GpmlOnePointFiveOutputVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GpmlOnePointFiveOutputVisitor( const XmlOutputInterface &xoi)` | constructor | `None` | public | — |
| `~GpmlOnePointFiveOutputVisitor()` | destructor | `None` | public | — |
| `visit_feature_handle( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | protected | — |
| `visit_top_level_property_inline( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `void` | protected | — |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | protected | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | protected | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | protected | — |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | protected | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_finite_rotation( const GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | protected | — |
| `visit_gpml_finite_rotation_slerp( const GPlatesPropertyValues::GpmlFiniteRotationSlerp &gpml_finite_rotation_slerp)` | method | `void` | protected | — |
| `visit_gpml_irregular_sampling( const GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | protected | — |
| `visit_gpml_old_plates_header( const GPlatesPropertyValues::GpmlOldPlatesHeader &gpml_old_plates_header)` | method | `void` | protected | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `visit_xs_string( const GPlatesPropertyValues::XsString &xs_string)` | method | `void` | protected | — |
| `d_output` | field | `XmlOutputInterface` | private | — |
| `write_gpml_time_sample( const GPlatesPropertyValues::GpmlTimeSample &gpml_time_sample)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GPMLONEPOINTFIVEOUTPUTVISITOR_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/deprecated/GpmlOnePointFiveOutputVisitor tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/deprecated/GpmlOnePointFiveOutputVisitor.h
python scripts/gpq.py def GPlatesFileIO::GpmlOnePointFiveOutputVisitor --body
python scripts/gpq.py uses GpmlOnePointFiveOutputVisitor --kind class
python scripts/gpq.py hier GpmlOnePointFiveOutputVisitor
```
