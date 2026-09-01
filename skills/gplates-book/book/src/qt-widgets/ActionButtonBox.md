# ActionButtonBox

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1446 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ActionButtonBox.h` | C++ | 100 |
| `src/qt-widgets/ActionButtonBox.cc` | C++ | 95 |

## Overview

`ActionButtonBox` turns a set of `QAction` objects into a row (or grid) of icon
buttons without requiring a Qt Designer `.ui` form: it builds its own
`QGridLayout` by hand and hands out a fresh `QToolButton` per `add_action()`
call, wiring each button to its action with `setDefaultAction()` so the button
tracks the action's enabled state, icon and tooltip automatically. `next_cell()`
walks the grid left to right, wrapping to a new row every `d_num_columns`
buttons.

It is used wherever a dock or panel needs a compact strip of toolbar-style
buttons alongside a widget rather than in the main toolbar, such as
`TaskPanel` and `TopologySectionsTable`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ActionButtonBox`](#gplatesqtwidgetsactionbuttonbox) | class | `QWidget` | — | 0 | A lightweight reusable box of QActions, each triggered by a QToolButton and automatically laid out in a grid arrangement. |

## Members

### `GPlatesQtWidgets::ActionButtonBox`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ActionButtonBox( int num_columns, int default_icon_size, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `add_action( QAction *action_ptr)` | method | `void` | public | Adds a new QToolButton linked to the given action\_ptr . |
| `next_cell()` | method | `void` | private | Adjusts d\_next\_row and d\_next\_col to point to the next grid cell in the sequence. |
| `d_num_columns` | field | `int` | private | How many columns should be used for the grid layout. |
| `d_default_icon_size` | field | `int` | private | The default width and height of icons for the QToolButtons, in pixels. |
| `d_layout_ptr` | field | `QGridLayout` | private | The layout for this ActionButtonBox. |
| `d_next_row` | field | `int` | private | The next empty grid cell's row number. |
| `d_next_col` | field | `int` | private | The next empty grid cell's column number. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_ACTIONBUTTONBOX_H` | macro | `None` | — |

## Notes

Neither `ActionButtonBox` nor the `QToolButton` it creates takes ownership of
the `QAction` passed to `add_action()` — the caller must keep the action
alive. `add_action()` explicitly clears the button's shortcut
(`setShortcut(QKeySequence())`) because `setDefaultAction()` otherwise copies
the action's mnemonic onto the button, which fights with the same mnemonic on
the action's menu item elsewhere in the UI; this assumes every action added
here is already reachable from a menu.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 7 |
| [qt-widgets/DigitisationWidget](DigitisationWidget.md) | qt-widgets | 5 |
| [qt-widgets/TaskPanel](TaskPanel.md) | qt-widgets | 5 |
| [gui/TopologySectionsTable](../gui/TopologySectionsTable.md) | gui | 4 |
| [qt-widgets/ModifyReconstructionPoleWidget](ModifyReconstructionPoleWidget.md) | qt-widgets | 4 |
| [qt-widgets/TopologyToolsWidget](TopologyToolsWidget.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ActionButtonBox.h
python scripts/gpq.py def GPlatesQtWidgets::ActionButtonBox --body
python scripts/gpq.py uses ActionButtonBox --kind class
python scripts/gpq.py hier ActionButtonBox
```
