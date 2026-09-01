# Presenter

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 1872 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/presenter/Presenter.h` | C++ | 43 |

## Overview

[[[PROSE overview unit=deprecated/presenter/Presenter tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPresenter::Presenter`](#gplatespresenterpresenter) | class | — | — | 0 | — |

## Members

### `GPlatesPresenter::Presenter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Presenter()` | constructor | `None` | private | This is a Singleton so we need to hide the usual suspects. |
| `Presenter(const Presenter &)` | constructor | `None` | private | — |
| `operator=` | field | `Presenter` | private | — |
| `~Presenter()` | destructor | `None` | private | — |

## Free functions and macros

*None.*

## Notes

[[[PROSE notes unit=deprecated/presenter/Presenter tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/presenter/Presenter.h
python scripts/gpq.py def GPlatesPresenter::Presenter --body
python scripts/gpq.py uses Presenter --kind class
python scripts/gpq.py hier Presenter
```
