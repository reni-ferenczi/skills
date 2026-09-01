# ScribeConstructObject

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1397 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeConstructObject.h` | C++ | 260 |

## Overview

[[[PROSE overview unit=scribe/ScribeConstructObject tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=scribe/ScribeConstructObject tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
