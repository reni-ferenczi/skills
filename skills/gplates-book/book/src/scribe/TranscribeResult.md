# TranscribeResult

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 89 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/TranscribeResult.h` | C++ | 87 |

## Overview

`TranscribeResult` is the status code returned from every transcribe call in the `GPlatesScribe` serialisation framework. `TRANSCRIBE_SUCCESS` means the object was read or written normally; the other two values distinguish two different ways an archive can fail to match the current code, which matters because they are recovered from differently. `TRANSCRIBE_INCOMPATIBLE` covers a structural mismatch — a tag missing from the transcription, or a primitive of the wrong kind — and can be handled by supplying a default value for the object. `TRANSCRIBE_UNKNOWN_TYPE` covers a polymorphic pointer, enum value or `boost::variant` alternative that this build of GPlates does not know about; callers that transcribe collections via a polymorphic base or a variant can use this distinction to drop just the unrecognised elements rather than treating the whole load as incompatible, which is the mechanism that lets older GPlates versions open project files saved by a newer one.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::TranscribeResult`](#gplatesscribetranscriberesult) | enum | — | — | 0 | The result of transcribing an object. |

## Members

### `GPlatesScribe::TranscribeResult`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TRANSCRIBE_SUCCESS` | enumerator | `None` | — | The type of the transcribed object was compatible (transcription-protocol-wise) with the transcription (loaded from archive) and hence was successfully transcribed. |
| `TRANSCRIBE_INCOMPATIBLE` | enumerator | `None` | — | The object was not transcribed because it was incompatible with the loaded transcription. |
| `TRANSCRIBE_UNKNOWN_TYPE` | enumerator | `None` | — | The object was not transcribed because an unknown type was encountered. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_TRANSCRIBERESULT_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 49 |
| [scribe/TranscribeBoost](TranscribeBoost.md) | scribe | 40 |
| [scribe/TranscribeQt](TranscribeQt.md) | scribe | 31 |
| [scribe/TranscribeStd](TranscribeStd.md) | scribe | 31 |
| [scribe/Scribe](Scribe.md) | scribe | 25 |
| [view-operations/ScalarField3DRenderParameters](../view-operations/ScalarField3DRenderParameters.md) | view-operations | 23 |
| [scribe/TranscribeArray](TranscribeArray.md) | scribe | 15 |
| [gui/BuiltinColourPalettes](../gui/BuiltinColourPalettes.md) | gui | 14 |
| [property-values/GeoTimeInstant](../property-values/GeoTimeInstant.md) | property-values | 12 |
| [app-logic/TopologyNetworkParams](../app-logic/TopologyNetworkParams.md) | app-logic | 11 |
| [scribe/TranscribeEnumProtocol](TranscribeEnumProtocol.md) | scribe | 10 |
| [scribe/TranscribeNonNullIntrusivePtr](TranscribeNonNullIntrusivePtr.md) | scribe | 10 |
| [data-mining/CoRegConfigurationTable](../data-mining/CoRegConfigurationTable.md) | data-mining | 9 |
| [gui/BuiltinColourPaletteType](../gui/BuiltinColourPaletteType.md) | gui | 8 |
| [scribe/ScribeAccess](ScribeAccess.md) | scribe | 7 |
| [data-mining/RegionOfInterestFilter](../data-mining/RegionOfInterestFilter.md) | data-mining | 6 |
| [scribe/ScribeInternalAccess](ScribeInternalAccess.md) | scribe | 6 |
| [app-logic/VelocityParams](../app-logic/VelocityParams.md) | app-logic | 5 |
| [gui/Symbol](../gui/Symbol.md) | gui | 5 |
| [scribe/TranscribeImpl](TranscribeImpl.md) | scribe | 5 |

*... and 26 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/TranscribeResult.h
python scripts/gpq.py def GPlatesScribe::TranscribeResult --body
python scripts/gpq.py uses TranscribeResult --kind enum
```
