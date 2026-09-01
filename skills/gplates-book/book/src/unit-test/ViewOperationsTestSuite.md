# ViewOperationsTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/ViewOperationsTestSuite.h` | C++ | 46 |
| `src/unit-test/ViewOperationsTestSuite.cc` | C++ | 46 |

## Overview

Hierarchical test suite for view operations in GPlates. Currently empty with no child test suites added; the `construct_maps()` method contains a placeholder comment for future test suite additions. This suite is structured to support testing of view-related functionality as needed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::ViewOperationsTestSuite`](#gplatesunittestviewoperationstestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::ViewOperationsTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ViewOperationsTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_VIEW_OPERATIONS_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/ViewOperationsTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::ViewOperationsTestSuite --body
python scripts/gpq.py uses ViewOperationsTestSuite --kind class
python scripts/gpq.py hier ViewOperationsTestSuite
```
