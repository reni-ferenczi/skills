# RealTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1659 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/RealTest.h` | C++ | 75 |
| `src/unit-test/RealTest.cc` | C++ | 90 |

## Overview

Tests the floating-point utility functions in `GPlatesMaths` that classify special double values. `RealTest` contains four test methods that verify the predicates for detecting positive infinity, negative infinity, NaN (not-a-number), and zero—checking both positive and negative cases. `RealTestSuite` wraps these tests in the hierarchical framework, instantiating `RealTest` and registering its test cases via the `ADD_TESTCASE` macro.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::RealTest`](#gplatesunittestrealtest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::RealTestSuite`](#gplatesunittestrealtestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::RealTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RealTest()` | constructor | `None` | public | — |
| `test_positive_infinity()` | method | `void` | public | — |
| `test_negative_infinity()` | method | `void` | public | — |
| `test_nan()` | method | `void` | public | — |
| `test_zero()` | method | `void` | public | — |
| `zero` | field | `double` | private | — |

### `GPlatesUnitTest::RealTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RealTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_REAL_TEST_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/MathsTestSuite](MathsTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/RealTest.h
python scripts/gpq.py def GPlatesUnitTest::RealTest --body
python scripts/gpq.py uses RealTest --kind class
python scripts/gpq.py hier RealTest
```
