# InvalidOperationException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidOperationException.h` | C++ | 75 |

## Overview

An exception thrown when an invalid mathematical operation is attempted. Code in the maths module raises this to signal that an operation cannot be completed because the input data or state violates a mathematical constraint—for instance, attempting to construct a geometric primitive with degenerate parameters.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::InvalidOperationException`](#gplatesmathsinvalidoperationexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when an invalid mathematical operation is attempted. |

## Members

### `GPlatesMaths::InvalidOperationException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidOperationException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which cause the operation to be invalid. |
| `~InvalidOperationException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_INVALIDOPERATIONEXCEPTION_H_` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/RotationHistory](deprecated/RotationHistory.md) | maths | 4 |
| [maths/deprecated/RotationSequence](deprecated/RotationSequence.md) | maths | 4 |
| [maths/FiniteRotation](FiniteRotation.md) | maths | 1 |
| [maths/Rotation](Rotation.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/InvalidOperationException.h
python scripts/gpq.py def GPlatesMaths::InvalidOperationException --body
python scripts/gpq.py uses InvalidOperationException --kind class
python scripts/gpq.py hier InvalidOperationException
```
