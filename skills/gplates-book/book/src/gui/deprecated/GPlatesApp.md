# GPlatesApp

[Book TOC](../../../TOC.md) · [gui](../../../components/gui.md) · cluster Community 215 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/deprecated/GPlatesApp.h` | C++ | 56 |
| `src/gui/deprecated/GPlatesApp.cc` | C++ | 147 |

## Overview

[[[PROSE overview unit=gui/deprecated/GPlatesApp tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::GPlatesApp`](#gplatesguigplatesapp) | class | `wxApp` | — | 0 | — |

## Members

### `GPlatesGui::GPlatesApp`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `OnInit()` | method | `bool` | public | This function is called by wxWindows during the application's start-up ("initialisation") phase. |
| `OnExit()` | method | `int` | public | — |
| `d_main_win` | field | `MainWindow` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `fix_mesa_bug()` | function | `void` | Set the MESA\_NO\_SSE environment variable to 1 to circumvent a Mesa bug described at http://www.geosci.usyd.edu.au/users/hlaw/pmwiki/pmwiki.php?pagename=Main.NurbsBug This will have no effect on systems that do not have this bug, nor on ... |
| `GPLATES_GUI_GPLATESAPP_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/deprecated/GPlatesApp tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [maths/deprecated/PolylineIntersections_test](../../maths/deprecated/PolylineIntersections_test.md) | maths | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/deprecated/GPlatesApp.h
python scripts/gpq.py def GPlatesGui::GPlatesApp --body
python scripts/gpq.py uses GPlatesApp --kind class
python scripts/gpq.py hier GPlatesApp
```
