# AppLogicTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/AppLogicTestSuite.h` | C++ | 46 |
| `src/unit-test/AppLogicTestSuite.cc` | C++ | 50 |

## Overview

[[[PROSE overview unit=unit-test/AppLogicTestSuite tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=unit-test/AppLogicTestSuite tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
