# UnableToNormaliseZeroVectorException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnableToNormaliseZeroVectorException.h` | C++ | 65 |

## Overview

An exception thrown when code attempts to normalize a zero vector, which is mathematically undefined since it would require division by zero. Normalization produces a unit vector pointing in the same direction; the zero vector has no direction. The exception inherits from `MathematicalException`, categorizing it as a mathematical constraint violation rather than a resource or precondition error.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::UnableToNormaliseZeroVectorException`](#gplatesmathsunabletonormalisezerovectorexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | This is the exception thrown when an attempt is made to normalise a zero vector. |

## Members

### `GPlatesMaths::UnableToNormaliseZeroVectorException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnableToNormaliseZeroVectorException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~UnableToNormaliseZeroVectorException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MATHS_UNABLETONORMALILEZEROVECTOREXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/Vector3D](Vector3D.md) | maths | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/UnableToNormaliseZeroVectorException.h
python scripts/gpq.py def GPlatesMaths::UnableToNormaliseZeroVectorException --body
python scripts/gpq.py uses UnableToNormaliseZeroVectorException --kind class
python scripts/gpq.py hier UnableToNormaliseZeroVectorException
```
