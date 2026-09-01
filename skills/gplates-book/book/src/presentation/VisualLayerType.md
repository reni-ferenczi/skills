# VisualLayerType

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 14 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayerType.h` | C++ | 47 |

## Overview

[[[PROSE overview unit=presentation/VisualLayerType tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=presentation/VisualLayerType tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
