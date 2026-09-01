# DataMiningUtils

[Book TOC](../../TOC.md) · [data-mining](../../components/data-mining.md) · cluster Community 16 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/DataMiningUtils.h` | C++ | 195 |
| `src/data-mining/DataMiningUtils.cc` | C++ | 326 |

## Overview

`DataMiningUtils` is a free-function toolbox the rest of `data-mining` shares rather than a class: attribute extraction (`get_property_value_by_name`, `get_shape_file_value_by_name`, `convert_qvariant_to_Opaque_data`), geometry distance (`shortest_distance`), numeric conversion (`convert_to_double_vector`, `minimum`), and small file-handling helpers (`load_file`, `load_files`, `load_cfg`, `load_one_line_cfg`) used mainly by `unit-test/CoregTest` fixtures. `get_property_value_by_name` walks a `GPlatesModel::FeatureHandle`'s properties looking for one matching `prop_name`, delegates value extraction to a `GetValueFromPropertyVisitor`, and returns its first result as `OpaqueData`; it special-cases the literal name `"gpml feature type"` to return the feature's type name directly rather than a property value. `get_shape_file_value_by_name` does the analogous lookup inside the `shapefileAttributes` property using a `GPlatesFeatureVisitors::ShapefileAttributeFinder`, warning (but not failing) if more than one attribute matches the requested name.

`shortest_distance` has two overloads built on `GPlatesMaths::minimum_distance`: one finds the closest of a set of seed geometries to a single target geometry, the other finds the closest pair between two sets by calling the first overload repeatedly; both treat polygon interiors as solid, so a point inside a polygon reports zero distance. These are the geometric primitives behind region-of-interest based co-registration.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_DATAMININGUTILS_H` | macro | `None` | — |
| `minimum( const std::vector< double >& input)` | function | `boost::optional< double >` | Return the minimum value Return boost::none if the input vector is empty. |
| `convert_to_double_vector( std::vector<OpaqueData>::const_iterator begin, std::vector<OpaqueData>::const_iterator end, std::vector<double>& result)` | function | `void` | Convert a vector of OpaqueData to a vector of double. |
| `shortest_distance( const std::vector<const GPlatesAppLogic::ReconstructedFeatureGeometry*>& seed_geos, const GPlatesAppLogic::ReconstructedFeatureGeometry* geo)` | function | `double` | Calculate the distances between each two geometries return the shortest distance. |
| `shortest_distance( const std::vector<const GPlatesAppLogic::ReconstructedFeatureGeometry*>& first, const std::vector<const GPlatesAppLogic::ReconstructedFeatureGeometry*>& second)` | function | `double` | — |
| `get_property_value_by_name( const GPlatesModel::FeatureHandle* feature_prt, QString prop_name)` | function | `OpaqueData` | Given the feature handle, find a property by the name. |
| `get_property_value_by_name( GPlatesModel::FeatureHandle::const_weak_ref feature_ref, QString prop_name)` | function | `OpaqueData` | — |
| `convert_qvariant_to_Opaque_data( const QVariant& data)` | function | `OpaqueData` | Since the shape file visitor return QVariant, convert QVariant to OpaqueData |
| `get_shape_file_value_by_name( const GPlatesModel::FeatureHandle* feature_ptr, QString attr_name)` | function | `OpaqueData` | Fine the shape file attribute from the given feature handle |
| `get_shape_file_value_by_name( GPlatesModel::FeatureHandle::const_weak_ref feature_ref, QString attr_name)` | function | `OpaqueData` | — |
| `load_file( const QString fn, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry, GPlatesFileIO::ReadErrorAccumulation* read_errors = NULL)` | function | `GPlatesFileIO::File::non_null_ptr_type` | — |
| `load_files( const std::vector<QString>& filenames, std::vector<GPlatesFileIO::File::non_null_ptr_type>& files, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry, GPlatesFileIO::ReadErrorAccumulation* read_errors = NULL)` | function | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | Given a list of file names, load all the files and return a vector of weak reference of feature collection handle |
| `load_files( const std::vector<const char*>& filenames, std::vector<GPlatesFileIO::File::non_null_ptr_type>& files, const GPlatesFileIO::FeatureCollectionFileFormat::Registry &file_format_registry, GPlatesFileIO::ReadErrorAccumulation* read_errors = NULL)` | function | `std::vector<GPlatesModel::FeatureCollectionHandle::weak_ref>` | — |
| `load_cfg( const QString& cfg_filename, const QString& section_name)` | function | `std::vector<QString>` | Return particular section of configuration file. |
| `load_one_line_cfg( const QString& cfg_file, const QString& section_name)` | function | `QString` | Convenient function for loading cfg section having only one line. |

## Notes

`shortest_distance` throws `GPlatesGlobal::LogException` if either input vector of geometries is empty — callers must guarantee non-empty seed/target sets. `load_cfg` parses a simple line-based `.cfg` format (a line starting with `section_name`, followed by non-comment, non-blank lines until the next blank line) using `std::ifstream` rather than Qt's file classes, as the source comment flags as a known FIXME.

## Used by

| Unit | Component | References |
|---|---|---|
| [api/CoReg](../api/CoReg.md) | api | 27 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 26 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 7 |
| [api/PyFeature](../api/PyFeature.md) | api | 6 |
| [data-mining/LookupReducer](LookupReducer.md) | data-mining | 6 |
| [data-mining/RFGToPropertyValueMapper](RFGToPropertyValueMapper.md) | data-mining | 5 |
| [data-mining/deprecated/DistanceDataOperator](deprecated/DistanceDataOperator.md) | data-mining | 5 |
| [data-mining/DataSelector](DataSelector.md) | data-mining | 3 |
| [data-mining/MaxReducer](MaxReducer.md) | data-mining | 3 |
| [data-mining/MeanReducer](MeanReducer.md) | data-mining | 3 |
| [data-mining/MedianReducer](MedianReducer.md) | data-mining | 3 |
| [data-mining/MinReducer](MinReducer.md) | data-mining | 3 |
| [data-mining/RFGToRelationalPropertyMapper](RFGToRelationalPropertyMapper.md) | data-mining | 3 |
| [data-mining/deprecated/DataOperator](deprecated/DataOperator.md) | data-mining | 3 |
| [data-mining/deprecated/MinDistanceDataOperator](deprecated/MinDistanceDataOperator.md) | data-mining | 3 |
| [unit-test/CoregTest](../unit-test/CoregTest.md) | unit-test | 2 |
| [data-mining/deprecated/DataOperatorFactory](deprecated/DataOperatorFactory.md) | data-mining | 1 |
| [data-mining/deprecated/MaxDistanceDataOperator](deprecated/MaxDistanceDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/MeanDistanceDataOperator](deprecated/MeanDistanceDataOperator.md) | data-mining | 1 |
| [data-mining/deprecated/MedianDistanceDataOperator](deprecated/MedianDistanceDataOperator.md) | data-mining | 1 |

*... and 1 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/DataMiningUtils.h
```
