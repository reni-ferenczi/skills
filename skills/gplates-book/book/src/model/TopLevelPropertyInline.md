# TopLevelPropertyInline

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 129 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/TopLevelPropertyInline.h` | C++ | 287 |
| `src/model/TopLevelPropertyInline.cc` | C++ | 195 |

## Overview

This is the only concrete `TopLevelProperty` in the tree — the abstract base anticipates a
`TopLevelPropertyXlink` that would reference a property remotely through a GML XLink, but
it was never written, so in practice every property of every feature is one of these. Its
job is to pair the `PropertyName` and XML attribute map it inherits from
`TopLevelProperty` with the property's values, held inline in a `std::vector` of
`PropertyValue::non_null_ptr_type`. The GPML reader (`GpmlFeatureReaderImpl`) always builds
single-valued properties, but the container is a vector and
`FeatureVisitorBase::visit_property_values` walks all of the elements, so code that assumes
exactly one value is making an assumption the type does not enforce.

Construction goes exclusively through the static `create` overloads: the constructors are
protected and return the object already wrapped in a `non_null_intrusive_ptr`, matching the
`ReferenceCount` ownership used everywhere in `model`. The property name is fixed at
construction and `TopLevelProperty` deliberately provides no setter for it — renaming a
property means building a new one. `accept_visitor` dispatches to
`FeatureVisitorBase::visit_top_level_property_inline`, which is the single hook every
feature visitor and every writer in `file-io` goes through to reach a feature's values.

The const/non-const iterator asymmetry is intentional. `const_iterator` is a
`boost::transform_iterator` that converts each stored pointer into a
`non_null_ptr_to_const_type`, so const access cannot hand out a mutable value; the
non-const `begin()`/`end()` expose the vector's own iterators and can. That second path is
a hole in the change-tracking machinery — see the notes.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::TopLevelPropertyInline`](#gplatesmodeltoplevelpropertyinline) | class | [`TopLevelProperty`](TopLevelProperty.md) | — | 0 | This class represents a top-level property of a feature, which is containing its property-value inline. |

## Members

### `GPlatesModel::TopLevelPropertyInline`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopLevelPropertyInline>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<TopLevelPropertyInline\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopLevelPropertyInline>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const TopLevelPropertyInline\>. |
| `container_type` | typedef | `std::vector<PropertyValue::non_null_ptr_type>` | public | The type of our container of PropertyValue pointers. |
| `iterator` | typedef | `container_type::iterator` | public | The type of an iterator that iterates over the PropertyValue instances contained in this TopLevelPropertyInline. |
| `make_const_ptr_fn_type` | typedef | `boost::function< PropertyValue::non_null_ptr_to_const_type ( const PropertyValue::non_null_ptr_type &) >` | private | The type of a function that converts a pointer to non-const PropertyValue to a pointer to const. |
| `const_iterator` | typedef | `boost::transform_iterator<make_const_ptr_fn_type, container_type::const_iterator>` | public | The type of an iterator that const-iterates over the PropertyValue instances contained in this TopLevelPropertyInline. |
| `~TopLevelPropertyInline()` | destructor | `None` | public | — |
| `create( const PropertyName &property_name_, const container_type &values_, const xml_attributes_type &xml_attributes_ = xml_attributes_type())` | method | `non_null_ptr_type` | public | — |
| `create( const PropertyName &property_name_, const PropertyValueIterator &values_begin_, const PropertyValueIterator &values_end_, const xml_attributes_type &xml_attributes_ = xml_attributes_type())` | method | `non_null_ptr_type` | public | — |
| `create( const PropertyName &property_name_, PropertyValue::non_null_ptr_type value_, const xml_attributes_type &xml_attributes_ = xml_attributes_type())` | method | `non_null_ptr_type` | public | — |
| `create( const PropertyName &property_name_, PropertyValue::non_null_ptr_type value_, const GPlatesUtils::UnicodeString &attribute_name_string, const GPlatesUtils::UnicodeString &attribute_value_string)` | method | `non_null_ptr_type` | public | — |
| `create( const PropertyName &property_name_, PropertyValue::non_null_ptr_type value_, const AttributeIterator &attributes_begin, const AttributeIterator &attributes_end)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `TopLevelProperty::non_null_ptr_type` | public | — |
| `deep_clone()` | method | `TopLevelProperty::non_null_ptr_type` | public | — |
| `begin()` | method | `const_iterator` | public | — |
| `end()` | method | `const_iterator` | public | — |
| `size()` | method | `size_t` | public | — |
| `accept_visitor( ConstFeatureVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( FeatureVisitor &visitor)` | method | `void` | public | — |
| `print_to` | field | `std::ostream` | public | — |
| `operator==( const TopLevelProperty &other)` | operator | `bool` | public | — |
| `TopLevelPropertyInline( const PropertyName &property_name_, const container_type &values_, const xml_attributes_type &xml_attributes_)` | constructor | `None` | protected | — |
| `TopLevelPropertyInline( const PropertyName &property_name_, const PropertyValueIterator &values_begin_, const PropertyValueIterator &values_end_, const xml_attributes_type &xml_attributes_)` | constructor | `None` | protected | — |
| `TopLevelPropertyInline( const PropertyName &property_name_, PropertyValue::non_null_ptr_type value_, const xml_attributes_type &xml_attributes_)` | constructor | `None` | protected | — |
| `TopLevelPropertyInline( const TopLevelPropertyInline &other)` | constructor | `None` | protected | — |
| `d_values` | field | `container_type` | private | — |
| `operator=` | field | `TopLevelPropertyInline` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISABLE_MSVC_WARNING` | variable | `PUSH_MSVC_WARNINGS` | — |
| `operator==( const TopLevelProperty &other)` | operator | `bool` | — |
| `GPLATES_MODEL_TOPLEVELPROPERTYINLINE_H` | macro | `None` | — |

## Notes

- **`clone()` is shallow and usually wrong.** It copies the vector of pointers, so the copy
  and the original share their `PropertyValue` objects; mutating a value through one is
  visible through the other. `deep_clone()` calls `deep_clone_as_prop_val()` on every
  element and is what you want when duplicating a feature or preparing an edit — it is also
  what `FeatureHandle::set` calls on the incoming property before storing it, precisely so
  that the caller cannot keep a back door into the model.
- **`operator==` inherits `PropertyValue`'s clone-identity semantics.** The name and the
  XML attributes are compared normally, but the values are compared with
  `PropertyValue::operator==`, which is an instance-id test rather than a data comparison.
  Two properties built independently from identical inputs compare unequal; an unmodified
  deep clone compares equal. `FeatureHandle::set` uses exactly this to decide whether an
  edit is a no-op, so a derived property value that forgets `update_instance_id()` in a
  setter will make edits vanish here. Comparison against any other `TopLevelProperty`
  subclass returns `false` through the caught `std::bad_cast`.
- **The non-const `begin()`/`end()` bypass change tracking.** They yield the vector's own
  iterators over `non_null_ptr_type`, so a caller who reaches a property through
  `FeatureHandle` and mutates a value in place produces no modification notification, no
  unsaved-changes flag on the feature collection and no `ChangesetHandle` entry. This is
  the reason `RevisionAwareIterator<FeatureHandle>` dereferences to a
  `TopLevelPropertyRef` proxy instead of a raw pointer. Edit by cloning and assigning
  through that proxy, not by writing through these iterators.
- **Ownership.** Copy-assignment is declared and never defined; instances are shared by
  intrusive pointer. As with `PropertyValue`, the copy constructor leaves the new object's
  reference count at zero, so a clone must go straight into a `non_null_intrusive_ptr` —
  which the `create` and `clone` functions already do.
- The `.cc` file pushes and pops MSVC warning 4181 around a Boost 1.35 header; leave the
  `PUSH_MSVC_WARNINGS` / `POP_MSVC_WARNINGS` pair alone when editing near the top or bottom
  of that file.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/ModelUtils](ModelUtils.md) | model | 19 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 17 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 17 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 16 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 13 |
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 11 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 10 |
| [feature-visitors/TotalReconstructionSequenceTimePeriodFinder](../feature-visitors/TotalReconstructionSequenceTimePeriodFinder.md) | feature-visitors | 9 |
| [model/FeatureVisitor](FeatureVisitor.md) | model | 9 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 7 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 7 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 7 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 7 |
| [feature-visitors/FeatureClassifier](../feature-visitors/FeatureClassifier.md) | feature-visitors | 6 |
| [feature-visitors/KeyValueDictionaryFinder](../feature-visitors/KeyValueDictionaryFinder.md) | feature-visitors | 6 |
| [feature-visitors/TotalReconstructionSequencePlateIdFinder](../feature-visitors/TotalReconstructionSequencePlateIdFinder.md) | feature-visitors | 6 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 6 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 6 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 6 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 5 |

*... and 45 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/TopLevelPropertyInline.h
python scripts/gpq.py def GPlatesModel::TopLevelPropertyInline --body
python scripts/gpq.py uses TopLevelPropertyInline --kind class
python scripts/gpq.py hier TopLevelPropertyInline
```
