# RealTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1659 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/RealTest.h` | C++ | 75 |
| `src/unit-test/RealTest.cc` | C++ | 90 |

## Overview

[[[PROSE overview unit=unit-test/RealTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=unit-test/RealTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
