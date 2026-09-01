# VisualLayerWidget

[Book TOC](../../TOC.md) · [qt-widgets](../../components/qt-widgets.md) · cluster Community 373 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/qt-widgets/VisualLayerWidget.h` | C++ | 469 |
| `src/qt-widgets/VisualLayerWidget.cc` | C++ | 1299 |
| `src/qt-widgets/VisualLayerWidgetUi.ui` | Qt form | 462 |

## Overview

[[[PROSE overview unit=qt-widgets/VisualLayerWidget tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::DisconnectInputConnectionLabel`](#anonymousdisconnectinputconnectionlabel) | class | `QLabel` | — | 0 | — |
| [`GPlatesQtWidgets::VisualLayerWidgetInternals::ToggleIcon`](#gplatesqtwidgetsvisuallayerwidgetinternalstoggleicon) | class | `QLabel` | — | 0 | ToggleIcon is an icon that has two states, on and off, and can display a different icon for each of these two states. |
| [`GPlatesQtWidgets::VisualLayerWidgetInternals::InputConnectionWidget`](#gplatesqtwidgetsvisuallayerwidgetinternalsinputconnectionwidget) | class | `QWidget` | — | 0 | Displays an existing input connection. |
| [`GPlatesQtWidgets::VisualLayerWidgetInternals::AddNewConnectionWidget`](#gplatesqtwidgetsvisuallayerwidgetinternalsaddnewconnectionwidget) | class | `QLabel` | — | 0 | A widget that allows the user to add new connections to a channel. |
| [`GPlatesQtWidgets::VisualLayerWidgetInternals::InputChannelWidget`](#gplatesqtwidgetsvisuallayerwidgetinternalsinputchannelwidget) | class | `QWidget` | — | 0 | Displays the input connections on a particular input channel, and allows the user to add or remove input connections. |
| [`GPlatesQtWidgets::VisualLayerWidget`](#gplatesqtwidgetsvisuallayerwidget) | class | `QWidget`<br>`Ui_VisualLayerWidget` | — | 0 | The VisualLayerWidget displays information about a single VisualLayer, and is contained within a VisualLayersWidget. |

## Members

### `(anonymous)::DisconnectInputConnectionLabel`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DisconnectInputConnectionLabel( GPlatesAppLogic::Layer::InputConnection &current_input_connection, QWidget *parent_)` | constructor | `None` | public | — |
| `mousePressEvent( QMouseEvent *event_)` | method | `void` | protected | — |
| `d_current_input_connection` | field | `GPlatesAppLogic::Layer::InputConnection` | private | — |

### `GPlatesQtWidgets::VisualLayerWidgetInternals::ToggleIcon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ToggleIcon( const QPixmap &on_icon, const QPixmap &off_icon, bool is_clickable = true, bool show_frame_when_clickable = true, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `show_icon( bool on = true)` | method | `void` | public | — |
| `set_clickable( bool is_clickable = true)` | method | `void` | public | — |
| `clicked()` | method | `void` | public | — |
| `mousePressEvent( QMouseEvent *event_)` | method | `void` | protected | — |
| `changeEvent( QEvent *event_)` | method | `void` | protected | — |
| `set_cursor()` | method | `void` | private | — |
| `d_on_icon` | field | `QPixmap` | private | — |
| `d_off_icon` | field | `QPixmap` | private | — |
| `d_is_clickable` | field | `bool` | private | — |
| `d_show_frame_when_clickable` | field | `bool` | private | — |

### `GPlatesQtWidgets::VisualLayerWidgetInternals::InputConnectionWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InputConnectionWidget( GPlatesGui::VisualLayersProxy &visual_layers, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_data( const GPlatesAppLogic::Layer::InputConnection &input_connection, const GPlatesGui::Colour &background_colour)` | method | `void` | public | Causes this widget to display the input\_connection. |
| `get_disconnect_pixmap` | field | `QPixmap` | private | — |
| `d_visual_layers` | field | `GPlatesGui::VisualLayersProxy` | private | — |
| `d_input_connection_label` | field | `ElidedLabel` | private | — |
| `d_disconnect_icon` | field | `QLabel` | private | — |
| `d_current_input_connection` | field | `GPlatesAppLogic::Layer::InputConnection` | private | — |

### `GPlatesQtWidgets::VisualLayerWidgetInternals::AddNewConnectionWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AddNewConnectionWidget( const QString &display_text, QMenu *menu, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_highlight_colour( const GPlatesGui::Colour &highlight_colour)` | method | `void` | public | — |
| `mousePressEvent( QMouseEvent *ev)` | method | `void` | protected | — |
| `enterEvent( QEvent *ev)` | method | `void` | protected | — |
| `leaveEvent( QEvent *ev)` | method | `void` | protected | — |
| `changeEvent( QEvent *ev)` | method | `void` | protected | — |
| `d_menu` | field | `QMenu` | private | — |
| `d_highlight_colour` | field | `GPlatesGui::Colour` | private | — |
| `d_menu_open` | field | `bool` | private | — |

### `GPlatesQtWidgets::VisualLayerWidgetInternals::InputChannelWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InputChannelWidget( GPlatesGui::VisualLayersProxy &visual_layers, GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_data( const GPlatesAppLogic::Layer &layer, const GPlatesAppLogic::LayerInputChannelType &layer_input_channel_type, const std::vector<GPlatesAppLogic::Layer::InputConnection> &input_connections, const GPlatesGui::Colour &light_layer_colour)` | method | `void` | public | Causes this widget to display the input\_connections for the input channel defined by layer\_input\_channel\_type. |
| `populate_with_feature_collections( const GPlatesAppLogic::Layer &layer, const GPlatesAppLogic::LayerInputChannelName::Type input_data_channel)` | method | `void` | private | — |
| `populate_with_layers( const GPlatesAppLogic::Layer &layer, const GPlatesAppLogic::LayerInputChannelName::Type input_data_channel, const std::vector<GPlatesAppLogic::LayerInputChannelType::InputLayerType> &input_layer_types)` | method | `void` | private | — |
| `d_visual_layers` | field | `GPlatesGui::VisualLayersProxy` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_input_channel_name_label` | field | `ElidedLabel` | private | — |
| `d_yet_another_container` | field | `QWidget` | private | — |
| `d_input_connection_widgets_container` | field | `QWidget` | private | — |
| `d_add_new_connection_menu` | field | `QMenu` | private | — |
| `d_add_new_connection_widget` | field | `AddNewConnectionWidget` | private | — |
| `d_input_connection_widgets_layout` | field | `QVBoxLayout` | private | A pointer to the layout of the Qt container that holds the widgets that display input connections. |
| `d_input_connection_widgets` | field | `std::vector<InputConnectionWidget *>` | private | A pool of InputConnectionWidgets that can be used to display information about the input connections for the current input channel. |

### `GPlatesQtWidgets::VisualLayerWidget`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `VisualLayerWidget( GPlatesGui::VisualLayersProxy &visual_layers, GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, ViewportWindow *viewport_window, QWidget *parent_ = NULL)` | constructor | `None` | public | — |
| `set_data( boost::weak_ptr<GPlatesPresentation::VisualLayer> visual_layer, int row)` | method | `void` | public | — |
| `mousePressEvent( QMouseEvent *event_)` | method | `void` | protected | — |
| `handle_expand_icon_clicked()` | method | `void` | private | — |
| `handle_visibility_icon_clicked()` | method | `void` | private | — |
| `handle_is_default_icon_clicked()` | method | `void` | private | — |
| `handle_expand_input_channels_icon_clicked()` | method | `void` | private | — |
| `handle_expand_layer_options_icon_clicked()` | method | `void` | private | — |
| `handle_expand_advanced_options_icon_clicked()` | method | `void` | private | — |
| `handle_enable_layer_link_activated()` | method | `void` | private | — |
| `handle_rename_layer_link_activated()` | method | `void` | private | — |
| `handle_delete_layer_link_activated()` | method | `void` | private | — |
| `make_signal_slot_connections()` | method | `void` | private | — |
| `set_input_channel_data( const GPlatesAppLogic::Layer &layer, const GPlatesGui::Colour &light_layer_colour)` | method | `void` | private | Called by refresh to set up the input channel widgets. |
| `d_visual_layers` | field | `GPlatesGui::VisualLayersProxy` | private | — |
| `d_application_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_viewport_window` | field | `ViewportWindow` | private | — |
| `d_visual_layer` | field | `boost::weak_ptr<GPlatesPresentation::VisualLayer>` | private | A weak pointer to the visual layer that we're currently displaying. |
| `d_row` | field | `int` | private | The index of the row that this widget is showing. |
| `d_left_widget` | field | `QWidget` | private | — |
| `d_expand_icon` | field | `VisualLayerWidgetInternals::ToggleIcon` | private | The main expand/collapse icon on the left. |
| `d_visibility_icon` | field | `VisualLayerWidgetInternals::ToggleIcon` | private | The hide/show icon on the top. |
| `d_is_default_icon` | field | `VisualLayerWidgetInternals::ToggleIcon` | private | The icon that shows whether the current layer is the default reconstruction tree. |
| `d_expand_input_channels_icon` | field | `VisualLayerWidgetInternals::ToggleIcon` | private | The icon that allows the user to expand/collapse the input channels section. |
| `d_expand_layer_options_icon` | field | `VisualLayerWidgetInternals::ToggleIcon` | private | The icon that allows the user to expand/collapse the layer options section. |
| `d_expand_advanced_options_icon` | field | `VisualLayerWidgetInternals::ToggleIcon` | private | The icon that allows the user to expand/collapse the advanced options section. |
| `d_visibility_default_stackedwidget` | field | `QStackedWidget` | private | The d\_visibility\_icon (page 0) and d\_is\_default\_icon (page 1) are placed inside this; they occupy the same position on screen and this is used to switch between them. |
| `d_name_label` | field | `ElidedLabel` | private | The label showing the name of the layer in bold. |
| `d_type_label` | field | `ElidedLabel` | private | The label showing the type of the layer. |
| `d_input_channels_widget_layout` | field | `QVBoxLayout` | private | The layout of the input\_channels\_widget. |
| `d_input_channel_widgets` | field | `std::vector<VisualLayerWidgetInternals::InputChannelWidget *>` | private | A pool of InputChannelWidgets that can be used to display information about the input channels for the current visual layer. |
| `d_current_layer_options_widget` | field | `LayerOptionsWidget` | private | — |
| `d_layer_options_widget_layout` | field | `QVBoxLayout` | private | — |
| `d_enable_layer_link` | field | `LinkWidget` | private | Shows the "Disable layer" or "Enable layer" link as appropriate. |
| `d_rename_layer_link` | field | `LinkWidget` | private | Shows the "Rename layer" link. |
| `d_delete_layer_link` | field | `LinkWidget` | private | Shows the "Delete layer" link. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NEW_FEATURE_COLLECTION` | variable | `char` | — |
| `SCROLL_BAR_ADJUSTMENT` | variable | `int` | This is the track thickness for scroll bars (regular size). |
| `lighten( const GPlatesGui::Colour &colour)` | function | `GPlatesGui::Colour` | — |
| `darken( const GPlatesGui::Colour &colour)` | function | `GPlatesGui::Colour` | — |
| `move_main_input_channel_to_front( InputChannelContainerType &input_channels, GPlatesAppLogic::LayerInputChannelName::Type main_input_channel)` | function | `void` | — |
| `GPLATES_QTWIDGETS_VISUALLAYERWIDGET_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=qt-widgets/VisualLayerWidget tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/VisualLayersDelegate](VisualLayersDelegate.md) | qt-widgets | 19 |

## Related

**Qt Designer forms**

| Form class | Base widget | Title | Widgets |
|---|---|---|---|
| `VisualLayerWidget` | `QWidget` | Layer | 26 |

**Qt signal/slot connections** (9 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `d_expand_icon` | `clicked()` | `this` | `handle_expand_icon_clicked()` |
| `d_visibility_icon` | `clicked()` | `this` | `handle_visibility_icon_clicked()` |
| `d_is_default_icon` | `clicked()` | `this` | `handle_is_default_icon_clicked()` |
| `d_expand_input_channels_icon` | `clicked()` | `this` | `handle_expand_input_channels_icon_clicked()` |
| `d_expand_layer_options_icon` | `clicked()` | `this` | `handle_expand_layer_options_icon_clicked()` |
| `d_expand_advanced_options_icon` | `clicked()` | `this` | `handle_expand_advanced_options_icon_clicked()` |
| `d_enable_layer_link` | `link_activated()` | `this` | `handle_enable_layer_link_activated()` |
| `d_rename_layer_link` | `link_activated()` | `this` | `handle_rename_layer_link_activated()` |
| `d_delete_layer_link` | `link_activated()` | `this` | `handle_delete_layer_link_activated()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/qt-widgets/VisualLayerWidget.h
python scripts/gpq.py def GPlatesQtWidgets::VisualLayerWidget --body
python scripts/gpq.py uses VisualLayerWidget --kind class
python scripts/gpq.py hier VisualLayerWidget
```
