# ApplicationStateTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1725 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/ApplicationStateTest.h` | C++ | 100 |
| `src/unit-test/ApplicationStateTest.cc` | C++ | 56 |

## Overview

[[[PROSE overview unit=unit-test/ApplicationStateTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=unit-test/ApplicationStateTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
