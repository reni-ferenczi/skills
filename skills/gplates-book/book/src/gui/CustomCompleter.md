# CustomCompleter

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 771 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/CustomCompleter.h` | C++ | 71 |
| `src/gui/CustomCompleter.cc` | C++ | 94 |

## Overview

A `QCompleter` subclass that customizes completion behaviour for two-column models. The completer maintains a two-column model where the first column holds raw completion text and the second holds display text; the popup is configured as a custom `QTreeView` that hides the first column at zero width while maintaining proper focus behaviour. The `splitPath()` method returns the trimmed user input as-is, and `pathFromIndex()` extracts the `EditRole` text from the model for insertion.

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

The first column must remain visible (at zero width) rather than being hidden via `setSectionHidden()`, because `QCompleter` only navigates the zero-th column; hiding it breaks keyboard navigation. Column expansion is controlled via header resize modes to prevent user interaction.

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
