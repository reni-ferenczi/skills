# IdStringSet

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 490 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/IdStringSet.h` | C++ | 684 |
| `src/utils/IdStringSet.cc` | C++ | 126 |

## Overview

A reference-counted string pool with a reverse index attached to each entry.
Despite the name it does not derive from `GPlatesUtils::StringSet`; it is a
parallel implementation of the same idea, with one addition that justifies the
duplication. Every pooled string carries a `back_ref_list_type` — a
`SmartNodeLinkedList` of `AbstractBackRef *` — recording which live objects are
identified by that string. This is what makes "find every feature with this
feature ID" cost O(n) in the number of matching objects rather than O(N) over
every feature loaded.

In practice there is exactly one instance in the program:
`GPlatesModel::StringSetSingletons::feature_id_instance()`, a
`GPlatesUtils::Singleton<IdStringSet>`. All the other pools in that file are
plain `StringSet`s, because feature IDs are the only strings that need to point
back at their owners. The client is `GPlatesModel::IdTypeGenerator`, from which
`GPlatesModel::FeatureId` is typedef'd. `IdTypeGenerator` holds a
`SharedIterator` for its string and, optionally, a `BackRef` derived from
`AbstractBackRef`; the `BackRef` owns a `back_ref_list_type::Node` whose
destructor splices itself out of the list. That is the whole dangling-ID story:
when a `FeatureHandle` dies, its `FeatureId` dies, its `BackRef` dies, the node
unlinks, and the reverse index is correct again — with no observer registry and
no sweep.

The three-layer structure is deliberate rather than incidental. `IdStringSetImpl`
holds the `std::set` and is itself reference-counted via
`GPlatesUtils::ReferenceCount`; `IdStringSet` and every `SharedIterator` share
ownership of it through `boost::intrusive_ptr`, so an initialised
`SharedIterator` stays dereferenceable even after the `IdStringSet` is gone.
`std::set` is chosen (not a hash table or a vector) because its iterators survive
insertion and erasure of *other* elements — a `SharedIterator` stores a raw
`collection_type::iterator` and would otherwise be invalidated by the next
insert.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::IdStringSet`](#gplatesutilsidstringset) | class | — | — | 0 | An extension of class StringSet in which the strings are intended to be IDs. |

## Members

### `GPlatesUtils::IdStringSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AbstractBackRef` | class | `None` | public | The abstract base class of back-references. |
| `back_ref_type` | typedef | `AbstractBackRef` | public | The type of a back-reference. |
| `back_ref_list_type` | typedef | `SmartNodeLinkedList<back_ref_type>` | public | The type of a list of back-references. |
| `UnicodeStringAndRefCountWithBackRef` | struct | `None` | public | This is the element which is contained in the std::set inside IdStringSetImpl. |
| `collection_type` | typedef | `std::set< UnicodeStringAndRefCountWithBackRef >` | public | — |
| `size_type` | typedef | `collection_type::size_type` | public | — |
| `IdStringSetImpl` | class | `None` | public | A set of UnicodeString instances, each with an associated reference-count and a (possibly-empty) list of back-references. |
| `SharedIterator` | class | `None` | public | de-allocated. -# When a SharedIterator instance is copy-assigned to another instance, the copy-assignment function acts to handle the increment/decrement of the number of references to elements of the std::set : if a SharedIterator ... |
| `IdStringSet()` | constructor | `None` | public | Construct a new, empty IdStringSet instance. |
| `size()` | method | `size_type` | public | Return the number of UnicodeString instances contained within the IdStringSet instance. @pre True. @post Return-value is the number of elements in the IdStringSet instance. |
| `contains( const GPlatesUtils::UnicodeString &s)` | method | `boost::optional<SharedIterator>` | public | Determine whether the IdStringSet instance contains the UnicodeString instance s, without modifying the contents of the IdStringSet instance. a boost::optional instance which contains a SharedIterator instance which points to the element ... |
| `insert( const GPlatesUtils::UnicodeString &s)` | method | `SharedIterator` | public | Obtain a SharedIterator instance which points to the UnicodeString instance s within an IdStringSet instance. |
| `d_impl` | field | `boost::intrusive_ptr<IdStringSetImpl>` | private | — |
| `IdStringSet( const IdStringSet &)` | constructor | `None` | private | This constructor should never be defined, because we don't want to allow copy-construction (since the copy-constructed instance might contain strings with non-zero reference-counts, without SharedIterators referencing them). |
| `operator=` | field | `IdStringSet` | private | This operator should never be defined, because we don't want to allow copy-assignment (since the copy-assigned instance might contain strings with non-zero reference-counts, without SharedIterators referencing them). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator==( const SharedIterator &other)` | operator | `bool` | — |
| `GPLATES_UTILS_IDSTRINGSET_H` | macro | `None` | — |
| `GPLATES_ICU_BOOL` | macro_function | `((b) != 0)` | — |
| `swap( GPlatesUtils::IdStringSet::SharedIterator &sh_iter1, GPlatesUtils::IdStringSet::SharedIterator &sh_iter2)` | function | `void` | — |

## Notes

- **Two independent reference counts.** `IdStringSetImpl` is counted by
  `intrusive_ptr` (keeps the *set* alive); each element's `d_ref_count` is
  incremented by `SharedIterator` (keeps the *string* alive). When an element's
  count reaches zero, `decrement_ref_count()` erases it from the `std::set`
  immediately — back-reference list and all. A string is therefore only in the
  pool while some `SharedIterator` names it; there is no long-lived interning.
- **`contains()` is `const` but mutates.** Constness does not propagate through
  `d_impl`, and the `SharedIterator` it returns bumps the element's ref count.
  `d_ref_count` and `d_back_refs` are `mutable` precisely because `std::set`
  elements are const. Do not assume a `const IdStringSet &` is read-only.
- **Both lookups allocate.** `contains()` and `insert()` each construct a full
  `UnicodeStringAndRefCountWithBackRef` — copying the `UnicodeString` — just to
  hand `std::set::find` a comparison key. That is a string copy on every probe,
  including the hit path.
- **`insert()` cannot carry back-references.** The element's copy constructor
  deliberately resets the ref count to zero and starts a *fresh empty* back-ref
  list rather than copying `other`'s, because `std::set` stores a copy of the
  temporary. Back-references must therefore be attached after insertion, through
  `SharedIterator::back_refs()` — which is what `IdTypeGenerator::BackRef` does.
- **`AbstractBackRef` ownership is not here.** The typedef comment states the
  contract: whoever owns the `SmartNodeLinkedList` `Node` also owns the back-ref
  object. `IdStringSet` never deletes a back-ref, and downcasting to the real
  type requires `dynamic_cast` — `IdTypeGenerator::find_back_ref_targets()`
  silently skips entries whose cast fails.
- **Not thread safe.** No synchronisation anywhere: the ref counts are plain
  `long`, the `std::set` and the linked lists are unguarded, and the single
  instance is a process-wide singleton.
- **Non-copyable by declaration only.** The copy constructor and assignment
  operator are private and *never defined* — a pre-C++11 idiom, so misuse from
  inside the class surfaces as a link error rather than a compile error.
- `GPLATES_ICU_BOOL` is a `#ifndef`-guarded shim for ICU's integer `UBool`,
  applied to the `UnicodeString` comparison in `operator<`.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/StringSetSingletons](../model/StringSetSingletons.md) | model | 86 |
