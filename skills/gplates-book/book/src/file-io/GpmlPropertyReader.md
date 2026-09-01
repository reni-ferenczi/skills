# GpmlPropertyReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 214 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlPropertyReader.h` | C++ | 254 |
| `src/file-io/GpmlPropertyReader.cc` | C++ | 822 |

## Overview

`GpmlPropertyReader` reads one named feature property, validating it against a
single `GpgimProperty` rather than a hard-coded schema: `create` binds a reader to
one GPGIM property definition, and `read_properties` scans a feature's XML element
for all children with that property name, checking the property's multiplicity
(`ZERO_OR_ONE`, `ONE`, `ONE_OR_MORE`, ...) and reporting `NecessaryPropertyNotFound`
or `DuplicateProperty` read errors when the count is wrong. Because GPML wraps a
property's structural type in time-dependent structures such as
`gpml:ConstantValue`, `gpml:IrregularSampling` or `gpml:PiecewiseAggregation`, most
of the private machinery — `read_property_structural_type`,
`convert_unwrapped_to_time_dependent_wrapped_structural_type` and its inverse,
`get_time_dependent_wrapped_structural_type` — exists to reconcile whatever wrapping
(or lack of it) is actually present in the file against what the GPGIM property
declares.

A property whose name is recognised but whose structural type the GPGIM rejects
is not dropped: it is wrapped in an `UninterpretedPropertyValue` so it round-trips
unchanged when the feature collection is written back out. Only a property name
the GPGIM does not accept at all yields no property value. This class is created
per property by `GpmlFeatureReaderFactory`/`GpmlFeatureReaderImpl` machinery built
from the GPGIM, and it delegates the actual structural parsing to a
`GpmlPropertyStructuralTypeReader`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GpmlPropertyReader`](#gplatesfileiogpmlpropertyreader) | class | [`GPlatesUtils::ReferenceCount<GpmlPropertyReader>`](../utils/ReferenceCount.md) | — | 0 | Reads feature properties by referring to the GPGIM (specifically a GpgimProperty). |

## Members

### `GPlatesFileIO::GpmlPropertyReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlPropertyReader>` | public | A convenience typedef for a shared pointer to a non-const GpmlPropertyReader. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlPropertyReader>` | public | A convenience typedef for a shared pointer to a const GpmlPropertyReader. |
| `xml_node_seq_type` | typedef | `std::list<GPlatesModel::XmlNode::non_null_ptr_type>` | public | Typedef for a sequence of XmlNode objects. |
| `create( const GPlatesModel::GpgimProperty::non_null_ptr_to_const_type &gpgim_property, const GpmlPropertyStructuralTypeReader::non_null_ptr_to_const_type &property_structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version)` | method | `non_null_ptr_type` | public | Creates a GpmlPropertyReader from the specified GPGIM property. |
| `read_properties( std::vector<GPlatesModel::PropertyValue::non_null_ptr_type> &property_values, const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `void` | public | Creates and reads feature properties that match the GPGIM feature property specification passed into constructor. |
| `StructuralReaderType` | struct | `None` | private | Associates a structural type with its structural reader function. |
| `structural_reader_type_seq_type` | typedef | `std::vector<StructuralReaderType>` | private | Typedef for a sequence of structural reader types. |
| `d_gpgim_property` | field | `GPlatesModel::GpgimProperty::non_null_ptr_to_const_type` | private | The GPGIM property. |
| `d_property_structural_type_reader` | field | `GpmlPropertyStructuralTypeReader::non_null_ptr_to_const_type` | private | Used to read property structural types from a GPML file. |
| `d_gpml_version` | field | `GPlatesModel::GpgimVersion` | private | The version of the GPGIM used to create the GPML file being read. |
| `d_structural_reader_types` | field | `structural_reader_type_seq_type` | private | Sequence of allowed structural types (and associated reader functions). |
| `d_constant_value_structural_reader_function` | field | `GpmlPropertyStructuralTypeReader::structural_type_reader_function_type` | private | Structural reader function for 'gpml:ConstantValue'. |
| `d_irregular_sampling_structural_reader_function` | field | `GpmlPropertyStructuralTypeReader::structural_type_reader_function_type` | private | Structural reader function for 'gpml:IrregularSampling'. |
| `d_piecewise_aggregation_structural_reader_function` | field | `GpmlPropertyStructuralTypeReader::structural_type_reader_function_type` | private | Structural reader function for 'gpml:PiecewiseAggregation'. |
| `GpmlPropertyReader( const GPlatesModel::GpgimProperty::non_null_ptr_to_const_type &gpgim_property, const GpmlPropertyStructuralTypeReader::non_null_ptr_to_const_type &property_structural_type_reader, const GPlatesModel::GpgimVersion &gpml_version)` | constructor | `None` | private | — |
| `read_property( const GPlatesModel::XmlElementNode::non_null_ptr_type &property_xml_element, GpmlReaderUtils::ReaderParams &reader_params)` | method | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | Attempt to read the property if it matches the GPGIM. |
| `read_property_structural_type( const GPlatesModel::XmlElementNode::non_null_ptr_type &property_xml_element, boost::optional<GPlatesModel::XmlElementNode::non_null_ptr_type> structural_xml_element, GpmlReaderUtils::ReaderParams &reader_params)` | method | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | Attempt to read the property structural type if it matches the GPGIM. |
| `convert_unwrapped_to_time_dependent_wrapped_structural_type( const GPlatesModel::XmlElementNode::non_null_ptr_type &property_xml_element, boost::optional<GPlatesModel::XmlElementNode::non_null_ptr_type> structural_xml_element, GpmlReaderUtils::ReaderParams &reader_params)` | method | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | Attempt to convert an unwrapped (structural) type to a time-dependent wrapped structural type. |
| `convert_time_dependent_wrapped_to_unwrapped_structural_type( const GPlatesModel::XmlElementNode::non_null_ptr_type &property_xml_element, const GPlatesModel::XmlElementNode::non_null_ptr_type &structural_xml_element, GpmlReaderUtils::ReaderParams &reader_params)` | method | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | Attempt to convert a time-dependent wrapped structural type to an unwrapped structural type. |
| `get_time_dependent_wrapped_structural_type( const GPlatesModel::XmlElementNode::non_null_ptr_type &structural_xml_element, GpmlReaderUtils::ReaderParams &reader_params)` | method | `boost::optional<GPlatesPropertyValues::StructuralType>` | private | Returns the structural type, wrapped in time-dependent structure, if accepted by the GPGIM. |
| `get_structural_creation_function( const GPlatesModel::XmlElementNode::non_null_ptr_type &structural_xml_element)` | method | `boost::optional<GpmlPropertyStructuralTypeReader::structural_type_reader_function_type>` | private | Returns the structural reader function for the specified (non-time-dependent) structural element. |
| `read_structural_type( const GPlatesModel::XmlElementNode::non_null_ptr_type &property_xml_element, const GpmlPropertyStructuralTypeReader::structural_type_reader_function_type &structural_creation_function, GpmlReaderUtils::ReaderParams &reader_params)` | method | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | Attempt to read (non-time-dependent) structural type with the specified structural reader function. |
| `read_unspecified_structural_type( const GPlatesModel::XmlElementNode::non_null_ptr_type &property_xml_element, GpmlReaderUtils::ReaderParams &reader_params, boost::optional<unsigned int &> structural_creation_type_index = boost::none)` | method | `boost::optional<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | Attempt to read (non-time-dependent) structural type that has no structural type specified in the GPML file (as a structural XML element). |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_GPMLPROPERTYREADER_H` | macro | `None` | — |

## Notes

Processed XML property nodes are always erased from
`unprocessed_feature_property_xml_nodes`, even when the result is an
`UninterpretedPropertyValue` rather than an interpreted one — callers must not
assume a node surviving in that list means the property name was unrecognised in
some other sense. `d_structural_reader_types` is guaranteed non-empty by the GPGIM
property that constructed this reader. `d_gpml_version` records the GPGIM version the file was written against and is
threaded through to every structural-type creation call
(`GpmlPropertyStructuralTypeReaderUtils::create_*`), since parsing some structural
elements depends on which GPGIM version produced them.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlUpgradeReaderUtils](GpmlUpgradeReaderUtils.md) | file-io | 11 |
| [file-io/GpmlFeatureReaderImpl](GpmlFeatureReaderImpl.md) | file-io | 8 |
| [file-io/GpmlFeatureReaderFactory](GpmlFeatureReaderFactory.md) | file-io | 3 |
| [model/GpgimProperty](../model/GpgimProperty.md) | model | 3 |
| [model/GpgimFeatureClass](../model/GpgimFeatureClass.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlPropertyReader.h
python scripts/gpq.py def GPlatesFileIO::GpmlPropertyReader --body
python scripts/gpq.py uses GpmlPropertyReader --kind class
python scripts/gpq.py hier GpmlPropertyReader
```
