# ProjectionException

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ProjectionException.h` | C++ | 77 |

## Overview

A `GuiException` subclass for errors in map projection operations. Thrown when projection calculations fail—for example, when a map view encounters invalid parameters or cannot compute a coordinate transformation. The exception stores a message string describing the problem and is caught by map projection, map grid, and other projection-related code to handle errors gracefully.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::ProjectionException`](#gplatesguiprojectionexception) | class | [`GuiException`](GuiException.md) | — | 0 | A projection error exception. |

## Members

### `GPlatesGui::ProjectionException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ProjectionException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | in which the problem occurs. |
| `~ProjectionException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_PROJECTIONEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/MapProjection](MapProjection.md) | gui | 5 |
| [gui/MapGrid](MapGrid.md) | gui | 3 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 3 |
| [gui/MapBackground](MapBackground.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ProjectionException.h
python scripts/gpq.py def GPlatesGui::ProjectionException --body
python scripts/gpq.py uses ProjectionException --kind class
python scripts/gpq.py hier ProjectionException
```
