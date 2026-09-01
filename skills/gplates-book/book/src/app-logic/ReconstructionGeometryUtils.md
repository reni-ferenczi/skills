# ReconstructionGeometryUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 95 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGeometryUtils.h` | C++ | 1205 |
| `src/app-logic/ReconstructionGeometryUtils.cc` | C++ | 561 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionGeometryUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionGeometryUtils::reconstruction_geom_seq_type`](#gplatesapplogicreconstructiongeometryutilsreconstruction_geom_seq_type) | typedef | — | — | 0 | Typedef for sequence of ReconstructionGeometry objects. |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::ReconstructionGeometryDerivedTypeFinder`](#gplatesapplogicreconstructiongeometryutilsreconstructiongeometryderivedtypefinder) | class | [`ReconstructionGeometryVisitorBase< typename GPlatesUtils::CopyConst< ReconstructionGeometryDerivedType, ReconstructionGeometry>::type >`](ReconstructionGeometryVisitor.md) | `<class ReconstructionGeometryDerivedType>` | 0 | Template visitor class to find instances of a class derived from ReconstructionGeometry. |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::Implementation::GetNonNullIntrusivePointeeType`](#gplatesapplogicreconstructiongeometryutilsimplementationgetnonnullintrusivepointeetype) | struct | — | `<typename NonNullIntrusivePtrType>` | 0 | Metafunction to extract pointee type (pointed-to type) from a non-null intrusive pointer. |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::Implementation::GetNonNullIntrusivePointeeType< GPlatesUtils::non_null_intrusive_ptr<Type> >`](#gplatesapplogicreconstructiongeometryutilsimplementationgetnonnullintrusivepointeetype-gplatesutilsnon_null_intrusive_ptrtype-) | struct | — | `<typename Type>` | 0 | We only want it to compile/work for non-null intrusive smart pointer types. |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::Implementation::GetPointeeType`](#gplatesapplogicreconstructiongeometryutilsimplementationgetpointeetype) | struct | — | `<typename PointerType>` | 0 | Metafunction to extract pointee type (pointed-to type) from a raw pointer or non-null intrusive pointer. |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetFeatureRef`](#gplatesapplogicreconstructiongeometryutilsgetfeatureref) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetGeometryProperty`](#gplatesapplogicreconstructiongeometryutilsgetgeometryproperty) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetPlateId`](#gplatesapplogicreconstructiongeometryutilsgetplateid) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetTimeOfFormation`](#gplatesapplogicreconstructiongeometryutilsgettimeofformation) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetReconstructionTree`](#gplatesapplogicreconstructiongeometryutilsgetreconstructiontree) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetReconstructionTreeCreator`](#gplatesapplogicreconstructiongeometryutilsgetreconstructiontreecreator) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetResolvedTopologicalBoundarySubSegmentSequence`](#gplatesapplogicreconstructiongeometryutilsgetresolvedtopologicalboundarysubsegmentsequence) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetResolvedTopologicalBoundaryOrLineGeometry`](#gplatesapplogicreconstructiongeometryutilsgetresolvedtopologicalboundaryorlinegeometry) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetResolvedTopologicalBoundaryPolygon`](#gplatesapplogicreconstructiongeometryutilsgetresolvedtopologicalboundarypolygon) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetBoundaryPolygon`](#gplatesapplogicreconstructiongeometryutilsgetboundarypolygon) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |
| [`GPlatesAppLogic::ReconstructionGeometryUtils::GetResolvedTopologicalBoundarySectionGeometry`](#gplatesapplogicreconstructiongeometryutilsgetresolvedtopologicalboundarysectiongeometry) | class | [`ConstReconstructionGeometryVisitor`](ReconstructionGeometry.md) | — | 0 | — |

## Members

### `GPlatesAppLogic::ReconstructionGeometryUtils::reconstruction_geom_seq_type`

*None.*

### `GPlatesAppLogic::ReconstructionGeometryUtils::ReconstructionGeometryDerivedTypeFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `base_class_type` | typedef | `ReconstructionGeometryVisitorBase< typename GPlatesUtils::CopyConst< ReconstructionGeometryDerivedType, ReconstructionGeometry>::type >` | public | Typedef for base class type. |
| `reconstruction_geometry_derived_type` | typedef | `ReconstructionGeometryDerivedType` | public | Convenience typedef for the template parameter which is a type derived from ReconstructionGeometry. |
| `container_type` | typedef | `std::vector<reconstruction_geometry_derived_type *>` | public | Convenience typedef for sequence of pointers to reconstruction geometry derived type. |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstruction_geometry_derived_type> &rg)` | method | `void` | public | Visit method for the derived ReconstructionGeometry type. |
| `d_found_geometries` | field | `container_type` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::Implementation::GetNonNullIntrusivePointeeType`

*None.*

### `GPlatesAppLogic::ReconstructionGeometryUtils::Implementation::GetNonNullIntrusivePointeeType< GPlatesUtils::non_null_intrusive_ptr<Type> >`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `typename GPlatesUtils::non_null_intrusive_ptr<Type>::element_type` | public | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::Implementation::GetPointeeType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `type` | typedef | `typename boost::mpl::eval_if< boost::is_pointer<PointerType>, // Is raw pointer ? boost::remove_pointer<PointerType>, // Delay instantiation until sure not a raw pointer because // ...` | public | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetFeatureRef`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit( const GPlatesUtils::non_null_intrusive_ptr<multi_point_vector_field_type> &mpvf)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | public | Derivations of ReconstructedFeatureGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | public | Derivations of ResolvedTopologicalGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_scalar_coverage_type> &rsc)` | method | `void` | public | — |
| `d_feature_ref` | field | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetGeometryProperty`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit( const GPlatesUtils::non_null_intrusive_ptr<multi_point_vector_field_type> &mpvf)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | public | Derivations of ReconstructedFeatureGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | public | Derivations of ResolvedTopologicalGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_scalar_coverage_type> &rsc)` | method | `void` | public | — |
| `d_property` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetPlateId`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit( const GPlatesUtils::non_null_intrusive_ptr<multi_point_vector_field_type> &mpvf)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | public | Derivations of ReconstructedFeatureGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | public | Derivations of ResolvedTopologicalGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_scalar_coverage_type> &rsc)` | method | `void` | public | — |
| `d_plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetTimeOfFormation`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit( const GPlatesUtils::non_null_intrusive_ptr<multi_point_vector_field_type> &mpvf)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | public | Derivations of ReconstructedFeatureGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | public | Derivations of ResolvedTopologicalGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_scalar_coverage_type> &rsc)` | method | `void` | public | — |
| `d_time_of_formation` | field | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetReconstructionTree`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetReconstructionTree( boost::optional<double> reconstruction_time)` | constructor | `None` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<multi_point_vector_field_type> &mpvf)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | public | Derivations of ReconstructedFeatureGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | public | Derivations of ResolvedTopologicalGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_scalar_coverage_type> &rsc)` | method | `void` | public | — |
| `d_reconstruction_time` | field | `boost::optional<double>` | private | — |
| `d_reconstruction_tree` | field | `boost::optional<ReconstructionTree::non_null_ptr_to_const_type>` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetReconstructionTreeCreator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit( const GPlatesUtils::non_null_intrusive_ptr<multi_point_vector_field_type> &mpvf)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | public | Derivations of ReconstructedFeatureGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | public | Derivations of ResolvedTopologicalGeometry default to its implementation... |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_scalar_coverage_type> &rsc)` | method | `void` | public | — |
| `d_reconstruction_tree_creator` | field | `boost::optional<ReconstructionTreeCreator>` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetResolvedTopologicalBoundarySubSegmentSequence`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_sub_segment_sequence()` | method | `boost::optional<const sub_segment_seq_type &>` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_boundary_type> &rtb)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `d_sub_segment_sequence` | field | `boost::optional<const sub_segment_seq_type &>` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetResolvedTopologicalBoundaryOrLineGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetResolvedTopologicalBoundaryOrLineGeometry( bool include_network_rigid_block_holes)` | constructor | `None` | public | — |
| `get_geometry()` | method | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_geometry_type> &rtg)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `d_geometry` | field | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | — |
| `d_include_network_rigid_block_holes` | field | `bool` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetResolvedTopologicalBoundaryPolygon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetResolvedTopologicalBoundaryPolygon( bool include_network_rigid_block_holes)` | constructor | `None` | public | — |
| `get_boundary_polygon()` | method | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_boundary_type> &rtb)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `d_boundary_polygon` | field | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | private | — |
| `d_include_network_rigid_block_holes` | field | `bool` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetBoundaryPolygon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GetBoundaryPolygon( bool include_network_rigid_block_holes)` | constructor | `None` | public | — |
| `get_boundary_polygon()` | method | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_boundary_type> &rtb)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_network_type> &rtn)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_scalar_coverage_type> &rsc)` | method | `void` | public | — |
| `d_boundary_polygon` | field | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | private | — |
| `d_include_network_rigid_block_holes` | field | `bool` | private | — |

### `GPlatesAppLogic::ReconstructionGeometryUtils::GetResolvedTopologicalBoundarySectionGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `get_boundary_section_geometry()` | method | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<reconstructed_feature_geometry_type> &rfg)` | method | `void` | public | — |
| `visit( const GPlatesUtils::non_null_intrusive_ptr<resolved_topological_line_type> &rtl)` | method | `void` | public | — |
| `d_boundary_section_geometry` | field | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_reconstruction_geometries_subset( ReconstructionGeometryUtils::reconstruction_geom_seq_type &reconstruction_geometries_observing_feature, const ReconstructionGeometryUtils::reconstruction_geom_seq_type &reconstruction_geometries_subset, const ReconstructionGeometryFinder &rg_finder)` | function | `bool` | Returns those reconstruction geometries found by rg\_finder that are in the subset reconstruction\_geometries\_subset. |
| `GPLATES_APPLOGIC_RECONSTRUCTIONGEOMETRYUTILS_H` | macro | `None` | — |
| `get_feature_handle_ptr( ReconstructionGeometryPointer reconstruction_geom_ptr)` | function | `boost::optional<GPlatesModel::FeatureHandle *>` | Visits a ReconstructionGeometry to get a pointer to its feature handle. |
| `get_reconstruction_tree( ReconstructionGeometryPointer reconstruction_geom_ptr, boost::optional<double> reconstruction_time = boost::none)` | function | `boost::optional<ReconstructionTree::non_null_ptr_to_const_type>` | Visits a ReconstructionGeometry to get the reconstruction tree for the specified time. |
| `get_resolved_topological_boundary_or_line_geometry( ReconstructionGeometryPointer reconstruction_geom_ptr, bool include_network_rigid_block_holes = false)` | function | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | Returns the boundary polygon (or line polyline) of the specified resolved topology. reconstruction\_geom\_ptr can be a ResolvedTopologicalLine, ResolvedTopologicalBoundary or ResolvedTopologicalNetwork. |
| `get_resolved_topological_boundary_polygon( ReconstructionGeometryPointer reconstruction_geom_ptr, bool include_network_rigid_block_holes = false)` | function | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | Returns the boundary polygon of the specified resolved topology. reconstruction\_geom\_ptr can be either a ResolvedTopologicalBoundary or ResolvedTopologicalNetwork. |
| `get_boundary_polygon( ReconstructionGeometryPointer reconstruction_geom_ptr, bool include_network_rigid_block_holes = false)` | function | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | Returns the boundary polygon of the specified reconstruction geometry. reconstruction\_geom\_ptr can be a ReconstructedFeatureGeometry (or derived from it), a ResolvedTopologicalBoundary or a ResolvedTopologicalNetwork. |
| `find_reconstruction_geometries_observing_feature( reconstruction_geom_seq_type &reconstruction_geometries_observing_feature, const reconstruction_geom_seq_type &reconstruction_geometries_subset, const ReconstructionGeometry &reconstruction_geometry, boost::optional<const std::vector<ReconstructHandle::type> &> reconstr ...` | function | `bool` | Finds the ReconstructionGeometry objects that were generated from the same geometry property as reconstruction\_geometry and that were optionally reconstructed using reconstruction\_tree and that are from the subset of reconstruction ... |
| `find_reconstruction_geometries_observing_feature( reconstruction_geom_seq_type &reconstruction_geometries_observing_feature, const reconstruction_geom_seq_type &reconstruction_geometries_subset, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, boost::optional<const std::vector<ReconstructHandle::type> &> recon ...` | function | `bool` | Finds the ReconstructionGeometry objects from feature feature\_ref and that were optionally reconstructed using reconstruction\_tree and that are from the subset of reconstruction geometries in reconstruction\_geometries\_subset. |
| `find_reconstruction_geometries_observing_feature( reconstruction_geom_seq_type &reconstruction_geometries_observing_feature, const reconstruction_geom_seq_type &reconstruction_geometries_subset, const GPlatesModel::FeatureHandle::weak_ref &feature_ref, const GPlatesModel::FeatureHandle::iterator &geometry_property_iter ...` | function | `bool` | Finds the ReconstructionGeometry objects that were optionally generated from the geometry property geometry\_property\_iterator in feature feature\_ref and that were optionally reconstructed using reconstruction\_tree and that are from the ... |
| `get_reconstruction_geometry_derived_type( ReconstructionGeometryPointer reconstruction_geom_ptr)` | function | `boost::optional<ReconstructionGeometryDerivedPointer>` | — |
| `get_reconstruction_geometry_derived_type_sequence( ReconstructionGeometryForwardIter reconstruction_geoms_begin, ReconstructionGeometryForwardIter reconstruction_geoms_end, ContainerOfReconstructionGeometryDerivedPointerType &reconstruction_geom_derived_type_seq)` | function | `bool` | — |
| `get_feature_ref( ReconstructionGeometryPointer reconstruction_geom_ptr)` | function | `boost::optional<GPlatesModel::FeatureHandle::weak_ref>` | — |
| `get_geometry_property_iterator( ReconstructionGeometryPointer reconstruction_geom_ptr)` | function | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | — |
| `get_plate_id( ReconstructionGeometryPointer reconstruction_geom_ptr)` | function | `boost::optional<GPlatesModel::integer_plate_id_type>` | — |
| `get_time_of_formation( ReconstructionGeometryPointer reconstruction_geom_ptr)` | function | `boost::optional<GPlatesPropertyValues::GeoTimeInstant>` | — |
| `get_reconstruction_tree( ReconstructionGeometryPointer reconstruction_geom_ptr, boost::optional<double> reconstruction_time)` | function | `boost::optional<ReconstructionTree::non_null_ptr_to_const_type>` | — |
| `get_reconstruction_tree_creator( ReconstructionGeometryPointer reconstruction_geom_ptr)` | function | `boost::optional<ReconstructionTreeCreator>` | — |
| `get_resolved_topological_boundary_sub_segment_sequence( ReconstructionGeometryPointer reconstruction_geom_ptr)` | function | `boost::optional<const sub_segment_seq_type &>` | — |
| `get_resolved_topological_boundary_or_line_geometry( ReconstructionGeometryPointer reconstruction_geom_ptr, bool include_network_rigid_block_holes)` | function | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | — |
| `get_resolved_topological_boundary_polygon( ReconstructionGeometryPointer reconstruction_geom_ptr, bool include_network_rigid_block_holes)` | function | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | — |
| `get_boundary_polygon( ReconstructionGeometryPointer reconstruction_geom_ptr, bool include_network_rigid_block_holes)` | function | `boost::optional<GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type>` | — |
| `get_resolved_topological_boundary_section_geometry( ReconstructionGeometryPointer reconstruction_geom_ptr)` | function | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | — |

