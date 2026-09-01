# ReconstructionGeometry

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1562 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGeometry.h` | C++ | 159 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionGeometry tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionGeometryVisitor`](#gplatesapplogicreconstructiongeometryvisitor) | typedef | — | — | 1 | Typedef for visitor over non-const ReconstructionGeometry objects. |
| [`GPlatesAppLogic::ConstReconstructionGeometryVisitor`](#gplatesapplogicconstreconstructiongeometryvisitor) | typedef | — | — | 13 | Typedef for visitor over const ReconstructionGeometry objects. |
| [`GPlatesAppLogic::ReconstructionGeometry`](#gplatesapplogicreconstructiongeometry) | class | [`GPlatesUtils::ReferenceCount<ReconstructionGeometry>`](../utils/ReferenceCount.md) | — | 15 | Classes derived from ReconstructionGeometry contain geometry that has been reconstructed to a particular geological time-instant. |

## Members

### `GPlatesAppLogic::ReconstructionGeometryVisitor`

*None.*

### `GPlatesAppLogic::ConstReconstructionGeometryVisitor`

*None.*

### `GPlatesAppLogic::ReconstructionGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructionGeometry>` | public | A convenience typedef for a shared pointer to a non-const ReconstructionGeometry. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructionGeometry>` | public | A convenience typedef for a shared pointer to a const ReconstructionGeometry. |
| `maybe_null_ptr_type` | typedef | `boost::intrusive_ptr<ReconstructionGeometry>` | public | A convenience typedef for boost::intrusive\_ptr\<ReconstructionGeometry\>. |
| `maybe_null_ptr_to_const_type` | typedef | `boost::intrusive_ptr<const ReconstructionGeometry>` | public | A convenience typedef for boost::intrusive\_ptr\<const ReconstructionGeometry\>. |
| `~ReconstructionGeometry()` | destructor | `None` | public | — |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `ReconstructionGeometry( const double &reconstruction_time_, boost::optional<ReconstructHandle::type> reconstruct_handle_ = boost::none)` | constructor | `None` | protected | Construct a ReconstructionGeometry instance. |
| `d_reconstruction_time` | field | `double` | private | The reconstruction time of this reconstruction geometry. |
| `d_reconstruct_handle` | field | `boost::optional<ReconstructHandle::type>` | private | An optional reconstruct handle that can be used by clients to identify where this RG came from. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTIONGEOMETRY_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructionGeometry tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 65 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 48 |
| [view-operations/RenderedGeometryFactory](../view-operations/RenderedGeometryFactory.md) | view-operations | 34 |
| [gui/MapRenderedGeometryLayerPainter](../gui/MapRenderedGeometryLayerPainter.md) | gui | 29 |
| [app-logic/ResolvedSubSegmentRangeInSection](ResolvedSubSegmentRangeInSection.md) | app-logic | 28 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 22 |
| [app-logic/TopologyIntersections](TopologyIntersections.md) | app-logic | 21 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 20 |
| [gui/ColourProxy](../gui/ColourProxy.md) | gui | 20 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 18 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 17 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 16 |
| [app-logic/PartitionFeatureUtils](PartitionFeatureUtils.md) | app-logic | 15 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 15 |
| [gui/GlobeRenderedGeometryLayerPainter](../gui/GlobeRenderedGeometryLayerPainter.md) | gui | 15 |
| [gui/AddClickedGeometriesToFeatureTable](../gui/AddClickedGeometriesToFeatureTable.md) | gui | 14 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 14 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 13 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 12 |
| [view-operations/RenderedGeometryUtils](../view-operations/RenderedGeometryUtils.md) | view-operations | 12 |

*... and 98 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionGeometry.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionGeometry --body
python scripts/gpq.py uses ReconstructionGeometry --kind class
python scripts/gpq.py hier ReconstructionGeometry
```
