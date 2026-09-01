# RefToValue

[Book TOC](../../../TOC.md) · [system-fixes](../../../components/system-fixes.md) · cluster Community 1808 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/system-fixes/loki/RefToValue.h` | C++ | 68 |

## Overview

A template class from the Loki library that transports a reference as a value, enabling the Colvin/Gibbons trick used by SmartPtr and ScopeGuard to maintain reference semantics across object copies and template instantiations. `RefToValue<T>` wraps a reference to type T and provides a conversion operator to recover the original reference, allowing references to be passed through containers and template parameters that normally require value types.

The `ByRef` helper function creates instances with type deduction, commonly used when passing references through APIs that expect value types.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`Loki::RefToValue`](#lokireftovalue) | class | — | `<class T>` | 0 | RefToValue SmartPointerGroup Transports a reference as a value Serves to implement the Colvin/Gibbons trick for SmartPtr/ScopeGuard |

## Members

### `Loki::RefToValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RefToValue(T& ref)` | constructor | `None` | public | — |
| `RefToValue(const RefToValue& rhs)` | constructor | `None` | public | — |
| `RefToValue()` | constructor | `None` | private | Disable - not implemented |
| `operator=` | field | `RefToValue` | private | — |
| `ref_` | field | `T` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LOKI_REFTOVALUE_H` | macro | `None` | — |
| `ByRef(T& t)` | function | `RefToValue<T>` | ExceptionGroup RefToValue creator. |

## Notes

Copy construction is allowed and preserves reference identity—the copy refers to the same object as the original. Default construction and assignment are disabled to prevent dangling references.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/KeyValueCache](../../utils/KeyValueCache.md) | utils | 6 |
| [utils/ObjectPool](../../utils/ObjectPool.md) | utils | 2 |
| [system-fixes/loki/ScopeGuard](ScopeGuard.md) | system-fixes | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/system-fixes/loki/RefToValue.h
python scripts/gpq.py def Loki::RefToValue --body
python scripts/gpq.py uses RefToValue --kind class
python scripts/gpq.py hier RefToValue
```
