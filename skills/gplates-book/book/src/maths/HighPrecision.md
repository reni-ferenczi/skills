# HighPrecision

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 5 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/HighPrecision.h` | C++ | 140 |

## Overview

[[[PROSE overview unit=maths/HighPrecision tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::HighPrecision`](#gplatesmathshighprecision) | class | — | `< typename T >` | 0 | This class is used to enable high-precision output of scalar values. |

## Members

### `GPlatesMaths::HighPrecision`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `output_type` | typedef | `T` | public | — |
| `HighPrecision( const T &val)` | constructor | `None` | public | — |
| `write_to( std::ostream &os)` | method | `void` | public | — |
| `HIGH_PRECISION` | field | `unsigned int` | private | — |
| `d_val` | field | `output_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_HIGHPRECISION_H_` | macro | `None` | — |
| `operator <<( QDebug dbg, const HighPrecision< T > &hp)` | operator | `QDebug` | Write using qDebug(), qWarning(), qCritical() or qFatal(). |

## Notes

[[[PROSE notes unit=maths/HighPrecision tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/UnitQuaternion3D](UnitQuaternion3D.md) | maths | 18 |
| [maths/Real](Real.md) | maths | 5 |
| [maths/UnitVector3D](UnitVector3D.md) | maths | 4 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 3 |
| [maths/deprecated/PolylineIntersections_test](deprecated/PolylineIntersections_test.md) | maths | 2 |
| [maths/PolygonOnSphere](PolygonOnSphere.md) | maths | 1 |
| [maths/PolylineOnSphere](PolylineOnSphere.md) | maths | 1 |
| [maths/Vector3D](Vector3D.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/HighPrecision.h
python scripts/gpq.py def GPlatesMaths::HighPrecision --body
python scripts/gpq.py uses HighPrecision --kind class
python scripts/gpq.py hier HighPrecision
```
