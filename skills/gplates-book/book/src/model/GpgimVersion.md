# GpgimVersion

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1124 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimVersion.h` | C++ | 186 |
| `src/model/GpgimVersion.cc` | C++ | 213 |

## Overview

[[[PROSE overview unit=model/GpgimVersion tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::GpgimVersion`](#gplatesmodelgpgimversion) | class | `boost::less_than_comparable<GpgimVersion>`<br>`boost::equality_comparable<GpgimVersion>`<br>[`GPlatesUtils::QtStreamable<GpgimVersion>`](../utils/QtStreamable.md) | — | 0 | The GPlates Geological Information Model (GPGIM) version number. |

## Members

### `GPlatesModel::GpgimVersion`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DEFAULT_ONE_POINT_SIX_REVISION` | field | `unsigned int` | public | The default version for "1.6" is "1.6.0317". |
| `FEATURE_COLLECTION_TAG` | field | `std::string` | public | The key string used when storing the GPGIM version as a tag in a FeatureCollectionHandle. |
| `create( const QString &version)` | method | `boost::optional<GpgimVersion>` | public | Creates a GpgimVersion from a "\<MAJOR\>.\<MINOR\>.\<REVISION\>" version string, or boost::none if the version string cannot be parsed. |
| `GpgimVersion( unsigned int major_, unsigned int minor_, unsigned int revision_)` | constructor | `None` | public | Constructs a GpgimVersion from version numbers. |
| `get_major()` | method | `unsigned int` | public | Returns the major version number in "\<MAJOR\>.\<MINOR\>.\<REVISION\>". |
| `get_minor()` | method | `unsigned int` | public | Returns the minor version number in "\<MAJOR\>.\<MINOR\>.\<REVISION\>". |
| `get_revision()` | method | `unsigned int` | public | Returns the revision number in "\<MAJOR\>.\<MINOR\>.\<REVISION\>". |
| `get_version_string()` | method | `QString` | public | Returns the version string as "\<MAJOR\>.\<MINOR\>.\<REVISION\>". |
| `operator==( const GpgimVersion &rhs)` | operator | `bool` | public | Equality comparison operator. |
| `operator<( const GpgimVersion &rhs)` | operator | `bool` | public | Less than comparison operator. |
| `d_major` | field | `unsigned int` | private | — |
| `d_minor` | field | `unsigned int` | private | — |
| `d_revision` | field | `unsigned int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `FEATURE_COLLECTION_TAG` | variable | `std::string` | — |
| `operator<( const GpgimVersion &rhs)` | operator | `bool` | — |
| `GPLATES_MODEL_GPGIMVERSION_H` | macro | `None` | — |
| `operator<<` | variable | `std::ostream` | — |

## Notes

[[[PROSE notes unit=model/GpgimVersion tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/Gpgim](Gpgim.md) | model | 8 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 5 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 3 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 3 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 2 |
| [qt-widgets/AboutDialog](../qt-widgets/AboutDialog.md) | qt-widgets | 2 |
| [qt-widgets/GpgimVersionWarningDialog](../qt-widgets/GpgimVersionWarningDialog.md) | qt-widgets | 2 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 1 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 1 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/GpgimVersion.h
python scripts/gpq.py def GPlatesModel::GpgimVersion --body
python scripts/gpq.py uses GpgimVersion --kind class
python scripts/gpq.py hier GpgimVersion
```
