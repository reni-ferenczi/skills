# GpmlTimeWindow

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1183 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlTimeWindow.h` | C++ | 153 |
| `src/property-values/GpmlTimeWindow.cc` | C++ | 65 |

## Overview

`GpmlTimeWindow` is a plain value type — not a `PropertyValue` — that pairs a time-dependent `PropertyValue` with the `GmlTimePeriod` over which it is valid, plus the fixed `StructuralType` of the wrapped value. It is the element type of `GpmlPiecewiseAggregation`, the piecewise-constant time-dependent property representation: a feature property that changes value over discrete time ranges (for example, plate boundary topology that differs before and after a reorganisation) is stored as a sequence of `GpmlTimeWindow`s, each covering one interval.

This mirrors `GpmlTimeSample` (used by `GpmlIrregularSampling`) but covers a time *period* rather than a single time *instant*, matching the different sampling models GPML supports for time-dependent properties. `app-logic/TopologyInternalUtils` and the raster/scalar-field feature-property extractors are the heaviest consumers, picking the window whose period covers the reconstruction time being evaluated.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlTimeWindow`](#gplatespropertyvaluesgpmltimewindow) | class | [`GPlatesUtils::QtStreamable<GpmlTimeWindow>`](../utils/QtStreamable.md) | — | 0 | Since all the members of this class are of type boost::intrusive\_ptr or StructuralType (which wraps an StringSet::SharedIterator instance which points to a pre-allocated node in a StringSet), none of the construction, copy-construction or ... |

## Members

### `GPlatesPropertyValues::GpmlTimeWindow`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GpmlTimeWindow( GPlatesModel::PropertyValue::non_null_ptr_type time_dependent_value_, GmlTimePeriod::non_null_ptr_type valid_time_, const StructuralType &value_type_)` | constructor | `None` | public | — |
| `GpmlTimeWindow( const GpmlTimeWindow &other)` | constructor | `None` | public | — |
| `deep_clone()` | method | `GpmlTimeWindow` | public | — |
| `time_dependent_value()` | method | `GPlatesModel::PropertyValue::non_null_ptr_to_const_type` | public | Returns the 'const' time-dependent property value. |
| `set_time_dependent_value( GPlatesModel::PropertyValue::non_null_ptr_type v)` | method | `void` | public | — |
| `valid_time()` | method | `GmlTimePeriod::non_null_ptr_to_const_type` | public | Returns the 'const' time period. |
| `set_valid_time( GmlTimePeriod::non_null_ptr_type vt)` | method | `void` | public | — |
| `operator==( const GpmlTimeWindow &other)` | operator | `bool` | public | — |
| `d_time_dependent_value` | field | `GPlatesModel::PropertyValue::non_null_ptr_type` | private | — |
| `d_valid_time` | field | `GmlTimePeriod::non_null_ptr_type` | private | — |
| `d_value_type` | field | `StructuralType` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator==( const GpmlTimeWindow &other)` | operator | `bool` | — |
| `GPLATES_PROPERTYVALUES_GPMLTIMEWINDOW_H` | macro | `None` | — |
| `operator<<` | variable | `std::ostream` | operator\<\< for GpmlTimeWindow. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 24 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 8 |
| [app-logic/ExtractScalarField3DFeatureProperties](../app-logic/ExtractScalarField3DFeatureProperties.md) | app-logic | 8 |
| [property-values/GpmlPiecewiseAggregation](GpmlPiecewiseAggregation.md) | property-values | 8 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 7 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 6 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 4 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 4 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 3 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 3 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 3 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 3 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 2 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 2 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 2 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlTimeWindow.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlTimeWindow --body
python scripts/gpq.py uses GpmlTimeWindow --kind class
python scripts/gpq.py hier GpmlTimeWindow
```
