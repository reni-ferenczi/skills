# MainTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1726 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/MainTestSuite.h` | C++ | 61 |
| `src/unit-test/MainTestSuite.cc` | C++ | 87 |

## Overview

[[[PROSE overview unit=unit-test/MainTestSuite tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=unit-test/MainTestSuite tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
