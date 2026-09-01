# GpmlPiecewiseAggregation

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1156 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlPiecewiseAggregation.h` | C++ | 205 |
| `src/property-values/GpmlPiecewiseAggregation.cc` | C++ | 82 |

## Overview

[[[PROSE overview unit=property-values/GpmlPiecewiseAggregation tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlPiecewiseAggregation`](#gplatespropertyvaluesgpmlpiecewiseaggregation) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlPiecewiseAggregation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlPiecewiseAggregation>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlPiecewiseAggregation\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlPiecewiseAggregation>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlPiecewiseAggregation\>. |
| `~GpmlPiecewiseAggregation()` | destructor | `None` | public | — |
| `create( const std::vector<GpmlTimeWindow> &time_windows_, const StructuralType &value_type_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GpmlPiecewiseAggregation::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlPiecewiseAggregation( const std::vector<GpmlTimeWindow> &time_windows_, const StructuralType &value_type_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlPiecewiseAggregation( const GpmlPiecewiseAggregation &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | — |
| `d_time_windows` | field | `std::vector<GpmlTimeWindow>` | private | — |
| `d_value_type` | field | `StructuralType` | private | — |
| `operator=` | field | `GpmlPiecewiseAggregation` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLPIECEWISEAGGREGATION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlPiecewiseAggregation tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 2 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 1 |
| [app-logic/ExtractScalarField3DFeatureProperties](../app-logic/ExtractScalarField3DFeatureProperties.md) | app-logic | 1 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 1 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 1 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 1 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 1 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 1 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 1 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |

*... and 3 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlPiecewiseAggregation.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlPiecewiseAggregation --body
python scripts/gpq.py uses GpmlPiecewiseAggregation --kind class
python scripts/gpq.py hier GpmlPiecewiseAggregation
```
