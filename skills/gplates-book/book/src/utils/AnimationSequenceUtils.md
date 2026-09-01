# AnimationSequenceUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 752 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/AnimationSequenceUtils.h` | C++ | 136 |
| `src/utils/AnimationSequenceUtils.cc` | C++ | 180 |

## Overview

The `GPlatesUtils::AnimationSequence` namespace is the single place that turns a
desired start time, end time and time increment into a concrete frame-by-frame
animation schedule. It exists so that the two independent consumers of that
schedule — `AnimationController`, which drives on-screen playback, and
`ExportTemplateFilenameSequence`, which generates export filenames — always
agree on how many frames there are and what reconstruction time each one falls
on, rather than each re-deriving that arithmetic and risking drift between the
displayed animation and the exported files.

`calculate_sequence()` does the actual work, producing a `SequenceInfo` that
records both the caller's desired range and the range actually achieved. The
bulk of its logic handles the case where `(end_time - start_time)` is not an
exact multiple of the time increment: depending on `should_finish_exactly_on_end_time`,
it either drops the leftover span or adds a final "remainder frame" shorter
than the rest, and it uses `GPlatesMaths::are_geo_times_approximately_equal()`
to decide whether an apparent remainder is real or just floating-point noise
from the division. `calculate_time_for_frame()` then maps a frame index back
to a reconstruction time using the precomputed `SequenceInfo`, treating the
last frame as a special case so it lands exactly on `actual_end_time` even
when earlier frames were spaced by `raw_time_increment`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::AnimationSequence::size_type`](#gplatesutilsanimationsequencesize_type) | typedef | — | — | 0 | Typedef for frame indexes and sequence durations. |
| [`GPlatesUtils::AnimationSequence::SequenceInfo`](#gplatesutilsanimationsequencesequenceinfo) | struct | — | — | 0 | Struct to act as the return value from the calculate\_sequence() function. |
| [`GPlatesUtils::AnimationSequence::TimeIncrementZero`](#gplatesutilsanimationsequencetimeincrementzero) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | Exception thrown by calculate\_sequence() when given time increment is zero. |

## Members

### `GPlatesUtils::AnimationSequence::size_type`

*None.*

### `GPlatesUtils::AnimationSequence::SequenceInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `desired_start_time` | field | `double` | public | — |
| `desired_end_time` | field | `double` | public | — |
| `abs_time_increment` | field | `double` | public | — |
| `raw_time_increment` | field | `double` | public | — |
| `should_finish_exactly_on_end_time` | field | `bool` | public | — |
| `duration_in_frames` | field | `size_type` | public | — |
| `duration_in_ma` | field | `double` | public | — |
| `includes_remainder_frame` | field | `bool` | public | — |
| `remainder_frame_length` | field | `double` | public | — |
| `actual_start_time` | field | `double` | public | — |
| `actual_end_time` | field | `double` | public | — |

### `GPlatesUtils::AnimationSequence::TimeIncrementZero`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TimeIncrementZero( const GPlatesUtils::CallStack::Trace &src)` | constructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_ANIMATIONSEQUENCEUTILS_H` | macro | `None` | — |
| `calculate_sequence( const double &start_time, const double &end_time, const double &abs_time_increment, bool should_finish_exactly_on_end_time)` | function | `SequenceInfo` | Calculates everything you might want to know about a given animation sequence in one handy pass. |
| `raw_time_increment( const double &start_time, const double &end_time, const double &abs_time_increment)` | function | `double` | Adjusts an absolute-value time increment to be positive or negative, appropriate for iterating through the given range. |
| `calculate_time_for_frame( const SequenceInfo &sequence_info, const size_type &frame_index)` | function | `double` | Calculates the appropriate reconstruction time for the given SequenceInfo and frame index (starts at 0). |

## Notes

- `calculate_sequence()` throws `TimeIncrementZero` if `abs_time_increment` is
  (approximately) zero; callers must catch it rather than assume a valid
  `SequenceInfo` is always returned.
- A zero-length remainder is treated as "no remainder frame" even when
  `should_finish_exactly_on_end_time` is true: the near-zero check against
  `are_geo_times_approximately_equal()` exists specifically to absorb
  floating-point error in the range/increment division, not to model a real
  edge case.
- `raw_time_increment` (the field) carries a sign derived from whether
  `start_time < end_time`, independent of the `abs_time_increment` argument's
  sign; use it, not the input parameter, when stepping through frames.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/AnimationController](../gui/AnimationController.md) | gui | 26 |
| [file-io/ExportTemplateFilenameSequenceImpl](../file-io/ExportTemplateFilenameSequenceImpl.md) | file-io | 22 |
| [gui/ExportAnimationContext](../gui/ExportAnimationContext.md) | gui | 13 |
| [file-io/ExportTemplateFilenameSequence](../file-io/ExportTemplateFilenameSequence.md) | file-io | 7 |
| [qt-widgets/ExportAnimationDialog](../qt-widgets/ExportAnimationDialog.md) | qt-widgets | 5 |
| [gui/ExportAnimationStrategy](../gui/ExportAnimationStrategy.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/AnimationSequenceUtils.h
python scripts/gpq.py def GPlatesUtils::AnimationSequence::TimeIncrementZero --body
python scripts/gpq.py uses TimeIncrementZero --kind class
python scripts/gpq.py hier TimeIncrementZero
```
