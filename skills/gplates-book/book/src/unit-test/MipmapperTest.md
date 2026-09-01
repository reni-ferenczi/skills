# MipmapperTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 690 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/MipmapperTest.h` | C++ | 78 |
| `src/unit-test/MipmapperTest.cc` | C++ | 307 |

## Overview

Tests the mipmapping functionality in `GPlatesGui::Mipmapper`, which generates downsampled image pyramids from raster data. `MipmapperTest` contains seven test methods that verify raster extension and downsampling behavior across different data types: extending rasters to even dimensions (tests 1-4), and validating mipmap generation for RGBA, floating-point, and integer rasters. `MipmapperTestSuite` wraps these tests in the hierarchical test framework, instantiating `MipmapperTest` and registering its test cases via the `ADD_TESTCASE` macro.

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

*None.*

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
