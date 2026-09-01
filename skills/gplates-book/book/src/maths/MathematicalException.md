# MathematicalException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/MathematicalException.h` | C++ | 50 |

## Overview

[[[PROSE overview unit=maths/MathematicalException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::MathematicalException`](#gplatesmathsmathematicalexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 10 | The (pure virtual) base class of all mathematical exceptions. |

## Members

### `GPlatesMaths::MathematicalException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MathematicalException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~MathematicalException()` | destructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_MATHEMATICALEXCEPTION_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/MathematicalException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/FunctionDomainException](FunctionDomainException.md) | maths | 3 |
| [maths/IndeterminateResultException](IndeterminateResultException.md) | maths | 3 |
| [maths/InvalidGreatCircleArcException](InvalidGreatCircleArcException.md) | maths | 3 |
| [maths/InvalidGridException](InvalidGridException.md) | maths | 3 |
| [maths/InvalidOperationException](InvalidOperationException.md) | maths | 3 |
| [maths/UnableToNormaliseZeroVectorException](UnableToNormaliseZeroVectorException.md) | maths | 3 |
| [maths/ViolatedClassInvariantException](ViolatedClassInvariantException.md) | maths | 3 |
| [maths/ViolatedDirVectorInvariantException](ViolatedDirVectorInvariantException.md) | maths | 3 |
| [maths/ViolatedSmallCircleInvariantException](ViolatedSmallCircleInvariantException.md) | maths | 3 |
| [maths/ViolatedUnitVectorInvariantException](ViolatedUnitVectorInvariantException.md) | maths | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/MathematicalException.h
python scripts/gpq.py def GPlatesMaths::MathematicalException --body
python scripts/gpq.py uses MathematicalException --kind class
python scripts/gpq.py hier MathematicalException
```
