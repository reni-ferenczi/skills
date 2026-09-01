# GpmlOldPlatesHeader

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 216 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlOldPlatesHeader.h` | C++ | 488 |
| `src/property-values/GpmlOldPlatesHeader.cc` | C++ | 104 |

## Overview

`GpmlOldPlatesHeader` is a `GPlatesModel::PropertyValue` that carries the fixed-format header fields of a PLATES4 line-format record (region, reference and string numbers, geographic description, plate id, ages of appearance/disappearance, data type code, conjugate plate id, colour code and point count) so that legacy PLATES data can be read into the GPML model and written back out without losing those fields. Every setter calls `update_instance_id()`, following the mutable-property-value convention used throughout `property-values`.

`old_feature_id()` reformats the stored fields back into the fixed-width, underscore-separated feature id string used by GPlates 0.8 (for example `gplates_00_00_0000_..._999.0_-999.0_RI_0000_000_`), reproducing the exact field widths and padding characters (zero-padded numeric fields, space-padded age fields) that the old format relied on. `print_to()` simply delegates to it, so streaming this property value shows the reconstructed legacy id rather than its individual fields.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlOldPlatesHeader`](#gplatespropertyvaluesgpmloldplatesheader) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlOldPlatesHeader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlOldPlatesHeader>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlOldPlatesHeader\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlOldPlatesHeader>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlOldPlatesHeader\>. |
| `~GpmlOldPlatesHeader()` | destructor | `None` | public | — |
| `create( unsigned int region_number, unsigned int reference_number, unsigned int string_number, const GPlatesUtils::UnicodeString &geographic_description, GPlatesModel::integer_plate_id_type plate_id_number, const double &age_of_appearance, const double &age_of_disappearance, const GPlatesUtils::UnicodeString &data_type ...` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `region_number()` | method | `unsigned int` | public | — |
| `set_region_number( const unsigned int &i)` | method | `void` | public | Set the region number to i. |
| `reference_number()` | method | `unsigned int` | public | — |
| `set_reference_number( const unsigned int &i)` | method | `void` | public | Set the reference number to i. |
| `string_number()` | method | `unsigned int` | public | — |
| `set_string_number( const unsigned int &i)` | method | `void` | public | Set the string number to i. |
| `set_geographic_description( const GPlatesUtils::UnicodeString &us)` | method | `void` | public | Set the geographic description to us. |
| `plate_id_number()` | method | `GPlatesModel::integer_plate_id_type` | public | — |
| `set_plate_id_number( const GPlatesModel::integer_plate_id_type &i)` | method | `void` | public | Set the plate id number to i. |
| `set_age_of_appearance( const double &d)` | method | `void` | public | Set the age of appearance to d. |
| `set_age_of_disappearance( const double &d)` | method | `void` | public | Set the age of disappearance to d. |
| `set_data_type_code( const GPlatesUtils::UnicodeString &us)` | method | `void` | public | Set the data type code to us. |
| `data_type_code_number()` | method | `unsigned int` | public | — |
| `set_data_type_code_number( const unsigned int &i)` | method | `void` | public | Set the data type code number to i. |
| `set_data_type_code_number_additional( const GPlatesUtils::UnicodeString &us)` | method | `void` | public | Set the data type code number (additional) string to us. |
| `conjugate_plate_id_number()` | method | `GPlatesModel::integer_plate_id_type` | public | — |
| `set_conjugate_plate_id_number( const GPlatesModel::integer_plate_id_type &i)` | method | `void` | public | Set the conjugate plate id number to i. |
| `colour_code()` | method | `unsigned int` | public | — |
| `set_colour_code( const unsigned int &i)` | method | `void` | public | Set the colour code to i. |
| `number_of_points()` | method | `unsigned int` | public | — |
| `set_number_of_points( const unsigned int &i)` | method | `void` | public | Set the number of points to i. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `old_feature_id()` | method | `GPlatesUtils::UnicodeString` | public | — |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlOldPlatesHeader( unsigned int region_number_, unsigned int reference_number_, unsigned int string_number_, const GPlatesUtils::UnicodeString &geographic_description_, GPlatesModel::integer_plate_id_type plate_id_number_, const double &age_of_appearance_, const double &age_of_disappearance_, const GPlatesUtils::Unic ...` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlOldPlatesHeader( const GpmlOldPlatesHeader &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_region_number` | field | `unsigned int` | private | — |
| `d_reference_number` | field | `unsigned int` | private | — |
| `d_string_number` | field | `unsigned int` | private | — |
| `d_geographic_description` | field | `TextContent` | private | — |
| `d_plate_id_number` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_age_of_appearance` | field | `double` | private | — |
| `d_age_of_disappearance` | field | `double` | private | — |
| `d_data_type_code` | field | `TextContent` | private | — |
| `d_data_type_code_number` | field | `unsigned int` | private | — |
| `d_data_type_code_number_additional` | field | `TextContent` | private | — |
| `d_conjugate_plate_id_number` | field | `GPlatesModel::integer_plate_id_type` | private | — |
| `d_colour_code` | field | `unsigned int` | private | — |
| `d_number_of_points` | field | `unsigned int` | private | — |
| `operator=` | field | `GpmlOldPlatesHeader` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLOLDPLATESHEADER_H` | macro | `None` | — |

## Notes

The field widths and fill characters in `old_feature_id()` (zero-fill for most numeric fields, space-fill for the two age fields) exactly reproduce the old PLATES4/GPlates 0.8 id layout; changing them would break round-tripping of feature ids for data exported in that legacy style.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditOldPlatesHeaderWidget](../qt-widgets/EditOldPlatesHeaderWidget.md) | qt-widgets | 22 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 9 |
| [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) | file-io | 9 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 8 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 8 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 6 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 5 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [file-io/PlatesLineFormatHeaderVisitor](../file-io/PlatesLineFormatHeaderVisitor.md) | file-io | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) | file-io | 1 |
| [file-io/GMTFormatWriter](../file-io/GMTFormatWriter.md) | file-io | 1 |
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 1 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [qt-widgets/EditWidgetChooser](../qt-widgets/EditWidgetChooser.md) | qt-widgets | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlOldPlatesHeader.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlOldPlatesHeader --body
python scripts/gpq.py uses GpmlOldPlatesHeader --kind class
python scripts/gpq.py hier GpmlOldPlatesHeader
```
