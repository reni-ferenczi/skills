# FeatureVisitorsTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/FeatureVisitorsTestSuite.h` | C++ | 46 |
| `src/unit-test/FeatureVisitorsTestSuite.cc` | C++ | 45 |

## Overview

Placeholder test suite for feature visitor patterns. Currently empty—no test cases are registered in `construct_maps()`. Intended to hold unit tests for the visitor pattern implementations used to traverse and process feature data structures in the model layer.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::FeatureVisitorsTestSuite`](#gplatesunittestfeaturevisitorstestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::FeatureVisitorsTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureVisitorsTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_FEATURE_VISITORS_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/FeatureVisitorsTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::FeatureVisitorsTestSuite --body
python scripts/gpq.py uses FeatureVisitorsTestSuite --kind class
python scripts/gpq.py hier FeatureVisitorsTestSuite
```
