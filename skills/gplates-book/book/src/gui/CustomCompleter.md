# CustomCompleter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 771 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/CustomCompleter.h` | C++ | 71 |
| `src/gui/CustomCompleter.cc` | C++ | 94 |

## Overview

[[[PROSE overview unit=gui/CustomCompleter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ModelColumnName`](#anonymousmodelcolumnname) | enum | — | — | 0 | — |
| [`GPlatesGui::CustomCompleter`](#gplatesguicustomcompleter) | class | `QCompleter` | — | 0 | We subclass QCompleter to get at the two protected virtual methods, splitPath and pathFromIndex. |

## Members

### `(anonymous)::ModelColumnName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MODEL_COLUMN_COMPLETION` | enumerator | `None` | — | — |
| `MODEL_COLUMN_POPUP` | enumerator | `None` | — | — |

### `GPlatesGui::CustomCompleter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CustomCompleter( QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `set_custom_popup()` | method | `void` | public | — |
| `splitPath( const QString &path)` | method | `QStringList` | protected | Seems to only get called as the user is typing, and then only to split up what they typed, not the model data. |
| `pathFromIndex( const QModelIndex &idx)` | method | `QString` | protected | Seems to only get called once some entry is selected to generate the final text that gets inserted. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_CUSTOMCOMPLETER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/CustomCompleter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/Completionist](Completionist.md) | gui | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/CustomCompleter.h
python scripts/gpq.py def GPlatesGui::CustomCompleter --body
python scripts/gpq.py uses CustomCompleter --kind class
python scripts/gpq.py hier CustomCompleter
```
