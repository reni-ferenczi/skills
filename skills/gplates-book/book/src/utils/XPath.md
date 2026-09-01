# XPath

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 657 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/XPath.h` | C++ | 191 |
| `src/utils/XPath.cc` | C++ | 432 |

## Overview

[[[PROSE overview unit=utils/XPath tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::TokenizerState`](#anonymoustokenizerstate) | enum | — | — | 0 | — |
| [`GPlatesUtils::XPath::Tokenizer`](#gplatesutilsxpathtokenizer) | class | — | — | 0 | A tokenizer to assist with parsing an XPath expression. |

## Members

### `(anonymous)::TokenizerState`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TOKEN_START` | enumerator | `None` | — | — |
| `IN_VARIABLE` | enumerator | `None` | — | — |
| `IN_NUMERIC_LITERAL` | enumerator | `None` | — | — |
| `IN_NUMERIC_LITERAL_IMMEDIATELY_AFTER_E` | enumerator | `None` | — | — |
| `IN_STRING_LITERAL` | enumerator | `None` | — | — |
| `IN_STRING_LITERAL_POTENTIAL_CLOSING_QUOTE_SEEN` | enumerator | `None` | — | — |
| `IN_OPERATOR` | enumerator | `None` | — | — |

### `GPlatesUtils::XPath::Tokenizer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Token` | enum | `None` | public | — |
| `Exception` | struct | `None` | public | Thrown by this class to indicate a failed tokenization \*/ |
| `Tokenizer( const QString &str)` | constructor | `None` | public | Constructs a Tokenizer that will tokenize str. |
| `next()` | method | `void` | public | Advances the tokenizer to the next token. |
| `curr_token()` | method | `Token` | public | Returns the current token as an enumerated value. |
| `curr_integer_literal()` | method | `int` | public | Returns the current integer literal. |
| `curr_double_literal()` | method | `double` | public | Returns the current double literal. |
| `get_token_as_string` | field | `QString` | public | Returns a string version of the given token; useful for debugging. |
| `parse_variable( const QString &str)` | method | `void` | private | — |
| `parse_numeric_literal( const QString &str)` | method | `void` | private | — |
| `parse_operator( const QString &str)` | method | `void` | private | — |
| `throw_exception()` | method | `void` | private | — |
| `d_str` | field | `QString` | private | — |
| `d_pos` | field | `int` | private | — |
| `d_curr_token` | field | `Token` | private | — |
| `d_curr_variable` | field | `boost::optional<QString>` | private | — |
| `d_curr_integer_literal` | field | `boost::optional<int>` | private | — |
| `d_curr_double_literal` | field | `boost::optional<double>` | private | — |
| `d_curr_string_literal` | field | `boost::optional<QString>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_XPATH_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=utils/XPath tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/XPath.h
python scripts/gpq.py def GPlatesUtils::XPath::Tokenizer --body
python scripts/gpq.py uses Tokenizer --kind class
python scripts/gpq.py hier Tokenizer
```
