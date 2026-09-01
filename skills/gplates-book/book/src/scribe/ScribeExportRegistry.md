# ScribeExportRegistry

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 28 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeExportRegistry.h` | C++ | 269 |
| `src/scribe/ScribeExportRegistry.cc` | C++ | 66 |

## Overview

`ExportRegistry` is the runtime type registry the scribe framework needs whenever an object is transcribed through something other than its own concrete type — a base-class pointer, or a value stored inside a `boost::variant`. Without a registry, decoding a transcription that stored a polymorphic pointer would have no way to know which concrete `Type` to reconstruct; registration (normally done declaratively via an entry in `ScribeExportRegistration.h`, not by calling `register_class_type()` directly) records a string `class_id_name`, the `std::type_info`, and a `TranscribeOwningPointer` that knows how to construct and own that concrete type, then makes the mapping searchable both by name (for reading an archive) and by `std::type_info` (for writing one).

`ExportClassType` instances live in a `boost::object_pool`, owned for the process lifetime by the `ExportRegistry` singleton, so the `const ExportClassType &` returned by lookups stays valid indefinitely. `register_class_type()` statically asserts the type is not abstract (an abstract type can never be the concrete object behind a pointer) and tolerates being called twice for the same class as long as both calls agree on the type, since registration entries can appear more than once in translation units that both include the same header.

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

Registering the same `class_id_name` string for two different types, or the same `Type` under two different `class_id_name` strings, both throw (`ExportRegisteredMultipleClassTypesWithSameClassName` / `ExportRegisteredMultipleClassNamesWithSameClassType`) rather than silently overwriting an entry — a duplicate name is only safe when it is genuinely a re-registration of the same type. `unregister_class_type()` exists solely for unit tests to undo a registration; production code has no supported way to remove an entry once registered.

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
