# DrawStyleDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 176 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/DrawStyleDialog.h` | C++ | 345 |
| `src/qt-widgets/DrawStyleDialog.cc` | C++ | 1002 |
| `src/qt-widgets/DrawStyleDialogUi.ui` | Qt form | 309 |

## Overview

`DrawStyleDialog` is the "Draw Style" dialog: it lets the user pick, edit and
preview the `GPlatesGui::StyleAdapter` (a Python-configurable colouring/drawing
style) applied to a single visual layer, or to "All" layers via `LayerGroupComboBox`
— a `VisualLayersComboBox` restricted (through its `predicate_type` `pred()`) to
reconstruct and topology-resolver layers, with an extra synthetic "All" entry
prepended by `insert_all()`. Available styles are organised into categories in
`categories_table` (populated from `GPlatesGui::DrawStyleManager::all_catagories()`)
and listed per-category in `style_list`; selecting one calls `set_style()`, which
either stores the adapter directly in the locked layer's visual params or, for
"All", records it in `d_style_of_all` and pushes it out to every layer via
`apply_style_to_all_layers()`. Editable style configurations (`GPlatesGui::Configuration`,
built from Python-exposed `PythonCfgItem`s) are rendered into ad hoc widgets by
`create_cfg_widget()`, one specialised subclass per config item type
(`PythonArgColorWidget`, `PythonArgPaletteWidget`, or the generic
`PythonArgDefaultWidget`), and edits there flow back through `handle_configuration_changed()`.

Each style entry gets a live preview icon rendered from the actual globe/map
canvas: the dialog listens to the main `GlobeAndMapWidget`'s `repainted()` signal
in `handle_main_repaint()` and calls `show_preview_icons()` whenever the mouse is
released and the dialog is visible, guarding against the resulting
select-style-to-preview -> repaint -> select-style-to-preview feedback loop with
`d_ignore_next_main_repaint`. The nested `PreviewGuard` RAII class disables the
combo box and categories table for the duration of an icon-generation pass (which
temporarily switches the active style for each candidate) and restores the
previously selected style and re-enables the widgets on destruction. `reset()`
(re-)initialises the dialog for a given layer — or "All" if the weak pointer is
invalid — each time it is popped up, and its `style_` parameter is a documented
workaround (see the `FIXME` on it) letting an external observer push a style
change into the dialog's own state without the dialog otherwise tracking layer
visual-params changes made elsewhere.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::LayerGroupComboBox`](#gplatesqtwidgetslayergroupcombobox) | class | [`VisualLayersComboBox`](VisualLayersComboBox.md) | — | 0 | — |
| [`GPlatesQtWidgets::DrawStyleDialog`](#gplatesqtwidgetsdrawstyledialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_DrawStyleDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::LayerGroupComboBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LayerGroupComboBox( GPlatesPresentation::VisualLayers &visual_layers, GPlatesPresentation::VisualLayerRegistry &visual_layer_registry, const predicate_type &predicate, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_selected_visual_layer( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer)` | method | `void` | public | Override base class since need to handle 'all' layers (represented by an invalid weak\_ptr). |
| `populate()` | method | `void` | protected | — |
| `insert_all()` | method | `void` | protected | — |

