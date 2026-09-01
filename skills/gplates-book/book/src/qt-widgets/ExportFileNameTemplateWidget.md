# ExportFileNameTemplateWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1025 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ExportFileNameTemplateWidget.h` | C++ | 84 |
| `src/qt-widgets/ExportFileNameTemplateWidget.cc` | C++ | 109 |
| `src/qt-widgets/ExportFileNameTemplateWidgetUi.ui` | Qt form | 190 |

## Overview

[[[PROSE overview unit=qt-widgets/ExportFileNameTemplateWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ExportFileNameTemplateWidget`](#gplatesqtwidgetsexportfilenametemplatewidget) | class | `QWidget`<br>`Ui_ExportFileNameTemplateWidget` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ExportFileNameTemplateWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportFileNameTemplateWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `clear_file_name_template()` | method | `void` | public | Clears the filename template field. |
| `set_file_name_template( const QString &file_name_template, GPlatesGui::ExportAnimationType::Format export_format)` | method | `void` | public | Sets the filename template field. |
| `get_file_name_template()` | method | `QString` | public | Returns the filename template (base name and extension). |
| `focus_on_line_edit_filename()` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `set_fixed_size_for_item_view( QAbstractItemView *view)` | function | `void` | — |
| `GPLATES_QTWIDGETS_EXPORTFILENAMETEMPLATEWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ExportFileNameTemplateWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ConfigureExportParametersDialog](ConfigureExportParametersDialog.md) | qt-widgets | 5 |
| [qt-widgets/EditExportParametersDialog](EditExportParametersDialog.md) | qt-widgets | 5 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ExportFileNameTemplateWidget` | `QWidget` | File Name Template | 8 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ExportFileNameTemplateWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ExportFileNameTemplateWidget --body
python scripts/gpq.py uses ExportFileNameTemplateWidget --kind class
python scripts/gpq.py hier ExportFileNameTemplateWidget
```
