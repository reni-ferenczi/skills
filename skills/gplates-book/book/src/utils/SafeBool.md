# SafeBool

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 572 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/SafeBool.h` | C++ | 125 |

## Overview

`SafeBool<T>` is a reusable, pre-`explicit operator bool` implementation of the safe-bool idiom: a class wants to be usable in a boolean context (`if (obj)`) without also being implicitly convertible to `int` and silently participating in arithmetic, ordering or cross-type comparisons. A class opts in by publicly inheriting `SafeBool<Derived>` (CRTP) and providing a `bool boolean_test() const` member; the base then supplies `operator bool_type()`, which returns a pointer-to-member-function that is truthy or `NULL` but cannot be compared, added, or implicitly converted to another type. Seven classes across the model, maths and scribe modules use it where a predicate-like object needs to behave like a bool in conditionals only.

The free `operator==`/`operator!=` overloads on `SafeBool<T>` exist purely to fail template instantiation (via `BOOST_STATIC_ASSERT(sizeof(T) == 0)`) if someone tries to compare two `SafeBool`-derived objects directly, which is exactly the accidental usage the idiom is designed to prevent.

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

A derived class must supply a public, non-virtual `bool boolean_test() const` — `operator bool_type()` calls it via `static_cast<const T*>(this)`, so its absence is a compile error at the point of instantiation, not at the `SafeBool` declaration itself.

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
