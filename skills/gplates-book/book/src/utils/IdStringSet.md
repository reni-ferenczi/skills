# IdStringSet

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 490 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/IdStringSet.h` | C++ | 684 |
| `src/utils/IdStringSet.cc` | C++ | 126 |

## Overview

[[[PROSE overview unit=utils/IdStringSet tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/IdStringSet tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
