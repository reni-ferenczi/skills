# ScribeConstructObject

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1397 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeConstructObject.h` | C++ | 260 |

## Overview

`ConstructObject<ObjectType>` lets `transcribe_construct_data()` hand a client's `transcribe_construct_data` overload a slot for an object that does not yet exist, so types without a default constructor can still be transcribed from an archive. When loading, the `ConstructObject` initially wraps uninitialised memory; the client calls one of the `construct_object()` overloads (generated for 1 up to `GPLATES_SCRIBE_CONSTRUCT_MAX_CONSTRUCTOR_ARGS` arguments via the Boost.Preprocessor `GPLATES_SCRIBE_CONSTRUCT_OBJECT` macro) to placement-construct `ObjectType` in place with whatever arguments its constructor needs, after which `get_object()`/`operator*`/`operator->` become valid. When saving, the wrapped object is already constructed and `ConstructObject` is just a reference to it.

Because `Access::construct_object()` does the actual placement-new, a type with a private constructor only needs `friend class GPlatesScribe::Access;` to be constructible this way — the scribe framework never needs public access to the constructor itself.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::ConstructObject`](#gplatesscribeconstructobject) | class | `boost::noncopyable` | `<typename ObjectType>` | 3 | Wrapper around a (possibly) un-initialised, or un-constructed, object. |

## Members

### `GPlatesScribe::ConstructObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator->()` | operator | `ObjectType` | public | Returns a pointer to the internal object. |
| `construct_object()` | method | `void` | public | Constructs the internal object using the default constructor of 'ObjectType'. |
| `GPLATES_SCRIBE_CONSTRUCT_OBJECT` | field | `BOOST_PP_REPEAT_FROM_TO` | public | Create 'construct\_object()' overloads. |
| `get_object_address()` | method | `ObjectType` | public | Returns the address of the internal object. |
| `ConstructObject( ObjectType *object_, bool is_object_initialised_)` | constructor | `None` | protected | — |
| `is_object_initialised()` | method | `bool` | protected | — |
| `d_object` | field | `ObjectType` | private | — |
| `d_is_object_initialised` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBECONSTRUCTOBJECT_H` | macro | `None` | — |
| `GPLATES_SCRIBE_CONSTRUCT_MAX_CONSTRUCTOR_ARGS` | macro | `GPLATES_SCRIBE_ACCESS_CONSTRUCT_MAX_CONSTRUCTOR_ARGS` | The maximum number of object constructor arguments supported in ConstructOjbect\<\>::construct\_object(). |
| `GPLATES_SCRIBE_CONSTRUCT_OBJECT_PARAM` | macro_function | `BOOST_PP_CAT(const A, i) &BOOST_PP_CAT(a, i)` | The following preprocessor macros generate the following code: template \<typename A1\> void construct\_object( const A1 &a1); template \<typename A1, typename A2\> void construct\_object( const A1 &a1, const A2 &a2); template \<typename A1, ... |
| `GPLATES_SCRIBE_CONSTRUCT_OBJECT` | macro_function | `template <BOOST_PP_ENUM_SHIFTED_PARAMS(BOOST_PP_INC(n), typename A)> \ void \ construct_object( \ BOOST_PP_ENUM_SHIFTED(BOOST_PP_INC(n), GPLATES_SCRIBE_CONSTRUCT_OBJECT_PARAM, _) ) ...` | — |

## Notes

Calling `construct_object()` a second time, or accessing the object before construction, both throw `Exceptions::ScribeLibraryError` via the class's own assertions. Constructor arguments are taken as `const` references, so a constructor parameter that must bind to a non-const reference (or an in-place-constructed temporary) needs to be passed through `boost::ref()`, exactly as with `boost::in_place()`. `get_object_address()` returns the raw pointer regardless of construction state and must not be dereferenced directly — use `get_object()` or the dereference operators, which check initialisation first.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/ScribeSaveLoadConstructObject](ScribeSaveLoadConstructObject.md) | scribe | 7 |
| [scribe/ScribeLoadRefImpl](ScribeLoadRefImpl.md) | scribe | 6 |
| [scribe/Scribe](Scribe.md) | scribe | 1 |
| [scribe/TranscribeArray](TranscribeArray.md) | scribe | 1 |
| [scribe/TranscribeImpl](TranscribeImpl.md) | scribe | 1 |
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeConstructObject.h
python scripts/gpq.py def GPlatesScribe::ConstructObject --body
python scripts/gpq.py uses ConstructObject --kind class
python scripts/gpq.py hier ConstructObject
```
