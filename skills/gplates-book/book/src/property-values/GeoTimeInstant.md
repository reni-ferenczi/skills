# GeoTimeInstant

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 186 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GeoTimeInstant.h` | C++ | 265 |
| `src/property-values/GeoTimeInstant.cc` | C++ | 348 |

## Overview

[[[PROSE overview unit=property-values/GeoTimeInstant tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GeoTimeInstant`](#gplatespropertyvaluesgeotimeinstant) | class | `boost::less_than_comparable<GeoTimeInstant>`<br>`boost::equality_comparable<GeoTimeInstant>`<br>`boost::equivalent<GeoTimeInstant>`<br>[`GPlatesUtils::QtStreamable<GeoTimeInstant>`](../utils/QtStreamable.md) | — | 0 | Instances of this class represent an instant in geological time, resolved and refined into a form which GPlates can efficiently process. |

## Members

### `GPlatesPropertyValues::GeoTimeInstant`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TimePositionTypes` | struct | `None` | private | — |
| `create_distant_past()` | method | `GeoTimeInstant` | public | Create a GeoTimeInstant instance for the distant past. |
| `create_distant_future()` | method | `GeoTimeInstant` | public | Create a GeoTimeInstant instance for the distant future. |
| `GeoTimeInstant( const double &value_)` | constructor | `None` | public | Create a GeoTimeInstant instance for a time-position of value million years ago. |
| `value()` | method | `double` | public | Access the floating-point representation of the time-position of this instance. |
| `is_distant_past()` | method | `bool` | public | Return true if this instance is a time-instant in the distant past; false otherwise. |
| `is_distant_future()` | method | `bool` | public | Return true if this instance is a time-instant in the distant future; false otherwise. |
| `is_real()` | method | `bool` | public | Return true if this instance is a time-instant whose time-position may be expressed as a "real" floating-point number; false otherwise. |
| `is_strictly_earlier_than( const GeoTimeInstant &other)` | method | `bool` | public | Return true if this instance is strictly earlier than other; false otherwise. |
| `is_earlier_than_or_coincident_with( const GeoTimeInstant &other)` | method | `bool` | public | Return true if this instance is either earlier than other or temporally-coincident with other; false otherwise. |
| `is_strictly_later_than( const GeoTimeInstant &other)` | method | `bool` | public | Return true if this instance is later than other; false otherwise. |
| `is_later_than_or_coincident_with( const GeoTimeInstant &other)` | method | `bool` | public | Return true if this instance is either later than other or temporally-coincident with other; false otherwise. |
| `is_coincident_with( const GeoTimeInstant &other)` | method | `bool` | public | Return true if this instance is temporally-coincident with other; false otherwise. |
| `operator<( const GeoTimeInstant &rhs)` | operator | `bool` | public | Less than comparison operator - all other operators supplied by Boost. |
| `d_type` | field | `TimePositionTypes::TimePositionType` | private | — |
| `d_value` | field | `double` | private | — |
| `GeoTimeInstant( TimePositionTypes::TimePositionType type_, const double &value_)` | constructor | `None` | private | Create a GeoTimeInstant instance for a time-position type type\_. |
| `transcribe_construct_data( GPlatesScribe::Scribe &scribe, GPlatesScribe::ConstructObject<GeoTimeInstant> &geo_time_instant)` | method | `GPlatesScribe::TranscribeResult` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator<( const GeoTimeInstant &other)` | operator | `bool` | — |
| `GPLATES_PROPERTYVALUES_GEOTIMEINSTANT_H` | macro | `None` | — |
| `operator<<` | variable | `std::ostream` | — |

## Notes

[[[PROSE notes unit=property-values/GeoTimeInstant tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 61 |
| [presentation/ReconstructVisualLayerParams](../presentation/ReconstructVisualLayerParams.md) | presentation | 37 |
| [gui/TopologySectionsTableColumns](../gui/TopologySectionsTableColumns.md) | gui | 31 |
| [qt-widgets/EditTimePeriodWidget](../qt-widgets/EditTimePeriodWidget.md) | qt-widgets | 31 |
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 27 |
| [qt-widgets/SetVGPVisibilityDialog](../qt-widgets/SetVGPVisibilityDialog.md) | qt-widgets | 27 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 21 |
| [app-logic/ReconstructedFeatureGeometry](../app-logic/ReconstructedFeatureGeometry.md) | app-logic | 21 |
| [app-logic/ReconstructionTree](../app-logic/ReconstructionTree.md) | app-logic | 21 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 21 |
| [app-logic/deprecated/PaleomagUtils](../app-logic/deprecated/PaleomagUtils.md) | app-logic | 20 |
| [qt-widgets/EditOldPlatesHeaderWidget](../qt-widgets/EditOldPlatesHeaderWidget.md) | qt-widgets | 18 |
| [utils/FeatureUtils](../utils/FeatureUtils.md) | utils | 18 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 17 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 17 |
| [app-logic/ReconstructionFeatureProperties](../app-logic/ReconstructionFeatureProperties.md) | app-logic | 16 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 16 |
| [feature-visitors/TotalReconstructionSequenceRotationInterpolater](../feature-visitors/TotalReconstructionSequenceRotationInterpolater.md) | feature-visitors | 16 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 16 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 16 |

*... and 141 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GeoTimeInstant.h
python scripts/gpq.py def GPlatesPropertyValues::GeoTimeInstant --body
python scripts/gpq.py uses GeoTimeInstant --kind class
python scripts/gpq.py hier GeoTimeInstant
```
