# python

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 0 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/global/python.h` | C++ | 172 |

## Overview

[[[PROSE overview unit=global/python tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=global/python tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
