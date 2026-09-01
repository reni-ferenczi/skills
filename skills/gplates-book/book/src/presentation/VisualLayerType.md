# VisualLayerType

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 14 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayerType.h` | C++ | 47 |

## Overview

`VisualLayerType::Type` is a plain alias for `GPlatesAppLogic::LayerTaskType::Type`. The header's own comment explains why the alias still exists: it used to be a distinct enumeration so that visual layers not backed by an app-logic layer could be represented, but every visual layer is now backed by one, so the type has been collapsed to a typedef of the app-logic type it wraps.

The alias is kept, rather than replacing all uses with `GPlatesAppLogic::LayerTaskType::Type` directly, so that presentation-layer code (`VisualLayerRegistry`, `VisualLayers`, the Qt widgets that list layer types) can keep referring to "visual layer type" in its own vocabulary while still being the same value as the underlying layer task type.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresentation::VisualLayerType::Type`](#gplatespresentationvisuallayertypetype) | typedef | — | — | 0 | — |

## Members

### `GPlatesPresentation::VisualLayerType::Type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_VISUALLAYERTYPE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/VisualLayerRegistry](VisualLayerRegistry.md) | presentation | 35 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 8 |
| [presentation/VisualLayer](VisualLayer.md) | presentation | 4 |
| [presentation/VisualLayers](VisualLayers.md) | presentation | 4 |
| [qt-widgets/AddNewLayerDialog](../qt-widgets/AddNewLayerDialog.md) | qt-widgets | 4 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 3 |
| [qt-widgets/VisualLayersComboBox](../qt-widgets/VisualLayersComboBox.md) | qt-widgets | 3 |
| [qt-widgets/ConfigureVelocityLegendOverlayDialog](../qt-widgets/ConfigureVelocityLegendOverlayDialog.md) | qt-widgets | 1 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/VisualLayerType.h
python scripts/gpq.py def GPlatesPresentation::VisualLayerType::Type --body
python scripts/gpq.py uses Type --kind typedef
```
