# GlobalTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/GlobalTestSuite.h` | C++ | 46 |
| `src/unit-test/GlobalTestSuite.cc` | C++ | 46 |

## Overview

A container for global-scope test cases. The suite inherits from `GPlatesTestSuite` and manages the registration of individual tests via `construct_maps()`. Tests registered here exercise cross-cutting concerns or global functionality that does not fit into other module-specific test suites.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::GlobalTestSuite`](#gplatesunittestglobaltestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::GlobalTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GlobalTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_GLOBAL_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/GlobalTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::GlobalTestSuite --body
python scripts/gpq.py uses GlobalTestSuite --kind class
python scripts/gpq.py hier GlobalTestSuite
```
