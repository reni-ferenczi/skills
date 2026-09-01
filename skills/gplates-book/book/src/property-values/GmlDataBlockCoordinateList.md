# GmlDataBlockCoordinateList

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 692 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlDataBlockCoordinateList.h` | C++ | 314 |
| `src/property-values/GmlDataBlockCoordinateList.cc` | C++ | 69 |

## Overview

[[[PROSE overview unit=property-values/GmlDataBlockCoordinateList tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlDataBlockCoordinateList`](#gplatespropertyvaluesgmldatablockcoordinatelist) | class | [`GPlatesUtils::ReferenceCount<GmlDataBlockCoordinateList>`](../utils/ReferenceCount.md) | — | 0 | This associates a ValueObjectType instance with a sequence of "i-th" coordinates from a \<gml:tupleList\> property in a "gml:DataBlock". |

## Members

### `GPlatesPropertyValues::GmlDataBlockCoordinateList`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlDataBlockCoordinateList>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlDataBlockCoordinateList\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlDataBlockCoordinateList>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlDataBlockCoordinateList\>. |
| `xml_attributes_type` | typedef | `std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue>` | public | The type which contains XML attribute names and values. |
| `coordinate_list_type` | typedef | `std::vector<double>` | public | The type containing the coordinates. |
| `~GmlDataBlockCoordinateList()` | destructor | `None` | public | — |
| `create_empty( const ValueObjectType &value_object_type_, const xml_attributes_type &value_object_xml_attributes_, coordinate_list_type::size_type list_len)` | method | `non_null_ptr_type` | public | Create a new GmlDataBlockCoordinateList instance, leaving its coordinates empty (but pre-allocated to the capacity list\_len). |
| `create_copy( const ValueObjectType &value_object_type_, const xml_attributes_type &value_object_xml_attributes_, CoordinateIter coordinates_begin_, CoordinateIter coordinates_end_)` | method | `non_null_ptr_type` | public | Create a new GmlDataBlockCoordinateList instance, then copy the values from the iterator range from coordinates\_begin\_ to coordinates\_end\_ into the GmlDataBlockCoordinateList. |
| `create_swap( const ValueObjectType &value_object_type_, const xml_attributes_type &value_object_xml_attributes_, coordinate_list_type &coordinates_to_swap)` | method | `non_null_ptr_type` | public | Create a new GmlDataBlockCoordinateList instance, then swap the contents of the supplied container coordinates\_to\_swap into the GmlDataBlockCoordinateList, leaving coordinates\_to\_swap empty. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `coordinates_len()` | method | `coordinate_list_type::size_type` | public | — |
| `coordinates_begin()` | method | `coordinate_list_type::const_iterator` | public | — |
| `coordinates_end()` | method | `coordinate_list_type::const_iterator` | public | — |
| `coordinates_push_back( const double &coord)` | method | `void` | public | NOTE: No non-const iterators provided yet -- When we need them, we should define an iterator wrapper which creates new revisions of this class when appropriate. |
| `coordinates_assign( CoordinateIter begin, CoordinateIter end)` | method | `void` | public | — |
| `operator==( const GmlDataBlockCoordinateList &other)` | operator | `bool` | public | — |
| `GmlDataBlockCoordinateList( const ValueObjectType &value_object_type_, const xml_attributes_type &value_object_xml_attributes_, coordinate_list_type::size_type list_len)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlDataBlockCoordinateList( const ValueObjectType &value_object_type_, const xml_attributes_type &value_object_xml_attributes_, CoordinateIter coordinates_begin_, CoordinateIter coordinates_end_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlDataBlockCoordinateList( const ValueObjectType &value_object_type_, const xml_attributes_type &value_object_xml_attributes_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlDataBlockCoordinateList( const GmlDataBlockCoordinateList &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_value_object_type` | field | `ValueObjectType` | private | — |
| `d_value_object_xml_attributes` | field | `xml_attributes_type` | private | — |
| `d_coordinates` | field | `coordinate_list_type` | private | — |
| `operator=` | field | `GmlDataBlockCoordinateList` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `double_eq( double d1, double d2)` | function | `bool` | — |
| `operator==( const GmlDataBlockCoordinateList &other)` | operator | `bool` | — |
| `GPLATES_PROPERTYVALUES_GMLDATABLOCKCOORDINATELIST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GmlDataBlockCoordinateList tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 25 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 18 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 18 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 10 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 10 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 9 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 7 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 5 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 5 |
| [app-logic/ReconstructScalarCoverageLayerProxy](../app-logic/ReconstructScalarCoverageLayerProxy.md) | app-logic | 4 |
| [property-values/GmlDataBlock](GmlDataBlock.md) | property-values | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlDataBlockCoordinateList.h
python scripts/gpq.py def GPlatesPropertyValues::GmlDataBlockCoordinateList --body
python scripts/gpq.py uses GmlDataBlockCoordinateList --kind class
python scripts/gpq.py hier GmlDataBlockCoordinateList
```
