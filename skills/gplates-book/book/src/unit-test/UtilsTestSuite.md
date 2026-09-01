# UtilsTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/UtilsTestSuite.h` | C++ | 46 |
| `src/unit-test/UtilsTestSuite.cc` | C++ | 50 |

## Overview

Hierarchical test suite for GPlates utility classes. Contains test suites for `GPlatesUtils::SmartNodeLinkedList`, a smart-pointer-managed linked list, and `GPlatesUtils::StringSet`, a string interning data structure. This suite groups tests for foundational utility components that are used throughout the codebase.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::UtilsTestSuite`](#gplatesunittestutilstestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::UtilsTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UtilsTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_UTILS_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/UtilsTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::UtilsTestSuite --body
python scripts/gpq.py uses UtilsTestSuite --kind class
python scripts/gpq.py hier UtilsTestSuite
```
