# PointLiesOnGreatCircleArc

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1490 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PointLiesOnGreatCircleArc.h` | C++ | 104 |
| `src/maths/PointLiesOnGreatCircleArc.cc` | C++ | 72 |

## Overview

A function object that tests whether a point lies on a given `GreatCircleArc`. It extracts and caches the arc's start point, end point, and rotation axis (the normal to the plane containing the arc) during construction, then uses these to efficiently test points at call time. Designed for use with STL algorithms like `std::remove_if()` where the same arc is tested against many points.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::PointLiesOnGreatCircleArc`](#gplatesmathspointliesongreatcirclearc) | class | — | — | 0 | This class instantiates to a function object which determines whether a point lies on a given GreatCircleArc. |

## Members

### `GPlatesMaths::PointLiesOnGreatCircleArc`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PointLiesOnGreatCircleArc( const GreatCircleArc &arc)` | constructor | `None` | public | Instantiate a function object which determines whether a given point lies on arc. |
| `operator()( const PointOnSphere &test_point)` | operator | `bool` | public | Test whether test\_point lies on the arc supplied to the constructor. |
| `d_arc_start` | field | `PointOnSphere` | private | The start-point of the arc. |
| `d_arc_end` | field | `PointOnSphere` | private | The end-point of the arc. |
| `d_arc_normal` | field | `boost::optional<UnitVector3D>` | private | The normal to the plane which contains the arc. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator()( const PointOnSphere &test_point)` | operator | `bool` | — |
| `GPLATES_MATHS_POINTLIESONGREATCIRCLEARC_H` | macro | `None` | — |

## Notes

The `d_arc_normal` field is optional because zero-length arcs have no well-defined plane; in that case, the test function treats the arc as a point and only tests for coincidence with the start point.

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/PointOnSphere](PointOnSphere.md) | maths | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/PointLiesOnGreatCircleArc.h
python scripts/gpq.py def GPlatesMaths::PointLiesOnGreatCircleArc --body
python scripts/gpq.py uses PointLiesOnGreatCircleArc --kind class
python scripts/gpq.py hier PointLiesOnGreatCircleArc
```
