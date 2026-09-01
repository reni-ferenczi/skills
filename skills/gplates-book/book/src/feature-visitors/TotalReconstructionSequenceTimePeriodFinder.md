# TotalReconstructionSequenceTimePeriodFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 192 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/TotalReconstructionSequenceTimePeriodFinder.h` | C++ | 142 |
| `src/feature-visitors/TotalReconstructionSequenceTimePeriodFinder.cc` | C++ | 154 |

## Overview

`TotalReconstructionSequenceTimePeriodFinder` scans the `gpml:totalReconstructionPole` property of a total reconstruction sequence (TRS) feature and derives the sequence's overall begin and end times from its `GpmlIrregularSampling` of `GpmlTimeSample`s. It assumes the samples are ordered most-recent first and progressively earlier, so it can take the first sample's time as a running `d_end_time` and the last non-anomalous sample's time as `d_begin_time`, tracking both as it iterates in `visit_gpml_irregular_sampling`.

By default the constructor sets `d_skip_over_disabled_samples` to `true`, which is what most callers want: disabled time samples are excluded from the begin/end calculation. Passing `false` keeps disabled samples in the scan instead, which is needed when displaying the raw contents of a rotation file, as in `TotalReconstructionSequencesDialog`, where every sample and every sequence should be shown regardless of its enabled state. It plays the same role as `TotalReconstructionSequencePlateIdFinder` but extracts the time period rather than the plate IDs.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFeatureVisitors::TotalReconstructionSequenceTimePeriodFinder`](#gplatesfeaturevisitorstotalreconstructionsequencetimeperiodfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | This const feature visitor finds the begin and end times of a total reconstruction sequence feature. |

## Members

### `GPlatesFeatureVisitors::TotalReconstructionSequenceTimePeriodFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TotalReconstructionSequenceTimePeriodFinder( bool skip_over_disabled_samples = true)` | constructor | `None` | public | Create a new finder instance. |
| `~TotalReconstructionSequenceTimePeriodFinder()` | destructor | `None` | public | — |
| `reset()` | method | `void` | public | Reset a TotalReconstructionSequenceTimePeriodFinder instance, as if it were freshly instantiated. |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &top_level_property_inline)` | method | `bool` | protected | — |
| `visit_gpml_irregular_sampling( const GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | protected | — |
| `d_skip_over_disabled_samples` | field | `bool` | private | Whether client code wants us to skip over any disabled time samples when iterating through the irregular sampling. |
| `d_property_names_to_allow` | field | `std::vector<GPlatesModel::PropertyName>` | private | — |
| `d_most_recent_propname_read` | field | `boost::optional<GPlatesModel::PropertyName>` | private | — |
| `d_begin_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_end_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `contains_elem( const C &container, const E &elem)` | function | `bool` | — |
| `GPLATES_FEATUREVISITORS_TOTALRECONSTRUCTIONSEQUENCETIMEPERIODFINDER_H` | macro | `None` | — |

## Notes

If a time sample's position is not a real value (i.e. distant-past or distant-future), or if samples appear out of the expected most-recent-first order (and are not disabled), `visit_gpml_irregular_sampling` logs a warning to `std::cerr` and otherwise ignores the anomaly rather than failing; both cases are marked `FIXME` as unresolved in the source. `begin_time()` and `end_time()` return `boost::none` when the sequence contained no usable (non-disabled) time samples, so callers must check before dereferencing.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/InsertVGPReconstructionPoleDialog](../qt-widgets/InsertVGPReconstructionPoleDialog.md) | qt-widgets | 4 |
| [qt-widgets/ModifyReconstructionPoleWidget](../qt-widgets/ModifyReconstructionPoleWidget.md) | qt-widgets | 4 |
| [app-logic/TRSUtils](../app-logic/TRSUtils.md) | app-logic | 2 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 2 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 1 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](../qt-widgets/CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditTotalReconstructionSequenceDialog](../qt-widgets/EditTotalReconstructionSequenceDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |
| [qt-widgets/deprecated/CreateTopologyWidget](../qt-widgets/deprecated/CreateTopologyWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/feature-visitors/TotalReconstructionSequenceTimePeriodFinder.h
python scripts/gpq.py def GPlatesFeatureVisitors::TotalReconstructionSequenceTimePeriodFinder --body
python scripts/gpq.py uses TotalReconstructionSequenceTimePeriodFinder --kind class
python scripts/gpq.py hier TotalReconstructionSequenceTimePeriodFinder
```
