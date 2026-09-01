# AbstractEditWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 452 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/AbstractEditWidget.h` | C++ | 286 |
| `src/qt-widgets/AbstractEditWidget.cc` | C++ | 101 |

## Overview

This is the contract that lets one piece of generic property-editing UI drive
sixteen unrelated Qt Designer forms. Each subclass pairs with a `Ui_Edit*Widget`
form and knows exactly one family of `GPlatesPropertyValues` types; the base
class defines the four operations the surrounding machinery needs from all of
them — reset to defaults, optionally reconfigure for a named
`GPlatesPropertyValues::StructuralType`, mint a fresh
`GPlatesModel::PropertyValue` from the current fields, and push the fields back
into the property value the widget was last loaded from. Everything the base
class implements itself is the small amount of shared state that goes with those
operations: the dirty flag, the Enter-key policy, and an optional pointer to the
form's "default" label.

The two callers that matter are `EditWidgetGroupBox`, which pre-allocates one
instance of every subclass and shows exactly one at a time, and
`EditWidgetChooser`, a property-value visitor that picks which one by dispatching
on the concrete property value type. That split is why the base class carries
`configure_for_property_value_type()` with a do-nothing default: most widgets
serve a single structural type and never override it, while `EditGeometryWidget`
and `EditEnumerationWidget` cover several and use the call to reshape themselves
(and to reject types they cannot handle, by throwing
`PropertyValueNotSupportedException`). The header's own comment is the
authoritative checklist for adding a new widget — it lists the five places in
`EditWidgetGroupBox` and the two in `EditWidgetChooser` that must be touched,
because none of that wiring is automatic.

There is an asymmetry between the two write paths that is easy to miss.
`create_property_value_from_widget()` is `const` and builds a brand-new value —
the path used by `AddPropertyDialog` and `CreateFeatureDialog`, where no model
object exists yet. `update_property_value_from_widget()` mutates the property
value the subclass stashed during its own `update_widget_from_xxxx()` call (see
`EditPlateIdWidget::update_widget_from_plate_id`, which caches a pointer to the
`GpmlPlateId`), which is the path `EditFeaturePropertiesWidget` uses for
in-place editing of a focused feature.

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

`set_handle_enter_key(false)` does not do what its documentation says. In
`keyPressEvent()` the `d_handle_enter_key` test calls `ev->ignore()` but does not
return, so control falls straight into the `Key_Enter` / `Key_Return` branches,
which emit `enter_pressed()` and `commit_me()` and then `accept()` the event
regardless. If you need a widget that genuinely lets Enter propagate to a dialog's
default button, fix the fall-through rather than relying on the flag.

`keyPressEvent()` also swallows the base-class implementation entirely: every
other key is merely `ignore()`d, `QWidget::keyPressEvent()` is never called. That
is harmless for the current subclasses because the real input focus lives in a
child spinbox or line edit (constructors typically call `setFocusProxy()`), so
ordinary typing never reaches this handler.

The dirty flag is a convention, not an enforced invariant. Nothing in the base
class sets it; each subclass must connect its own editing controls to the
`set_dirty()` slot, and only user-driven changes should do so — a
`update_widget_from_xxxx()` call is expected to end with `set_clean()`. Get this
wrong and `EditWidgetGroupBox::update_property_value_from_widget()` either
silently drops the user's edit or, because it returns "the model was altered",
feeds an unnecessary `FeatureFocus` modification notification back into the
widget and risks a signal loop.

`update_property_value_from_widget()` has a precondition that the base class
cannot check: a preceding `update_widget_from_xxxx()` call. Subclasses signal the
violation by throwing `UninitialisedEditWidgetException` (a
`GPlatesGlobal::PreconditionViolationError`), and `reset_widget_to_default_values()`
is specified to put the widget back into that uninitialised state — it must clear
the cached property-value pointer, not merely blank the fields.

Ownership follows Qt's parent/child rule: `EditWidgetGroupBox` constructs one of
each subclass with itself as parent and never deletes them, so instances outlive
any individual property being edited and must be fully re-initialised on each
activation. The `QLabel *` handed to `declare_default_label()` is a non-owning
pointer to a child of the widget's own form; `label()` returns NULL for widgets
that never declared one, so callers must check.

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
