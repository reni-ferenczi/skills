# StringSetTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/StringSetTest.h` | C++ | 63 |
| `src/unit-test/StringSetTest.cc` | C++ | 71 |

## Overview

Test suite for `GPlatesUtils::StringSet`, a string interning data structure that maintains a single instance of each unique string. The tests verify that identical strings inserted into the set return equal iterators, and that the structure correctly identifies equal feature types created with different string types.

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

*None.*

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
