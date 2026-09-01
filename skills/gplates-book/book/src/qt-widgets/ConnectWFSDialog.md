# ConnectWFSDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 443 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConnectWFSDialog.h` | C++ | 138 |
| `src/qt-widgets/ConnectWFSDialog.cc` | C++ | 537 |
| `src/qt-widgets/ConnectWFSDialogUi.ui` | Qt form | 178 |

## Overview

[[[PROSE overview unit=qt-widgets/ConnectWFSDialog tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::ConnectWFSDialog`](#gplatesqtwidgetsconnectwfsdialog) | class | [`GPlatesDialog`](GPlatesDialog.md)<br>`Ui_ConnectWFSDialog` | — | 0 | — |

## Members

### `GPlatesQtWidgets::ConnectWFSDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConnectWFSDialog( GPlatesAppLogic::ApplicationState& app_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ConnectWFSDialog()` | destructor | `None` | public | — |
| `set_request_geometry( GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_ )` | method | `void` | public | — |
| `startRequest(QUrl url)` | method | `void` | public | — |
| `process_xml()` | method | `void` | public | — |
| `downloadFile()` | method | `void` | private | — |
| `cancelDownload()` | method | `void` | private | — |
| `httpFinished()` | method | `void` | private | These slots are connected to d\_reply within startRequest() |
| `httpReadyRead()` | method | `void` | private | — |
| `updateDataReadProgress(qint64 bytesRead, qint64 totalBytes)` | method | `void` | private | — |
| `handle_apply_valid_time()` | method | `void` | private | These slots are connected to widgets on the dialog |
| `handle_proxy_state_change(int)` | method | `void` | private | — |
| `update_global_proxy()` | method | `void` | private | Update the GPlates-wide proxy details based on what the proxy widgets are set to. |
| `d_app_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_progress_dlg` | field | `QProgressDialog` | private | — |
| `d_url` | field | `QUrl` | private | — |
| `d_qnam` | field | `QNetworkAccessManager` | private | — |
| `d_reply` | field | `QNetworkReply` | private | — |
| `d_xml_file` | field | `QFile` | private | — |
| `d_request_id` | field | `int` | private | — |
| `d_httpRequestAborted` | field | `bool` | private | — |
| `ConnectWFSDialog()` | constructor | `None` | private | — |
| `ConnectWFSDialog(const ConnectWFSDialog&)` | constructor | `None` | private | — |
| `d_request_geom_string` | field | `QString` | private | — |
| `d_request_time_string` | field | `QString` | private | — |
| `d_request_type_string` | field | `QString` | private | — |
| `d_xml_data` | field | `QByteArray` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QTWIDGETS_CONNECTWFSDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/ConnectWFSDialog tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GpgimVersionWarningDialog](GpgimVersionWarningDialog.md) | qt-widgets | 15 |
| [qt-widgets/EditTotalReconstructionSequenceDialog](EditTotalReconstructionSequenceDialog.md) | qt-widgets | 12 |
| [qt-widgets/PythonArgumentWidget](PythonArgumentWidget.md) | qt-widgets | 12 |
| [qt-widgets/ReconstructionViewWidget](ReconstructionViewWidget.md) | qt-widgets | 12 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 10 |
| [file-io/RasterFileCache](../file-io/RasterFileCache.md) | file-io | 10 |
| [file-io/RgbaRasterReader](../file-io/RgbaRasterReader.md) | file-io | 10 |
| [qt-widgets/MissingSessionFilesDialog](MissingSessionFilesDialog.md) | qt-widgets | 10 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 10 |
| [qt-widgets/FriendlyLineEdit](FriendlyLineEdit.md) | qt-widgets | 9 |
| [qt-widgets/MeasureDistanceWidget](MeasureDistanceWidget.md) | qt-widgets | 8 |
| [qt-widgets/UnsavedChangesWarningDialog](UnsavedChangesWarningDialog.md) | qt-widgets | 8 |
| [qt-widgets/VisualLayerWidget](VisualLayerWidget.md) | qt-widgets | 8 |
| [qt-widgets/OpenProjectRelativeOrAbsoluteDialog](OpenProjectRelativeOrAbsoluteDialog.md) | qt-widgets | 7 |
| [file-io/HellingerReader](../file-io/HellingerReader.md) | file-io | 6 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 6 |
| [qt-widgets/ApplyReconstructionPoleAdjustmentDialog](ApplyReconstructionPoleAdjustmentDialog.md) | qt-widgets | 6 |
| [qt-widgets/ChangeFeatureTypeDialog](ChangeFeatureTypeDialog.md) | qt-widgets | 6 |
| [file-io/GeoscimlProfile](../file-io/GeoscimlProfile.md) | file-io | 5 |
| [qt-widgets/AbstractEditWidget](AbstractEditWidget.md) | qt-widgets | 5 |

*... and 97 more units.*

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `ConnectWFSDialog` | `QDialog` | Connect to WFS | 14 |

**Qt signal/slot connections** (8 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `buttonBox` | `accepted()` | `this` | `downloadFile()` |
| `buttonBox` | `rejected()` | `this` | `close()` |
| `d_progress_dlg` | `canceled()` | `this` | `cancelDownload()` |
| `checkBox_proxy` | `stateChanged(int)` | `this` | `handle_proxy_state_change(int)` |
| `pushButton_apply` | `clicked()` | `this` | `handle_apply_valid_time()` |
| `d_reply` | `finished()` | `this` | `httpFinished()` |
| `d_reply` | `readyRead()` | `this` | `httpReadyRead()` |
| `d_reply` | `downloadProgress(qint64,qint64)` | `this` | `updateDataReadProgress(qint64,qint64)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/ConnectWFSDialog.h
python scripts/gpq.py def GPlatesQtWidgets::ConnectWFSDialog --body
python scripts/gpq.py uses ConnectWFSDialog --kind class
python scripts/gpq.py hier ConnectWFSDialog
```
