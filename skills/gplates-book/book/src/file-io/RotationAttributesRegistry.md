# RotationAttributesRegistry

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1075 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/RotationAttributesRegistry.h` | C++ | 123 |
| `src/file-io/RotationAttributesRegistry.cc` | C++ | 86 |

## Overview

`RotationMetadataRegistry` is a `GPlatesUtils::Singleton` schema for the
metadata attribute names that can appear in a GPlates-extended PLATES4
rotation (`.rot`) file — things like `DC:creator:name`, `MPRS:pid`, `GTS`,
`REF`, `HELL:kappahat`. Its constructor registers every known attribute name
against a `MetadataAttribute` describing which category it belongs to
(`HEADER`, `DC` for Dublin Core, `MPRS` for the moving-plate rotation
sequence, or `POLE` for a single pole), whether it is `MANDATORY`, whether it
can occur more than once (`MULTI_OCCUR`), and — for `REFERENCE` attributes
such as `REF`, `DOI`, `AU`, `GTS` and `CHRONID` — which other registered
attribute's value it points back to (carried in `ref_name`).

Readers and dialogs that parse or display rotation-file metadata (notably
`PlatesRotationFileProxy` and `PlatesRotationFormatReader`) look attribute
names up here rather than hard-coding the schema, and can also pull the
subset matching a combination of `MetadataType` flags via the bitmask
overload of `get()`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::MetadataType::MetadataType`](#gplatesfileiometadatatypemetadatatype) | enum | — | — | 0 | — |
| [`GPlatesFileIO::MetadataAttribute`](#gplatesfileiometadataattribute) | struct | — | — | 0 | — |
| [`GPlatesFileIO::RotationMetadataRegistry`](#gplatesfileiorotationmetadataregistry) | class | [`GPlatesUtils::Singleton<RotationMetadataRegistry>`](../utils/Singleton.md) | — | 0 | Rotation Attributes Registry |

## Members

### `GPlatesFileIO::MetadataType::MetadataType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Invalid` | enumerator | `None` | — | — |
| `DC` | enumerator | `None` | — | — |
| `HEADER` | enumerator | `None` | — | — |
| `MPRS` | enumerator | `None` | — | — |
| `POLE` | enumerator | `None` | — | — |
| `MANDATORY` | enumerator | `None` | — | — |
| `MULTI_OCCUR` | enumerator | `None` | — | — |
| `REFERENCE` | enumerator | `None` | — | — |

### `GPlatesFileIO::MetadataAttribute`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MetadataAttribute( quint64 flags = MetadataType::Invalid, const QString& ref_str = "")` | constructor | `None` | public | — |
| `type_flag` | field | `quint64` | public | — |
| `ref_name` | field | `QString` | public | — |

### `GPlatesFileIO::RotationMetadataRegistry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MetadataAttrMap` | typedef | `std::map<QString,MetadataAttribute>` | public | — |
| `register_metadata( const QString& name, const MetadataAttribute& attr)` | method | `void` | public | — |
| `get( const QString& name)` | method | `MetadataAttribute` | public | — |
| `get( quint64 flags)` | method | `MetadataAttrMap` | public | — |
| `d_map` | field | `MetadataAttrMap` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILEIO_ROTATIONATTRIBUTESREGISTRY_H` | macro | `None` | — |

## Notes

`get(const QString &name)` returns a default-constructed `MetadataAttribute`
(`type_flag == MetadataType::Invalid`) for an unregistered name rather than
signalling failure some other way — callers must check the flag, not assume a
non-null return means the name was recognised.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesRotationFileProxy](PlatesRotationFileProxy.md) | file-io | 38 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 23 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 18 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 10 |
| [file-io/PlatesRotationFormatReader](PlatesRotationFormatReader.md) | file-io | 8 |
| [feature-visitors/TotalReconstructionSequenceRotationInserter](../feature-visitors/TotalReconstructionSequenceRotationInserter.md) | feature-visitors | 2 |
| [qt-widgets/GenerateVelocityDomainTerraDialog](../qt-widgets/GenerateVelocityDomainTerraDialog.md) | qt-widgets | 2 |
| [file-io/GsmlPropertyHandlers](GsmlPropertyHandlers.md) | file-io | 1 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 1 |
| [model/XmlNode](../model/XmlNode.md) | model | 1 |
| [qt-widgets/ScalarField3DDepthLayersPage](../qt-widgets/ScalarField3DDepthLayersPage.md) | qt-widgets | 1 |
| [qt-widgets/TimeDependentRasterPage](../qt-widgets/TimeDependentRasterPage.md) | qt-widgets | 1 |
| [utils/XQueryUtils](../utils/XQueryUtils.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/RotationAttributesRegistry.h
python scripts/gpq.py def GPlatesFileIO::RotationMetadataRegistry --body
python scripts/gpq.py uses RotationMetadataRegistry --kind class
python scripts/gpq.py hier RotationMetadataRegistry
```
