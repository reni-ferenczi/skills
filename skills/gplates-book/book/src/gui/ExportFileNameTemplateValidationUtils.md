# ExportFileNameTemplateValidationUtils

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 1583 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/ExportFileNameTemplateValidationUtils.h` | C++ | 109 |
| `src/gui/ExportFileNameTemplateValidationUtils.cc` | C++ | 169 |

## Overview

`ExportFileNameTemplateValidationUtils` is a small function namespace that checks export filename templates before an animation export runs, so `ExportAnimationRegistry`'s `validate_filename_template()` and the export option widgets can reject a bad template (illegal characters, missing `%P` where a per-export-type placeholder is required, or no time-varying placeholder when one is needed) with an explanatory message instead of failing partway through a batch export. `is_valid_template_filename_sequence()` does the actual sequence check by constructing an `ExportTemplateFilename`; `does_template_filename_have_invalid_characters()` and `does_template_filename_have_percent_P()` check narrower conditions, and `is_valid_template_filename_sequence_with_percent_P()` / `..._without_percent_P()` combine all three checks for the two common cases — export strategies that need one file per `ReconstructionGeometry` type (`%P`) and those that do not.

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

The invalid-character set (`INVALID_CHARACTERS` in the `.cc`) is `/\|*?"><:` — the characters illegal in Windows filenames — so validation is stricter than a POSIX filesystem strictly requires.

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
