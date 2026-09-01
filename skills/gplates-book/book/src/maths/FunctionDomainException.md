# FunctionDomainException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/FunctionDomainException.h` | C++ | 76 |

## Overview

[[[PROSE overview unit=maths/FunctionDomainException tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesMaths::FunctionDomainException`](#gplatesmathsfunctiondomainexception) | class | [`MathematicalException`](MathematicalException.md) | — | 0 | The Exception thrown when the argument to a mathematical function lies outside the valid domain of the function. |

## Members

### `GPlatesMaths::FunctionDomainException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FunctionDomainException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | which cause the invariant to be violated. |
| `~FunctionDomainException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_MATHS_FUNCTIONDOMAINEXCEPTION_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=maths/FunctionDomainException tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/Real](Real.md) | maths | 39 |
| [maths/deprecated/GridOnSphere](deprecated/GridOnSphere.md) | maths | 19 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/FunctionDomainException.h
python scripts/gpq.py def GPlatesMaths::FunctionDomainException --body
python scripts/gpq.py uses FunctionDomainException --kind class
python scripts/gpq.py hier FunctionDomainException
```
