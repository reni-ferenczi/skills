# ExternalSyncController

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 288 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExternalSyncController.h` | C++ | 350 |
| `src/gui/ExternalSyncController.cc` | C++ | 814 |

## Overview

`ExternalSyncController` synchronises GPlates' current time, camera orientation/zoom and loaded files with an external process over a line-based text protocol carried on standard input/output. Depending on `d_gplates_is_master`, GPlates either launches and owns the external program as a `QProcess` (writing to its stdin, reading `readyReadStandardOutput()`) or is itself the child, in which case a dedicated `StdInThread` blocks on `std::cin` and emits `std_in_string_read` for each line so the read never stalls the Qt event loop.

Incoming lines are tokenised and dispatched by `process_external_command` on a fixed vocabulary of commands (`TIME`, `PROJECTIONCENTRE`, `DISTANCE`, `GAINFOCUS`, `ORIENTATION`, `OPENSHAPEFILE`) to the matching `process_*_command` method, which pulls the new state out of `d_viewport_window_ptr`'s `ReconstructionViewWidget`, `AnimationController` and `ViewState`. Outgoing state changes are the mirror image: `connect_message_signals` wires `AnimationController::view_time_changed`, and the camera/orientation/zoom signals from `ReconstructionViewWidget` and `ViewportZoom`, to the `send_external_*_command` slots that format and write the same protocol back out.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::StdInThread`](#gplatesguistdinthread) | class | `QThread` | — | 0 | Thread for monitoring stdIn |
| [`GPlatesGui::ExternalSyncController`](#gplatesguiexternalsynccontroller) | class | `QObject` | — | 0 | — |

## Members

### `GPlatesGui::StdInThread`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `StdInThread()` | constructor | `None` | public | — |
| `run()` | method | `void` | public | — |
| `std_in_string_read( QString str)` | method | `void` | public | — |

### `GPlatesGui::ExternalSyncController`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExternalSyncController( const bool &gplates_is_master, GPlatesQtWidgets::ViewportWindow *viewport_window_ptr, GPlatesPresentation::ViewState *view_state_ptr)` | constructor | `None` | public | — |
| `~ExternalSyncController()` | destructor | `None` | public | — |
| `enable_external_syncing()` | method | `void` | public | Enable everything, that is to say: read and write to std io; respond to view, time and file messages; send view and time message. |
| `disable_external_syncing()` | method | `void` | public | — |
| `enable_time_commands()` | method | `void` | public | Switch on auto-sync of time signals. |
| `enable_view_commands()` | method | `void` | public | — |
| `enable_file_commands()` | method | `void` | public | — |
| `disable_time_commands()` | method | `void` | public | — |
| `disable_view_commands()` | method | `void` | public | — |
| `disable_file_commands()` | method | `void` | public | — |
| `start_external_process( const QString &process)` | method | `void` | public | — |
| `auto_sync_view( bool sync)` | method | `void` | public | Continuously send and receive/process projection-centre and zoom signals from std in/out |
| `auto_sync_time( bool sync)` | method | `void` | public | Continuously send and receive/process time signals from std in/out |
| `start_thread()` | method | `void` | public | — |
| `sync_external_time()` | method | `void` | public | Sync the time of the external app with the gplates time. |
| `sync_external_view()` | method | `void` | public | Sync the view (orienation and zoom) of the external app to that of gplates. |
| `sync_gplates_view()` | method | `void` | public | Sync the view (orienation and zoom) of gplates to that of the external app. |
| `sync_gplates_time()` | method | `void` | public | Sync the time of gplates to that of the external app. |
| `connect_message_signals()` | method | `void` | public | — |
| `send_external_command( QString &command)` | method | `void` | public | — |
| `process_finished()` | method | `void` | public | Emitted when the external process finishes. |
| `handle_command_received( QString str)` | method | `void` | private | — |
| `send_external_time_command( double time)` | method | `void` | private | — |
| `send_external_camera_command( double lat, double lon)` | method | `void` | private | — |
| `send_external_orientation_command( GPlatesMaths::Rotation &rotation)` | method | `void` | private | — |
| `send_external_zoom_command( double zoom)` | method | `void` | private | — |
| `handle_process_finished( int exit_code, QProcess::ExitStatus exit_status)` | method | `void` | private | — |
| `handle_process_started()` | method | `void` | private | — |
| `handle_process_error( QProcess::ProcessError error)` | method | `void` | private | — |
| `read_process_output()` | method | `void` | private | — |
| `process_external_command( const QString &command_string)` | method | `void` | private | This parses the command string and farms it out to the various other "process..." methods as appropriate. |
| `process_time_command( const QStringList &commands)` | method | `void` | private | — |
| `process_viewport_centre_command( const QStringList &commands)` | method | `void` | private | — |
| `process_orientation_command( const QStringList &commands)` | method | `void` | private | — |
| `process_zoom_command( const QStringList &commands)` | method | `void` | private | — |
| `process_gain_focus_command()` | method | `void` | private | — |
| `process_open_file_command( const QStringList &commands)` | method | `void` | private | — |
| `get_time()` | method | `double` | private | — |
| `get_projection_centre()` | method | `boost::optional<GPlatesMaths::LatLonPoint>` | private | — |
| `get_zoom()` | method | `double` | private | — |
| `get_orientation()` | method | `boost::optional<GPlatesMaths::Rotation>` | private | — |
| `set_time( const double &time)` | method | `void` | private | — |
| `set_projection_centre( const GPlatesMaths::LatLonPoint &llp)` | method | `void` | private | — |
| `set_zoom( const double &zoom)` | method | `void` | private | — |
| `set_orientation( const GPlatesMaths::Rotation &rotation)` | method | `void` | private | — |
| `d_std_in_thread_ptr` | field | `StdInThread` | private | Thread for monitoring stdin. |
| `d_process` | field | `QProcess` | private | Process for launching external app. |
| `d_viewport_window_ptr` | field | `GPlatesQtWidgets::ViewportWindow` | private | Need the viewport window to access: ReconstructionViewWidget (set camera viewpoint) ViewState's ViewportZoom (set zoom) AnimationController (set time) |
| `d_animation_controller_ptr` | field | `GPlatesGui::AnimationController` | private | — |
| `d_reconstruction_view_widget_ptr` | field | `GPlatesQtWidgets::ReconstructionViewWidget` | private | — |
| `d_view_state_ptr` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_should_sync_view` | field | `bool` | private | — |
| `d_should_sync_time` | field | `bool` | private | — |
| `d_most_recent_time` | field | `double` | private | — |
| `d_most_recent_llp` | field | `GPlatesMaths::LatLonPoint` | private | — |
| `d_most_recent_zoom` | field | `double` | private | — |
| `d_most_recent_orientation` | field | `GPlatesMaths::Rotation` | private | — |
| `d_gplates_is_master` | field | `bool` | private | True if gplates launches the external program, and therefore controls synchronisation. |
| `d_should_send_output` | field | `bool` | private | Whether or not we should send signals. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `debug_send_message( const QString &message)` | function | `void` | — |
| `debug_receive_message( const QString &message)` | function | `void` | — |
| `get_filenames_from_argument_list( const QStringList &string_list)` | function | `QStringList` | Ensures string\_list has at least 2 items and removes the first item. |
| `get_centre_from_argument_list( const QStringList &string_list)` | function | `boost::optional<GPlatesMaths::LatLonPoint>` | Extracts llp from string\_list when string\_list is of the form VIEWPORTCENTRE \<lat\> \<lon\> |
| `get_time_from_argument_list( const QStringList &string_list)` | function | `boost::optional<double>` | Extracts time from string\_list when string\_list is of the form TIME \<time\> |
| `get_zoom_from_argument_list( const QStringList &string_list)` | function | `boost::optional<double>` | Extracts zoom from string\_list when string\_list is of the form ZOOM \<zoom\> |
| `get_orientation_from_argument_list( const QStringList &string_list)` | function | `boost::optional<GPlatesMaths::Rotation>` | Extracts a rotation from string\_list when string\_list is of the form ORIENTATION \<lat\> \<lon\> \<angle\> \<lat\> \<lon\> and \<angle\> represent a rotation around \<lat\>\<lon\> by \<angle\> |
| `GPLATES_GUI_EXTERNALSYNCCONTROLLER_H` | macro | `None` | — |

## Notes

- `d_should_send_output` is set false for the duration of `process_external_command` and restored afterwards, specifically to stop an incoming command's resulting state change from being echoed straight back out and causing a feedback loop between the two applications.
- `d_gplates_is_master` is `const`, fixing at construction time which half of the master/slave protocol this instance plays, since that decides whether communication goes through a `QProcess` this object owns or through the standalone `StdInThread`.
- The `PROJECTIONCENTRE` command path (`process_viewport_centre_command`) is compiled out (`#if 0`) in `process_external_command`, so that command is currently a no-op even though its handler still exists.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ColouringDialog](../qt-widgets/ColouringDialog.md) | qt-widgets | 33 |
| [api/PyViewportWindow](../api/PyViewportWindow.md) | api | 12 |
| [gui/FeatureFocus](FeatureFocus.md) | gui | 11 |
| [gui/CommandServer](CommandServer.md) | gui | 8 |
| [gui/PythonManager](PythonManager.md) | gui | 6 |
| [gui/GenericColourScheme](GenericColourScheme.md) | gui | 3 |
| [presentation/Application](../presentation/Application.md) | presentation | 3 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 2 |
| [entry-points/gplates_main](../entry-points/gplates_main.md) | entry-points | 1 |

## Related

**Qt signal/slot connections** (9 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_std_in_thread_ptr` | `std_in_string_read(QString)` | `this` | `handle_command_received(QString)` |
| `d_animation_controller_ptr` | `view_time_changed(double)` | `this` | `send_external_time_command(double)` |
| `d_reconstruction_view_widget_ptr` | `send_camera_pos_to_stdout(double, double)` | `this` | `send_external_camera_command(double,double)` |
| `d_reconstruction_view_widget_ptr` | `send_orientation_to_stdout(GPlatesMaths::Rotation &)` | `this` | `send_external_orientation_command(GPlatesMaths::Rotation &)` |
| `&d_view_state_ptr->get_viewport_zoom()` | `send_zoom_to_stdout(double)` | `this` | `send_external_zoom_command(double)` |
| `d_process` | `finished(int,QProcess::ExitStatus)` | `this` | `handle_process_finished(int, QProcess::ExitStatus)` |
| `d_process` | `error(QProcess::ProcessError)` | `this` | `handle_process_error(QProcess::ProcessError)` |
| `d_process` | `started()` | `this` | `handle_process_started()` |
| `d_process` | `readyReadStandardOutput()` | `this` | `read_process_output()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExternalSyncController.h
python scripts/gpq.py def GPlatesGui::ExternalSyncController --body
python scripts/gpq.py uses ExternalSyncController --kind class
python scripts/gpq.py hier ExternalSyncController
```
