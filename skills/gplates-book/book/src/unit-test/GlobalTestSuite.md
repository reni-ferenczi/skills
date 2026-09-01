# GlobalTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/GlobalTestSuite.h` | C++ | 46 |
| `src/unit-test/GlobalTestSuite.cc` | C++ | 46 |

## Overview

[[[PROSE overview unit=unit-test/GlobalTestSuite tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::GlobalTestSuite`](#gplatesunittestglobaltestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::GlobalTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GlobalTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_GLOBAL_TEST_SUITE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/GlobalTestSuite tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/MainTestSuite](MainTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/GlobalTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::GlobalTestSuite --body
python scripts/gpq.py uses GlobalTestSuite --kind class
python scripts/gpq.py hier GlobalTestSuite
```
