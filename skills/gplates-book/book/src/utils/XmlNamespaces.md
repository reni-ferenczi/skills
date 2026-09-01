# XmlNamespaces

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1116 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/XmlNamespaces.h` | C++ | 159 |
| `src/utils/XmlNamespaces.cc` | C++ | 274 |

## Overview

[[[PROSE overview unit=utils/XmlNamespaces tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_XMLNAMESPACES_H` | macro | `None` | — |
| `gpgim_namespace()` | function | `char` | NOTE: The GPGIM namespace is not part of the feature readers but is placed here in order to re-use a lot of the XML parsing machinery when reading the GPGIM XML file. |
| `gpml_namespace()` | function | `char` | — |
| `gml_namespace()` | function | `char` | — |
| `xsi_namespace()` | function | `char` | — |
| `gpgim_standard_alias()` | function | `char` | NOTE: The GPGIM namespace is not part of the feature readers but is placed here in order to re-use a lot of the XML parsing machinery when reading the GPGIM XML file. |
| `gpml_standard_alias()` | function | `char` | — |
| `gml_standard_alias()` | function | `char` | — |
| `xsi_standard_alias()` | function | `char` | — |
| `get_gpgim_namespace` | variable | `GPlatesUtils::UnicodeString` | — |
| `get_gpml_namespace` | variable | `GPlatesUtils::UnicodeString` | — |
| `get_gml_namespace` | variable | `GPlatesUtils::UnicodeString` | — |
| `get_xsi_namespace` | variable | `GPlatesUtils::UnicodeString` | — |
| `get_gpgim_namespace_qstring` | variable | `QString` | — |
| `get_gpml_namespace_qstring` | variable | `QString` | — |
| `get_gml_namespace_qstring` | variable | `QString` | — |
| `get_xsi_namespace_qstring` | variable | `QString` | — |
| `get_gpgim_standard_alias` | variable | `GPlatesUtils::UnicodeString` | — |
| `get_gpml_standard_alias` | variable | `GPlatesUtils::UnicodeString` | — |
| `get_gml_standard_alias` | variable | `GPlatesUtils::UnicodeString` | — |
| `get_xsi_standard_alias` | variable | `GPlatesUtils::UnicodeString` | — |
| `get_gpgim_standard_alias_qstring` | variable | `QString` | — |
| `get_gpml_standard_alias_qstring` | variable | `QString` | — |
| `get_gml_standard_alias_qstring` | variable | `QString` | — |
| `get_xsi_standard_alias_qstring` | variable | `QString` | — |
| `get_standard_alias_for_namespace( const GPlatesUtils::UnicodeString &namespace_uri)` | function | `StringSet::SharedIterator` | Returns the standard namespace alias for the given namespace URI. |
| `get_namespace_for_standard_alias( const GPlatesUtils::UnicodeString &namespace_alias)` | function | `StringSet::SharedIterator` | Returns the namespace URI for the given standard namespace alias. |

## Notes

[[[PROSE notes unit=utils/XmlNamespaces tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/QualifiedXmlName](../model/QualifiedXmlName.md) | model | 21 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 15 |
| [file-io/XmlWriter](../file-io/XmlWriter.md) | file-io | 13 |
| [model/Gpgim](../model/Gpgim.md) | model | 9 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/XmlNamespaces.h
```
