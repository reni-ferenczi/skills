# PaleomagUtils

[Book TOC](../../../TOC.md) · [app-logic](../../../components/app-logic.md) · cluster Community 549 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/deprecated/PaleomagUtils.h` | C++ | 196 |
| `src/app-logic/deprecated/PaleomagUtils.cc` | C++ | 379 |

## Overview

Utility visitors for paleomagnetic data handling. `DetectPaleomagFeatures` traverses feature collections to determine whether they contain paleomagnetic features. `VgpRenderer` renders Virtual Geomagnetic Pole features by visiting and collecting properties such as site point, pole location, confidence parameters, plate ID, and age information, optionally applying an additional rotation before rendering to the target layer.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::PaleomagUtils::DetectPaleomagFeatures`](#gplatesapplogicpaleomagutilsdetectpaleomagfeatures) | class | [`GPlatesModel::ConstFeatureVisitor`](../../model/FeatureVisitor.md) | — | 0 | Determines if there are any paleomag features in the collection. |
| [`GPlatesAppLogic::PaleomagUtils::VgpRenderer`](#gplatesapplogicpaleomagutilsvgprenderer) | class | [`GPlatesModel::FeatureVisitor`](../../model/FeatureVisitor.md) | — | 0 | — |

## Members

### `GPlatesAppLogic::PaleomagUtils::DetectPaleomagFeatures`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DetectPaleomagFeatures()` | constructor | `None` | public | — |
| `has_paleomag_features()` | method | `bool` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `d_found_paleomag_features` | field | `bool` | private | — |

### `GPlatesAppLogic::PaleomagUtils::VgpRenderer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VgpRenderer( Reconstruction &reconstruction, boost::optional<GPlatesMaths::Rotation> &additional_rotation, GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type target_layer, const GPlatesGui::ColourProxy &colour, GPlatesPresentation::ViewState *view_state_, bool should_add_to_reconstruction = f ...` | constructor | `None` | public | — |
| `finalise_post_feature_properties( GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_plate_id( GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | public | — |
| `visit_gml_point( GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | public | — |
| `visit_gml_time_period( GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | public | — |
| `visit_xs_double( GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | public | — |
| `d_reconstruction` | field | `Reconstruction` | private | — |
| `d_additional_rotation` | field | `boost::optional<GPlatesMaths::Rotation>` | private | A rotation applied to the Vgp geometries before rendering. |
| `d_target_layer` | field | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_owner_ptr_type` | private | — |
| `d_colour` | field | `GPlatesGui::ColourProxy` | private | — |
| `d_view_state_ptr` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_should_add_to_reconstruction` | field | `bool` | private | Whether or not the reconstructed Vgp geometries should be added to the set of reconstruction geometries. |
| `d_site_point` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `d_site_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `d_vgp_point` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `d_vgp_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `d_a95` | field | `boost::optional<double>` | private | — |
| `d_dm` | field | `boost::optional<double>` | private | — |
| `d_dp` | field | `boost::optional<double>` | private | — |
| `d_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_begin_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_end_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |
| `d_age` | field | `boost::optional<double>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_PALEOMAGUTILS_H` | macro | `None` | — |
| `SITE_POINT_SIZE` | variable | `double` | — |
| `POLE_POINT_SIZE` | variable | `double` | — |
| `detect_paleomag_features( GPlatesModel::FeatureCollectionHandle::weak_ref feature_collection)` | function | `bool` | Returns true if there are any paleomag features in feature\_collection. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/deprecated/PaleomagWorkflow](PaleomagWorkflow.md) | app-logic | 9 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](ReconstructedFeatureGeometryPopulator.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/deprecated/PaleomagUtils.h
python scripts/gpq.py def GPlatesAppLogic::PaleomagUtils::VgpRenderer --body
python scripts/gpq.py uses VgpRenderer --kind class
python scripts/gpq.py hier VgpRenderer
```
