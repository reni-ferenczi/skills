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
| [CheckAttrTypeVisitor](../src/data-mining/CheckAttrTypeVisitor.md) | 2 | 294 | 58 | (pending) |
| [CoRegConfigurationTable](../src/data-mining/CoRegConfigurationTable.md) | 1 | 526 | 420 | (pending) |
| [CoRegFilter](../src/data-mining/CoRegFilter.md) | 2 | 218 | 65 | (pending) |
| [CoRegFilterCache](../src/data-mining/CoRegFilterCache.md) | 3 | 170 | 7 | (pending) |
| [CoRegFilterMapReduceFactory](../src/data-mining/CoRegFilterMapReduceFactory.md) | 3 | 215 | 4 | (pending) |
| [CoRegMapper](../src/data-mining/CoRegMapper.md) | 2 | 95 | 20 | (pending) |
| [CoRegReducer](../src/data-mining/CoRegReducer.md) | 2 | 132 | 47 | (pending) |
| [DataMiningCache](../src/data-mining/DataMiningCache.md) | 3 | 89 | 0 | (pending) |
| [DataMiningUtils](../src/data-mining/DataMiningUtils.md) | 2 | 521 | 92 | (pending) |
| [DataSelector](../src/data-mining/DataSelector.md) | 2 | 730 | 23 | (pending) |
| [DataTable](../src/data-mining/DataTable.md) | 2 | 287 | 127 | (pending) |
| [GetValueFromPropertyVisitor](../src/data-mining/GetValueFromPropertyVisitor.md) | 3 | 308 | 5 | (pending) |
| [LookupReducer](../src/data-mining/LookupReducer.md) | 3 | 249 | 1 | (pending) |
| [MaxReducer](../src/data-mining/MaxReducer.md) | 3 | 76 | 1 | (pending) |
| [MeanReducer](../src/data-mining/MeanReducer.md) | 3 | 59 | 1 | (pending) |
| [MedianReducer](../src/data-mining/MedianReducer.md) | 3 | 69 | 1 | (pending) |
| [MinReducer](../src/data-mining/MinReducer.md) | 3 | 78 | 1 | (pending) |
| [OpaqueData](../src/data-mining/OpaqueData.md) | 2 | 102 | 96 | (pending) |
| [OpaqueDataToDouble](../src/data-mining/OpaqueDataToDouble.md) | 3 | 89 | 2 | (pending) |
| [OpaqueDataToQString](../src/data-mining/OpaqueDataToQString.md) | 3 | 98 | 8 | (pending) |
| [PercentileReducer](../src/data-mining/PercentileReducer.md) | 3 | 53 | 1 | (pending) |
| [PopulateShapeFileAttributesVisitor](../src/data-mining/PopulateShapeFileAttributesVisitor.md) | 3 | 204 | 4 | (pending) |
| [RFGToPropertyValueMapper](../src/data-mining/RFGToPropertyValueMapper.md) | 3 | 97 | 2 | (pending) |
| [RFGToRelationalPropertyMapper](../src/data-mining/RFGToRelationalPropertyMapper.md) | 3 | 124 | 1 | (pending) |
| [RegionOfInterestFilter](../src/data-mining/RegionOfInterestFilter.md) | 3 | 321 | 6 | (pending) |
| [ScribeExportDataMining](../src/data-mining/ScribeExportDataMining.md) | 3 | 56 | 0 | (pending) |
| [SeedSelfFilter](../src/data-mining/SeedSelfFilter.md) | 3 | 168 | 1 | (pending) |
| [Types](../src/data-mining/Types.md) | 2 | 199 | 91 | (pending) |
| [VoteReducer](../src/data-mining/VoteReducer.md) | 3 | 85 | 1 | (pending) |
| [WeightedMeanReducer](../src/data-mining/WeightedMeanReducer.md) | 3 | 52 | 1 | (pending) |

### `src/data-mining/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AssociationOperatorFactory](../src/data-mining/deprecated/AssociationOperatorFactory.md) | 3 | 60 | 2 | (pending) |
| [DataOperator](../src/data-mining/deprecated/DataOperator.md) | 3 | 278 | 37 | (pending) |
| [DataOperatorFactory](../src/data-mining/deprecated/DataOperatorFactory.md) | 3 | 124 | 10 | (pending) |
| [DistanceDataOperator](../src/data-mining/deprecated/DistanceDataOperator.md) | 3 | 142 | 4 | (pending) |
| [IsInRegionOfInterestVisitor](../src/data-mining/deprecated/IsInRegionOfInterestVisitor.md) | 3 | 595 | 47 | (pending) |
| [LookupDataOperator](../src/data-mining/deprecated/LookupDataOperator.md) | 3 | 224 | 1 | (pending) |
| [MaxDistanceDataOperator](../src/data-mining/deprecated/MaxDistanceDataOperator.md) | 3 | 70 | 0 | (pending) |
| [MeanDistanceDataOperator](../src/data-mining/deprecated/MeanDistanceDataOperator.md) | 3 | 73 | 0 | (pending) |
| [MedianDistanceDataOperator](../src/data-mining/deprecated/MedianDistanceDataOperator.md) | 3 | 73 | 0 | (pending) |
| [MinDataOperator](../src/data-mining/deprecated/MinDataOperator.md) | 3 | 200 | 2 | (pending) |
| [MinDistanceDataOperator](../src/data-mining/deprecated/MinDistanceDataOperator.md) | 3 | 96 | 1 | (pending) |
| [NumInROIDataOperator](../src/data-mining/deprecated/NumInROIDataOperator.md) | 3 | 77 | 1 | (pending) |
| [PresenceDataOperator](../src/data-mining/deprecated/PresenceDataOperator.md) | 3 | 83 | 1 | (pending) |
| [Prospector](../src/data-mining/deprecated/Prospector.md) | 3 | 47 | 8 | (pending) |
| [RegionOfInterestAssociationOperator](../src/data-mining/deprecated/RegionOfInterestAssociationOperator.md) | 3 | 233 | 2 | (pending) |
| [SubDataSelector](../src/data-mining/deprecated/SubDataSelector.md) | 3 | 161 | 0 | (pending) |
| [TaskQueue](../src/data-mining/deprecated/TaskQueue.md) | 3 | 189 | 0 | (pending) |


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
