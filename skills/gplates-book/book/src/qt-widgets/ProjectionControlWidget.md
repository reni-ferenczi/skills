# ProjectionControlWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1013 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ProjectionControlWidget.h` | C++ | 92 |
| `src/qt-widgets/ProjectionControlWidget.cc` | C++ | 171 |
| `src/qt-widgets/ProjectionControlWidgetUi.ui` | Qt form | 58 |

## Overview

[[[PROSE overview unit=qt-widgets/ProjectionControlWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ProjectionControlWidget`](#gplatesqtwidgetsprojectioncontrolwidget) | class | `QWidget`<br>`Ui_ProjectionControlWidget` | — | 0 | Small widget with combobox, to let the user switch projections. |

## Members

### `GPlatesQtWidgets::ProjectionControlWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ProjectionControlWidget( GPlatesGui::ViewportProjection &viewport_projection, QWidget *parent_)` | constructor | `None` | public | — |
| `handle_combobox_changed( int idx)` | method | `void` | private | — |
| `handle_shortcut_triggered()` | method | `void` | private | — |
| `handle_projection_type_changed( const GPlatesGui::ViewportProjection &)` | method | `void` | public | — |
| `show_label( bool show_)` | method | `void` | public | — |
| `d_viewport_projection` | field | `GPlatesGui::ViewportProjection` | private | — |
| `add_projection( const QString &projection_text, GPlatesGui::MapProjection::Type projection_type, const QString &shortcut_key_sequence)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_PROJECTIONCONTROLWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ProjectionControlWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ProjectionControlWidget` | `QWidget` | Form | 3 |

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `combo_projections` | `activated(int)` | `this` | `handle_combobox_changed(int)` |
| `&d_viewport_projection` | `projection_type_changed(const GPlatesGui::ViewportProjection &)` | `this` | `handle_projection_type_changed(const GPlatesGui::ViewportProjection &)` |
| `shortcut_action` | `triggered()` | `this` | `handle_shortcut_triggered()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ProjectionControlWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ProjectionControlWidget --body
python scripts/gpq.py uses ProjectionControlWidget --kind class
python scripts/gpq.py hier ProjectionControlWidget
```
