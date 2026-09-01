# TotalReconstructionSequencePlateIdFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 192 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/TotalReconstructionSequencePlateIdFinder.h` | C++ | 103 |
| `src/feature-visitors/TotalReconstructionSequencePlateIdFinder.cc` | C++ | 109 |

## Overview

`TotalReconstructionSequencePlateIdFinder` walks a single total reconstruction sequence (TRS) feature and picks out its `gpml:fixedReferenceFrame` and `gpml:movingReferenceFrame` plate IDs. The constructor restricts `initialise_pre_property_values` to just those two property names, so the visitor skips straight past `gpml:totalReconstructionPole` and any other properties on the feature; `visit_gpml_constant_value` then unwraps the constant-value wrapper and `visit_gpml_plate_id` records the plate ID under whichever of the two names `current_top_level_propname()` reports.

Callers construct one instance, `accept_visitor` it over a TRS feature, then read back `fixed_ref_frame_plate_id()` and `moving_ref_frame_plate_id()`; `reset()` lets the same instance be reused across many features instead of reconstructing it each time. It is the plate-ID counterpart to `TotalReconstructionSequenceTimePeriodFinder`, which extracts the begin/end times from the same kind of feature.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::TotalReconstructionSequencePlateIdFinder`](#gplatesfeaturevisitorstotalreconstructionsequenceplateidfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | This const feature visitor finds the fixed and moving reference frame plate IDs within a total reconstruction sequence feature. |

## Members

### `GPlatesFeatureVisitors::TotalReconstructionSequencePlateIdFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TotalReconstructionSequencePlateIdFinder()` | constructor | `None` | public | FIXME: We should also pass the current reconstruction time, so we can correctly handle time-dependent property values. |
| `~TotalReconstructionSequencePlateIdFinder()` | destructor | `None` | public | — |
| `reset()` | method | `void` | public | Reset a TotalReconstructionSequencePlateIdFinder instance, as if it were freshly instantiated. |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | protected | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | protected | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | protected | — |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |
| `d_fixed_ref_frame_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_moving_ref_frame_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_FEATUREVISITORS_TOTALRECONSTRUCTIONSEQUENCEPLATEIDFINDER_H` | macro | `None` | — |

## Notes

`visit_gpml_plate_id` assumes a property name has already been read and dereferences `current_top_level_propname()` unconditionally; it relies on `initialise_pre_property_values` having filtered the visit to `fixedReferenceFrame` or `movingReferenceFrame` beforehand. The constructor's own `FIXME` notes that it ignores the current reconstruction time, so it cannot correctly resolve time-dependent property values.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/InsertVGPReconstructionPoleDialog](../qt-widgets/InsertVGPReconstructionPoleDialog.md) | qt-widgets | 13 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 10 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 4 |
| [app-logic/TRSUtils](../app-logic/TRSUtils.md) | app-logic | 3 |
| [feature-visitors/TotalReconstructionSequenceRotationInserter](TotalReconstructionSequenceRotationInserter.md) | feature-visitors | 2 |
| [file-io/FeatureCollectionFileFormatClassify](../file-io/FeatureCollectionFileFormatClassify.md) | file-io | 2 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](../qt-widgets/CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditTotalReconstructionSequenceDialog](../qt-widgets/EditTotalReconstructionSequenceDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/TotalReconstructionSequencePlateIdFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::TotalReconstructionSequencePlateIdFinder --body
python scripts/gpq.py uses TotalReconstructionSequencePlateIdFinder --kind class
python scripts/gpq.py hier TotalReconstructionSequencePlateIdFinder
```
