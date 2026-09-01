# CptPaletteTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1398 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/CptPaletteTest.h` | C++ | 79 |
| `src/unit-test/CptPaletteTest.cc` | C++ | 145 |

## Overview

[[[PROSE overview unit=unit-test/CptPaletteTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::CptPaletteTest`](#gplatesunittestcptpalettetest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::CptPaletteTestSuite`](#gplatesunittestcptpalettetestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::CptPaletteTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CptPaletteTest()` | constructor | `None` | public | — |
| `test_case_1()` | method | `void` | public | — |
| `test_case_2()` | method | `void` | public | — |
| `test_case_3()` | method | `void` | public | — |
| `test_case_4()` | method | `void` | public | — |
| `test_case_5()` | method | `void` | public | — |
| `test_case_6()` | method | `void` | public | — |
| `test_case_7()` | method | `void` | public | — |

### `GPlatesUnitTest::CptPaletteTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CptPaletteTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_CPTPALETTE_TEST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/CptPaletteTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/GuiTestSuite](GuiTestSuite.md) | unit-test | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/CptPaletteTest.h
python scripts/gpq.py def GPlatesUnitTest::CptPaletteTest --body
python scripts/gpq.py uses CptPaletteTest --kind class
python scripts/gpq.py hier CptPaletteTest
```
