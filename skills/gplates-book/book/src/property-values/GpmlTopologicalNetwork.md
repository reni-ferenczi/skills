# GpmlTopologicalNetwork

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 725 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlTopologicalNetwork.h` | C++ | 278 |
| `src/property-values/GpmlTopologicalNetwork.cc` | C++ | 150 |

## Overview

[[[PROSE overview unit=property-values/GpmlTopologicalNetwork tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlTopologicalNetwork`](#gplatespropertyvaluesgpmltopologicalnetwork) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gpml:TopologicalNetwork". |

## Members

### `GPlatesPropertyValues::GpmlTopologicalNetwork`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlTopologicalNetwork>` | public | A convenience typedef for a shared pointer to a non-const GpmlTopologicalNetwork. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlTopologicalNetwork>` | public | A convenience typedef for a shared pointer to a const GpmlTopologicalNetwork. |
| `boundary_sections_seq_type` | typedef | `std::vector<GpmlTopologicalSection::non_null_ptr_type>` | public | Typedef for a sequence of boundary sections. |
| `boundary_sections_const_iterator` | typedef | `boundary_sections_seq_type::const_iterator` | public | Typedef for a const iterator over the boundary sections. |
| `interior_geometry_seq_type` | typedef | `std::vector<GpmlPropertyDelegate::non_null_ptr_type>` | public | Typedef for a sequence of interior geometries. |
| `interior_geometries_const_iterator` | typedef | `interior_geometry_seq_type::const_iterator` | public | Typedef for a const iterator over the interior geometries. |
| `~GpmlTopologicalNetwork()` | destructor | `None` | public | — |
| `create( const BoundaryTopologicalSectionsIterator &boundary_sections_begin_, const BoundaryTopologicalSectionsIterator &boundary_sections_end_)` | method | `non_null_ptr_type` | public | Create a GpmlTopologicalNetwork instance which contains a boundary only (no interior geometries). |
| `create( const BoundaryTopologicalSectionsIterator &boundary_sections_begin_, const BoundaryTopologicalSectionsIterator &boundary_sections_end_, const InteriorGeometriesIterator &interior_geometries_begin_, const InteriorGeometriesIterator &interior_geometries_end_)` | method | `non_null_ptr_type` | public | Create a GpmlTopologicalNetwork instance which contains a boundary and interior geometries. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `boundary_sections_begin()` | method | `boundary_sections_const_iterator` | public | Return the "begin" const iterator to iterate over the boundary sections. |
| `boundary_sections_end()` | method | `boundary_sections_const_iterator` | public | Return the "end" const iterator for iterating over the boundary sections. |
| `interior_geometries_begin()` | method | `interior_geometries_const_iterator` | public | Return the "begin" const iterator to iterate over the interior geometries. |
| `interior_geometries_end()` | method | `interior_geometries_const_iterator` | public | Return the "end" const iterator for iterating over the interior geometries. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlTopologicalNetwork( const BoundaryTopologicalSectionsIterator &boundary_sections_begin_, const BoundaryTopologicalSectionsIterator &boundary_sections_end_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlTopologicalNetwork( const BoundaryTopologicalSectionsIterator &boundary_sections_begin_, const BoundaryTopologicalSectionsIterator &boundary_sections_end_, const InteriorGeometriesIterator &interior_geometries_begin_, const InteriorGeometriesIterator &interior_geometries_end_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlTopologicalNetwork( const GpmlTopologicalNetwork &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | Need to compare all data members (recursively) since our boundary sections and interior geometries are \*non-const\* non\_null\_intrusive\_ptr and hence can be modified by clients. |
| `d_boundary_sections` | field | `boundary_sections_seq_type` | private | — |
| `d_interior_geometries` | field | `interior_geometry_seq_type` | private | — |
| `operator=` | field | `GpmlTopologicalNetwork` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `section_eq( const GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_to_const_type &p1, const GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_to_const_type &p2)` | function | `bool` | — |
| `delegate_eq( const GPlatesPropertyValues::GpmlPropertyDelegate::non_null_ptr_to_const_type &d1, const GPlatesPropertyValues::GpmlPropertyDelegate::non_null_ptr_to_const_type &d2)` | function | `bool` | — |
| `GPLATES_PROPERTY_VALUES_GPMLTOPOLOGICALNETWORK_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlTopologicalNetwork tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 10 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 10 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 8 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 8 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 2 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 1 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlTopologicalNetwork.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlTopologicalNetwork --body
python scripts/gpq.py uses GpmlTopologicalNetwork --kind class
python scripts/gpq.py hier GpmlTopologicalNetwork
```
