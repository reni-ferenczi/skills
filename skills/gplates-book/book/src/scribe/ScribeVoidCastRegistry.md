# ScribeVoidCastRegistry

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 28 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeVoidCastRegistry.h` | C++ | 514 |
| `src/scribe/ScribeVoidCastRegistry.cc` | C++ | 315 |

## Overview

`VoidCastRegistry` lets `Scribe` cast between base and derived class pointers when it only has a `void *` and a pair of `std::type_info` references — the situation it is in whenever it transcribes a polymorphic object through a base-class interface. Code registers each inheritance edge once, at static-initialisation time, via the templated `register_derived_base_class_inheritance()`; the registry stores the edges as a graph of `ClassNode`s linked by `ClassLink`s keyed on `std::type_info`, so later casts are a graph search rather than a compile-time `static_cast`.

`up_cast()` and `down_cast()` each find the path between the derived and base `ClassNode`s with `find_derived_to_base_path()`, then walk it applying each link's virtual `upcast()`/`downcast()`. The per-link cast itself is generated at registration time by the templated `DerivedBaseClassLink<DerivedType, BaseType>`, which picks a `dynamic_cast` (checked, throws `std::bad_cast` on failure) or a `static_cast` depending on whether `DerivedType`/`BaseType` is polymorphic, so the registry works even for non-polymorphic types that only `Scribe` treats as related. `boost::shared_ptr<void>` overloads exist alongside the raw-pointer ones because `Scribe` special-cases `shared_ptr`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::VoidCastRegistry`](#gplatesscribevoidcastregistry) | class | `boost::noncopyable` | — | 0 | Handles casting 'void \*' pointers from base to derived classes and vice versa. |

## Members

### `GPlatesScribe::VoidCastRegistry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `register_derived_base_class_inheritance()` | method | `void` | public | Registers an inheritance link between the specified base and derived class types. |
| `up_cast( const std::type_info &derived_type, const std::type_info &base_type, void *derived_object_address)` | method | `boost::optional<void *>` | public | Casts a 'void' pointer from a derived class to a base class. derived\_object\_address is expected to be a pointer to type derived\_type. |
| `up_cast( const std::type_info &derived_type, const std::type_info &base_type, const boost::shared_ptr<void> &derived_object_address)` | method | `boost::optional< boost::shared_ptr<void> >` | public | Helper function for up-casting a boost::shared\_ptr. |
| `down_cast( const std::type_info &derived_type, const std::type_info &base_type, void *base_object_address)` | method | `boost::optional<void *>` | public | Casts a 'void' pointer from a base class to a derived class. base\_object\_address is expected to be a pointer to type base\_type. |
| `down_cast( const std::type_info &derived_type, const std::type_info &base_type, const boost::shared_ptr<void> &base_object_address)` | method | `boost::optional< boost::shared_ptr<void> >` | public | Helper function for down-casting a boost::shared\_ptr. |
| `class_type_info_to_node_map_type` | typedef | `std::map<const std::type_info *, ClassNode *, InternalUtils::SortTypeInfoPredicate>` | private | Typedef for a mapping from class type info to ClassNode. |
| `class_type_info_to_link_map_type` | typedef | `std::map<const std::type_info *, ClassLink *, InternalUtils::SortTypeInfoPredicate>` | private | Typedef for a mapping from class type info to ClassNode. |
| `ClassNode` | struct | `None` | private | Represents a class in the inheritance graph. |
| `ClassLink` | struct | `None` | private | Represents an inheritance link between two classes in the inheritance graph. |
| `DerivedBaseClassLink` | struct | `None` | private | — |
| `class_links_list_type` | typedef | `GPlatesUtils::IntrusiveSinglyLinkedList<const ClassLink>` | private | Typedef for a linked list of class links. |
| `class_node_pool_type` | typedef | `boost::object_pool<ClassNode>` | private | Typedef for a pool of ClassNode objects. |
| `link_seq_type` | typedef | `std::vector<ClassLink::non_null_ptr_type>` | private | Typedef for a sequence of class links. |
| `d_class_node_storage` | field | `class_node_pool_type` | private | — |
| `d_class_link_storage` | field | `link_seq_type` | private | — |
| `d_class_type_info_to_node_map` | field | `class_type_info_to_node_map_type` | private | — |
| `get_or_create_class_node( const std::type_info &class_type_info)` | method | `ClassNode` | private | Gets, or creates if doesn't exist, the class node for the specified class type info. |
| `create_class_link_if_necessary( ClassNode *derived_class_node, ClassNode *base_class_node)` | method | `void` | private | Creates, if necessary, a class link between the specified derived and base class nodes. |
| `find_derived_to_base_path( class_links_list_type &derived_to_base_path, const std::type_info &derived_type, const std::type_info &base_type)` | method | `bool` | private | Used when recursively searching for a path from derived type to a base type. |
| `find_derived_to_base_path( class_links_list_type &derived_to_base_path, const ClassNode &current_class_node, const std::type_info &derived_type, const std::type_info &base_type)` | method | `bool` | private | Used when recursively searching for a path from derived type to a base type. |
| `get_base_to_derived_path( class_links_list_type &base_to_derived_path, class_links_list_type::const_iterator derived_to_base_path_iter, class_links_list_type::const_iterator derived_to_base_path_end)` | method | `void` | private | Reverses the derived-to-base path to get the base-to-derived path. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEVOIDCASTREGISTRY_H` | macro | `None` | — |

## Notes

- A derived type with more than one distinct path to the same base (repeated non-virtual inheritance, or a diamond) makes `find_derived_to_base_path()` throw `Exceptions::AmbiguousCast` instead of picking one path arbitrarily; virtual-inheritance diamonds throw for the same reason even though they have only one base sub-object, because the registry does not model virtual bases.
- `up_cast()`/`down_cast()` return `boost::none` rather than throwing when no registered path exists between the two types — callers must check the `boost::optional` before dereferencing.
- Casting between identical `derived_type`/`base_type` short-circuits to the original address without a graph lookup.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeVoidCastRegistry.h
python scripts/gpq.py def GPlatesScribe::VoidCastRegistry --body
python scripts/gpq.py uses VoidCastRegistry --kind class
python scripts/gpq.py hier VoidCastRegistry
```
