# VisualLayerInputChannelName

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayerInputChannelName.h` | C++ | 52 |
| `src/presentation/VisualLayerInputChannelName.cc` | C++ | 102 |

## Overview

Provides a mapping from app-logic `LayerInputChannelName` enumerations to human-readable display strings for the GUI. The single function `get_input_channel_name()` translates layer connection type identifiers into user-friendly labels describing what kind of layer data each input channel expects—for example, `RECONSTRUCTION_FEATURES` becomes `"Reconstruction features"` and `CO_REGISTRATION_SEED_GEOMETRIES` becomes `"Reconstructed seed geometries"`.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PRESENTATION_VISUALLAYERINPUTCHANNELNAME_H` | macro | `None` | — |
| `get_input_channel_name( GPlatesAppLogic::LayerInputChannelName::Type layer_input_channel_name)` | function | `QString` | The visual layer input channel names. |

## Notes

The function asserts on unknown enumeration values; keep the switch statement in sync with `GPlatesAppLogic::LayerInputChannelName::Type`. The returned strings are presented directly to the user in the GUI, so changes to the text should be reviewed for UI impact.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/presentation/VisualLayerInputChannelName.h
```
