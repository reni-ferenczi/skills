# LogFilterModel

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 814 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/LogFilterModel.h` | C++ | 116 |
| `src/gui/LogFilterModel.cc` | C++ | 167 |

## Overview

[[[PROSE overview unit=gui/LogFilterModel tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::LogFilterModel`](#gplatesguilogfiltermodel) | class | `QSortFilterProxyModel`<br>`boost::noncopyable` | — | 0 | Qt Model/View filter model - this sits between the app-logic LogModel and the LogDialog and provides filtering of log entries. |

## Members

### `GPlatesGui::LogFilterModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LogFilterModel( QObject *_parent)` | constructor | `None` | public | — |
| `~LogFilterModel()` | destructor | `None` | public | — |
| `data( const QModelIndex &idx, int role = Qt::DisplayRole)` | method | `QVariant` | public | Reimplementation of QSortFilterProxyModel::data(). |
| `set_filter( const QString &filter_text, bool show_debug_messages, bool show_warning_messages, bool show_critical_messages)` | method | `void` | public | — |
| `filterAcceptsRow( int source_row, const QModelIndex &source_parent)` | method | `bool` | protected | Reimplementation of QSortFilterProxyModel::filterAcceptsRow(). |
| `matches_severity_filters( const GPlatesAppLogic::LogModel::LogEntry::Severity entry_severity)` | method | `bool` | protected | Used by filterAcceptsRow(). |
| `matches_text_filter( const QString &row_text)` | method | `bool` | protected | Used by filterAcceptsRow(). |
| `d_show_debug_messages` | field | `bool` | private | — |
| `d_show_warning_messages` | field | `bool` | private | — |
| `d_show_critical_messages` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_LOGFILTERMODEL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/LogFilterModel tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/LogDialog](../qt-widgets/LogDialog.md) | qt-widgets | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/LogFilterModel.h
python scripts/gpq.py def GPlatesGui::LogFilterModel --body
python scripts/gpq.py uses LogFilterModel --kind class
python scripts/gpq.py hier LogFilterModel
```
