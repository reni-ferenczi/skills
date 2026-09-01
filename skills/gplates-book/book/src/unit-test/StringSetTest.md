# StringSetTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/StringSetTest.h` | C++ | 63 |
| `src/unit-test/StringSetTest.cc` | C++ | 71 |

## Overview

[[[PROSE overview unit=unit-test/StringSetTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::StringSetTest`](#gplatesunitteststringsettest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::StringSetTestSuite`](#gplatesunitteststringsettestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::StringSetTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StringSetTest()` | constructor | `None` | public | — |
| `equality_test()` | method | `void` | public | — |

### `GPlatesUnitTest::StringSetTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StringSetTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_STRINGSET_TEST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/StringSetTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/UtilsTestSuite](UtilsTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/StringSetTest.h
python scripts/gpq.py def GPlatesUnitTest::StringSetTestSuite --body
python scripts/gpq.py uses StringSetTestSuite --kind class
python scripts/gpq.py hier StringSetTestSuite
```
