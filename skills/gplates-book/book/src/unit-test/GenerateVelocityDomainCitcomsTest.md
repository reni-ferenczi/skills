# GenerateVelocityDomainCitcomsTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 624 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/GenerateVelocityDomainCitcomsTest.h` | C++ | 96 |
| `src/unit-test/GenerateVelocityDomainCitcomsTest.cc` | C++ | 249 |

## Overview

[[[PROSE overview unit=unit-test/GenerateVelocityDomainCitcomsTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::GenerateVelocityDomainCitcomsTest`](#gplatesunittestgeneratevelocitydomaincitcomstest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::GenerateVelocityDomainCitcomsTestSuite`](#gplatesunittestgeneratevelocitydomaincitcomstestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::GenerateVelocityDomainCitcomsTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenerateVelocityDomainCitcomsTest()` | constructor | `None` | public | — |
| `test_case_1()` | method | `void` | public | — |
| `test_case_2()` | method | `void` | public | — |
| `test_case_3()` | method | `void` | public | — |
| `test_case_4()` | method | `void` | public | — |
| `test_case_5()` | method | `void` | public | — |
| `test_case_6()` | method | `void` | public | — |
| `test_case_7()` | method | `void` | public | — |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_file_format_registry` | field | `GPlatesFileIO::FeatureCollectionFileFormat::Registry` | private | — |
| `d_files` | field | `std::vector<GPlatesFileIO::File::non_null_ptr_type>` | private | — |
| `check(int)` | method | `bool` | private | — |
| `load_mesh_files( int res_str)` | method | `std::vector<GPlatesModel::FeatureCollectionHandle::const_weak_ref>` | private | — |

### `GPlatesUnitTest::GenerateVelocityDomainCitcomsTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenerateVelocityDomainCitcomsTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UNIT_TEST_GENERATE_VELOCITY_DOMAIN_CITCOMS_TEST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/GenerateVelocityDomainCitcomsTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/AppLogicTestSuite](AppLogicTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/GenerateVelocityDomainCitcomsTest.h
python scripts/gpq.py def GPlatesUnitTest::GenerateVelocityDomainCitcomsTest --body
python scripts/gpq.py uses GenerateVelocityDomainCitcomsTest --kind class
python scripts/gpq.py hier GenerateVelocityDomainCitcomsTest
```
