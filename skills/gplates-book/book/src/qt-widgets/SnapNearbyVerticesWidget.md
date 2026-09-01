# SnapNearbyVerticesWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 424 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SnapNearbyVerticesWidget.h` | C++ | 105 |
| `src/qt-widgets/SnapNearbyVerticesWidget.cc` | C++ | 190 |
| `src/qt-widgets/SnapNearbyVerticesWidgetUi.ui` | Qt form | 176 |

## Overview

A configuration widget for snapping vertices during interactive geometry editing, embedded in the task panel. The widget provides checkboxes to enable/disable snapping to nearby vertices and snapping to a specific plate ID, plus spinboxes for the threshold distance (in degrees) and the plate ID value. The conjugate plate ID is optionally extracted from the focused feature and displayed.

When any control changes, the widget updates the `ModifyGeometryState` to reflect the current snap settings, which the geometry modification tools then apply during editing.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SnapNearbyVerticesWidget`](#gplatesqtwidgetssnapnearbyverticeswidget) | class | `QWidget`<br>`Ui_SnapNearbyVerticesWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::SnapNearbyVerticesWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SnapNearbyVerticesWidget( GPlatesCanvasTools::ModifyGeometryState &modify_geometry_state, GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `setup_connections()` | method | `void` | private | — |
| `send_update_signal()` | method | `void` | private | — |
| `set_default_widget_values()` | method | `void` | private | — |
| `handle_vertex_checkbox_changed(int)` | method | `void` | private | — |
| `handle_plate_checkbox_changed(int)` | method | `void` | private | — |
| `handle_spinbox_threshold_changed(double)` | method | `void` | private | — |
| `handle_spinbox_plate_id_changed(int)` | method | `void` | private | — |
| `d_modify_geometry_state` | field | `GPlatesCanvasTools::ModifyGeometryState` | private | — |
| `d_feature_focus_ptr` | field | `GPlatesGui::FeatureFocus` | private | — |
| `d_conjugate_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_focused_feature` | field | `GPlatesModel::FeatureHandle::const_weak_ref` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DEFAULT_THRESHOLD_DEGREES` | variable | `double` | — |
| `get_conjugate_plate_id( const GPlatesModel::FeatureHandle::const_weak_ref &feature_handle)` | function | `boost::optional<GPlatesModel::integer_plate_id_type>` | — |
| `GPLATES_QTWIDGETS_SNAPNEARBYVERTICESWIDGET_H` | macro | `None` | — |

## Notes

The widget maintains weak references to the focused feature and holds the conjugate plate ID as an optional value, defaulting to absent if the feature does not define one or if no feature is focused. The plate ID spinbox accepts values in the range [0, 2^31-1].

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 2 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SnapNearbyVerticesWidget` | `QWidget` | Form | 10 |

**Qt signal/slot connections** (4 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `checkbox_vertices` | `stateChanged(int)` | `this` | `handle_vertex_checkbox_changed(int)` |
| `checkbox_plate_id` | `stateChanged(int)` | `this` | `handle_plate_checkbox_changed(int)` |
| `spinbox_threshold` | `valueChanged(double)` | `this` | `handle_spinbox_threshold_changed(double)` |
| `spinbox_plate_id` | `valueChanged(int)` | `this` | `handle_spinbox_plate_id_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SnapNearbyVerticesWidget.h
python scripts/gpq.py def GPlatesQtWidgets::SnapNearbyVerticesWidget --body
python scripts/gpq.py uses SnapNearbyVerticesWidget --kind class
python scripts/gpq.py hier SnapNearbyVerticesWidget
```
