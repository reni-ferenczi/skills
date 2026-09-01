# unit-test

[Book TOC](../TOC.md)

36 unit page(s), 70 source file(s) documented here, 2 further file(s) listed below.

## Overview

[[[PROSE component unit=component:unit-test tier=1]]]
Replace this whole block, markers included, with 2-4 paragraphs: what this component is responsible for, the load-bearing units and how it connects to neighbouring components. Do not restate the unit table.
[[[/PROSE]]]

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [AppLogicTestSuite](../src/unit-test/AppLogicTestSuite.md) | 3 | 96 | 11 | (pending) |
| [ApplicationStateTest](../src/unit-test/ApplicationStateTest.md) | 3 | 156 | 0 | (pending) |
| [CanvasToolsTestSuite](../src/unit-test/CanvasToolsTestSuite.md) | 3 | 91 | 0 | (pending) |
| [CoregTest](../src/unit-test/CoregTest.md) | 3 | 618 | 0 | (pending) |
| [CptPaletteTest](../src/unit-test/CptPaletteTest.md) | 3 | 224 | 3 | (pending) |
| [DataAssociationDataTableTest](../src/unit-test/DataAssociationDataTableTest.md) | 3 | 181 | 0 | (pending) |
| [DataMiningTestSuite](../src/unit-test/DataMiningTestSuite.md) | 3 | 102 | 0 | (pending) |
| [FeatureHandleTest](../src/unit-test/FeatureHandleTest.md) | 2 | 424 | 31 | (pending) |
| [FeatureVisitorsTestSuite](../src/unit-test/FeatureVisitorsTestSuite.md) | 3 | 91 | 0 | (pending) |
| [FileIoTestSuite](../src/unit-test/FileIoTestSuite.md) | 3 | 91 | 0 | (pending) |
| [FilterTest](../src/unit-test/FilterTest.md) | 3 | 276 | 0 | (pending) |
| [GPlatesGlobalFixture](../src/unit-test/GPlatesGlobalFixture.md) | 3 | 49 | 1 | (pending) |
| [GPlatesTestSuite](../src/unit-test/GPlatesTestSuite.md) | 2 | 158 | 333 | (pending) |
| [GenerateVelocityDomainCitcomsTest](../src/unit-test/GenerateVelocityDomainCitcomsTest.md) | 3 | 345 | 0 | (pending) |
| [GeometryVisitorsTestSuite](../src/unit-test/GeometryVisitorsTestSuite.md) | 3 | 92 | 0 | (pending) |
| [GlobalTestSuite](../src/unit-test/GlobalTestSuite.md) | 3 | 92 | 0 | (pending) |
| [GuiTestSuite](../src/unit-test/GuiTestSuite.md) | 3 | 95 | 0 | (pending) |
| [MainTestSuite](../src/unit-test/MainTestSuite.md) | 3 | 148 | 1 | (pending) |
| [MathsTestSuite](../src/unit-test/MathsTestSuite.md) | 3 | 93 | 0 | (pending) |
| [MipmapperTest](../src/unit-test/MipmapperTest.md) | 3 | 385 | 0 | (pending) |
| [ModelTestSuite](../src/unit-test/ModelTestSuite.md) | 3 | 94 | 0 | (pending) |
| [MultiThreadTest](../src/unit-test/MultiThreadTest.md) | 3 | 250 | 0 | (pending) |
| [PresentationTestSuite](../src/unit-test/PresentationTestSuite.md) | 3 | 93 | 0 | (pending) |
| [PropertyValuesTestSuite](../src/unit-test/PropertyValuesTestSuite.md) | 3 | 93 | 0 | (pending) |
| [RealTest](../src/unit-test/RealTest.md) | 3 | 165 | 0 | (pending) |
| [ScribeExportUnitTest](../src/unit-test/ScribeExportUnitTest.md) | 3 | 54 | 0 | (pending) |
| [ScribeTestSuite](../src/unit-test/ScribeTestSuite.md) | 3 | 98 | 0 | (pending) |
| [SmartNodeLinkedListTest](../src/unit-test/SmartNodeLinkedListTest.md) | 3 | 298 | 0 | (pending) |
| [StringSetTest](../src/unit-test/StringSetTest.md) | 3 | 134 | 0 | (pending) |
| [TestCase](../src/unit-test/TestCase.md) | 3 | 188 | 0 | (pending) |
| [TestSuiteFilter](../src/unit-test/TestSuiteFilter.md) | 2 | 237 | 43 | (pending) |
| [TestSuiteFilterTest](../src/unit-test/TestSuiteFilterTest.md) | 3 | 187 | 0 | (pending) |
| [TranscribeTest](../src/unit-test/TranscribeTest.md) | 2 | 3375 | 70 | (pending) |
| [UnitTestTestSuite](../src/unit-test/UnitTestTestSuite.md) | 3 | 93 | 0 | (pending) |
| [UtilsTestSuite](../src/unit-test/UtilsTestSuite.md) | 3 | 96 | 0 | (pending) |
| [ViewOperationsTestSuite](../src/unit-test/ViewOperationsTestSuite.md) | 3 | 92 | 0 | (pending) |

## Other files

| File | Kind | Lines |
|---|---|---|
| `src/unit-test/CMakeLists.txt` | build | 89 |
| `src/unit-test/add_tests.py` | Python | 70 |

## Depends on

| Component | References |
|---|---|
| [scribe](scribe.md) | 1263 |
| [model](model.md) | 201 |
| [utils](utils.md) | 181 |
| [gui](gui.md) | 175 |
| [maths](maths.md) | 163 |
| [property-values](property-values.md) | 110 |
| [file-io](file-io.md) | 74 |
| [data-mining](data-mining.md) | 48 |
| [global](global.md) | 29 |
| [app-logic](app-logic.md) | 20 |
| [qt-widgets](qt-widgets.md) | 13 |
| [feature-visitors](feature-visitors.md) | 5 |

## Used by

| Component | References |
|---|---|
| [qt-widgets](qt-widgets.md) | 21 |
| [file-io](file-io.md) | 19 |
| [opengl](opengl.md) | 15 |
| [gui](gui.md) | 12 |
| [app-logic](app-logic.md) | 10 |
| [entry-points](entry-points.md) | 10 |
| [deprecated](deprecated.md) | 7 |
| [api](api.md) | 5 |
| [scribe](scribe.md) | 5 |
| [utils](utils.md) | 2 |
| [data-mining](data-mining.md) | 1 |
| [maths](maths.md) | 1 |

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree src/unit-test
python scripts/gpq.py sym . --mode sub --path src/unit-test --defs-only
```
