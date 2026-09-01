# DeleteFeatureOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1732 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/DeleteFeatureOperation.h` | C++ | 71 |
| `src/view-operations/DeleteFeatureOperation.cc` | C++ | 59 |

## Overview

A thin wrapper that removes the currently focused feature from its parent feature collection. It exists to bridge the Qt signal/slot system with the feature model layer, allowing the main window and other GUI components to trigger feature deletion through `delete_focused_feature()` rather than directly manipulating the model.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::DeleteFeatureOperation`](#gplatesviewoperationsdeletefeatureoperation) | class | `QObject` | — | 0 | This class encapsulates the logic behind deleting the currently focused feature. |

## Members

### `GPlatesViewOperations::DeleteFeatureOperation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DeleteFeatureOperation( GPlatesGui::FeatureFocus &feature_focus, GPlatesAppLogic::ApplicationState &application_state)` | constructor | `None` | public | — |
| `delete_focused_feature()` | method | `void` | public | — |
| `d_feature_focus` | field | `GPlatesGui::FeatureFocus` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_VIEWOPERATIONS_DELETEFEATUREOPERATION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/DeleteFeatureOperation.h
python scripts/gpq.py def GPlatesViewOperations::DeleteFeatureOperation --body
python scripts/gpq.py uses DeleteFeatureOperation --kind class
python scripts/gpq.py hier DeleteFeatureOperation
```
