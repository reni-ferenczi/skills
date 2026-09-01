# SelectionWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 553 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SelectionWidget.h` | C++ | 273 |
| `src/qt-widgets/SelectionWidget.cc` | C++ | 193 |

## Overview

[[[PROSE overview unit=qt-widgets/SelectionWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SelectionWidget`](#gplatesqtwidgetsselectionwidget) | class | `QWidget` | — | 0 | SelectionWidget is a widget that unifies QListWidget and QComboBox, providing the user with a mechanism to make one choice out of a possible many. |

## Members

### `GPlatesQtWidgets::SelectionWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DisplayWidget` | enum | `None` | public | — |
| `SelectionWidget( DisplayWidget display_widget, QWidget *parent_ = NULL)` | constructor | `None` | public | Creates a SelectionWidget that encapsulates either a QListWidget or a QComboBox, depending on the value of display\_widget. |
| `add_item( const QString &display_text, typename GPlatesUtils::TypeTraits<T>::argument_type user_data)` | method | `void` | public | Appends an item to the selections available. |
| `clear()` | method | `void` | public | Removes all items. |
| `get_count()` | method | `int` | public | Returns the number of items. |
| `get_current_index()` | method | `int` | public | Returns the index of the currently selected item. |
| `set_current_index( int index)` | method | `void` | public | Sets the selected index to be index. |
| `get_data( int index)` | method | `boost::optional<T>` | public | Returns the data at the given index. |
| `find_text( const QString &text, Qt::MatchFlags flags = Qt::MatchExactly \| Qt::MatchCaseSensitive)` | method | `int` | public | Returns the index of the item containing the given text. |
| `find_data( typename GPlatesUtils::TypeTraits<T>::argument_type user_data)` | method | `int` | public | Returns the index of the item containing the given user\_data. |
| `item_activated( int index)` | method | `void` | public | Emitted when the user clicks or double clicks on an item (depending on system configuration) and when the user presses the activation key. |
| `current_index_changed( int index)` | method | `void` | public | Emitted when the current index changes either through user interaction or programmatically. |
| `focusInEvent( QFocusEvent *ev)` | method | `void` | protected | — |
| `handle_listwidget_item_activated( QListWidgetItem *item)` | method | `void` | private | — |
| `handle_listwidget_current_row_changed( int current_row)` | method | `void` | private | — |
| `handle_combobox_current_index_changed( int index)` | method | `void` | private | — |
| `InternalListWidget` | class | `None` | private | — |
| `d_listwidget` | field | `InternalListWidget` | private | Precisely one of d\_listwidget and d\_combobox is non-NULL. |
| `d_combobox` | field | `QComboBox` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_SELECTIONWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/SelectionWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ChooseFeatureTypeWidget](ChooseFeatureTypeWidget.md) | qt-widgets | 16 |
| [qt-widgets/ChoosePropertyWidget](ChoosePropertyWidget.md) | qt-widgets | 15 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 4 |
| [qt-widgets/ChangeFeatureTypeDialog](ChangeFeatureTypeDialog.md) | qt-widgets | 2 |
| [qt-widgets/ChangePropertyWidget](ChangePropertyWidget.md) | qt-widgets | 2 |

## Related

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_listwidget` | `itemActivated(QListWidgetItem *)` | `this` | `handle_listwidget_item_activated(QListWidgetItem *)` |
| `d_listwidget` | `currentRowChanged(int)` | `this` | `handle_listwidget_current_row_changed(int)` |
| `d_combobox` | `currentIndexChanged(int)` | `this` | `handle_combobox_current_index_changed(int)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SelectionWidget.h
python scripts/gpq.py def GPlatesQtWidgets::SelectionWidget --body
python scripts/gpq.py uses SelectionWidget --kind class
python scripts/gpq.py hier SelectionWidget
```
