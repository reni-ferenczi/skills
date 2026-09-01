# IllegalParametersException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/IllegalParametersException.h` | C++ | 75 |

## Overview

[[[PROSE overview unit=global/IllegalParametersException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::IllegalParametersException`](#gplatesglobalillegalparametersexception) | class | [`Exception`](GPlatesException.md) | — | 1 | Should be thrown when a method is called with illegal or unreasonable parameters. |

## Members

### `GPlatesGlobal::IllegalParametersException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `IllegalParametersException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `~IllegalParametersException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_ILLEGALPARAMETERSEXCEPTION_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/IllegalParametersException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/PropertyValueNotSupportedException](../qt-widgets/PropertyValueNotSupportedException.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/IllegalParametersException.h
python scripts/gpq.py def GPlatesGlobal::IllegalParametersException --body
python scripts/gpq.py uses IllegalParametersException --kind class
python scripts/gpq.py hier IllegalParametersException
```
