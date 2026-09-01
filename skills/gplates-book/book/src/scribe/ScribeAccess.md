# ScribeAccess

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 429 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeAccess.h` | C++ | 421 |
| `src/scribe/ScribeAccess.cc` | C++ | 39 |

## Overview

[[[PROSE overview unit=scribe/ScribeAccess tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::Access`](#gplatesscribeaccess) | class | — | — | 0 | A central place for client classes to befriend in order for the scribe system to privately access client classes. |

## Members

### `GPlatesScribe::Access`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `transcribe( Scribe &scribe, ObjectType &object, bool transcribed_construct_data)` | method | `TranscribeResult` | private | — |
| `transcribe_construct_data( Scribe &scribe, ConstructObject<ObjectType> &object)` | method | `TranscribeResult` | private | — |
| `relocated( Scribe &scribe, const ObjectType &relocated_object, const ObjectType &transcribed_object)` | method | `void` | private | — |
| `DISABLE_MSVC_WARNING(4345)` | method | `PUSH_MSVC_WARNINGS` | private | Disable MSVC warning C4345: "behavior change: an object of POD type constructed with an initializer of the form () will be default-initialized" ...that happens when 'new (object) ObjectType()' is called on a POD type. |
| `construct_object( ObjectType *object)` | method | `void` | private | — |
| `GPLATES_SCRIBE_ACCESS_CONSTRUCT_OBJECT` | field | `BOOST_PP_REPEAT_FROM_TO` | private | Create 'construct\_object()' overloads. |
| `yes` | typedef | `char` | private | The following are implementation details that enable us to provide meta-functions that check if class 'ObjectType' has particular members. |
| `no` | typedef | `char` | private | — |
| `TypeCheck` | struct | `None` | private | — |
| `check_transcribe_construct_data` | variable | `yes` | private | — |
| `check_relocated` | variable | `yes` | private | — |
| `HasStaticMemberTranscribeConstructData` | struct | `None` | private | A meta-function that checks if class 'ObjectType' has the following static method: static TranscribeResult ObjectType::transcribe\_construct\_data( Scribe &, ConstructObject\<ObjectType\> &); Note: Only class Access can form the expression ... |
| `HasStaticMemberRelocated` | struct | `None` | private | A meta-function that checks if class 'ObjectType' has the following static method: static void ObjectType::relocated( Scribe &, const ObjectType &, const ObjectType &); Note: Only class Access can form the expression ... |
| `export_registered_classes_type` | typedef | `std::vector< boost::reference_wrapper<const ExportClassType> >` | private | Typedef for a sequence of export registered classes. |
| `EXPORT_REGISTERED_CLASSES` | field | `export_registered_classes_type` | private | Static variable to force classes to be exported registered at program startup. |
| `export_register_classes()` | method | `export_registered_classes_type` | private | Static method used to initialise EXPORT\_REGISTERED\_CLASSES. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `EXPORT_REGISTERED_CLASSES` | variable | `GPlatesScribe::Access::export_registered_classes_type` | — |
| `GPLATES_SCRIBE_SCRIBEACCESS_H` | macro | `None` | — |
| `GPLATES_SCRIBE_ACCESS_CONSTRUCT_MAX_CONSTRUCTOR_ARGS` | macro | `10` | The maximum number of object constructor arguments supported in Access::construct\_object(). |
| `GPLATES_SCRIBE_ACCESS_CONSTRUCT_OBJECT_PARAM` | macro_function | `BOOST_PP_CAT(const A, i) &BOOST_PP_CAT(a, i)` | The following preprocessor macros generate the following code: template \<typename ObjectType, typename A1\> static void construct\_object( ObjectType \*object, const A1 &a1); template \<typename ObjectType, typename A1, typename A2\> static ... |
| `GPLATES_SCRIBE_ACCESS_CONSTRUCT_OBJECT` | macro_function | `template < \ typename ObjectType, \ BOOST_PP_ENUM_SHIFTED_PARAMS(BOOST_PP_INC(n), typename A)> \ static \ void \ construct_object( \ ObjectType *object, \ BOOST_PP_ENUM_SHIFTED(BOO ...` | — |

## Notes

[[[PROSE notes unit=scribe/ScribeAccess tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 72 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 21 |
| [scribe/TranscribeImpl](TranscribeImpl.md) | scribe | 16 |
| [scribe/TranscribeBoost](TranscribeBoost.md) | scribe | 12 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 9 |
| [scribe/ScribeSaveLoadConstructObject](ScribeSaveLoadConstructObject.md) | scribe | 8 |
| [property-values/GeoTimeInstant](../property-values/GeoTimeInstant.md) | property-values | 7 |
| [scribe/TranscribeUtils](TranscribeUtils.md) | scribe | 6 |
| [scribe/ScribeXmlArchiveReader](ScribeXmlArchiveReader.md) | scribe | 4 |
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 4 |
| [scribe/TranscribeArray](TranscribeArray.md) | scribe | 3 |
| [scribe/TranscribeNonNullIntrusivePtr](TranscribeNonNullIntrusivePtr.md) | scribe | 3 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 2 |
| [gui/BuiltinColourPalettes](../gui/BuiltinColourPalettes.md) | gui | 2 |
| [model/TranscribeQualifiedXmlName](../model/TranscribeQualifiedXmlName.md) | model | 2 |
| [model/TranscribeStringContentTypeGenerator](../model/TranscribeStringContentTypeGenerator.md) | model | 2 |
| [scribe/ScribeConstructObject](ScribeConstructObject.md) | scribe | 2 |
| [scribe/TranscribeQt](TranscribeQt.md) | scribe | 2 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeAccess.h
python scripts/gpq.py def GPlatesScribe::Access --body
python scripts/gpq.py uses Access --kind class
python scripts/gpq.py hier Access
```
