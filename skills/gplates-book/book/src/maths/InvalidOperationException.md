# InvalidOperationException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidOperationException.h` | C++ | 75 |

## Overview

[[[PROSE overview unit=maths/InvalidOperationException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/InvalidOperationException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
