# UnitTestTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/UnitTestTestSuite.h` | C++ | 46 |
| `src/unit-test/UnitTestTestSuite.cc` | C++ | 47 |

## Overview

Hierarchical test suite for the unit-test framework itself. Contains tests for `GPlatesUnitTest::TestSuiteFilter`, the singleton that manages selective test execution based on hierarchical name patterns. This suite exists to verify the test infrastructure works correctly and to demonstrate how to compose nested test suites using the `GPlatesTestSuite` base class pattern.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::UnitTestTestSuite`](#gplatesunittestunittesttestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::UnitTestTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnitTestTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_UNIT_TEST_TEST_SUITE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/MainTestSuite](MainTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/UnitTestTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::UnitTestTestSuite --body
python scripts/gpq.py uses UnitTestTestSuite --kind class
python scripts/gpq.py hier UnitTestTestSuite
```
