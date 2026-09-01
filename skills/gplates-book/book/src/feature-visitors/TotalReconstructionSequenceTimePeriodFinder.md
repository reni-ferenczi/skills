# TotalReconstructionSequenceTimePeriodFinder

[Book TOC](../../TOC.md) · [feature-visitors](../../components/feature-visitors.md) · cluster Community 192 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/feature-visitors/TotalReconstructionSequenceTimePeriodFinder.h` | C++ | 142 |
| `src/feature-visitors/TotalReconstructionSequenceTimePeriodFinder.cc` | C++ | 154 |

## Overview

[[[PROSE overview unit=feature-visitors/TotalReconstructionSequenceTimePeriodFinder tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=feature-visitors/TotalReconstructionSequenceTimePeriodFinder tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
