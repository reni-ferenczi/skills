# ChooseFeatureCollectionWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 254 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ChooseFeatureCollectionWidget.h` | C++ | 154 |
| `src/qt-widgets/ChooseFeatureCollectionWidget.cc` | C++ | 351 |
| `src/qt-widgets/ChooseFeatureCollectionWidgetUi.ui` | Qt form | 37 |

## Overview

`ChooseFeatureCollectionWidget` is the reusable "pick a feature collection to
add this to" control embedded in many creation dialogs
(`CreateFeatureDialog`, `CreateVGPDialog`, `CreateTotalReconstructionSequenceDialog`,
and others). It lists every loaded `FeatureCollectionHandle` via
`populate_feature_collections_list()`, optionally filtered to a set of
`GPlatesFileIO::FeatureCollectionFileFormat::classifications_type` (e.g.
reconstruction-only) checked through the module's `ReconstructMethodRegistry`,
and always appends a synthetic "&lt;Create a new feature collection&gt;" row.
Each row is a `FeatureCollectionItem`, a private `QListWidgetItem` subclass
that either wraps a real `FeatureCollectionFileState::file_reference` or (for
the synthetic row) none at all; `get_file_reference()` on the widget resolves
the user's pick, creating a brand-new feature collection on the fly if the
synthetic row was chosen, and throws `NoFeatureCollectionSelectedException`
if nothing is selected.

`initialise()` re-populates the list from the current file state while trying
to preserve the previous selection, comparing by the underlying
`FeatureCollectionHandle::weak_ref` rather than by the file reference itself
— a file reference can be invalidated by unloading, but the feature
collection weak reference degrades safely to invalid instead of crashing.

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

`FeatureCollectionItem::get_file_reference()` asserts if called on the
synthetic "create new" item or before `set_file_reference()` — callers must
check `is_create_new_collection_item()` first, as the header note says.
`get_feature_collection_reference()` exists specifically to avoid that crash
path when only the referenced feature collection (not the file) is needed,
such as when re-matching the previous selection after a repopulate.

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
