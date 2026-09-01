# SmartNodeLinkedListTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 127 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/SmartNodeLinkedListTest.h` | C++ | 64 |
| `src/unit-test/SmartNodeLinkedListTest.cc` | C++ | 234 |

## Overview

[[[PROSE overview unit=unit-test/SmartNodeLinkedListTest tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::A`](#anonymousa) | struct | — | — | 0 | — |
| [`GPlatesUnitTest::SmartNodeLinkedListTest`](#gplatesunittestsmartnodelinkedlisttest) | class | — | — | 0 | — |
| [`GPlatesUnitTest::SmartNodeLinkedListTestSuite`](#gplatesunittestsmartnodelinkedlisttestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | — |

## Members

### `(anonymous)::A`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `i` | field | `int` | public | — |
| `j` | field | `int` | public | — |

### `GPlatesUnitTest::SmartNodeLinkedListTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SmartNodeLinkedListTest()` | constructor | `None` | public | — |
| `test_increment_decrement_and_operator_arrow()` | method | `void` | public | — |
| `test_list_scoping()` | method | `void` | public | — |

### `GPlatesUnitTest::SmartNodeLinkedListTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SmartNodeLinkedListTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `add_node_3( GPlatesUtils::SmartNodeLinkedList<int> &list)` | function | `std::unique_ptr<GPlatesUtils::SmartNodeLinkedList<int>::Node>` | — |
| `add_node_2( GPlatesUtils::SmartNodeLinkedList<int> &list)` | function | `std::unique_ptr<GPlatesUtils::SmartNodeLinkedList<int>::Node>` | — |
| `invoke_add_node_2( GPlatesUtils::SmartNodeLinkedList<int> &list)` | function | `void` | — |
| `add_node_1( GPlatesUtils::SmartNodeLinkedList<int> &list)` | function | `void` | — |
| `GPLATES_UNIT_TEST_SMARTNODELINKEDLIST_TEST_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=unit-test/SmartNodeLinkedListTest tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/UtilsTestSuite](UtilsTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/SmartNodeLinkedListTest.h
python scripts/gpq.py def GPlatesUnitTest::SmartNodeLinkedListTest --body
python scripts/gpq.py uses SmartNodeLinkedListTest --kind class
python scripts/gpq.py hier SmartNodeLinkedListTest
```
