# GpmlScalarField3DFile

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1213 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlScalarField3DFile.h` | C++ | 191 |
| `src/property-values/GpmlScalarField3DFile.cc` | C++ | 44 |

## Overview

Encodes a reference to a 3D scalar field file in the GPML model as a property value. It holds a filename as an `XsString` and provides access via `file_name()` and modification via `set_file_name()`. When the filename is updated, the property's instance ID is marked as changed. This class follows the standard property value pattern with heap-only allocation and visitor-based traversal support.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlScalarField3DFile`](#gplatespropertyvaluesgpmlscalarfield3dfile) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue referencing a GPlates-specific 3D scalar field file. |

## Members

### `GPlatesPropertyValues::GpmlScalarField3DFile`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlScalarField3DFile>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlScalarField3DFile\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlScalarField3DFile>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlScalarField3DFile\>. |
| `~GpmlScalarField3DFile()` | destructor | `None` | public | — |
| `file_name_type` | typedef | `XsString::non_null_ptr_to_const_type` | public | — |
| `create( const file_name_type &filename_)` | method | `non_null_ptr_type` | public | Create a GpmlScalarField3DFile instance from a filename. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_file_name( const file_name_type &filename_)` | method | `void` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlScalarField3DFile( const file_name_type &filename_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlScalarField3DFile( const GpmlScalarField3DFile &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_filename` | field | `file_name_type` | private | — |
| `operator=` | field | `GpmlScalarField3DFile` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTY_VALUES_GPMLSCALARFIELD3DFILE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [app-logic/ExtractScalarField3DFeatureProperties](../app-logic/ExtractScalarField3DFeatureProperties.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 1 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlScalarField3DFile.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlScalarField3DFile --body
python scripts/gpq.py uses GpmlScalarField3DFile --kind class
python scripts/gpq.py hier GpmlScalarField3DFile
```
