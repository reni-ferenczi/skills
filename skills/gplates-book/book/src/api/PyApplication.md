# PyApplication

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 354 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyApplication.cc` | C++ | 286 |

## Overview

`Application` is a Python wrapper around `GPlatesPresentation::Application` that exposes application state and lifecycle operations to the Python API. It provides methods to execute or evaluate Python code on the GUI thread via `exec_gui_string()`, `eval_gui_string()`, and `exec_gui_file()`, ensuring thread-safe execution of GUI operations. The class also supports registering custom utilities and draw styles from Python, querying loaded feature collections, and accessing the current reconstruction time — all critical operations for scripts running in the Python console.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesApi::Application`](#gplatesapiapplication) | class | — | — | 0 | — |

## Members

### `GPlatesApi::Application`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Application()` | constructor | `None` | public | — |
| `exec_gui_string( const char* str)` | method | `void` | public | — |
| `eval_gui_string( const char* str)` | method | `void` | public | — |
| `exec_gui_file( const char* filepath)` | method | `void` | public | — |
| `register_utility( const object &utility)` | method | `void` | public | — |
| `register_draw_style( object &style)` | method | `void` | public | — |
| `get_loaded_files()` | method | `list` | public | — |
| `get_feature_collection_from_loaded_file( const object &filename)` | method | `object` | public | — |
| `feature_collections()` | method | `list` | public | — |
| `current_time()` | method | `double` | public | — |
| `d_app` | field | `GPlatesPresentation::Application` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `call_utility( const boost::python::object &utility)` | function | `void` | — |
| `export_instance()` | function | `void` | — |

## Notes

All methods that interact with the GUI (exec_gui_string, eval_gui_string, exec_gui_file, register_utility, register_draw_style) use `DISPATCH_GUI_FUN` to ensure the operation runs on the main GUI thread, making them safe to call from Python scripts running in any thread context.

## Used by

*Nothing in the tree references this unit.*

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `Application` | class | — | `Application` |
| `get_main_window` | method | `Application` | `// &Application::get_main_window` |
| `exec_gui_file` | method | `Application` | `&Application::exec_gui_file` |
| `exec_gui_string` | method | `Application` | `&Application::exec_gui_string` |
| `eval_gui_string` | method | `Application` | `&Application::eval_gui_string` |
| `register_utility` | method | `Application` | `&Application::register_utility` |
| `get_loaded_files` | method | `Application` | `&Application::get_loaded_files` |
| `get_feature_collection_from_loaded_file` | method | `Application` | `&Application::get_feature_collection_from_loaded_file` |
| `register_draw_style` | method | `Application` | `&Application::register_draw_style` |
| `feature_collections` | method | `Application` | `&Application::feature_collections` |
| `current_time` | method | `Application` | `&Application::current_time` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PyApplication.cc
python scripts/gpq.py def GPlatesApi::Application --body
python scripts/gpq.py uses Application --kind class
python scripts/gpq.py hier Application
```
