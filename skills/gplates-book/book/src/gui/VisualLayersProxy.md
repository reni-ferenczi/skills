# VisualLayersProxy

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 618 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/VisualLayersProxy.h` | C++ | 223 |
| `src/gui/VisualLayersProxy.cc` | C++ | 265 |

## Overview

`VisualLayersProxy` adapts `GPlatesPresentation::VisualLayers` for the layers
UI. `VisualLayers` stores layers in draw order (back to front, since that is
what the renderer needs), but the "Visual Layers" panel presents them
top-first (front to back), which is more natural for a user reordering them.
This class is that reversal: every index-taking method (`visual_layer_at()`,
`child_layer_index_at()`, `move_layer()`) runs the index through `fix_index()`
before or after delegating to `VisualLayers`, and every index-carrying signal
`VisualLayers` emits is caught, re-indexed, and re-emitted in the flipped
order so that `VisualLayersListModel` and the rest of the UI never has to
think about the underlying storage order.

It is the sole way the GUI layer talks to `VisualLayers` for listing, showing,
hiding, reordering and looking up visual layers (`get_visual_layer()`,
`show_all()`, `hide_all()`); `VisualLayersListModel` and the `VisualLayers*`
widgets all hold a `VisualLayersProxy &` rather than a `VisualLayers &`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::VisualLayersProxy`](#gplatesguivisuallayersproxy) | class | `QObject` | — | 0 | VisualLayersProxy is a simple wrapper around VisualLayers that reverses the order of visual layers. |

## Members

### `GPlatesGui::VisualLayersProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VisualLayersProxy( GPlatesPresentation::VisualLayers &visual_layers)` | constructor | `None` | public | — |
| `size()` | method | `size_t` | public | — |
| `move_layer( size_t from_index, size_t to_index)` | method | `void` | public | — |
| `visual_layer_at( size_t index)` | method | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | public | — |
| `child_layer_index_at( size_t index)` | method | `GPlatesViewOperations::RenderedGeometryCollection::child_layer_index_type` | public | — |
| `get_visual_layer( const GPlatesAppLogic::Layer &layer)` | method | `boost::weak_ptr<const GPlatesPresentation::VisualLayer>` | public | — |
| `show_all()` | method | `void` | public | — |
| `hide_all()` | method | `void` | public | — |
| `handle_layer_order_changed( size_t first_index, size_t last_index)` | method | `void` | private | — |
| `handle_begin_add_or_remove_layers()` | method | `void` | private | — |
| `handle_end_add_or_remove_layers()` | method | `void` | private | — |
| `handle_layer_about_to_be_added( size_t index)` | method | `void` | private | — |
| `handle_layer_added( size_t index)` | method | `void` | private | — |
| `handle_layer_added( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | private | — |
| `handle_layer_about_to_be_removed( size_t index)` | method | `void` | private | — |
| `handle_layer_about_to_be_removed( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | private | — |
| `handle_layer_removed( size_t index)` | method | `void` | private | — |
| `handle_layer_modified( size_t index)` | method | `void` | private | — |
| `handle_layer_modified( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | private | — |
| `layer_order_changed( size_t first_index, size_t last_index)` | method | `void` | public | — |
| `begin_add_or_remove_layers()` | method | `void` | public | — |
| `end_add_or_remove_layers()` | method | `void` | public | — |
| `layer_about_to_be_added( size_t index)` | method | `void` | public | — |
| `layer_added( size_t index)` | method | `void` | public | — |
| `layer_added( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | — |
| `layer_about_to_be_removed( size_t index)` | method | `void` | public | — |
| `layer_about_to_be_removed( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | — |
| `layer_removed( size_t index)` | method | `void` | public | — |
| `layer_modified( size_t index)` | method | `void` | public | — |
| `layer_modified( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | — |
| `fix_index( size_t index)` | method | `size_t` | private | — |
| `fix_index( size_t index, size_t custom_visual_layers_size)` | method | `size_t` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_visual_layers` | field | `GPlatesPresentation::VisualLayers` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_VISUALLAYERSPROXY_H` | macro | `None` | — |

## Notes

- `fix_index(index)` computes `size() - 1 - index`, so it depends on the
  *current* container size — that is why `handle_layer_about_to_be_added()`
  passes the explicit-size overload `fix_index(index, size() + 1)`: at that
  point in the add sequence the underlying `VisualLayers` container has not
  been resized yet, so `size()` alone would give the wrong flipped index.
- `handle_layer_order_changed()` re-emits with `first_index`/`last_index`
  swapped as well as flipped (`fix_index(last_index), fix_index(first_index)`),
  since reversing a `[first, last]` range also reverses which end is which.
- `d_visual_layers` is stored as a reference; the `VisualLayers` instance it
  wraps must outlive the proxy.

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/VisualLayersListModel](VisualLayersListModel.md) | gui | 12 |
| [qt-widgets/VisualLayersDelegate](../qt-widgets/VisualLayersDelegate.md) | qt-widgets | 10 |
| [qt-widgets/VisualLayersWidget](../qt-widgets/VisualLayersWidget.md) | qt-widgets | 10 |
| [qt-widgets/VisualLayersDialog](../qt-widgets/VisualLayersDialog.md) | qt-widgets | 4 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 3 |
| [qt-widgets/VisualLayersListView](../qt-widgets/VisualLayersListView.md) | qt-widgets | 3 |

## Related

**Qt signal/slot connections** (11 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `&d_visual_layers` | `layer_order_changed(size_t, size_t)` | `this` | `handle_layer_order_changed(size_t, size_t)` |
| `&d_visual_layers` | `begin_add_or_remove_layers()` | `this` | `handle_begin_add_or_remove_layers()` |
| `&d_visual_layers` | `end_add_or_remove_layers()` | `this` | `handle_end_add_or_remove_layers()` |
| `&d_visual_layers` | `layer_about_to_be_added(size_t)` | `this` | `handle_layer_about_to_be_added(size_t)` |
| `&d_visual_layers` | `layer_added(size_t)` | `this` | `handle_layer_added(size_t)` |
| `&d_visual_layers` | `layer_added(boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | `this` | `handle_layer_added(boost::weak_ptr<GPlatesPresentation::VisualLayer>)` |
| `&d_visual_layers` | `layer_about_to_be_removed(size_t)` | `this` | `handle_layer_about_to_be_removed(size_t)` |
| `&d_visual_layers` | `layer_about_to_be_removed(boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | `this` | `handle_layer_about_to_be_removed(boost::weak_ptr<GPlatesPresentation::VisualLayer>)` |
| `&d_visual_layers` | `layer_removed(size_t)` | `this` | `handle_layer_removed(size_t)` |
| `&d_visual_layers` | `layer_modified(size_t)` | `this` | `handle_layer_modified(size_t)` |
| `&d_visual_layers` | `layer_modified(boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | `this` | `handle_layer_modified(boost::weak_ptr<GPlatesPresentation::VisualLayer>)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/VisualLayersProxy.h
python scripts/gpq.py def GPlatesGui::VisualLayersProxy --body
python scripts/gpq.py uses VisualLayersProxy --kind class
python scripts/gpq.py hier VisualLayersProxy
```
