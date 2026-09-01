# TotalReconstructionSequenceRotationInterpolater

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 1261 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/TotalReconstructionSequenceRotationInterpolater.h` | C++ | 111 |
| `src/feature-visitors/TotalReconstructionSequenceRotationInterpolater.cc` | C++ | 303 |

## Overview

[[[PROSE overview unit=feature-visitors/TotalReconstructionSequenceRotationInterpolater tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::TotalReconstructionSequenceRotationInterpolater`](#gplatesfeaturevisitorstotalreconstructionsequencerotationinterpolater) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Interpolate a finite rotation from a total reconstruction sequence for a particular reconstruction time. |

## Members

### `GPlatesFeatureVisitors::TotalReconstructionSequenceRotationInterpolater`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TotalReconstructionSequenceRotationInterpolater( const double &recon_time)` | constructor | `None` | public | — |
| `~TotalReconstructionSequenceRotationInterpolater()` | destructor | `None` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `visit_gpml_finite_rotation( const GPlatesPropertyValues::GpmlFiniteRotation &gpml_finite_rotation)` | method | `void` | protected | — |
| `visit_gpml_finite_rotation_slerp( const GPlatesPropertyValues::GpmlFiniteRotationSlerp &gpml_finite_rotation_slerp)` | method | `void` | protected | — |
| `visit_gpml_irregular_sampling( const GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | protected | — |
| `d_recon_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | — |
| `d_is_expecting_a_finite_rotation` | field | `bool` | private | — |
| `d_trp_time_matches_exactly` | field | `bool` | private | — |
| `d_finite_rotation_result` | field | `boost::optional<GPlatesMaths::FiniteRotation>` | private | — |
| `d_finite_rotation_for_interp` | field | `boost::optional<GPlatesMaths::FiniteRotation>` | private | — |
| `TotalReconstructionSequenceRotationInterpolater( const TotalReconstructionSequenceRotationInterpolater &)` | constructor | `None` | private | This constructor should never be defined, because we don't want to allow copy-construction. |
| `operator=` | field | `TotalReconstructionSequenceRotationInterpolater` | private | This operator should never be defined, because we don't want to allow copy-assignment. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FEATUREVISITORS_TOTALRECONSTRUCTIONSEQUENCEROTATIONINTERPOLATER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=feature-visitors/TotalReconstructionSequenceRotationInterpolater tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ApplyReconstructionPoleAdjustmentDialog](../qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/TotalReconstructionSequenceRotationInterpolater.h
python scripts/gpq.py def GPlatesFeatureVisitors::TotalReconstructionSequenceRotationInterpolater --body
python scripts/gpq.py uses TotalReconstructionSequenceRotationInterpolater --kind class
python scripts/gpq.py hier TotalReconstructionSequenceRotationInterpolater
```
