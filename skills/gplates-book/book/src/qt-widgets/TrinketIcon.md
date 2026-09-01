# TrinketIcon

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 726 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/TrinketIcon.h` | C++ | 147 |
| `src/qt-widgets/TrinketIcon.cc` | C++ | 89 |

## Overview

An interactive icon widget extending `QLabel` for use in status bars. It wraps a static icon label with mouse event handling and callback support: when clicked (if enabled), it invokes a user-supplied callback function and emits a `clicked` signal. The widget maintains separate pixmaps for normal and pressed states to give visual feedback during interaction. It is primarily used by `TrinketArea` to manage a collection of interactive icons in the application's status bar.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::TrinketIcon`](#gplatesqtwidgetstrinketicon) | class | `QLabel` | — | 0 | This widget is a subclass of QLabel specialising in displaying the icons in the status bar, adding a thin veneer of interactivity to the otherwise static QLabel class. |

## Members

### `GPlatesQtWidgets::TrinketIcon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `clicked_callback_function_type` | typedef | `boost::function<void ()>` | public | Typedef for the callback function object which you can set for the on-click event. |
| `TrinketIcon( const QIcon &icon, const QString &tooltip, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~TrinketIcon()` | destructor | `None` | public | — |
| `setIcon( const QIcon &icon)` | method | `void` | public | — |
| `set_clickable( bool is_clickable)` | method | `void` | public | — |
| `clickable()` | method | `bool` | public | — |
| `clicked_callback_function()` | method | `clicked_callback_function_type` | public | — |
| `set_clicked_callback_function( clicked_callback_function_type f)` | method | `void` | public | — |
| `clicked( GPlatesQtWidgets::TrinketIcon *self, QMouseEvent *ev)` | method | `void` | public | — |
| `mousePressEvent( QMouseEvent *ev)` | method | `void` | protected | — |
| `mouseMoveEvent( QMouseEvent *ev)` | method | `void` | protected | — |
| `mouseReleaseEvent( QMouseEvent *ev)` | method | `void` | protected | — |
| `d_clickable` | field | `bool` | private | Can the user click on this icon to interact with it? |
| `d_clicked_callback` | field | `clicked_callback_function_type` | private | What do we do when clicked? |
| `d_pixmap_normal` | field | `QPixmap` | private | Pixmap for the icon. |
| `d_pixmap_clicking` | field | `QPixmap` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_TRINKETICON_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TrinketArea](../gui/TrinketArea.md) | gui | 18 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/TrinketIcon.h
python scripts/gpq.py def GPlatesQtWidgets::TrinketIcon --body
python scripts/gpq.py uses TrinketIcon --kind class
python scripts/gpq.py hier TrinketIcon
```
