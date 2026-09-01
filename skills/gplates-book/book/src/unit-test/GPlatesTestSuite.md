# GPlatesTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/GPlatesTestSuite.h` | C++ | 87 |
| `src/unit-test/GPlatesTestSuite.cc` | C++ | 71 |

## Overview

`GPlatesTestSuite` is the common base for every `boost::unit_test::test_suite` in this directory, giving the hand-written suite hierarchy a uniform two-phase construction: `init()` calls the virtual `construct_maps()` (overridden by each concrete suite to populate `d_test_cases_map` and `d_test_suites_map` via the `ADD_TESTCASE`/`ADD_TESTSUITE` macros), then `add_test_suites()` and `add_test_cases()` walk those maps and register each entry with Boost.Test's `add()`, but only if `TestSuiteFilter::instance().pass(name, d_level)` allows it. This is what lets a single command-line filter decide, suite by suite and case by case, which parts of the (very large) tree actually run.

`d_level` records the suite's depth from the root and is threaded through `ADD_TESTSUITE` as `d_level + 1` when a suite instantiates its children, so the filter can apply depth-based rules as well as name-based ones. The private default constructor blocks a `GPlatesTestSuite` from being built without a name, since `boost::unit_test::test_suite` requires one.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::GPlatesTestSuite`](#gplatesunittestgplatestestsuite) | class | `boost::unit_test::test_suite` | — | 31 | — |

## Members

### `GPlatesUnitTest::GPlatesTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GPlatesTestSuite(std::string name)` | constructor | `None` | public | — |
| `TestSuiteMap` | typedef | `std::map< const std::string, GPlatesUnitTest::GPlatesTestSuite*>` | protected | — |
| `TestCaseMap` | typedef | `std::map< const std::string, boost::unit_test::test_case*>` | protected | — |
| `d_test_suites_map` | field | `TestSuiteMap` | protected | — |
| `d_test_cases_map` | field | `TestCaseMap` | protected | — |
| `d_level` | field | `unsigned` | protected | — |
| `init(unsigned level)` | method | `void` | protected | — |
| `construct_maps()` | method | `void` | protected | — |
| `add_test_suites()` | method | `void` | protected | — |
| `add_test_cases()` | method | `void` | protected | — |
| `GPlatesTestSuite()` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_GPLATESTESTSUITE_H` | macro | `None` | — |
| `ADD_TESTCASE` | macro_function | `d_test_cases_map[#test_case_name] = BOOST_CLASS_TEST_CASE( \ &test_suite_name::test_case_name, instance ); \ qDebug()<<"creating "#test_case_name" testcase ...";` | — |
| `ADD_TESTSUITE` | macro_function | `d_test_suites_map[#test_suite_name] = \ new GPlatesUnitTest::test_suite_name ## TestSuite(d_level+1); \ qDebug()<<"creating "#test_suite_name"TestSuite ...";` | — |

## Notes

`ADD_TESTSUITE` heap-allocates the child suite with `new` inside `construct_maps()`, before `add_test_suites()` ever consults `TestSuiteFilter`. So a suite rejected by the filter is still fully constructed — including running its own `construct_maps()`, which recursively builds and allocates further child suites — it is simply never passed to Boost.Test's `add()` and never executed.

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](TranscribeTest.md) | unit-test | 67 |
| [unit-test/GenerateVelocityDomainCitcomsTest](GenerateVelocityDomainCitcomsTest.md) | unit-test | 24 |
| [unit-test/MainTestSuite](MainTestSuite.md) | unit-test | 24 |
| [unit-test/MipmapperTest](MipmapperTest.md) | unit-test | 21 |
| [unit-test/MultiThreadTest](MultiThreadTest.md) | unit-test | 21 |
| [unit-test/TestSuiteFilterTest](TestSuiteFilterTest.md) | unit-test | 18 |
| [unit-test/RealTest](RealTest.md) | unit-test | 15 |
| [unit-test/CptPaletteTest](CptPaletteTest.md) | unit-test | 11 |
| [unit-test/FeatureHandleTest](FeatureHandleTest.md) | unit-test | 11 |
| [unit-test/FilterTest](FilterTest.md) | unit-test | 11 |
| [unit-test/SmartNodeLinkedListTest](SmartNodeLinkedListTest.md) | unit-test | 11 |
| [unit-test/StringSetTest](StringSetTest.md) | unit-test | 9 |
| [unit-test/UtilsTestSuite](UtilsTestSuite.md) | unit-test | 9 |
| [unit-test/DataMiningTestSuite](DataMiningTestSuite.md) | unit-test | 8 |
| [unit-test/MathsTestSuite](MathsTestSuite.md) | unit-test | 8 |
| [unit-test/ScribeTestSuite](ScribeTestSuite.md) | unit-test | 8 |
| [unit-test/UnitTestTestSuite](UnitTestTestSuite.md) | unit-test | 8 |
| [unit-test/GeometryVisitorsTestSuite](GeometryVisitorsTestSuite.md) | unit-test | 7 |
| [unit-test/GlobalTestSuite](GlobalTestSuite.md) | unit-test | 7 |
| [unit-test/PresentationTestSuite](PresentationTestSuite.md) | unit-test | 7 |

*... and 13 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/GPlatesTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::GPlatesTestSuite --body
python scripts/gpq.py uses GPlatesTestSuite --kind class
python scripts/gpq.py hier GPlatesTestSuite
```
