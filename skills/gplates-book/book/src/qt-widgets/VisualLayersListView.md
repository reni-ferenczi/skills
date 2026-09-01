# VisualLayersListView

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1169 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/VisualLayersListView.h` | C++ | 125 |
| `src/qt-widgets/VisualLayersListView.cc` | C++ | 203 |

## Overview

A list view for displaying visual layers with drag-and-drop support for reordering. Uses persistent editors (one `VisualLayerWidget` per row) that remain open so users can edit each layer without double-clicking. Handles the lifecycle of editors as layers are added and removed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::VisualLayersListView`](#gplatesqtwidgetsvisuallayerslistview) | class | `QListView` | — | 0 | — |

## Members

### `GPlatesQtWidgets::VisualLayersListView`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VisualLayersListView( GPlatesGui::VisualLayersProxy &visual_layers, GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `dragEnterEvent( QDragEnterEvent *event_)` | method | `void` | public | — |
| `dropEvent( QDropEvent *event_)` | method | `void` | public | — |
| `rowsInserted( const QModelIndex &parent_, int start, int end)` | method | `void` | protected | — |
| `handle_begin_add_or_remove_layers()` | method | `void` | private | — |
| `handle_end_add_or_remove_layers()` | method | `void` | private | — |
| `open_persistent_editors( int begin_row, int end_row)` | method | `void` | private | Opens the persistent editor for entries in the list from begin\_row up to the entry before end\_row (i.e. half-open range). |
| `close_persistent_editors( int begin_row, int end_row)` | method | `void` | private | Same as open\_persistent\_editors but closes editors. |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_visual_layers` | field | `GPlatesGui::VisualLayersProxy` | private | — |
| `d_list_model` | field | `QAbstractItemModel` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_VISUALLAYERSLISTVIEW_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayersWidget](VisualLayersWidget.md) | qt-widgets | 2 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_visual_layers` | `begin_add_or_remove_layers()` | `this` | `handle_begin_add_or_remove_layers()` |
| `&d_visual_layers` | `end_add_or_remove_layers()` | `this` | `handle_end_add_or_remove_layers()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/VisualLayersListView.h
python scripts/gpq.py def GPlatesQtWidgets::VisualLayersListView --body
python scripts/gpq.py uses VisualLayersListView --kind class
python scripts/gpq.py hier VisualLayersListView
```
