# TestSuiteFilter

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1603 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/TestSuiteFilter.h` | C++ | 76 |
| `src/unit-test/TestSuiteFilter.cc` | C++ | 161 |

## Overview

`TestSuiteFilter` is the `GPlatesUtils::Singleton` that `GPlatesTestSuite::add_test_suites()`/`add_test_cases()` consult to decide which suites and cases actually get registered with Boost.Test, letting a single command-line string select a subtree of the otherwise-fixed test hierarchy without recompiling. `set_filter_string()` parses that string on `/` into one path segment per tree depth, then each segment on `,` into a `FilterData` of alternative name patterns for that depth; `pass(test_suite_name, depth)` returns true if the filter has no entry for that depth (`is_empty()`) or if `test_suite_name` matches any pattern at that depth via `is_match()`.

`is_match()` supports exact names, an empty pattern or a bare `*` (match anything), and a single leading or trailing `*` for suffix/prefix matching — it does not implement general glob or regex matching beyond those cases.

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

`d_filter` is `static`, so the filter string set via `set_filter_string()` is shared by every reference to the singleton — there is exactly one active filter for the whole test binary, not one per suite. `is_empty()` and `is_match()` treat malformed input leniently: an out-of-range depth or an exception during lookup makes `is_empty()` return `true` (i.e. "no restriction, let it pass") rather than propagating the error, and `is_match()` falls through to `false` for any pattern shape it does not recognise instead of raising one.

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
