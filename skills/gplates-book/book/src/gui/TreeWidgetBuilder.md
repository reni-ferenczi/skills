# TreeWidgetBuilder

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 221 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/TreeWidgetBuilder.h` | C++ | 641 |
| `src/gui/TreeWidgetBuilder.cc` | C++ | 806 |

## Overview

`TreeWidgetBuilder` lets code assemble a `QTreeWidget` hierarchy — items,
children, per-item fields, and deferred callbacks — before any of it is
attached to a real `QTreeWidgetItem`/`QTreeWidget`. Callers build the tree
using opaque `item_handle_type` values (`create_item()`, `add_child()`,
`insert_child()`, `push_current_item()`/`pop_current_item()` for a
depth-first "current item" cursor) rather than touching `QTreeWidgetItem`
pointers directly, then call `update_qtree_widget_with_added_or_inserted_items()`
once to transfer the whole pending hierarchy onto the widget in one pass.

The class was originally written on the assumption that batching child
insertion was faster than adding items one at a time; that turned out not to
matter, but the class stayed useful for a different reason: some
`QTreeWidgetItem` calls, notably `setExpanded()`, silently do nothing until
the item is actually linked into a `QTreeWidget`. `add_function()` /
`add_function_to_current_item()` let a caller queue such a call
(`qtree_widget_item_function_type`, typically built with `boost::bind`) to run
only once the item has been transferred and is safe to call it on.

The free functions declared alongside the class (`add_top_level_item`,
`add_child_to_current_item`, `add_children`, `destroy_children`, etc.) are
convenience wrappers over the member functions for the common cases of
building simple name/value rows, and are what most call sites — the
feature-property and geometry table populators — actually use instead of the
class's own methods.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::TreeWidgetBuilder`](#gplatesguitreewidgetbuilder) | class | `boost::noncopyable` | — | 0 | Manages hierarchical building of a QTreeWidget. |

## Members

### `GPlatesGui::TreeWidgetBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `qtree_widget_item_function_type` | typedef | `boost::function<void (QTreeWidgetItem *, QTreeWidget *)>` | public | A generalised function to call that takes a 'QTreeWidgetItem \*' argument followed by a 'QTreeWidget \*' argument. |
| `item_handle_type` | typedef | `unsigned int` | public | Item handles are used to identify QTreeWidgetItem's. |
| `TreeWidgetBuilder( QTreeWidget *tree_widget)` | constructor | `None` | public | Constructor. |
| `reset()` | method | `void` | public | Resets internal state so can be used again from scratch. |
| `get_root_handle()` | method | `item_handle_type` | public | Returns the handle to the root of the widget tree. |
| `get_current_item_handle()` | method | `item_handle_type` | public | Returns current item's handle. |
| `get_qtree_widget_item( item_handle_type item_handle)` | method | `QTreeWidgetItem` | public | Returns the QTreeWidgetItem associated with item\_handle. |
| `create_item( const QStringList &fields = QStringList())` | method | `item_handle_type` | public | Creates a tree widget item and returns handle identifying it. |
| `destroy_item( item_handle_type)` | method | `void` | public | Destroys a tree widget item (and items in its child subtrees). |
| `get_num_children( item_handle_type parent_item_handle)` | method | `unsigned int` | public | Returns the number of children of the item parent\_item\_handle. parent\_item\_handle can be the root handle in which case it returns the number of top-level items. |
| `get_child_item_handle( item_handle_type parent_item_handle, const unsigned int child_index)` | method | `item_handle_type` | public | Returns the handle of child item of parent\_item\_handle at child index child\_index. |
| `add_child( const item_handle_type parent_item_handle, const item_handle_type child_item_handle)` | method | `void` | public | Adds a previously created child item to a previously created parent item. |
| `insert_child( const item_handle_type parent_item_handle, const item_handle_type child_item_handle, const unsigned int child_index)` | method | `void` | public | Inserts a previously created child item into the list of children of a previously created parent item at the child index child\_index. |
| `remove_child( const item_handle_type parent_item_handle, const item_handle_type child_item_handle)` | method | `void` | public | Removes a previously created child item from a previously created parent item. |
| `remove_child_at_index( const item_handle_type parent_item_handle, const unsigned int child_index)` | method | `void` | public | Removes a previously created child item from a previously created parent item. |
| `add_function( item_handle_type item_handle, const qtree_widget_item_function_type &function)` | method | `void` | public | Adds function to the item identified by item\_handle. |
| `push_current_item( item_handle_type item_handle)` | method | `void` | public | Changes the current item to refer to item\_handle. |
| `pop_current_item()` | method | `item_handle_type` | public | Pops the current item off the stack and restores previous current item. |
| `update_qtree_widget_with_added_or_inserted_items()` | method | `void` | public | Transfers all QTreeWidgetItems added or inserted since last call to update\_qtree\_widget\_with\_added\_or\_inserted\_items to the QTreeWidget passed in the constructor. |
| `item_handle_seq_type` | typedef | `std::vector<item_handle_type>` | private | A sequence of item handles. |
| `item_ptr_seq_type` | typedef | `std::vector<Item *>` | private | A sequence of item pointers (not memory-managed). |
| `managed_item_ptr_type` | typedef | `boost::shared_ptr<Item>` | private | A memory-managed pointer to Item. |
| `managed_item_ptr_seq_type` | typedef | `std::vector<managed_item_ptr_type>` | private | A sequence of memory-managed item pointers. |
| `item_function_seq_type` | typedef | `std::list<qtree_widget_item_function_type>` | private | A sequence of functions to call on a QTreeWidgetItem. |
| `ItemHandleManager` | class | `None` | private | Manages allocating/deallocating item handles. |
| `Item` | struct | `None` | private | Keeps track a tree widget item, its children, its functions and its parent. |
| `d_tree_widget` | field | `QTreeWidget` | private | — |
| `d_item_handle_manager` | field | `ItemHandleManager` | private | — |
| `d_current_item_handle` | field | `item_handle_type` | private | — |
| `d_root_handle` | field | `item_handle_type` | private | There is no actual root QTreeWidgetItem - this just helps identify top-level items. |
| `d_current_item_handle_stack` | field | `std::stack<item_handle_type>` | private | Keeps track of push\_current\_item and pop\_current\_item calls. |
| `d_items` | field | `managed_item_ptr_seq_type` | private | A sequence of all items created so far (memory-managed). |
| `have_current_item()` | method | `bool` | private | Returns true if we have a current item. |
| `get_current_item()` | method | `Item` | private | Returns current item (throws exception if have\_current\_item returns false). |
| `get_item( item_handle_type item_handle)` | method | `Item` | private | Returns item identified by item\_handle. |
| `allocate_item( managed_item_ptr_type new_item)` | method | `item_handle_type` | private | — |
| `deallocate_item( item_handle_type item_handle)` | method | `void` | private | — |
| `allocate_root_item()` | method | `void` | private | — |
| `destroy_item_without_removing_from_parent( item_handle_type item_handle)` | method | `void` | private | — |
| `remove_child( Item *parent_item, item_handle_type child_item_handle, unsigned int child_index)` | method | `void` | private | — |
| `visit_item_recursively( Item *item)` | method | `void` | private | — |
| `transfer_managed_tree_widget_items_to_qlist( const item_handle_seq_type &item_seq, QList<QTreeWidgetItem *> &transfer_list, int *insert_child_index)` | method | `bool` | private | — |
| `call_item_functions( Item *item)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_GUI_TREEWIDGETBUILDER_H` | macro | `None` | — |
| `get_current_qtree_widget_item( TreeWidgetBuilder &tree_widget_builder)` | function | `QTreeWidgetItem` | Returns the QTreeWidgetItem associated with the current item. |
| `add_top_level_item( TreeWidgetBuilder &tree_widget_builder, const QString &name, const QString &value = QString())` | function | `TreeWidgetBuilder::item_handle_type` | Creates top-level tree widget item. |
| `add_top_level_item( TreeWidgetBuilder &tree_widget_builder, const QStringList &fields = QStringList())` | function | `TreeWidgetBuilder::item_handle_type` | Creates top-level tree widget item. |
| `add_top_level_item( TreeWidgetBuilder &tree_widget_builder, TreeWidgetBuilder::item_handle_type top_level_item_handle)` | function | `void` | Adds top\_level\_item\_handle as top-level tree widget item. |
| `add_child_to_current_item( TreeWidgetBuilder &tree_widget_builder, const QString &name, const QString &value = QString())` | function | `TreeWidgetBuilder::item_handle_type` | Creates and adds a child tree widget item to the current item. |
| `add_child_to_current_item( TreeWidgetBuilder &tree_widget_builder, const QStringList &fields = QStringList())` | function | `TreeWidgetBuilder::item_handle_type` | Creates and adds a child tree widget item to the current item. |
| `add_child( TreeWidgetBuilder &tree_widget_builder, const TreeWidgetBuilder::item_handle_type parent_item_handle, const QString &name, const QString &value = QString())` | function | `TreeWidgetBuilder::item_handle_type` | Creates and adds a child tree widget item to parent\_item\_handle. |
| `add_child( TreeWidgetBuilder &tree_widget_builder, const TreeWidgetBuilder::item_handle_type parent_item_handle, const QStringList &fields = QStringList())` | function | `TreeWidgetBuilder::item_handle_type` | Creates and adds a child tree widget item to parent\_item\_handle. |
| `add_children( TreeWidgetBuilder &tree_widget_builder, const TreeWidgetBuilder::item_handle_type parent_item_handle, ItemHandleForwardIter begin_child_item_handles, ItemHandleForwardIter end_child_item_handles)` | function | `void` | Adds sequence of previously created children item handles to a previously created parent item. |
| `add_children_to_current_item( TreeWidgetBuilder &tree_widget_builder, ItemHandleForwardIter begin_child_item_handles, ItemHandleForwardIter end_child_item_handles)` | function | `void` | Adds sequence of previously created children item handles to the current item. |
| `add_top_level_items( TreeWidgetBuilder &tree_widget_builder, ItemHandleForwardIter begin_child_item_handles, ItemHandleForwardIter end_child_item_handles)` | function | `void` | Adds sequence of previously created children item handles as top-level items. |
| `insert_top_level_item( TreeWidgetBuilder &tree_widget_builder, TreeWidgetBuilder::item_handle_type top_level_item_handle, const unsigned int top_level_item_index)` | function | `void` | Inserts top\_level\_item\_handle as top-level tree widget item at index top\_level\_item\_index. |
| `destroy_children( TreeWidgetBuilder &tree_widget_builder, const TreeWidgetBuilder::item_handle_type parent_item_handle)` | function | `void` | Destroys children from parent\_item\_handle. |
| `destroy_top_level_items( TreeWidgetBuilder &tree_widget_builder)` | function | `void` | Destroys all top-level items. |
| `get_num_top_level_items( TreeWidgetBuilder &tree_widget_builder)` | function | `unsigned int` | Returns the number of top-level items. |
| `get_top_level_item_handle( TreeWidgetBuilder &tree_widget_builder, const unsigned int top_level_item_index)` | function | `TreeWidgetBuilder::item_handle_type` | Returns item handle of a top-level item. |
| `get_child_qtree_widget_item( TreeWidgetBuilder &tree_widget_builder, TreeWidgetBuilder::item_handle_type parent_item_handle, const unsigned int child_index)` | function | `QTreeWidgetItem` | Gets the QTreeWidgetItem of the child of parent\_item\_handle at index child\_index. |
| `add_function_to_current_item( TreeWidgetBuilder &tree_widget_builder, const TreeWidgetBuilder::qtree_widget_item_function_type &function)` | function | `void` | Adds function to the current item. |

## Notes

- `item_handle_type` values are recycled: `ItemHandleManager` hands out
  deallocated handles again on a later `create_item()`, so holding onto a
  handle after `destroy_item()` or `reset()` and using it later can silently
  address a different, unrelated item rather than fail.
- `get_root_handle()` is a bookkeeping value, not a real `QTreeWidgetItem` —
  top-level items attach directly to the `QTreeWidget`. Calling
  `add_function()` or `get_qtree_widget_item()` with it throws.
- Items and their functions are only actually attached to the `QTreeWidget`
  passed to the constructor when `update_qtree_widget_with_added_or_inserted_items()`
  is called; building the handle-based hierarchy has no visible effect on the
  widget until then.

## Used by

| Unit | Component | References |
|---|---|---|
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 108 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 90 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 71 |
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 2 |
| [qt-widgets/ModifyGeometryWidget](../qt-widgets/ModifyGeometryWidget.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/TreeWidgetBuilder.h
python scripts/gpq.py def GPlatesGui::TreeWidgetBuilder --body
python scripts/gpq.py uses TreeWidgetBuilder --kind class
python scripts/gpq.py hier TreeWidgetBuilder
```
