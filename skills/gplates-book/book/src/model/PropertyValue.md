# PropertyValue

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 931 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/PropertyValue.h` | C++ | 296 |
| `src/model/PropertyValue.cc` | C++ | 56 |

## Overview

This is the root of the property-value hierarchy: every concrete GPML and GML value type
in `property-values` (`GpmlPlateId`, `GmlTimePeriod`, `GpmlConstantValue`,
`GpmlIrregularSampling`, …) derives from it, and a feature's content is ultimately a tree
of these hanging off `TopLevelPropertyInline`. The base fixes four things for all of them:
intrusive reference counting through `GPlatesUtils::ReferenceCount`, so values are always
passed as `non_null_ptr_type` and never by value; double dispatch onto
`FeatureVisitorBase` via `accept_visitor`, which is how everything in `feature-visitors`
and the writers in `file-io` reads a feature; a `GPlatesPropertyValues::StructuralType`
tag that ties the C++ class back to the GPGIM type it implements; and a deep copy
operation.

Copying is deliberately awkward. Copy-assignment is declared and never defined, so the
only way to duplicate a value is `deep_clone_as_prop_val()`, which recursively copies
nested values as well. That function cannot live in the base — it forwards to a
non-virtual `deep_clone()` whose return type is the derived class — so each derived class
plants an identical definition by invoking the `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()`
macro in its class body. The Doxygen here says a "Bubble-Up revisioning system" would make
deep cloning redundant; that system was never finished, and in this version editing a
feature really does mean cloning a property value, changing the clone, and handing it back
to `FeatureHandle::set`.

The `d_instance_id` counter is the mechanism that makes that clone-edit-check-in cycle
work without a revisioning system, and it is the one piece of this class whose behaviour
is not what its name suggests — see the notes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureVisitor`](#gplatesmodelfeaturevisitor) | typedef | — | — | 0 | — |
| [`GPlatesModel::ConstFeatureVisitor`](#gplatesmodelconstfeaturevisitor) | typedef | — | — | 0 | — |
| [`GPlatesModel::PropertyValue`](#gplatesmodelpropertyvalue) | class | [`GPlatesUtils::ReferenceCount<PropertyValue>`](../utils/ReferenceCount.md)<br>[`GPlatesUtils::QtStreamable<PropertyValue>`](../utils/QtStreamable.md) | — | 46 | This class is the abstract base of all property values. |

## Members

### `GPlatesModel::FeatureVisitor`

*None.*

### `GPlatesModel::ConstFeatureVisitor`

*None.*

### `GPlatesModel::PropertyValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<PropertyValue, GPlatesUtils::NullIntrusivePointerHandler>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<PropertyValue, GPlatesUtils::NullIntrusivePointerHandler\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const PropertyValue, GPlatesUtils::NullIntrusivePointerHandler>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const PropertyValue, GPlatesUtils::NullIntrusivePointerHandler\>. |
| `PropertyValue()` | constructor | `None` | public | Construct a PropertyValue instance. |
| `PropertyValue( const PropertyValue &other)` | constructor | `None` | public | Construct a PropertyValue instance which is a copy of other. |
| `~PropertyValue()` | destructor | `None` | public | — |
| `deep_clone_as_prop_val()` | method | `non_null_ptr_type` | public | Create a duplicate of this PropertyValue instance, including a recursive copy of any property values this instance might contain. |
| `get_structural_type()` | method | `GPlatesPropertyValues::StructuralType` | public | Returns the structural type associated with the type of the derived property value class. |
| `accept_visitor( ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | Prints the contents of this PropertyValue to the stream os. |
| `operator==( const PropertyValue &other)` | operator | `bool` | public | — |
| `update_instance_id()` | method | `void` | protected | Give this PropertyValue instance a new instance id. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | Reimplement in derived classes where there are instance variables that can be modified by client code without using a set\_\*() function. |
| `operator=` | field | `PropertyValue` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |
| `instance_id_type` | class | `None` | private | Just in case we happen to run into a compiler without 64-bit integers. |
| `d_instance_id` | field | `instance_id_type` | private | Assists in speeding up operator==. |
| `s_next_instance_id` | field | `instance_id_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_next_instance_id` | variable | `GPlatesModel::PropertyValue::instance_id_type` | — |
| `operator==( const PropertyValue &other)` | operator | `bool` | — |
| `GPLATES_MODEL_PROPERTYVALUE_H` | macro | `None` | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL` | macro_function | `virtual \ const GPlatesModel::PropertyValue::non_null_ptr_type \ deep_clone_as_prop_val() const \ { \ return deep_clone(); \ }` | This macro is used to define the virtual function 'deep\_clone\_as\_prop\_val' inside a class which derives from PropertyValue. |
| `operator<<` | variable | `std::ostream` | operator\<\< for PropertyValue. |

## Notes

- **`operator==` is not value equality.** The `.cc` comment is explicit: it compares
  `d_instance_id` (plus `directly_modifiable_fields_equal`) and therefore answers "is
  `other` an unmodified clone of `this`", not "do these hold the same data". Two values
  built independently from identical inputs compare unequal. The copy constructor
  deliberately propagates the instance id, so a fresh clone compares equal to its original
  until something mutates it.
- **Every mutator must call `update_instance_id()`.** That call is what breaks the link
  between a clone and its original. It is the whole contract: `FeatureHandle::set` skips
  the store — and so emits no modification notification, sets no unsaved-changes flag and
  creates no changeset entry — when the incoming value compares equal to the one already
  there. A setter added to a derived class that forgets `update_instance_id()` silently
  discards the user's edit. Around 30 files in `property-values` make this call.
- **Override `directly_modifiable_fields_equal` when you leak internals.** If a derived
  class hands out a member by non-const reference or as a `non_null_intrusive_ptr` (an XML
  attribute map, a nested property value), the client can mutate it without any setter
  running, so the instance id stays stale. The override compensates by comparing those
  fields for real — `GpmlConstantValue` compares its nested value with `*d_value ==
  *other.d_value`, and `GmlTimePeriod`, `GpmlArray`, `GpmlKeyValueDictionary` and about a
  dozen others do the same. The base returns `true`, which means "trust the instance id".
- **Reference count starts at zero.** Both constructors initialise a fresh
  `ReferenceCount`, including the copy constructor. A newly constructed or cloned value is
  only safe once it is inside a `non_null_intrusive_ptr`; that is why `create` and
  `clone` in every derived class wrap the `new` immediately.
- **`s_next_instance_id` is a plain non-atomic process-wide counter**, incremented by the
  default constructor and by `update_instance_id()`. Constructing or mutating property
  values on more than one thread races on it, and a collision would make two unrelated
  values compare equal.
- `print_to` is virtual and `operator<<` is the free function that dispatches to it; the
  `QtStreamable` base is what extends that to `qDebug()` and `QTextStream`.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/ModelUtils](ModelUtils.md) | model | 50 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 39 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 25 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 24 |
| [property-values/GpmlAge](../property-values/GpmlAge.md) | property-values | 23 |
| [property-values/GpmlArray](../property-values/GpmlArray.md) | property-values | 23 |
| [property-values/GmlRectifiedGrid](../property-values/GmlRectifiedGrid.md) | property-values | 22 |
| [property-values/GpmlConstantValue](../property-values/GpmlConstantValue.md) | property-values | 22 |
| [property-values/GmlFile](../property-values/GmlFile.md) | property-values | 21 |
| [property-values/GmlTimePeriod](../property-values/GmlTimePeriod.md) | property-values | 20 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 19 |
| [model/TopLevelPropertyInline](TopLevelPropertyInline.md) | model | 18 |
| [property-values/GpmlOldPlatesHeader](../property-values/GpmlOldPlatesHeader.md) | property-values | 18 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 18 |
| [property-values/GpmlHotSpotTrailMark](../property-values/GpmlHotSpotTrailMark.md) | property-values | 17 |
| [property-values/GpmlKeyValueDictionaryElement](../property-values/GpmlKeyValueDictionaryElement.md) | property-values | 17 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 16 |
| [property-values/GpmlTopologicalNetwork](../property-values/GpmlTopologicalNetwork.md) | property-values | 16 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 13 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 13 |

*... and 119 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/PropertyValue.h
python scripts/gpq.py def GPlatesModel::PropertyValue --body
python scripts/gpq.py uses PropertyValue --kind class
python scripts/gpq.py hier PropertyValue
```
