# RefToValue

[Book TOC](../../../TOC.md) · [system-fixes](../../../components/system-fixes.md) · cluster Community 1808 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/system-fixes/loki/RefToValue.h` | C++ | 68 |

## Overview

[[[PROSE overview unit=system-fixes/loki/RefToValue tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=system-fixes/loki/RefToValue tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
