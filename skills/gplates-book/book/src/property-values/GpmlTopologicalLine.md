# GpmlTopologicalLine

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1003 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlTopologicalLine.h` | C++ | 213 |
| `src/property-values/GpmlTopologicalLine.cc` | C++ | 109 |

## Overview

`GpmlTopologicalLine` implements the `gpml:TopologicalLine` property value: a topological polyline defined as an ordered sequence of `GpmlTopologicalSection` elements, each of which contributes part of the line's geometry (typically by delegating to another feature's line geometry, possibly clipped between two points). It is the line counterpart of the topological-polygon/network property values, letting a feature such as a plate boundary segment be defined in terms of shared sections rather than duplicating coordinates.

`app-logic/TopologyGeometryResolver` and `app-logic/TopologyInternalUtils` walk the section sequence via `sections_begin()`/`sections_end()` to resolve the referenced features into an actual polyline geometry at a given reconstruction time.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlTopologicalLine`](#gplatespropertyvaluesgpmltopologicalline) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gpml:TopologicalLine". |

## Members

### `GPlatesPropertyValues::GpmlTopologicalLine`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlTopologicalLine>` | public | A convenience typedef for a shared pointer to a non-const GpmlTopologicalLine. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlTopologicalLine>` | public | A convenience typedef for a shared pointer to a const GpmlTopologicalLine. |
| `sections_seq_type` | typedef | `std::vector<GpmlTopologicalSection::non_null_ptr_type>` | public | Typedef for a sequence of topological sections. |
| `sections_const_iterator` | typedef | `sections_seq_type::const_iterator` | public | Typedef for a const iterator over the topological sections. |
| `~GpmlTopologicalLine()` | destructor | `None` | public | — |
| `create( const TopologicalSectionsIterator &sections_begin_, const TopologicalSectionsIterator &sections_end_)` | method | `non_null_ptr_type` | public | Create a GpmlTopologicalLine instance from the specified sequence of topological sections. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `sections_begin()` | method | `sections_const_iterator` | public | Return the "begin" const iterator to iterate over the topological sections. |
| `sections_end()` | method | `sections_const_iterator` | public | Return the "end" const iterator for iterating over the topological sections. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlTopologicalLine( const TopologicalSectionsIterator &sections_begin_, const TopologicalSectionsIterator &sections_end_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlTopologicalLine( const GpmlTopologicalLine &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | Need to compare all data members (recursively) since our sections are \*non-const\* non\_null\_intrusive\_ptr and hence can be modified by clients. |
| `d_sections` | field | `sections_seq_type` | private | — |
| `operator=` | field | `GpmlTopologicalLine` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `section_eq( const GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type &p1, const GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type &p2)` | function | `bool` | — |
| `GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALLINE_H` | macro | `None` | — |

## Notes

The sections vector holds *non-const* `non_null_intrusive_ptr`s, so a section reachable through this property value can be mutated by holders elsewhere; `directly_modifiable_fields_equal()` therefore compares sections by deep value equality (`operator==` on each `GpmlTopologicalSection`) rather than by pointer identity, and `deep_clone()` clones every section rather than sharing them. The header notes this as a known wart it would rather avoid by using const pointers throughout, but that would require const feature visitors and is a broader change.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 8 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 7 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 7 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 3 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlTopologicalLine.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlTopologicalLine --body
python scripts/gpq.py uses GpmlTopologicalLine --kind class
python scripts/gpq.py hier GpmlTopologicalLine
```
