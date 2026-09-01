# GuiException

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/GuiException.h` | C++ | 49 |

## Overview

A marker exception class for GUI-related errors. All GUI exceptions inherit from this class, which itself inherits from `GPlatesGlobal::Exception`. This provides a consistent way to catch and handle GUI-specific failures throughout the application.

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

*None.*

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
