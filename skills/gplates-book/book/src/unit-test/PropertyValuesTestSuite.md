# PropertyValuesTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/PropertyValuesTestSuite.h` | C++ | 47 |
| `src/unit-test/PropertyValuesTestSuite.cc` | C++ | 46 |

## Overview

[[[PROSE overview unit=unit-test/PropertyValuesTestSuite tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::PropertyValuesTestSuite`](#gplatesunittestpropertyvaluestestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::PropertyValuesTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PropertyValuesTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_PROPERTYVALUES_TEST_SUITE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/PropertyValuesTestSuite tier=3]]]
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
python scripts/gpq.py file src/unit-test/PropertyValuesTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::PropertyValuesTestSuite --body
python scripts/gpq.py uses PropertyValuesTestSuite --kind class
python scripts/gpq.py hier PropertyValuesTestSuite
```
