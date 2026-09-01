# ExportFileNameTemplateValidationUtils

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1583 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportFileNameTemplateValidationUtils.h` | C++ | 109 |
| `src/gui/ExportFileNameTemplateValidationUtils.cc` | C++ | 169 |

## Overview

[[[PROSE overview unit=gui/ExportFileNameTemplateValidationUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `INVALID_CHARACTERS` | variable | `std::string` | — |
| `GPLATES_GUI_EXPORTFILENAMETEMPLATEVALIDATIONUTILS_H` | macro | `None` | — |
| `is_valid_template_filename_sequence( const QString &filename_template, QString &filename_template_validation_message, bool check_filename_variation = true)` | function | `bool` | Returns true if filename template is a valid filename sequence. |
| `does_template_filename_have_invalid_characters( const QString &filename_template, QString &filename_template_validation_message)` | function | `bool` | Returns true if filename template has invalid characters. |
| `does_template_filename_have_percent_P( const QString &filename_template, QString &filename_template_validation_message)` | function | `bool` | Returns true if filename template contains "%P". |
| `is_valid_template_filename_sequence_without_percent_P( const QString &filename_template, QString &filename_template_validation_message, bool check_filename_variation = true)` | function | `bool` | A common usage of the above functions. |
| `is_valid_template_filename_sequence_with_percent_P( const QString &filename_template, QString &filename_template_validation_message, bool check_filename_variation = true)` | function | `bool` | A common usage of the above functions. |

## Notes

[[[PROSE notes unit=gui/ExportFileNameTemplateValidationUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/ExportAnimationRegistry](ExportAnimationRegistry.md) | gui | 97 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/ExportFileNameTemplateValidationUtils.h
```