## Notes

[[[PROSE notes unit=app-logic/ReconstructionGeometryUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/RenderedGeometryUtils](../view-operations/RenderedGeometryUtils.md) | view-operations | 20 |
| [app-logic/TopologyNetworkResolver](TopologyNetworkResolver.md) | app-logic | 19 |
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 17 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 17 |
| [app-logic/GeometryCookieCutter](GeometryCookieCutter.md) | app-logic | 15 |
| [file-io/CitcomsResolvedTopologicalBoundaryExport](../file-io/CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 13 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 13 |
| [app-logic/PlateVelocityUtils](PlateVelocityUtils.md) | app-logic | 12 |
| [app-logic/ResolvedTopologicalSubSegmentImpl](ResolvedTopologicalSubSegmentImpl.md) | app-logic | 12 |
| [gui/FeatureTableModel](../gui/FeatureTableModel.md) | gui | 12 |
| [gui/ExportNetRotationAnimationStrategy](../gui/ExportNetRotationAnimationStrategy.md) | gui | 10 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 9 |
| [file-io/ReconstructionGeometryExportImpl](../file-io/ReconstructionGeometryExportImpl.md) | file-io | 9 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 9 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 8 |
| [qt-widgets/QueryFeaturePropertiesWidget](../qt-widgets/QueryFeaturePropertiesWidget.md) | qt-widgets | 8 |
| [app-logic/PropertyExtractors](PropertyExtractors.md) | app-logic | 7 |
| [app-logic/TopologyGeometryResolver](TopologyGeometryResolver.md) | app-logic | 7 |
| [app-logic/TopologyGeometryResolverLayerProxy](TopologyGeometryResolverLayerProxy.md) | app-logic | 7 |
| [qt-widgets/GenerateDeformingMeshPointsDialog](../qt-widgets/GenerateDeformingMeshPointsDialog.md) | qt-widgets | 7 |

*... and 39 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionGeometryUtils.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionGeometryUtils::GetReconstructionTree --body
python scripts/gpq.py uses GetReconstructionTree --kind class
python scripts/gpq.py hier GetReconstructionTree
```
