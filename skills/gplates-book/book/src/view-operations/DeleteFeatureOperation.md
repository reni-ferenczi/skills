# DeleteFeatureOperation

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 1732 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/DeleteFeatureOperation.h` | C++ | 71 |
| `src/view-operations/DeleteFeatureOperation.cc` | C++ | 59 |

## Overview

[[[PROSE overview unit=view-operations/DeleteFeatureOperation tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=view-operations/DeleteFeatureOperation tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
