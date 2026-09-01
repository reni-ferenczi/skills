# ModelInterface

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1644 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/ModelInterface.h` | C++ | 111 |
| `src/model/ModelInterface.cc` | C++ | 36 |

## Overview

`ModelInterface` is the public face of the p-impl pair with `Model`: it holds a
`boost::shared_ptr<Model>` and forwards member access through `operator->()`
(and the equivalent `access_model()`) so that everything outside the model tier
depends only on this header, never on `Model.h`. That keeps `Model`'s own
includes out of the rest of the codebase's compile graph and lets `Model`'s
internals change without forcing a rebuild of its many callers.

The default constructor creates a brand-new `Model`; copy-construction instead
shares the existing one, cheaply, by copying the `shared_ptr` and bumping its
reference count. Because of that sharing, every `ModelInterface` copied from a
given original refers to the same underlying `Model` and its feature store —
copying a `ModelInterface` does not clone the model's data.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::ModelInterface`](#gplatesmodelmodelinterface) | class | — | — | 0 | This class serves as a very simple "p-impl" interface to class Model. |

## Members

### `GPlatesModel::ModelInterface`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ModelInterface()` | constructor | `None` | public | Construct a new ModelInterface instance. |
| `ModelInterface( const ModelInterface &other)` | constructor | `None` | public | Copy-construct a new ModelInterface instance. |
| `~ModelInterface()` | destructor | `None` | public | Destroy this ModelInterface instance. |
| `operator->()` | operator | `Model` | public | Access the members of the Model instance. |
| `access_model()` | method | `Model` | public | Access the members of the Model instance. |
| `d_model_ptr` | field | `boost::shared_ptr<Model>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_MODELINTERFACE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/FeatureCollectionFileIO](../app-logic/FeatureCollectionFileIO.md) | app-logic | 10 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 7 |
| [canvas-tools/SplitFeature](../canvas-tools/SplitFeature.md) | canvas-tools | 5 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 5 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 5 |
| [app-logic/ApplicationState](../app-logic/ApplicationState.md) | app-logic | 4 |
| [app-logic/FeatureCollectionFileState](../app-logic/FeatureCollectionFileState.md) | app-logic | 4 |
| [cli/CliFeatureCollectionFileIO](../cli/CliFeatureCollectionFileIO.md) | cli | 4 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 4 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 4 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 4 |
| [qt-widgets/ManageFeatureCollectionsEditConfigurations](../qt-widgets/ManageFeatureCollectionsEditConfigurations.md) | qt-widgets | 4 |
| [view-operations/SplitFeatureGeometryOperation](../view-operations/SplitFeatureGeometryOperation.md) | view-operations | 4 |
| [app-logic/deprecated/PaleomagWorkflow](../app-logic/deprecated/PaleomagWorkflow.md) | app-logic | 3 |
| [app-logic/deprecated/PlateVelocityWorkflow](../app-logic/deprecated/PlateVelocityWorkflow.md) | app-logic | 3 |
| [cli/CliConvertFileFormatCommand](../cli/CliConvertFileFormatCommand.md) | cli | 3 |
| [file-io/File](../file-io/File.md) | file-io | 3 |
| [file-io/deprecated/Writer](../file-io/deprecated/Writer.md) | file-io | 3 |
| [model/ModelUtils](ModelUtils.md) | model | 3 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](../qt-widgets/GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 3 |

*... and 28 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/ModelInterface.h
python scripts/gpq.py def GPlatesModel::ModelInterface --body
python scripts/gpq.py uses ModelInterface --kind class
python scripts/gpq.py hier ModelInterface
```
