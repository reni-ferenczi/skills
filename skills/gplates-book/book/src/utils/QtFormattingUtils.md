# QtFormattingUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1864 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/QtFormattingUtils.h` | C++ | 77 |

## Overview

Provides formatting utilities for Qt types. `qdatetime_to_elapsed_duration()` takes a `QDateTime` (typically a feature creation time) and returns a human-readable string describing the elapsed time since that moment. For recent events it returns phrases like "right now", "5 minutes ago", "1 hour ago"; for events more than a week old it returns the date itself. This is used in the Clicked Feature Table to provide at-a-glance feedback on when features were created.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_QTFORMATTINGUTILS_H` | macro | `None` | — |
| `qdatetime_to_elapsed_duration( const QDateTime &from)` | function | `QString` | Format a QDateTime from (e.g. |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/QtFormattingUtils.h
```
