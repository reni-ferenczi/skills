# CoregTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 226 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/CoregTest.h` | C++ | 151 |
| `src/unit-test/CoregTest.cc` | C++ | 467 |

## Overview

Unit tests for co-registration (CoReg) functionality in the data-mining subsystem. Tests load feature collections from configuration files, manipulate rotation and seed data, and validate results at various time periods. The test suite verifies `CoRegConfigurationTable` population, data loading, and the core co-registration algorithm through seven test cases. Implementation is incomplete—marked as TODO pending a lower-level Python API.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::CoregTest`](#gplatesunittestcoregtest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::CoregTestSuite`](#gplatesunittestcoregtestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `GPlatesUnitTest::CoregTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CoregTest()` | constructor | `None` | public | — |
| `test_case_1()` | method | `void` | public | — |
| `test_case_2()` | method | `void` | public | — |
| `test_case_3()` | method | `void` | public | — |
| `test_case_4()` | method | `void` | public | — |
| `test_case_5()` | method | `void` | public | — |
| `test_case_6()` | method | `void` | public | — |
| `test_case_7()` | method | `void` | public | — |
| `load_test_data()` | method | `void` | private | Load test data files. |
| `load_cfg( const QString& cfg_file, const QString& section_name)` | method | `std::vector<QString>` | private | Return particular section of configuration file. |
| `load_one_line_cfg( const QString& cfg_file, const QString& section_name)` | method | `QString` | private | — |
| `test(double time)` | method | `void` | private | Run the test at certain time. |
| `check_result(double time)` | method | `bool` | private | Check the result at certain time. |
| `populate_cfg_table( GPlatesDataMining::CoRegConfigurationTable& table, const QString& filename)` | method | `void` | private | Populate CoRegConfigurationTable from configuration file. |
| `get_output_name(double time)` | method | `QString` | private | — |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |
| `d_file_format_registry` | field | `GPlatesFileIO::FeatureCollectionFileFormat::Registry` | private | — |
| `d_loaded_files` | field | `std::vector<GPlatesFileIO::File::non_null_ptr_type>` | private | — |
| `d_rotation_fc` | field | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | private | — |
| `d_seed_fc` | field | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | private | — |
| `d_coreg_fc` | field | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | private | — |
| `d_output_prefix` | field | `QString` | private | — |
| `d_output_path` | field | `QString` | private | — |

### `GPlatesUnitTest::CoregTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CoregTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `unit_test_data_path` | variable | `QString` | ./gplates-unit-test --detect\_memory\_leaks=0 --G\_test\_to\_run=\*/Coreg |
| `cfg_file` | variable | `QString` | — |
| `load_result_data( const QString& filename)` | function | `std::map<QString, QStringList>` | — |
| `GPLATES_UNIT_TEST_COREG_TEST_H` | macro | `None` | — |

## Notes

Test methods `test_case_1()` through `test_case_7()` are placeholders—the actual test implementation is incomplete and logs a warning stating "not implemented". The test cases are intended to be re-implemented using a lower-level Python API approach.

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/DataMiningTestSuite](DataMiningTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/CoregTest.h
python scripts/gpq.py def GPlatesUnitTest::CoregTest --body
python scripts/gpq.py uses CoregTest --kind class
python scripts/gpq.py hier CoregTest
```
