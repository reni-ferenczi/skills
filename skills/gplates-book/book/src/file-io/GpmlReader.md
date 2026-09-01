# GpmlReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 746 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GpmlReader.h` | C++ | 55 |
| `src/file-io/GpmlReader.cc` | C++ | 452 |

## Overview

The main entry point for reading GPML XML files into the GPlates feature model. `GpmlReader::read_file` opens the GPML file (detecting gzip compression), reads the root element to extract the embedded GPGIM version, and creates a `GpmlFeatureReaderFactory` configured for that version. It then parses each feature in the feature collection using the factory's readers. A helper visitor, `MakeFilePathsAbsoluteVisitor`, walks the loaded features to convert relative file paths to absolute, so that referenced data files (meshes, scalar fields) can be located regardless of working directory.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::MakeFilePathsAbsoluteVisitor`](#anonymousmakefilepathsabsolutevisitor) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Turns the relative file paths in the GPML into absolute file paths in the model. |
| [`GPlatesFileIO::GpmlReader`](#gplatesfileiogpmlreader) | class | — | — | 0 | — |

## Members

### `(anonymous)::MakeFilePathsAbsoluteVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MakeFilePathsAbsoluteVisitor( const QString &absolute_path, GPlatesFileIO::ReadErrorAccumulation &read_errors)` | constructor | `None` | public | — |
| `visit_gml_file( GPlatesPropertyValues::GmlFile &gml_file)` | method | `void` | public | — |
| `visit_gpml_scalar_field_3d_file( GPlatesPropertyValues::GpmlScalarField3DFile &gpml_scalar_field_3d_file)` | method | `void` | public | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `d_absolute_path` | field | `QString` | private | — |
| `d_read_errors` | field | `GPlatesFileIO::ReadErrorAccumulation` | private | — |

### `GPlatesFileIO::GpmlReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_file( File::Reference &file, const GpmlPropertyStructuralTypeReader::non_null_ptr_to_const_type &property_structural_type_reader, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes, bool use_gzip = false)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `qualified_names_are_equal( const QXmlStreamReader &reader, const QString &namespaceUri, const QString &name)` | function | `bool` | Returns true if the given namespaceUri and name match reader.namespaceUri() and reader.name(), false otherwise. |
| `read_feature( const Model::XmlElementNode::non_null_ptr_type &feature_xml_element, const IO::GpmlFeatureReaderFactory &feature_reader_factory, const Model::FeatureCollectionHandle::weak_ref &feature_collection, Utils::ReaderParams &params)` | function | `void` | — |
| `read_feature_member( Utils::ReaderParams &params, const IO::GpmlFeatureReaderFactory &feature_reader_factory, const Model::FeatureCollectionHandle::weak_ref &feature_collection, const boost::shared_ptr<Model::XmlElementNode::AliasToNamespaceMap> &alias_map)` | function | `void` | — |
| `read_root_element( Utils::ReaderParams &params, boost::shared_ptr<Model::XmlElementNode::AliasToNamespaceMap> alias_map)` | function | `boost::optional<Model::GpgimVersion>` | — |
| `GPLATES_FILEIO_GPMLREADER_H` | macro | `None` | — |

## Notes

The file path conversion happens on the fully loaded feature model, not during parsing. This allows relative paths (which GPlates always writes) to work regardless of the current working directory. The reader tolerates absolute paths in GPML files without modification.

## Used by

| Unit | Component | References |
|---|---|---|
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 3 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GpmlReader.h
python scripts/gpq.py def (anonymous)::MakeFilePathsAbsoluteVisitor --body
python scripts/gpq.py uses MakeFilePathsAbsoluteVisitor --kind class
python scripts/gpq.py hier MakeFilePathsAbsoluteVisitor
```
