# GmlFile

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 650 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlFile.h` | C++ | 300 |
| `src/property-values/GmlFile.cc` | C++ | 101 |

## Overview

[[[PROSE overview unit=property-values/GmlFile tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlFile`](#gplatespropertyvaluesgmlfile) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:File". |

## Members

### `GPlatesPropertyValues::GmlFile`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlFile>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlFile\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlFile>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlFile\>. |
| `xml_attributes_type` | typedef | `std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue>` | public | — |
| `value_component_type` | typedef | `std::pair<ValueObjectType, xml_attributes_type>` | public | — |
| `composite_value_type` | typedef | `std::vector<value_component_type>` | public | — |
| `~GmlFile()` | destructor | `None` | public | — |
| `create( const composite_value_type &range_parameters_, const XsString::non_null_ptr_to_const_type &file_name_, const XsString::non_null_ptr_to_const_type &file_structure_, const boost::optional<XsString::non_null_ptr_to_const_type> &mime_type_ = boost::none, const boost::optional<XsString::non_null_ptr_to_const_type> & ...` | method | `non_null_ptr_type` | public | Create a GmlFile instance. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_range_parameters( const composite_value_type &range_parameters_)` | method | `void` | public | — |
| `set_file_name( const XsString::non_null_ptr_to_const_type &file_name_, GPlatesFileIO::ReadErrorAccumulation *read_errors = NULL)` | method | `void` | public | — |
| `set_file_structure( const XsString::non_null_ptr_to_const_type &file_structure_)` | method | `void` | public | — |
| `set_mime_type( const boost::optional<XsString::non_null_ptr_to_const_type> &mime_type_)` | method | `void` | public | — |
| `set_compression( const boost::optional<XsString::non_null_ptr_to_const_type> &compression_)` | method | `void` | public | — |
| `proxied_raw_rasters()` | method | `std::vector<RawRaster::non_null_ptr_type>` | public | If the file is a raster file, and the bands could be read, returns one proxied RawRaster for each band in that raster file. |
| `get_spatial_reference_system()` | method | `boost::optional<SpatialReferenceSystem::non_null_ptr_to_const_type>` | public | FIXME: This will be moved to its own property value once we store the raster spatial reference system in a new property value. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlFile( const composite_value_type &range_parameters_, const XsString::non_null_ptr_to_const_type &file_name_, const XsString::non_null_ptr_to_const_type &file_structure_, const boost::optional<XsString::non_null_ptr_to_const_type> &mime_type_, const boost::optional<XsString::non_null_ptr_to_const_type> &compression_, ...` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlFile( const GmlFile &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_range_parameters` | field | `composite_value_type` | private | — |
| `d_file_name` | field | `XsString::non_null_ptr_to_const_type` | private | — |
| `d_file_structure` | field | `XsString::non_null_ptr_to_const_type` | private | — |
| `d_mime_type` | field | `boost::optional<XsString::non_null_ptr_to_const_type>` | private | — |
| `d_compression` | field | `boost::optional<XsString::non_null_ptr_to_const_type>` | private | — |
| `d_proxied_raster_cache` | field | `ProxiedRasterCache::non_null_ptr_type` | private | — |
| `operator=` | field | `GmlFile` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLFILE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GmlFile tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 12 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 7 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 3 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 3 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [qt-widgets/ImportScalarField3DDialog](../qt-widgets/ImportScalarField3DDialog.md) | qt-widgets | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlFile.h
python scripts/gpq.py def GPlatesPropertyValues::GmlFile --body
python scripts/gpq.py uses GmlFile --kind class
python scripts/gpq.py hier GmlFile
```
