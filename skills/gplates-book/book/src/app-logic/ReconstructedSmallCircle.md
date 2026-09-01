# ReconstructedSmallCircle

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 932 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructedSmallCircle.h` | C++ | 165 |
| `src/app-logic/ReconstructedSmallCircle.cc` | C++ | 50 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructedSmallCircle tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructedSmallCircle`](#gplatesapplogicreconstructedsmallcircle) | class | [`ReconstructedFeatureGeometry`](ReconstructedFeatureGeometry.md) | — | 0 | A reconstructed small circle. |

## Members

### `GPlatesAppLogic::ReconstructedSmallCircle`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructedSmallCircle>` | public | A convenience typedef for a non-null shared pointer to a non-const ReconstructedSmallCircle. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructedSmallCircle>` | public | A convenience typedef for a non-null shared pointer to a const ReconstructedSmallCircle. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ReconstructedSmallCircle>` | public | A convenience typedef for boost::intrusive\_ptr\<ReconstructedSmallCircle\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ReconstructedSmallCircle>` | public | A convenience typedef for boost::intrusive\_ptr\<const ReconstructedSmallCircle\>. |
| `small_circle_centre_type` | typedef | `GPlatesMaths::PointOnSphere` | public | A convenience typedef for a PointOnSphere type. |
| `create( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree, const ReconstructionTreeCreator &reconstruction_tree_creator, const small_circle_centre_type &centre_ptr, const double &radius, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_iterator, boost:: ...` | method | `non_null_ptr_type` | public | Create a ReconstructedSmallCircle instance with an optional reconstruction plate ID and an optional time of formation. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `radius()` | method | `double` | public | — |
| `ReconstructedSmallCircle( const ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_, const ReconstructionTreeCreator &reconstruction_tree_creator, const small_circle_centre_type &centre_, const double &radius_, GPlatesModel::FeatureHandle &feature_handle, GPlatesModel::FeatureHandle::iterator property_ ...` | constructor | `None` | private | Instantiate a reconstructed small circle. |
| `d_centre` | field | `small_circle_centre_type` | private | — |
| `d_radius` | field | `double` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTEDSMALLCIRCLE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructedSmallCircle tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/SmallCircleGeometryPopulator](SmallCircleGeometryPopulator.md) | app-logic | 7 |
| [model/WeakObserverVisitor](../model/WeakObserverVisitor.md) | model | 2 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 2 |
| [app-logic/ReconstructMethodSmallCircle](ReconstructMethodSmallCircle.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryVisitor](ReconstructionGeometryVisitor.md) | app-logic | 1 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 1 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructedSmallCircle.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructedSmallCircle --body
python scripts/gpq.py uses ReconstructedSmallCircle --kind class
python scripts/gpq.py hier ReconstructedSmallCircle
```
