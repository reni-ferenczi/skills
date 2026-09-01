# TopologySectionsContainer

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 137 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/TopologySectionsContainer.h` | C++ | 630 |
| `src/gui/TopologySectionsContainer.cc` | C++ | 261 |

## Overview

[[[PROSE overview unit=gui/TopologySectionsContainer tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::TopologySectionsContainer`](#gplatesguitopologysectionscontainer) | class | `QObject` | — | 0 | Class to manage the back-end data containing topology sections (and useful metadata) while a topology is being built up by the topology tools. |

## Members

### `GPlatesGui::TopologySectionsContainer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TableRow` | class | `None` | public | A struct holding the internal data that will be tracked per row of data in the table (not counting the 'insertion point' special row). |
| `container_type` | typedef | `std::vector<TableRow>` | public | — |
| `size_type` | typedef | `container_type::size_type` | public | — |
| `iterator` | typedef | `container_type::iterator` | public | — |
| `const_iterator` | typedef | `container_type::const_iterator` | public | — |
| `TopologySectionsContainer()` | constructor | `None` | public | — |
| `~TopologySectionsContainer()` | destructor | `None` | public | — |
| `update_table_from_container()` | method | `void` | public | update the table from the container |
| `size()` | method | `size_type` | public | Returns the number of topology sections in the container. |
| `size(int i)` | method | `size_type` | public | — |
| `begin()` | method | `const_iterator` | public | Const 'begin' iterator of the underlying vector. |
| `end()` | method | `const_iterator` | public | Const 'end' iterator of the underlying vector. |
| `at` | field | `TableRow` | public | Accesses an entry of the table by index. |
| `insert( const TableRow &entry)` | method | `void` | public | Inserts a new entry into the container. |
| `insert( I begin_it, I end_it)` | method | `void` | public | Inserts a bunch of new entries into the container. |
| `initialise( int seq_num, ITR begin_it, ITR end_it)` | method | `void` | public | — |
| `update_at( const size_type index, const TableRow &entry)` | method | `void` | public | Updates an existing TableRow in the collection. |
| `remove_at( const size_type index)` | method | `void` | public | Removes an existing TableRow in the collection. |
| `insertion_point()` | method | `size_type` | public | Returns the current index associated with the Insertion Point. |
| `move_insertion_point( size_type new_index)` | method | `void` | public | Moves the Insertion Point to a new row of the table. |
| `set_focus_feature_at_index( size_type index )` | method | `void` | public | The focus\_feature\_at\_index(int) signal is emitted. |
| `set_container_ptr_in_table( GPlatesGui::TopologySectionsContainer *ptr)` | method | `void` | public | The container\_change(GPlatesGui::TopologySectionsContainer \*) signal is emitted. |
| `reset_insertion_point()` | method | `void` | public | Moves the Insertion Point to the end of the table. |
| `clear()` | method | `void` | public | Clears the container of data and resets the insertion point. |
| `insert_test_data()` | method | `void` | public | they should go away once everything works fine. |
| `move_insertion_point_idx_4()` | method | `void` | public | TESTING: manipulate the Insertion Point. |
| `remove_idx_2()` | method | `void` | public | TESTING: remove some data. |
| `do_update()` | method | `void` | public | emmited when table is updated |
| `cleared()` | method | `void` | public | Emitted when clear() is called and all data has been removed. |
| `insertion_point_moved( GPlatesGui::TopologySectionsContainer::size_type new_index)` | method | `void` | public | Emitted whenever the insertion point changes location. |
| `entry_removed( GPlatesGui::TopologySectionsContainer::size_type deleted_index)` | method | `void` | public | Emitted whenever a entry has been deleted from the container. |
| `entries_initialised( int i, GPlatesGui::TopologySectionsContainer::size_type inserted_index, GPlatesGui::TopologySectionsContainer::size_type quantity, GPlatesGui::TopologySectionsContainer::const_iterator inserted_begin, GPlatesGui::TopologySectionsContainer::const_iterator inserted_end)` | method | `void` | public | Emitted whenever the TopologySectionsContainer is initialized with a sequence of sections |
| `entries_inserted( GPlatesGui::TopologySectionsContainer::size_type inserted_index, GPlatesGui::TopologySectionsContainer::size_type quantity, GPlatesGui::TopologySectionsContainer::const_iterator inserted_begin, GPlatesGui::TopologySectionsContainer::const_iterator inserted_end)` | method | `void` | public | Emitted whenever a number of entries have been inserted into the container. |
| `entry_modified( GPlatesGui::TopologySectionsContainer::size_type modified_index)` | method | `void` | public | Emitted whenever the data in an entry has been modified. |
| `focus_feature_at_index( GPlatesGui::TopologySectionsContainer::size_type index)` | method | `void` | public | Emitted whenever a feature is focused |
| `container_change( GPlatesGui::TopologySectionsContainer *)` | method | `void` | public | Emitted whenever the container changes FIXME: Ugh, what is this ? |
| `container_changed( GPlatesGui::TopologySectionsContainer &topology_sections_container)` | method | `void` | public | Emitted whenever any state of this container has changed. |
| `d_container` | field | `container_type` | private | The vector of TableRow holding the data to be displayed. |
| `d_insertion_point` | field | `TopologySectionsContainer::size_type` | private | The index that new data entries will be inserted into. |
| `d_insertion_points` | field | `std::vector<TopologySectionsContainer::size_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `find_properties_iterator( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::PropertyName &property_name)` | function | `GPlatesModel::FeatureHandle::iterator` | "Resolves" the target of a PropertyDelegate to a FeatureHandle::properties\_iterator. |
| `GPLATES_GUI_TOPOLOGYSECTIONSCONTAINER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=gui/TopologySectionsContainer tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologySectionsTableColumns](TopologySectionsTableColumns.md) | gui | 107 |
| [gui/TopologyTools](TopologyTools.md) | gui | 80 |
| [gui/TopologySectionsTable](TopologySectionsTable.md) | gui | 72 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 30 |
| [api/PyTopologyTools](../api/PyTopologyTools.md) | api | 7 |
| [presentation/ViewState](../presentation/ViewState.md) | presentation | 7 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 2 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 2 |
| [qt-widgets/TopologyToolsWidget](../qt-widgets/TopologyToolsWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/TopologySectionsContainer.h
python scripts/gpq.py def GPlatesGui::TopologySectionsContainer --body
python scripts/gpq.py uses TopologySectionsContainer --kind class
python scripts/gpq.py hier TopologySectionsContainer
```
