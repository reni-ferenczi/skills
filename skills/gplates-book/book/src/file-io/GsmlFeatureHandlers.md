# GsmlFeatureHandlers

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 663 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GsmlFeatureHandlers.h` | C++ | 81 |
| `src/file-io/GsmlFeatureHandlers.cc` | C++ | 160 |

## Overview

[[[PROSE overview unit=file-io/GsmlFeatureHandlers tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::GsmlFeatureHandler`](#gplatesfileiogsmlfeaturehandler) | class | — | — | 0 | — |
| [`GPlatesFileIO::GsmlFeatureHandlerFactory`](#gplatesfileiogsmlfeaturehandlerfactory) | class | — | — | 0 | — |

## Members

### `GPlatesFileIO::GsmlFeatureHandler`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `handle_feature_member( FeatureCollectionHandle::weak_ref fc, QByteArray&)` | method | `void` | public | — |
| `~GsmlFeatureHandler()` | destructor | `None` | public | — |
| `handle_gsml_feature( const QString& feature_type_str, FeatureCollectionHandle::weak_ref fc, QBuffer& xml_data)` | method | `void` | protected | Override this function in subclass to change the behavior of GsmlFeatureHandler. |

### `GPlatesFileIO::GsmlFeatureHandlerFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_instance()` | method | `boost::shared_ptr<GsmlFeatureHandler>` | public | Give user an opportunity to use different GsmlFeatureHandler. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_GSMLFEATUREHANDLERS_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GsmlFeatureHandlers tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GeoscimlProfile](GeoscimlProfile.md) | file-io | 7 |
| [file-io/GsmlFeaturesDef](GsmlFeaturesDef.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GsmlFeatureHandlers.h
python scripts/gpq.py def GPlatesFileIO::GsmlFeatureHandler --body
python scripts/gpq.py uses GsmlFeatureHandler --kind class
python scripts/gpq.py hier GsmlFeatureHandler
```
