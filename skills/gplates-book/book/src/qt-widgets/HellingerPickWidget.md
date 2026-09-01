# HellingerPickWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 75 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/HellingerPickWidget.h` | C++ | 261 |
| `src/qt-widgets/HellingerPickWidget.cc` | C++ | 901 |
| `src/qt-widgets/HellingerPickWidgetUi.ui` | Qt form | 378 |

## Overview

[[[PROSE overview unit=qt-widgets/HellingerPickWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::PickColumns`](#anonymouspickcolumns) | enum | — | — | 0 | — |
| [`GPlatesQtWidgets::HellingerPickWidget`](#gplatesqtwidgetshellingerpickwidget) | class | `QWidget`<br>`Ui_HellingerPickWidget` | — | 0 | — |

## Members

### `(anonymous)::PickColumns`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SEGMENT_NUMBER` | enumerator | `None` | — | — |
| `SEGMENT_TYPE` | enumerator | `None` | — | — |
| `LAT` | enumerator | `None` | — | — |
| `LON` | enumerator | `None` | — | — |
| `UNCERTAINTY` | enumerator | `None` | — | — |
| `NUM_COLUMNS` | enumerator | `None` | — | — |

### `GPlatesQtWidgets::HellingerPickWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `expanded_status_map_type` | typedef | `std::map<int,bool>` | private | — |
| `tree_items_collection_type` | typedef | `std::vector<QTreeWidgetItem*>` | public | — |
| `HellingerPickWidget( HellingerDialog *hellinger_dialog, HellingerModel *hellinger_model)` | constructor | `None` | public | — |
| `~HellingerPickWidget()` | destructor | `None` | public | — |
| `update_after_switching_tabs()` | method | `void` | public | — |
| `update_from_model( bool expand_tree_after_update = false)` | method | `void` | public | — |
| `update_buttons()` | method | `void` | public | — |
| `segment_number_of_selected_pick()` | method | `boost::optional<unsigned int>` | public | — |
| `selected_segment()` | method | `boost::optional<unsigned int>` | public | — |
| `selected_row()` | method | `boost::optional<unsigned int>` | public | — |
| `selected_pick()` | method | `boost::optional<hellinger_model_type::const_iterator>` | public | — |
| `tree_items()` | method | `tree_items_collection_type` | public | — |
| `restore()` | method | `void` | public | — |
| `handle_close()` | method | `void` | public | — |
| `picks_loaded()` | method | `bool` | public | — |
| `update_hovered_item( const unsigned int geometry_index, bool is_enabled)` | method | `void` | public | — |
| `set_selected_pick_from_geometry_index( const unsigned int index)` | method | `void` | public | — |
| `clear_hovered_item()` | method | `void` | public | — |
| `renumber_segments()` | method | `void` | public | — |
| `update_after_new_or_edited_pick( const hellinger_model_type::const_iterator &it, const int segment_number)` | method | `void` | public | — |
| `update_after_new_or_edited_segment( const int segment_number)` | method | `void` | public | — |
| `store_scrollbar_status()` | method | `void` | public | — |
| `restore_scrollbar_status()` | method | `void` | public | — |
| `edit_pick_signal()` | method | `void` | public | — |
| `add_new_pick_signal()` | method | `void` | public | — |
| `add_new_segment_signal()` | method | `void` | public | — |
| `edit_segment_signal()` | method | `void` | public | — |
| `tree_updated_signal()` | method | `void` | public | — |
| `handle_expand_all()` | method | `void` | private | — |
| `handle_collapse_all()` | method | `void` | private | — |
| `handle_edit_pick()` | method | `void` | private | — |
| `handle_add_new_pick()` | method | `void` | private | — |
| `handle_remove_pick()` | method | `void` | private | — |
| `handle_remove_segment()` | method | `void` | private | — |
| `handle_add_new_segment()` | method | `void` | private | — |
| `handle_edit_segment()` | method | `void` | private | — |
| `handle_selection_changed( const QItemSelection &, const QItemSelection &)` | method | `void` | private | — |
| `handle_pick_state_changed()` | method | `void` | private | — |
| `handle_clear()` | method | `void` | private | — |
| `handle_renumber_segments()` | method | `void` | private | — |
| `store_expanded_status()` | method | `void` | private | — |
| `restore_expanded_status()` | method | `void` | private | — |
| `initialise_widgets()` | method | `void` | private | — |
| `set_up_connections()` | method | `void` | private | — |
| `update_tree_from_model()` | method | `void` | private | — |
| `update_selected_pick_and_segment()` | method | `void` | private | — |
| `update_enable_disable_buttons()` | method | `void` | private | — |
| `expand_segment( const unsigned int segment_number)` | method | `void` | private | — |
| `set_selected_segment( const unsigned int segment_number)` | method | `void` | private | — |
| `set_selected_pick( const hellinger_model_type::const_iterator &it)` | method | `void` | private | — |
| `d_hellinger_dialog_ptr` | field | `HellingerDialog` | private | — |
| `d_hellinger_model_ptr` | field | `HellingerModel` | private | — |
| `d_tree_items` | field | `tree_items_collection_type` | private | — |
| `d_selected_segment` | field | `boost::optional<unsigned int>` | private | d\_selected\_segment - the number of the selected segment, if a segment has been selected in the tree\_widget |
| `d_selected_pick` | field | `boost::optional<hellinger_model_type::const_iterator>` | private | d\_selected\_pick - the selected pick in the tree\_widget, if a pick has been selected |
| `d_segment_number_of_selected_pick` | field | `boost::optional<unsigned int>` | private | d\_segment\_number\_of\_selected\_pick - if a pick has been selected, the segment number of that pick. |
| `d_segment_expanded_status` | field | `expanded_status_map_type` | private | d\_segment\_expanded\_status - map storing the status of expanded/collapsed parts of the tree widget, so that this can be restored when necessary. |
| `d_scrollbar_position` | field | `int` | private | — |
| `d_scrollbar_maximum` | field | `int` | private | — |
| `d_hovered_item` | field | `boost::optional<QTreeWidgetItem*>` | private | — |
| `d_hovered_item_original_state` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `selected_segment_from_tree_widget( const QTreeWidget *tree)` | function | `boost::optional<unsigned int>` | — |
| `selected_row_from_tree_widget( const QTreeWidget *tree)` | function | `boost::optional<unsigned int>` | — |
| `tree_item_is_pick_item( const QTreeWidgetItem *item)` | function | `bool` | — |
| `tree_item_is_segment_item( const QTreeWidgetItem *item)` | function | `bool` | — |
| `renumber_expanded_status_map( GPlatesQtWidgets::HellingerDialog::expanded_status_map_type &map)` | function | `void` | renumber\_expanded\_status\_map On return the keys of map will be contiguous from 1. |
| `set_text_colour_according_to_enabled_state( QTreeWidgetItem *item, bool enabled)` | function | `void` | — |
| `set_hovered_item( QTreeWidgetItem *item)` | function | `void` | — |
| `reset_hovered_item( QTreeWidgetItem *item, bool original_state)` | function | `void` | — |
| `translate_segment_type( GPlatesQtWidgets::HellingerPlateIndex type)` | function | `QString` | translate\_segment\_type Convert PLATE\_ONE\_PICK\_TYPE/DISABLED\_PLATE\_ONE\_PICK\_TYPE types to a QString form of PLATE\_ONE\_PICK\_TYPE; similarly for PLATE\_TWO... and PLATE\_THREE... |
| `add_pick_to_segment( QTreeWidget *tree, QTreeWidgetItem *parent_item, const int &segment_number, const GPlatesQtWidgets::HellingerPick &pick, GPlatesQtWidgets::HellingerPickWidget::tree_items_collection_type &tree_indices, bool set_as_selected)` | function | `void` | — |
| `add_pick_to_tree( const int &segment_number, const GPlatesQtWidgets::HellingerPick &pick, QTreeWidget *tree, GPlatesQtWidgets::HellingerPickWidget::tree_items_collection_type &tree_indices, bool set_as_selected_pick)` | function | `void` | — |
| `display_map( const GPlatesQtWidgets::HellingerDialog::expanded_status_map_type &map)` | function | `void` | For debugging. |
| `GPLATES_QTWIDGETS_HELLINGERPICKWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/HellingerPickWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](HellingerDialog.md) | qt-widgets | 9 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `HellingerPickWidget` | `QWidget` | Form | 16 |

**Qt signal/slot connections** (20 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_expand_all` | `clicked()` | `this` | `handle_expand_all()` |
| `button_collapse_all` | `clicked()` | `this` | `handle_collapse_all()` |
| `button_new_pick` | `clicked()` | `this` | `handle_add_new_pick()` |
| `button_edit_pick` | `clicked()` | `this` | `handle_edit_pick()` |
| `button_remove_pick` | `clicked()` | `this` | `handle_remove_pick()` |
| `button_remove_segment` | `clicked()` | `this` | `handle_remove_segment()` |
| `button_new_segment` | `clicked()` | `this` | `handle_add_new_segment()` |
| `button_edit_segment` | `clicked()` | `this` | `handle_edit_segment()` |
| `button_activate_pick` | `clicked()` | `this` | `handle_pick_state_changed()` |
| `button_deactivate_pick` | `clicked()` | `this` | `handle_pick_state_changed()` |
| `button_renumber` | `clicked()` | `this` | `handle_renumber_segments()` |
| `button_clear` | `clicked()` | `this` | `handle_clear()` |
| `tree_widget` | `collapsed(QModelIndex)` | `this` | `store_expanded_status()` |
| `tree_widget` | `expanded(QModelIndex)` | `this` | `store_expanded_status()` |
| `tree_widget->selectionModel()` | `selectionChanged (const QItemSelection &, const QItemSelection &)` | `this` | `handle_selection_changed(const QItemSelection &, const QItemSelection &)` |

*... and 5 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/HellingerPickWidget.h
python scripts/gpq.py def GPlatesQtWidgets::HellingerPickWidget --body
python scripts/gpq.py uses HellingerPickWidget --kind class
python scripts/gpq.py hier HellingerPickWidget
```
