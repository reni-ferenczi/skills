# UnableToNormaliseZeroVectorException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/UnableToNormaliseZeroVectorException.h` | C++ | 65 |

## Overview

[[[PROSE overview unit=maths/UnableToNormaliseZeroVectorException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=maths/UnableToNormaliseZeroVectorException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
