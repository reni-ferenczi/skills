# GmlRectifiedGrid

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 621 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlRectifiedGrid.h` | C++ | 330 |
| `src/property-values/GmlRectifiedGrid.cc` | C++ | 156 |

## Overview

`GmlRectifiedGrid` is the `GPlatesModel::PropertyValue` for `gml:RectifiedGrid`,
GML's way of describing a raster's placement in space: a `GmlGridEnvelope`
giving the grid's index limits, a list of axis names (`d_axes`), a `GmlPoint`
origin, and a list of per-axis offset vectors. It is also the bridge between
GML's generic grid model and GPlates' own `Georeferencing`, which is what the
rest of the raster pipeline actually consumes. The two-argument `create()`
overload builds a `GmlRectifiedGrid` directly from a `Georeferencing` plus a
raster's width and height — assuming longitude/latitude axes and placing the
origin at the georeferencing's top-left corner — while `convert_to_georeferencing()`
does the inverse, reconstructing a `Georeferencing` from the grid's own
axes and offset vectors when one wasn't supplied at construction.

The class does not validate that the dimensionality of the axes list, the
offset vectors and the origin all agree with each other or with any `dimension`
XML attribute present — the header states this explicitly, so a caller
supplying an inconsistent combination will not be caught here.

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

- `convert_to_georeferencing()` caches its result in the `mutable`
  `d_cached_georeferencing`; `set_origin()` and `set_offset_vectors()` each
  invalidate that cache (reset it to `boost::none`) since both feed into the
  derived `Georeferencing`, but `set_limits()`, `set_axes()` and
  `set_xml_attributes()` do not, because those fields don't affect it.
  `convert_to_georeferencing()` also gives up and returns `boost::none` if
  `d_offset_vectors` does not have exactly 2 entries.
- The two-argument raster `create()` overload populates
  `d_cached_georeferencing` with the `Georeferencing` it was given, so a
  `GmlRectifiedGrid` built that way returns it from `convert_to_georeferencing()`
  without recomputation, even before any offset vectors are inspected.
- `convert_to_georeferencing()` reads the origin via `d_origin->point_2d()`
  rather than `point_in_lat_lon()`, deliberately skipping latitude/longitude
  range validation: georeferenced origins may be in a projected coordinate
  system, or offset by half a pixel for a gridline-registered global raster,
  and so can legitimately fall outside valid lat/lon ranges.

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
