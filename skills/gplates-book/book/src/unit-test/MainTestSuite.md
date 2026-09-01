# MainTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1726 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/MainTestSuite.h` | C++ | 61 |
| `src/unit-test/MainTestSuite.cc` | C++ | 87 |

## Overview

The root test suite that aggregates all module-specific test suites. It inherits from `GPlatesTestSuite` with test level 0 and registers 16 sub-suites via `construct_maps()`: AppLogic, CanvasTools, DataMining, FeatureVisitors, FileIo, GeometryVisitors, Global, Gui, Maths, Model, Presentation, PropertyValues, Scribe, Utils, ViewOperations, and UnitTest. The `add_test_suites()` method registers each sub-suite with the Boost.Test master suite using a filter to control which tests run based on verbosity level.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::MainTestSuite`](#gplatesunittestmaintestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::MainTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MainTestSuite()` | constructor | `None` | public | — |
| `~MainTestSuite()` | destructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |
| `add_test_suites()` | method | `void` | protected | — |
| `add_test_cases()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_MAINTESTSUITE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_unit_test_main](../entry-points/gplates_unit_test_main.md) | entry-points | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/MainTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::MainTestSuite --body
python scripts/gpq.py uses MainTestSuite --kind class
python scripts/gpq.py hier MainTestSuite
```
