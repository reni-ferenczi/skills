# ChooseFeatureCollectionWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 254 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChooseFeatureCollectionWidget.h` | C++ | 154 |
| `src/qt-widgets/ChooseFeatureCollectionWidget.cc` | C++ | 351 |
| `src/qt-widgets/ChooseFeatureCollectionWidgetUi.ui` | Qt form | 37 |

## Overview

[[[PROSE overview unit=qt-widgets/ChooseFeatureCollectionWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::FeatureCollectionItem`](#anonymousfeaturecollectionitem) | class | `QListWidgetItem` | — | 0 | Subclass of QListWidgetItem so that we can display a list of FeatureCollection in the list widget using the filename as the label, while keeping track of which list item corresponds to which FeatureCollection. |
| [`GPlatesQtWidgets::ChooseFeatureCollectionWidget`](#gplatesqtwidgetschoosefeaturecollectionwidget) | class | `QGroupBox`<br>`Ui_ChooseFeatureCollectionWidget` | — | 0 | — |

## Members

### `(anonymous)::FeatureCollectionItem`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureCollectionItem( GPlatesAppLogic::FeatureCollectionFileState::file_reference file_ref, const QString &label)` | constructor | `None` | public | Standard constructor for creating FeatureCollection entry. |
| `FeatureCollectionItem( const QString &label)` | constructor | `None` | public | Constructor for creating fake "Make a new Feature Collection" entry. |
| `is_create_new_collection_item()` | method | `bool` | public | — |
| `get_file_reference()` | method | `GPlatesAppLogic::FeatureCollectionFileState::file_reference` | public | NOTE: Check with is\_create\_new\_collection\_item first and set a valid file iterator if necessary before calling this method. |
| `set_file_reference( GPlatesAppLogic::FeatureCollectionFileState::file_reference file_ref)` | method | `void` | public | — |
| `get_feature_collection_reference()` | method | `GPlatesModel::FeatureCollectionHandle::weak_ref` | public | Returns the referenced feature collection or an invalid weak reference if either not created with a file or file has since been unloaded. |
| `File` | struct | `None` | private | — |
| `d_file` | field | `boost::optional<File>` | private | — |

### `GPlatesQtWidgets::ChooseFeatureCollectionWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NoFeatureCollectionSelectedException` | struct | `None` | public | — |
| `ChooseFeatureCollectionWidget( const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry, GPlatesAppLogic::FeatureCollectionFileState &file_state, GPlatesAppLogic::FeatureCollectionFileIO &file_io, QWidget *parent_ = NULL, const boost::optional<GPlatesFileIO::FeatureCollectionFileFormat::classificat ...` | constructor | `None` | public | — |
| `initialise()` | method | `void` | public | Initialises the ChooseFeatureCollectionWidget with the currently loaded feature collections. |
| `set_help_text( const QString &text)` | method | `void` | public | Changes the help text in the widget to text. |
| `get_file_reference()` | method | `std::pair<GPlatesAppLogic::FeatureCollectionFileState::file_reference, bool>` | public | Returns an iterator to the file selected by the user, and a boolean value indicating whether the iterator points to a file that was newly created. |
| `select_file_reference( const GPlatesAppLogic::FeatureCollectionFileState::file_reference &file_reference)` | method | `void` | public | Selects the item in the list that corresponds to file\_reference. |
| `select_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection)` | method | `void` | public | Selects the item in the list that corresponds to feature\_collection. |
| `item_activated()` | method | `void` | public | — |
| `handle_listwidget_item_activated( QListWidgetItem *)` | method | `void` | private | — |
| `focusInEvent( QFocusEvent *ev)` | method | `void` | protected | — |
| `d_file_state` | field | `GPlatesAppLogic::FeatureCollectionFileState` | private | — |
| `d_file_io` | field | `GPlatesAppLogic::FeatureCollectionFileIO` | private | — |
| `d_allowed_collection_types` | field | `boost::optional<GPlatesFileIO::FeatureCollectionFileFormat::classifications_type>` | private | The collection types which we wish to display in the widget. |
| `d_reconstruct_method_registry` | field | `GPlatesAppLogic::ReconstructMethodRegistry` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `collection_is_of_allowed_type( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection_ref, const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry, const boost::optional<GPlatesFileIO::FeatureCollectionFileFormat::classifications_type> &allowed_types)` | function | `bool` | — |
| `populate_feature_collections_list( QListWidget &list_widget, GPlatesAppLogic::FeatureCollectionFileState &state, const boost::optional<GPlatesFileIO::FeatureCollectionFileFormat::classifications_type> &allowed_collection_types, const GPlatesAppLogic::ReconstructMethodRegistry &reconstruct_method_registry)` | function | `void` | Fill the list with currently loaded FeatureCollections we can add the feature to. |
| `GPLATES_QTWIDGETS_CHOOSEFEATURECOLLECTIONWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ChooseFeatureCollectionWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/CreateTotalReconstructionSequenceDialog](CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 22 |
| [qt-widgets/CreateSmallCircleFeatureDialog](CreateSmallCircleFeatureDialog.md) | qt-widgets | 8 |
| [qt-widgets/CreateVGPDialog](CreateVGPDialog.md) | qt-widgets | 8 |
| [qt-widgets/ChooseFeatureCollectionDialog](ChooseFeatureCollectionDialog.md) | qt-widgets | 7 |
| [qt-widgets/CreateFeatureDialog](CreateFeatureDialog.md) | qt-widgets | 7 |
| [gui/UnsavedChangesTracker](../gui/UnsavedChangesTracker.md) | gui | 6 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](GenerateDeformingMeshPointsDialog.md) | qt-widgets | 5 |
| [qt-widgets/ShapefileAttributeViewerDialog](ShapefileAttributeViewerDialog.md) | qt-widgets | 4 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 3 |
| [app-logic/ReconstructContext](../app-logic/ReconstructContext.md) | app-logic | 3 |
| [presentation/SessionManagement](../presentation/SessionManagement.md) | presentation | 3 |
| [qt-widgets/ManageFeatureCollectionsDialog](ManageFeatureCollectionsDialog.md) | qt-widgets | 3 |
| [api/PyApplication](../api/PyApplication.md) | api | 2 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 2 |
| [gui/GuiDebug](../gui/GuiDebug.md) | gui | 2 |
| [presentation/DeprecatedSessionRestore](../presentation/DeprecatedSessionRestore.md) | presentation | 2 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 2 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 2 |
| [qt-widgets/FeatureSummaryWidget](FeatureSummaryWidget.md) | qt-widgets | 2 |
| [qt-widgets/TotalReconstructionSequencesDialog](TotalReconstructionSequencesDialog.md) | qt-widgets | 2 |

*... and 12 more units.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ChooseFeatureCollectionWidget` | `QGroupBox` | Feature Collection | 3 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `listwidget_feature_collections` | `itemActivated(QListWidgetItem *)` | `this` | `handle_listwidget_item_activated(QListWidgetItem *)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ChooseFeatureCollectionWidget.h
python scripts/gpq.py def GPlatesQtWidgets::ChooseFeatureCollectionWidget --body
python scripts/gpq.py uses ChooseFeatureCollectionWidget --kind class
python scripts/gpq.py hier ChooseFeatureCollectionWidget
```
