# Dialogs

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 773 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/controls/Dialogs.h` | C++ | 54 |
| `src/deprecated/controls/Dialogs.cc` | C++ | 55 |

## Overview

A minimal wrapper namespace providing two modal dialogs over wxWidgets' `wxMessageBox`: `ErrorMessage()` displays an error dialog with title, message, and result text in two sections; `InfoMessage()` displays a simpler informational dialog with only title and message. Both dialogs have a single OK button.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_CONTROLS_DIALOGS_H_` | macro | `None` | — |
| `ErrorMessage(const char* title, const char* message, const char* result)` | function | `void` | Present an error dialog with the given title, message and result, with a single OK button for them to click. |
| `InfoMessage(const char *title, const char *message)` | function | `void` | Present an informational dialog with the given title and message, with a single OK button for them to click. |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/controls/Dialogs.h
```
