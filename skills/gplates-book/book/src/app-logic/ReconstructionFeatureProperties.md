# ReconstructionFeatureProperties

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 807 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionFeatureProperties.h` | C++ | 228 |
| `src/app-logic/ReconstructionFeatureProperties.cc` | C++ | 171 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionFeatureProperties tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionFeatureProperties`](#gplatesapplogicreconstructionfeatureproperties) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | A visitor that retrieves commonly used reconstruction parameters from a feature's property values. |

## Members

### `GPlatesAppLogic::ReconstructionFeatureProperties`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TimePeriod` | struct | `None` | public | A valid time period. |
| `is_feature_defined_at_recon_time( const double &reconstruction_time)` | method | `bool` | public | Returns true unless a "gml:validTime" property in the feature has a time period that does not include the specified time. |
| `visit_gml_time_instant( const GPlatesPropertyValues::GmlTimeInstant &gml_time_instant)` | method | `void` | public | — |
| `visit_gml_time_period( const GPlatesPropertyValues::GmlTimePeriod &gml_time_period)` | method | `void` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_plate_id( const GPlatesPropertyValues::GpmlPlateId &gpml_plate_id)` | method | `void` | public | — |
| `visit_xs_double( const GPlatesPropertyValues::XsDouble &xs_double)` | method | `void` | public | — |
| `visit_enumeration( const enumeration_type &enumeration)` | method | `void` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | protected | — |
| `d_recon_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_valid_time` | field | `TimePeriod` | private | — |
| `d_recon_method` | field | `boost::optional<GPlatesPropertyValues::EnumerationContent>` | private | — |
| `d_right_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_left_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_spreading_asymmetry` | field | `boost::optional<double>` | private | — |
| `d_geometry_import_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONFEATUREPROPERTIES_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructionFeatureProperties tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 34 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 14 |
| [app-logic/RotationUtils](RotationUtils.md) | app-logic | 8 |
| [app-logic/ReconstructMethodHalfStageRotation](ReconstructMethodHalfStageRotation.md) | app-logic | 7 |
| [app-logic/ResolvedVertexSourceInfo](ResolvedVertexSourceInfo.md) | app-logic | 7 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 7 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 5 |
| [app-logic/ReconstructMethodVirtualGeomagneticPole](ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 4 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 3 |
| [app-logic/ReconstructMethodInterface](ReconstructMethodInterface.md) | app-logic | 3 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 3 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 3 |
| [app-logic/ReconstructMethodMotionPath](ReconstructMethodMotionPath.md) | app-logic | 2 |
| [app-logic/ReconstructMethodSmallCircle](ReconstructMethodSmallCircle.md) | app-logic | 2 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 2 |
| [app-logic/MotionPathGeometryPopulator](MotionPathGeometryPopulator.md) | app-logic | 1 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 1 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 1 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 1 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionFeatureProperties.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionFeatureProperties --body
python scripts/gpq.py uses ReconstructionFeatureProperties --kind class
python scripts/gpq.py hier ReconstructionFeatureProperties
```
