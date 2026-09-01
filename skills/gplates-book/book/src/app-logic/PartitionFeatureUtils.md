# PartitionFeatureUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 355 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/PartitionFeatureUtils.h` | C++ | 585 |
| `src/app-logic/PartitionFeatureUtils.cc` | C++ | 1491 |

## Overview

[[[PROSE overview unit=app-logic/PartitionFeatureUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::PartitionFeatureUtils::(anonymous)::PartitionFeatureGeometryProperties`](#gplatesapplogicpartitionfeatureutilsanonymouspartitionfeaturegeometryproperties) | class | [`GPlatesModel::FeatureVisitorThatGuaranteesNotToModify`](../model/FeatureVisitor.md) | — | 0 | Visit a feature property and, if it contains geometry, partitions it using partitioning polygons and stores results for later retrieval. |
| [`GPlatesAppLogic::PartitionFeatureUtils::(anonymous)::GeometrySize`](#gplatesapplogicpartitionfeatureutilsanonymousgeometrysize) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | — |
| [`GPlatesAppLogic::PartitionFeatureUtils::geometry_domain_type`](#gplatesapplogicpartitionfeatureutilsgeometry_domain_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::PartitionFeatureUtils::geometry_range_type`](#gplatesapplogicpartitionfeatureutilsgeometry_range_type) | typedef | — | — | 0 | — |
| [`GPlatesAppLogic::PartitionFeatureUtils::PartitionedFeature`](#gplatesapplogicpartitionfeatureutilspartitionedfeature) | class | — | — | 0 | The results of partitioning the geometry properties of a feature. |
| [`GPlatesAppLogic::PartitionFeatureUtils::PropertyValueAssigner`](#gplatesapplogicpartitionfeatureutilspropertyvalueassigner) | class | — | — | 1 | Abstract base class for copying property values from a partitioning polygon feature to a partitioned feature. |
| [`GPlatesAppLogic::PartitionFeatureUtils::GenericFeaturePropertyAssigner`](#gplatesapplogicpartitionfeatureutilsgenericfeaturepropertyassigner) | class | [`PropertyValueAssigner`](PartitionFeatureUtils.md) | — | 0 | Optionally assigns various feature property types such as reconstruction plate ids and time periods. |
| [`GPlatesAppLogic::PartitionFeatureUtils::PartitionedFeatureManager`](#gplatesapplogicpartitionfeatureutilspartitionedfeaturemanager) | class | — | — | 0 | Manages creation/cloning of features for partitioned geometries. |
| [`GPlatesAppLogic::PartitionFeatureUtils::GeometrySizeMetric`](#gplatesapplogicpartitionfeatureutilsgeometrysizemetric) | class | `boost::less_than_comparable<GeometrySizeMetric>` | — | 0 | Visits a GeometryOnSphere and accumulates a size metric for it; for points/multipoints this is number of points and for polylines/polygons this is arc distance. |

## Members

### `GPlatesAppLogic::PartitionFeatureUtils::(anonymous)::PartitionFeatureGeometryProperties`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PartitionFeatureGeometryProperties( const GeometryCookieCutter &geometry_cookie_cutter, const std::vector<ScalarCoverageFeatureProperties::Coverage> &geometry_coverages, boost::optional< std::vector<GPlatesModel::FeatureHandle::iterator> &> partitioned_properties)` | constructor | `None` | public | — |
| `get_partitioned_feature_geometries()` | method | `boost::shared_ptr<const PartitionedFeature>` | public | — |
| `visit_gml_line_string( gml_line_string_type &gml_line_string)` | method | `void` | protected | — |
| `visit_gml_multi_point( gml_multi_point_type &gml_multi_point)` | method | `void` | protected | — |
| `visit_gml_orientable_curve( gml_orientable_curve_type &gml_orientable_curve)` | method | `void` | protected | — |
| `visit_gml_point( gml_point_type &gml_point)` | method | `void` | protected | — |
| `visit_gml_polygon( gml_polygon_type &gml_polygon)` | method | `void` | protected | — |
| `visit_gpml_constant_value( gpml_constant_value_type &gpml_constant_value)` | method | `void` | protected | — |
| `d_cookie_cut_geometry` | field | `GeometryCookieCutter` | private | Does the cookie-cutting. |
| `d_geometry_coverages` | field | `std::vector<ScalarCoverageFeatureProperties::Coverage>` | private | Scalar coverages associated with geometry properties. |
| `d_partitioned_properties` | field | `boost::optional< std::vector<GPlatesModel::FeatureHandle::iterator> &>` | private | Optional sequence of partitioned properties (geometry domains and associated ranges) to return to caller. |
| `d_partition_results` | field | `boost::shared_ptr<PartitionedFeature>` | private | The results of the cookie-cutting. |
| `POLY_GEOMETRY_DISTANCE_THRESHOLD` | field | `GPlatesMaths::AngularExtent` | private | Distance threshold used when determining interpolated scalar values for points in partitioned geometries that don't correspond to any point in original geometry. |
| `domain_to_range_map_type` | typedef | `std::map< GPlatesMaths::PointOnSphere, unsigned int/*point index*/, GPlatesMaths::PointOnSphereMapPredicate>` | private | Typedef for mapping points in the geometry domain to indices into geometry domain/range. |
| `Range` | struct | `None` | private | Contains the geometry range and information to map the associated domain to this range. |
| `add_geometry( const geometry_domain_type &geometry_domain)` | method | `void` | private | Partition the geometry geometry of the current geometry property. |
| `partition_geometry( const geometry_domain_type &geometry_domain, const boost::optional<Range> &geometry_range, PartitionedFeature::GeometryProperty &partitioned_geometry_property)` | method | `void` | private | — |
| `partition_geometries( const geometry_domain_type &geometry_domain, const boost::optional<Range> &geometry_range, const GeometryCookieCutter::partitioned_geometry_seq_type &partitioned_domains, PartitionedFeature::partitioned_geometry_seq_type &partitioned_geometries)` | method | `void` | private | — |
| `partition_range( geometry_range_type &partitioned_range, const geometry_domain_type &partitioned_domain, const Range &geometry_range, const geometry_domain_type &geometry_domain)` | method | `void` | private | — |

### `GPlatesAppLogic::PartitionFeatureUtils::(anonymous)::GeometrySize`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometrySize( unsigned int &num_points, GPlatesMaths::real_t &arc_distance, bool &using_arc_distance)` | constructor | `None` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type /*point_on_sphere*/)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `d_num_points` | field | `unsigned int` | public | — |
| `d_arc_distance` | field | `GPlatesMaths::real_t` | public | — |
| `d_using_arc_distance` | field | `bool` | public | — |

### `GPlatesAppLogic::PartitionFeatureUtils::geometry_domain_type`

*None.*

### `GPlatesAppLogic::PartitionFeatureUtils::geometry_range_type`

*None.*

### `GPlatesAppLogic::PartitionFeatureUtils::PartitionedFeature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PartitionedGeometry` | class | `None` | public | A partitioned geometry and optional associated partitioned scalar coverage. |
| `partitioned_geometry_seq_type` | typedef | `std::vector<PartitionedGeometry>` | public | — |
| `Partition` | class | `None` | public | A partitioning polygon and the geometries (and optional scalar coverages) partitioned inside it. |
| `partition_seq_type` | typedef | `std::list<Partition>` | public | — |
| `GeometryPropertyClone` | class | `None` | public | Clone of a top-level geometry domain (and optional range) property. |
| `geometry_property_clone_seq_type` | typedef | `std::vector<GeometryPropertyClone>` | public | — |
| `GeometryProperty` | class | `None` | public | The results of partitioning a feature's geometry properties with a specific geometry \*domain\* property name. |
| `partitioned_geometry_property_map_type` | typedef | `std::map<GPlatesModel::PropertyName, GeometryProperty>` | public | Mapping of geometry domain property names to partitioning results for geometry properties in the feature. |
| `partitioned_geometry_properties` | field | `partitioned_geometry_property_map_type` | public | Partitioning results for each geometry property in the feature. |

### `GPlatesAppLogic::PartitionFeatureUtils::PropertyValueAssigner`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~PropertyValueAssigner()` | destructor | `None` | public | — |
| `assign_property_values( const GPlatesModel::FeatureHandle::weak_ref &partitioned_feature, boost::optional<GPlatesModel::FeatureHandle::const_weak_ref> partitioning_feature)` | method | `void` | public | Copies property values from partitioning\_feature to partitioned\_feature. |

### `GPlatesAppLogic::PartitionFeatureUtils::GenericFeaturePropertyAssigner`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GenericFeaturePropertyAssigner( const GPlatesModel::FeatureHandle::const_weak_ref &original_feature, const AssignPlateIds::feature_property_flags_type &feature_property_types_to_assign, bool verify_information_model)` | constructor | `None` | public | Default property values, to use when there is no partitioning feature, are obtained from original\_feature. |
| `assign_property_values( const GPlatesModel::FeatureHandle::weak_ref &partitioned_feature, boost::optional<GPlatesModel::FeatureHandle::const_weak_ref> partitioning_feature)` | method | `void` | public | — |
| `d_verify_information_model` | field | `bool` | private | — |
| `d_default_reconstruction_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_default_conjugate_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |
| `d_default_valid_time` | field | `boost::optional<GPlatesPropertyValues::GmlTimePeriod::non_null_ptr_to_const_type>` | private | — |
| `d_feature_property_types_to_assign` | field | `AssignPlateIds::feature_property_flags_type` | private | — |

### `GPlatesAppLogic::PartitionFeatureUtils::PartitionedFeatureManager`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PartitionedFeatureManager( const GPlatesModel::FeatureHandle::weak_ref &original_feature, const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, const boost::shared_ptr<PropertyValueAssigner> &property_value_assigner)` | constructor | `None` | public | — |
| `get_feature_for_partition( const GPlatesModel::PropertyName &geometry_domain_property_name, bool geometry_domain_has_associated_range, boost::optional<const ReconstructionGeometry *> partition = boost::none)` | method | `GPlatesModel::FeatureHandle::weak_ref` | public | Returns the feature mapped to partition (allocates new feature if necessary). |
| `feature_contents_type` | typedef | `std::map< GPlatesModel::PropertyName/*geometry_domain_property_name*/, bool/*geometry_domain_has_associated_range*/>` | private | Typedef for a mapping of domain property name to boolean indicating an associated range. |
| `FeatureInfo` | struct | `None` | private | — |
| `feature_info_seq_type` | typedef | `std::list<FeatureInfo>` | private | — |
| `partition_to_feature_map_type` | typedef | `std::map< boost::optional<const ReconstructionGeometry *>, feature_info_seq_type>` | private | Typedef for mapping partitions to features. |
| `d_original_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | private | The original feature. |
| `d_has_original_feature_been_claimed` | field | `bool` | private | Whether the original feature is being used by an inside or outside feature. |
| `d_feature_to_clone_from` | field | `GPlatesModel::FeatureHandle::non_null_ptr_to_const_type` | private | A cloned version of the original feature. |
| `d_feature_collection` | field | `GPlatesModel::FeatureCollectionHandle::weak_ref` | private | The feature collection containing the original feature and any cloned features. |
| `d_property_value_assigner` | field | `boost::shared_ptr<PropertyValueAssigner>` | private | Used to copy requested property values from partitioning polygon feature to partitioned features. |
| `d_partitioned_features` | field | `partition_to_feature_map_type` | private | The currently assigned features for the various partitions (including the the feature representing no partition). |
| `create_feature()` | method | `GPlatesModel::FeatureHandle::weak_ref` | private | Return the original feature is it hasn't been claimed yet or return a clone of it (without geometry properties or plate id). |
| `assign_property_values( const GPlatesModel::FeatureHandle::weak_ref &partitioned_feature, boost::optional<const ReconstructionGeometry *> partition)` | method | `void` | private | Assigns property values when a feature is first referenced. |

### `GPlatesAppLogic::PartitionFeatureUtils::GeometrySizeMetric`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometrySizeMetric()` | constructor | `None` | public | — |
| `accumulate( const GPlatesMaths::GeometryOnSphere &geometry)` | method | `void` | public | For points and multipoints adds number of points to current total number of points; for polylines and polygons adds the arc distance (unit sphere) to the current total arc distance. |
| `accumulate( const GeometrySizeMetric &geometry_size_metric)` | method | `void` | public | Adds metric geometry\_size\_metric to this object. |
| `operator<( const GeometrySizeMetric &rhs)` | operator | `bool` | public | Less than operator. |
| `d_num_points` | field | `unsigned int` | private | — |
| `d_arc_distance` | field | `GPlatesMaths::real_t` | private | — |
| `d_using_arc_distance` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `POLY_GEOMETRY_DISTANCE_THRESHOLD` | variable | `GPlatesMaths::AngularExtent` | — |
| `calculate_arc_distance( GreatCircleArcForwardIteratorType gca_begin, GreatCircleArcForwardIteratorType gca_end)` | function | `GPlatesMaths::real_t` | Calculate polyline distance along unit radius sphere. |
| `calculate_partition_size_metric( const PartitionedFeature::Partition &partition)` | function | `GeometrySizeMetric` | Calculates the accumulated size metric for all partitioned inside geometries of partition. |
| `add_partitioned_geometries_to_feature( const PartitionedFeature::partitioned_geometry_seq_type &partitioned_geometries, const GPlatesModel::PropertyName &geometry_domain_property_name, const boost::optional<GPlatesModel::PropertyName> &geometry_range_property_name, PartitionedFeatureManager &partitioned_feature_manager ...` | function | `void` | Adds partitioned geometries to the partitioned feature associated with partition. |
| `operator<( const GeometrySizeMetric &rhs)` | operator | `bool` | — |
| `GPLATES_APP_LOGIC_PARTITIONFEATUREUTILS_H` | macro | `None` | — |
| `partition_feature( const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GeometryCookieCutter &geometry_cookie_cutter, bool respect_feature_time_period = true, boost::optional< std::vector<GPlatesModel::FeatureHandle::iterator> &> partitioned_properties = boost::none)` | function | `boost::shared_ptr<const PartitionedFeature>` | Partitions the geometries in the geometry properties of feature\_ref using partitioning polygons in geometry\_cookie\_cutter. |
| `add_partitioned_geometry_to_feature( const PartitionedFeature::GeometryProperty &geometry_property, PartitionedFeatureManager &partitioned_feature_manager, const ReconstructMethodInterface::Context &reconstruct_method_context, const double &reconstruction_time)` | function | `void` | Adds partitioned inside geometries to the partitioned features associated with the partitioned polygons. |
| `add_unpartitioned_geometry_to_feature( const PartitionedFeature::GeometryProperty &geometry_property, PartitionedFeatureManager &partitioned_feature_manager, const ReconstructMethodInterface::Context &reconstruct_method_context, const double &reconstruction_time, boost::optional<const ReconstructionGeometry *> partitio ...` | function | `void` | Adds the reconstructed geometry geometry\_domain\_property to the partitioned feature associated with partition and reverse reconstructs the geometry to present day (if partition has a plate id and the reconstruction time is not present day ... |
| `find_partition_containing_most_geometry( const PartitionedFeature &partitioned_feature)` | function | `boost::optional<const ReconstructionGeometry *>` | Finds the partitioning polygon that contains the most partitioned geometries of partitioned\_feature. |
| `does_feature_exist_at_reconstruction_time( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref, const double &reconstruction_time)` | function | `bool` | Returns true if feature\_ref exists at time reconstruction\_time. |
| `reverse_reconstruct( const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &reconstructed_geometry, const GPlatesModel::FeatureHandle::weak_ref &feature, const ReconstructMethodInterface::Context &reconstruct_method_context, const double &reconstruction_time)` | function | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | Returns the reverse reconstructed geometry from reconstructed\_geometry to present day using the intrinsic state (properties) of feature and extrinsic state of reconstruct\_method\_context. |
| `get_reconstruction_plate_id_from_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | function | `boost::optional<GPlatesModel::integer_plate_id_type>` | Returns the 'gpml:reconstructionPlateId' plate id if one exists. |
| `assign_reconstruction_plate_id_to_feature( boost::optional<GPlatesModel::integer_plate_id_type> reconstruction_plate_id, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, bool verify_information_model)` | function | `void` | Assigns a 'gpml:reconstructionPlateId' property value to feature\_ref. |
| `get_conjugate_plate_id_from_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | function | `boost::optional<GPlatesModel::integer_plate_id_type>` | Returns the 'gpml:conjugatePlateId' plate id if one exists. |
| `assign_conjugate_plate_id_to_feature( boost::optional<GPlatesModel::integer_plate_id_type> conjugate_plate_id, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, bool verify_information_model)` | function | `void` | Assigns a 'gpml:conjugatePlateId' property value to feature\_ref. |
| `get_valid_time_from_feature( const GPlatesModel::FeatureHandle::const_weak_ref &feature_ref)` | function | `boost::optional<GPlatesPropertyValues::GmlTimePeriod::non_null_ptr_to_const_type>` | Returns the 'gml:validTime' time period if one exists. |
| `assign_valid_time_to_feature( boost::optional<GPlatesPropertyValues::GmlTimePeriod::non_null_ptr_to_const_type> valid_time, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, bool verify_information_model)` | function | `void` | Assigns a 'gml:validTime' property value to feature\_ref. |
| `append_geometry_domain_to_feature( const geometry_domain_type &geometry_domain, const GPlatesModel::PropertyName &geometry_domain_property_name, const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | function | `void` | Creates a property value suitable for geometry\_domain and appends it to feature\_ref with the property name geometry\_domain\_property\_name. |
| `append_geometry_range_to_feature( const geometry_range_type &geometry_range, const GPlatesModel::PropertyName &geometry_range_property_name, const GPlatesModel::FeatureHandle::weak_ref &feature_ref)` | function | `void` | Creates a property value suitable for geometry\_range and appends it to feature\_ref with the property name geometry\_range\_property\_name. |

## Notes

[[[PROSE notes unit=app-logic/PartitionFeatureUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GenericPartitionFeatureTask](GenericPartitionFeatureTask.md) | app-logic | 62 |
| [app-logic/deprecated/PropertyValuePropogator](deprecated/PropertyValuePropogator.md) | app-logic | 28 |
| [app-logic/ReconstructMethodByPlateId](ReconstructMethodByPlateId.md) | app-logic | 5 |
| [app-logic/VgpPartitionFeatureTask](VgpPartitionFeatureTask.md) | app-logic | 5 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 4 |
| [gui/FileIOFeedback](../gui/FileIOFeedback.md) | gui | 4 |
| [api/PyViewportWindow](../api/PyViewportWindow.md) | api | 2 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 2 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 2 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 2 |
| [unit-test/FeatureHandleTest](../unit-test/FeatureHandleTest.md) | unit-test | 2 |
| [app-logic/TopologyReconstruct](TopologyReconstruct.md) | app-logic | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/PartitionFeatureUtils.h
python scripts/gpq.py def GPlatesAppLogic::PartitionFeatureUtils::(anonymous)::PartitionFeatureGeometryProperties --body
python scripts/gpq.py uses PartitionFeatureGeometryProperties --kind class
python scripts/gpq.py hier PartitionFeatureGeometryProperties
```
