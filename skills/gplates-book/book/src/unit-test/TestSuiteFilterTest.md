# TestSuiteFilterTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1549 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/TestSuiteFilterTest.h` | C++ | 72 |
| `src/unit-test/TestSuiteFilterTest.cc` | C++ | 115 |

## Overview

Test suite for `GPlatesUnitTest::TestSuiteFilter`, a singleton that selectively runs tests based on hierarchical name patterns. The filter uses a format similar to filesystem paths (with `/` and `,` delimiters) to specify which tests to include at each depth level, and supports wildcard matching with `*` to enable flexible test selection from the command line.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::TestSuiteFilterTest`](#gplatesunittesttestsuitefiltertest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::TestSuiteFilterTestSuite`](#gplatesunittesttestsuitefiltertestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::TestSuiteFilterTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TestSuiteFilterTest()` | constructor | `None` | public | — |
| `test_is_empty()` | method | `void` | public | — |
| `test_is_match()` | method | `void` | public | — |
| `test_pass()` | method | `void` | public | — |
| `test_set_filter_string()` | method | `void` | public | — |
| `d_test_suite_filter` | field | `GPlatesUnitTest::TestSuiteFilter` | private | — |

### `GPlatesUnitTest::TestSuiteFilterTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TestSuiteFilterTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_TESTSUITEFILTER_TEST_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/UnitTestTestSuite](UnitTestTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/TestSuiteFilterTest.h
python scripts/gpq.py def GPlatesUnitTest::TestSuiteFilterTest --body
python scripts/gpq.py uses TestSuiteFilterTest --kind class
python scripts/gpq.py hier TestSuiteFilterTest
```
