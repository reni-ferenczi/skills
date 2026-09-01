# StringSet

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 635 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/StringSet.h` | C++ | 702 |
| `src/utils/StringSet.cc` | C++ | 122 |

## Overview

A reference-counted string interning pool. Every distinct
`GPlatesUtils::UnicodeString` put into a `StringSet` is stored exactly once, and
client code holds a `SharedIterator` in place of the string. That buys two
things at once, both of which the model depends on: the obvious memory saving
when tens of thousands of features repeat the same feature type or property
name, and — because the set holds each string uniquely — the ability to compare
two strings for identity in O(1) by comparing iterators, instead of walking two
Unicode strings code point by code point. Ordering is still by string content
(`std::set` needs a strict weak order), so an `insert()` costs O(L log N); only
the subsequent comparisons are free. The class comment's advice is to pay that
cost once per call site by caching the returned `SharedIterator` in a
function-scope static.

The type is deliberately split in two. `StringSet` holds a
`boost::intrusive_ptr<StringSetImpl>`, and `StringSetImpl` — a
`GPlatesUtils::ReferenceCount` subclass, heap-only, created through its static
`create()` — owns the actual `std::set`. Each `SharedIterator` holds its own
intrusive pointer to the same impl, so the pool outlives the `StringSet` handle
whenever any iterator is still alive. This is not incidental: the sets are
process-wide singletons and the iterators are embedded in model objects, so the
impl split is what makes teardown order at process exit a non-issue. The other
half of the reference counting lives in the element itself —
`UnicodeStringAndRefCount` carries a `mutable long` count that
`SharedIterator`'s constructor, copy-constructor and destructor drive, and when
it reaches zero `decrement_ref_count()` erases the element from the set. A
string is therefore in the pool exactly as long as somebody is holding it.

Nothing in `utils` instantiates a `StringSet`; the pools live in
`GPlatesModel::StringSetSingletons`, which uses `GPlatesUtils::Singleton` with
one empty tag struct per pool (`FeatureTypeInstance`, `PropertyNameInstance`,
`TextContentInstance`, `XMLNamespaceInstance`, …) to get a dozen separate
instances of the same type. `GPlatesModel::StringContentTypeGenerator` and
`GPlatesModel::QualifiedXmlName` are the wrappers that everything else sees: they
store a `SharedIterator` and forward `operator==` to it, which is why feature
types, property names, structural types and XML names compare in constant time
throughout `model`, `file-io` and `property-values`. The related
`GPlatesUtils::IdStringSet` is the same design with back-references added, used
for feature IDs.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::StringSet`](#gplatesutilsstringset) | class | — | — | 0 | @par Implementation (white box) description: (This description complements the abstraction description.) -# The conceptual StringSet is implemented using two classes: StringSet and StringSetImpl. |

## Members

### `GPlatesUtils::StringSet`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnicodeStringAndRefCount` | struct | `None` | public | This is the element which is contained in the std::set inside StringSetImpl. |
| `collection_type` | typedef | `std::set< UnicodeStringAndRefCount >` | public | — |
| `size_type` | typedef | `collection_type::size_type` | public | — |
| `StringSetImpl` | class | `None` | public | A set of UnicodeString instances, each with an associated reference-count. |
| `SharedIterator` | class | `None` | public | de-allocated. -# When a SharedIterator instance is copy-assigned to another instance, the copy-assignment function acts to handle the increment/decrement of the number of references to elements of the std::set : if a SharedIterator ... |
| `StringSet()` | constructor | `None` | public | Construct a new, empty StringSet instance. |
| `size()` | method | `size_type` | public | Return the number of UnicodeString instances contained within the StringSet instance. @pre True. @post Return-value is the number of elements in the StringSet instance. |
| `contains( const GPlatesUtils::UnicodeString &s)` | method | `boost::optional<SharedIterator>` | public | Determine whether the StringSet instance contains the UnicodeString instance s, without modifying the contents of the StringSet instance. a boost::optional instance which contains a SharedIterator instance which points to the element of ... |
| `insert( const GPlatesUtils::UnicodeString &s)` | method | `SharedIterator` | public | Obtain a SharedIterator instance which points to the UnicodeString instance s within a StringSet instance. |
| `d_impl` | field | `boost::intrusive_ptr<StringSetImpl>` | private | — |
| `StringSet( const StringSet &)` | constructor | `None` | private | This constructor should never be defined, because we don't want to allow copy-construction (since the copy-constructed instance might contain strings with non-zero reference-counts, without SharedIterators referencing them). |
| `operator=` | field | `StringSet` | private | This operator should never be defined, because we don't want to allow copy-assignment (since the copy-assigned instance might contain strings with non-zero reference-counts, without SharedIterators referencing them). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator==( const SharedIterator &other)` | operator | `bool` | — |
| `GPLATES_UTILS_STRINGSET_H` | macro | `None` | — |
| `GPLATES_ICU_BOOL` | macro_function | `((b) != 0)` | — |
| `swap( GPlatesUtils::StringSet::SharedIterator &sh_iter1, GPlatesUtils::StringSet::SharedIterator &sh_iter2)` | function | `void` | — |

## Notes

- **The set does not keep strings alive; the iterators do.** An element exists
  only while its reference count is above zero, so `insert()` whose result is
  discarded leaves the set exactly as it found it — the temporary
  `SharedIterator`'s destructor erases the element again. `size()` counts
  currently-referenced strings, not everything ever inserted.
- **`contains()` is `const` but still touches the count.** It hands back a
  `SharedIterator`, which increments the element's `mutable` reference count for
  as long as the returned `boost::optional` lives. It does not change the *set*,
  which is what the "without modifying the contents" wording means.
- **Iterators outlive the `StringSet`.** Both the handle and every
  `SharedIterator` hold an `intrusive_ptr` to the same `StringSetImpl`, so
  destroying the `StringSet` does not invalidate outstanding iterators — the impl
  survives until the last one goes. Combined with the singleton pools in
  `GPlatesModel::StringSetSingletons`, this is what makes static destruction
  order safe.
- **`std::set` node stability is load-bearing.** A `SharedIterator` stores a raw
  `collection_type::iterator`, so the design relies on `std::set` never moving or
  invalidating an element while other elements are inserted or erased. Swapping
  the container for anything with different iterator-stability guarantees would
  break every held iterator.
- **Comparison is only meaningful within one pool.** `operator==` returns false
  outright when the impl pointers differ, so iterators from two different
  `StringSet` instances never compare equal even for identical text. This is why
  each kind of name gets its own singleton, and why mixing pools silently
  produces "not equal" rather than an error.
- **All default-constructed iterators compare equal to each other.** That is the
  documented way to test whether an instance is initialised. Dereferencing an
  uninitialised `SharedIterator` is unchecked — `access_target()` simply
  dereferences an uninitialised `std::set` iterator.
- **Not copyable, by design.** `StringSet`'s copy constructor and assignment are
  declared private and never defined; a copy would carry elements with non-zero
  counts that no iterator of that copy references. The same reasoning explains
  `UnicodeStringAndRefCount`'s hand-written copy constructor, which resets the
  count to zero so that the copy `std::set::insert` stores starts clean.
- **No thread safety at all.** The reference count is a plain `long` incremented
  and decremented without synchronisation, and the `std::set` is mutated on
  insert and on last release. Since the real instances are process-wide
  singletons reached from `model`, `file-io` and the Python API, creating or
  destroying feature types or property names off the main thread is unsafe.
- **`GPLATES_ICU_BOOL`.** Defined here (guarded by `#ifndef`) and used to coerce
  the result of `UnicodeString::operator<` to `bool`, a leftover from when that
  comparison returned an ICU `UBool`. It leaks into every translation unit that
  includes this header.

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 46 |
| [model/Gpgim](../model/Gpgim.md) | model | 40 |
| [model/StringSetSingletons](../model/StringSetSingletons.md) | model | 40 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 28 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 26 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 26 |
| [model/Metadata](../model/Metadata.md) | model | 23 |
| [model/XmlNode](../model/XmlNode.md) | model | 18 |
| [file-io/XmlWriter](../file-io/XmlWriter.md) | file-io | 14 |
| [unit-test/StringSetTest](../unit-test/StringSetTest.md) | unit-test | 10 |
| [utils/XmlNamespaces](XmlNamespaces.md) | utils | 9 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 8 |
| [property-values/GpmlIrregularSampling](../property-values/GpmlIrregularSampling.md) | property-values | 7 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 6 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 5 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 5 |
| [model/QualifiedXmlName](../model/QualifiedXmlName.md) | model | 5 |
| [model/StringContentTypeGenerator](../model/StringContentTypeGenerator.md) | model | 5 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 5 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 4 |

*... and 19 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/StringSet.h
python scripts/gpq.py def GPlatesUtils::StringSet --body
python scripts/gpq.py uses StringSet --kind class
python scripts/gpq.py hier StringSet
```
