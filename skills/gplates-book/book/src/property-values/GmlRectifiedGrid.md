# GmlRectifiedGrid

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 621 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlRectifiedGrid.h` | C++ | 330 |
| `src/property-values/GmlRectifiedGrid.cc` | C++ | 156 |

## Overview

[[[PROSE overview unit=property-values/GmlRectifiedGrid tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlRectifiedGrid`](#gplatespropertyvaluesgmlrectifiedgrid) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:RectifiedGrid". |

## Members

### `GPlatesPropertyValues::GmlRectifiedGrid`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlRectifiedGrid>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlRectifiedGrid\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlRectifiedGrid>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlRectifiedGrid\>. |
| `axes_list_type` | typedef | `std::vector<XsString::non_null_ptr_to_const_type>` | public | — |
| `offset_vector_type` | typedef | `std::vector<double>` | public | — |
| `offset_vector_list_type` | typedef | `std::vector<offset_vector_type>` | public | — |
| `xml_attributes_type` | typedef | `std::map<GPlatesModel::XmlAttributeName, GPlatesModel::XmlAttributeValue>` | public | — |
| `~GmlRectifiedGrid()` | destructor | `None` | public | — |
| `create( const GmlGridEnvelope::non_null_ptr_to_const_type &limits_, const axes_list_type &axes_, const GmlPoint::non_null_ptr_to_const_type &origin_, const offset_vector_list_type &offset_vectors_, const xml_attributes_type &xml_attributes_)` | method | `non_null_ptr_type` | public | Create a GmlRectifiedGrid instance. |
| `create( const Georeferencing::non_null_ptr_to_const_type &georeferencing, unsigned int raster_width, unsigned int raster_height, const xml_attributes_type &xml_attributes_)` | method | `non_null_ptr_type` | public | Convenience function for creating a GmlRectifiedGrid from georeferencing information, and raster width and height. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_limits( const GmlGridEnvelope::non_null_ptr_to_const_type &limits_)` | method | `void` | public | Sets the internal limits. |
| `set_axes( const axes_list_type &axes_)` | method | `void` | public | Sets the internal axes. |
| `set_origin( const GmlPoint::non_null_ptr_to_const_type &origin_)` | method | `void` | public | Sets the internal origin. |
| `set_offset_vectors( const offset_vector_list_type &offset_vectors_)` | method | `void` | public | — |
| `set_xml_attributes( const xml_attributes_type &xml_attributes_)` | method | `void` | public | — |
| `convert_to_georeferencing()` | method | `boost::optional<Georeferencing::non_null_ptr_to_const_type>` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlRectifiedGrid( const GmlGridEnvelope::non_null_ptr_to_const_type &limits_, const axes_list_type &axes_, const GmlPoint::non_null_ptr_to_const_type &origin_, const offset_vector_list_type &offset_vectors_, const xml_attributes_type xml_attributes_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlRectifiedGrid( const GmlRectifiedGrid &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_limits` | field | `GmlGridEnvelope::non_null_ptr_to_const_type` | private | — |
| `d_axes` | field | `axes_list_type` | private | — |
| `d_origin` | field | `GmlPoint::non_null_ptr_to_const_type` | private | — |
| `d_offset_vectors` | field | `offset_vector_list_type` | private | — |
| `d_xml_attributes` | field | `xml_attributes_type` | private | — |
| `d_cached_georeferencing` | field | `boost::optional<Georeferencing::non_null_ptr_to_const_type>` | private | — |
| `operator=` | field | `GmlRectifiedGrid` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLRECTIFIEDGRID_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GmlRectifiedGrid tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 7 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 4 |
| [app-logic/ExtractRasterFeatureProperties](../app-logic/ExtractRasterFeatureProperties.md) | app-logic | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlRectifiedGrid.h
python scripts/gpq.py def GPlatesPropertyValues::GmlRectifiedGrid --body
python scripts/gpq.py uses GmlRectifiedGrid --kind class
python scripts/gpq.py hier GmlRectifiedGrid
```
