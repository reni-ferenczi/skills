# FunctionTypes

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 512 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/FunctionTypes.h` | C++ | 511 |

## Overview

`GPlatesUtils::FunctionTypes` is a hand-written, pre-C++11 substitute for
`Boost.FunctionTypes`, kept because the codebase originally targeted a Boost
version older than 1.35. `component_types<FunctionType>` is specialised by
hand for every combination of arity (0 through 9 arguments) and calling
convention (free function pointer, non-const member function pointer, const
member function pointer) that the codebase actually needs; each
specialisation exposes a `types` typedef that is a `boost::mpl::vector` of
the result type followed by the parameter types, with a member-pointer's
implicit `Class` receiver type counted as the first parameter to match
Boost's own convention. `function_arity<FunctionType>` then derives the
parameter count from the size of that vector. Because only the exact
signatures used elsewhere in the tree are specialised, volatile functions,
variadic functions and arities beyond 9 are unsupported — anything else fails
to compile as an undefined-template error rather than falling back to a
generic implementation.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)() >`](#gplatesutilsfunctiontypescomponent_types-result--) | struct | — | `< typename Result >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-) | struct | — | `< typename Result, typename A0 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)() >`](#gplatesutilsfunctiontypescomponent_types-result-class-) | struct | — | `< typename Result, typename Class >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)() const >`](#gplatesutilsfunctiontypescomponent_types-result-class-const-) | struct | — | `< typename Result, typename Class >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-a1-) | struct | — | `< typename Result, typename A0, typename A1 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1) >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-) | struct | — | `< typename Result, typename Class, typename A1 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1) const >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-const-) | struct | — | `< typename Result, typename Class, typename A1 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-a1-a2-) | struct | — | `< typename Result, typename A0, typename A1, typename A2 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2) >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-) | struct | — | `< typename Result, typename Class, typename A1, typename A2 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2) const >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-const-) | struct | — | `< typename Result, typename Class, typename A1, typename A2 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-a1-a2-a3-) | struct | — | `< typename Result, typename A0, typename A1, typename A2, typename A3 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3) >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3) const >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-const-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-a1-a2-a3-a4-) | struct | — | `< typename Result, typename A0, typename A1, typename A2, typename A3, typename A4 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4) >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4) const >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-const-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-a1-a2-a3-a4-a5-) | struct | — | `< typename Result, typename A0, typename A1, typename A2, typename A3, typename A4, typename A5 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5) >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5) const >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-const-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5, A6) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-a1-a2-a3-a4-a5-a6-) | struct | — | `< typename Result, typename A0, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6) >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-a6-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6) const >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-a6-const-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5, A6, A7) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-a1-a2-a3-a4-a5-a6-a7-) | struct | — | `< typename Result, typename A0, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6, typename A7 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7) >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-a6-a7-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6, typename A7 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7) const >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-a6-a7-const-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6, typename A7 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5, A6, A7, A8) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-a1-a2-a3-a4-a5-a6-a7-a8-) | struct | — | `< typename Result, typename A0, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6, typename A7, typename A8 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7, A8) >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-a6-a7-a8-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6, typename A7, typename A8 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7, A8) const >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-a6-a7-a8-const-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6, typename A7, typename A8 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5, A6, A7, A8, A9) >`](#gplatesutilsfunctiontypescomponent_types-result-a0-a1-a2-a3-a4-a5-a6-a7-a8-a9-) | struct | — | `< typename Result, typename A0, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6, typename A7, typename A8, typename A9 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7, A8, A9) >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-a6-a7-a8-a9-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6, typename A7, typename A8, typename A9 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7, A8, A9) const >`](#gplatesutilsfunctiontypescomponent_types-result-classa1-a2-a3-a4-a5-a6-a7-a8-a9-const-) | struct | — | `< typename Result, typename Class, typename A1, typename A2, typename A3, typename A4, typename A5, typename A6, typename A7, typename A8, typename A9 >` | 0 | — |
| [`GPlatesUtils::FunctionTypes::function_arity`](#gplatesutilsfunctiontypesfunction_arity) | struct | — | `<typename FunctionType>` | 0 | This mimics the struct function\_arity in Boost.FunctionTypes. |

## Members

### `GPlatesUtils::FunctionTypes::component_types< Result (*)() >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)() >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)() const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0, A1>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1) const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0, A1, A2>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2) const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0, A1, A2, A3>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3) const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0, A1, A2, A3, A4>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4) const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0, A1, A2, A3, A4, A5>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5) const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5, A6) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0, A1, A2, A3, A4, A5, A6>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5, A6>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6) const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5, A6>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5, A6, A7) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0, A1, A2, A3, A4, A5, A6, A7>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5, A6, A7>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7) const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5, A6, A7>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5, A6, A7, A8) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0, A1, A2, A3, A4, A5, A6, A7, A8>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7, A8) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5, A6, A7, A8>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7, A8) const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5, A6, A7, A8>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (*)(A0, A1, A2, A3, A4, A5, A6, A7, A8, A9) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, A0, A1, A2, A3, A4, A5, A6, A7, A8, A9>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7, A8, A9) >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5, A6, A7, A8, A9>` | public | — |

### `GPlatesUtils::FunctionTypes::component_types< Result (Class::*)(A1, A2, A3, A4, A5, A6, A7, A8, A9) const >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `boost::mpl::vector<Result, Class, A1, A2, A3, A4, A5, A6, A7, A8, A9>` | public | — |

### `GPlatesUtils::FunctionTypes::function_arity`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `value` | field | `std::size_t` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_FUNCTIONTYPES_H` | macro | `None` | — |

## Notes

The header comment notes that once the project's minimum Boost version rose
to 1.35, `Boost.FunctionTypes` could replace this namespace outright, with
only a namespace change needed in client code — this file was never migrated.

## Used by

| Unit | Component | References |
|---|---|---|
| [api/DeferredApiCallImpl](../api/DeferredApiCallImpl.md) | api | 35 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/FunctionTypes.h
python scripts/gpq.py def GPlatesUtils::FunctionTypes::component_types< Result (*)() > --body
python scripts/gpq.py uses component_types< Result (*)() > --kind struct
python scripts/gpq.py hier component_types< Result (*)() >
```
