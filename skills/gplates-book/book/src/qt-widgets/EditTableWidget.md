# EditTableWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1791 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/EditTableWidget.h` | C++ | 65 |

## Overview

An abstract interface that table-editing widgets inherit from to handle row insertion and deletion operations. `EditTableActionWidget` instances (which display action buttons in table cells) use this interface to notify the table editor when the user requests to insert a row above, insert a row below, or delete a row. Concrete subclasses override the three pure virtual methods to implement their table-specific row management.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::EditTableWidget`](#gplatesqtwidgetsedittablewidget) | class | — | — | 4 | An abstract base class for classes which will make use of the EditTableActionWidget. |

## Members

### `GPlatesQtWidgets::EditTableWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~EditTableWidget()` | destructor | `None` | public | — |
| `handle_insert_row_above( const EditTableActionWidget *)` | method | `void` | public | — |
| `handle_insert_row_below( const EditTableActionWidget *)` | method | `void` | public | — |
| `handle_delete_row( const EditTableActionWidget *)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_EDITTABLEWIDGET_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditTableActionWidget](EditTableActionWidget.md) | qt-widgets | 4 |
| [qt-widgets/EditGeometryWidget](EditGeometryWidget.md) | qt-widgets | 3 |
| [qt-widgets/EditStringListWidget](EditStringListWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditTimeSequenceWidget](EditTimeSequenceWidget.md) | qt-widgets | 2 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](EditTotalReconstructionSequenceWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/EditTableWidget.h
python scripts/gpq.py def GPlatesQtWidgets::EditTableWidget --body
python scripts/gpq.py uses EditTableWidget --kind class
python scripts/gpq.py hier EditTableWidget
```
