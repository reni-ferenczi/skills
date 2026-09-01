# TranscribeEnumProtocol

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 1070 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeEnumProtocol.h` | C++ | 309 |
| `src/scribe/TranscribeEnumProtocol.cc` | C++ | 65 |

## Overview

[[[PROSE overview unit=scribe/TranscribeEnumProtocol tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::EnumValue`](#gplatesscribeenumvalue) | struct | — | — | 0 | Associate an enumeration value (integer) with a name (string). |

## Members

### `GPlatesScribe::EnumValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `EnumValue( const char *name_, int value_)` | constructor | `None` | public | — |
| `name` | field | `char` | public | — |
| `value` | field | `int` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBEENUMPROTOCOL_H` | macro | `None` | — |
| `TRANSCRIBE_SOURCE` | macro | `GPlatesUtils::CallStack::Trace(__FILE__, __LINE__)` | — |
| `transcribe_enum_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, // Use 'TRANSCRIBE_SOURCE' here Scribe &scribe, EnumType &e, EnumValueIter enum_values_begin, EnumValueIter enum_values_end)` | function | `TranscribeResult` | ENUM\_VALUE\_2, ENUM\_VALUE\_3 // NOTE: Any new values should also be added to transcribe. }; // // Transcribe for sessions/projects. // // Use friend function (injection) so can access private enum. // And implement in class body otherwise ... |
| `is_scribe_saving( Scribe &scribe)` | function | `bool` | — |
| `is_scribe_loading( Scribe &scribe)` | function | `bool` | — |
| `transcribe_enum_name( Scribe &scribe, const std::string &enum_name)` | function | `TranscribeResult` | — |
| `transcribe_enum_protocol( const GPlatesUtils::CallStack::Trace &transcribe_source, Scribe &scribe, EnumType &e, EnumValueIter enum_values_begin, EnumValueIter enum_values_end)` | function | `TranscribeResult` | — |

## Notes

[[[PROSE notes unit=scribe/TranscribeEnumProtocol tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/BuiltinColourPalettes](../gui/BuiltinColourPalettes.md) | gui | 80 |
| [data-mining/Types](../data-mining/Types.md) | data-mining | 25 |
| [app-logic/LayerInputChannelName](../app-logic/LayerInputChannelName.md) | app-logic | 24 |
| [view-operations/ScalarField3DRenderParameters](../view-operations/ScalarField3DRenderParameters.md) | view-operations | 19 |
| [app-logic/LayerTaskType](../app-logic/LayerTaskType.md) | app-logic | 13 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 13 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 12 |
| [gui/BuiltinColourPaletteType](../gui/BuiltinColourPaletteType.md) | gui | 8 |
| [gui/Symbol](../gui/Symbol.md) | gui | 8 |
| [app-logic/VelocityDeltaTime](../app-logic/VelocityDeltaTime.md) | app-logic | 7 |
| [app-logic/TopologyNetworkParams](../app-logic/TopologyNetworkParams.md) | app-logic | 6 |
| [presentation/ReconstructVisualLayerParams](../presentation/ReconstructVisualLayerParams.md) | presentation | 6 |
| [app-logic/VelocityParams](../app-logic/VelocityParams.md) | app-logic | 5 |
| [app-logic/ReconstructParams](../app-logic/ReconstructParams.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeEnumProtocol.h
python scripts/gpq.py def GPlatesScribe::EnumValue --body
python scripts/gpq.py uses EnumValue --kind struct
python scripts/gpq.py hier EnumValue
```