| [utils/XmlNamespaces](XmlNamespaces.md) | utils | 59 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 43 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 41 |
| [model/QualifiedXmlName](../model/QualifiedXmlName.md) | model | 18 |
| [file-io/XmlWriter](../file-io/XmlWriter.md) | file-io | 17 |
| [model/IdTypeGenerator](../model/IdTypeGenerator.md) | model | 16 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 13 |
| [property-values/GmlDataBlockCoordinateList](../property-values/GmlDataBlockCoordinateList.md) | property-values | 7 |
| [property-values/GmlOrientableCurve](../property-values/GmlOrientableCurve.md) | property-values | 7 |
| [property-values/GpmlMeasure](../property-values/GpmlMeasure.md) | property-values | 7 |
| [model/XmlNode](../model/XmlNode.md) | model | 6 |
| [property-values/GmlFile](../property-values/GmlFile.md) | property-values | 6 |
| [property-values/GmlRectifiedGrid](../property-values/GmlRectifiedGrid.md) | property-values | 6 |
| [model/TranscribeQualifiedXmlName](../model/TranscribeQualifiedXmlName.md) | model | 3 |
| [property-values/GmlTimeInstant](../property-values/GmlTimeInstant.md) | property-values | 3 |
| [qt-widgets/EditAngleWidget](../qt-widgets/EditAngleWidget.md) | qt-widgets | 3 |
| [property-values/GmlTimePeriod](../property-values/GmlTimePeriod.md) | property-values | 2 |
| [property-values/UninterpretedPropertyValue](../property-values/UninterpretedPropertyValue.md) | property-values | 2 |
| [property-values/XsString](../property-values/XsString.md) | property-values | 2 |

*... and 9 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/IdStringSet.h
python scripts/gpq.py def GPlatesUtils::IdStringSet --body
python scripts/gpq.py uses IdStringSet --kind class
python scripts/gpq.py hier IdStringSet
```
