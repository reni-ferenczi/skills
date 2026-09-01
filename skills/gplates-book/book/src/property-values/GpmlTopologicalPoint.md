# GpmlTopologicalPoint

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1157 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlTopologicalPoint.h` | C++ | 184 |
| `src/property-values/GpmlTopologicalPoint.cc` | C++ | 61 |

## Overview

[[[PROSE overview unit=property-values/GpmlTopologicalPoint tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlTopologicalPoint`](#gplatespropertyvaluesgpmltopologicalpoint) | class | [`GpmlTopologicalSection`](GpmlTopologicalSection.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlTopologicalPoint`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlTopologicalPoint>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlTopologicalPoint\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlTopologicalPoint>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlTopologicalPoint\>. |
| `~GpmlTopologicalPoint()` | destructor | `None` | public | — |
| `create( GpmlPropertyDelegate::non_null_ptr_type source_geometry)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GpmlTopologicalPoint::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_TOPO_SECTION()` | method | `None` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `get_source_geometry()` | method | `GpmlPropertyDelegate::non_null_ptr_type` | public | access to d\_source\_geometry |
| `set_source_geometry( GpmlPropertyDelegate::non_null_ptr_type intersection_geom)` | method | `void` | public | — |
| `GpmlTopologicalPoint( GpmlPropertyDelegate::non_null_ptr_type source_geometry)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlTopologicalPoint( const GpmlTopologicalPoint &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `operator=` | field | `GpmlTopologicalPoint` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |
| `d_source_geometry` | field | `GpmlPropertyDelegate::non_null_ptr_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALPOINT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlTopologicalPoint tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 1 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 1 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlTopologicalPoint.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlTopologicalPoint --body
python scripts/gpq.py uses GpmlTopologicalPoint --kind class
python scripts/gpq.py hier GpmlTopologicalPoint
```
