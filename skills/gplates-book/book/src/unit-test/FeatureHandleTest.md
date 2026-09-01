# FeatureHandleTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1017 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/FeatureHandleTest.h` | C++ | 82 |
| `src/unit-test/FeatureHandleTest.cc` | C++ | 342 |

## Overview

`FeatureHandleTest` is a Boost.Test fixture registered through `FeatureHandleTestSuite`, which builds on `GPlatesTestSuite` the same way every other suite in this directory does. In principle it exercises `GPlatesModel::FeatureHandle` construction and property assignment via the `d_model` member, but in practice almost none of that testing exists: `test_case_2` and `test_case_4` through `test_case_7` are empty stubs ("Add you test code here"), and `test_case_1` and `test_case_3` contain real code that is wrapped in `#if 0` and therefore never compiled into the running test.

The disabled bodies are a memory-efficiency experiment rather than a correctness test: they build features with a `GpmlKeyValueDictionary` of eighty attributes to see how much memory a populated `FeatureHandle` consumes, and separately benchmark `boost::singleton_pool` allocation against ordinary `malloc` for a fixed-size `TestStruct`. The free helpers at the top of the `.cc` — `MyPoolTag`, `TestStruct`, `my_pool`, the `operator new(size_t, bool)`/`operator delete(void*, bool)` overloads, and `print_memory_usage()` (Windows-only, via `GetProcessMemoryInfo`) — exist solely to support that disabled experiment.

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

`#define new new(true)` near the top of the `.cc` is unmatched by any `#undef`: every subsequent `new` expression in the rest of the file — not just the ones inside the disabled test bodies — is silently rewritten to call the custom `operator new(size_t, bool)`, which pool-allocates only when `size == sizeof(TestStruct)` and otherwise falls back to `malloc`. Because the code that actually exercises this is inside `#if 0`, the overload is currently dead weight, but it would surprise anyone who added a new, unrelated test case below this point in the file expecting ordinary `new` semantics.

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
