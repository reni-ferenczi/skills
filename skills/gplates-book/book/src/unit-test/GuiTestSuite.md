# GuiTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 690 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/GuiTestSuite.h` | C++ | 46 |
| `src/unit-test/GuiTestSuite.cc` | C++ | 49 |

## Overview

A container for GUI-related test suites. It inherits from `GPlatesTestSuite` and registers two sub-suites via `construct_maps()`: the `Mipmapper` suite and the `CptPalette` suite. Tests in these sub-suites exercise components from the `gui` module such as mipmapping for rendering efficiency and colour palette handling.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::GuiTestSuite`](#gplatesunittestguitestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::GuiTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GuiTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_GUI_TEST_SUITE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/MainTestSuite](MainTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/GuiTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::GuiTestSuite --body
python scripts/gpq.py uses GuiTestSuite --kind class
python scripts/gpq.py hier GuiTestSuite
```
