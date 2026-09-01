# ReconstructedVirtualGeomagneticPole

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 607 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructedVirtualGeomagneticPole.h` | C++ | 188 |
| `src/app-logic/ReconstructedVirtualGeomagneticPole.cc` | C++ | 54 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructedVirtualGeomagneticPole tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructedVirtualGeomagneticPoleParams`](#gplatesapplogicreconstructedvirtualgeomagneticpoleparams) | struct | — | — | 0 | — |
| [`GPlatesAppLogic::ReconstructedVirtualGeomagneticPole`](#gplatesapplogicreconstructedvirtualgeomagneticpole) | class | [`ReconstructedFeatureGeometry`](ReconstructedFeatureGeometry.md) | — | 0 | A reconstructed virtual geomagnetic pole minus the sample site geometry (which is a ReconstructedFeatureGeometry). |

## Members

### `GPlatesAppLogic::ReconstructedVirtualGeomagneticPoleParams`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `d_site_point` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | public | — |
| `d_site_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | public | — |
| `d_vgp_point` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | public | — |
| `d_vgp_iterator` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | public | — |
| `d_a95` | field | `boost::optional<double>` | public | — |
| `d_dm` | field | `boost::optional<double>` | public | — |
| `d_dp` | field | `boost::optional<double>` | public | — |
| `d_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | public | — |
| `d_begin_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | public | — |
| `d_end_time` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | public | — |
| `d_age` | field | `boost::optional<double>` | public | — |

### `GPlatesAppLogic::ReconstructedVirtualGeomagneticPole`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructedVirtualGeomagneticPole>` | public | A convenience typedef for a non-null shared pointer to a non-const ReconstructedVirtualGeomagneticPole. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructedVirtualGeomagneticPole>` | public | A convenience typedef for a non-null shared pointer to a const ReconstructedVirtualGeomagneticPole. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ReconstructedVirtualGeomagneticPole>` | public | A convenience typedef for boost::intrusive\_ptr\<ReconstructedVirtualGeomagneticPole\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ReconstructedVirtualGeomagneticPole>` | public | A convenience typedef for boost::intrusive\_ptr\<const ReconstructedVirtualGeomagneticPole\>. |
| `create( const ReconstructedVirtualGeomagneticPoleParams &params, const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree, const ReconstructionTreeCreator &reconstruction_tree_creator, const geometry_ptr_type &geometry_ptr, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::itera ...` | method | `non_null_ptr_type` | public | Create a ReconstructedVirtualGeomagneticPole instance with an optional reconstruction plate ID and an optional time of formation. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `ReconstructedVirtualGeomagneticPole( const ReconstructedVirtualGeomagneticPoleParams &params, const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator, const geometry_ptr_type &geometry_ptr, GPlatesModel::FeatureHandle &feature_handle, GPla ...` | constructor | `None` | private | Instantiate a reconstructed virtual geomagnetic pole with an optional reconstruction plate ID and an optional time of formation. |
| `d_VGP_params` | field | `ReconstructedVirtualGeomagneticPoleParams` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTEDVIRTUALGEOMAGNETICPOLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructedVirtualGeomagneticPole tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructMethodVirtualGeomagneticPole](ReconstructMethodVirtualGeomagneticPole.md) | app-logic | 15 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 15 |
| [app-logic/PalaeomagUtils](PalaeomagUtils.md) | app-logic | 2 |
| [app-logic/deprecated/ReconstructedFeatureGeometryPopulator](deprecated/ReconstructedFeatureGeometryPopulator.md) | app-logic | 2 |
| [model/WeakObserverVisitor](../model/WeakObserverVisitor.md) | model | 2 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryVisitor](ReconstructionGeometryVisitor.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructedVirtualGeomagneticPole.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructedVirtualGeomagneticPole --body
python scripts/gpq.py uses ReconstructedVirtualGeomagneticPole --kind class
python scripts/gpq.py hier ReconstructedVirtualGeomagneticPole
```
