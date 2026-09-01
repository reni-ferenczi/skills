# FeaturePropertyTableModel

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 271 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/FeaturePropertyTableModel.h` | C++ | 221 |
| `src/gui/FeaturePropertyTableModel.cc` | C++ | 507 |

## Overview

[[[PROSE overview unit=gui/FeaturePropertyTableModel tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::FeaturePropertyTableInfo`](#gplatesguifeaturepropertytableinfo) | struct | — | — | 0 | Struct used by FeaturePropertyTableModel to keep track of the properties being presented by the model and their state (i.e. editability). |
| [`GPlatesGui::FeaturePropertyTableModel`](#gplatesguifeaturepropertytablemodel) | class | `QAbstractTableModel` | — | 0 | This class is used by Qt to map a FeatureHandle::weak\_ref to a QTableView. |

## Members

### `GPlatesGui::FeaturePropertyTableInfo`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `property_name` | field | `GPlatesModel::PropertyName` | public | — |
| `property_iterator` | field | `GPlatesModel::FeatureHandle::iterator` | public | — |
| `editable_inline` | field | `bool` | public | — |

### `GPlatesGui::FeaturePropertyTableModel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `property_info_container_type` | typedef | `std::vector<FeaturePropertyTableInfo>` | public | — |
| `property_info_container_iterator` | typedef | `property_info_container_type::iterator` | public | — |
| `property_info_container_const_iterator` | typedef | `property_info_container_type::const_iterator` | public | — |
| `FeaturePropertyTableModel( GPlatesGui::FeatureFocus &feature_focus, QObject *parent_ = NULL)` | constructor | `None` | public | — |
| `rowCount( const QModelIndex &parent_ = QModelIndex())` | method | `int` | public | Qt Model/View function used to access row count, which will depend on the number of top-level properties of the feature. |
| `columnCount( const QModelIndex &parent_ = QModelIndex())` | method | `int` | public | Qt Model/View function used to access column count, which will be a fixed number. |
| `flags( const QModelIndex &idx)` | method | `Qt::ItemFlags` | public | Qt Model/View function used to access editable/selectable/etc status of cells. |
| `headerData( int section, Qt::Orientation orientation, int role = Qt::DisplayRole)` | method | `QVariant` | public | Qt Model/View function used to access header data, both horizontal and vertical. |
| `data( const QModelIndex &idx, int role)` | method | `QVariant` | public | Qt Model/View function used to access individual cells of data. |
| `setData( const QModelIndex &idx, const QVariant &value, int role = Qt::EditRole)` | method | `bool` | public | Qt Model/View function used to set individual cells of data. |
| `get_property_name( int row)` | method | `GPlatesModel::PropertyName` | public | — |
| `get_property_iterator_for_row( int row)` | method | `GPlatesModel::FeatureHandle::iterator` | public | Given a row of the table model, returns the corresponding property iterator. |
| `get_row_for_property_iterator( GPlatesModel::FeatureHandle::iterator property_iterator)` | method | `int` | public | Given a property iterator, returns the corresponding row of the table model. |
| `is_property_editable_inline( int row)` | method | `bool` | public | — |
| `set_feature_reference( GPlatesModel::FeatureHandle::weak_ref feature_ref)` | method | `void` | public | Use this slot to clear the table and set it to a new feature reference. |
| `refresh_data()` | method | `void` | public | Use this slot to simply rebuild the table from the current feature reference. |
| `feature_modified( GPlatesModel::FeatureHandle::weak_ref feature_ref)` | method | `void` | public | Emitted when changes have been made to a feature. |
| `clear_table()` | method | `void` | private | — |
| `get_property_name_as_qvariant( int row)` | method | `QVariant` | private | — |
| `get_property_value_as_qvariant( int row, int role)` | method | `QVariant` | private | — |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |
| `d_feature_ref` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | — |
| `d_property_info_cache` | field | `property_info_container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `top_level_property_to_simple_qvariant( const GPlatesModel::TopLevelProperty &top_level_property, int role)` | function | `QVariant` | Returns a simple representation of the first value of a TopLevelProperty. |
| `top_level_property_to_verbose_qstring( const GPlatesModel::TopLevelProperty &top_level_property, int role)` | function | `QVariant` | Returns a more verbose representation of a TopLevelProperty. |
| `calculate_number_of_properties( const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | function | `int` | This function is necessary to calculate the number of properties that are about to be added to the model, to work around a regression that affects QTableView in Qt version 4.3.0 (Trolltech Bug #169255). |
| `GPLATES_GUI_FEATUREPROPERTYTABLEMODEL_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/FeaturePropertyTableModel tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/EditFeaturePropertiesWidget](../qt-widgets/EditFeaturePropertiesWidget.md) | qt-widgets | 16 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 6 |
| [model/TopLevelPropertyInline](../model/TopLevelPropertyInline.md) | model | 4 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 4 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 4 |
| [app-logic/ScalarCoverageFeatureProperties](../app-logic/ScalarCoverageFeatureProperties.md) | app-logic | 3 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 3 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 3 |
| [api/PyTopologyTools](../api/PyTopologyTools.md) | api | 2 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 2 |
| [data-mining/DataMiningUtils](../data-mining/DataMiningUtils.md) | data-mining | 2 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 2 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 2 |
| [gui/FileIOFeedback](FileIOFeedback.md) | gui | 2 |
| [model/Gpgim](../model/Gpgim.md) | model | 2 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 2 |
| [api/PyFeature](../api/PyFeature.md) | api | 1 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 1 |
| [app-logic/ReconstructedFeatureGeometryFinder](../app-logic/ReconstructedFeatureGeometryFinder.md) | app-logic | 1 |
| [app-logic/ReconstructionGeometryFinder](../app-logic/ReconstructionGeometryFinder.md) | app-logic | 1 |

*... and 30 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/FeaturePropertyTableModel.h
python scripts/gpq.py def GPlatesGui::FeaturePropertyTableModel --body
python scripts/gpq.py uses FeaturePropertyTableModel --kind class
python scripts/gpq.py hier FeaturePropertyTableModel
```
