# PalaeomagUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 975 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/PalaeomagUtils.h` | C++ | 123 |
| `src/app-logic/PalaeomagUtils.cc` | C++ | 96 |

## Overview

[[[PROSE overview unit=app-logic/PalaeomagUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/PalaeomagUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
