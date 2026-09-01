# VisualLayersDelegate

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1067 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/VisualLayersDelegate.h` | C++ | 131 |
| `src/qt-widgets/VisualLayersDelegate.cc` | C++ | 174 |

## Overview

Qt item delegate that renders and edits visual layers in the layers list view. Each layer row is edited with a `VisualLayerWidget`, which provides the controls for layer visibility, name, and type-specific options. The delegate maintains a map of active editor widgets keyed by layer, and cleans up editors when layers are removed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::VisualLayersDelegate`](#gplatesqtwidgetsvisuallayersdelegate) | class | `QItemDelegate` | — | 0 | VisualLayersDelegate provides display and editing facilities for the model underlying the VisualLayersWidget. |

## Members

### `GPlatesQtWidgets::VisualLayersDelegate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VisualLayersDelegate( GPlatesGui::VisualLayersProxy &visual_layers, GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `sizeHint( const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `QSize` | public | — |
| `createEditor( QWidget *parent_, const QStyleOptionViewItem &option, const QModelIndex &index)` | method | `QWidget` | public | — |
| `setEditorData( QWidget *editor, const QModelIndex &index)` | method | `void` | public | — |
| `handle_layer_about_to_be_removed( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `emit_size_hint_changed( const QModelIndex &index)` | method | `void` | private | — |
| `editor_ptr_map_type` | typedef | `std::map< boost::weak_ptr<GPlatesPresentation::VisualLayer>, VisualLayerWidget * >` | private | Typedef for map that remembers which edit widget is currently displaying the contents of a particular VisualLayer. |
| `d_visual_layers` | field | `GPlatesGui::VisualLayersProxy` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_editor_ptrs` | field | `editor_ptr_map_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_VISUALLAYERSDELEGATE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayersListView](VisualLayersListView.md) | qt-widgets | 15 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_visual_layers` | `layer_about_to_be_removed( boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | `this` | `handle_layer_about_to_be_removed( boost::weak_ptr<GPlatesPresentation::VisualLayer>)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/VisualLayersDelegate.h
python scripts/gpq.py def GPlatesQtWidgets::VisualLayersDelegate --body
python scripts/gpq.py uses VisualLayersDelegate --kind class
python scripts/gpq.py hier VisualLayersDelegate
```
