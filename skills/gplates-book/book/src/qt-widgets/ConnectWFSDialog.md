# ConnectWFSDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 443 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/ConnectWFSDialog.h` | C++ | 138 |
| `src/qt-widgets/ConnectWFSDialog.cc` | C++ | 537 |
| `src/qt-widgets/ConnectWFSDialogUi.ui` | Qt form | 178 |

## Overview

The "Connect WFS" dialog fetches GeoSciML from a web service and loads the result
as a new feature collection. It is one of only two places in GPlates that speaks
HTTP: it owns a `QNetworkAccessManager` outright, drives it with the classic
`readyRead()`/`downloadProgress()`/`finished()` slot trio against a
`QProgressDialog`, and on completion hands the accumulated bytes to
`GPlatesAppLogic::FeatureCollectionFileIO` — first `count_features_in_xml_data()`
so the user can be told what they are about to load, then `load_xml_data()` if
they agree. That second call runs the body through
`GPlatesFileIO::ArbitraryXmlReader` with a `GPlatesFileIO::GeoscimlProfile` and
adds the resulting `File` to the application's file state, which is what makes the
downloaded features appear as a layer.

The dialog is reachable two ways. `GPlatesGui::Dialogs::pop_up_connect_wfs_dialog()`
opens it empty from the main menu. The more interesting path is
`DigitisationWidget::handle_use_in_wfs()`: the user digitises a polygon on the
globe, presses "Use in WFS Query...", and the widget pops the dialog up and calls
`set_request_geometry()` with the `GPlatesMaths::GeometryOnSphere` from the
`GeometryBuilder`. That converts the polygon's exterior ring into a
`lon lat, lon lat, ...` list and then synthesises an Apply click so the age
spinboxes are folded in too. This is the only reason the dialog depends on
`maths` and `app-logic/GeometryUtils` at all.

Read the request format before assuming this is a standards-compliant WFS client.
What it builds is a bespoke query string —
`?&polygon=<coords>&age_bottom=<Ma>&age_top=<Ma>` appended to whichever base URL is
in the combo box — not an OGC `GetFeature` request, and the URLs shipped as
defaults in `ConnectWFSDialogUi.ui` are CGI test endpoints. Only the response side
is generic, and only to the extent that `GeoscimlProfile` can find
`wfs:FeatureCollection/gml:featureMember` in it. The request text is editable in a
plain text box, so the dialog is really a hand-rolled query builder with a free-text
escape hatch.

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

This class carries a lot of debug scaffolding that was never removed, and several
of its rough edges bite. Treat the list below as things to check before you touch
it.

The proxy is applied one request too late. `startRequest()` issues
`d_qnam.get()` and only then calls `update_global_proxy()`, so a
`QNetworkAccessManager::setProxy()` made there cannot affect the reply already in
flight. Despite the method's name and comment nothing GPlates-wide is updated
either: the proxy lives on this dialog's own `d_qnam`, and the
`GPlatesAppLogic::UserPreferences` keys `net/proxy/enabled` and `net/proxy/url`
are read once in the constructor and never written back.

The response body is buffered twice and the accumulation buffer is not always
reset. `httpReadyRead()` appends to `d_xml_data` *and* writes to `d_xml_file`,
so the comment claiming the file copy saves RAM no longer holds. `d_xml_data` is
cleared only at the very end of `process_xml()`; both early returns — the transport
error path (which still falls through into `process_xml()`) and the
`startsWith("<?xml")` guard — leave the partial body in place, and the HTTP
redirect branch restarts the request without clearing it. In each case the next
download appends to stale bytes.

The on-disk copy is a debugging artefact with a hard-coded name. Whatever the URL
path suggests, `downloadFile()` overwrites `fileName` with `"TEST.xml"` and
silently removes any existing file of that name in the process's current working
directory. Separately, the `filename` that `process_xml()` passes to
`load_xml_data()` (the temp directory plus the dialog's name field) is only a label:
`FeatureCollectionFileIO::load_xml_data()` creates and closes that file but reads
the features out of the `QByteArray`, so the file on disk stays empty.

Lifetime and state. `GPlatesGui::Dialogs` constructs one instance lazily, parented
to the `ViewportWindow`, and keeps it for the session — so `d_request_id`,
`d_request_geom_string` and any editing the user did to the request text persist
across invocations. Within the dialog, `d_reply` and `d_xml_file` are raw pointers
that are only valid between `startRequest()` and `httpFinished()`; neither is
initialised in the constructor, and the abort branch of `httpFinished()` calls
`deleteLater()` without nulling `d_reply`. The `QErrorMessage` objects created for
the validation failures are parented to the dialog and never deleted, so they
accumulate for as long as it lives.

Two smaller constraints. `set_request_geometry()` accepts polygons only — anything
else produces an error message and leaves the request unchanged. And the progress
dialog's range is a fixed 0–50,000,000 bytes chosen from the sizes of a couple of
test queries, so the bar is meaningless for responses outside that scale.

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
