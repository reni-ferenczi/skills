# PresentationTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/PresentationTestSuite.h` | C++ | 47 |
| `src/unit-test/PresentationTestSuite.cc` | C++ | 46 |

## Overview

A test suite container for presentation-layer tests. It inherits from `GPlatesTestSuite` but is currently empty, with no child test suites registered. This is a placeholder in the hierarchical test framework for tests of the view state and visual layer subsystem in the presentation module.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::PresentationTestSuite`](#gplatesunittestpresentationtestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::PresentationTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PresentationTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_PRESENTATION_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/PresentationTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::PresentationTestSuite --body
python scripts/gpq.py uses PresentationTestSuite --kind class
python scripts/gpq.py hier PresentationTestSuite
```
