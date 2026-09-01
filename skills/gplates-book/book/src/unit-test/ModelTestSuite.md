# ModelTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/ModelTestSuite.h` | C++ | 46 |
| `src/unit-test/ModelTestSuite.cc` | C++ | 48 |

## Overview

A test suite container for model-related tests. It inherits from `GPlatesTestSuite` and aggregates child test suites—specifically `FeatureHandleTest`—via its `construct_maps()` method, which registers them using the `ADD_TESTSUITE` macro. This suite is part of GPlates' hierarchical test framework, organizing tests for the feature data model.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::ModelTestSuite`](#gplatesunittestmodeltestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::ModelTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ModelTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_MODEL_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/ModelTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::ModelTestSuite --body
python scripts/gpq.py uses ModelTestSuite --kind class
python scripts/gpq.py hier ModelTestSuite
```
