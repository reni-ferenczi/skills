# ApplicationStateTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1725 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/ApplicationStateTest.h` | C++ | 100 |
| `src/unit-test/ApplicationStateTest.cc` | C++ | 56 |

## Overview

Unit test for `GPlatesAppLogic::ApplicationState`, verifying the model interface accessor through `test_get_model_interface()`. The test class is minimal: full instantiation of `ApplicationState` in test context is problematic because it depends on `QCoreApplication` initialization, which the Boost test harness does not set up properly, causing crashes during destruction via `QSettings`. The test is wrapped in `ApplicationStateTestSuite` for inclusion in larger test suites.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::ApplicationStateTest`](#gplatesunittestapplicationstatetest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::ApplicationStateTestSuite`](#gplatesunittestapplicationstatetestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::ApplicationStateTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ApplicationStateTest()` | constructor | `None` | public | — |
| `test_get_model_interface()` | method | `void` | public | — |

### `GPlatesUnitTest::ApplicationStateTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ApplicationStateTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_APPLICATIONSTATE_TEST_H` | macro | `None` | — |

## Notes

Do not instantiate `ApplicationState` as a member variable in the test—it will crash during test cleanup due to QSettings trying to access `QCoreApplication::applicationName()` when no proper `QCoreApplication` exists.

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/AppLogicTestSuite](AppLogicTestSuite.md) | unit-test | 1 |
| [unit-test/DataMiningTestSuite](DataMiningTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/ApplicationStateTest.h
python scripts/gpq.py def GPlatesUnitTest::ApplicationStateTest --body
python scripts/gpq.py uses ApplicationStateTest --kind class
python scripts/gpq.py hier ApplicationStateTest
```
