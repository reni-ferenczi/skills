# MipmapperTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 690 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/MipmapperTest.h` | C++ | 78 |
| `src/unit-test/MipmapperTest.cc` | C++ | 307 |

## Overview

[[[PROSE overview unit=unit-test/MipmapperTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::MipmapperTest`](#gplatesunittestmipmappertest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::MipmapperTestSuite`](#gplatesunittestmipmappertestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::MipmapperTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `test_extend_raster1()` | method | `void` | public | — |
| `test_extend_raster2()` | method | `void` | public | — |
| `test_extend_raster3()` | method | `void` | public | — |
| `test_extend_raster4()` | method | `void` | public | — |
| `test_rgba_mipmapper()` | method | `void` | public | — |
| `test_float_mipmapper()` | method | `void` | public | — |
| `test_int_mipmapper()` | method | `void` | public | — |

### `GPlatesUnitTest::MipmapperTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MipmapperTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_REAL_TEST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/MipmapperTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/GuiTestSuite](GuiTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/MipmapperTest.h
python scripts/gpq.py def GPlatesUnitTest::MipmapperTest --body
python scripts/gpq.py uses MipmapperTest --kind class
python scripts/gpq.py hier MipmapperTest
```
