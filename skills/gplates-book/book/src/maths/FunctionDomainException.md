# FunctionDomainException

[Book TOC](../../TOC.md) · [maths](../../components/maths.md) · cluster Community 83 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/FunctionDomainException.h` | C++ | 76 |

## Overview

`FunctionDomainException` is the maths module's counterpart to the C library's
`EDOM` error: it is thrown when an argument passed to a mathematical function
falls outside the domain that function is defined for. It derives from
`MathematicalException`, so it plugs into the same `GPlatesGlobal::Exception`
hierarchy and call-stack-trace reporting as the other maths exceptions rather
than defining its own error-reporting scheme.

The class carries nothing beyond a plain string message, supplied by the
caller at the point the invalid argument is detected; `exception_name()` and
`write_message()` are the two hooks `MathematicalException` requires an
implementation to fill in so the base class can format a uniform diagnostic.

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

*None.*

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
