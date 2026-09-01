# OverloadResolution

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 629 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/OverloadResolution.h` | C++ | 382 |

## Overview

[[[PROSE overview unit=utils/OverloadResolution tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertype) | struct | — | `< class Class, typename Ret, typename Arg1, typename Arg2, typename Arg3, typename Arg4, typename Arg5 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, Arg2, Arg3, Arg4, Arg5>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypenonmemberfunction-ret-arg1-arg2-arg3-arg4-arg5) | struct | — | `< typename Ret, typename Arg1, typename Arg2, typename Arg3, typename Arg4, typename Arg5 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, Arg1, Arg2, Arg3, Arg4, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypeclass-ret-arg1-arg2-arg3-arg4-nulltype) | struct | — | `< class Class, typename Ret, typename Arg1, typename Arg2, typename Arg3, typename Arg4 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, Arg2, Arg3, Arg4, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypenonmemberfunction-ret-arg1-arg2-arg3-arg4-nulltype) | struct | — | `< typename Ret, typename Arg1, typename Arg2, typename Arg3, typename Arg4 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, Arg1, Arg2, Arg3, NullType, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypeclass-ret-arg1-arg2-arg3-nulltype-nulltype) | struct | — | `< class Class, typename Ret, typename Arg1, typename Arg2, typename Arg3 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, Arg2, Arg3, NullType, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypenonmemberfunction-ret-arg1-arg2-arg3-nulltype-nulltype) | struct | — | `< typename Ret, typename Arg1, typename Arg2, typename Arg3 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, Arg1, Arg2, NullType, NullType, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypeclass-ret-arg1-arg2-nulltype-nulltype-nulltype) | struct | — | `< class Class, typename Ret, typename Arg1, typename Arg2 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, Arg2, NullType, NullType, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypenonmemberfunction-ret-arg1-arg2-nulltype-nulltype-nulltype) | struct | — | `< typename Ret, typename Arg1, typename Arg2 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, Arg1, NullType, NullType, NullType, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypeclass-ret-arg1-nulltype-nulltype-nulltype-nulltype) | struct | — | `< class Class, typename Ret, typename Arg1 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, NullType, NullType, NullType, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypenonmemberfunction-ret-arg1-nulltype-nulltype-nulltype-nulltype) | struct | — | `< typename Ret, typename Arg1 >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, NullType, NullType, NullType, NullType, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypeclass-ret-nulltype-nulltype-nulltype-nulltype-nulltype) | struct | — | `< class Class, typename Ret >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, NullType, NullType, NullType, NullType, NullType>`](#gplatesutilsoverloadresolutionoverloadresolutioninternalsdeducememberfunctionpointertypenonmemberfunction-ret-nulltype-nulltype-nulltype-nulltype-nulltype) | struct | — | `< typename Ret >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::Params`](#gplatesutilsoverloadresolutionparams) | struct | — | `< typename _Arg1 = OverloadResolutionInternals::NullType, typename _Arg2 = OverloadResolutionInternals::NullType, typename _Arg3 = OverloadResolutionInternals::NullType, typename _Arg4 = OverloadResolutionInternals::NullType, typename _Arg5 = OverloadResolutionInternals::NullType >` | 0 | — |
| [`GPlatesUtils::OverloadResolution::mem_fn_types`](#gplatesutilsoverloadresolutionmem_fn_types) | struct | — | `<class Class>` | 0 | For commonly used overloaded functions in the STL/Qt, we provide a more convenient form of resolve that takes the type of the function pointer as template parameter. |
| [`GPlatesUtils::OverloadResolution::mem_fn_types_for_maps`](#gplatesutilsoverloadresolutionmem_fn_types_for_maps) | struct | — | `<class MapType>` | 2 | — |
| [`GPlatesUtils::OverloadResolution::mem_fn_types<std::map<T, U> >`](#gplatesutilsoverloadresolutionmem_fn_typesstdmapt-u-) | struct | [`mem_fn_types_for_maps<std::map<T, U> >`](OverloadResolution.md) | `<typename T, typename U>` | 0 | — |
| [`GPlatesUtils::OverloadResolution::mem_fn_types<std::multimap<T, U> >`](#gplatesutilsoverloadresolutionmem_fn_typesstdmultimapt-u-) | struct | [`mem_fn_types_for_maps<std::multimap<T, U> >`](OverloadResolution.md) | `<typename T, typename U>` | 0 | — |
| [`GPlatesUtils::OverloadResolution::mem_fn_types<QString>`](#gplatesutilsoverloadresolutionmem_fn_typesqstring) | struct | — | `<>` | 0 | — |

## Members

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, Arg2, Arg3, Arg4, Arg5>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, Arg1, Arg2, Arg3, Arg4, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, Arg2, Arg3, Arg4, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, Arg1, Arg2, Arg3, NullType, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, Arg2, Arg3, NullType, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, Arg1, Arg2, NullType, NullType, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, Arg2, NullType, NullType, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, Arg1, NullType, NullType, NullType, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, Arg1, NullType, NullType, NullType, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<Class, Ret, NullType, NullType, NullType, NullType, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::OverloadResolutionInternals::DeduceMemberFunctionPointerType<NonMemberFunction, Ret, NullType, NullType, NullType, NullType, NullType>`

