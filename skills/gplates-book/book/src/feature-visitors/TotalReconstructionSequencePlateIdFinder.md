# TotalReconstructionSequencePlateIdFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 192 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/TotalReconstructionSequencePlateIdFinder.h` | C++ | 103 |
| `src/feature-visitors/TotalReconstructionSequencePlateIdFinder.cc` | C++ | 109 |

## Overview

[[[PROSE overview unit=feature-visitors/TotalReconstructionSequencePlateIdFinder tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=feature-visitors/TotalReconstructionSequencePlateIdFinder tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
