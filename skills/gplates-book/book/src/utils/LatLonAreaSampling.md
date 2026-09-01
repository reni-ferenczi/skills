# LatLonAreaSampling

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 698 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/LatLonAreaSampling.h` | C++ | 839 |

## Overview

[[[PROSE overview unit=utils/LatLonAreaSampling tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/LatLonAreaSampling tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
