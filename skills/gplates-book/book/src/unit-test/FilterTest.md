# FilterTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1278 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/FilterTest.h` | C++ | 81 |
| `src/unit-test/FilterTest.cc` | C++ | 195 |

## Overview

Test fixtures for filter operations, likely exercising the `GPlatesUtils::PredicateFilter` and `GPlatesUtils::GenericFilter` classes used in data-mining workflows. The suite includes `FilterTest`, which holds seven individual test cases (test_case_1 through test_case_7), registered via `FilterTestSuite::construct_maps()`. The class uses auxiliary types like `MyPred` and `MyGFilterImpl` to demonstrate predicate and generic filter implementations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`InputIter`](#inputiter) | typedef | — | — | 0 | — |
| [`OutputIter`](#outputiter) | typedef | — | — | 0 | — |
| [`MyGFilterImpl`](#mygfilterimpl) | class | — | — | 0 | — |
| [`MyPred`](#mypred) | struct | — | — | 0 | — |
| [`GPlatesUnitTest::FilterTest`](#gplatesunittestfiltertest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::FilterTestSuite`](#gplatesunittestfiltertestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `InputIter`

*None.*

### `OutputIter`

*None.*

### `MyGFilterImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( std::vector<int>::const_iterator input_begin, std::vector<int>::const_iterator input_end, GPlatesUtils::FilterMapOutputHandler<OutputType, OutputMode> &result )` | operator | `int` | public | — |

### `MyPred`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `operator()( int)` | operator | `bool` | public | — |

### `GPlatesUnitTest::FilterTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FilterTest()` | constructor | `None` | public | — |
| `test_case_1()` | method | `void` | public | — |
| `test_case_2()` | method | `void` | public | — |
| `test_case_3()` | method | `void` | public | — |
| `test_case_4()` | method | `void` | public | — |
| `test_case_5()` | method | `void` | public | — |
| `test_case_6()` | method | `void` | public | — |
| `test_case_7()` | method | `void` | public | — |

### `GPlatesUnitTest::FilterTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FilterTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `dummy(int)` | function | `bool` | — |
| `GPLATES_UNIT_TEST_FILTER_TEST_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/DataMiningTestSuite](DataMiningTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/FilterTest.h
python scripts/gpq.py def GPlatesUnitTest::FilterTest --body
python scripts/gpq.py uses FilterTest --kind class
python scripts/gpq.py hier FilterTest
```
