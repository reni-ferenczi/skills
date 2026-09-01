# VgpPartitionFeatureTask

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1746 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/VgpPartitionFeatureTask.h` | C++ | 71 |
| `src/app-logic/VgpPartitionFeatureTask.cc` | C++ | 132 |

## Overview

Assigns properties to VirtualGeomagneticPole features by partitioning them. When partitioning a VGP, the task locates the VGP's average sample site point within the partitioning polygons and assigns the reconstruction plate ID of the containing polygon to the feature.

VGP data represents present-day measurements regardless of sample age; the sample site location is not reconstructed at the requested time. Partitioning thus requires present-day polygon boundaries and the feature time period is ignored.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::VgpPartitionFeatureTask`](#gplatesapplogicvgppartitionfeaturetask) | class | [`PartitionFeatureTask`](PartitionFeatureTask.md) | — | 0 | Task for assigning properties to VirtualGeomagneticPole features. |

## Members

### `GPlatesAppLogic::VgpPartitionFeatureTask`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VgpPartitionFeatureTask( bool verify_information_model)` | constructor | `None` | public | If 'verify\_information\_model' is true then feature property types are only added if they don't not violate the GPGIM. |
| `can_partition_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | method | `bool` | public | — |
| `partition_feature( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, const GeometryCookieCutter &geometry_cookie_cutter, const ReconstructMethodInterface::Context &reconstruct_method_context, const double &reconstruction_time, bool r ...` | method | `void` | public | — |
| `d_verify_information_model` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_VGPPARTITIONFEATURETASK_H` | macro | `None` | — |

## Notes

VGP paleomagnetic data is always present-day, not reconstructed, despite the sample having an age. Partitioning uses only the present-day sample site location and requires present-day partitioning polygon boundaries. The `respect_feature_time_period` parameter is ignored.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/PartitionFeatureTask](PartitionFeatureTask.md) | app-logic | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/VgpPartitionFeatureTask.h
python scripts/gpq.py def GPlatesAppLogic::VgpPartitionFeatureTask --body
python scripts/gpq.py uses VgpPartitionFeatureTask --kind class
python scripts/gpq.py hier VgpPartitionFeatureTask
```
