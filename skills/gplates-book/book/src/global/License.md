# License

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 0 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/License.h` | C++ | 49 |

## Overview

The `License` namespace provides functions to retrieve GPlates' copyright information in plain-text and HTML-formatted forms, used by the About dialog and other UI components that display license and attribution details.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GLOBAL_LICENSE_H` | macro | `None` | — |
| `get_copyright_string()` | function | `QString` | — |
| `get_html_copyright_string()` | function | `QString` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/AboutDialog](../qt-widgets/AboutDialog.md) | qt-widgets | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/License.h
```
