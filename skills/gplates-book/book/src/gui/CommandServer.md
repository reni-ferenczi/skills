# CommandServer

[Book TOC](../../TOC.md) · [gui](../../components/gui.md) · cluster Community 420 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/gui/CommandServer.h` | C++ | 359 |
| `src/gui/CommandServer.cc` | C++ | 679 |

## Overview

[[[PROSE overview unit=gui/CommandServer tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesGui::Command`](#gplatesguicommand) | class | — | — | 7 | — |
| [`GPlatesGui::GetSeedsCommand`](#gplatesguigetseedscommand) | class | [`Command`](CommandServer.md) | — | 0 | — |
| [`GPlatesGui::GetTimeSettingCommand`](#gplatesguigettimesettingcommand) | class | [`Command`](CommandServer.md) | — | 0 | — |
| [`GPlatesGui::GetBeginTimeCommand`](#gplatesguigetbegintimecommand) | class | [`Command`](CommandServer.md) | — | 0 | — |
| [`GPlatesGui::GetAssociationsCommand`](#gplatesguigetassociationscommand) | class | [`Command`](CommandServer.md) | — | 0 | — |
| [`GPlatesGui::GetAssociationDataCommand`](#gplatesguigetassociationdatacommand) | class | [`Command`](CommandServer.md) | — | 0 | — |
| [`GPlatesGui::GetBirthAttributeCommand`](#gplatesguigetbirthattributecommand) | class | [`Command`](CommandServer.md) | — | 0 | — |
| [`GPlatesGui::SetReconstructionTimeCommand`](#gplatesguisetreconstructiontimecommand) | class | [`Command`](CommandServer.md) | — | 0 | — |
| [`GPlatesGui::CommandServer`](#gplatesguicommandserver) | class | `QTcpServer` | — | 0 | — |

## Members

### `GPlatesGui::Command`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `execute( QTcpSocket*)` | method | `bool` | public | — |
| `~Command()` | destructor | `None` | public | — |

### `GPlatesGui::GetSeedsCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetSeedsCommand( GPlatesPresentation::ViewState &view_state, const QString& layer_name)` | constructor | `None` | public | — |
| `execute( QTcpSocket* socket)` | method | `bool` | public | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_layer_name` | field | `QString` | private | — |

### `GPlatesGui::GetTimeSettingCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetTimeSettingCommand( GPlatesPresentation::ViewState &view_state)` | constructor | `None` | public | — |
| `execute( QTcpSocket* socket)` | method | `bool` | public | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |

### `GPlatesGui::GetBeginTimeCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetBeginTimeCommand( const QString feature_id)` | constructor | `None` | public | — |
| `execute( QTcpSocket* socket)` | method | `bool` | public | — |
| `d_feature_id` | field | `QString` | private | — |

### `GPlatesGui::GetAssociationsCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetAssociationsCommand( GPlatesPresentation::ViewState &view_state, const QString& layer_name)` | constructor | `None` | public | — |
| `execute( QTcpSocket* socket)` | method | `bool` | public | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_layer_name` | field | `QString` | private | — |

### `GPlatesGui::GetAssociationDataCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetAssociationDataCommand( GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &main_window, double time, const QString& layer_name, bool is_invalid = false)` | constructor | `None` | public | — |
| `execute( QTcpSocket* socket)` | method | `bool` | public | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_main_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | — |
| `d_time` | field | `double` | private | — |
| `d_layer_name` | field | `QString` | private | — |
| `d_invalid_time` | field | `bool` | private | — |

### `GPlatesGui::GetBirthAttributeCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetBirthAttributeCommand( GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &main_window, const QString& feature_id, const QString& layer_name)` | constructor | `None` | public | — |
| `execute( QTcpSocket* socket)` | method | `bool` | public | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_main_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | — |
| `d_feature_id` | field | `QString` | private | — |
| `d_layer_name` | field | `QString` | private | — |

### `GPlatesGui::SetReconstructionTimeCommand`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SetReconstructionTimeCommand( GPlatesPresentation::ViewState &view_state, double time)` | constructor | `None` | public | — |
| `execute( QTcpSocket* socket)` | method | `bool` | public | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_time` | field | `double` | private | — |

### `GPlatesGui::CommandServer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CommandServer( GPlatesAppLogic::ApplicationState &application_state, GPlatesPresentation::ViewState &view_state, GPlatesQtWidgets::ViewportWindow &main_window, unsigned port = 0, QObject* _parent = 0)` | constructor | `None` | public | — |
| `incomingConnection( qintptr socket)` | method | `void` | public | — |
| `pause()` | method | `void` | public | — |
| `resume()` | method | `void` | public | — |
| `create_get_seeds_command( QXmlStreamReader& reader)` | method | `boost::shared_ptr<Command>` | protected | The following group of functions create Command objects for CommandServer. |
| `create_get_time_setting_command( QXmlStreamReader& reader)` | method | `boost::shared_ptr<Command>` | protected | — |
| `create_get_begin_time_command( QXmlStreamReader& reader)` | method | `boost::shared_ptr<Command>` | protected | — |
| `create_get_associations_command( QXmlStreamReader& reader)` | method | `boost::shared_ptr<Command>` | protected | — |
| `create_get_association_data_command( QXmlStreamReader& reader)` | method | `boost::shared_ptr<Command>` | protected | — |
| `create_get_birth_attribute_command( QXmlStreamReader& reader)` | method | `boost::shared_ptr<Command>` | protected | — |
| `create_set_reconstruction_time_command( QXmlStreamReader& reader)` | method | `boost::shared_ptr<Command>` | protected | — |
| `readClient()` | method | `void` | private | — |
| `discardClient()` | method | `void` | private | — |
| `timeout()` | method | `void` | private | — |
| `create_command( const QString& request)` | method | `boost::shared_ptr<Command>` | private | — |
| `CommandServer(const CommandServer&)` | constructor | `None` | private | — |
| `operator=` | field | `CommandServer` | private | — |
| `d_disabled` | field | `bool` | private | — |
| `d_command_map` | field | `std::map<QString, CreateFun>` | private | — |
| `d_command` | field | `QString` | private | — |
| `d_timeout` | field | `bool` | private | — |
| `d_timer` | field | `QTimer` | private | — |
| `d_app_state` | field | `GPlatesAppLogic::ApplicationState` | private | — |
| `d_view_state` | field | `GPlatesPresentation::ViewState` | private | — |
| `d_main_window` | field | `GPlatesQtWidgets::ViewportWindow` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `readNextStartElement( QXmlStreamReader& reader)` | function | `bool` | — |
| `get_coregistration_layer_proxy( GPlatesPresentation::ViewState &view_state, const QString &layer_name)` | function | `boost::optional<GPlatesAppLogic::CoRegistrationLayerProxy::non_null_ptr_type>` | — |
| `GPLATES_GUI_COMMANDSERVER_H` | macro | `None` | — |
| `escape_reserved_xml_characters( const QString str)` | function | `QString` | — |
| `read_next_element_txt( QXmlStreamReader& reader, const QString& name="")` | function | `QString` | — |

## Notes

[[[PROSE notes unit=gui/CommandServer tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [presentation/Application](../presentation/Application.md) | presentation | 20 |
| [gui/FeatureFocus](FeatureFocus.md) | gui | 12 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 4 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 4 |
| [gui/GPlatesQApplication](GPlatesQApplication.md) | gui | 1 |
| [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](../qt-widgets/TopologyGeometryResolverLayerOptionsWidget.md) | qt-widgets | 1 |
| [qt-widgets/ViewportWindow](../qt-widgets/ViewportWindow.md) | qt-widgets | 1 |

## Related

**Qt signal/slot connections** (3 in this unit)

| Sender | Signal | Receiver | Slot |
|---|---|---|---|
| `s` | `readyRead()` | `this` | `readClient()` |
| `s` | `disconnected()` | `this` | `discardClient()` |
| `d_timer` | `timeout()` | `this` | `timeout()` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gui/CommandServer.h
python scripts/gpq.py def GPlatesGui::CommandServer --body
python scripts/gpq.py uses CommandServer --kind class
python scripts/gpq.py hier CommandServer
```
