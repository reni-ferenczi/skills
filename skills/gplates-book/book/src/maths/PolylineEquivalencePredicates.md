# PolylineEquivalencePredicates

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1442 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PolylineEquivalencePredicates.h` | C++ | 110 |

## Overview

[[[PROSE overview unit=maths/PolylineEquivalencePredicates tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PolylineIsDirectedEquivalentRef`](#gplatesmathspolylineisdirectedequivalentref) | class | `std::unary_function< PolylineOnSphere, bool >` | — | 0 | This class instantiates to a function object which determines whether a polyline is equivalent to another polyline when the directedness of the polyline segments is taken into account. |
| [`GPlatesMaths::PolylineIsUndirectedEquivalentRef`](#gplatesmathspolylineisundirectedequivalentref) | class | `std::unary_function< PolylineOnSphere, bool >` | — | 0 | This class instantiates to a function object which determines whether a polyline is equivalent to another polyline when the directedness of the polyline segments is ignored. |

## Members

### `GPlatesMaths::PolylineIsDirectedEquivalentRef`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PolylineIsDirectedEquivalentRef( const PolylineOnSphere &poly)` | constructor | `None` | public | — |
| `operator()( const PolylineOnSphere &other_poly)` | operator | `bool` | public | — |
| `d_poly_ptr` | field | `PolylineOnSphere` | private | — |

### `GPlatesMaths::PolylineIsUndirectedEquivalentRef`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PolylineIsUndirectedEquivalentRef( const PolylineOnSphere &poly)` | constructor | `None` | public | — |
| `operator()( const PolylineOnSphere &other_poly)` | operator | `bool` | public | — |
| `d_poly_ptr` | field | `PolylineOnSphere` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_POLYLINEEQUIVALENCEPREDICATES_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/PolylineEquivalencePredicates tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/PolylineIntersections_test](deprecated/PolylineIntersections_test.md) | maths | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PolylineEquivalencePredicates.h
python scripts/gpq.py def GPlatesMaths::PolylineIsDirectedEquivalentRef --body
python scripts/gpq.py uses PolylineIsDirectedEquivalentRef --kind class
python scripts/gpq.py hier PolylineIsDirectedEquivalentRef
```