### `GPlatesQtWidgets::DrawStyleDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DrawStyleDialog( GPlatesPresentation::ViewState &view_state, QWidget* parent_ = NULL)` | constructor | `None` | public | — |
| `~DrawStyleDialog()` | destructor | `None` | public | — |
| `reset()` | method | `void` | public | Similar to the other overload of reset, but uses the layer (or none) currently set by the most recent call to that reset. |
| `reset( boost::weak_ptr<GPlatesPresentation::VisualLayer> layer, // // FIXME: DrawStyleDialog should update its GUI when the draw style changes in visual layer params. // // Currently DrawStyleDialog clobbers the draw style in the visual layer params. // DrawStyleDialog should just be one observer of visual layer params ...` | method | `void` | public | Set up this dialog (after it has been popped up) for a specific layer, or 'all' layers if layer is invalid. |
| `showEvent( QShowEvent *show_event)` | method | `void` | protected | — |
| `init_category_table()` | method | `void` | protected | — |
| `init_dlg()` | method | `void` | protected | — |
| `make_signal_slot_connections()` | method | `void` | protected | — |
| `set_style()` | method | `void` | protected | — |
| `set_style( GPlatesGui::StyleAdapter* style)` | method | `void` | protected | — |
| `load_category( const GPlatesGui::StyleCategory& )` | method | `void` | protected | — |
| `show_preview_icons()` | method | `void` | protected | — |
| `get_catagory( QTableWidgetItem& item)` | method | `GPlatesGui::StyleCategory` | protected | — |
| `get_style( QListWidgetItem* item)` | method | `GPlatesGui::StyleAdapter` | protected | — |
| `refresh_current_icon()` | method | `void` | protected | — |
| `create_cfg_widget( GPlatesGui::PythonCfgItem* item)` | method | `QWidget` | protected | — |
| `build_config_panel(const GPlatesGui::Configuration& cfg)` | method | `void` | protected | — |
| `enable_config_panel(bool flag)` | method | `void` | protected | — |
| `get_current_style()` | method | `GPlatesGui::StyleAdapter` | protected | — |
| `is_style_name_valid( const GPlatesGui::StyleCategory&, const QString&)` | method | `bool` | protected | — |
| `generate_new_valid_style_name( const GPlatesGui::StyleCategory&, const QString&)` | method | `QString` | protected | — |
| `focus_style( const GPlatesGui::StyleAdapter*)` | method | `void` | protected | — |
| `apply_style_to_all_layers()` | method | `void` | protected | — |
| `handle_close_button_clicked()` | method | `void` | private | — |
| `handle_remove_button_clicked()` | method | `void` | private | — |
| `handle_categories_table_cell_changed( int current_row, int current_column, int previous_row, int previous_column)` | method | `void` | private | — |
| `handle_style_selection_changed( QListWidgetItem* current, QListWidgetItem* previous)` | method | `void` | private | — |
| `handle_main_repaint( bool)` | method | `void` | private | — |
| `handle_show_thumbnails_changed( int state)` | method | `void` | private | — |
| `handle_cfg_name_changed( const QString& new_cfg_name)` | method | `void` | private | — |
| `handle_add_button_clicked( bool)` | method | `void` | private | — |
| `handle_configuration_changed()` | method | `void` | private | — |
| `handle_layer_changed( boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | method | `void` | private | — |
| `PreviewGuard` | class | `None` | private | — |
| `ICON_SIZE` | field | `int` | private | — |
| `d_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | — |
| `d_blank_icon` | field | `QIcon` | private | — |
| `d_style_mgr` | field | `GPlatesGui::DrawStyleManager` | private | — |
| `d_show_thumbnails` | field | `bool` | private | — |
| `d_ignore_next_main_repaint` | field | `bool` | private | — |
| `d_globe_and_map_widget_ptr` | field | `GlobeAndMapWidget` | private | — |
| `d_last_open_directory` | field | `QString` | private | — |
| `d_cfg_widgets` | field | `std::vector<QWidget*>` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_combo_box` | field | `LayerGroupComboBox` | private | — |
| `d_style_of_all` | field | `GPlatesGui::StyleAdapter` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `pred(GPlatesPresentation::VisualLayerType::Type t)` | function | `bool` | — |
| `to_QPixmap( const QImage& img)` | function | `QPixmap` | — |
| `GPLATES_QTWIDGETS_DRAWSTYLEDIALOG_H` | macro | `None` | — |

## Notes

`DrawStyleDialog` does not merely observe a layer's draw style — `set_style()` and
`reset()` write into it directly, so as the `FIXME` on `reset()`'s `style_`
parameter documents, another code path that changes a layer's style bypasses this
dialog's own GUI state unless it goes through that parameter to keep the two in
sync. The destructor calls `GPlatesGui::DrawStyleManager::save_user_defined_styles()`
only if `DrawStyleManager::is_alive()`, since the manager is a Meyer's-style
singleton that may already have been destroyed at static-destruction time.
`handle_main_repaint()` must ignore the repaint triggered by its own style change
(via `d_ignore_next_main_repaint`) or preview-icon generation would trigger
another repaint indefinitely.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructLayerOptionsWidget](ReconstructLayerOptionsWidget.md) | qt-widgets | 4 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 4 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 2 |
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 2 |
| [gui/Dialogs](../gui/Dialogs.md) | gui | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `DrawStyleDialog` | `QDialog` | Draw Style | 21 |

**Qt signal/slot connections** (11 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `this` | `currentIndexChanged(int)` | `this` | `handle_current_index_changed(int)` |
| `close_button` | `clicked()` | `this` | `handle_close_button_clicked()` |
| `remove_button` | `clicked()` | `this` | `handle_remove_button_clicked()` |
| `add_button` | `clicked(bool)` | `this` | `handle_add_button_clicked(bool)` |
| `categories_table` | `currentCellChanged(int, int, int, int)` | `this` | `handle_categories_table_cell_changed(int, int, int, int)` |
| `style_list` | `currentItemChanged(QListWidgetItem*,QListWidgetItem*)` | `this` | `handle_style_selection_changed(QListWidgetItem*,QListWidgetItem*)` |
| `&GPlatesPresentation::Application::instance().get_main_window().reconstruction_view_widget().globe_and_map_widget()` | `repainted(bool)` | `this` | `handle_main_repaint(bool)` |
| `show_thumbnails_checkbox` | `stateChanged(int)` | `this` | `handle_show_thumbnails_changed(int)` |
| `cfg_name_line_edit` | `textChanged(const QString&)` | `this` | `handle_cfg_name_changed(const QString&)` |
| `d_combo_box` | `selected_visual_layer_changed( boost::weak_ptr<GPlatesPresentation::VisualLayer>)` | `this` | `handle_layer_changed( boost::weak_ptr<GPlatesPresentation::VisualLayer>)` |
| `cfg_widget` | `configuration_changed()` | `this` | `handle_configuration_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/DrawStyleDialog.h
python scripts/gpq.py def GPlatesQtWidgets::DrawStyleDialog --body
python scripts/gpq.py uses DrawStyleDialog --kind class
python scripts/gpq.py hier DrawStyleDialog
```
