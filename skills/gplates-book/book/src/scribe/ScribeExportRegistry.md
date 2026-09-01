# ScribeExportRegistry

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 28 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeExportRegistry.h` | C++ | 269 |
| `src/scribe/ScribeExportRegistry.cc` | C++ | 66 |

## Overview

[[[PROSE overview unit=scribe/ScribeExportRegistry tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::ExportClassType`](#gplatesscribeexportclasstype) | class | — | — | 0 | Export registered information for a class type. |
| [`GPlatesScribe::ExportRegistry`](#gplatesscribeexportregistry) | class | [`GPlatesUtils::Singleton<ExportRegistry>`](../utils/Singleton.md) | — | 0 | Used to register types to the scribe system so that they can be transcribed through base class pointers (ie, where the pointer dereference type is not the actual object type) and transcribed as stored types inside boost::variant. |

## Members

### `GPlatesScribe::ExportClassType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportClassType( const std::string &type_id_name_, const std::type_info &type_info_, const InternalUtils::TranscribeOwningPointer::non_null_ptr_to_const_type &transcribe_owning_pointer_)` | constructor | `None` | public | — |
| `type_id_name` | field | `std::string` | public | — |
| `type_info` | field | `boost::reference_wrapper<const std::type_info>` | public | — |
| `transcribe_owning_pointer` | field | `InternalUtils::TranscribeOwningPointer::non_null_ptr_to_const_type` | public | — |

### `GPlatesScribe::ExportRegistry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `register_class_type` | variable | `ExportClassType` | public | Registers a class type. |
| `get_class_type( const std::string &class_id_name)` | method | `boost::optional<const ExportClassType &>` | public | Returns the registered class type associated with the specified class id name. |
| `get_class_type( const std::type_info &class_type_info)` | method | `boost::optional<const ExportClassType &>` | public | Returns the registered class type associated with the specified class type info. |
| `unregister_class_type()` | method | `ExportClassType` | public | Unregisters a class type. |
| `class_type_pool_type` | typedef | `boost::object_pool<ExportClassType>` | private | Typedef for an object pool for ExportClassType. |
| `class_type_info_to_type_map_type` | typedef | `std::map<const std::type_info *, const ExportClassType *, InternalUtils::SortTypeInfoPredicate>` | private | Typedef for a mapping from class type info to ExportClassType. |
| `class_id_name_to_type_map_type` | typedef | `std::map<std::string, const ExportClassType *>` | private | Typedef for a mapping from class id name to ExportClassType. |
| `d_class_type_pool` | field | `class_type_pool_type` | private | Pool allocator for ExportClassType objects. |
| `d_class_type_info_to_type_map` | field | `class_type_info_to_type_map_type` | private | For searching ExportClassType by class type info. |
| `d_class_id_name_to_type_map` | field | `class_id_name_to_type_map_type` | private | For searching ExportClassType by class id name. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEEXPORTREGISTRY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=scribe/ScribeExportRegistry tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/ScribeVoidCastRegistry](ScribeVoidCastRegistry.md) | scribe | 33 |
| [scribe/Scribe](Scribe.md) | scribe | 20 |
| [scribe/ScribeExceptions](ScribeExceptions.md) | scribe | 15 |
| [scribe/TranscribeBoost](TranscribeBoost.md) | scribe | 10 |
| [scribe/ScribeInternalUtils](ScribeInternalUtils.md) | scribe | 5 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 2 |
| [scribe/ScribeExportRegistration](ScribeExportRegistration.md) | scribe | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeExportRegistry.h
python scripts/gpq.py def GPlatesScribe::ExportRegistry --body
python scripts/gpq.py uses ExportRegistry --kind class
python scripts/gpq.py hier ExportRegistry
```
