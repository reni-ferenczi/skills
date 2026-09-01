# PythonConsoleDialog

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 161 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/PythonConsoleDialog.h` | C++ | 563 |
| `src/qt-widgets/PythonConsoleDialog.cc` | C++ | 1319 |
| `src/qt-widgets/PythonConsoleDialogUi.ui` | Qt form | 129 |

## Overview

[[[PROSE overview unit=qt-widgets/PythonConsoleDialog tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::PythonConsoleDialog`](#gplatesqtwidgetspythonconsoledialog) | class | `QDialog`<br>[`GPlatesApi::AbstractConsole`](../api/AbstractConsole.md)<br>`Ui_PythonConsoleDialog` | — | 0 | PythonConsoleDialog is a dialog that allows for the interactive input of statements into the Python intepreter and displays the corresponding output. |
| [`GPlatesQtWidgets::ConsoleInputTextEdit`](#gplatesqtwidgetsconsoleinputtextedit) | class | `QPlainTextEdit` | — | 0 | ConsoleInputTextEdit is a widget for the input of one line of Python. |
| [`GPlatesQtWidgets::ConsoleTextEdit`](#gplatesqtwidgetsconsoletextedit) | class | `QPlainTextEdit` | — | 0 | ConsoleTextEdit is the widget that echoes inputs and displays outputs. |

## Members

### `GPlatesQtWidgets::PythonConsoleDialog`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PythonConsoleDialog( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `append_text( const QString &text, bool error = false)` | method | `void` | public | Appends the given text to the console. |
| `append_text( const boost::python::object &obj, bool error = false)` | method | `void` | public | Appends the stringified version of obj to the console. |
| `read_line()` | method | `QString` | public | Prompts the user for a line of input. |
| `get_recent_scripts_menu()` | method | `QMenu` | public | Returns a menu that is populated with recent scripts that can be run again. |
| `get_last_non_blank_line()` | method | `QString` | public | Returns the last line in the console that is not blank. |
| `show_cancel_widget()` | method | `QWidget` | public | — |
| `hide_cancel_widget()` | method | `QWidget` | public | — |
| `run_script()` | method | `void` | public | Prompts the user to select a Python script, and runs that Python script. |
| `clear()` | method | `void` | public | Clears the output textedit. |
| `text_changed()` | method | `void` | public | Emitted when the text has been added to the console via stdout or stderr. |
| `showEvent( QShowEvent *ev)` | method | `void` | protected | — |
| `keyPressEvent( QKeyEvent *ev)` | method | `void` | protected | — |
| `closeEvent( QCloseEvent *ev)` | method | `void` | protected | — |
| `handle_return_pressed( QString line)` | method | `void` | private | — |
| `handle_control_c_pressed( QString line)` | method | `void` | private | — |
| `handle_save_button_clicked()` | method | `void` | private | — |
| `handle_system_exit_exception_raised( int exit_status, QString exit_error_message)` | method | `void` | private | — |
| `handle_recent_script_action_triggered( QAction *action)` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `print_banner()` | method | `void` | private | — |
| `do_append_text( const QString &text, bool error)` | method | `void` | private | — |
| `do_append_object( const boost::python::object &obj, bool error)` | method | `void` | private | — |
| `do_read_line()` | method | `QString` | private | — |
| `run_script( const QString &filename)` | method | `void` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_python_execution_thread` | field | `GPlatesApi::PythonExecutionThread` | private | — |
| `d_python_manager` | field | `GPlatesGui::PythonManager` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_output_textedit` | field | `ConsoleTextEdit` | private | The widget that echoes inputs and displays outputs. |
| `d_open_file_dialog` | field | `OpenFileDialog` | private | To let the user choose a Python script to run. |
| `d_save_file_dialog` | field | `SaveFileDialog` | private | To let the user choose a file name when they click the "Save" button. |
| `d_buffered_lines` | field | `QString` | private | Any text buffered and not yet sent to the Python interpreter. |
| `d_stdout_writer` | field | `GPlatesApi::ConsoleWriter` | private | Redirects writes to Python's sys.stdout to this dialog. |
| `d_readline_dialog` | field | `PythonReadlineDialog` | private | A modal dialog to read a line of input from the user. |
| `d_stdin_reader` | field | `GPlatesApi::ConsoleReader` | private | Redirects attempts to read from sys.stdin to a custom modal dialog. |
| `d_stderr_writer` | field | `GPlatesApi::ConsoleWriter` | private | Redirects writes to Python's sys.stderr to this dialog. |
| `d_disable_close` | field | `bool` | private | If true, close events are rejected. |
| `d_recent_scripts_menu` | field | `QMenu` | private | A menu that allows the user to run recently-run scripts. |
| `d_monitor_widget` | field | `PythonExecutionMonitorWidget` | private | Allows the user to cancel execution with a GUI widget. |
| `d_num_banner_lines` | field | `int` | private | The number of lines in the output textedit that are banner text. |
| `d_system_exit_messagebox` | field | `QMessageBox` | private | Used to display messages telling the user about SystemExit exceptions. |

### `GPlatesQtWidgets::ConsoleInputTextEdit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Prompt` | enum | `None` | public | — |
| `ConsoleInputTextEdit( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_prompt( Prompt prompt)` | method | `void` | public | — |
| `set_text( const QString &text)` | method | `void` | public | — |
| `sizeHint()` | method | `QSize` | public | — |
| `set_vertical_padding( int padding)` | method | `void` | public | — |
| `handle_key_press_event( QKeyEvent *ev)` | method | `void` | public | — |
| `get_prompt` | field | `QString` | public | — |
| `return_pressed( QString line)` | method | `void` | public | — |
| `up_pressed( QString line)` | method | `void` | public | — |
| `down_pressed( QString line)` | method | `void` | public | — |
| `control_c_pressed( QString line)` | method | `void` | public | — |
| `keyPressEvent( QKeyEvent *ev)` | method | `void` | protected | — |
| `mousePressEvent( QMouseEvent *ev)` | method | `void` | protected | — |
| `viewportEvent( QEvent *ev)` | method | `bool` | protected | — |
| `canInsertFromMimeData( const QMimeData *source)` | method | `bool` | protected | — |
| `handle_text_changed()` | method | `void` | private | — |
| `check_cursor_position()` | method | `void` | private | — |
| `handle_internal_scrolling( int value)` | method | `void` | private | — |
| `set_prompt( const QString &prompt)` | method | `void` | private | — |
| `get_text()` | method | `QString` | private | — |
| `d_inside_handle_text_changed` | field | `bool` | private | — |
| `d_prompt` | field | `QString` | private | — |
| `d_vertical_padding` | field | `int` | private | — |

### `GPlatesQtWidgets::ConsoleTextEdit`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConsoleTextEdit( QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `~ConsoleTextEdit()` | destructor | `None` | public | — |
| `append_text( const QString &text, bool error = false)` | method | `void` | public | — |
| `append_text( const QString &prompt, const QString &text)` | method | `void` | public | — |
| `focus_on_input_widget()` | method | `void` | public | — |
| `set_input_prompt( ConsoleInputTextEdit::Prompt prompt)` | method | `void` | public | — |
| `set_input_widget_visible( bool visible)` | method | `void` | public | — |
| `get_last_non_blank_line( int num_banner_lines)` | method | `QString` | public | — |
| `return_pressed( QString line)` | method | `void` | public | — |
| `control_c_pressed( QString line)` | method | `void` | public | — |
| `keyPressEvent( QKeyEvent *ev)` | method | `void` | protected | — |
| `resizeEvent( QResizeEvent *ev)` | method | `void` | protected | — |
| `mousePressEvent( QMouseEvent *ev)` | method | `void` | protected | — |
| `eventFilter( QObject *watched, QEvent *ev)` | method | `bool` | protected | — |
| `handle_text_changed()` | method | `void` | private | — |
| `handle_return_pressed( QString line)` | method | `void` | private | — |
| `handle_up_pressed( QString line)` | method | `void` | private | — |
| `handle_down_pressed( QString line)` | method | `void` | private | — |
| `handle_control_c_pressed( QString line)` | method | `void` | private | — |
| `reposition_input_widget()` | method | `void` | private | — |
| `scroll_to_bottom()` | method | `void` | private | — |
| `d_input_textedit` | field | `ConsoleInputTextEdit` | private | — |
| `d_vertical_padding` | field | `int` | private | — |
| `d_console_history` | field | `boost::scoped_ptr<GPlatesGui::PythonConsoleHistory>` | private | — |
| `d_on_blank_line` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `START_PROMPT_TEXT` | variable | `char` | — |
| `CONTINUATION_PROMPT_TEXT` | variable | `char` | — |
| `build_fixed_width_font()` | function | `QFont` | — |
| `build_prompt_format()` | function | `QTextCharFormat` | — |
| `build_command_format()` | function | `QTextCharFormat` | — |
| `build_normal_text_format()` | function | `QTextCharFormat` | — |
| `build_error_text_format()` | function | `QTextCharFormat` | — |
| `get_tab_stop_width()` | function | `int` | — |
| `SAVE_FILE_DIALOG_TITLE` | variable | `char` | const char \*BUILT\_WITHOUT\_PYTHON = QT\_TR\_NOOP("This version of GPlates was built without Python support"); |
| `get_save_file_dialog_filters()` | function | `GPlatesQtWidgets::SaveFileDialog::filter_list_type` | — |
| `OPEN_FILE_DIALOG_TITLE` | variable | `char` | — |
| `OPEN_FILE_DIALOG_FILTER` | variable | `char` | — |
| `is_all_whitespace( const QString &line)` | function | `bool` | — |
| `GPLATES_QTWIDGETS_PYTHONCONSOLEDIALOG_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/PythonConsoleDialog tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/PythonManager](../gui/PythonManager.md) | gui | 3 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `PythonConsoleDialog` | `QDialog` | Python Console | 7 |

**Qt signal/slot connections** (18 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_output_textedit` | `return_pressed(QString)` | `this` | `handle_return_pressed(QString)` |
| `d_output_textedit` | `control_c_pressed(QString)` | `this` | `handle_control_c_pressed(QString)` |
| `run_script_button` | `clicked()` | `this` | `run_script()` |
| `save_button` | `clicked()` | `this` | `handle_save_button_clicked()` |
| `clear_button` | `clicked()` | `this` | `clear()` |
| `d_recent_scripts_menu` | `triggered(QAction *)` | `this` | `handle_recent_script_action_triggered(QAction *)` |
| `d_python_execution_thread` | `system_exit_exception_raised(int, QString )` | `this` | `handle_system_exit_exception_raised(int, QString )` |
| `&GPlatesApi::PythonUtils::python_manager()` | `system_exit_exception_raised(int, QString )` | `this` | `handle_system_exit_exception_raised(int, QString )` |
| `this` | `textChanged()` | `this` | `handle_text_changed()` |
| `this` | `cursorPositionChanged()` | `this` | `check_cursor_position()` |
| `this` | `selectionChanged()` | `this` | `check_cursor_position()` |
| `verticalScrollBar()` | `valueChanged(int)` | `this` | `handle_internal_scrolling(int)` |
| `this` | `textChanged()` | `this` | `handle_text_changed()` |
| `d_input_textedit` | `return_pressed(QString)` | `this` | `handle_return_pressed(QString)` |
| `d_input_textedit` | `up_pressed(QString)` | `this` | `handle_up_pressed(QString)` |

*... and 3 more connections.*


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/PythonConsoleDialog.h
python scripts/gpq.py def GPlatesQtWidgets::PythonConsoleDialog --body
python scripts/gpq.py uses PythonConsoleDialog --kind class
python scripts/gpq.py hier PythonConsoleDialog
```
