# IllegalParametersException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/IllegalParametersException.h` | C++ | 75 |

## Overview

`IllegalParametersException` is thrown when a function or method is called with parameters that are illegal or semantically invalid. It wraps a message describing what made the parameters unacceptable and inherits from `Exception` to capture the call stack for debugging.

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

*None.*

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
