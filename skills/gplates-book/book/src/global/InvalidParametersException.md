# InvalidParametersException

[Book TOC](../../TOC.md) · [global](../../components/global.md) · cluster Community 17 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/global/InvalidParametersException.h` | C++ | 73 |

## Overview

[[[PROSE overview unit=global/InvalidParametersException tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGlobal::InvalidParametersException`](#gplatesglobalinvalidparametersexception) | class | [`Exception`](GPlatesException.md) | — | 0 | Should be thrown when a method is called with parameters which are invalid in combination (but none are specifically invalid on their own). |

## Members

### `GPlatesGlobal::InvalidParametersException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidParametersException( const GPlatesUtils::CallStack::Trace &exception_source, const char *msg)` | constructor | `None` | public | — |
| `~InvalidParametersException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `_msg` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `_GPLATES_GLOBAL_INVALIDPARAMETERSEXCEPTION_H_` | macro | `None` | — |

## Notes

[[[PROSE notes unit=global/InvalidParametersException tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/FeatureSummaryWidget](../qt-widgets/FeatureSummaryWidget.md) | qt-widgets | 2 |
| [maths/PolygonOnSphere](../maths/PolygonOnSphere.md) | maths | 1 |
| [maths/PolylineOnSphere](../maths/PolylineOnSphere.md) | maths | 1 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/global/InvalidParametersException.h
python scripts/gpq.py def GPlatesGlobal::InvalidParametersException --body
python scripts/gpq.py uses InvalidParametersException --kind class
python scripts/gpq.py hier InvalidParametersException
```
