# GeoTimeInstant

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 186 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GeoTimeInstant.h` | C++ | 265 |
| `src/property-values/GeoTimeInstant.cc` | C++ | 348 |

## Overview

`GeoTimeInstant` is the scalar time type the whole application reconstructs against. It lives in `property-values` but it is deliberately *not* a `PropertyValue`: it has no revisioning, no visitor hook and no `non_null_ptr_type`, and it is copied by value. The property-value type that does sit in the model hierarchy is `GmlTimeInstant`, which wraps one `GeoTimeInstant` plus the GML XML attributes; `GmlTimePeriod` in turn holds a begin and an end `GmlTimeInstant`. Everything downstream of the model — reconstruction times, feature validity ranges, animation frames — passes `GeoTimeInstant` around directly.

The design problem it solves is that geological time has two open ends. A GML `timePosition` may say "0 Ma", but it may equally say "distant past" or "distant future", and those have to compare correctly against real times without every caller writing a special case. The class encodes that as a private three-valued `TimePositionTypes::TimePositionType` (`Real`, `DistantPast`, `DistantFuture`) alongside a `double`, and keeps the two consistent: the distant past *is* positive infinity and the distant future *is* negative infinity, so `value()` is always meaningful and the ordering falls out of ordinary arithmetic for the `Real`/`Real` case. The public constructor infers the type from the value, which means `GeoTimeInstant(GPlatesMaths::positive_infinity<double>())` and `create_distant_past()` produce the same object.

The comparison surface is intentionally wider than `operator<` alone. The named predicates (`is_strictly_earlier_than`, `is_earlier_than_or_coincident_with`, and their mirrors, plus `is_coincident_with`) exist because "earlier" is the reader-facing question, and because the sign convention is inverted relative to the number line — larger doubles are *further in the past*. `operator<` therefore means "earlier than", and sorting a container of `GeoTimeInstant` by `<` gives descending numeric order. The Boost operator bases supply `>`, `<=`, `>=`, `==` and `!=` from that one operator, and `GPlatesUtils::QtStreamable` lifts the `std::ostream` inserter (which prints `(distant past)` / `(distant future)` for the non-real cases) into `qDebug()` and `QTextStream`.

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

**NaN aborts the process.** The public constructor classifies its argument as finite, `+inf` or `-inf`; anything else falls through to `GPlatesGlobal::Abort(GPLATES_ASSERTION_SOURCE)`. This is not a thrown exception you can catch — validate user input or file input *before* building a `GeoTimeInstant`.

**Equality is approximate, and therefore not transitive.** Both `is_coincident_with` and the Boost-generated `operator==` treat two real times as equal when they lie within `GPlatesMaths::GEO_TIMES_EPSILON` (1.0e-9, `src/maths/MathsUtils.h`). `operator<` is written as `diff > GEO_TIMES_EPSILON` specifically so that `!(x < y) && !(y < x)` holds inside the epsilon band, which is what `boost::equivalent` and `std::map` require of a strict weak ordering. Strictly speaking epsilon comparison is not transitive, so a `std::map<GeoTimeInstant, ...>` can behave surprisingly when keys are spaced at around the epsilon; in practice geological times are many orders of magnitude larger, and the code relies on that. If you add a comparison method here, route it through the same epsilon rather than comparing `d_value` raw.

**Two distant instants of the same kind compare equal.** Two "distant past" instants are coincident, as are two "distant future" ones, even though nothing is actually known about when they were. The `.cc` comment flags this as a deliberate choice, not an accident, and it is what makes the `operator<`-derived `operator==` self-consistent.

**Transcription only stores the double.** `transcribe_construct_data` and `transcribe` write `d_value` through `transcribe_delegate_protocol` and re-derive `d_type` on load, which makes `GeoTimeInstant`, `GPlatesMaths::Real`, `double` and `float` interchangeable in saved sessions and projects. The one asymmetry is NaN: the other three types can carry it, so loading a NaN into a `GeoTimeInstant` returns `TRANSCRIBE_INCOMPATIBLE` rather than aborting. If you ever add a field to this class, note that the archive format has no slot for it and existing archives would need a version bump.

The type is immutable after construction (only the private transcribe path writes the fields), has no heap state and no ownership, so instances are freely copyable and safe to share across threads.

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
