# TimeSpanUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 58 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TimeSpanUtils.h` | C++ | 1058 |
| `src/app-logic/TimeSpanUtils.cc` | C++ | 237 |

## Overview

Anything in GPlates that steps through geological time rather than evaluating a
single instant needs the same two things: a discretisation of a time interval into
numbered slots, and a table of per-slot results. `TimeRange` is the discretisation and
`TimeSpan<T>` is the table. Slot 0 is the begin time — the *oldest* time — and slot
`n-1` is the end time, with `get_time(slot) = begin_time - slot * time_increment`, so
the slot index runs forward in time while the time value decreases. Everything
downstream inherits that orientation: `TopologyReconstruct::GeometryTimeSpan` keeps a
`TimeWindowSpan<GeometrySample::non_null_ptr_type>` and its resolved boundary and
network tables are `TimeSampleSpan`s, `ReconstructContext` keeps a
`TimeSampleSpan<ReconstructedFeatureGeometry::non_null_ptr_type>`, and
`ScalarCoverageEvolution` keeps a `TimeWindowSpan<EvolvedScalarCoverage::non_null_ptr_type>`.

The two `TimeSpan<T>` implementations trade memory against lookup cost, and the
choice between them is the reason this header exists in two halves.
`TimeSampleSpan` is a dense `std::vector<boost::optional<T>>` sized to the whole
range: constant-time lookup, but one slot allocated per time step whether or not the
feature exists then. `TimeWindowSpan` stores only the initialised slots, as a
`std::list` of `TimeWindow` runs of contiguous slots, each run a `std::deque`; setting
a slot extends a window at either end, merges two windows that become adjacent, or
starts a new one. That matters for deformation, where a feature may be active over a
small part of a range that is sampled at every million years.

`TimeWindowSpan` also carries the two `boost::function` callbacks that let it answer
for times it has no sample for. `get_or_create_sample` — the only method that uses
them — resolves a time to bounding slots via `TimeRange::get_bounding_time_slots`;
if the time lands between two initialised slots it calls the interpolator, and
otherwise it calls the creator with the requested time plus a *source* sample and the
source's time: the first sample of the next window forward in time if there is one,
and the present-day sample (with source time 0) if there is not. That is how a
geometry can be asked for at any non-negative time, including present day and times
outside the range entirely, without the span having to store a sample there.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::TimeSpanUtils::TimeRange`](#gplatesapplogictimespanutilstimerange) | class | — | — | 0 | A time range consisting of time slots where the following constraints hold: begin\_time = end\_time + (num\_time\_slots - 1) \* time\_increment num\_time\_slots \>= 2 |
| [`GPlatesAppLogic::TimeSpanUtils::TimeSpan`](#gplatesapplogictimespanutilstimespan) | class | [`GPlatesUtils::ReferenceCount< TimeSpan<T> >`](../utils/ReferenceCount.md) | `<typename T>` | 2 | Interface to look samples of 'T' over a time range. |
| [`GPlatesAppLogic::TimeSpanUtils::TimeSampleSpan`](#gplatesapplogictimespanutilstimesamplespan) | class | [`TimeSpan<T>`](TimeSpanUtils.md) | `<typename T>` | 0 | A look up table of samples of 'T' over a time span. |
| [`GPlatesAppLogic::TimeSpanUtils::TimeWindowSpan`](#gplatesapplogictimespanutilstimewindowspan) | class | [`TimeSpan<T>`](TimeSpanUtils.md) | `<typename T>` | 0 | A look up table of samples of 'T' over a time span implemented using time windows. |

## Members

### `GPlatesAppLogic::TimeSpanUtils::TimeRange`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Adjust` | enum | `None` | public | Whether to adjust begin time, end time or time increment such that the constraints hold: begin\_time = end\_time + (num\_time\_slots - 1) \* time\_increment num\_time\_slots \>= 2 |
| `TimeRange( const double &begin_time, const double &end_time, const double &time_increment, Adjust adjust)` | constructor | `None` | public | Create a time range and adjust, if necessary, begin\_time, end\_time or time\_increment depending on adjust. |
| `TimeRange( const double &begin_time, const double &end_time, unsigned int num_time_slots)` | constructor | `None` | public | Create a time range where the time increment is: time\_increment = (begin\_time - end\_time) / (num\_time\_slots - 1) Throws exception if num\_time\_slots is less than two, or if end\_time is less than or equal to begin\_time. |
| `get_num_time_slots()` | method | `unsigned int` | public | Returns the number of time slots in the time range. |
| `get_num_time_intervals()` | method | `unsigned int` | public | Returns the number of time intervals in the time range. |
| `get_time_period()` | method | `double` | public | Returns the time period of this time range (from begin time to end time). |
| `get_time( unsigned int time_slot)` | method | `double` | public | Returns the time associated with the specified time slot. |
| `get_time_slot( const double &time)` | method | `boost::optional<unsigned int>` | public | Returns the matching time slot if the specified time matches (within epsilon) the time of a time slot. |
| `get_nearest_time_slot( const double &time)` | method | `boost::optional<unsigned int>` | public | Returns the nearest time slot for the specified time. |
| `get_bounding_time_slots( const double &time, double &interpolate_position)` | method | `boost::optional< std::pair<unsigned int/*first_time_slot*/, unsigned int/*second_time_slot*/> >` | public | Returns the two time slots that bound the specified time (if any). |
| `d_begin_time` | field | `double` | private | — |
| `d_end_time` | field | `double` | private | — |
| `d_time_increment` | field | `double` | private | — |
| `d_num_time_slots` | field | `unsigned int` | private | — |
| `calc_num_time_slots( const double &begin_time, const double &end_time, const double &time_increment)` | method | `unsigned int` | private | Returns the number of time slots rounded up to the nearest integer. |

