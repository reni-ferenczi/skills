# AbstractEditWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 452 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AbstractEditWidget.h` | C++ | 286 |
| `src/qt-widgets/AbstractEditWidget.cc` | C++ | 101 |

## Overview

[[[PROSE overview unit=qt-widgets/AbstractEditWidget tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::AbstractEditWidget`](#gplatesqtwidgetsabstracteditwidget) | class | `QWidget` | — | 16 | Abstract base of all GPlatesQtWidgets::Edit\*Widget. |

## Members

### `GPlatesQtWidgets::AbstractEditWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AbstractEditWidget( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~AbstractEditWidget()` | destructor | `None` | public | — |
| `reset_widget_to_default_values()` | method | `void` | public | Sets sensible default values for all line edits, spinboxes etc that belong to this edit widget. |
| `configure_for_property_value_type( const GPlatesPropertyValues::StructuralType &property_value_type)` | method | `void` | public | Informs the edit widget of the specific property value type (by name) that we are requesting this edit widget handle. |
| `create_property_value_from_widget()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | public | Requests that the edit widget convert its fields into a new PropertyValue and return it, ready for insertion into the Model. |
| `update_property_value_from_widget()` | method | `bool` | public | Requests that the edit widget should use setter methods to update whichever PropertyValue the widget last read values from. |
| `is_dirty()` | method | `bool` | public | Checks if this edit widget is 'dirty' (user has modified fields and data is not in the model) |
| `will_handle_enter_key()` | method | `bool` | public | Returns whether the edit widget will process the Enter key and emit the commit\_me() signal when it is pressed. |
| `label()` | method | `QLabel` | public | Some derivations of AbstractEditWidget may declare one of their (presumably Qt-Designer made) labels as the 'default' label. |
| `declare_default_label( QLabel *label_)` | method | `void` | protected | Derivations of AbstractEditWidget can call this member in their constructor to set a label as the 'default' for this edit widget; This allows the owner of the edit widget to hide, show, or change default mneumonic keys of the label as ... |
| `keyPressEvent( QKeyEvent *ev)` | method | `void` | protected | — |
| `set_dirty()` | method | `void` | public | set\_dirty() should be called whenever a widget is modified by a user (not programatically!) to keep track of whether this edit widget should have it's data committed by the EditFeaturePropertiesWidget. |
| `set_clean()` | method | `void` | public | set\_clean() will be called by EditWidgetGroupBox::set\_clean(), which should be called whenever a PropertyValue has been constructed and committed into the model from this widget. |
| `set_handle_enter_key( bool should_handle)` | method | `void` | public | Controls whether the edit widget will process the Enter key and emit the commit\_me() and enter\_pressed() signals when it is pressed. |
| `commit_me()` | method | `void` | public | Signal typically emitted when the user presses enter, indicating an updated value. |
| `enter_pressed()` | method | `void` | public | Signal emitted when the user presses enter. |
| `operator=` | field | `AbstractEditWidget` | private | This operator should never be defined, because we don't want/need to allow copy-assignment. |
| `d_default_label_ptr` | field | `QLabel` | private | The 'default' label for this edit widget. |
| `d_dirty` | field | `bool` | private | — |
| `d_handle_enter_key` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_ABSTRACTEDITWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/AbstractEditWidget tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditStringListWidget](EditStringListWidget.md) | qt-widgets | 38 |
| [qt-widgets/CreateFeaturePropertiesPage](CreateFeaturePropertiesPage.md) | qt-widgets | 24 |
| [qt-widgets/EditTimePeriodWidget](EditTimePeriodWidget.md) | qt-widgets | 24 |
| [qt-widgets/EditWidgetChooser](EditWidgetChooser.md) | qt-widgets | 23 |
| [qt-widgets/EditWidgetGroupBox](EditWidgetGroupBox.md) | qt-widgets | 23 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 22 |
| [qt-widgets/EditPlateIdWidget](EditPlateIdWidget.md) | qt-widgets | 17 |
| [qt-widgets/EditEnumerationWidget](EditEnumerationWidget.md) | qt-widgets | 15 |
| [qt-widgets/EditAgeWidget](EditAgeWidget.md) | qt-widgets | 14 |
| [qt-widgets/EditBooleanWidget](EditBooleanWidget.md) | qt-widgets | 14 |
| [qt-widgets/EditGeometryWidget](EditGeometryWidget.md) | qt-widgets | 14 |
| [qt-widgets/CreateFeatureAddOrEditPropertyDialog](CreateFeatureAddOrEditPropertyDialog.md) | qt-widgets | 13 |
| [qt-widgets/EditAngleWidget](EditAngleWidget.md) | qt-widgets | 13 |
| [qt-widgets/EditDoubleWidget](EditDoubleWidget.md) | qt-widgets | 13 |
| [qt-widgets/EditIntegerWidget](EditIntegerWidget.md) | qt-widgets | 13 |
| [qt-widgets/EditShapefileAttributesWidget](EditShapefileAttributesWidget.md) | qt-widgets | 13 |
| [qt-widgets/EditStringWidget](EditStringWidget.md) | qt-widgets | 13 |
| [qt-widgets/EditTimeInstantWidget](EditTimeInstantWidget.md) | qt-widgets | 13 |
| [qt-widgets/EditOldPlatesHeaderWidget](EditOldPlatesHeaderWidget.md) | qt-widgets | 12 |
| [qt-widgets/EditPolarityChronIdWidget](EditPolarityChronIdWidget.md) | qt-widgets | 12 |

*... and 5 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/AbstractEditWidget.h
python scripts/gpq.py def GPlatesQtWidgets::AbstractEditWidget --body
python scripts/gpq.py uses AbstractEditWidget --kind class
python scripts/gpq.py hier AbstractEditWidget
```
