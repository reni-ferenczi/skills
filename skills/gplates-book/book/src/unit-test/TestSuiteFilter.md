# TestSuiteFilter

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1603 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/TestSuiteFilter.h` | C++ | 76 |
| `src/unit-test/TestSuiteFilter.cc` | C++ | 161 |

## Overview

[[[PROSE overview unit=unit-test/TestSuiteFilter tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::FilterData`](#gplatesunittestfilterdata) | typedef | — | — | 0 | — |
| [`GPlatesUnitTest::TestSuiteFilter`](#gplatesunittesttestsuitefilter) | class | [`GPlatesUtils::Singleton<TestSuiteFilter>`](../utils/Singleton.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::FilterData`

*None.*

### `GPlatesUnitTest::TestSuiteFilter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `set_filter_string( std::string)` | method | `void` | public | — |
| `is_empty( unsigned depth)` | method | `bool` | public | — |
| `pass( std::string test_suite_name, unsigned depth)` | method | `bool` | public | — |
| `is_match( std::string, std::string)` | method | `bool` | public | — |
| `get_filter()` | method | `FilterData` | public | — |
| `d_filter` | field | `FilterData` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `d_filter` | variable | `GPlatesUnitTest::FilterData` | — |
| `GPLATES_UNIT_TEST_TESTSUITEFILTER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/TestSuiteFilter tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TestSuiteFilterTest](TestSuiteFilterTest.md) | unit-test | 35 |
| [unit-test/GPlatesTestSuite](GPlatesTestSuite.md) | unit-test | 5 |
| [entry-points/gplates_unit_test_main](../entry-points/gplates_unit_test_main.md) | entry-points | 3 |
| [unit-test/MainTestSuite](MainTestSuite.md) | unit-test | 3 |
| [unit-test/UnitTestTestSuite](UnitTestTestSuite.md) | unit-test | 2 |
| [unit-test/AppLogicTestSuite](AppLogicTestSuite.md) | unit-test | 1 |
| [unit-test/CanvasToolsTestSuite](CanvasToolsTestSuite.md) | unit-test | 1 |
| [unit-test/DataMiningTestSuite](DataMiningTestSuite.md) | unit-test | 1 |
| [unit-test/FeatureVisitorsTestSuite](FeatureVisitorsTestSuite.md) | unit-test | 1 |
| [unit-test/FileIoTestSuite](FileIoTestSuite.md) | unit-test | 1 |
| [unit-test/GeometryVisitorsTestSuite](GeometryVisitorsTestSuite.md) | unit-test | 1 |
| [unit-test/GlobalTestSuite](GlobalTestSuite.md) | unit-test | 1 |
| [unit-test/GuiTestSuite](GuiTestSuite.md) | unit-test | 1 |
| [unit-test/MathsTestSuite](MathsTestSuite.md) | unit-test | 1 |
| [unit-test/ModelTestSuite](ModelTestSuite.md) | unit-test | 1 |
| [unit-test/PresentationTestSuite](PresentationTestSuite.md) | unit-test | 1 |
| [unit-test/PropertyValuesTestSuite](PropertyValuesTestSuite.md) | unit-test | 1 |
| [unit-test/UtilsTestSuite](UtilsTestSuite.md) | unit-test | 1 |
| [unit-test/ViewOperationsTestSuite](ViewOperationsTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/TestSuiteFilter.h
python scripts/gpq.py def GPlatesUnitTest::TestSuiteFilter --body
python scripts/gpq.py uses TestSuiteFilter --kind class
python scripts/gpq.py hier TestSuiteFilter
```
