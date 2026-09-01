# Lifetime

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 215 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/controls/Lifetime.h` | C++ | 73 |
| `src/deprecated/controls/Lifetime.cc` | C++ | 95 |

## Overview

[[[PROSE overview unit=deprecated/controls/Lifetime tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesControls::Lifetime`](#gplatescontrolslifetime) | class | — | — | 0 | This class is used to control the lifetime of the program. |

## Members

### `GPlatesControls::Lifetime`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `init(GPlatesGui::MainWindow *main_win)` | method | `void` | public | — |
| `instance()` | method | `Lifetime` | public | — |
| `terminate(const std::string &reason)` | method | `void` | public | — |
| `Lifetime()` | constructor | `None` | protected | — |
| `_instance` | field | `Lifetime` | private | — |
| `_is_initialised` | field | `bool` | private | — |
| `_main_win` | field | `GPlatesGui::MainWindow` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_instance` | variable | `GPlatesControls::Lifetime` | — |
| `_is_initialised` | variable | `bool` | — |
| `_main_win` | variable | `GPlatesGui::MainWindow` | — |
| `_GPLATES_CONTROLS_LIFETIME_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=deprecated/controls/Lifetime tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/deprecated/GLCanvas](../../gui/deprecated/GLCanvas.md) | gui | 17 |
| [deprecated/controls/File](File.md) | deprecated | 15 |
| [deprecated/controls/AnimationTimer](AnimationTimer.md) | deprecated | 4 |
| [gui/deprecated/GPlatesApp](../../gui/deprecated/GPlatesApp.md) | gui | 4 |
| [maths/deprecated/PolylineIntersections_test](../../maths/deprecated/PolylineIntersections_test.md) | maths | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/controls/Lifetime.h
python scripts/gpq.py def GPlatesControls::Lifetime --body
python scripts/gpq.py uses Lifetime --kind class
python scripts/gpq.py hier Lifetime
```
