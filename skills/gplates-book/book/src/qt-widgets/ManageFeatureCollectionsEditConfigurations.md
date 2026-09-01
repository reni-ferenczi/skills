# ManageFeatureCollectionsEditConfigurations

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 1220 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ManageFeatureCollectionsEditConfigurations.h` | C++ | 137 |
| `src/qt-widgets/ManageFeatureCollectionsEditConfigurations.cc` | C++ | 188 |

## Overview

Configuration handlers for saving feature collections in different file formats, used by the Manage Feature Collection dialog. The `EditConfiguration` base class defines the interface for format-specific configuration dialogs. `GMTEditConfiguration` handles output options for the GMT ".xy" format, while `ShapefileEditConfiguration` manages attribute mapping and wrap-to-dateline options for multiple OGR-based formats including Shapefile, GeoJSON, and GeoPackage. The `register_default_edit_configurations` function wires these handlers into a dialog so that users can edit format-specific options when saving.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ManageFeatureCollections::EditConfiguration`](#gplatesqtwidgetsmanagefeaturecollectionseditconfiguration) | class | — | — | 2 | Base class for editing a file's configuration in the Manage Feature Collection dialog. |
| [`GPlatesQtWidgets::ManageFeatureCollections::GMTEditConfiguration`](#gplatesqtwidgetsmanagefeaturecollectionsgmteditconfiguration) | class | [`EditConfiguration`](ManageFeatureCollectionsEditConfigurations.md) | — | 0 | Handles output options when writing to the write-only GMT ".xy" file format. |
| [`GPlatesQtWidgets::ManageFeatureCollections::ShapefileEditConfiguration`](#gplatesqtwidgetsmanagefeaturecollectionsshapefileeditconfiguration) | class | [`EditConfiguration`](ManageFeatureCollectionsEditConfigurations.md) | — | 0 | Handles input/output options for the Shapefile format. |

## Members

### `GPlatesQtWidgets::ManageFeatureCollections::EditConfiguration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const EditConfiguration>` | public | Typedef for a shared pointer to const EditConfiguration. |
| `shared_ptr_type` | typedef | `boost::shared_ptr<EditConfiguration>` | public | Typedef for a shared pointer to EditConfiguration. |
| `~EditConfiguration()` | destructor | `None` | public | — |
| `edit_configuration( GPlatesFileIO::File::Reference &file_reference, const GPlatesFileIO::FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type & current_configuration, QWidget *parent_widget)` | method | `GPlatesFileIO::FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type` | public | Allow the user to edit current\_configuration. |

### `GPlatesQtWidgets::ManageFeatureCollections::GMTEditConfiguration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const GMTEditConfiguration>` | public | — |
| `shared_ptr_type` | typedef | `boost::shared_ptr<GMTEditConfiguration>` | public | — |
| `edit_configuration( GPlatesFileIO::File::Reference &file_reference, const GPlatesFileIO::FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type & current_configuration, QWidget *parent_widget)` | method | `GPlatesFileIO::FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type` | public | — |

### `GPlatesQtWidgets::ManageFeatureCollections::ShapefileEditConfiguration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const ShapefileEditConfiguration>` | public | — |
| `shared_ptr_type` | typedef | `boost::shared_ptr<ShapefileEditConfiguration>` | public | — |
| `ShapefileEditConfiguration( GPlatesModel::ModelInterface &model)` | constructor | `None` | public | — |
| `edit_configuration( GPlatesFileIO::File::Reference &file_reference, const GPlatesFileIO::FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type & current_configuration, QWidget *parent_widget)` | method | `GPlatesFileIO::FeatureCollectionFileFormat::Configuration::shared_ptr_to_const_type` | public | — |
| `d_model` | field | `GPlatesModel::ModelInterface` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_MANAGEFEATURECOLLECTIONSEDITCONFIGURATIONS_H` | macro | `None` | — |
| `register_default_edit_configurations( ManageFeatureCollectionsDialog &manage_feature_collections_dialog, GPlatesModel::ModelInterface &model)` | function | `void` | Registers the default edit configurations for those file formats that have configurations. |

## Notes

The model-to-attribute map is stored in the feature collection itself, not in the file configuration. `ShapefileEditConfiguration` remaps file attributes through `GPlatesFileIO::OgrReader::remap_shapefile_attributes`, which requires the updated file configuration to already be stored on the file reference. If the file is deleted before the configuration dialog opens, a dialog reports the error and the original configuration is returned unchanged.

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/Application](../presentation/Application.md) | presentation | 3 |
| [qt-widgets/ManageFeatureCollectionsDialog](ManageFeatureCollectionsDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ManageFeatureCollectionsEditConfigurations.h
python scripts/gpq.py def GPlatesQtWidgets::ManageFeatureCollections::EditConfiguration --body
python scripts/gpq.py uses EditConfiguration --kind class
python scripts/gpq.py hier EditConfiguration
```
