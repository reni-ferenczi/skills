# TRSUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 457 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TRSUtils.h` | C++ | 141 |
| `src/app-logic/TRSUtils.cc` | C++ | 238 |

## Overview

Helpers for working with Total Reconstruction Sequence (TRS) features — the `gpml:TotalReconstructionSequence` features that store rotation-file poles as model features rather than as raw `.rot` text. `TRSFinder` is a `FeatureVisitor` restricted (via `initialise_pre_property_values` and `d_property_names_to_allow`) to just the four properties a TRS can have — `gpml:fixedReferenceFrame`, `gpml:movingReferenceFrame`, `gpml:mprsAttributes`, `gpml:totalReconstructionPole` — and it records the fixed and moving plate IDs, the `GpmlIrregularSampling` holding the pole time samples, and the `FeatureHandle::iterator` for each so a caller (typically a rotation-editing dialog) can locate and rewrite those specific properties in place. `can_process_trs` reports whether all three pieces were actually found, since a malformed or non-TRS feature will leave some of them unset.

`build_trs_summary_string_from_trs_feature` and `one_of_trs_plate_ids_is_999` are independent of `TRSFinder` — they run `GPlatesFeatureVisitors::TotalReconstructionSequencePlateIdFinder`/`TotalReconstructionSequenceTimePeriodFinder` themselves to produce, respectively, a one-line "moving rel fixed [end : begin]" description for list widgets and a check for whether either plate ID is 999.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TRSUtils::TRSFinder`](#gplatesapplogictrsutilstrsfinder) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Finds irregular-sampling and plate-id properties, and their iterators, from a TRS feature. |

## Members

### `GPlatesAppLogic::TRSUtils::TRSFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TRSFinder()` | constructor | `None` | public | — |
| `~TRSFinder()` | destructor | `None` | public | — |
| `reset()` | method | `void` | public | — |
| `can_process_trs()` | method | `bool` | public | — |
| `irregular_sampling_property_iterator()` | method | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | public | — |
| `moving_ref_frame_property_iterator()` | method | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | public | — |
| `fixed_ref_frame_property_iterator()` | method | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | public | — |
| `initialise_pre_property_values( top_level_property_inline_type &top_level_property_inline)` | method | `bool` | private | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_irregular_sampling( GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | private | — |
| `visit_gpml_plate_id( GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | private | — |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |
| `d_irregular_sampling_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `d_irregular_sampling` | field | `boost::optional<GPlatesPropertyValues::GpmlIrregularSampling::non_null_ptr_type>` | private | — |
| `d_moving_ref_frame_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `d_moving_ref_frame_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_fixed_ref_frame_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `d_fixed_ref_frame_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | Copied from TotalReconstructionSequencePlateIdFinder |
| `GPLATESAPPLOGIC_TRSUTILS_H` | macro | `None` | — |
| `build_trs_summary_string_from_trs_feature( const GPlatesModel::FeatureHandle::weak_ref &trs_feature)` | function | `QString` | — |
| `one_of_trs_plate_ids_is_999(const GPlatesModel::FeatureHandle::weak_ref &trs_feature)` | function | `bool` | — |

## Notes

`TRSFinder` must be `reset()` before reuse on a different feature — the plate IDs, iterators and irregular sampling are only ever set from within `visit_*`, never cleared automatically between visits. `visit_gpml_plate_id` assumes it has already read a property name (dereferences `current_top_level_propname()` without checking), so `TRSFinder` relies on being driven through the normal feature-visitor traversal rather than being handed a plate ID value directly.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 21 |
| [qt-widgets/EditTotalReconstructionSequenceDialog](../qt-widgets/EditTotalReconstructionSequenceDialog.md) | qt-widgets | 12 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 2 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](../qt-widgets/CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 2 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TRSUtils.h
python scripts/gpq.py def GPlatesAppLogic::TRSUtils::TRSFinder --body
python scripts/gpq.py uses TRSFinder --kind class
python scripts/gpq.py hier TRSFinder
```
