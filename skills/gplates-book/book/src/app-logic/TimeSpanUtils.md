# TimeSpanUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 58 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TimeSpanUtils.h` | C++ | 1058 |
| `src/app-logic/TimeSpanUtils.cc` | C++ | 237 |

## Overview

[[[PROSE overview unit=app-logic/TimeSpanUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/TimeSpanUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
