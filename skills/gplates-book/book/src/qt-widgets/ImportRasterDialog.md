# ImportRasterDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 225 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ImportRasterDialog.h` | C++ | 230 |
| `src/qt-widgets/ImportRasterDialog.cc` | C++ | 834 |

## Overview

[[[PROSE overview unit=qt-widgets/ImportRasterDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::TimeDependentRasterSequence`](#gplatesqtwidgetstimedependentrastersequence) | class | — | — | 0 | — |
| [`GPlatesQtWidgets::ImportRasterDialog`](#gplatesqtwidgetsimportrasterdialog) | class | `QWizard` | — | 0 | — |

## Members

### `GPlatesQtWidgets::TimeDependentRasterSequence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FileInfo` | struct | `None` | public | — |
| `element_type` | typedef | `FileInfo` | public | — |
| `sequence_type` | typedef | `std::vector<element_type>` | public | — |
| `empty()` | method | `bool` | public | — |
| `push_back( boost::optional<double> time, const QString &absolute_file_path, const QString &file_name, const std::vector<GPlatesPropertyValues::RasterType::Type> &band_types_, unsigned int width, unsigned int height)` | method | `void` | public | — |
| `add_all( const TimeDependentRasterSequence &other)` | method | `void` | public | — |
| `clear()` | method | `void` | public | — |
| `erase( unsigned int begin_index, unsigned int end_index)` | method | `void` | public | — |
| `set_time( unsigned int index, const boost::optional<double> &time)` | method | `void` | public | — |
| `sort_by_time()` | method | `void` | public | — |
| `sort_by_file_name()` | method | `void` | public | — |
| `d_sequence` | field | `sequence_type` | private | — |

### `GPlatesQtWidgets::ImportRasterDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ImportRasterDialog( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, GPlatesGui::UnsavedChangesTracker *unsaved_changes_tracker, GPlatesGui::FileIOFeedback *file_io_feedback, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `display( bool time_dependent_raster, GPlatesFileIO::ReadErrorAccumulation *read_errors = NULL)` | method | `void` | public | Call this to open the import raster wizard, instead of show(). |
| `PageId` | enum | `None` | private | Wizard page ids. |
| `nextId()` | method | `int` | private | Override the next page id so we can skip georeferencing page if raster has inbuilt georeferencing. |
| `get_raster_georeferencing()` | method | `boost::optional<GPlatesPropertyValues::Georeferencing::non_null_ptr_to_const_type>` | private | Returns (first) raster's inbuilt georeferencing (if any). |
| `set_number_of_bands( unsigned int number_of_bands)` | method | `void` | private | — |
| `create_range_set( bool time_dependent_raster)` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | private | Note: this sorts d\_raster\_sequence, in place. |
| `create_band_names()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | private | — |
| `create_domain_set()` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | private | — |
| `create_gpml_file_path( bool time_dependent_raster)` | method | `QString` | private | — |
| `GPML_EXT` | field | `QString` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_unsaved_changes_tracker` | field | `GPlatesGui::UnsavedChangesTracker` | private | — |
| `d_file_io_feedback` | field | `GPlatesGui::FileIOFeedback` | private | — |
| `d_open_file_dialog` | field | `OpenFileDialog` | private | — |
| `d_raster_width` | field | `unsigned int` | private | For communication between pages. |
| `d_raster_height` | field | `unsigned int` | private | — |
| `d_raster_sequence` | field | `TimeDependentRasterSequence` | private | — |
| `d_band_names` | field | `std::vector<QString>` | private | — |
| `d_georeferencing` | field | `GPlatesPropertyValues::Georeferencing::non_null_ptr_type` | private | — |
| `d_save_after_finish` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPML_EXT` | variable | `QString` | — |
| `build_mime_type_map()` | function | `std::map<QString, XsString::non_null_ptr_to_const_type>` | — |
| `get_mime_type( const QString &file_name)` | function | `boost::optional<XsString::non_null_ptr_to_const_type>` | — |
| `create_gml_file( const GPlatesQtWidgets::TimeDependentRasterSequence::FileInfo &file_info)` | function | `GmlFile::non_null_ptr_type` | — |
| `GPLATES_QTWIDGETS_IMPORTRASTERDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ImportRasterDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/TimeDependentRasterPage](TimeDependentRasterPage.md) | qt-widgets | 45 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 2 |
| [qt-widgets/RasterGeoreferencingPage](RasterGeoreferencingPage.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ImportRasterDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ImportRasterDialog --body
python scripts/gpq.py uses ImportRasterDialog --kind class
python scripts/gpq.py hier ImportRasterDialog
```
