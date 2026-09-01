# GmlDataBlock

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 907 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlDataBlock.h` | C++ | 207 |
| `src/property-values/GmlDataBlock.cc` | C++ | 59 |

## Overview

`GmlDataBlock` is the `GPlatesModel::PropertyValue` for GML's `gml:DataBlock`: a
sequence (`tuple_list_type`) of `GmlDataBlockCoordinateList` elements, each one a
named list of scalar coordinate values. It is how GPlates attaches scalar coverages —
per-point data such as crustal thickness or strain — to a geometry, with one
`GmlDataBlockCoordinateList` per scalar field so a single point geometry can carry
several parallel scalar sequences at once.

Like other property values, it is stack-unconstructible (protected constructors) and
non-copy-assignable; all copying goes through `clone()`/`deep_clone()`. `deep_clone()`
differs from `clone()` only in that it also clones each element of the tuple list
rather than sharing the child `GmlDataBlockCoordinateList` pointers, since those
children are themselves reference-counted and mutable.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlDataBlock`](#gplatespropertyvaluesgmldatablock) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:DataBlock". |

## Members

### `GPlatesPropertyValues::GmlDataBlock`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlDataBlock>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlDataBlock\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlDataBlock>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlDataBlock\>. |
| `tuple_list_type` | typedef | `std::vector<GmlDataBlockCoordinateList::non_null_ptr_to_const_type>` | public | The type of the sequence of GmlDataBlockCoordinateList instances. |
| `~GmlDataBlock()` | destructor | `None` | public | — |
| `create()` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `is_empty()` | method | `bool` | public | — |
| `tuple_list_begin()` | method | `tuple_list_type::const_iterator` | public | — |
| `tuple_list_end()` | method | `tuple_list_type::const_iterator` | public | — |
| `tuple_list_clear()` | method | `void` | public | — |
| `tuple_list_push_back( const GmlDataBlockCoordinateList::non_null_ptr_to_const_type &elem)` | method | `void` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlDataBlock()` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlDataBlock( const GmlDataBlock &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_tuple_list` | field | `tuple_list_type` | private | — |
| `operator=` | field | `GmlDataBlock` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLDATABLOCK_H` | macro | `None` | — |

## Notes

`tuple_list_clear()` and `tuple_list_push_back()` both call `update_instance_id()`,
so mutating the tuple list in place is tracked the same way as replacing the whole
property value. `print_to()` is a stub (`"{ GmlDataBlock }"`) rather than a real
dump of the contained coordinate lists.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 10 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 9 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 9 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 8 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 5 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 4 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 4 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 3 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 3 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 2 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlDataBlock.h
python scripts/gpq.py def GPlatesPropertyValues::GmlDataBlock --body
python scripts/gpq.py uses GmlDataBlock --kind class
python scripts/gpq.py hier GmlDataBlock
```
