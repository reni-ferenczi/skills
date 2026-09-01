# CoReg

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 224 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/CoReg.cc` | C++ | 578 |

## Overview

[[[PROSE overview unit=api/CoReg tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::CoRegistration`](#anonymouscoregistration) | class | — | — | 0 | — |

## Members

### `(anonymous)::CoRegistration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CoRegistration()` | constructor | `None` | public | — |
| `~CoRegistration()` | destructor | `None` | public | — |
| `exec(const char* cfg_file)` | method | `bool` | public | — |
| `exec()` | method | `bool` | public | — |
| `exec(double time)` | method | `bool` | public | — |
| `clear()` | method | `void` | public | — |
| `set_start_time(double t)` | method | `void` | public | — |
| `set_end_time(double t)` | method | `void` | public | — |
| `set_inc_time(double t)` | method | `void` | public | — |
| `load_recon_files(list& fl)` | method | `void` | public | — |
| `load_seed_files(list& fl)` | method | `void` | public | — |
| `load_coreg_files(list& fl)` | method | `void` | public | — |
| `load_cfg_file(const char* cfg_file)` | method | `void` | public | — |
| `add_cfg_row(const char* line)` | method | `void` | public | — |
| `clear_cfg_rows()` | method | `void` | public | — |
| `set_output_path(const char* path)` | method | `void` | public | — |
| `set_output_prefix(const char* prefix)` | method | `void` | public | — |
| `export_data()` | method | `void` | public | — |
| `print()` | method | `void` | public | — |
| `feature_ids(boost::python::object file)` | method | `boost::python::list` | public | — |
| `roi_filter( boost::python::object time, boost::python::object range, boost::python::object seed_id)` | method | `boost::python::list` | public | — |
| `get_result_data_from_layer()` | method | `list` | public | — |
| `get_data_header()` | method | `list` | public | — |
| `get_seed_rfg( const QString& id, std::vector<ReconstructedFeatureGeometry::non_null_ptr_type>& rfgs)` | method | `std::vector<const ReconstructedFeatureGeometry*>` | protected | — |
| `gen_data(double time)` | method | `void` | protected | — |
| `load_cfg_file()` | method | `void` | protected | — |
| `populate_cfg_table( CoRegConfigurationTable& table, const QString& filename)` | method | `void` | protected | — |
| `parse_cfg_row(const QString& line)` | method | `ConfigurationTableRow` | protected | — |
| `d_rotation_files` | field | `std::vector<File::non_null_ptr_type>` | private | — |
| `d_seed_files` | field | `std::vector<File::non_null_ptr_type>` | private | — |
| `d_coreg_files` | field | `std::vector<File::non_null_ptr_type>` | private | — |
| `d_rotation_fc` | field | `std::vector<FeatureCollectionHandle::weak_ref>` | private | — |
| `d_seed_fc` | field | `std::vector<FeatureCollectionHandle::weak_ref>` | private | — |
| `d_coreg_fc` | field | `std::vector<FeatureCollectionHandle::weak_ref>` | private | — |
| `d_output_prefix` | field | `QString` | private | — |
| `d_output_path` | field | `QString` | private | — |
| `d_cfg_file` | field | `QString` | private | — |
| `d_s_time` | field | `double` | private | — |
| `d_e_time` | field | `double` | private | — |
| `d_inc_time` | field | `double` | private | — |
| `d_cfg_table` | field | `CoRegConfigurationTable` | private | — |
| `d_result_table` | field | `std::vector<DataTable>` | private | — |
| `d_registry` | field | `FeatureCollectionFileFormat::Registry` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `export_co_registration()` | function | `void` | — |

## Notes

[[[PROSE notes unit=api/CoReg tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/NetCDFReader](../file-io/deprecated/NetCDFReader.md) | file-io | 1 |

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `CoRegistration` | class | — | `CoRegistration` |
| `run` | method | `CoRegistration` | `exec` |
| `run` | method | `CoRegistration` | `exec_file` |
| `run` | method | `CoRegistration` | `exec_time` |
| `clear` | method | `CoRegistration` | `&CoRegistration::clear` |
| `load_coreg_files` | method | `CoRegistration` | `&CoRegistration::load_coreg_files` |
| `load_recon_files` | method | `CoRegistration` | `&CoRegistration::load_recon_files` |
| `load_seed_files` | method | `CoRegistration` | `&CoRegistration::load_seed_files` |
| `load_cfg_file` | method | `CoRegistration` | `load_cfg_file` |
| `set_start_time` | method | `CoRegistration` | `&CoRegistration::set_start_time` |
| `set_end_time` | method | `CoRegistration` | `&CoRegistration::set_end_time` |
| `set_inc_time` | method | `CoRegistration` | `&CoRegistration::set_inc_time` |
| `set_output_path` | method | `CoRegistration` | `&CoRegistration::set_output_path` |
| `set_output_prefix` | method | `CoRegistration` | `&CoRegistration::set_output_prefix` |
| `add_cfg_row` | method | `CoRegistration` | `&CoRegistration::add_cfg_row` |

*... and 7 more bindings.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/CoReg.cc
python scripts/gpq.py def (anonymous)::CoRegistration --body
python scripts/gpq.py uses CoRegistration --kind class
python scripts/gpq.py hier CoRegistration
```
