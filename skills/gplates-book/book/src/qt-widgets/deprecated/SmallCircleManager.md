# SmallCircleManager

[Book TOC](../../../TOC.md) · [qt-widgets](../../../components/qt-widgets.md) · cluster Community 1009 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/deprecated/SmallCircleManager.h` | C++ | 108 |
| `src/qt-widgets/deprecated/SmallCircleManager.cc` | C++ | 288 |
| `src/qt-widgets/deprecated/SmallCircleManagerUi.ui` | Qt form | 151 |

## Overview

A dialog for managing a collection of small circles on the globe, displaying them in a table and on the rendered geometry layer. The dialog shows center coordinates (as latitude/longitude) and radius (in degrees) for each circle, and provides buttons to add new circles using a `CreateSmallCircleDialog`, remove selected rows, or clear the entire collection. Most functionality is disabled via preprocessor conditionals.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SmallCircleManager`](#gplatesqtwidgetssmallcirclemanager) | class | `QDialog`<br>`Ui_SmallCircleManager` | — | 0 | — |

## Members

### `GPlatesQtWidgets::SmallCircleManager`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `(anonymous enum)` | enum | `None` | public | — |
| `SmallCircleManager( GPlatesViewOperations::RenderedGeometryCollection &rendered_geometry_collection, GPlatesAppLogic::ApplicationState &application_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `add_circle( const GPlatesMaths::SmallCircle &small_circle)` | method | `void` | public | — |
| `handle_add()` | method | `void` | public | — |
| `handle_remove()` | method | `void` | public | — |
| `handle_circle_added()` | method | `void` | public | — |
| `handle_remove_all()` | method | `void` | public | — |
| `handle_item_selection_changed()` | method | `void` | public | — |
| `update_buttons()` | method | `void` | public | — |
| `d_small_circle_layer` | field | `GPlatesViewOperations::RenderedGeometryLayer` | public | — |
| `d_create_small_circle_dialog_ptr` | field | `CreateSmallCircleDialog` | public | — |
| `d_small_circle_collection` | field | `std::vector<GPlatesMaths::SmallCircle>` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `remove_row( int row, std::vector<GPlatesMaths::SmallCircle> &small_circle_collection, QTableWidget *table_widget)` | function | `void` | — |
| `remove_rows( std::vector<GPlatesMaths::SmallCircle> &small_circle_collection, QTableWidget *table_widget)` | function | `void` | This removes contiguous rows from a QTableWidget specified by the the table widget's selectedRanges() function. |
| `small_circles_are_approximately_equal( const GPlatesMaths::SmallCircle &c1, const GPlatesMaths::SmallCircle &c2)` | function | `bool` | — |
| `collection_contains( const std::vector<GPlatesMaths::SmallCircle> &small_circle_collection, const GPlatesMaths::SmallCircle &small_circle)` | function | `bool` | — |
| `update_layer( GPlatesViewOperations::RenderedGeometryLayer *layer, const std::vector<GPlatesMaths::SmallCircle> &small_circles)` | function | `void` | — |
| `update_table( QTableWidget *table_widget, const std::vector<GPlatesMaths::SmallCircle> &small_circles)` | function | `void` | — |
| `GPLATES_QTWIDGETS_SMALLCIRCLEMANAGER_H` | macro | `None` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SmallCircleManager` | `QDialog` | Small Circle Manager | 7 |

**Qt signal/slot connections** (5 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `button_add` | `clicked()` | `this` | `handle_add()` |
| `button_remove` | `clicked()` | `this` | `handle_remove()` |
| `d_create_small_circle_dialog_ptr` | `circle_added()` | `this` | `handle_circle_added()` |
| `button_remove_all` | `clicked()` | `this` | `handle_remove_all()` |
| `table_circles` | `itemSelectionChanged()` | `this` | `handle_item_selection_changed()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/deprecated/SmallCircleManager.h
python scripts/gpq.py def GPlatesQtWidgets::SmallCircleManager --body
python scripts/gpq.py uses SmallCircleManager --kind class
python scripts/gpq.py hier SmallCircleManager
```
