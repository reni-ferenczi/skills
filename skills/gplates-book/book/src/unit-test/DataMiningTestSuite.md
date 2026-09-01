# DataMiningTestSuite

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 76 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/DataMiningTestSuite.h` | C++ | 47 |
| `src/unit-test/DataMiningTestSuite.cc` | C++ | 55 |

## Overview

Aggregate test suite for the data-mining subsystem. Combines tests for co-registration (`CoregTest`), data table operations (`DataAssociationDataTableTest`), multi-threaded data processing (`MultiThreadTest`), and filtering (`FilterTest`). Provides a single entry point for validating all data-mining functionality.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::DataMiningTestSuite`](#gplatesunittestdataminingtestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::DataMiningTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DataMiningTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_DATA_MINING_TEST_SUITE_H` | macro | `None` | — |

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
python scripts/gpq.py file src/unit-test/DataMiningTestSuite.h
python scripts/gpq.py def GPlatesUnitTest::DataMiningTestSuite --body
python scripts/gpq.py uses DataMiningTestSuite --kind class
python scripts/gpq.py hier DataMiningTestSuite
```
