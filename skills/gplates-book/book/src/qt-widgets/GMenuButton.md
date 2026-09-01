# GMenuButton

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1599 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/GMenuButton.h` | C++ | 78 |
| `src/qt-widgets/GMenuButton.cc` | C++ | 52 |
| `src/qt-widgets/GMenuButtonUi.ui` | Qt form | 68 |

## Overview

A widget that provides menu access in full-screen mode when the main menubar is hidden. It contains a button that displays a dropdown menu mirroring the main menu bar's top-level menus, allowing users to access menu items and keyboard shortcuts without the menubar visible.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::GMenuButton`](#gplatesqtwidgetsgmenubutton) | class | `QWidget`<br>`Ui_GMenuButton` | — | 0 | This button appears in the main window during full-screen mode. |

## Members

### `GPlatesQtWidgets::GMenuButton`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GMenuButton( GPlatesQtWidgets::ViewportWindow &main_window, QWidget *parent_)` | constructor | `None` | public | — |
| `~GMenuButton()` | destructor | `None` | public | — |
| `d_menu_ptr` | field | `QMenu` | private | This is the menu that pops up when you click the GMenuButton. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_GMENUBUTTON_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 3 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `GMenuButton` | `QWidget` | GMenu | 2 |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/GMenuButton.h
python scripts/gpq.py def GPlatesQtWidgets::GMenuButton --body
python scripts/gpq.py uses GMenuButton --kind class
python scripts/gpq.py hier GMenuButton
```
