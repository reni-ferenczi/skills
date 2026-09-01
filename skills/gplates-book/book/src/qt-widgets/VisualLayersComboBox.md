# VisualLayersComboBox

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 786 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/VisualLayersComboBox.h` | C++ | 115 |
| `src/qt-widgets/VisualLayersComboBox.cc` | C++ | 179 |

## Overview

[[[PROSE overview unit=qt-widgets/VisualLayersComboBox tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::VisualLayersComboBox`](#gplatesqtwidgetsvisuallayerscombobox) | class | `QComboBox` | — | 1 | VisualLayersComboBox allows the user to select a visual layer. |

## Members

### `GPlatesQtWidgets::VisualLayersComboBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `predicate_type` | typedef | `boost::function< bool ( GPlatesPresentation::VisualLayerType::Type ) >` | public | — |
| `VisualLayersComboBox( GPlatesPresentation::VisualLayers &visual_layers, GPlatesPresentation::VisualLayerRegistry &visual_layer_registry, const predicate_type &predicate, QWidget *parent_ = NULL)` | constructor | `None` | public | Constructs a VisualLayersComboBox that shows visual layers that meet a the given predicate based on the type of the visual layer. |
| `~VisualLayersComboBox()` | destructor | `None` | public | — |
| `get_selected_visual_layer()` | method | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | public | — |
| `set_selected_visual_layer( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | — |
| `selected_visual_layer_changed( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | — |
| `handle_visual_layers_changed()` | method | `void` | protected | Called when anything in the visual layers state is changed. |
| `handle_current_index_changed( int index)` | method | `void` | protected | — |
| `make_signal_slot_connections( GPlatesPresentation::VisualLayers *visual_layers)` | method | `void` | protected | — |
| `populate()` | method | `void` | protected | — |
| `d_visual_layers` | field | `GPlatesPresentation::VisualLayers` | protected | — |
| `d_visual_layer_registry` | field | `GPlatesPresentation::VisualLayerRegistry` | protected | — |
| `d_predicate` | field | `predicate_type` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_VISUALLAYERSCOMBOBOX_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/VisualLayersComboBox tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/DrawStyleDialog](DrawStyleDialog.md) | qt-widgets | 8 |
| [qt-widgets/TotalReconstructionPolesDialog](TotalReconstructionPolesDialog.md) | qt-widgets | 4 |
| [qt-widgets/ConfigureVelocityLegendOverlayDialog](ConfigureVelocityLegendOverlayDialog.md) | qt-widgets | 3 |

## Related

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `visual_layers` | `changed()` | `this` | `handle_visual_layers_changed()` |
| `this` | `currentIndexChanged(int)` | `this` | `handle_current_index_changed(int)` |
| `this` | `currentIndexChanged(int)` | `this` | `handle_current_index_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/VisualLayersComboBox.h
python scripts/gpq.py def GPlatesQtWidgets::VisualLayersComboBox --body
python scripts/gpq.py uses VisualLayersComboBox --kind class
python scripts/gpq.py hier VisualLayersComboBox
```
