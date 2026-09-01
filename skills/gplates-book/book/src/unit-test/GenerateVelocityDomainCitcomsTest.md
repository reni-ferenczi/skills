# GenerateVelocityDomainCitcomsTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 624 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/GenerateVelocityDomainCitcomsTest.h` | C++ | 96 |
| `src/unit-test/GenerateVelocityDomainCitcomsTest.cc` | C++ | 249 |

## Overview

Tests for velocity domain generation from CitCOMS (Citcom-S) geodynamic models. The test class loads mesh files from the unit-test-data directory and exercises the `GenerateVelocityDomainCitcoms` functionality in `app-logic`. It maintains a `ModelInterface`, a file format registry, and utilities to load and check mesh files at various resolutions.

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

*None.*

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
