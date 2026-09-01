# LatLonAreaSampling

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 698 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/LatLonAreaSampling.h` | C++ | 839 |

## Overview

`LatLonAreaSampling<ElementType>` decimates a dense set of points on the
sphere down to roughly one representative element per unit area, which is
what `view-operations/RenderedGeometryLayer` uses it for: thinning out point
markers that would otherwise overplot at low zoom. Elements are added via
`add_element` at a `GPlatesMaths::PointOnSphere` location; internally each is
converted to a `GPlatesMaths::LatLonPoint` and dropped into a `SampleBin`
looked up first by latitude row (`LatitudeLookup`) and then by longitude
within that row (`LongitudeLookup`). Only the element closest to each bin's
centre survives as that bin's "sample element" — `get_sampled_element`
iterates just those, not every element added. Longitude bin counts are
computed per latitude row (`reset_spacing`) so that a bin's east-west extent
along its small circle of latitude approximates the same surface distance as
its north-south extent, keeping the bins close to equal area near the poles
as well as the equator despite meridians converging.

Both bin lookups use an `ObjectPool` for storage, so bin addresses stay
stable once created, and an `IntrusiveSinglyLinkedList` to track which bins
and element entries exist without extra per-node allocation.
`LongitudeLookup` picks between two internal representations depending on
how many longitude bins that latitude row could need: below
`MAX_SAMPLE_BINS_FOR_HIGH_SPEED_LOOKUP` (500) it uses a flat array indexed
directly by longitude bin, and above that threshold it switches to a lower
memory layout that packs up to 8 bins' worth of pointers per `OuterBin` using
a bitmask and an intrusive list, trading lookup speed for roughly a quarter
of the memory. In both cases a `SampleBin` is only actually constructed the
first time an element lands in it, since most bins in a large lat/lon grid
typically end up unused.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::LatLonAreaSampling`](#gplatesutilslatlonareasampling) | class | — | `<typename ElementType>` | 0 | A roughly uniform area sampling of the sphere into segments aligned along latitude and longitude. |

## Members

### `GPlatesUtils::LatLonAreaSampling`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LatLonAreaSampling( const double &sample_bin_angle_spacing_degrees)` | constructor | `None` | public | Creates a lat/lon area sampling where the angular dimension of each lat/lon area bin is roughly sample\_bin\_angle\_spacing\_degrees. |
| `reset_sample_spacing( const double &sample_bin_angle_spacing_degrees)` | method | `void` | public | Changes the angular dimension of each lat/lon area bin to be roughly sample\_bin\_angle\_spacing\_degrees. |
| `empty()` | method | `bool` | public | Returns true if there are no sampled elements. |
| `get_num_sampled_elements()` | method | `unsigned int` | public | Returns the number of sampled elements. |
| `get_sampled_element` | field | `ElementType` | public | Returns the sampled element at index sampled\_element\_index. |
| `add_element( const ElementType &element, const GPlatesMaths::PointOnSphere &point_on_sphere_location)` | method | `void` | public | Add an element at the location on sphere point\_on\_sphere\_location. |
| `clear_elements()` | method | `void` | public | Removes all elements added with add\_element which also removes all sampled elements. |
| `sample_element_seq_type` | typedef | `std::vector<const ElementEntry *>` | private | Typedef for global sequence of sample elements. |
| `ElementEntry` | class | `None` | private | Keeps element together with its location on the sphere. |
| `LongitudeLookupFullListTag` | struct | `None` | private | — |
| `LongitudeLookupInnerListTag` | struct | `None` | private | — |
| `SampleBin` | class | `None` | private | Represents a single roughly equal-area sample area on surface of sphere. |
| `LongitudeLookup` | class | `None` | private | Handles lookups using longitude. |
| `LatitudeLookup` | class | `None` | private | Handles lookups using latitude. |
| `d_element_entry_storage` | field | `GPlatesUtils::ObjectPool<ElementEntry>` | private | — |
| `d_latitude_lookup` | field | `LatitudeLookup` | private | — |
| `d_sample_element_seq` | field | `sample_element_seq_type` | private | — |
| `d_element_list` | field | `GPlatesUtils::IntrusiveSinglyLinkedList<ElementEntry>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_LATLONAREASAMPLING_H` | macro | `None` | — |

## Notes

`reset_sample_spacing` rebuilds the entire lat/lon grid and re-adds every
previously added element (via the intrusive `d_element_list`), so it is an
O(N) operation over all elements added so far, not a cheap parameter tweak.
`get_sampled_element` does no bounds checking in release builds — the
assertion on `sample_element_index` is compiled out behind `#if 0`, so an
out-of-range index is undefined behaviour. The order of sampled elements
returned by `get_sampled_element` is unspecified and can change across a
`reset_sample_spacing` call.

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/RenderedGeometryLayer](../view-operations/RenderedGeometryLayer.md) | view-operations | 7 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/LatLonAreaSampling.h
python scripts/gpq.py def GPlatesUtils::LatLonAreaSampling --body
python scripts/gpq.py uses LatLonAreaSampling --kind class
python scripts/gpq.py hier LatLonAreaSampling
```
