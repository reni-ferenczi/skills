# IndeterminateResultException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/IndeterminateResultException.h` | C++ | 75 |

## Overview

Exception thrown when a mathematical calculation would produce an indeterminate result (such as 0/0 or undefined operations on degenerate geometries). The exception carries a message describing the conditions that led to the indeterminate result and inherits from `MathematicalException`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::IndeterminateResultException`](#gplatesmathsindeterminateresultexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when a mathematical calculation is attempted which would return an indeterminate result. |

## Members

### `GPlatesMaths::IndeterminateResultException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IndeterminateResultException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which would result in an indeterminate result. |
| `~IndeterminateResultException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_INDETERMINATERESULTEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/GreatCircle](GreatCircle.md) | maths | 3 |
| [maths/deprecated/StageRotation](deprecated/StageRotation.md) | maths | 3 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 2 |
| [maths/GreatCircleArc](GreatCircleArc.md) | maths | 2 |
| [maths/UnitQuaternion3D](UnitQuaternion3D.md) | maths | 2 |
| [maths/LatLonPoint](LatLonPoint.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/IndeterminateResultException.h
python scripts/gpq.py def GPlatesMaths::IndeterminateResultException --body
python scripts/gpq.py uses IndeterminateResultException --kind class
python scripts/gpq.py hier IndeterminateResultException
```
