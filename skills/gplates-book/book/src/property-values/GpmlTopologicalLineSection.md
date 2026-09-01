# GpmlTopologicalLineSection

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1055 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlTopologicalLineSection.h` | C++ | 206 |
| `src/property-values/GpmlTopologicalLineSection.cc` | C++ | 61 |

## Overview

`GpmlTopologicalLineSection` implements `gpml:TopologicalLineSection`, one concrete kind of `GpmlTopologicalSection` used as an element of `GpmlTopologicalLine` (and of the boundary/interior sequences of topological polygons and networks). Rather than storing geometry directly, a section holds a `GpmlPropertyDelegate` pointing at the line geometry property of another feature, plus a `get_reverse_order()` flag saying whether that geometry should be traversed backwards when the sections are concatenated into a continuous line — since two adjacent sections must join head-to-tail regardless of how each source feature's coordinates happen to be ordered.

`app-logic/TopologyGeometryResolver` and `app-logic/TopologyNetworkResolver` are the primary consumers: they resolve each section's delegate to the referenced feature's actual geometry at a given reconstruction time and stitch the (possibly reversed) pieces together.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlTopologicalLineSection`](#gplatespropertyvaluesgpmltopologicallinesection) | class | [`GpmlTopologicalSection`](GpmlTopologicalSection.md) | — | 0 | This class implements the PropertyValue which corresponds to "gpml:TopologicalLineSection". |

## Members

### `GPlatesPropertyValues::GpmlTopologicalLineSection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlTopologicalLineSection>` | public | A convenience typedef for a shared pointer to a non-const GpmlTopologicalLineSection. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlTopologicalLineSection>` | public | A convenience typedef for a shared pointer to a const GpmlTopologicalLineSection. |
| `~GpmlTopologicalLineSection()` | destructor | `None` | public | — |
| `create( GpmlPropertyDelegate::non_null_ptr_type source_geometry, const bool reverse_order)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GpmlTopologicalLineSection::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_TOPO_SECTION()` | method | `None` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `get_source_geometry()` | method | `GpmlPropertyDelegate::non_null_ptr_type` | public | Returns the source geometry. |
| `set_source_geometry( const GpmlPropertyDelegate::non_null_ptr_type &source_geometry)` | method | `void` | public | Sets the source geometry. |
| `get_reverse_order()` | method | `bool` | public | Returns the reverse order. |
| `set_reverse_order( bool reverse_order)` | method | `void` | public | Sets the reverse order. |
| `GpmlTopologicalLineSection( GpmlPropertyDelegate::non_null_ptr_type source_geometry, const bool reverse_order)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlTopologicalLineSection( const GpmlTopologicalLineSection &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `operator=` | field | `GpmlTopologicalLineSection` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |
| `d_source_geometry` | field | `GpmlPropertyDelegate::non_null_ptr_type` | private | — |
| `d_reverse_order` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALLINESECTION_H` | macro | `None` | — |

## Notes

`directly_modifiable_fields_equal()` compares only the source-geometry delegate (by value, via `GpmlPropertyDelegate::operator==`); `d_reverse_order` is not part of that equality check, so two sections that reference the same source geometry but disagree on traversal direction currently compare equal for property-value-equality purposes.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 6 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 6 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 4 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 4 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 3 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 3 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlTopologicalLineSection.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlTopologicalLineSection --body
python scripts/gpq.py uses GpmlTopologicalLineSection --kind class
python scripts/gpq.py hier GpmlTopologicalLineSection
```
