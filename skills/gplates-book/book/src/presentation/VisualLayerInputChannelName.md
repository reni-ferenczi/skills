# VisualLayerInputChannelName

[Book TOC](../../TOC.md) · [presentation](../../components/presentation.md) · cluster Community 6 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/presentation/VisualLayerInputChannelName.h` | C++ | 52 |
| `src/presentation/VisualLayerInputChannelName.cc` | C++ | 102 |

## Overview

[[[PROSE overview unit=presentation/VisualLayerInputChannelName tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=presentation/VisualLayerInputChannelName tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
