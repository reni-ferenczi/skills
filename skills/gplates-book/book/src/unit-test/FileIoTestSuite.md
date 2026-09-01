# FileIoTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/FileIoTestSuite.h` | C++ | 46 |
| `src/unit-test/FileIoTestSuite.cc` | C++ | 45 |

## Overview

A container for Boost.Test cases exercising file I/O operations. The test suite inherits from `GPlatesTestSuite`, which manages the registration and collection of individual test cases via `construct_maps()`. Individual tests are added by concrete subclasses or via the `ADD_TESTCASE` macro to exercise readers and writers in the `file-io` module.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::FileIoTestSuite`](#gplatesunittestfileiotestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::FileIoTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FileIoTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_FILE_IO_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/FileIoTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::FileIoTestSuite --body
python scripts/gpq.py uses FileIoTestSuite --kind class
python scripts/gpq.py hier FileIoTestSuite
```
