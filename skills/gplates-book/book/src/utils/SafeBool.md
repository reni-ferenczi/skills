# SafeBool

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 572 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/SafeBool.h` | C++ | 125 |

## Overview

[[[PROSE overview unit=utils/SafeBool tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::SafeBool`](#gplatesutilssafebool) | class | — | `<class T>` | 7 | SafeBool is a reuseable solution to the safe bool idiom. |

## Members

### `GPlatesUtils::SafeBool`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `this_type_does_not_support_comparisons()` | method | `void` | protected | — |
| `SafeBool()` | constructor | `None` | protected | — |
| `SafeBool( const SafeBool<U> &)` | constructor | `None` | protected | — |
| `~SafeBool()` | destructor | `None` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_SAFEBOOL_H` | macro | `None` | — |
| `operator==( const SafeBool<T> &lhs, const SafeBool<U> &rhs)` | operator | `bool` | Disallow operator== on SafeBools. |
| `operator!=( const SafeBool<T> &lhs, const SafeBool<U> &rhs)` | operator | `bool` | Disallow operator!= on SafeBools. |

## Notes

[[[PROSE notes unit=utils/SafeBool tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/LineReader](../file-io/LineReader.md) | file-io | 3 |
| [maths/CubeQuadTreePartition](../maths/CubeQuadTreePartition.md) | maths | 3 |
| [model/TopLevelPropertyRef](../model/TopLevelPropertyRef.md) | model | 3 |
| [app-logic/LayerProxyUtils](../app-logic/LayerProxyUtils.md) | app-logic | 2 |
| [model/WeakReference](../model/WeakReference.md) | model | 2 |
| [scribe/Scribe](../scribe/Scribe.md) | scribe | 2 |
| [utils/ObjectPool](ObjectPool.md) | utils | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/SafeBool.h
python scripts/gpq.py def GPlatesUtils::SafeBool --body
python scripts/gpq.py uses SafeBool --kind class
python scripts/gpq.py hier SafeBool
```
