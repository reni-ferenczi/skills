# TopologyInternalUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1083 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/TopologyInternalUtils.h` | C++ | 335 |
| `src/app-logic/TopologyInternalUtils.cc` | C++ | 1360 |

## Overview

[[[PROSE overview unit=app-logic/TopologyInternalUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::TopologicalGeometryPropertyValue`](#anonymoustopologicalgeometrypropertyvalue) | class | [`GPlatesModel::FeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Returns the topological geometry property value (topological line, polygon or network) at the specified reconstruction time (only applies if property value is time-dependent). |
| [`(anonymous)::TopologicalGeometryPropertyValueType`](#anonymoustopologicalgeometrypropertyvaluetype) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Used to determine if a feature property is a topological geometry. |
| [`(anonymous)::CreateTopologicalSectionPropertyValue`](#anonymouscreatetopologicalsectionpropertyvalue) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Creates a GpmlTopologicalSection |
| [`(anonymous)::CreateTopologicalNetworkInterior`](#anonymouscreatetopologicalnetworkinterior) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Creates a GpmlTopologicalNetwork::Interior |
| [`(anonymous)::FindTopologicalSectionsReferenced`](#anonymousfindtopologicalsectionsreferenced) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Used to find feature IDs of all topological sections referenced by topological geometries/networks. |
| [`GPlatesAppLogic::TopologyInternalUtils::topological_geometry_property_value_type`](#gplatesapplogictopologyinternalutilstopological_geometry_property_value_type) | typedef | — | — | 0 | Topological geometry property value types (topological line, polygon and network). |

## Members

### `(anonymous)::TopologicalGeometryPropertyValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TopologicalGeometryPropertyValue( const double &reconstruction_time)` | constructor | `None` | public | — |
| `get_topological_geometry_property_value()` | method | `boost::optional<GPlatesAppLogic::TopologyInternalUtils::topological_geometry_property_value_type>` | public | — |
| `visit_gpml_constant_value( GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gpml_time_window( GPlatesPropertyValues::GpmlTimeWindow &gpml_time_window)` | method | `void` | public | — |
| `visit_gpml_topological_network( GPlatesPropertyValues::GpmlTopologicalNetwork &gpml_topological_network)` | method | `void` | public | — |
| `visit_gpml_topological_line( GPlatesPropertyValues::GpmlTopologicalLine &gpml_topological_line)` | method | `void` | public | — |
| `visit_gpml_topological_polygon( GPlatesPropertyValues::GpmlTopologicalPolygon &gpml_topological_polygon)` | method | `void` | public | — |
| `d_reconstruction_time` | field | `double` | private | — |
| `d_topological_geometry_property_value` | field | `boost::optional<GPlatesAppLogic::TopologyInternalUtils::topological_geometry_property_value_type>` | private | — |

### `(anonymous)::TopologicalGeometryPropertyValueType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_topological_geometry_property_value_type()` | method | `boost::optional<GPlatesPropertyValues::StructuralType>` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gpml_topological_network( const GPlatesPropertyValues::GpmlTopologicalNetwork &gpml_topological_network)` | method | `void` | public | — |
| `visit_gpml_topological_line( const GPlatesPropertyValues::GpmlTopologicalLine &gpml_topological_line)` | method | `void` | public | — |
| `visit_gpml_topological_polygon( const GPlatesPropertyValues::GpmlTopologicalPolygon &gpml_topological_polygon)` | method | `void` | public | — |
| `d_topological_geometry_property_value_type` | field | `boost::optional<GPlatesPropertyValues::StructuralType>` | private | — |

### `(anonymous)::CreateTopologicalSectionPropertyValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CreateTopologicalSectionPropertyValue()` | constructor | `None` | public | — |
| `create_gpml_topological_section( const GPlatesModel::FeatureHandle::iterator &geometry_property, bool reverse_order)` | method | `boost::optional<GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type>` | public | — |
| `d_geometry_property` | field | `GPlatesModel::FeatureHandle::iterator` | private | — |
| `d_reverse_order` | field | `bool` | private | — |
| `d_topological_section` | field | `boost::optional<GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type>` | private | — |
| `d_visited_topological_line` | field | `bool` | private | If GpmlTopologicalLine is in a piecewise aggregration then we only need to visit one time window. |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &/*gml_multi_point*/)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &/*gml_polygon*/)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | private | — |
| `visit_gpml_topological_line( const GPlatesPropertyValues::GpmlTopologicalLine &gpml_topological_line)` | method | `void` | private | — |
| `create_topological_point( const GPlatesPropertyValues::StructuralType &property_value_type)` | method | `void` | private | — |
| `create_topological_line_section( const GPlatesPropertyValues::StructuralType &property_value_type)` | method | `void` | private | — |

### `(anonymous)::CreateTopologicalNetworkInterior`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CreateTopologicalNetworkInterior()` | constructor | `None` | public | — |
| `create_gpml_topological_network_interior( const GPlatesModel::FeatureHandle::iterator &geometry_property)` | method | `boost::optional<GPlatesPropertyValues::GpmlPropertyDelegate::non_null_ptr_type>` | public | — |
| `d_geometry_property` | field | `GPlatesModel::FeatureHandle::iterator` | private | — |
| `d_topological_interior` | field | `boost::optional<GPlatesPropertyValues::GpmlPropertyDelegate::non_null_ptr_type>` | private | — |
| `d_visited_topological_line` | field | `bool` | private | If GpmlTopologicalLine is in a piecewise aggregration then we only need to visit one time window. |
| `visit_gml_line_string( const GPlatesPropertyValues::GmlLineString &gml_line_string)` | method | `void` | private | — |
| `visit_gml_multi_point( const GPlatesPropertyValues::GmlMultiPoint &gml_multi_point)` | method | `void` | private | — |
| `visit_gml_orientable_curve( const GPlatesPropertyValues::GmlOrientableCurve &gml_orientable_curve)` | method | `void` | private | — |
| `visit_gml_point( const GPlatesPropertyValues::GmlPoint &gml_point)` | method | `void` | private | — |
| `visit_gml_polygon( const GPlatesPropertyValues::GmlPolygon &/*gml_polygon*/)` | method | `void` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | private | — |
| `visit_gpml_topological_line( const GPlatesPropertyValues::GpmlTopologicalLine &gpml_topological_line)` | method | `void` | private | — |
| `create_topological_network_interior( const GPlatesPropertyValues::StructuralType &property_value_type)` | method | `void` | private | — |

### `(anonymous)::FindTopologicalSectionsReferenced`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FindTopologicalSectionsReferenced( std::set<GPlatesModel::FeatureId> &topological_sections_referenced, boost::optional<GPlatesAppLogic::TopologyGeometry::Type> topology_geometry_type = boost::none, boost::optional<double> reconstruction_time = boost::none)` | constructor | `None` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | public | — |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | public | — |
| `visit_gpml_topological_network( const GPlatesPropertyValues::GpmlTopologicalNetwork &gpml_topological_network)` | method | `void` | public | — |
| `visit_gpml_topological_line( const GPlatesPropertyValues::GpmlTopologicalLine &gpml_topological_line)` | method | `void` | public | — |
| `visit_gpml_topological_polygon( const GPlatesPropertyValues::GpmlTopologicalPolygon &gpml_topological_polygon)` | method | `void` | public | — |
| `visit_gpml_topological_line_section( const GPlatesPropertyValues::GpmlTopologicalLineSection &gpml_topological_line_section)` | method | `void` | public | — |
| `visit_gpml_topological_point( const GPlatesPropertyValues::GpmlTopologicalPoint &gpml_topological_point)` | method | `void` | public | — |
| `d_topological_sections_referenced` | field | `std::set<GPlatesModel::FeatureId>` | private | — |
| `d_topology_geometry_type` | field | `boost::optional<GPlatesAppLogic::TopologyGeometry::Type>` | private | — |
| `d_reconstruction_time` | field | `boost::optional<double>` | private | — |

### `GPlatesAppLogic::TopologyInternalUtils::topological_geometry_property_value_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `find_topological_section_reconstruction_geometry( const std::vector<GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_type> &found_rgs, const std::vector<GPlatesModel::FeatureHandle::weak_ref> &feature_refs, const GPlatesModel::PropertyName &property_name, const double &reconstruction_time)` | function | `boost::optional<GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_type>` | — |
| `GPLATES_APP_LOGIC_TOPOLOGYINTERNALUTILS_H` | macro | `None` | — |
| `get_topology_geometry_property_value( GPlatesModel::TopLevelProperty &property, const double &reconstruction_time = 0.0)` | function | `boost::optional<topological_geometry_property_value_type>` | Returns the topological geometry property value (topological line, polygon or network) at the specified reconstruction time (only applies if property value is time-dependent). |
| `get_topology_geometry_property_value( const GPlatesModel::FeatureHandle::iterator &property, const double &reconstruction_time = 0.0)` | function | `boost::optional<topological_geometry_property_value_type>` | — |
| `get_topology_geometry_property_value_type( const GPlatesModel::TopLevelProperty &property)` | function | `boost::optional<GPlatesPropertyValues::StructuralType>` | Determines the type of topological geometry property value. |
| `get_topology_geometry_property_value_type( const GPlatesModel::FeatureHandle::const_iterator &property)` | function | `boost::optional<GPlatesPropertyValues::StructuralType>` | — |
| `create_gpml_topological_section( const GPlatesModel::FeatureHandle::iterator &geometry_property, bool reverse_order = false)` | function | `boost::optional<GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type>` | Creates and returns a gpml topological section property value that references the geometry property geometry\_property. |
| `create_gpml_topological_network_interior( const GPlatesModel::FeatureHandle::iterator &geometry_property)` | function | `boost::optional<GPlatesPropertyValues::GpmlPropertyDelegate::non_null_ptr_type>` | Creates and returns a gpml topological network interior that references the geometry property geometry\_property. |
| `create_geometry_property_delegate( const GPlatesModel::FeatureHandle::iterator &geometry_property, const GPlatesPropertyValues::StructuralType &property_value_type)` | function | `boost::optional<GPlatesPropertyValues::GpmlPropertyDelegate::non_null_ptr_type>` | Create a geometry property delegate from a feature properties iterator and a property value type string (eg, "gml:LineString"). |
| `resolve_feature_id( const GPlatesModel::FeatureId &feature_id)` | function | `GPlatesModel::FeatureHandle::weak_ref` | Retrieves a FeatureHandle weak reference associated with feature\_id. |
| `find_topological_sections_referenced( std::set<GPlatesModel::FeatureId> &topological_sections_referenced, const GPlatesModel::FeatureHandle::weak_ref &topology_feature_ref, boost::optional<TopologyGeometry::Type> topology_geometry_type = boost::none, boost::optional<double> reconstruction_time = boost::none)` | function | `void` | Inserts all topological section features referenced by the topological feature topology\_feature\_ref (which can be a topological line, boundary or network). |
| `find_topological_sections_referenced( std::set<GPlatesModel::FeatureId> &topological_sections_referenced, const GPlatesModel::FeatureCollectionHandle::weak_ref &topology_feature_collection_ref, boost::optional<TopologyGeometry::Type> topology_geometry_type = boost::none, boost::optional<double> reconstruction_time = bo ...` | function | `void` | An overload of find\_topological\_sections\_referenced accepting a topological feature collection instead of a single topological feature. |
| `find_topological_sections_referenced( std::set<GPlatesModel::FeatureId> &topological_sections_referenced, const std::vector<GPlatesModel::FeatureHandle::weak_ref> &topology_features, boost::optional<TopologyGeometry::Type> topology_geometry_type = boost::none, boost::optional<double> reconstruction_time = boost::none)` | function | `void` | An overload of find\_topological\_sections\_referenced accepting a vector of topological features instead of a feature collection. |
| `find_topological_reconstruction_geometry( const GPlatesPropertyValues::GpmlPropertyDelegate &geometry_delegate, const double &reconstruction_time, boost::optional<const std::vector<ReconstructHandle::type> &> reconstruct_handles = boost::none)` | function | `boost::optional<ReconstructionGeometry::non_null_ptr_type>` | Finds the reconstruction geometry for the geometry property referenced by the property delegate geometry\_delegate. |
| `find_topological_reconstruction_geometry( const GPlatesModel::FeatureHandle::iterator &geometry_property, const double &reconstruction_time, boost::optional<const std::vector<ReconstructHandle::type> &> reconstruct_handles = boost::none)` | function | `boost::optional<ReconstructionGeometry::non_null_ptr_type>` | Finds the reconstruction geometry for the geometry properties iterator geometry\_property. |
| `can_use_as_resolved_line_topological_section( const ReconstructionGeometry::non_null_ptr_to_const_type &recon_geom)` | function | `bool` | Returns true if recon\_geom can be used as a topological section for a resolved line. |
| `can_use_as_resolved_boundary_topological_section( const ReconstructionGeometry::non_null_ptr_to_const_type &recon_geom)` | function | `bool` | Returns true if recon\_geom can be used as a topological section for a resolved boundary. |
| `can_use_as_resolved_network_topological_section( const ReconstructionGeometry::non_null_ptr_to_const_type &recon_geom)` | function | `bool` | Returns true if recon\_geom can be used as a topological section for a resolved network. |

## Notes

[[[PROSE notes unit=app-logic/TopologyInternalUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 17 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 11 |
| [canvas-tools/BuildTopology](../canvas-tools/BuildTopology.md) | canvas-tools | 7 |
| [canvas-tools/EditTopology](../canvas-tools/EditTopology.md) | canvas-tools | 7 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 5 |
| [app-logic/ApplicationState](ApplicationState.md) | app-logic | 3 |
| [app-logic/DependentTopologicalSectionLayers](DependentTopologicalSectionLayers.md) | app-logic | 3 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 3 |
| [app-logic/TopologyNetworkResolverLayerProxy](TopologyNetworkResolverLayerProxy.md) | app-logic | 3 |
| [gui/TopologySectionsContainer](../gui/TopologySectionsContainer.md) | gui | 3 |
| [qt-widgets/TopologyToolsWidget](../qt-widgets/TopologyToolsWidget.md) | qt-widgets | 3 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 2 |
| [canvas-tools/ClickGeometry](../canvas-tools/ClickGeometry.md) | canvas-tools | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [gui/TopologyCanvasToolWorkflow](../gui/TopologyCanvasToolWorkflow.md) | gui | 1 |
| [gui/TopologySectionsTableColumns](../gui/TopologySectionsTableColumns.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/TopologyInternalUtils.h
python scripts/gpq.py def (anonymous)::FindTopologicalSectionsReferenced --body
python scripts/gpq.py uses FindTopologicalSectionsReferenced --kind class
python scripts/gpq.py hier FindTopologicalSectionsReferenced
```
