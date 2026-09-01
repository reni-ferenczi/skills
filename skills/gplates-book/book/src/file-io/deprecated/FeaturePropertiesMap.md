# FeaturePropertiesMap

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 45 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/FeaturePropertiesMap.h` | C++ | 87 |
| `src/file-io/deprecated/FeaturePropertiesMap.cc` | C++ | 1416 |

## Overview

[[[PROSE overview unit=file-io/deprecated/FeaturePropertiesMap tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::FeaturePropertiesMap`](#gplatesfileiofeaturepropertiesmap) | class | [`GPlatesUtils::Singleton<FeaturePropertiesMap>`](../../utils/Singleton.md) | — | 0 | This class encapsulates a mapping from a (fully qualified) feature type name to a mapping from the properties allowed in the feature to creation functions for the properties. feature type name -----\> ( property p -----\> creation\_function ... |

## Members

### `GPlatesFileIO::FeaturePropertiesMap`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `feature_properties_map_type` | typedef | `std::map< GPlatesModel::FeatureType, GpmlPropertyReaderUtils::PropertyCreatorMap>` | private | — |
| `const_iterator` | typedef | `feature_properties_map_type::const_iterator` | public | — |
| `find( const GPlatesModel::FeatureType &key)` | method | `const_iterator` | public | — |
| `begin()` | method | `const_iterator` | public | — |
| `end()` | method | `const_iterator` | public | — |
| `is_valid_property( const GPlatesModel::FeatureType &feature_type, const GPlatesModel::PropertyName &property_name)` | method | `bool` | public | Returns whether property\_name is a valid property of feature\_type. |
| `d_map` | field | `feature_properties_map_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GET_PROP_VAL_NAME` | macro_function | `GPlatesFileIO::GpmlPropertyReaderUtils::create_prop##_as_prop_val` | — |
| `get_gml_abstract_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_abstract_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_time_variant_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_reconstructable_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_tangible_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_abstract_geological_plane_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_abstract_geological_contact_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_geological_plane_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_fold_plane_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_fault_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_terrane_boundary_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_unconformity_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_unknown_contact_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_isochron_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_magnetic_anomaly_identification_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_magnetic_anomaly_ship_track_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_fracture_zone_identification_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_suture_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_psuedo_fault_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_island_arc_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_hot_spot_trail_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_hot_spot_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_seamount_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_slab_edge_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_volcano_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_navdat_sample_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_pluton_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_ophiolite_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_aseismic_ridge_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_coastline_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_craton_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_large_igneous_province_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_basin_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_extended_continental_crust_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_transitional_crust_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_continental_fragment_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_geological_lineation_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_pseudo_fault_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_virtual_geomagnetic_pole_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_unclassified_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_mesh_node_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_abstract_field_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_tectonic_section_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_mid_ocean_ridge_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_subduction_zone_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_orogenic_belt_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_transform_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_passive_continental_boundary_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_instantaneous_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_abstract_rock_unit_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_basic_rock_unit_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_artificial_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_closed_plate_boundary_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_closed_continental_boundary_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_inferred_paleo_boundary_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_political_boundary_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_old_plates_grid_mark_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_topological_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_topological_closed_plate_boundary_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_topological_slab_boundary_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_topological_network_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_unclassified_topological_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_reconstruction_feature_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_total_reconstruction_sequence_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_absolute_reference_frame_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_raster_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_scalar_field_3d_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_flowline_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_motion_path_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_small_circle_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_polygon_centroid_point_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `get_displacement_point_properties()` | function | `GpmlPropertyReaderUtils::PropertyCreatorMap` | — |
| `GPLATES_FILEIO_FEATUREPROPERTIESMAP_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/deprecated/FeaturePropertiesMap tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/deprecated/FeaturePropertiesMap.h
python scripts/gpq.py def GPlatesFileIO::FeaturePropertiesMap --body
python scripts/gpq.py uses FeaturePropertiesMap --kind class
python scripts/gpq.py hier FeaturePropertiesMap
```
