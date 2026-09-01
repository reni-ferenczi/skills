# MultiThreadTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 1506 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/MultiThreadTest.h` | C++ | 79 |
| `src/unit-test/MultiThreadTest.cc` | C++ | 171 |

## Overview

A test framework for multi-threading and performance profiling. `MultiThreadTest` provides seven test methods that are designed to measure and verify concurrent operations—atomic counters, mutex-based synchronization, and profiling—though most test cases are disabled via preprocessor guards. `MultiThreadTestSuite` wraps these tests in the hierarchical framework, instantiating `MultiThreadTest` and registering its test cases. The tests exist as a foundation for future multi-threaded performance analysis using Boost threading primitives and profiling instrumentation.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::MultiThreadTest`](#gplatesunittestmultithreadtest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::MultiThreadTestSuite`](#gplatesunittestmultithreadtestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::MultiThreadTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MultiThreadTest()` | constructor | `None` | public | — |
| `test_case_1()` | method | `void` | public | — |
| `test_case_2()` | method | `void` | public | — |
| `test_case_3()` | method | `void` | public | — |
| `test_case_4()` | method | `void` | public | — |
| `test_case_5()` | method | `void` | public | — |
| `test_case_6()` | method | `void` | public | — |
| `test_case_7()` | method | `void` | public | — |

### `GPlatesUnitTest::MultiThreadTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MultiThreadTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_MULTITHREAD_TEST_H` | macro | `None` | — |

## Notes

Most test cases are disabled by `#if 0` preprocessor guards; they are currently placeholders for performance profiling experiments. When enabled, they exercise atomic counters, mutexes, and other synchronization primitives from Boost.

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/DataMiningTestSuite](DataMiningTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/MultiThreadTest.h
python scripts/gpq.py def GPlatesUnitTest::MultiThreadTest --body
python scripts/gpq.py uses MultiThreadTest --kind class
python scripts/gpq.py hier MultiThreadTest
```
