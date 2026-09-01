# GuiException

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GuiException.h` | C++ | 49 |

## Overview

[[[PROSE overview unit=gui/GuiException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GuiException`](#gplatesguiguiexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 1 | The (pure virtual) base class of all GUI exceptions. |

## Members

### `GPlatesGui::GuiException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GuiException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GUI_GUIEXCEPTION_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/GuiException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ProjectionException](ProjectionException.md) | gui | 3 |
| [opengl/GLMapCubeMeshGenerator](../opengl/GLMapCubeMeshGenerator.md) | opengl | 2 |
| [qt-widgets/SetProjectionDialog](../qt-widgets/SetProjectionDialog.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/GuiException.h
python scripts/gpq.py def GPlatesGui::GuiException --body
python scripts/gpq.py uses GuiException --kind class
python scripts/gpq.py hier GuiException
```
