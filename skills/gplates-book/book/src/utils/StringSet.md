# StringSet

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 635 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/StringSet.h` | C++ | 702 |
| `src/utils/StringSet.cc` | C++ | 122 |

## Overview

[[[PROSE overview unit=utils/StringSet tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/StringSet tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
