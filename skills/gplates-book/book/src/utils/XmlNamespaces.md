# XmlNamespaces

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1116 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/XmlNamespaces.h` | C++ | 159 |
| `src/utils/XmlNamespaces.cc` | C++ | 274 |

## Overview

Central registry of the fixed XML namespace URIs and their standard aliases
used when reading and writing GPlates' XML formats: `gpml` (GPlates' own
namespace), `gml` (OGC Geography Markup Language), `xsi`
(XMLSchema-instance) and `gpgim` (the GPGIM's own XML schema, which reuses
this machinery purely to share XML parsing code with the feature readers,
per the header's own note, even though it is not itself a feature namespace).
Each namespace/alias is exposed both as an ICU `GPlatesUtils::UnicodeString`
and as a `QString`, since callers on the parsing side work in ICU strings and
callers on the Qt/GUI side work in `QString`.

`get_standard_alias_for_namespace()` and `get_namespace_for_standard_alias()`
do the URI-to-alias and alias-to-URI lookups through a `StringSet`, falling
back to the `gpml` namespace/alias when given anything unrecognised, so callers
get a definite answer rather than an empty or invalid result for unexpected
input.

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

The namespace and alias strings are function-local `static const` values
(Meyers singletons) rather than namespace-scope statics, specifically to
sidestep C++'s unspecified initialisation order for non-local static objects
across translation units — a comment in the header calls this out explicitly.
Unrecognised namespace URIs or aliases silently map to `gpml` rather than
signalling an error, so a typo in calling code will not surface as a lookup
failure.

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
