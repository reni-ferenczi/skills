# FriendlyLineEdit

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 157 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/FriendlyLineEdit.h` | C++ | 210 |
| `src/qt-widgets/FriendlyLineEdit.cc` | C++ | 258 |

## Overview

[[[PROSE overview unit=qt-widgets/FriendlyLineEdit tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::FriendlyLineEditInternals::InternalLineEdit`](#gplatesqtwidgetsfriendlylineeditinternalsinternallineedit) | class | `QLineEdit` | — | 0 | — |
| [`GPlatesQtWidgets::FriendlyLineEdit`](#gplatesqtwidgetsfriendlylineedit) | class | `QWidget` | — | 2 | FriendlyLineEdit wraps around a QLineEdit and displays a custom string in the line edit when the logical contents of the line edit is the empty string; this custom string is displayed in grey and italics. |

## Members

### `GPlatesQtWidgets::FriendlyLineEditInternals::InternalLineEdit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InternalLineEdit( const QString &message_on_empty_string, const boost::function<void (QFocusEvent *)> &parent_focus_in_event_function, const boost::function<void (QFocusEvent *)> &parent_focus_out_event_function, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `text()` | method | `QString` | public | text is not virtual but we'll override it anyway. |
| `setText( const QString &)` | method | `void` | public | setText is not virtual but we'll override it anyway. |
| `focusInEvent( QFocusEvent *event)` | method | `void` | protected | — |
| `focusOutEvent( QFocusEvent *event)` | method | `void` | protected | — |
| `handle_focus_in()` | method | `void` | private | — |
| `handle_focus_out()` | method | `void` | private | — |
| `d_message_on_empty_string` | field | `QString` | private | — |
| `d_parent_focus_in_event_function` | field | `boost::function<void (QFocusEvent *)>` | private | — |
| `d_parent_focus_out_event_function` | field | `boost::function<void (QFocusEvent *)>` | private | — |
| `d_default_palette` | field | `QPalette` | private | — |
| `d_empty_string_palette` | field | `QPalette` | private | — |
| `d_default_font` | field | `QFont` | private | — |
| `d_empty_string_font` | field | `QFont` | private | — |
| `d_is_empty_string` | field | `bool` | private | — |

### `GPlatesQtWidgets::FriendlyLineEdit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FriendlyLineEdit( const QString &contents = QString(), const QString &message_on_empty_string = QString(), QWidget *parent_ = NULL)` | constructor | `None` | public | Constructs a FriendlyLineEdit. |
| `text()` | method | `QString` | public | Using Qt naming conventions here. |
| `setText( const QString& text)` | method | `void` | public | — |
| `isReadOnly()` | method | `bool` | public | — |
| `setReadOnly( bool read_only)` | method | `void` | public | — |
| `setValidator( const QValidator *v)` | method | `void` | public | — |
| `validator()` | method | `QValidator` | public | — |
| `setAlignment( Qt::Alignment flag)` | method | `void` | public | — |
| `alignment()` | method | `Qt::Alignment` | public | — |
| `setLineEditSizePolicy( QSizePolicy policy)` | method | `void` | public | — |
| `lineEditSizePolicy()` | method | `QSizePolicy` | public | — |
| `editingFinished()` | method | `void` | public | Using Qt naming conventions here. |
| `textEdited( const QString &text_)` | method | `void` | public | — |
| `handle_text_edited( const QString &text_)` | method | `void` | protected | — |
| `focusInEvent( QFocusEvent *event_)` | method | `void` | protected | — |
| `handle_internal_line_edit_editing_finished()` | method | `void` | private | — |
| `handle_internal_line_edit_text_edited( const QString &text_)` | method | `void` | private | — |
| `d_line_edit` | field | `FriendlyLineEditInternals::InternalLineEdit` | private | The line edit that we wrap around. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_FRIENDLYLINEEDIT_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/FriendlyLineEdit tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 33 |
| [qt-widgets/RemappedColourPaletteWidget](RemappedColourPaletteWidget.md) | qt-widgets | 12 |
| [qt-widgets/ScalarField3DDepthLayersPage](ScalarField3DDepthLayersPage.md) | qt-widgets | 12 |
| [qt-widgets/TimeDependentRasterPage](TimeDependentRasterPage.md) | qt-widgets | 12 |
| [qt-widgets/RasterPropertiesDialog](RasterPropertiesDialog.md) | qt-widgets | 6 |

## Related

**Qt signal/slot connections** (2 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_line_edit` | `editingFinished()` | `this` | `handle_internal_line_edit_editing_finished()` |
| `d_line_edit` | `textEdited(const QString &)` | `this` | `handle_internal_line_edit_text_edited(const QString &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/FriendlyLineEdit.h
python scripts/gpq.py def GPlatesQtWidgets::FriendlyLineEdit --body
python scripts/gpq.py uses FriendlyLineEdit --kind class
python scripts/gpq.py hier FriendlyLineEdit
```
