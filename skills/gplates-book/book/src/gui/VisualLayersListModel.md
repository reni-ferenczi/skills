# VisualLayersListModel

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1099 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/VisualLayersListModel.h` | C++ | 144 |
| `src/gui/VisualLayersListModel.cc` | C++ | 296 |

## Overview

`VisualLayersListModel` is a thin `QAbstractListModel` adapter over
`VisualLayersProxy`, letting `VisualLayersListView` display and reorder the
application's visual layers as an ordinary Qt item view. Each row's `data()`
is just the underlying layer's index (`child_layer_index_at()`); the actual
per-layer widget content is supplied elsewhere by `VisualLayersDelegate` and
`VisualLayerWidget`.

The model deliberately supports only one kind of edit — drag-and-drop
reordering. `dropMimeData()` decodes a row index from a custom
`VISUAL_LAYERS_MIME_TYPE` payload and calls `VisualLayersProxy::move_layer()`;
adding or removing layers has to go through `ReconstructGraph` instead; this
model only mirrors those changes back into the view via the
`handle_visual_layer_added`/`removed`/`modified`/`about_to_be_*` slots
connected to `VisualLayersProxy`'s signals. Using a private MIME type rather
than a generic one is intentional: it stops a layer being dragged out into an
unrelated application or view.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::VisualLayersListModel`](#gplatesguivisuallayerslistmodel) | class | `QAbstractListModel` | — | 0 | The VisualLayersListModel is a model that represents the ordering of visual layers that can be viewed and modified in a list view in the GUI. |

## Members

### `GPlatesGui::VisualLayersListModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VISUAL_LAYERS_MIME_TYPE` | field | `QString` | public | We need to define our own MIME type, otherwise users will be able to do silly things like drag from the visual layers list into another application. |
| `VisualLayersListModel( VisualLayersProxy &visual_layers, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `flags( const QModelIndex &index_)` | method | `Qt::ItemFlags` | public | — |
| `data( const QModelIndex &index_, int role = Qt::DisplayRole)` | method | `QVariant` | public | — |
| `rowCount( const QModelIndex &parent_ = QModelIndex())` | method | `int` | public | — |
| `supportedDropActions()` | method | `Qt::DropActions` | public | — |
| `mimeTypes()` | method | `QStringList` | public | — |
| `mimeData( const QModelIndexList &indices)` | method | `QMimeData` | public | — |
| `dropMimeData( const QMimeData *mime_data, Qt::DropAction action, int row, int column, const QModelIndex &parent_)` | method | `bool` | public | — |
| `handle_visual_layers_order_changed( size_t first_row, size_t last_row)` | method | `void` | private | — |
| `handle_visual_layer_about_to_be_added( size_t row)` | method | `void` | private | — |
| `handle_visual_layer_added( size_t row)` | method | `void` | private | — |
| `handle_visual_layer_about_to_be_removed( size_t row)` | method | `void` | private | — |
| `handle_visual_layer_removed( size_t row)` | method | `void` | private | — |
| `handle_visual_layer_modified( size_t row)` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_visual_layers` | field | `VisualLayersProxy` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `VISUAL_LAYERS_MIME_TYPE` | variable | `QString` | — |
| `GPLATES_GUI_VISUALLAYERSLISTMODEL_H` | macro | `None` | — |

## Notes

- Layers cannot be inserted or removed through this model's own API (`data()`
  is read-only apart from drag-and-drop) — always go through
  `ReconstructGraph`/`VisualLayersProxy` and let the `layer_added`/`layer_removed`
  signals update the view.
- `d_visual_layers` is stored as a reference, so the `VisualLayersProxy` it
  wraps must outlive the model.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 14 |
| [qt-widgets/VisualLayersListView](../qt-widgets/VisualLayersListView.md) | qt-widgets | 11 |
| [qt-widgets/VisualLayersDelegate](../qt-widgets/VisualLayersDelegate.md) | qt-widgets | 7 |

## Related

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_visual_layers` | `layer_order_changed(size_t, size_t)` | `this` | `handle_visual_layers_order_changed(size_t, size_t)` |
| `&d_visual_layers` | `layer_about_to_be_added(size_t)` | `this` | `handle_visual_layer_about_to_be_added(size_t)` |
| `&d_visual_layers` | `layer_added(size_t)` | `this` | `handle_visual_layer_added(size_t)` |
| `&d_visual_layers` | `layer_about_to_be_removed(size_t)` | `this` | `handle_visual_layer_about_to_be_removed(size_t)` |
| `&d_visual_layers` | `layer_removed(size_t)` | `this` | `handle_visual_layer_removed(size_t)` |
| `&d_visual_layers` | `layer_modified(size_t)` | `this` | `handle_visual_layer_modified(size_t)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/VisualLayersListModel.h
python scripts/gpq.py def GPlatesGui::VisualLayersListModel --body
python scripts/gpq.py uses VisualLayersListModel --kind class
python scripts/gpq.py hier VisualLayersListModel
```
