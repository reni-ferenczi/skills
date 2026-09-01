# ViolatedClassInvariantException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/ViolatedClassInvariantException.h` | C++ | 76 |

## Overview

An exception thrown by mathematical classes when their invariants are violated. Mathematical types in GPlatesMaths (such as `PointOnSphere` or `FiniteRotation`) enforce preconditions on construction and operations; when those preconditions fail, they throw this exception with a message describing which invariant was violated. It is a simple wrapper around a string message, carrying stack trace information inherited from its `MathematicalException` parent.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::ViolatedClassInvariantException`](#gplatesmathsviolatedclassinvariantexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when class invariants are violated. |

## Members

### `GPlatesMaths::ViolatedClassInvariantException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViolatedClassInvariantException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which cause the invariant to be violated. |
| `~ViolatedClassInvariantException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_VIOLATEDCLASSINVARIANTEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/GridOnSphere](deprecated/GridOnSphere.md) | maths | 4 |
| [maths/UnitQuaternion3D](UnitQuaternion3D.md) | maths | 3 |
| [maths/SmallCircle](SmallCircle.md) | maths | 2 |
| [maths/SmallCircleArc](SmallCircleArc.md) | maths | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/ViolatedClassInvariantException.h
python scripts/gpq.py def GPlatesMaths::ViolatedClassInvariantException --body
python scripts/gpq.py uses ViolatedClassInvariantException --kind class
python scripts/gpq.py hier ViolatedClassInvariantException
```
