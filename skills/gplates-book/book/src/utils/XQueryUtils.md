# XQueryUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1200 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/XQueryUtils.h` | C++ | 127 |
| `src/utils/XQueryUtils.cc` | C++ | 420 |

## Overview

Thin wrappers around Qt's `QXmlQuery`/`QXmlSerializer` XQuery engine, giving
callers a way to run an XQuery/XPath expression against an in-memory XML
document and get plain `QByteArray` or `QVariant` results back instead of
Qt's node/item API. `evaluate_query()` and `evaluate_features()` both prefix
the caller's query with `GPlatesFileIO::GsmlConst::all_namespaces()` so
callers can write bare, unprefixed GeoSciML/GML element names, evaluate to a
single serialized `QByteArray`, and then split that byte array back into
individual elements by textually matching the closing/opening tag pair for
the queried element name (`evaluate_query()`) or `gml:featureMember`
(`evaluate_features()`) — there is no structural splitting, so it depends on
the serializer not reformatting those tags. `evaluate_attribute()` instead
walks a `QXmlResultItems` to pull out atomic attribute values. This unit
exists specifically to support the GeoSciML file readers (`GsmlNodeProcessor`,
`GsmlFeatureHandlers`, `GsmlPropertyHandlers`) and `model/Metadata`, which query
XML metadata blocks rather than parsing them with a DOM or SAX-style reader.

`next_start_element()` is unrelated to XQuery: it is a small polyfill for
`QXmlStreamReader::readNextStartElement()`, kept here for callers stuck with
an older Qt.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::XQuery::IsEmptyFun`](#gplatesutilsxqueryisemptyfun) | typedef | — | — | 0 | — |

## Members

### `GPlatesUtils::XQuery::IsEmptyFun`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_XQUERYUTILS_H` | macro | `None` | — |
| `evaluate_query( QByteArray& xml_data, const QString& query_str)` | function | `std::vector<QByteArray>` | — |
| `evaluate_query( QBuffer& buf, const QString& query_str)` | function | `std::vector<QByteArray>` | — |
| `evaluate_features( QByteArray& xml_data, const QString& query_str)` | function | `std::vector<QByteArray>` | FIXME: could this test be replaced with above? |
| `evaluate( QByteArray& xml_data, const QString& query_str, IsEmptyFun is_empty)` | function | `std::vector<QByteArray>` | Run the query\_str on xml\_data return the result in std::vector\<QByteArray\> |
| `evaluate( QBuffer& buf, const QString& query_str, IsEmptyFun is_empty)` | function | `std::vector<QByteArray>` | — |
| `evaluate_attribute( QByteArray& xml_data, const QString& attr_name)` | function | `std::vector<QVariant>` | retrieve the attribute value from xml\_data as string. |
| `wrap_xml_data( QByteArray& xml_data, const QString& wrapper)` | function | `void` | — |
| `is_empty(const QBuffer& data)` | function | `bool` | — |
| `next_start_element( QXmlStreamReader&)` | function | `bool` | The same as QXmlStreamReader::readNextStartElement(). |

## Notes

`evaluate_query()`'s tag-name splitting is derived from the last path segment
of the query string (text after the final `/`), so it only works for queries
shaped like simple element-selecting paths; a query that does not end in a
plain element name will not split correctly. The `evaluate()` overloads
declared with `IsEmptyFun` and the alternate result-walking path in
`evaluate_features()` are compiled out (`#if 0`) and are dead code, not part
of the active API despite appearing in the header.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/Metadata](../model/Metadata.md) | model | 59 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 26 |
| [file-io/GsmlFeatureHandlers](../file-io/GsmlFeatureHandlers.md) | file-io | 12 |
| [file-io/GeoscimlProfile](../file-io/GeoscimlProfile.md) | file-io | 6 |
| [file-io/GsmlNodeProcessor](../file-io/GsmlNodeProcessor.md) | file-io | 4 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/XQueryUtils.h
python scripts/gpq.py def GPlatesUtils::XQuery::IsEmptyFun --body
python scripts/gpq.py uses IsEmptyFun --kind typedef
```
