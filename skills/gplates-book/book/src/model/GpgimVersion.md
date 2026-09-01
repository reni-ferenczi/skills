# GpgimVersion

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1124 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimVersion.h` | C++ | 186 |
| `src/model/GpgimVersion.cc` | C++ | 213 |

## Overview

`GpgimVersion` is a small value type for the `<MAJOR>.<MINOR>.<REVISION>` version
number stamped on the GPGIM itself, stored as the `gpml:version` attribute of a
GPML feature collection element and as the `FEATURE_COLLECTION_TAG` tag on a
`FeatureCollectionHandle`. It lets readers and writers compare "the version this
file was written against" to "the version this build of GPlates implements" and
decide whether an upgrade path is needed.

`create()` parses a version string leniently: the revision field can be omitted
only for `"1.6"`, in which case it defaults to `DEFAULT_ONE_POINT_SIX_REVISION`
(317), because GPlates wrote plain `"1.6"` into GPML files for years before the
three-part scheme was introduced in 2012, and existing files need to keep parsing
to the same effective version. `get_version_string()` renders the revision back out
zero-padded to four digits (`"1.6.0317"`), which is the convention used on the
GPGIM feed, even though `create()` also accepts the unpadded form. Ordering
(`operator<`, and the rest via `boost::less_than_comparable`) compares major, then
minor, then revision numerically, so version strings must not be compared as text.

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

The direct constructor throws `GPlatesGlobal::LogException` if given numbers that
don't form a valid version (major/minor not a non-zero single digit, major.minor
below 1.6, or revision zero or over 9999); `create()` instead returns `boost::none`
for the same conditions when parsing a string, so callers get a validating
constructor and a non-throwing parser side by side.

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
