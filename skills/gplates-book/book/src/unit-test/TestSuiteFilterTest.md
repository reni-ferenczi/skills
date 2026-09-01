# TestSuiteFilterTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1549 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/TestSuiteFilterTest.h` | C++ | 72 |
| `src/unit-test/TestSuiteFilterTest.cc` | C++ | 115 |

## Overview

[[[PROSE overview unit=unit-test/TestSuiteFilterTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=unit-test/TestSuiteFilterTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