### `GPlatesAppLogic::TimeSpanUtils::TimeSpan`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TimeSpan>` | public | A convenience typedef for a shared pointer to a non-const TimeSpan. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TimeSpan>` | public | A convenience typedef for a shared pointer to a const TimeSpan. |
| `sample_type` | typedef | `T` | public | Typedef for the object type in each sample. |
| `~TimeSpan()` | destructor | `None` | public | — |
| `get_time_range()` | method | `TimeRange` | public | Returns the time range of the time span. |
| `empty()` | method | `bool` | public | Returns true if set\_sample\_in\_time\_slot has not been called for any time slots. |
| `set_sample_in_time_slot` | field | `T` | public | Set the sample for the specified time slot (and return it). |
| `get_sample_in_time_slot( unsigned int time_slot)` | method | `boost::optional<const T &>` | public | Get the sample for the specified time slot. |
| `get_nearest_sample_at_time( const double &time)` | method | `boost::optional<const T &>` | public | Get the sample in the nearest time slot for the specified time. |

### `GPlatesAppLogic::TimeSpanUtils::TimeSampleSpan`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TimeSampleSpan>` | public | A convenience typedef for a shared pointer to a non-const TimeSampleSpan. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TimeSampleSpan>` | public | A convenience typedef for a shared pointer to a const TimeSampleSpan. |
| `create( const TimeRange &time_range)` | method | `non_null_ptr_type` | public | Allocate a look up table with as many slots as there are in time\_range. |
| `get_time_range()` | method | `TimeRange` | public | Returns the time range of the time span. |
| `empty()` | method | `bool` | public | Returns true if set\_sample\_in\_time\_slot has not been called for any time slots. |
| `set_sample_in_time_slot` | field | `T` | public | Set the sample for the specified time slot (and return it). |
| `get_sample_in_time_slot( unsigned int time_slot)` | method | `boost::optional<const T &>` | public | Get the sample for the specified time slot. |
| `sample_time_seq_type` | typedef | `std::vector< boost::optional<T> >` | private | Typedef for a time sequence of samples. |
| `d_time_range` | field | `TimeRange` | private | — |
| `d_sample_time_sequence` | field | `sample_time_seq_type` | private | — |
| `d_is_empty` | field | `bool` | private | — |
| `TimeSampleSpan( const TimeRange &time_range)` | constructor | `None` | private | — |

