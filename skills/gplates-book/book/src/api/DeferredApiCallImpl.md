# DeferredApiCallImpl

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 739 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/DeferredApiCallImpl.h` | C++ | 799 |

## Overview

[[[PROSE overview unit=api/DeferredApiCallImpl tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::DeferredApiCallImpl::no_wrap`](#gplatesapideferredapicallimplno_wrap) | typedef | — | — | 0 | — |
| [`GPlatesApi::DeferredApiCallImpl::ref`](#gplatesapideferredapicallimplref) | typedef | — | — | 0 | — |
| [`GPlatesApi::DeferredApiCallImpl::cref`](#gplatesapideferredapicallimplcref) | typedef | — | — | 0 | — |
| [`GPlatesApi::DeferredApiCallImpl::get_wrapping_helper`](#gplatesapideferredapicallimplget_wrapping_helper) | struct | — | `<int I, class ArgReferenceWrappingsType>` | 0 | — |
| [`GPlatesApi::DeferredApiCallImpl::get_wrapping_helper<0, ArgReferenceWrappingsType>`](#gplatesapideferredapicallimplget_wrapping_helper0-argreferencewrappingstype) | struct | — | `<class ArgReferenceWrappingsType>` | 0 | — |
| [`GPlatesApi::DeferredApiCallImpl::Impl`](#gplatesapideferredapicallimplimpl) | struct | — | `<class ComponentTypes, class ArgReferenceWrappingsType>` | 0 | — |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 0>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-0) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 0. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 1>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-1) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 1. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 2>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-2) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 2. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 3>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-3) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 3. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 4>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-4) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 4. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 5>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-5) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 5. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 6>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-6) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 6. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 7>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-7) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 7. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 8>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-8) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 8. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 9>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-9) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 9. |
| [`GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 10>`](#gplatesapideferredapicallimpldeferredapicallfunctionptrtype-functionptr-argreferencewrappingstype-10) | struct | — | `<typename FunctionPtrType, FunctionPtrType FunctionPtr, class ArgReferenceWrappingsType>` | 0 | Arity = 10. |
| [`GPlatesApi::DeferredApiCallImpl::Wrapper`](#gplatesapideferredapicallimplwrapper) | struct | — | `<typename FunctionPtrType>` | 0 | The template parameter FunctionPtrType is deduced using make\_wrapper below, and once we have a Wrapper object instantiated with the correct FunctionPtrType, we can then call wrap, which takes the FunctionPtr itself as a template parameter. |
| [`GPlatesApi::DeferredApiCallImpl::MemberFunctionWrapper`](#gplatesapideferredapicallimplmemberfunctionwrapper) | struct | — | `<typename FunctionPtrType>` | 0 | The same as Wrapper but for member function pointers. |

## Members

### `GPlatesApi::DeferredApiCallImpl::no_wrap`

*None.*

### `GPlatesApi::DeferredApiCallImpl::ref`

*None.*

### `GPlatesApi::DeferredApiCallImpl::cref`

*None.*

### `GPlatesApi::DeferredApiCallImpl::get_wrapping_helper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `typename ArgReferenceWrappingsType::template get<I - 1>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::get_wrapping_helper<0, ArgReferenceWrappingsType>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `no_wrap` | public | — |

### `GPlatesApi::DeferredApiCallImpl::Impl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_wrapping` | struct | `None` | public | Extracts the wrapping appropriate for the I-th component (i.e. the {@code (I - 1)}-th parameter. |
| `wrap_arg_type_helper` | struct | `None` | public | — |
| `wrap_arg_type_helper<T, no_wrap>` | struct | `None` | public | — |
| `wrap_arg_type_helper<T, ref>` | struct | `None` | public | — |
| `wrap_arg_type_helper<T, cref>` | struct | `None` | public | — |
| `wrap_arg_type` | struct | `None` | public | Ensures that the parameter types of the synthesised function have the correct const-ness and reference-ness depending on what reference wrapping has been selected for the corresponding parameter. |
| `at` | struct | `None` | public | Extracts the I-th component and passes it through wrap\_arg\_type. |
| `wrapped_value_type_helper` | struct | `None` | public | — |
| `wrapped_value_type_helper<T, no_wrap>` | struct | `None` | public | — |
| `wrapped_value_type_helper<T, ref>` | struct | `None` | public | — |
| `wrapped_value_type_helper<T, cref>` | struct | `None` | public | — |
| `wrapped_value_type` | struct | `None` | public | — |
| `wrap_value( T &value, no_wrap)` | method | `T` | public | — |
| `wrap_value( T &value, ref)` | method | `boost::reference_wrapper<T>` | public | — |
| `wrap_value( T &value, cref)` | method | `boost::reference_wrapper<const T>` | public | — |
| `wrap_value( T &value)` | method | `typename wrapped_value_type<I, T>::type` | public | Applies the specified reference wrapping for the {@code (I - 1)}-th function parameter of value value. |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 0>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call()` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 1>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1)` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 2>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1, typename impl::template at<2>::type a2)` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 3>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1, typename impl::template at<2>::type a2, typename impl::template at<3>::type a3)` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 4>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1, typename impl::template at<2>::type a2, typename impl::template at<3>::type a3, typename impl::template at<4>::type a4)` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 5>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1, typename impl::template at<2>::type a2, typename impl::template at<3>::type a3, typename impl::template at<4>::type a4, typename impl::template at<5>::type a5)` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 6>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1, typename impl::template at<2>::type a2, typename impl::template at<3>::type a3, typename impl::template at<4>::type a4, typename impl::template at<5>::type a5, typename impl::template at<6>::type a6)` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 7>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1, typename impl::template at<2>::type a2, typename impl::template at<3>::type a3, typename impl::template at<4>::type a4, typename impl::template at<5>::type a5, typename impl::template at<6>::type a6, typename impl::template at<7>::type a7)` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 8>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1, typename impl::template at<2>::type a2, typename impl::template at<3>::type a3, typename impl::template at<4>::type a4, typename impl::template at<5>::type a5, typename impl::template at<6>::type a6, typename impl::template at<7>::type a7, typename impl::templa ...` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 9>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1, typename impl::template at<2>::type a2, typename impl::template at<3>::type a3, typename impl::template at<4>::type a4, typename impl::template at<5>::type a5, typename impl::template at<6>::type a6, typename impl::template at<7>::type a7, typename impl::templa ...` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::DeferredApiCall<FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, 10>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `types` | typedef | `typename GPlatesUtils::FunctionTypes::component_types<FunctionPtrType>::types` | public | — |
| `impl` | typedef | `Impl<types, ArgReferenceWrappingsType>` | public | — |
| `deferred_api_call( typename impl::template at<1>::type a1, typename impl::template at<2>::type a2, typename impl::template at<3>::type a3, typename impl::template at<4>::type a4, typename impl::template at<5>::type a5, typename impl::template at<6>::type a6, typename impl::template at<7>::type a7, typename impl::templa ...` | method | `typename impl::template at<0>::type` | public | — |

### `GPlatesApi::DeferredApiCallImpl::Wrapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `wrap( ArgReferenceWrappingsType)` | method | `typename DeferredApiCall< FunctionPtrType, static_cast<FunctionPtrType>(FunctionPtr), ArgReferenceWrappingsType, GPlatesUtils::FunctionTypes::function_arity<FunctionPtrType>::value ...` | public | Workaround for Visual Studio 2005. |

### `GPlatesApi::DeferredApiCallImpl::MemberFunctionWrapper`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `wrap( ArgReferenceWrappingsType)` | method | `typename DeferredApiCall< FunctionPtrType, FunctionPtr, ArgReferenceWrappingsType, GPlatesUtils::FunctionTypes::function_arity<FunctionPtrType>::value >::function_type` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_API_DEFERREDAPICALLIMPL_H` | macro | `None` | — |
| `make_wrapper( FunctionPtrType function_ptr, typename boost::disable_if< boost::is_member_function_pointer<FunctionPtrType> >::type *dummy = NULL)` | function | `Wrapper<FunctionPtrType>` | This function here is used to deduce the type of function\_ptr for pointers to non-member functions. |
| `make_wrapper( FunctionPtrType function_ptr, typename boost::enable_if< boost::is_member_function_pointer<FunctionPtrType> >::type *dummy = NULL)` | function | `MemberFunctionWrapper<FunctionPtrType>` | This function here is used to deduce the type of function\_ptr for pointers to member functions. |

## Notes

[[[PROSE notes unit=api/DeferredApiCallImpl tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [api/DeferredApiCall](DeferredApiCall.md) | api | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/DeferredApiCallImpl.h
python scripts/gpq.py def GPlatesApi::DeferredApiCallImpl::Impl --body
python scripts/gpq.py uses Impl --kind struct
python scripts/gpq.py hier Impl
```
