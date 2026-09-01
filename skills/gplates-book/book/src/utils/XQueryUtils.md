# XQueryUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1200 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/XQueryUtils.h` | C++ | 127 |
| `src/utils/XQueryUtils.cc` | C++ | 420 |

## Overview

[[[PROSE overview unit=utils/XQueryUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/XQueryUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
