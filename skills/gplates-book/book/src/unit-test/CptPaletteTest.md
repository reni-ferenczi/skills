# CptPaletteTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1398 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/CptPaletteTest.h` | C++ | 79 |
| `src/unit-test/CptPaletteTest.cc` | C++ | 145 |

## Overview

Unit tests for CPT (Cpt) color palette file parsing and color retrieval. Tests load `CptPalette` objects from CPT color palette files and verify that color lookups return correct values for various palette keys. Validates the `Palette` interface by exercising color interpolation and boundary conditions across seven test cases.

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

*None.*

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
