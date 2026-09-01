# Completionist

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 771 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/Completionist.h` | C++ | 107 |
| `src/gui/Completionist.cc` | C++ | 221 |

## Overview

[[[PROSE overview unit=gui/Completionist tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ModelColumnName`](#anonymousmodelcolumnname) | enum | — | — | 0 | — |
| [`GPlatesGui::Completionist`](#gplatesguicompletionist) | class | [`GPlatesUtils::Singleton<Completionist>`](../utils/Singleton.md) | — | 0 | GUI class to load and hold assorted lists of completion terms for tab completion or find-as-you-type functionality on QLineEdits and to generate appropriate Qt Models and QCompleter objects behind the scenes so that all you really need to ... |

## Members

### `(anonymous)::ModelColumnName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MODEL_COLUMN_COMPLETION` | enumerator | `None` | — | — |
| `MODEL_COLUMN_POPUP` | enumerator | `None` | — | — |

### `GPlatesGui::Completionist`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~Completionist()` | destructor | `None` | public | — |
| `install_completer( QLineEdit &widget)` | method | `void` | public | Creates a QCompleter object suitable for completion with the specified dictionary of terms, and installs it on the given QLineEdit using -\>setCompleter(). this implies doing -\>setWidget() on the QCompleter object - only one completer can ... |
| `get_model_for_dictionary( const QString &name)` | method | `QAbstractItemModel` | private | Instantiate or fetch a previously instantiated QAbstractItemModel for use by QCompleter. |
| `d_models` | field | `QMap<QString, QSharedPointer<QAbstractItemModel> >` | private | Holds the constructed Qt models corresponding to our dictionaries for use and re-use by QCompleter objects. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `appropriate_fg_colour( const QColor &bg_colour)` | function | `QColor` | — |
| `load_xml_completion_resource( const QString &resource_path)` | function | `QDomDocument` | — |
| `add_child_groups_to_model( int &row, int depth, QString indent, const QDomNode node, QAbstractItemModel *model)` | function | `void` | Recursively transform our XML Timescale document into a QAbstractItemModel for completion purposes. |
| `create_model_from_timescale_xml( const QDomDocument &dom)` | function | `QAbstractItemModel` | Creates a new AbstractItemModel corresponding to the given QDomDocument presuming it is a GPlatesTimescale document. |
| `GPLATES_GUI_COMPLETIONIST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/Completionist tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditAgeWidget](../qt-widgets/EditAgeWidget.md) | qt-widgets | 8 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/Completionist.h
python scripts/gpq.py def GPlatesGui::Completionist --body
python scripts/gpq.py uses Completionist --kind class
python scripts/gpq.py hier Completionist
```
