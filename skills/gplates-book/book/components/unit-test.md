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
| [AppLogicTestSuite](../src/unit-test/AppLogicTestSuite.md) | 3 | 96 | 11 | Test suite for application-logic subsystems |
| [ApplicationStateTest](../src/unit-test/ApplicationStateTest.md) | 3 | 156 | 0 | Unit test for ApplicationState model interface accessor |
| [CanvasToolsTestSuite](../src/unit-test/CanvasToolsTestSuite.md) | 3 | 91 | 0 | Placeholder test suite for canvas tools functionality |
| [CoregTest](../src/unit-test/CoregTest.md) | 3 | 618 | 0 | Unit tests for co-registration data mining functionality |
| [CptPaletteTest](../src/unit-test/CptPaletteTest.md) | 3 | 224 | 3 | Unit tests for CPT color palette parsing and retrieval |
| [DataAssociationDataTableTest](../src/unit-test/DataAssociationDataTableTest.md) | 3 | 181 | 0 | Unit test for DataTable heterogeneous data container |
| [DataMiningTestSuite](../src/unit-test/DataMiningTestSuite.md) | 3 | 102 | 0 | Aggregate test suite for data-mining subsystem |
| [FeatureHandleTest](../src/unit-test/FeatureHandleTest.md) | 2 | 424 | 31 | Boost.Test fixture for FeatureHandle whose test cases are stubs or disabled memory-pool experiments |
| [FeatureVisitorsTestSuite](../src/unit-test/FeatureVisitorsTestSuite.md) | 3 | 91 | 0 | Placeholder test suite for feature visitor patterns |
| [FileIoTestSuite](../src/unit-test/FileIoTestSuite.md) | 3 | 91 | 0 | Container for Boost.Test cases exercising file I/O operations |
| [FilterTest](../src/unit-test/FilterTest.md) | 3 | 276 | 0 | Test fixtures for filter operations in data-mining workflows |
| [GPlatesGlobalFixture](../src/unit-test/GPlatesGlobalFixture.md) | 3 | 49 | 1 | Global Boost.Test fixture redirecting test logging to file |
| [GPlatesTestSuite](../src/unit-test/GPlatesTestSuite.md) | 2 | 158 | 333 | Common base for the hand-written Boost.Test suite hierarchy, filtering suites/cases via TestSuiteFilter |
| [GenerateVelocityDomainCitcomsTest](../src/unit-test/GenerateVelocityDomainCitcomsTest.md) | 3 | 345 | 0 | Tests for velocity domain generation from CitCOMS geodynamic models |
| [GeometryVisitorsTestSuite](../src/unit-test/GeometryVisitorsTestSuite.md) | 3 | 92 | 0 | Container for test cases exercising geometry visitor patterns |
| [GlobalTestSuite](../src/unit-test/GlobalTestSuite.md) | 3 | 92 | 0 | Container for global-scope test cases |
| [GuiTestSuite](../src/unit-test/GuiTestSuite.md) | 3 | 95 | 0 | Container for GUI-related test suites |
| [MainTestSuite](../src/unit-test/MainTestSuite.md) | 3 | 148 | 1 | Root test suite aggregating all module-specific test suites |
| [MathsTestSuite](../src/unit-test/MathsTestSuite.md) | 3 | 93 | 0 | Test suite container for mathematics-related tests |
| [MipmapperTest](../src/unit-test/MipmapperTest.md) | 3 | 385 | 0 | Tests mipmapping functionality for raster downsampling across multiple data types |
| [ModelTestSuite](../src/unit-test/ModelTestSuite.md) | 3 | 94 | 0 | Test suite container for feature data model tests |
| [MultiThreadTest](../src/unit-test/MultiThreadTest.md) | 3 | 250 | 0 | Test framework for multi-threading and performance profiling |
| [PresentationTestSuite](../src/unit-test/PresentationTestSuite.md) | 3 | 93 | 0 | Test suite container for presentation-layer tests |
| [PropertyValuesTestSuite](../src/unit-test/PropertyValuesTestSuite.md) | 3 | 93 | 0 | Test suite container for property value type tests |
| [RealTest](../src/unit-test/RealTest.md) | 3 | 165 | 0 | Tests floating-point utility functions for classifying special values |
| [ScribeExportUnitTest](../src/unit-test/ScribeExportUnitTest.md) | 3 | 54 | 0 | Registers test classes with the Scribe serialization framework |
| [ScribeTestSuite](../src/unit-test/ScribeTestSuite.md) | 3 | 98 | 0 | test suite for the GPlatesScribe serialization framework |
| [SmartNodeLinkedListTest](../src/unit-test/SmartNodeLinkedListTest.md) | 3 | 298 | 0 | test suite for smart-pointer-managed linked-list operations |
| [StringSetTest](../src/unit-test/StringSetTest.md) | 3 | 134 | 0 | test suite for string interning data structure |
| [TestCase](../src/unit-test/TestCase.md) | 3 | 188 | 0 | template files for generating new test case classes |
| [TestSuiteFilter](../src/unit-test/TestSuiteFilter.md) | 2 | 237 | 43 | Singleton parsing a /- and ,-delimited filter string to decide which test suites/cases run |
| [TestSuiteFilterTest](../src/unit-test/TestSuiteFilterTest.md) | 3 | 187 | 0 | test suite for selective test execution with hierarchical patterns |
| [TranscribeTest](../src/unit-test/TranscribeTest.md) | 2 | 3375 | 70 | Round-trip test suite for the GPlatesScribe serialisation framework across text, binary and XML archives |
| [UnitTestTestSuite](../src/unit-test/UnitTestTestSuite.md) | 3 | 93 | 0 | hierarchical test suite for the unit-test framework |
| [UtilsTestSuite](../src/unit-test/UtilsTestSuite.md) | 3 | 96 | 0 | hierarchical test suite for GPlates utility classes |
| [ViewOperationsTestSuite](../src/unit-test/ViewOperationsTestSuite.md) | 3 | 92 | 0 | hierarchical test suite for view operations |

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
