# FeatureHandleTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1017 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/FeatureHandleTest.h` | C++ | 82 |
| `src/unit-test/FeatureHandleTest.cc` | C++ | 342 |

## Overview

[[[PROSE overview unit=unit-test/FeatureHandleTest tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`MyPoolTag`](#mypooltag) | struct | — | — | 0 | — |
| [`TestStruct`](#teststruct) | struct | — | — | 0 | — |
| [`my_pool`](#my_pool) | typedef | — | — | 0 | — |
| [`GPlatesUnitTest::FeatureHandleTest`](#gplatesunittestfeaturehandletest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::FeatureHandleTestSuite`](#gplatesunittestfeaturehandletestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `MyPoolTag`

*None.*

### `TestStruct`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `i` | field | `int` | public | — |
| `j` | field | `long int` | public | — |
| `n` | field | `long` | public | — |
| `d` | field | `double` | public | — |

### `my_pool`

*None.*

### `GPlatesUnitTest::FeatureHandleTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureHandleTest()` | constructor | `None` | public | — |
| `test_case_1()` | method | `void` | public | — |
| `test_case_2()` | method | `void` | public | — |
| `test_case_3()` | method | `void` | public | — |
| `test_case_4()` | method | `void` | public | — |
| `test_case_5()` | method | `void` | public | — |
| `test_case_6()` | method | `void` | public | — |
| `test_case_7()` | method | `void` | public | — |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |

### `GPlatesUnitTest::FeatureHandleTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureHandleTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_memory_usage()` | function | `void` | — |
| `operator new(size_t size, bool flag)` | operator | `void` | — |
| `operator delete(void*p, bool flag)` | operator | `void` | — |
| `new` | macro | `new(true)` | — |
| `GPLATES_UNIT_TEST_FEATUREHANDLE_TEST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/FeatureHandleTest tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | opengl | 6 |
| [opengl/GLMatrix](../opengl/GLMatrix.md) | opengl | 4 |
| [unit-test/ModelTestSuite](ModelTestSuite.md) | unit-test | 4 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 3 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 3 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 3 |
| [scribe/Scribe](../scribe/Scribe.md) | scribe | 2 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 1 |
| [qt-widgets/SaveFileDialog](../qt-widgets/SaveFileDialog.md) | qt-widgets | 1 |
| [scribe/ScribeAccess](../scribe/ScribeAccess.md) | scribe | 1 |
| [scribe/ScribeConstructObject](../scribe/ScribeConstructObject.md) | scribe | 1 |
| [scribe/ScribeSaveLoadConstructObject](../scribe/ScribeSaveLoadConstructObject.md) | scribe | 1 |
| [utils/Profile](../utils/Profile.md) | utils | 1 |
| [utils/UnicodeString](../utils/UnicodeString.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/FeatureHandleTest.h
python scripts/gpq.py def GPlatesUnitTest::FeatureHandleTest --body
python scripts/gpq.py uses FeatureHandleTest --kind class
python scripts/gpq.py hier FeatureHandleTest
```
