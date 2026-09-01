# PalaeomagUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 975 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/PalaeomagUtils.h` | C++ | 123 |
| `src/app-logic/PalaeomagUtils.cc` | C++ | 96 |

## Overview

`PalaeomagUtils` holds `VirtualGeomagneticPolePropertyFinder`, a `GPlatesModel::ConstFeatureVisitor` that pulls the properties needed to build a `ReconstructedVirtualGeomagneticPole` out of a `gpml:VirtualGeomagneticPole` feature. `initialise_pre_feature_properties` checks the feature's type and aborts the visit for anything else, so `is_vgp_feature` tells the caller whether the feature was even a VGP before trusting the rest of the results. The remaining visitor methods pick out the site position (`gml:averageSampleSitePosition`), the pole position (`gml:polePosition`), the plate id, and the average age by matching `current_top_level_propname()` against the known GPML property names, unwrapping `GpmlConstantValue` wrappers along the way.

The finder is a one-shot, stateless-per-visit accumulator: construct it, call `feature_handle.accept_visitor()` (or equivalent) once, then read the accumulated `boost::optional` fields.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::PalaeomagUtils::VirtualGeomagneticPolePropertyFinder`](#gplatesapplogicpalaeomagutilsvirtualgeomagneticpolepropertyfinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Obtains pmag related properties from a vgp feature. |

## Members

### `GPlatesAppLogic::PalaeomagUtils::VirtualGeomagneticPolePropertyFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VirtualGeomagneticPolePropertyFinder()` | constructor | `None` | public | — |
| `get_plate_id()` | method | `boost::optional<GPlatesModel::integer_plate_id_type>` | public | — |
| `get_age()` | method | `boost::optional<double>` | public | — |
| `is_vgp_feature()` | method | `bool` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | private | — |
| `visit_xs_double( const GPlatesPropertyValues:: XsDouble &xs_double)` | method | `void` | private | — |
| `d_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | May use this later to fill up the ReconVGPParams structure in the ReconstructedFeatureGeometryPopulator. |
| `d_site_point` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `d_vgp_point` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |
| `d_age` | field | `boost::optional<double>` | private | — |
| `d_is_vgp_feature` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_PALAEOMAGUTILS_H` | macro | `None` | — |

## Notes

- `get_plate_id`, `get_age`, `get_site_point` and `get_vgp_point` return whatever was found, even when `is_vgp_feature()` is false — callers must check `is_vgp_feature()` first, since a non-VGP feature simply short-circuits property collection rather than resetting these fields to a known "invalid" state.
- Matching is by top-level property name only; the visitor does not otherwise validate that a `GmlPoint` or `XsDouble` occurs where expected.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CalculateReconstructionPoleDialog](../qt-widgets/CalculateReconstructionPoleDialog.md) | qt-widgets | 7 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 6 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/PalaeomagUtils.h
python scripts/gpq.py def GPlatesAppLogic::PalaeomagUtils::VirtualGeomagneticPolePropertyFinder --body
python scripts/gpq.py uses VirtualGeomagneticPolePropertyFinder --kind class
python scripts/gpq.py hier VirtualGeomagneticPolePropertyFinder
```
