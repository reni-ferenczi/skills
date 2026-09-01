# AppLogicTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/AppLogicTestSuite.h` | C++ | 46 |
| `src/unit-test/AppLogicTestSuite.cc` | C++ | 50 |

## Overview

Test suite for application-logic subsystems. Aggregates unit tests for `ApplicationStateTest` and `GenerateVelocityDomainCitcomsTest`, which verify the core state management and domain-generation code that powers GPlates' interactive features. Used by higher-level test suites like `DataAssociationDataTableTest` and `DataMiningTestSuite` to ensure these dependencies work correctly in integration scenarios.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::AppLogicTestSuite`](#gplatesunittestapplogictestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::AppLogicTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AppLogicTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_APP_LOGIC_TEST_SUITE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/DataAssociationDataTableTest](DataAssociationDataTableTest.md) | unit-test | 5 |
| [unit-test/MainTestSuite](MainTestSuite.md) | unit-test | 5 |
| [unit-test/DataMiningTestSuite](DataMiningTestSuite.md) | unit-test | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/AppLogicTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::AppLogicTestSuite --body
python scripts/gpq.py uses AppLogicTestSuite --kind class
python scripts/gpq.py hier AppLogicTestSuite
```
