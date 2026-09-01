# UnicodeStringUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1810 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/UnicodeStringUtils.h` | C++ | 94 |

## Overview

Free functions that convert between ICU's `GPlatesUtils::UnicodeString` (an
alias defined in `global/unicode.h`) and Qt's `QString`/`std::string`, since
the model stores textual content — `FeatureType`, `FeatureId`, `PropertyName`,
`TextContent` and similar Unicode string containers — as ICU strings while the
GUI and most of the rest of the codebase work in `QString`. `make_qstring()`
is the generic entry point: it is a template that calls `T::get()` on any
Model string-container type and converts the result, so callers do not need
to know each container's exact accessor pattern.

Every function is a thin `inline` wrapper around ICU's own `qstring()`
conversion or a direct constructor call, with no buffering, encoding
negotiation or error handling of its own.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_UNICODESTRINGUTILS_H` | macro | `None` | — |
| `make_qstring_from_icu_string( const GPlatesUtils::UnicodeString &icu_string)` | function | `QString` | Make a QString from an ICU UnicodeString. |
| `make_std_string_from_icu_string( const GPlatesUtils::UnicodeString &icu_string)` | function | `std::string` | Make a std::string from an ICU UnicodeString. |
| `make_qstring( const T &source)` | function | `QString` | Make a QString from a Unicode string container in the Model. |
| `make_icu_string_from_qstring( const QString &qstring)` | function | `GPlatesUtils::UnicodeString` | Make a ICU UnicodeString from a QString. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 33 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 26 |
| [model/QualifiedXmlName](../model/QualifiedXmlName.md) | model | 19 |
| [file-io/XmlWriter](../file-io/XmlWriter.md) | file-io | 17 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 13 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 11 |
| [qt-widgets/EditOldPlatesHeaderWidget](../qt-widgets/EditOldPlatesHeaderWidget.md) | qt-widgets | 10 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](../file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 9 |
| [model/Gpgim](../model/Gpgim.md) | model | 9 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 8 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 7 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 6 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 6 |
| [model/XmlNode](../model/XmlNode.md) | model | 6 |
| [qt-widgets/CoRegistrationLayerConfigurationDialog](../qt-widgets/CoRegistrationLayerConfigurationDialog.md) | qt-widgets | 6 |
| [qt-widgets/EditStringListWidget](../qt-widgets/EditStringListWidget.md) | qt-widgets | 6 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 5 |
| [feature-visitors/ShapefileAttributeFinder](../feature-visitors/ShapefileAttributeFinder.md) | feature-visitors | 5 |
| [file-io/GpmlFeatureReaderFactory](../file-io/GpmlFeatureReaderFactory.md) | file-io | 5 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 5 |

*... and 89 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/UnicodeStringUtils.h
```
