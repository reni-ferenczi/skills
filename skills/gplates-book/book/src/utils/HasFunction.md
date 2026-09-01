# HasFunction

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 46 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/HasFunction.h` | C++ | 114 |

## Overview

[[[PROSE overview unit=utils/HasFunction tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_HASFUNCTION_H` | macro | `None` | — |
| `HAS_FUNCTION` | macro_function | `template <typename FunctionSignatureType> \ struct MetaFunctionName \ { \ typedef char yes[1]; \ typedef char no[2]; \ \ template <typename U, U> \ struct TypeCheck; \ \ template < ...` | The following macros provide meta-functions that check if a function (HAS\_FUNCTION) or class method (HAD\_MEMBER\_FUNCTION) exists with a particular signature. |
| `HAS_MEMBER_FUNCTION` | macro_function | `template <class ClassType, typename MethodSignatureType> \ struct MetaFunctionName \ { \ typedef char yes[1]; \ typedef char no[2]; \ \ template <typename U, U> \ struct TypeCheck; ...` | — |

## Notes

[[[PROSE notes unit=utils/HasFunction tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/OverloadResolution](OverloadResolution.md) | utils | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/HasFunction.h
```
