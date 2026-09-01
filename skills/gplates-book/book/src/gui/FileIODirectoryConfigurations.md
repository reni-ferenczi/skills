# FileIODirectoryConfigurations

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 795 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/FileIODirectoryConfigurations.h` | C++ | 100 |
| `src/gui/FileIODirectoryConfigurations.cc` | C++ | 142 |

## Overview

[[[PROSE overview unit=gui/FileIODirectoryConfigurations tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::DirectoryConfiguration`](#gplatesguidirectoryconfiguration) | class | — | — | 0 | — |
| [`GPlatesGui::FileIODirectoryConfigurations`](#gplatesguifileiodirectoryconfigurations) | class | `boost::noncopyable` | — | 0 | — |

## Members

### `GPlatesGui::DirectoryConfiguration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DirectoryConfiguration( GPlatesAppLogic::UserPreferences &prefs, const QString &default_key_string, const QString &last_used_key_string, const QString &behaviour_key_string )` | constructor | `None` | public | — |
| `initialise_from_preferences()` | method | `void` | public | — |
| `directory` | field | `QString` | public | — |
| `update_last_used_directory( const QString &directory)` | method | `void` | public | — |
| `last_used_directory` | field | `QString` | public | — |
| `d_prefs` | field | `GPlatesAppLogic::UserPreferences` | private | — |
| `d_default_key_string` | field | `QString` | private | — |
| `d_last_used_key_string` | field | `QString` | private | — |
| `d_behaviour_key_string` | field | `QString` | private | — |
| `d_default_directory` | field | `QString` | private | — |
| `d_last_used_directory` | field | `QString` | private | — |
| `d_last_used_directory_from_prefs` | field | `QString` | private | — |
| `d_behaviour` | field | `GPlatesQtWidgets::PreferencesPaneFiles::FileBehaviour` | private | — |
| `d_first_use` | field | `bool` | private | — |

### `GPlatesGui::FileIODirectoryConfigurations`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FileIODirectoryConfigurations( GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | — |
| `feature_collection_configuration` | field | `DirectoryConfiguration` | public | — |
| `project_configuration` | field | `DirectoryConfiguration` | public | — |
| `initialise_from_user_preferences()` | method | `void` | private | — |
| `d_feature_collection_configuration` | field | `DirectoryConfiguration` | private | — |
| `d_project_configuration` | field | `DirectoryConfiguration` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_FILE_IO_DIRECTORY_CONFIGURATIONS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/FileIODirectoryConfigurations tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/OpenFileDialog](../qt-widgets/OpenFileDialog.md) | qt-widgets | 13 |
| [gui/SessionMenu](SessionMenu.md) | gui | 12 |
| [qt-widgets/SaveFileDialog](../qt-widgets/SaveFileDialog.md) | qt-widgets | 6 |
| [gui/FileIOFeedback](FileIOFeedback.md) | gui | 5 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 4 |
| [qt-widgets/ManageFeatureCollectionsDialog](../qt-widgets/ManageFeatureCollectionsDialog.md) | qt-widgets | 3 |
| [qt-widgets/AgeModelManagerDialog](../qt-widgets/AgeModelManagerDialog.md) | qt-widgets | 2 |
| [qt-widgets/ExportCoordinatesDialog](../qt-widgets/ExportCoordinatesDialog.md) | qt-widgets | 2 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 2 |
| [qt-widgets/SaveFileDialogImpl](../qt-widgets/SaveFileDialogImpl.md) | qt-widgets | 2 |
| [qt-widgets/ScalarField3DDepthLayersPage](../qt-widgets/ScalarField3DDepthLayersPage.md) | qt-widgets | 2 |
| [qt-widgets/TimeDependentRasterPage](../qt-widgets/TimeDependentRasterPage.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/FileIODirectoryConfigurations.h
python scripts/gpq.py def GPlatesGui::DirectoryConfiguration --body
python scripts/gpq.py uses DirectoryConfiguration --kind class
python scripts/gpq.py hier DirectoryConfiguration
```
