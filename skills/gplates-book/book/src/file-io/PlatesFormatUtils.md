# PlatesFormatUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 116 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PlatesFormatUtils.h` | C++ | 58 |
| `src/file-io/PlatesFormatUtils.cc` | C++ | 640 |

## Overview

Maps GPlates geological feature types to PLATES4 format header data type codes. The module implements `get_plates_data_type_code()` which dispatches to feature-type-specific getter functions that return two-letter codes (e.g., "BA" for bathymetry, "AR" for aseismic ridge). Handles special cases like features with an `isActive` property, returning active or inactive variants of the code.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::plates_data_type_code_map_type`](#anonymousplates_data_type_code_map_type) | typedef | — | — | 0 | Maps feature type to plates header data type code. |

## Members

### `(anonymous)::plates_data_type_code_map_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_data_type_code_for_active_inactive_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature, const GPlatesUtils::UnicodeString &active_data_type_code, const GPlatesUtils::UnicodeString &inactive_data_type_code)` | function | `GPlatesUtils::UnicodeString` | If specified feature has "isActive" boolean property then return active data type code if its value is true otherwise return inactive data type code. |
| `get_data_type_code_for_aseismic_ridge( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_bathymetry( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_basin( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_continental_boundary( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_continental_fragment( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_craton( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_coastline( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_extended_continental_crust( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_fault( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_fracture_zone( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_grid_mark( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_gravimetry( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_heat_flow( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_hot_spot( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_hot_spot_trail( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_island_arc( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_isochron( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_isopach( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_unclassified_feature( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | -might- be Ice Shelf, might be Isochron. |
| `get_data_type_code_for_geological_lineation( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_magnetics( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_orogenic_belt( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_ophiolite_belt( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_inferred_paleo_boundary( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_magnetic_pick( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_ridge_segment( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_seamount( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_slab( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_suture( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_terrane_boundary( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_transitional_crust( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_transform( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_topography( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_subduction_zone( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_volcano( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_pluton( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_ophiolite( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_political_boundary( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_large_igneous_province( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_navdat_1( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_navdat_2( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_navdat_3( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `get_data_type_code_for_navdat_4( const GPlatesModel::FeatureHandle::const_weak_ref &)` | function | `GPlatesUtils::UnicodeString` | — |
| `GPLATES_FILE_IO_PLATESFORMATUTILS_H` | macro | `None` | — |
| `INVALID_DATA_TYPE_CODE` | variable | `GPlatesUtils::UnicodeString` | Used in the data type code field of PLATES header to indicate an unknown or invalid type. |
| `get_plates_data_type_code( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `GPlatesUtils::UnicodeString` | Determines the PLATES4 header data type code from the specified feature. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesLineFormatHeaderVisitor](PlatesLineFormatHeaderVisitor.md) | file-io | 13 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/PlatesFormatUtils.h
python scripts/gpq.py def (anonymous)::plates_data_type_code_map_type --body
python scripts/gpq.py uses plates_data_type_code_map_type --kind typedef
```
