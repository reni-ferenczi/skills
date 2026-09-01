# GpmlTopologicalSection

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1649 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlTopologicalSection.h` | C++ | 154 |
| `src/property-values/GpmlTopologicalSection.cc` | C++ | 40 |

## Overview

`GpmlTopologicalSection` is the abstract common base for the property values that can appear as one element of a topological boundary or interior: `GpmlTopologicalLineSection` (a reversible reference to a line geometry, used with reconstructed plate boundaries) and `GpmlTopologicalPoint` (a reference to a single point). Containers such as `GpmlTopologicalPolygon`, `GpmlTopologicalLine` and `GpmlTopologicalNetwork` store their sections through this base so they can treat both kinds uniformly.

The `DEFINE_FUNCTION_DEEP_CLONE_AS_TOPO_SECTION()` macro exists because every derived class needs an identical override of `deep_clone_as_topo_section()` that forwards to that class's own non-virtual `deep_clone()` — the base class cannot provide this itself since `deep_clone()` returns the derived type and is not virtual.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlTopologicalSection`](#gplatespropertyvaluesgpmltopologicalsection) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 2 | This is an abstract class, because it derives from class PropertyValue, which contains the pure virtual member functions clone and accept\_visitor, which this class does not override with non-pure-virtual definitions. |

## Members

### `GPlatesPropertyValues::GpmlTopologicalSection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlTopologicalSection>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlTopologicalSection\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlTopologicalSection>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlTopologicalSection\>. |
| `GpmlTopologicalSection()` | constructor | `None` | public | Construct a GpmlTopologicalSection instance. |
| `GpmlTopologicalSection( const GpmlTopologicalSection &other)` | constructor | `None` | public | Construct a GpmlTopologicalSection instance which is a copy of other. |
| `~GpmlTopologicalSection()` | destructor | `None` | public | — |
| `deep_clone_as_topo_section()` | method | `non_null_ptr_type` | public | — |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `operator=` | field | `GpmlTopologicalSection` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALSECTION_H` | macro | `None` | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_TOPO_SECTION` | macro_function | `virtual \ const GpmlTopologicalSection::non_null_ptr_type \ deep_clone_as_topo_section() const \ { \ return deep_clone(); \ }` | This macro is used to define the virtual function 'deep\_clone\_as\_topo\_section' inside a class which derives from TopologicalSection. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 8 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 8 |
| [property-values/GpmlTopologicalLine](GpmlTopologicalLine.md) | property-values | 6 |
| [property-values/GpmlTopologicalNetwork](GpmlTopologicalNetwork.md) | property-values | 6 |
| [property-values/GpmlTopologicalPolygon](GpmlTopologicalPolygon.md) | property-values | 6 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 4 |
| [property-values/GpmlTopologicalLineSection](GpmlTopologicalLineSection.md) | property-values | 4 |
| [property-values/GpmlTopologicalPoint](GpmlTopologicalPoint.md) | property-values | 4 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 3 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 3 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 3 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 2 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [gui/TopologySectionsContainer](../gui/TopologySectionsContainer.md) | gui | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlTopologicalSection.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlTopologicalSection --body
python scripts/gpq.py uses GpmlTopologicalSection --kind class
python scripts/gpq.py hier GpmlTopologicalSection
```
