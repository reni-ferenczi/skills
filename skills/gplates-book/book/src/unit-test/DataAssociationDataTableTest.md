# DataAssociationDataTableTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 389 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/DataAssociationDataTableTest.h` | C++ | 73 |
| `src/unit-test/DataAssociationDataTableTest.cc` | C++ | 108 |

## Overview

[[[PROSE overview unit=unit-test/DataAssociationDataTableTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=unit-test/DataAssociationDataTableTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
