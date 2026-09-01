# SearchResultsDockWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 470 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/SearchResultsDockWidget.h` | C++ | 125 |
| `src/qt-widgets/SearchResultsDockWidget.cc` | C++ | 195 |
| `src/qt-widgets/SearchResultsDockWidgetUi.ui` | Qt form | 128 |

## Overview

[[[PROSE overview unit=qt-widgets/SearchResultsDockWidget tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesQtWidgets::SearchResultsDockWidget`](#gplatesqtwidgetssearchresultsdockwidget) | class | [`DockWidget`](DockWidget.md)<br>`Ui_SearchResultsDockWidget` | — | 0 | A tabbed widget for displaying search results such as clicked features or topology sections. |

## Members

### `GPlatesQtWidgets::SearchResultsDockWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SearchResultsDockWidget( GPlatesGui::DockState &dock_state, GPlatesGui::FeatureTableModel &feature_table_model, ViewportWindow &main_window)` | constructor | `None` | public | — |
| `~SearchResultsDockWidget()` | destructor | `None` | public | — |
| `highlight_focused_feature_in_table( GPlatesGui::FeatureFocus &feature_focus)` | method | `void` | public | Highlights the row of the 'clicked geometry' feature table that corresponds to the focused feature. |
| `highlight_first_clicked_feature_table_row()` | method | `void` | public | Highlights the first row in the "clicked geometry" feature table. |
| `choose_clicked_geometry_table()` | method | `void` | public | — |
| `choose_topology_sections_table()` | method | `void` | public | — |
| `set_clicked_geometry_table_tab_text( const QString &text)` | method | `void` | public | — |
| `set_topology_sections_table_tab_text( const QString &text)` | method | `void` | public | — |
| `set_up_clicked_geometries_table()` | method | `void` | private | — |
| `set_up_topology_sections_table( ViewportWindow &main_window)` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_clicked_feature_table_model` | field | `GPlatesGui::FeatureTableModel` | private | — |
| `d_topology_sections_table` | field | `boost::scoped_ptr<GPlatesGui::TopologySectionsTable>` | private | Manages the 'Topology Sections' table widget. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_QT_WIDGETS_SEARCHRESULTSDOCKWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/SearchResultsDockWidget tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 7 |
| [gui/AddClickedGeometriesToFeatureTable](../gui/AddClickedGeometriesToFeatureTable.md) | gui | 3 |
| [qt-widgets/ViewportWindow](ViewportWindow.md) | qt-widgets | 3 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 2 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 2 |
| [presentation/Application](../presentation/Application.md) | presentation | 1 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `SearchResultsDockWidget` | `QDockWidget` | — | 7 |

**Qt signal/slot connections** (1 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `tree_view_clicked_geometries->selectionModel()` | `selectionChanged(const QItemSelection &, const QItemSelection &)` | `&d_clicked_feature_table_model` | `handle_selection_change(const QItemSelection &, const QItemSelection &)` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/SearchResultsDockWidget.h
python scripts/gpq.py def GPlatesQtWidgets::SearchResultsDockWidget --body
python scripts/gpq.py uses SearchResultsDockWidget --kind class
python scripts/gpq.py hier SearchResultsDockWidget
```
