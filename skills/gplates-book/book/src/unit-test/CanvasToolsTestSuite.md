# CanvasToolsTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/CanvasToolsTestSuite.h` | C++ | 46 |
| `src/unit-test/CanvasToolsTestSuite.cc` | C++ | 45 |

## Overview

Placeholder test suite for canvas tools functionality. Currently empty—no test cases are registered in `construct_maps()`. Intended to hold unit tests for the interactive canvas tools subsystem, which handles user interaction and rendering on the map viewport.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::CanvasToolsTestSuite`](#gplatesunittestcanvastoolstestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::CanvasToolsTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CanvasToolsTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_CANVAS_TOOLS_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/CanvasToolsTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::CanvasToolsTestSuite --body
python scripts/gpq.py uses CanvasToolsTestSuite --kind class
python scripts/gpq.py hier CanvasToolsTestSuite
```
