# ElidedLabel

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 469 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ElidedLabel.h` | C++ | 146 |
| `src/qt-widgets/ElidedLabel.cc` | C++ | 189 |

## Overview

[[[PROSE overview unit=qt-widgets/ElidedLabel tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ElidedLabel`](#gplatesqtwidgetselidedlabel) | class | `QWidget` | — | 0 | ElidedLabel is a widget that can display a piece of text, much like a QLabel. |

## Members

### `GPlatesQtWidgets::ElidedLabel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ElidedLabel( Qt::TextElideMode mode, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `ElidedLabel( const QString &text_, Qt::TextElideMode mode, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_text_elide_mode( Qt::TextElideMode mode)` | method | `void` | public | — |
| `get_text_elide_mode()` | method | `Qt::TextElideMode` | public | — |
| `setText( const QString &text_)` | method | `void` | public | Using Qt naming conventions here. |
| `text()` | method | `QString` | public | — |
| `setFrameStyle( int style_)` | method | `void` | public | — |
| `frameStyle()` | method | `int` | public | — |
| `resizeEvent( QResizeEvent *event_)` | method | `void` | protected | — |
| `paintEvent( QPaintEvent *event_)` | method | `void` | protected | — |
| `InternalLabel` | class | `None` | private | The internal label used to display the elided text. |
| `init()` | method | `void` | private | Initialisation common to both constructors. |
| `update_internal_label()` | method | `void` | private | — |
| `d_internal_label_frame` | field | `QFrame` | private | — |
| `d_internal_label` | field | `InternalLabel` | private | — |
| `d_text` | field | `QString` | private | The current full text. |
| `d_mode` | field | `Qt::TextElideMode` | private | Where the ellipsis should appear when eliding text. |
| `d_internal_label_needs_updating` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_ELIDEDLABEL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ElidedLabel tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayerWidget](VisualLayerWidget.md) | qt-widgets | 13 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ElidedLabel.h
python scripts/gpq.py def GPlatesQtWidgets::ElidedLabel --body
python scripts/gpq.py uses ElidedLabel --kind class
python scripts/gpq.py hier ElidedLabel
```
