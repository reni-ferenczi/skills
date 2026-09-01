# data-mining

[Book TOC](../TOC.md)

47 unit page(s), 68 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:data-mining tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/data-mining`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [CheckAttrTypeVisitor](../src/data-mining/CheckAttrTypeVisitor.md) | 2 | 294 | 58 | Feature visitor that classifies a property value's type as numeric or string for co-registration config |
| [CoRegConfigurationTable](../src/data-mining/CoRegConfigurationTable.md) | 1 | 526 | 420 | (pending) |
| [CoRegFilter](../src/data-mining/CoRegFilter.md) | 2 | 218 | 65 | Abstract base and Config for filters that narrow reconstructed features before co-registration |
| [CoRegFilterCache](../src/data-mining/CoRegFilterCache.md) | 3 | 170 | 7 | Cache for reconstructed feature vectors keyed by co-registration filter configuration |
| [CoRegFilterMapReduceFactory](../src/data-mining/CoRegFilterMapReduceFactory.md) | 3 | 215 | 4 | Static factories for filter, mapper, and reducer components of co-registration data mining |
| [CoRegMapper](../src/data-mining/CoRegMapper.md) | 2 | 95 | 20 | Abstract map stage that extracts one OpaqueData attribute per reconstructed feature |
| [CoRegReducer](../src/data-mining/CoRegReducer.md) | 2 | 132 | 47 | Abstract reduce stage that aggregates mapped attribute values into a single co-registration result |
| [DataMiningCache](../src/data-mining/DataMiningCache.md) | 3 | 89 | 0 | Generic template cache interface supporting perfect hits, partial hits, and misses |
| [DataMiningUtils](../src/data-mining/DataMiningUtils.md) | 2 | 521 | 92 | Free-function toolbox for attribute extraction, geometry distance and config-file loading in co-registration |
| [DataSelector](../src/data-mining/DataSelector.md) | 2 | 730 | 23 | Drives a co-registration run, filling a DataTable from seed features and target layer proxies |
| [DataTable](../src/data-mining/DataTable.md) | 2 | 287 | 127 | Co-registration result table: one DataRow of OpaqueData per seed, with header and CSV export |
| [GetValueFromPropertyVisitor](../src/data-mining/GetValueFromPropertyVisitor.md) | 3 | 308 | 5 | Visitor that extracts scalar and geometric data from property values |
| [LookupReducer](../src/data-mining/LookupReducer.md) | 3 | 249 | 1 | Reducer that selects data by proximity to a seed geometry |
| [MaxReducer](../src/data-mining/MaxReducer.md) | 3 | 76 | 1 | Reducer that returns the maximum numeric value from a dataset |
| [MeanReducer](../src/data-mining/MeanReducer.md) | 3 | 59 | 1 | Reducer that returns the arithmetic mean of numeric values |
| [MedianReducer](../src/data-mining/MedianReducer.md) | 3 | 69 | 1 | Reducer that returns the median of numeric values using partitioning |
| [MinReducer](../src/data-mining/MinReducer.md) | 3 | 78 | 1 | Computes the minimum value from a sequence of numerical data in co-registration pipelines |
| [OpaqueData](../src/data-mining/OpaqueData.md) | 2 | 102 | 96 | Shared variant value type and empty-value sentinel used across the co-registration pipeline |
| [OpaqueDataToDouble](../src/data-mining/OpaqueDataToDouble.md) | 3 | 89 | 2 | Visitor that extracts numeric values from opaque data variant type |
| [OpaqueDataToQString](../src/data-mining/OpaqueDataToQString.md) | 3 | 98 | 8 | Visitor that converts opaque data to QString for UI display |
| [PercentileReducer](../src/data-mining/PercentileReducer.md) | 3 | 53 | 1 | Placeholder reducer for computing percentiles from numerical data sequences |
| [PopulateShapeFileAttributesVisitor](../src/data-mining/PopulateShapeFileAttributesVisitor.md) | 3 | 204 | 4 | Feature visitor that extracts shapefile attribute names for export |
| [RFGToPropertyValueMapper](../src/data-mining/RFGToPropertyValueMapper.md) | 3 | 97 | 2 | Mapper extracting property values from reconstructed features for co-registration |
| [RFGToRelationalPropertyMapper](../src/data-mining/RFGToRelationalPropertyMapper.md) | 3 | 124 | 1 | Mapper computing relational attributes like distance between reconstructed features |
| [RegionOfInterestFilter](../src/data-mining/RegionOfInterestFilter.md) | 3 | 321 | 6 | Filters reconstructed geometries within a distance threshold of a seed feature |
| [ScribeExportDataMining](../src/data-mining/ScribeExportDataMining.md) | 3 | 56 | 0 | Registers Scribe serialization mappings for data-mining filter configuration classes |
| [SeedSelfFilter](../src/data-mining/SeedSelfFilter.md) | 3 | 168 | 1 | Filter that outputs a single seed feature regardless of input, used to bootstrap co-registration |
| [Types](../src/data-mining/Types.md) | 2 | 199 | 91 | Attribute-source and reducer enums shared by the co-registration filter/map/reduce pipeline |
| [VoteReducer](../src/data-mining/VoteReducer.md) | 3 | 85 | 1 | Reducer that finds the most frequently occurring value through voting |
| [WeightedMeanReducer](../src/data-mining/WeightedMeanReducer.md) | 3 | 52 | 1 | Stub reducer for computing weighted means, currently unimplemented |

### `src/data-mining/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AssociationOperatorFactory](../src/data-mining/deprecated/AssociationOperatorFactory.md) | 3 | 60 | 2 | Factory for creating AssociationOperator instances based on type enum |
| [DataOperator](../src/data-mining/deprecated/DataOperator.md) | 3 | 278 | 37 | Abstract base class for extracting and reducing feature data in data-mining workflows |
| [DataOperatorFactory](../src/data-mining/deprecated/DataOperatorFactory.md) | 3 | 124 | 10 | Factory for creating DataOperator instances based on operation type |
| [DistanceDataOperator](../src/data-mining/deprecated/DistanceDataOperator.md) | 3 | 142 | 4 | Abstract base for distance-based data extraction with pluggable reduction strategy |
| [IsInRegionOfInterestVisitor](../src/data-mining/deprecated/IsInRegionOfInterestVisitor.md) | 3 | 595 | 47 | Double-dispatch visitor for testing spatial proximity between spherical geometries |
| [LookupDataOperator](../src/data-mining/deprecated/LookupDataOperator.md) | 3 | 224 | 1 | Data operator that retrieves attribute values from features or shapefile attributes |
| [MaxDistanceDataOperator](../src/data-mining/deprecated/MaxDistanceDataOperator.md) | 3 | 70 | 0 | Data operator subclass for computing maximum distance (unimplemented) |
| [MeanDistanceDataOperator](../src/data-mining/deprecated/MeanDistanceDataOperator.md) | 3 | 73 | 0 | Data operator subclass for computing mean distance (unimplemented) |
| [MedianDistanceDataOperator](../src/data-mining/deprecated/MedianDistanceDataOperator.md) | 3 | 73 | 0 | Data operator subclass for computing median distance (unimplemented) |
| [MinDataOperator](../src/data-mining/deprecated/MinDataOperator.md) | 3 | 200 | 2 | Data operator that finds the minimum value from feature properties |
| [MinDistanceDataOperator](../src/data-mining/deprecated/MinDistanceDataOperator.md) | 3 | 96 | 1 | Data operator subclass for computing minimum distance |
| [NumInROIDataOperator](../src/data-mining/deprecated/NumInROIDataOperator.md) | 3 | 77 | 1 | Data operator that counts features in a region of interest |
| [PresenceDataOperator](../src/data-mining/deprecated/PresenceDataOperator.md) | 3 | 83 | 1 | Deprecated data operator that appends a presence indicator to a data row |
| [Prospector](../src/data-mining/deprecated/Prospector.md) | 3 | 47 | 8 | Deprecated abstract base class defining the interface for prospector jobs |
| [RegionOfInterestAssociationOperator](../src/data-mining/deprecated/RegionOfInterestAssociationOperator.md) | 3 | 233 | 2 | Deprecated association operator identifying target features within a proximity range of seed geometry |
| [SubDataSelector](../src/data-mining/deprecated/SubDataSelector.md) | 3 | 161 | 0 | Deprecated prospector job that extracts data for a seed feature using co-registration configuration |
| [TaskQueue](../src/data-mining/deprecated/TaskQueue.md) | 3 | 189 | 0 | Deprecated thread pool implementation for executing prospector jobs asynchronously |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/data-mining/CMakeLists.txt` | build | 57 |

## Depends on

| Component | References |
|---|---|
| [app-logic](app-logic.md) | 428 |
| [model](model.md) | 372 |
| [scribe](scribe.md) | 176 |
| [maths](maths.md) | 152 |
| [property-values](property-values.md) | 97 |
| [global](global.md) | 51 |
| [utils](utils.md) | 34 |
| [file-io](file-io.md) | 34 |
| [opengl](opengl.md) | 20 |
| [gui](gui.md) | 19 |
| [feature-visitors](feature-visitors.md) | 18 |
| [qt-widgets](qt-widgets.md) | 13 |
| [canvas-tools](canvas-tools.md) | 3 |
| [presentation](presentation.md) | 2 |
| [unit-test](unit-test.md) | 1 |

## Used by

| Component | References |
|---|---|
| [qt-widgets](qt-widgets.md) | 167 |
| [api](api.md) | 166 |
| [presentation](presentation.md) | 142 |
| [app-logic](app-logic.md) | 71 |
| [unit-test](unit-test.md) | 48 |
| [gui](gui.md) | 20 |
| [maths](maths.md) | 19 |
| [utils](utils.md) | 8 |
| [opengl](opengl.md) | 6 |
| [file-io](file-io.md) | 5 |
| [entry-points](entry-points.md) | 1 |
| [feature-visitors](feature-visitors.md) | 1 |
| [property-values](property-values.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/data-mining
python scripts/gpq.py sym . --mode sub --path src/data-mining --defs-only
```
