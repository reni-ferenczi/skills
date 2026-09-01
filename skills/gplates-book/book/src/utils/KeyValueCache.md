# KeyValueCache

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 729 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/KeyValueCache.h` | C++ | 429 |

## Overview

[[[PROSE overview unit=utils/KeyValueCache tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::KeyValueCache`](#gplatesutilskeyvaluecache) | class | — | `<typename KeyType, typename ValueType>` | 0 | A least-recently used cache where the cached object is the value and it is inserted and retrieved from the cache using its associated key. |

## Members

### `GPlatesUtils::KeyValueCache`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `key_type` | typedef | `KeyType` | public | — |
| `value_type` | typedef | `ValueType` | public | — |
| `create_value_object_function_type` | typedef | `boost::function< value_type (const key_type &) >` | public | Typedef for a function to create a value\_type object given a key\_type. |
| `KeyValueCache( const create_value_object_function_type &create_value_object_function, unsigned int maximum_num_values_in_cache)` | constructor | `None` | public | Constructor accepting a function that creates a value object given a key object. |
| `KeyValueCache( unsigned int maximum_num_values_in_cache)` | constructor | `None` | public | Constructor that creates new value objects using the default constructor of ValueType. |
| `set_maximum_num_values_in_cache( unsigned int maximum_num_values_in_cache)` | method | `void` | public | Sets the maximum number of values in the cache. |
| `clear()` | method | `void` | public | Clears the cache by removing all cached value objects. |
| `has_key( const key_type &key)` | method | `bool` | public | Returns true if key currently exists in the cache. |
| `get_value` | field | `value_type` | public | Returns the 'non-const' value object corresponding to the specified key. |
| `this_type` | typedef | `KeyValueCache<KeyType,ValueType>` | private | Typedef for this class. |
| `value_object_seq_type` | typedef | `std::list<ValueObjectInfo>` | private | Typedef for a sequence of value objects. |
| `key_value_map_type` | typedef | `std::map<key_type, typename value_object_seq_type::iterator>` | private | Typedef to map a key/value pair. |
| `key_value_order_seq_type` | typedef | `std::list<typename key_value_map_type::iterator>` | private | Typedef to track least-recently to most-recently requested keys. |
| `ValueObjectInfo` | struct | `None` | private | Contains the value object and a reference to its entry in the least-recently used order list. |
| `d_create_value_object_function` | field | `create_value_object_function_type` | private | — |
| `d_maximum_num_value_objects_in_cache` | field | `unsigned int` | private | — |
| `d_value_objects` | field | `value_object_seq_type` | private | — |
| `d_key_value_map` | field | `key_value_map_type` | private | — |
| `d_key_value_order_seq` | field | `key_value_order_seq_type` | private | — |
| `d_num_value_objects_in_cache` | field | `unsigned int` | private | — |
| `default_create_value_object_function( const key_type &)` | method | `value_type` | private | The create\_value\_object\_function\_type used when value objects are default constructed. |
| `remove_least_recently_used_value()` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_KEYVALUECACHE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/KeyValueCache tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionTreeCreator](../app-logic/ReconstructionTreeCreator.md) | app-logic | 16 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 11 |
| [app-logic/ResolvedTriangulationNetwork](../app-logic/ResolvedTriangulationNetwork.md) | app-logic | 9 |
| [app-logic/ReconstructScalarCoverageLayerProxy](../app-logic/ReconstructScalarCoverageLayerProxy.md) | app-logic | 6 |
| [app-logic/VelocityFieldCalculatorLayerProxy](../app-logic/VelocityFieldCalculatorLayerProxy.md) | app-logic | 3 |
| [app-logic/ReconstructContext](../app-logic/ReconstructContext.md) | app-logic | 2 |
| [app-logic/MotionPathUtils](../app-logic/MotionPathUtils.md) | app-logic | 1 |
| [app-logic/ReconstructedFeatureGeometryFinder](../app-logic/ReconstructedFeatureGeometryFinder.md) | app-logic | 1 |
| [app-logic/ResolvedTriangulationDelaunay2](../app-logic/ResolvedTriangulationDelaunay2.md) | app-logic | 1 |
| [view-operations/GeometryBuilder](../view-operations/GeometryBuilder.md) | view-operations | 1 |
| [view-operations/InsertVertexGeometryOperation](../view-operations/InsertVertexGeometryOperation.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/KeyValueCache.h
python scripts/gpq.py def GPlatesUtils::KeyValueCache --body
python scripts/gpq.py uses KeyValueCache --kind class
python scripts/gpq.py hier KeyValueCache
```
