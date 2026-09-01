# HasFunction

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 46 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/HasFunction.h` | C++ | 114 |

## Overview

`HasFunction` provides two preprocessor macros that generate compile-time meta-functions to detect whether functions or methods with specific signatures exist. The `HAS_FUNCTION` macro creates a meta-function for global functions, and `HAS_MEMBER_FUNCTION` creates one for class member functions.

Each generated meta-function uses SFINAE (Substitution Failure Is Not An Error) to test whether a function pointer with the specified signature can be bound. The meta-function provides both a `value` boolean constant and a `type` typedef with a Boost.MPL boolean, enabling use in conditional compilation and overload resolution. For example, `enable_if` can branch between alternative function implementations based on whether a method signature matches.

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

The generated meta-function is a template that must be instantiated with the exact function or method signature, including const, volatile, and reference qualifiers. For instance, `HasGetMember<MyClass, int (MyClass::*)() const>` and `HasGetMember<MyClass, int (MyClass::*)()>` check different signatures (const vs. non-const). The check is purely compile-time with no runtime cost or side effects.

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
