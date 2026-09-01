# CanvasTool

[Book TOC](../../TOC.md) · [canvas-tools](../../components/canvas-tools.md) · cluster Community 842 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/canvas-tools/CanvasTool.h` | C++ | 281 |

## Overview

`CanvasTool` is the view-agnostic half of GPlates' canvas-tool design. The real
mouse-handling interfaces are `GPlatesGui::GlobeCanvasTool` and
`GPlatesGui::MapCanvasTool`, and they are genuinely different: the globe hands a
tool two `PointOnSphere` positions (unoriented and oriented) plus an
`is_on_globe` flag, while the map hands it `QPointF` coordinates in the
`QGraphicsScene` plus a translation vector. Most tools do not care about that
difference — they want "where on the Earth did the user click, and how close does
a geometry have to be to count as hit". `CanvasTool` is that reduced interface:
one `GPlatesMaths::PointOnSphere`, an `is_on_earth` flag, and a
`proximity_inclusion_threshold`. Everything in `gpq hier CanvasTool` — feature
clicking, digitisation, vertex editing, topology building, distance measurement,
pole manipulation — is written once against it and works in both views.

The translation is done by `CanvasToolAdapterForGlobe` and
`CanvasToolAdapterForMap`, which derive from `GlobeCanvasTool` and
`MapCanvasTool` respectively and each hold a `CanvasTool::non_null_ptr_type`. A
workflow such as `GPlatesGui::DigitisationCanvasToolWorkflow` creates the tool
once (`ClickGeometry::create(...)`, `DigitiseGeometry::create(...)`, …) and wraps
that *same* instance in both adapters, then registers each adapter with the
corresponding canvas. The globe adapter forwards the *oriented* click position
but derives the proximity threshold from the *unoriented* one via
`GlobeCanvas::current_proximity_inclusion_threshold`; the map adapter inverts the
`GPlatesGui::MapProjection` to recover a point on the sphere and asks `MapView`
for the threshold. So a subclass sees a uniform coordinate space regardless of
which projection produced it.

Two conventions carry the rest of the design. Every handler is a header-only
virtual with a do-nothing body, so a subclass overrides only the gestures it
cares about and new handlers can be added without touching the thirteen existing
tools. And the four `handle_*ctrl*` drag/release handlers return `bool`: `true`
(the default) tells the adapter to also invoke `GlobeCanvasTool::handle_...` or
`MapCanvasTool::handle_...`, which reorients the globe or pans the map, so
Ctrl-drag navigation keeps working under every tool unless a tool deliberately
returns `false`. Tools that really do need the view-specific parameters bypass
`CanvasTool` entirely and derive from `GlobeCanvasTool` / `MapCanvasTool`
directly — `ReorientGlobe`, `ZoomGlobe`, `PanMap`, `ZoomMap`, `MovePoleGlobe` /
`MovePoleMap` and `ChangeLightDirectionGlobe` / `ChangeLightDirectionMap` are
the whole set, and they come in globe/map pairs precisely because they cannot use
this base class.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesCanvasTools::CanvasTool`](#gplatescanvastoolscanvastool) | class | [`GPlatesUtils::ReferenceCount<CanvasTool>`](../utils/ReferenceCount.md) | — | 13 | Base class for canvas tools that do not need to be implemented differently for globe and map views. |

## Members

### `GPlatesCanvasTools::CanvasTool`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~CanvasTool()` | destructor | `None` | public | — |
| `status_bar_callback_type` | typedef | `boost::function< void ( const char * ) >` | public | Typedef for a function that takes a C string and displays it on the status bar. |
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<CanvasTool>` | public | Convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<CanvasTool\>. |
| `handle_activation()` | method | `void` | public | — |
| `handle_deactivation()` | method | `void` | public | — |
| `handle_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_press( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphere> &c ...` | method | `void` | public | — |
| `handle_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::Poi ...` | method | `void` | public | — |
| `handle_shift_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_shift_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSphe ...` | method | `void` | public | — |
| `handle_shift_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMath ...` | method | `void` | public | — |
| `handle_ctrl_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_ctrl_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointOnSpher ...` | method | `bool` | public | — |
| `handle_ctrl_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths ...` | method | `bool` | public | — |
| `handle_shift_ctrl_left_click( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `handle_shift_ctrl_left_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlatesMaths::PointO ...` | method | `bool` | public | — |
| `handle_shift_ctrl_left_release_after_drag( const GPlatesMaths::PointOnSphere &initial_point_on_sphere, bool was_on_earth, double initial_proximity_inclusion_threshold, const GPlatesMaths::PointOnSphere &current_point_on_sphere, bool is_on_earth, double current_proximity_inclusion_threshold, const boost::optional<GPlate ...` | method | `bool` | public | — |
| `handle_move_without_drag( const GPlatesMaths::PointOnSphere &point_on_sphere, bool is_on_earth, double proximity_inclusion_threshold)` | method | `void` | public | — |
| `CanvasTool( const status_bar_callback_type &status_bar_callback)` | constructor | `None` | protected | Constructs CanvasTool, given status\_bar\_callback that can be used by the canvas tool to set status bar messages. |
| `set_status_bar_message( const char *message)` | method | `void` | protected | Subclasses call this function to set text on the status bar. |
| `d_status_bar_callback` | field | `status_bar_callback_type` | private | The callback used to show text on the status bar. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_CANVASTOOLS_CANVASTOOL_H` | macro | `None` | — |

## Notes

**One tool, two adapters.** Because the globe adapter and the map adapter share
a single `CanvasTool` instance, every event would be delivered twice if both
forwarded. Each adapter therefore guards every forward on
`globe_canvas().isVisible()` / `map_view().isVisible()` — the explicit comment on
`handle_deactivation` is "Avoid deactivating twice (in globe and map adaptor)".
Any handler you add to `CanvasTool` must be forwarded under the same guard in
both adapters, and a tool must not assume it is talked to by only one adapter
over its lifetime: switching between globe and map view swaps which one is live
while the tool's own state carries across.

**Ownership.** Tools are reference-counted through
`GPlatesUtils::ReferenceCount<CanvasTool>` and handed around as
`non_null_intrusive_ptr`; the workflow drops its local pointer after
construction and the two adapters keep the tool alive. The count is a
`boost::detail::atomic_count`, so the pointer itself is safe to copy across
threads even though the handlers are called from Qt's GUI thread.

**Oriented versus unoriented positions.** The `PointOnSphere` a handler receives
is the *oriented* position — the one to compare against geometry. The threshold
argument was computed by the adapter from the *unoriented* screen-relative
position, because that is what determines on-screen pixel distance. Do not try
to recompute the threshold from the point you were given.

**Off-globe and off-map are not symmetric.** In globe view the handlers are still
called when the click misses the globe: `is_on_earth` is `false` and the point is
the nearest point on the horizon. In map view `CanvasToolAdapterForMap` returns
early whenever `is_on_surface` is false, and also whenever the inverse map
projection yields no point, so the handler is simply never invoked — a tool
cannot rely on seeing an `is_on_earth == false` call in map view, nor on seeing
every gesture at all. Correspondingly `centre_of_viewport` is
`boost::optional`: the globe always supplies it, the map supplies the
inverse-projected viewport centre, which can be `boost::none`.

**Status bar strings must be untranslated.** `set_status_bar_message` takes a raw
`const char *` and the callback installed by `ViewportWindow` runs
`ViewportWindow::tr(message)` itself before appending a view-specific suffix
(different text for globe and map). Passing an already-`tr()`'d `QString`'s data
would defeat the lookup and lose the suffix. The call is also a silent no-op when
the `boost::function` is empty, so a tool constructed with a default-constructed
callback will not report an error.

**Two gaps in the map adapter.**
`CanvasToolAdapterForMap::handle_shift_ctrl_left_drag` dispatches to
`&CanvasTool::handle_ctrl_left_drag`, not to `handle_shift_ctrl_left_drag`, and
falls back to `MapCanvasTool::handle_ctrl_left_drag`; and
`handle_shift_ctrl_left_release_after_drag` is commented out in both the header
and the `.cc` with a `FIXME` noting that it is commented out in
`MapCanvasTool.h`. Overriding either of those two handlers in a `CanvasTool`
subclass will therefore not behave as declared in map view.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 52 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 47 |
| [canvas-tools/CanvasToolAdapterForMap](CanvasToolAdapterForMap.md) | canvas-tools | 42 |
| [canvas-tools/MeasureDistance](MeasureDistance.md) | canvas-tools | 36 |
| [canvas-tools/SelectHellingerGeometries](SelectHellingerGeometries.md) | canvas-tools | 27 |
| [gui/PoleManipulationCanvasToolWorkflow](../gui/PoleManipulationCanvasToolWorkflow.md) | gui | 25 |
| [canvas-tools/CanvasToolAdapterForGlobe](CanvasToolAdapterForGlobe.md) | canvas-tools | 24 |
| [canvas-tools/MoveVertex](MoveVertex.md) | canvas-tools | 20 |
| [gui/SmallCircleCanvasToolWorkflow](../gui/SmallCircleCanvasToolWorkflow.md) | gui | 20 |
| [gui/ViewCanvasToolWorkflow](../gui/ViewCanvasToolWorkflow.md) | gui | 19 |
| [gui/CanvasToolWorkflows](../gui/CanvasToolWorkflows.md) | gui | 17 |
| [canvas-tools/CreateSmallCircle](CreateSmallCircle.md) | canvas-tools | 16 |
| [canvas-tools/InsertVertex](InsertVertex.md) | canvas-tools | 16 |
| [canvas-tools/SplitFeature](SplitFeature.md) | canvas-tools | 16 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 16 |
| [canvas-tools/DeleteVertex](DeleteVertex.md) | canvas-tools | 15 |
| [canvas-tools/DigitiseGeometry](DigitiseGeometry.md) | canvas-tools | 15 |
| [gui/HellingerCanvasToolWorkflow](../gui/HellingerCanvasToolWorkflow.md) | gui | 15 |
| [canvas-tools/ManipulatePole](ManipulatePole.md) | canvas-tools | 14 |
| [canvas-tools/ClickGeometry](ClickGeometry.md) | canvas-tools | 12 |

*... and 20 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/canvas-tools/CanvasTool.h
python scripts/gpq.py def GPlatesCanvasTools::CanvasTool --body
python scripts/gpq.py uses CanvasTool --kind class
python scripts/gpq.py hier CanvasTool
```
