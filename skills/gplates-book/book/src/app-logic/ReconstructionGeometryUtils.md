# ReconstructionGeometryUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 95 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGeometryUtils.h` | C++ | 1205 |
| `src/app-logic/ReconstructionGeometryUtils.cc` | C++ | 561 |

## Overview

This is the type-dispatch toolkit for the `ReconstructionGeometry` hierarchy, and in practice it is how most of the application interacts with reconstruction output. A client that has been handed a `ReconstructionGeometry::non_null_ptr_to_const_type` almost always wants one of two things: a downcast to a particular derived type, or one attribute — the feature, the geometry property iterator, the plate ID, the time of formation, the reconstruction tree or its creator, a boundary polygon — that only some of the derived types possess. Neither is done with RTTI. Each attribute is a small `ConstReconstructionGeometryVisitor` that parks its answer in a `boost::optional`, wrapped in a one-line function template that constructs the visitor, calls `accept_visitor` and returns the optional. That is why so much of this unit lives in the header: the templates must see the visitor classes, so only the visitors' `visit` bodies and the three non-template search functions are in the `.cc`.

The downcast is `get_reconstruction_geometry_derived_type` and its sequence form, built on `ReconstructionGeometryDerivedTypeFinder`, which overrides exactly one `visit` — the one for the requested type. Two useful behaviours fall out of the visitor base's delegating defaults rather than from any code here: asking for `ReconstructedFeatureGeometry` also matches flowlines, motion paths, small circles, virtual geomagnetic poles and topology-reconstructed geometries, and asking for `ResolvedTopologicalGeometry` also matches resolved boundaries and lines. The `Implementation::GetPointeeType` metafunction is what lets the same template take a raw pointer or a `GPlatesUtils::non_null_intrusive_ptr`, const or not, independently on the input and on the requested output; it is deliberately written so that a `boost::shared_ptr` will not compile, since that would take ownership of a reference-counted object.

The attribute visitors also encode which derived types genuinely lack which attribute, and the gaps are intentional rather than defensive: `MultiPointVectorField` corresponds to no single plate and so yields no plate ID, no time of formation and no reconstruction tree; `ResolvedTopologicalNetwork` supports neither tree nor tree creator; `ReconstructedScalarCoverage` forwards nearly everything to the `ReconstructedFeatureGeometry` it wraps. Separately, the three `find_reconstruction_geometries_observing_feature` overloads are the feature-to-geometry direction: they run a `ReconstructionGeometryFinder` over the weak-observer chain of a `GPlatesModel::FeatureHandle`, optionally narrowed to one geometry property and to a set of reconstruct handles, then intersect the result with a caller-supplied subset. This is how the GUI keeps hold of a focused geometry when the reconstruction time changes and every reconstruction geometry has been rebuilt — including the case where the old geometry no longer exists because the new time fell outside the feature's valid time range.

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

**Every visitor here opens with `using ConstReconstructionGeometryVisitor::visit;`.** That is not decoration. Declaring any `visit` override hides the whole inherited overload set, which would silently disable the base visitor's delegating defaults and stop derived reconstruction-geometry types from resolving to their base's handler.

**A new `ReconstructionGeometry` subclass will silently return `boost::none` here.** Unless it derives from a type one of these visitors already handles, adding a subclass means adding an overload to each of `GetFeatureRef`, `GetGeometryProperty`, `GetPlateId`, `GetTimeOfFormation`, `GetReconstructionTree`, `GetReconstructionTreeCreator` and the polygon visitors. Nothing in the type system flags the omission.

**`none` means two different things, and only sometimes the same one.** `get_feature_ref` and `get_geometry_property_iterator` return `none` both when the derived type carries no such thing and when the stored reference has gone stale — they explicitly test `is_valid()` and `is_still_valid()`. `get_plate_id` and `get_time_of_formation` do no such filtering and report only absence.

**`get_boundary_polygon` is not free on a lazily reconstructed RFG.** Its `ReconstructedFeatureGeometry` overload calls `reconstructed_geometry()`, which forces the deferred finite-rotation transform (and caches it). The resolved-topology paths just return the polygon the topology resolver already built. It also returns `none` for a reconstructed geometry that is a polyline or multipoint rather than a polygon, which is not an error.

**Constness does not propagate to the model.** These are `Const`ReconstructionGeometryVisitor subclasses, yet `get_feature_ref` hands back a non-const `GPlatesModel::FeatureHandle::weak_ref` and `get_geometry_property_iterator` a non-const `iterator`. A const reconstruction geometry gives you write access to its feature.

**The subset intersection is quadratic.** `find_reconstruction_geometries_observing_feature` does a linear `std::find` through `reconstruction_geometries_subset` for each geometry the finder returns. That is fine for one focused feature against a layer's output, and a trap if you loop it over many features.

**`get_reconstruction_geometry_derived_type` yields at most one result** — a single `accept_visitor` can push at most one entry into the finder — whereas the sequence form reuses one finder across the whole input range and appends, so the output container is added to, not cleared.

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
