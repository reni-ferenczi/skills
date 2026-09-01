# ConfigValueEditorWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 641 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConfigValueEditorWidget.h` | C++ | 88 |
| `src/qt-widgets/ConfigValueEditorWidget.cc` | C++ | 76 |

## Overview

[[[PROSE overview unit=qt-widgets/ConfigValueEditorWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ConfigValueEditorWidget`](#gplatesqtwidgetsconfigvalueeditorwidget) | class | `QWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ConfigValueEditorWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConfigValueEditorWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ConfigValueEditorWidget()` | destructor | `None` | public | — |
| `wants_reset()` | method | `bool` | public | Has the user clicked the reset button on this editor? |
| `reset_requested( QWidget *editor)` | method | `void` | public | This widget wants to reset to the default value and close the editor, please. editor is set to 'this', to support a connection to ConfigValueDelegate::closeEditor(). |
| `handle_reset()` | method | `void` | private | Reset button has been clicked(), re-emit as our own custom signal. |
| `d_wants_reset` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CONFIGVALUEEDITORWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ConfigValueEditorWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ConfigValueDelegate](../gui/ConfigValueDelegate.md) | gui | 10 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `reset_button` | `clicked()` | `this` | `handle_reset()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ConfigValueEditorWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ConfigValueEditorWidget --body
python scripts/gpq.py uses ConfigValueEditorWidget --kind class
python scripts/gpq.py hier ConfigValueEditorWidget
```
