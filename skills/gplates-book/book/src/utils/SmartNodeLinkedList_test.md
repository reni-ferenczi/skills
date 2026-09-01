# SmartNodeLinkedList_test

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 127 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/SmartNodeLinkedList_test.cc` | C++ | 203 |

## Overview

[[[PROSE overview unit=utils/SmartNodeLinkedList_test tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`A`](#a) | struct | — | — | 0 | — |

## Members

### `A`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `i` | field | `int` | public | — |
| `j` | field | `int` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `print_list( GPlatesUtils::SmartNodeLinkedList<T> &list)` | function | `void` | — |
| `add_node_3( GPlatesUtils::SmartNodeLinkedList<int> &list)` | function | `std::auto_ptr<GPlatesUtils::SmartNodeLinkedList<int>::Node>` | — |
| `add_node_2( GPlatesUtils::SmartNodeLinkedList<int> &list)` | function | `std::auto_ptr<GPlatesUtils::SmartNodeLinkedList<int>::Node>` | — |
| `invoke_add_node_2( GPlatesUtils::SmartNodeLinkedList<int> &list)` | function | `void` | — |
| `add_node_1( GPlatesUtils::SmartNodeLinkedList<int> &list)` | function | `void` | — |
| `test_list_scoping()` | function | `void` | — |
| `test_increment_decrement_and_operator_arrow()` | function | `void` | — |
| `main()` | function | `int` | — |

## Notes

[[[PROSE notes unit=utils/SmartNodeLinkedList_test tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/SmartNodeLinkedList_test.cc
python scripts/gpq.py def A --body
python scripts/gpq.py uses A --kind struct
python scripts/gpq.py hier A
```
