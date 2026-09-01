# feature-visitors

[Book TOC](../TOC.md)

20 unit page(s), 40 source file(s) documented here, 1 further file(s) listed below.

## Overview

[[[PROSE component unit=component:feature-visitors tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

### `src/feature-visitors`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [FeatureClassifier](../src/feature-visitors/FeatureClassifier.md) | 3 | 360 | 0 | Classifies features by their GPML properties to categorize reconstruction, reconstructable, and instantaneous features |
| [FromQvariantConverter](../src/feature-visitors/FromQvariantConverter.md) | 2 | 313 | 13 | Rebuilds a PropertyValue from an edited QVariant by re-visiting the original value |
| [GeometryFinder](../src/feature-visitors/GeometryFinder.md) | 2 | 391 | 58 | Collects all point, line, multi-point and polygon geometry from a feature |
| [GeometryRotator](../src/feature-visitors/GeometryRotator.md) | 3 | 181 | 0 | Applies a finite rotation to all geometry properties in a feature |
| [GeometrySetter](../src/feature-visitors/GeometrySetter.md) | 2 | 281 | 362 | Writes a given GeometryOnSphere into an existing geometry PropertyValue |
| [GeometryTypeFinder](../src/feature-visitors/GeometryTypeFinder.md) | 2 | 465 | 64 | Counts geometry types found on a feature or GeometryOnSphere without collecting them |
| [KeyValueDictionaryFinder](../src/feature-visitors/KeyValueDictionaryFinder.md) | 2 | 180 | 43 | Collects GpmlKeyValueDictionary property values from a feature |
| [PropertyValueFinder](../src/feature-visitors/PropertyValueFinder.md) | 1 | 951 | 320 | (pending) |
| [QueryFeaturePropertiesWidgetPopulator](../src/feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | 3 | 945 | 4 | Populates a tree widget with all properties of a feature for display in the GUI |
| [ShapefileAttributeFinder](../src/feature-visitors/ShapefileAttributeFinder.md) | 2 | 309 | 95 | Reads one named shapefile attribute out of a feature's key-value dictionary |
| [ToQvariantConverter](../src/feature-visitors/ToQvariantConverter.md) | 2 | 575 | 38 | Converts a visited PropertyValue into a display- or edit-role QVariant |
| [TopologySectionsFinder](../src/feature-visitors/TopologySectionsFinder.md) | 2 | 530 | 61 | Extracts a topological feature's boundary and interior sections as table rows |
| [TotalReconstructionSequencePlateIdFinder](../src/feature-visitors/TotalReconstructionSequencePlateIdFinder.md) | 2 | 212 | 28 | Const feature visitor extracting fixed and moving reference-frame plate IDs from a TRS feature |
| [TotalReconstructionSequenceRotationInserter](../src/feature-visitors/TotalReconstructionSequenceRotationInserter.md) | 3 | 602 | 3 | Inserts or updates a rotation in a total reconstruction sequence at a specific time |
| [TotalReconstructionSequenceRotationInterpolater](../src/feature-visitors/TotalReconstructionSequenceRotationInterpolater.md) | 3 | 414 | 1 | Interpolates a rotation from a total reconstruction sequence at a specific time |
| [TotalReconstructionSequenceTimePeriodFinder](../src/feature-visitors/TotalReconstructionSequenceTimePeriodFinder.md) | 2 | 296 | 8 | Const feature visitor deriving the begin and end times of a TRS from its irregular sampling |
| [ViewFeatureGeometriesWidgetPopulator](../src/feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | 3 | 1018 | 6 | Populates a tree widget with both present-day and reconstructed geometry coordinates |

### `src/feature-visitors/deprecated`

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [GmlTimePeriodFinder](../src/feature-visitors/deprecated/GmlTimePeriodFinder.md) | 3 | 194 | 0 | Finds and accumulates all gml:TimePeriod objects in a feature |
| [PlateIdFinder](../src/feature-visitors/deprecated/PlateIdFinder.md) | 3 | 207 | 0 | Finds and accumulates all plate IDs in a feature |
| [XsStringFinder](../src/feature-visitors/deprecated/XsStringFinder.md) | 3 | 194 | 0 | const feature visitor for collecting XsString properties from a feature |


## Other files

| File | Kind | Lines |
|---|---|---|
| `src/feature-visitors/CMakeLists.txt` | build | 49 |

## Depends on

| Component | References |
|---|---|
| [model](model.md) | 1168 |
| [property-values](property-values.md) | 409 |
| [maths](maths.md) | 395 |
| [gui](gui.md) | 239 |
| [app-logic](app-logic.md) | 182 |
| [utils](utils.md) | 74 |
| [file-io](file-io.md) | 34 |
| [global](global.md) | 13 |
| [qt-widgets](qt-widgets.md) | 12 |
| [scribe](scribe.md) | 2 |
| [data-mining](data-mining.md) | 1 |

## Used by

| Component | References |
|---|---|
| [qt-widgets](qt-widgets.md) | 394 |
| [file-io](file-io.md) | 224 |
| [gui](gui.md) | 138 |
| [app-logic](app-logic.md) | 108 |
| [property-values](property-values.md) | 95 |
| [view-operations](view-operations.md) | 76 |
| [api](api.md) | 40 |
| [data-mining](data-mining.md) | 18 |
| [utils](utils.md) | 6 |
| [unit-test](unit-test.md) | 5 |
| [presentation](presentation.md) | 3 |
| [canvas-tools](canvas-tools.md) | 2 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/feature-visitors
python scripts/gpq.py sym . --mode sub --path src/feature-visitors --defs-only
```
