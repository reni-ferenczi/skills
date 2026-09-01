# LinkWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 916 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/LinkWidget.h` | C++ | 108 |
| `src/qt-widgets/LinkWidget.cc` | C++ | 128 |

## Overview

[[[PROSE overview unit=qt-widgets/LinkWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::LinkWidget`](#gplatesqtwidgetslinkwidget) | class | `QWidget` | — | 0 | LinkWidget wraps around a QLabel and provides a simple interface to have a clean-looking link that can be placed into the user interface. |

## Members

### `GPlatesQtWidgets::LinkWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LinkWidget( const QString &link_text, QWidget *parent_ = NULL)` | constructor | `None` | public | Constructs a LinkWidget with the given link\_text as the text displayed in the link. |
| `LinkWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | Constructs a blank LinkWidget. |
| `set_link_text( const QString &link_text)` | method | `void` | public | — |
| `link_activated()` | method | `void` | public | Emitted when the user clicks on the link. |
| `event( QEvent *ev)` | method | `bool` | protected | — |
| `handle_link_activated()` | method | `void` | private | — |
| `init()` | method | `void` | private | — |
| `update_internal_label()` | method | `void` | private | — |
| `d_internal_label` | field | `QLabel` | private | — |
| `d_link_text` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `LINK_TEMPLATE` | variable | `char` | — |
| `GPLATES_QTWIDGETS_LINKWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/LinkWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ReconstructLayerOptionsWidget](ReconstructLayerOptionsWidget.md) | qt-widgets | 7 |
| [qt-widgets/ReconstructionLayerOptionsWidget](ReconstructionLayerOptionsWidget.md) | qt-widgets | 5 |
| [qt-widgets/VisualLayerWidget](VisualLayerWidget.md) | qt-widgets | 5 |
| [qt-widgets/RemappedColourPaletteWidget](RemappedColourPaletteWidget.md) | qt-widgets | 3 |
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 3 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 3 |

## Related

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_internal_label` | `linkActivated(const QString &)` | `this` | `handle_link_activated()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/LinkWidget.h
python scripts/gpq.py def GPlatesQtWidgets::LinkWidget --body
python scripts/gpq.py uses LinkWidget --kind class
python scripts/gpq.py hier LinkWidget
```
