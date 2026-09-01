# DataAssociationDataTableTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 389 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/DataAssociationDataTableTest.h` | C++ | 73 |
| `src/unit-test/DataAssociationDataTableTest.cc` | C++ | 108 |

## Overview

Unit test for `GPlatesDataMining::DataTable`, a generic container for heterogeneous data rows used in data-mining operations. Tests create a `DataTable`, append `DataRow` objects containing cells of mixed types (integers, strings, booleans via `OpaqueData` variant), and verify that data is correctly stored and retrieved. Validates the core data table abstraction used by association and querying operations.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::DataAssociationDataTableTest`](#gplatesunittestdataassociationdatatabletest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::DataAssociationDataTableTestSuite`](#gplatesunittestdataassociationdatatabletestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::DataAssociationDataTableTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DataAssociationDataTableTest()` | constructor | `None` | public | — |
| `~DataAssociationDataTableTest()` | destructor | `None` | public | — |
| `test_data_table()` | method | `void` | public | — |
| `d_data_table` | field | `GPlatesDataMining::DataTable` | private | — |

### `GPlatesUnitTest::DataAssociationDataTableTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DataAssociationDataTableTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_DA_DATATABLE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/AppLogicTestSuite](AppLogicTestSuite.md) | unit-test | 1 |
| [unit-test/DataMiningTestSuite](DataMiningTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/DataAssociationDataTableTest.h
python scripts/gpq.py def GPlatesUnitTest::DataAssociationDataTableTest --body
python scripts/gpq.py uses DataAssociationDataTableTest --kind class
python scripts/gpq.py hier DataAssociationDataTableTest
```
