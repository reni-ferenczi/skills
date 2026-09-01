# DigitisationUndoParadoxException

[Book TOC](../../../TOC.md) · [qt-widgets](../../../components/qt-widgets.md) · cluster Community 6 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/deprecated/DigitisationUndoParadoxException.h` | C++ | 98 |

## Overview

[[[PROSE overview unit=qt-widgets/deprecated/DigitisationUndoParadoxException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::DigitisationUndoParadoxException`](#gplatesqtwidgetsdigitisationundoparadoxexception) | class | [`GPlatesGlobal::AssertionFailureException`](../../global/AssertionFailureException.md) | — | 0 | An AssertionFailureException that indicates a paradox has occurred in the DigitisationWidget's QUndoStack - an undo command previously pushed onto the stack has been undone, but encountered a situation which should not exist e.g:- 1. |

## Members

### `GPlatesQtWidgets::DigitisationUndoParadoxException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DigitisationUndoParadoxException( const char *filename_, int line_num_)` | constructor | `None` | public | FIXME: Ideally, we'd be tracking the call stack etc, and also supplying some sort of function object that might be used to do damage control for the program should such an exception be thrown. |
| `~DigitisationUndoParadoxException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_DIGITISATIONUNDOPARADOXEXCEPTION_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/deprecated/DigitisationUndoParadoxException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/deprecated/DigitisationUndoParadoxException.h
python scripts/gpq.py def GPlatesQtWidgets::DigitisationUndoParadoxException --body
python scripts/gpq.py uses DigitisationUndoParadoxException --kind class
python scripts/gpq.py hier DigitisationUndoParadoxException
```
