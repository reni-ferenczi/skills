# InvalidGridException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/InvalidGridException.h` | C++ | 75 |

## Overview

[[[PROSE overview unit=maths/InvalidGridException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::InvalidGridException`](#gplatesmathsinvalidgridexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when an attempt is made to create an invalid grid. |

## Members

### `GPlatesMaths::InvalidGridException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidGridException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which cause the grid to be invalid. |
| `~InvalidGridException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_INVALIDGRIDEXCEPTION_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/InvalidGridException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/GridOnSphere](deprecated/GridOnSphere.md) | maths | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/InvalidGridException.h
python scripts/gpq.py def GPlatesMaths::InvalidGridException --body
python scripts/gpq.py uses InvalidGridException --kind class
python scripts/gpq.py hier InvalidGridException
```
