# PropertyValuesTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/PropertyValuesTestSuite.h` | C++ | 47 |
| `src/unit-test/PropertyValuesTestSuite.cc` | C++ | 46 |

## Overview

A test suite container for property-values tests. It inherits from `GPlatesTestSuite` but is currently empty, with no child test suites registered. This is a placeholder in the hierarchical test framework for tests of the GPML and GML property value types in the property-values module.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::PropertyValuesTestSuite`](#gplatesunittestpropertyvaluestestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::PropertyValuesTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PropertyValuesTestSuite(unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_PROPERTYVALUES_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/PropertyValuesTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::PropertyValuesTestSuite --body
python scripts/gpq.py uses PropertyValuesTestSuite --kind class
python scripts/gpq.py hier PropertyValuesTestSuite
```