### `GPlatesAppLogic::TimeSpanUtils::TimeWindowSpan`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TimeWindowSpan>` | public | A convenience typedef for a shared pointer to a non-const TimeWindowSpan. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TimeWindowSpan>` | public | A convenience typedef for a shared pointer to a const TimeWindowSpan. |
| `sample_creator_function_type` | typedef | `boost::function< T ( const double &, const double &, const T &)>` | public | Convenience typedef for a function that creates a sample from another sample. |
| `interpolator_function_type` | typedef | `boost::function< T ( const double &, const double &, const double &, const T &, const T &)>` | public | Convenience typedef for a function that interpolates two adjacent samples. |
| `create( const TimeRange &time_range, const sample_creator_function_type &sample_creator_function, const interpolator_function_type &interpolator_function, const T &present_day_sample)` | method | `non_null_ptr_type` | public | Create a TimeWindowSpan. |
| `get_time_range()` | method | `TimeRange` | public | Returns the time range of the time span. |
| `empty()` | method | `bool` | public | Returns true if set\_sample\_in\_time\_slot has not been called for any time slots. |
| `set_sample_in_time_slot` | field | `T` | public | Set the sample for the specified time slot (and return it). |
| `get_sample_in_time_slot( unsigned int time_slot)` | method | `boost::optional<const T &>` | public | Get the sample for the specified time slot. |
| `get_or_create_sample( const double &time)` | method | `T` | public | Returns the sample associated with the time slot of the specified time, or creates a sample if the specified time does not correspond to an initialised time slot (ie, a time slot where get\_sample\_in\_time\_slot returns none). |
| `TimeWindow` | struct | `None` | private | A time window containing a contiguous time span of samples. |
| `time_window_seq_type` | typedef | `std::list<TimeWindow>` | private | Typedef for a sequence of time windows. |
| `d_time_range` | field | `TimeRange` | private | — |
| `d_sample_creator_function` | field | `sample_creator_function_type` | private | — |
| `d_interpolator_function` | field | `interpolator_function_type` | private | — |
| `d_present_day_sample` | field | `T` | private | — |
| `d_time_windows` | field | `time_window_seq_type` | private | — |
| `TimeWindowSpan( const TimeRange &time_range, const sample_creator_function_type &sample_creator_function, const interpolator_function_type &interpolator_function, const T &present_day_sample)` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_TIMESPANUTILS_H` | macro | `None` | — |

## Notes

**The `Adjust` constructor moves one of the values you passed it.** It rounds the
slot count *up* — `calc_num_time_slots` adds `1 - 1e-6` before truncating — and then
rewrites begin time, end time or the increment so that
`begin_time = end_time + (num_time_slots - 1) * time_increment` holds exactly. The
header's own example: begin 12.1, end 10.0, increment 1.0 with `ADJUST_BEGIN_TIME`
gives four slots at 13.0, 12.0, 11.0 and 10.0, so the begin time you get back is
older than the one you asked for. Read the accessors back rather than assuming your
inputs survived. Both constructors assert `begin_time > end_time`, and the range is
never degenerate: at least two slots, at least one interval.

**Three different "not found" answers.** `get_bounding_time_slots` returns none only
for a time outside `[end_time, begin_time]`, and signals "exactly on a slot" by
returning the same slot twice with `interpolate_position == 0`; snapping to a slot
uses `GPlatesMaths::GEO_TIMES_EPSILON`, at both ends of the interval, so a position
just under 1 is reported as slot `first + 1` rather than an interpolation.
`get_time_slot` narrows that to none for a time that is inside the range but between
slots. `get_sample_in_time_slot` returns none for an *uninitialised* slot but
**throws** `PreconditionViolationError` for an out-of-range slot index — an assert,
not a return value, on both implementations and on `set_sample_in_time_slot`.

**References into a `TimeWindowSpan` do not survive a merge.** `TimeWindow` uses a
`deque` deliberately, so pushing at either end keeps existing element references
valid, and the code relies on that when it returns a reference to a just-inserted
front sample. But the merge path copies the previous window's samples into the
current window's deque and then erases the previous window: every reference
previously handed out for a slot in that erased window dangles. Hold slot indices,
not references, across further `set_sample_in_time_slot` calls. Lookup on
`TimeWindowSpan` is also a linear walk of the window list, unlike the vector indexing
in `TimeSampleSpan`; a span that fragments into many windows pays for it on every
access.

**Ownership and lifetime.** `TimeSpan<T>` derives from `ReferenceCount<TimeSpan<T>>`
and has a virtual destructor, so instances are shared through
`non_null_intrusive_ptr` and deleting through the base pointer is safe; note that each
subclass redeclares `non_null_ptr_type` for its own type over the same count. `T` is
copied into and out of the tables (`get_or_create_sample` returns by value), which is
why the real instantiations all use `non_null_ptr_type` element types rather than the
objects themselves. `empty()` on `TimeSampleSpan` is a latch — `d_is_empty` is only
ever cleared, never restored — so it means "nothing was ever set", not "nothing is
set now".

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 76 |
| [app-logic/ScalarCoverageEvolution](ScalarCoverageEvolution.md) | app-logic | 39 |
| [app-logic/ReconstructContext](ReconstructContext.md) | app-logic | 36 |
| [app-logic/ReconstructLayerProxy](ReconstructLayerProxy.md) | app-logic | 17 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 7 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 5 |
| [app-logic/ScalarCoverageTimeSpan](ScalarCoverageTimeSpan.md) | app-logic | 3 |
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 3 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 3 |
| [app-logic/TopologyReconstructedFeatureGeometry](TopologyReconstructedFeatureGeometry.md) | app-logic | 2 |
| [app-logic/ReconstructScalarCoverageLayerParams](ReconstructScalarCoverageLayerParams.md) | app-logic | 1 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 1 |
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 1 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TimeSpanUtils.h
python scripts/gpq.py def GPlatesAppLogic::TimeSpanUtils::TimeWindowSpan --body
python scripts/gpq.py uses TimeWindowSpan --kind class
python scripts/gpq.py hier TimeWindowSpan
```
