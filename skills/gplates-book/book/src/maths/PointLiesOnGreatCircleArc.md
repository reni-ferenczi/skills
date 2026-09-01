# PointLiesOnGreatCircleArc

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 1490 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/PointLiesOnGreatCircleArc.h` | C++ | 104 |
| `src/maths/PointLiesOnGreatCircleArc.cc` | C++ | 72 |

## Overview

[[[PROSE overview unit=maths/PointLiesOnGreatCircleArc tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/PointLiesOnGreatCircleArc tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
