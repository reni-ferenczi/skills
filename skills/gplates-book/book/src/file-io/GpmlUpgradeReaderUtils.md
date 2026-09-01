# GpmlUpgradeReaderUtils

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 417 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlUpgradeReaderUtils.h` | C++ | 425 |
| `src/file-io/GpmlUpgradeReaderUtils.cc` | C++ | 1034 |

## Overview

[[[PROSE overview unit=file-io/GpmlUpgradeReaderUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::(anonymous)::topological_sections_seq_type`](#gplatesfileioanonymoustopological_sections_seq_type) | typedef | — | — | 0 | Typedef for a sequence of topological sections. |
| [`GPlatesFileIO::(anonymous)::OldVersionPropertyValueFinder`](#gplatesfileioanonymousoldversionpropertyvaluefinder) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Find a OldVersionPropertyValue property value given a PropertyValue. |
| [`GPlatesFileIO::GpmlUpgradeReaderUtils::PropertyRename`](#gplatesfileiogpmlupgradereaderutilspropertyrename) | struct | — | — | 0 | Structure used when renaming a GPGIM property. |
| [`GPlatesFileIO::GpmlUpgradeReaderUtils::RenamePropertyFeatureReaderImpl`](#gplatesfileiogpmlupgradereaderutilsrenamepropertyfeaturereaderimpl) | class | [`GpmlFeatureReaderImpl`](GpmlFeatureReaderImpl.md) | — | 0 | A feature reader that delegates feature reading to another reader and then renames properties, in the read feature, matching a specified property name. |
| [`GPlatesFileIO::GpmlUpgradeReaderUtils::RemovePropertyFeatureReaderImpl`](#gplatesfileiogpmlupgradereaderutilsremovepropertyfeaturereaderimpl) | class | [`GpmlFeatureReaderImpl`](GpmlFeatureReaderImpl.md) | — | 0 | A feature reader that delegates feature reading to another reader and then removes properties, in the read feature, matching a specified property name. |
| [`GPlatesFileIO::GpmlUpgradeReaderUtils::ChangeFeatureTypeFeatureReaderImpl`](#gplatesfileiogpmlupgradereaderutilschangefeaturetypefeaturereaderimpl) | class | [`GpmlFeatureReaderImpl`](GpmlFeatureReaderImpl.md) | — | 0 | A feature reader that delegates feature reading to another reader and then changes the feature type. |
| [`GPlatesFileIO::GpmlUpgradeReaderUtils::TopologicalNetworkFeatureReaderUpgrade_1_6_319`](#gplatesfileiogpmlupgradereaderutilstopologicalnetworkfeaturereaderupgrade_1_6_319) | class | [`GpmlFeatureReaderImpl`](GpmlFeatureReaderImpl.md) | — | 0 | This feature reader handles changes to 'gpml:TopologicalNetwork' made in GPGIM version 1.6.319. |
| [`GPlatesFileIO::GpmlUpgradeReaderUtils::CrustalThinningFactorUpgrade_1_6_338`](#gplatesfileiogpmlupgradereaderutilscrustalthinningfactorupgrade_1_6_338) | class | [`GpmlFeatureReaderImpl`](GpmlFeatureReaderImpl.md) | — | 0 | A feature reader that updates any crustal thinning factors in scalar coverage. |

## Members

### `GPlatesFileIO::(anonymous)::topological_sections_seq_type`

*None.*

### `GPlatesFileIO::(anonymous)::OldVersionPropertyValueFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_old_version_property_value( const GPlatesModel::PropertyValue &property_value)` | method | `boost::optional<const GPlatesPropertyValues::OldVersionPropertyValue &>` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | private | — |
| `visit_old_version_property_value( const GPlatesPropertyValues::OldVersionPropertyValue &old_version_prop_value)` | method | `void` | private | — |
| `d_old_version_property_value` | field | `boost::optional<const GPlatesPropertyValues::OldVersionPropertyValue &>` | private | — |

### `GPlatesFileIO::GpmlUpgradeReaderUtils::PropertyRename`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PropertyRename( const GPlatesModel::PropertyName &old_property_name_, const GPlatesModel::PropertyName &new_property_name_)` | constructor | `None` | public | — |
| `old_property_name` | field | `GPlatesModel::PropertyName` | public | — |
| `new_property_name` | field | `GPlatesModel::PropertyName` | public | — |

### `GPlatesFileIO::GpmlUpgradeReaderUtils::RenamePropertyFeatureReaderImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RenamePropertyFeatureReaderImpl>` | public | A convenience typedef for a shared pointer to a non-const RenamePropertyFeatureReaderImpl. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RenamePropertyFeatureReaderImpl>` | public | A convenience typedef for a shared pointer to a const RenamePropertyFeatureReaderImpl. |
| `create( const GPlatesModel::PropertyName &from_property_name, const GPlatesModel::PropertyName &to_property_name, const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | method | `non_null_ptr_type` | public | Creates a RenamePropertyFeatureReaderImpl. |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | — |
| `d_feature_reader` | field | `GpmlFeatureReaderImpl::non_null_ptr_to_const_type` | private | The feature reader that we delegate all property reading to. |
| `d_from_property_name` | field | `GPlatesModel::PropertyName` | private | — |
| `d_to_property_name` | field | `GPlatesModel::PropertyName` | private | — |
| `RenamePropertyFeatureReaderImpl( const GPlatesModel::PropertyName &from_property_name, const GPlatesModel::PropertyName &to_property_name, const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | constructor | `None` | private | — |

### `GPlatesFileIO::GpmlUpgradeReaderUtils::RemovePropertyFeatureReaderImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<RemovePropertyFeatureReaderImpl>` | public | A convenience typedef for a shared pointer to a non-const RemovePropertyFeatureReaderImpl. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const RemovePropertyFeatureReaderImpl>` | public | A convenience typedef for a shared pointer to a const RemovePropertyFeatureReaderImpl. |
| `create( const GPlatesModel::PropertyName &property_name, const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | method | `non_null_ptr_type` | public | Creates a RemovePropertyFeatureReaderImpl. |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | — |
| `d_feature_reader` | field | `GpmlFeatureReaderImpl::non_null_ptr_to_const_type` | private | The feature reader that we delegate all property reading to. |
| `d_property_name` | field | `GPlatesModel::PropertyName` | private | — |
| `RemovePropertyFeatureReaderImpl( const GPlatesModel::PropertyName &property_name, const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | constructor | `None` | private | — |

### `GPlatesFileIO::GpmlUpgradeReaderUtils::ChangeFeatureTypeFeatureReaderImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ChangeFeatureTypeFeatureReaderImpl>` | public | A convenience typedef for a shared pointer to a non-const ChangeFeatureTypeFeatureReaderImpl. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ChangeFeatureTypeFeatureReaderImpl>` | public | A convenience typedef for a shared pointer to a const ChangeFeatureTypeFeatureReaderImpl. |
| `create( const GPlatesModel::FeatureType &new_feature_type, const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | method | `non_null_ptr_type` | public | Creates a ChangeFeatureTypeFeatureReaderImpl. |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | — |
| `d_feature_reader` | field | `GpmlFeatureReaderImpl::non_null_ptr_to_const_type` | private | The feature reader that we delegate all property reading to. |
| `d_new_feature_type` | field | `GPlatesModel::FeatureType` | private | — |
| `ChangeFeatureTypeFeatureReaderImpl( const GPlatesModel::FeatureType &new_feature_type, const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | constructor | `None` | private | — |

### `GPlatesFileIO::GpmlUpgradeReaderUtils::TopologicalNetworkFeatureReaderUpgrade_1_6_319`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopologicalNetworkFeatureReaderUpgrade_1_6_319>` | public | A convenience typedef for a shared pointer to a non-const TopologicalNetworkFeatureReaderUpgrade\_1\_6\_319. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopologicalNetworkFeatureReaderUpgrade_1_6_319>` | public | A convenience typedef for a shared pointer to a const TopologicalNetworkFeatureReaderUpgrade\_1\_6\_319. |
| `create( const GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type &gpgim_feature_class, const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &parent_feature_reader, const GpmlPropertyStructuralTypeReader::non_null_ptr_to_const_type &property_structural_type_reader, const GPlatesModel::GpgimVersion &gpml_vers ...` | method | `boost::optional<non_null_ptr_type>` | public | — |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | — |
| `d_parent_feature_reader` | field | `GpmlFeatureReaderImpl::non_null_ptr_to_const_type` | private | The feature reader associated with the parent GPGIM feature class. |
| `d_boundary_property_reader` | field | `GpmlPropertyReader::non_null_ptr_to_const_type` | private | Reads the 'gpml:boundary' property. |
| `d_interior_property_reader` | field | `GpmlPropertyReader::non_null_ptr_to_const_type` | private | Reads the 'gpml:interior' property. |
| `d_network_property_name` | field | `GPlatesModel::PropertyName` | private | The network property name or whatever it currently is in the GPGIM. |
| `TopologicalNetworkFeatureReaderUpgrade_1_6_319( const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &parent_feature_reader, const GpmlPropertyReader::non_null_ptr_to_const_type &boundary_property_reader, const GpmlPropertyReader::non_null_ptr_to_const_type &interior_property_reader, const GPlatesModel::PropertyName ...` | constructor | `None` | private | — |

### `GPlatesFileIO::GpmlUpgradeReaderUtils::CrustalThinningFactorUpgrade_1_6_338`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<CrustalThinningFactorUpgrade_1_6_338>` | public | A convenience typedef for a shared pointer to a non-const ChangeFeatureTypeFeatureReaderImpl. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const CrustalThinningFactorUpgrade_1_6_338>` | public | A convenience typedef for a shared pointer to a const ChangeFeatureTypeFeatureReaderImpl. |
| `create( const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | method | `non_null_ptr_type` | public | Creates a ChangeFeatureTypeFeatureReaderImpl. |
| `read_feature( const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, xml_node_seq_type &unprocessed_feature_property_xml_nodes, GpmlReaderUtils::ReaderParams &reader_params)` | method | `GPlatesModel::FeatureHandle::non_null_ptr_type` | public | — |
| `d_feature_reader` | field | `GpmlFeatureReaderImpl::non_null_ptr_to_const_type` | private | The feature reader that we delegate all property reading to. |
| `CrustalThinningFactorUpgrade_1_6_338( const GpmlFeatureReaderImpl::non_null_ptr_to_const_type &feature_reader)` | constructor | `None` | private | — |
| `convert_crustal_thinning_factor_properties( GPlatesModel::FeatureHandle::non_null_ptr_type feature)` | method | `bool` | private | — |
| `convert_crustal_thinning_factors( const GPlatesPropertyValues::GmlDataBlock::non_null_ptr_to_const_type &range)` | method | `boost::optional<GPlatesPropertyValues::GmlDataBlock::non_null_ptr_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_topological_section_list( const GPlatesModel::XmlElementNode::non_null_ptr_type &parent, const GPlatesPropertyValues::StructuralType &structural_type, const GPlatesModel::GpgimVersion &gpml_version, ReadErrorAccumulation &read_errors)` | function | `GPlatesPropertyValues::OldVersionPropertyValue::non_null_ptr_type` | Reads a list of topological sections from an old version 'gpml:TopologicalPolygon' or 'gpml:TopologicalInterior'. |
| `append_reader_errors( GPlatesModel::ModelUtils::TopLevelPropertyError::Type error_code, const GPlatesModel::XmlElementNode::non_null_ptr_type &feature_xml_element, GpmlReaderUtils::ReaderParams &reader_params)` | function | `void` | — |
| `GPLATES_FILE_IO_GPMLUPGRADEREADERUTILS_H` | macro | `None` | — |
| `rename_gpgim_feature_class_properties( const GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type &feature_class, const std::vector<PropertyRename> &property_renames)` | function | `GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type` | Copy the specified GPGIM feature class, but change the specified property names. |
| `create_property_rename_feature_reader_impl( const GpmlFeatureReaderImpl::non_null_ptr_type &feature_reader_impl, const std::vector<PropertyRename> &property_renames)` | function | `GpmlFeatureReaderImpl::non_null_ptr_type` | Creates a feature reader impl that reads a feature using feature\_read\_impl and then renames feature properties with matching property names to the \*new\* property names. |
| `add_gpgim_feature_class_properties( const GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type &feature_class, const std::vector<GPlatesModel::GpgimProperty::non_null_ptr_to_const_type> &properties)` | function | `GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type` | Copy the specified GPGIM feature class, but add the specified GPGIM properties. |
| `remove_gpgim_feature_class_properties( const GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type &feature_class, const std::vector<GPlatesModel::PropertyName> &property_names)` | function | `GPlatesModel::GpgimFeatureClass::non_null_ptr_to_const_type` | Copy the specified GPGIM feature class, but remove GPGIM properties matching the specified property names. |
| `create_property_remove_feature_reader_impl( const GpmlFeatureReaderImpl::non_null_ptr_type &feature_reader_impl, const std::vector<GPlatesModel::PropertyName> &property_names)` | function | `GpmlFeatureReaderImpl::non_null_ptr_type` | Creates a feature reader impl that reads a feature using feature\_read\_impl and then removes feature properties matching the specified property names. |

## Notes

[[[PROSE notes unit=file-io/GpmlUpgradeReaderUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlFeatureReaderFactory](GpmlFeatureReaderFactory.md) | file-io | 27 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlUpgradeReaderUtils.h
python scripts/gpq.py def GPlatesFileIO::GpmlUpgradeReaderUtils::RenamePropertyFeatureReaderImpl --body
python scripts/gpq.py uses RenamePropertyFeatureReaderImpl --kind class
python scripts/gpq.py hier RenamePropertyFeatureReaderImpl
```
