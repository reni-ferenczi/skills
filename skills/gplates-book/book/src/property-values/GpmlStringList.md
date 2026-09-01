# GpmlStringList

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 535 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlStringList.h` | C++ | 354 |
| `src/property-values/GpmlStringList.cc` | C++ | 45 |

## Overview

[[[PROSE overview unit=property-values/GpmlStringList tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlStringList`](#gplatespropertyvaluesgpmlstringlist) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | A list of XsString instances in a "gpml:StringList". |

## Members

### `GPlatesPropertyValues::GpmlStringList`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlStringList>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlStringList\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlStringList>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlStringList\>. |
| `string_list_type` | typedef | `std::vector<TextContent>` | public | The type used to contain the list of strings. |
| `const_iterator` | typedef | `string_list_type::const_iterator` | public | The type used to iterate over the list of strings. |
| `iterator` | typedef | `string_list_type::iterator` | public | — |
| `~GpmlStringList()` | destructor | `None` | public | — |
| `create_empty()` | method | `non_null_ptr_type` | public | Create a new GpmlStringList instance, leaving its elements empty. |
| `create_copy( const StringContainer &strings)` | method | `non_null_ptr_type` | public | Create a new GpmlStringList instance, then copy the values from strings into the GpmlStringList. |
| `create_copy( StringIter strings_begin_, StringIter strings_end_)` | method | `non_null_ptr_type` | public | Create a new GpmlStringList instance, then copy the values from the iterator range \[ strings\_begin\_, strings\_end\_ ) into the GpmlStringList. |
| `create_swap( string_list_type &strings_to_swap)` | method | `non_null_ptr_type` | public | Create a new GpmlStringList instance, then swap the contents of the supplied container strings\_to\_swap into the GpmlStringList, leaving strings\_to\_swap empty. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `GpmlStringList::non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `is_empty()` | method | `bool` | public | — |
| `size()` | method | `string_list_type::size_type` | public | — |
| `begin()` | method | `const_iterator` | public | — |
| `end()` | method | `const_iterator` | public | — |
| `push_back( const GPlatesUtils::UnicodeString &s)` | method | `void` | public | — |
| `push_back( const TextContent &tc)` | method | `void` | public | — |
| `insert( const_iterator pos, const GPlatesUtils::UnicodeString &s)` | method | `const_iterator` | public | — |
| `insert( const_iterator pos, const TextContent &tc)` | method | `const_iterator` | public | — |
| `erase( string_list_type::const_iterator pos)` | method | `const_iterator` | public | — |
| `clear()` | method | `void` | public | — |
| `swap( string_list_type &strings_)` | method | `void` | public | Swap the contents of strings with the contents of the GpmlStringList. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlStringList()` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlStringList( StringIter strings_begin_, StringIter strings_end_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlStringList( const GpmlStringList &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `convert_to_non_const( const_iterator iter)` | method | `string_list_type::iterator` | protected | — |
| `d_strings` | field | `string_list_type` | private | — |
| `operator=` | field | `GpmlStringList` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLSTRINGLIST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlStringList tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditStringListWidget](../qt-widgets/EditStringListWidget.md) | qt-widgets | 22 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 10 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 10 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 9 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 7 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 5 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 2 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 1 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 1 |
| [qt-widgets/EditWidgetChooser](../qt-widgets/EditWidgetChooser.md) | qt-widgets | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlStringList.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlStringList --body
python scripts/gpq.py uses GpmlStringList --kind class
python scripts/gpq.py hier GpmlStringList
```
