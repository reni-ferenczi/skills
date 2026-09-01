# PythonArgumentWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 111 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PythonArgumentWidget.h` | C++ | 284 |

## Overview

[[[PROSE overview unit=qt-widgets/PythonArgumentWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PythonArgumentWidget`](#gplatesqtwidgetspythonargumentwidget) | class | `QWidget` | — | 3 | — |
| [`GPlatesQtWidgets::PythonArgDefaultWidget`](#gplatesqtwidgetspythonargdefaultwidget) | class | [`PythonArgumentWidget`](PythonArgumentWidget.md) | — | 0 | — |
| [`GPlatesQtWidgets::PythonArgColorWidget`](#gplatesqtwidgetspythonargcolorwidget) | class | [`PythonArgumentWidget`](PythonArgumentWidget.md) | — | 0 | — |
| [`GPlatesQtWidgets::PythonArgPaletteWidget`](#gplatesqtwidgetspythonargpalettewidget) | class | [`PythonArgumentWidget`](PythonArgumentWidget.md) | — | 0 | — |

## Members

### `GPlatesQtWidgets::PythonArgumentWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonArgumentWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `configuration_changed()` | method | `void` | public | — |

### `GPlatesQtWidgets::PythonArgDefaultWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonArgDefaultWidget( GPlatesGui::PythonCfgItem* cfg_item, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_string_changed( const QString& str)` | method | `void` | private | — |
| `handle_editing_finished()` | method | `void` | private | — |
| `d_cfg_item` | field | `GPlatesGui::PythonCfgItem` | private | — |

### `GPlatesQtWidgets::PythonArgColorWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonArgColorWidget( GPlatesGui::PythonCfgItem* cfg_item, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_choose_button_clicked(bool b)` | method | `void` | private | — |
| `handle_color_name_changed(const QString& _color_name)` | method | `void` | private | — |
| `hboxLayout` | field | `QHBoxLayout` | private | — |
| `color_name` | field | `QLineEdit` | private | — |
| `choose_button` | field | `QPushButton` | private | — |
| `d_cfg_item` | field | `GPlatesGui::PythonCfgItem` | private | — |

### `GPlatesQtWidgets::PythonArgPaletteWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonArgPaletteWidget( GPlatesGui::PythonCfgItem* cfg_item, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `handle_choose_button_clicked(bool b)` | method | `void` | private | — |
| `handle_reload_button_clicked(bool b)` | method | `void` | private | — |
| `hboxLayout` | field | `QHBoxLayout` | private | — |
| `line_edit` | field | `QLineEdit` | private | — |
| `choose_button` | field | `QPushButton` | private | — |
| `reload_button` | field | `QPushButton` | private | — |
| `spacer` | field | `QSpacerItem` | private | — |
| `d_last_open_directory` | field | `QString` | private | — |
| `d_cfg_item` | field | `GPlatesGui::PythonCfgItem` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_PYTHONARGUMENTWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/PythonArgumentWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditStringWidget](EditStringWidget.md) | qt-widgets | 7 |
| [qt-widgets/DrawStyleDialog](DrawStyleDialog.md) | qt-widgets | 5 |

## Related

**Qt signal/slot connections** (6 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `line_edit` | `textChanged(const QString&)` | `this` | `handle_string_changed(const QString&)` |
| `line_edit` | `editingFinished()` | `this` | `handle_editing_finished()` |
| `color_name` | `textChanged(const QString&)` | `this` | `handle_color_name_changed(const QString&)` |
| `choose_button` | `clicked(bool)` | `this` | `handle_choose_button_clicked(bool)` |
| `choose_button` | `clicked(bool)` | `this` | `handle_choose_button_clicked(bool)` |
| `reload_button` | `clicked(bool)` | `this` | `handle_reload_button_clicked(bool)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PythonArgumentWidget.h
python scripts/gpq.py def GPlatesQtWidgets::PythonArgPaletteWidget --body
python scripts/gpq.py uses PythonArgPaletteWidget --kind class
python scripts/gpq.py hier PythonArgPaletteWidget
```
