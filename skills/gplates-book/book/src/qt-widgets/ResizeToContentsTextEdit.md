# ResizeToContentsTextEdit

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1452 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ResizeToContentsTextEdit.h` | C++ | 98 |
| `src/qt-widgets/ResizeToContentsTextEdit.cc` | C++ | 129 |

## Overview

[[[PROSE overview unit=qt-widgets/ResizeToContentsTextEdit tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ResizeToContentsTextEdit`](#gplatesqtwidgetsresizetocontentstextedit) | class | `QTextEdit` | — | 0 | A QTextEdit that resizes to its contents (via overriding sizeHints and minimumSizeHints). |

## Members

### `GPlatesQtWidgets::ResizeToContentsTextEdit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ResizeToContentsTextEdit( QWidget* parent_ = NULL, bool resize_to_contents_width = false, bool resize_to_contents_height = true)` | constructor | `None` | public | Resized only to contents \*height\* by default. |
| `ResizeToContentsTextEdit( const QString &text_, QWidget* parent_ = NULL, bool resize_to_contents_width = false, bool resize_to_contents_height = true)` | constructor | `None` | public | Resized only to contents \*height\* by default. |
| `sizeHint()` | method | `QSize` | public | — |
| `minimumSizeHint()` | method | `QSize` | public | — |
| `fit_to_document_width()` | method | `void` | public | — |
| `fit_to_document_height()` | method | `void` | public | — |
| `fit_to_document()` | method | `void` | public | — |
| `d_fitted_width` | field | `boost::optional<int>` | private | — |
| `d_fitted_height` | field | `boost::optional<int>` | private | — |
| `initialise( bool resize_to_contents_width, bool resize_to_contents_height)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_RESIZETOCONTENTSTEXTEDIT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ResizeToContentsTextEdit tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 1 |
| [qt-widgets/CreateFeaturePropertiesPage](CreateFeaturePropertiesPage.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `this` | `textChanged()` | `this` | `fit_to_document()` |
| `this` | `textChanged()` | `this` | `fit_to_document_width()` |
| `this` | `textChanged()` | `this` | `fit_to_document_height()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ResizeToContentsTextEdit.h
python scripts/gpq.py def GPlatesQtWidgets::ResizeToContentsTextEdit --body
python scripts/gpq.py uses ResizeToContentsTextEdit --kind class
python scripts/gpq.py hier ResizeToContentsTextEdit
```