*None.*

### `GPlatesUtils::OverloadResolution::Params`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Arg1` | typedef | `_Arg1` | public | — |
| `Arg2` | typedef | `_Arg2` | public | — |
| `Arg3` | typedef | `_Arg3` | public | — |
| `Arg4` | typedef | `_Arg4` | public | — |
| `Arg5` | typedef | `_Arg5` | public | — |

### `GPlatesUtils::OverloadResolution::mem_fn_types`

*None.*

### `GPlatesUtils::OverloadResolution::mem_fn_types_for_maps`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `map_type` | typedef | `MapType` | public | — |
| `iterator_type` | typedef | `typename map_type::iterator` | public | — |
| `const_iterator_type` | typedef | `typename map_type::const_iterator` | public | — |
| `key_type` | typedef | `typename map_type::key_type` | public | — |
| `CheckMapEraseType` | struct | `None` | public | For MSVC we need to inherit 'map\_type' and bring its 'erase()' method into scope of derived class so that, when we check the method type, it doesn't find 'erase' in the base class of 'map\_type' and hence have a different method signature ... |
| `erase1` | typedef | `typename boost::mpl::if_< // See if erase method has signature 'iterator_type (map_type::*)(iterator_type)'... HasEraseMember<CheckMapEraseType, iterator_type (CheckMapEraseType::* ...` | public | — |

### `GPlatesUtils::OverloadResolution::mem_fn_types<std::map<T, U> >`

*None.*

### `GPlatesUtils::OverloadResolution::mem_fn_types<std::multimap<T, U> >`

*None.*

### `GPlatesUtils::OverloadResolution::mem_fn_types<QString>`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_OVERLOADRESOLUTION_H` | macro | `None` | — |
| `resolve( typename OverloadResolutionInternals::DeduceMemberFunctionPointerType< Class, Ret, typename Params::Arg1, typename Params::Arg2, typename Params::Arg3, typename Params::Arg4, typename Params::Arg5>::Type fp)` | function | `typename OverloadResolutionInternals::DeduceMemberFunctionPointerType< Class, Ret, typename Params::Arg1, typename Params::Arg2, typename Params::Arg3, typename Params::Arg4, typen ...` | — |
| `resolve( FunctionPointerType fp)` | function | `FunctionPointerType` | — |

## Notes

[[[PROSE notes unit=utils/OverloadResolution tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/RawRaster](../property-values/RawRaster.md) | property-values | 70 |
| [utils/KeyValueCache](KeyValueCache.md) | utils | 14 |
| [file-io/RasterReader](../file-io/RasterReader.md) | file-io | 5 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/OverloadResolution.h
python scripts/gpq.py def GPlatesUtils::OverloadResolution::mem_fn_types_for_maps --body
python scripts/gpq.py uses mem_fn_types_for_maps --kind struct
python scripts/gpq.py hier mem_fn_types_for_maps
```
