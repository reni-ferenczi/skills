# python

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 0 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/python.h` | C++ | 172 |

## Overview

`python.h` is the mandatory replacement for including `<Python.h>` (and, transitively, `<boost/python.hpp>`) directly anywhere in GPlates. It exists to paper over a string of platform- and version-specific incompatibilities between CPython's headers, Boost.Python and MSVC/Qt: it undefines stray `HAVE_DIRECT_H`/`HAVE_UNISTD_H`/`ssize_t` macros left over on Windows, defines `HAVE_SNPRINTF` for MSVC 2015+ so `pyconfig.h` doesn't redefine `snprintf`, and temporarily undefines `_DEBUG` around the `<Python.h>` include so MSVC debug builds don't try to link the (usually absent) `python27_d.lib`. It then pulls in `<boost/python.hpp>` with `BOOST_BIND_GLOBAL_PLACEHOLDERS` defined to silence a Boost 1.74 deprecation warning that Boost itself has not yet fixed, and optionally `<boost/python/numpy.hpp>` and the raw NumPy C API when `GPLATES_HAVE_BOOST_PYTHON_NUMPY` / `GPLATES_HAVE_NUMPY_C_API` are configured in.

The whole body is wrapped in `#ifndef Q_MOC_RUN` because Qt's moc cannot parse the `BOOST_JOIN` macro used inside Boost, so any header that both needs Python and is processed by moc must guard the Python include this way. `PUSH_MSVC_WARNINGS`/`DISABLE_MSVC_WARNING(4996)`/`POP_MSVC_WARNINGS` (from `CompilerWarnings.h`) bracket the includes to silence an MSVC deprecation warning raised by Boost.Python's use of `PyEval_CallFunction`.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_PYTHON_H` | macro | `None` | — |
| `DISABLE_MSVC_WARNING` | variable | `PUSH_MSVC_WARNINGS` | Disable MSVC warning C4996: "'PyEval\_CallFunction': deprecated in 3.9" ...since 'PyEval\_CallFunction' is used inside boost-python (tested with boost 1.69). |
| `HAVE_SNPRINTF` | macro | `None` | — |
| `DEBUG_UNDEFINED_FROM_GLOBAL_PYTHON_H` | macro | `None` | — |
| `_DEBUG` | macro | `None` | — |
| `BOOST_BIND_GLOBAL_PLACEHOLDERS` | macro | `None` | boost::python Note: Boost 1.73+ deprecated including \<boost/bind.hpp\> in favour of including \<boost/bind/bind.hpp\> in order to avoid importing the placeholders \_1, \_2, etc, into the global namespace. |
| `NO_IMPORT_ARRAY` | macro | `None` | — |
| `PY_ARRAY_UNIQUE_SYMBOL` | macro | `PYGPLATES_NUMPY_ARRAY_API` | This just needs to be something unique (that doesn't clash with boost::python::numpy for example). |
| `NPY_NO_DEPRECATED_API` | macro | `NPY_1_7_API_VERSION` | Avoid deprecation warnings. |

## Notes

Some source files must include this header before `<ctype.h>` gets pulled in transitively by anything else, to work around a `<pyport.h>` compile error on Python versions older than 2.7.13/3.5.3 — get the include order wrong and only some translation units will fail to build, depending on what else they include first.

## Used by

| Unit | Component | References |
|---|---|---|
| [utils/deprecated/FilterMapReduceWorkFlow](../utils/deprecated/FilterMapReduceWorkFlow.md) | utils | 4 |
| [api/PythonUtils](../api/PythonUtils.md) | api | 3 |
| [utils/deprecated/GenericFilter](../utils/deprecated/GenericFilter.md) | utils | 3 |
| [utils/deprecated/GenericMapper](../utils/deprecated/GenericMapper.md) | utils | 3 |
| [api/PyApplication](../api/PyApplication.md) | api | 2 |
| [api/PythonExecutionThread](../api/PythonExecutionThread.md) | api | 2 |
| [api/PythonRunner](../api/PythonRunner.md) | api | 2 |
| [data-mining/deprecated/DataOperator](../data-mining/deprecated/DataOperator.md) | data-mining | 2 |
| [data-mining/deprecated/IsInRegionOfInterestVisitor](../data-mining/deprecated/IsInRegionOfInterestVisitor.md) | data-mining | 2 |
| [gui/PythonManager](../gui/PythonManager.md) | gui | 2 |
| [api/AbstractConsole](../api/AbstractConsole.md) | api | 1 |
| [api/AbstractPythonRunner](../api/AbstractPythonRunner.md) | api | 1 |
| [api/CoReg](../api/CoReg.md) | api | 1 |
| [api/ConsoleReader](../api/ConsoleReader.md) | api | 1 |
| [api/ConsoleWriter](../api/ConsoleWriter.md) | api | 1 |
| [api/PyColour](../api/PyColour.md) | api | 1 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 1 |
| [api/PyFeature](../api/PyFeature.md) | api | 1 |
| [api/PyFeatureCollection](../api/PyFeatureCollection.md) | api | 1 |
| [api/PyFunctions](../api/PyFunctions.md) | api | 1 |

*... and 19 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/python.h
```
