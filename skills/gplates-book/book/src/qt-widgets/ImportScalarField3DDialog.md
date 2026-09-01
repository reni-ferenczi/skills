# ImportScalarField3DDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 307 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ImportScalarField3DDialog.h` | C++ | 282 |
| `src/qt-widgets/ImportScalarField3DDialog.cc` | C++ | 712 |

## Overview

[[[PROSE overview unit=qt-widgets/ImportScalarField3DDialog tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ScalarField3DDepthLayersSequence`](#gplatesqtwidgetsscalarfield3ddepthlayerssequence) | class | — | — | 0 | — |
| [`GPlatesQtWidgets::ImportScalarField3DDialog`](#gplatesqtwidgetsimportscalarfield3ddialog) | class | `QWizard` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ScalarField3DDepthLayersSequence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DEFAULT_RADIUS_OF_EARTH` | field | `double` | public | Radius of Earth in Kms. |
| `FileInfo` | struct | `None` | public | — |
| `element_type` | typedef | `FileInfo` | public | — |
| `sequence_type` | typedef | `std::vector<element_type>` | public | — |
| `empty()` | method | `bool` | public | — |
| `push_back( boost::optional<double> depth, const QString &absolute_file_path, const QString &file_name, unsigned int width, unsigned int height, bool remove_cache_files)` | method | `void` | public | — |
| `add_all( const ScalarField3DDepthLayersSequence &other)` | method | `void` | public | — |
| `clear()` | method | `void` | public | — |
| `clear_cache_files()` | method | `void` | public | Remove cache files of the depth layer rasters (if they didn't already exist prior to import). |
| `erase( unsigned int begin_index, unsigned int end_index)` | method | `void` | public | — |
| `set_depth( unsigned int index, const boost::optional<double> &depth)` | method | `void` | public | — |
| `sort_by_depth()` | method | `void` | public | — |
| `sort_by_file_name()` | method | `void` | public | — |
| `d_sequence` | field | `sequence_type` | private | — |

### `GPlatesQtWidgets::ImportScalarField3DDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ImportScalarField3DDialog( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow &viewport_window, GPlatesGui::UnsavedChangesTracker *unsaved_changes_tracker, GPlatesGui::FileIOFeedback *file_io_feedback, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `display( GPlatesFileIO::ReadErrorAccumulation *read_errors = NULL)` | method | `void` | public | Call this to open the import scalar field wizard, instead of show(). |
| `PageId` | enum | `None` | private | Wizard page ids. |
| `nextId()` | method | `int` | private | Override the next page id so we can skip georeferencing page if raster has inbuilt georeferencing. |
| `create_gl_renderer()` | method | `GPlatesGlobal::PointerTraits<GPlatesOpenGL::GLRenderer>::non_null_ptr_type` | private | — |
| `is_scalar_field_import_supported()` | method | `bool` | private | — |
| `import_georeferencing_and_spatial_reference_system()` | method | `bool` | private | Import georeferencing and spatial reference system (if any) from first depth layer raster. |
| `import_scalar_field_3d( GPlatesFileIO::ReadErrorAccumulation *read_errors)` | method | `void` | private | — |
| `generate_scalar_field( const QString &gpsf_file_path, GPlatesFileIO::ReadErrorAccumulation *read_errors)` | method | `bool` | private | — |
| `create_scalar_field_3d_file_property_value( const QString &gpsf_file_path)` | method | `GPlatesModel::PropertyValue::non_null_ptr_type` | private | — |
| `create_gpml_file_path()` | method | `QString` | private | — |
| `create_gpsf_file_path()` | method | `QString` | private | — |
| `create_file_basename_with_path()` | method | `QString` | private | — |
| `GPML_EXT` | field | `QString` | private | — |
| `GPSF_EXT` | field | `QString` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_unsaved_changes_tracker` | field | `GPlatesGui::UnsavedChangesTracker` | private | — |
| `d_file_io_feedback` | field | `GPlatesGui::FileIOFeedback` | private | — |
| `d_open_file_dialog` | field | `OpenFileDialog` | private | — |
| `d_raster_width` | field | `unsigned int` | private | For communication between pages. |
| `d_raster_height` | field | `unsigned int` | private | — |
| `d_depth_layers_sequence` | field | `ScalarField3DDepthLayersSequence` | private | — |
| `d_georeferencing` | field | `GPlatesPropertyValues::Georeferencing::non_null_ptr_type` | private | — |
| `d_coordinate_transformation` | field | `GPlatesPropertyValues::CoordinateTransformation::non_null_ptr_type` | private | — |
| `d_save_after_finish` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPML_EXT` | variable | `QString` | — |
| `GPSF_EXT` | variable | `QString` | — |
| `DEFAULT_RADIUS_OF_EARTH` | variable | `double` | — |
| `GPLATES_QT_WIDGETS_IMPORTSCALARFIELD3DDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ImportScalarField3DDialog tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ScalarField3DDepthLayersPage](ScalarField3DDepthLayersPage.md) | qt-widgets | 48 |
| [qt-widgets/ScalarField3DGeoreferencingPage](ScalarField3DGeoreferencingPage.md) | qt-widgets | 3 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ImportScalarField3DDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ScalarField3DDepthLayersSequence --body
python scripts/gpq.py uses ScalarField3DDepthLayersSequence --kind class
python scripts/gpq.py hier ScalarField3DDepthLayersSequence
```
