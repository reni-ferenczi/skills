# GeometryBuilder

[Book TOC](../../TOC.md) · [view-operations](../../components/view-operations.md) · cluster Community 182 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/view-operations/GeometryBuilder.h` | C++ | 947 |
| `src/view-operations/GeometryBuilder.cc` | C++ | 954 |

## Overview

`GeometryBuilder` is the mutable, observable model that sits behind geometry
digitisation and vertex editing. Everything downstream of it — `GeometryOnSphere`
and its subclasses — is immutable, so there has to be somewhere to accumulate a
half-finished polyline while the user is still clicking. That somewhere is a
sequence of `InternalGeometryBuilder` objects, each of which is little more than a
`std::vector<GPlatesMaths::PointOnSphere>` plus the *desired* geometry type and a
dirty flag. The immutable `GeometryOnSphere` is manufactured lazily by
`InternalGeometryBuilder::update()` and only when someone asks for it, which is
why the editing tools can insert, move and delete single vertices without paying
for a geometry rebuild on every mouse event. The distinction between the type the
user asked for (`get_geometry_build_type`) and the type the points currently
support (`get_actual_type_of_current_geometry`) is central: three clicks towards a
polygon are still only a polyline, and the `changed_actual_geometry_type` signal
is how the UI finds out when that promotion happens.

Two instances exist for the whole application, both owned by
`GPlatesPresentation::ViewState` as `boost::scoped_ptr` members: one for the
digitisation tools building a brand-new geometry, and one holding the focused
feature's geometry, which `FocusedFeatureGeometryManipulator` keeps synchronised
with the model in both directions. The `GeometryOperation` subclasses
(`AddPointGeometryOperation`, `InsertVertexGeometryOperation`,
`MoveVertexGeometryOperation`, `DeleteVertexGeometryOperation`,
`SplitFeatureGeometryOperation`) all mutate one of these builders and then render
the result; `GPlatesQtWidgets::LatLonCoordinatesTable` and `DigitisationWidget`
observe the same builder to show the vertex list.

Undo is not a command stack here — it is a memento protocol. Every public mutator
returns an opaque `UndoOperation` (a `boost::any` wrapping a
`boost::shared_ptr<GeometryBuilderInternal::UndoImplInterface>`), and the
`QUndoCommand` subclasses in `GeometryBuilderUndoCommands` simply hold that value
and hand it back to `undo()`. Undoing is double dispatch: `undo` unwraps the
memento, calls `accept_undo_visitor`, and the concrete memento calls back into the
matching `GeometryBuilder::visit_undo_operation` overload, which performs the
inverse *public* operation — undoing an insert is a remove, undoing a
set-geometry-type is another set-geometry-type. `CompositeUndoImpl` chains several
mementos and replays them in reverse, which is how the templated `set_geometry`
composes clear + set-type + insert into a single undoable step. The
`SecondaryGeometry` machinery is a separate concern bolted onto the same class:
it records neighbouring `GPlatesAppLogic::ReconstructedFeatureGeometry`s whose
vertices coincide with the vertex being dragged, so the MoveVertex tool can drag
shared vertices of adjacent features together. `GeometryUpdater` and
`GeometryVertexFinder` are the `ConstGeometryOnSphereVisitor`s that respectively
rebuild an immutable geometry with one vertex replaced, and read one vertex out of
it by index.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesViewOperations::GeometryBuilderInternal::UndoImplInterface`](#gplatesviewoperationsgeometrybuilderinternalundoimplinterface) | class | — | — | 7 | — |
| [`GPlatesViewOperations::GeometryBuilderInternal::InsertPointUndoImpl`](#gplatesviewoperationsgeometrybuilderinternalinsertpointundoimpl) | class | [`UndoImplInterface`](GeometryBuilder.md) | — | 0 | — |
| [`GPlatesViewOperations::GeometryBuilderInternal::RemovePointUndoImpl`](#gplatesviewoperationsgeometrybuilderinternalremovepointundoimpl) | class | [`UndoImplInterface`](GeometryBuilder.md) | — | 0 | — |
| [`GPlatesViewOperations::GeometryBuilderInternal::MovePointUndoImpl`](#gplatesviewoperationsgeometrybuilderinternalmovepointundoimpl) | class | [`UndoImplInterface`](GeometryBuilder.md) | — | 0 | — |
| [`GPlatesViewOperations::GeometryBuilderInternal::SetGeometryTypeUndoImpl`](#gplatesviewoperationsgeometrybuilderinternalsetgeometrytypeundoimpl) | class | [`UndoImplInterface`](GeometryBuilder.md) | — | 0 | — |
| [`GPlatesViewOperations::GeometryBuilderInternal::ClearAllGeometriesUndoImpl`](#gplatesviewoperationsgeometrybuilderinternalclearallgeometriesundoimpl) | class | [`UndoImplInterface`](GeometryBuilder.md) | — | 0 | — |
| [`GPlatesViewOperations::GeometryBuilderInternal::InsertGeometryUndoImpl`](#gplatesviewoperationsgeometrybuilderinternalinsertgeometryundoimpl) | class | [`UndoImplInterface`](GeometryBuilder.md) | — | 0 | — |
| [`GPlatesViewOperations::GeometryBuilderInternal::CompositeUndoImpl`](#gplatesviewoperationsgeometrybuilderinternalcompositeundoimpl) | class | [`UndoImplInterface`](GeometryBuilder.md) | — | 0 | — |
| [`GPlatesViewOperations::GeometryBuilderInternal::UndoImpl`](#gplatesviewoperationsgeometrybuilderinternalundoimpl) | typedef | — | — | 0 | — |
| [`GPlatesViewOperations::SecondaryGeometry`](#gplatesviewoperationssecondarygeometry) | struct | — | — | 0 | Stores any geometries which have vertices lying near the MoveVertex tool's highlighted point. @rfg is required so that we can update the feature's geometry property from @geometry\_on\_sphere at the end of a move vertex action. ... |
| [`GPlatesViewOperations::GeometryUpdater`](#gplatesviewoperationsgeometryupdater) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | Visitor for creating a new GeometryOnSphere in which vertex @index\_of\_vertex has been changed to @point\_on\_sphere. |
| [`GPlatesViewOperations::GeometryVertexFinder`](#gplatesviewoperationsgeometryvertexfinder) | class | [`GPlatesMaths::ConstGeometryOnSphereVisitor`](../maths/ConstGeometryOnSphereVisitor.md) | — | 0 | — |
| [`GPlatesViewOperations::GeometryBuilder`](#gplatesviewoperationsgeometrybuilder) | class | `QObject` | — | 0 | — |

## Members

### `GPlatesViewOperations::GeometryBuilderInternal::UndoImplInterface`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~UndoImplInterface()` | destructor | `None` | public | — |
| `accept_undo_visitor( GPlatesViewOperations::GeometryBuilder *)` | method | `void` | public | — |

### `GPlatesViewOperations::GeometryBuilderInternal::InsertPointUndoImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InsertPointUndoImpl( GeometryBuilder::PointIndex point_index)` | constructor | `None` | public | — |
| `accept_undo_visitor( GPlatesViewOperations::GeometryBuilder* geometry_builder)` | method | `void` | public | — |
| `d_point_index` | field | `GeometryBuilder::PointIndex` | public | — |

### `GPlatesViewOperations::GeometryBuilderInternal::RemovePointUndoImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RemovePointUndoImpl( GeometryBuilder::PointIndex point_index, const GPlatesMaths::PointOnSphere &point)` | constructor | `None` | public | — |
| `accept_undo_visitor( GPlatesViewOperations::GeometryBuilder* geometry_builder)` | method | `void` | public | — |
| `d_point_index` | field | `GeometryBuilder::PointIndex` | public | — |
| `d_point` | field | `GPlatesMaths::PointOnSphere` | public | — |

### `GPlatesViewOperations::GeometryBuilderInternal::MovePointUndoImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MovePointUndoImpl( GeometryBuilder::PointIndex point_index, const GPlatesMaths::PointOnSphere &old_point, std::vector<SecondaryGeometry> &secondary_geometries, std::vector<GPlatesMaths::PointOnSphere> &secondary_points)` | constructor | `None` | public | — |
| `accept_undo_visitor( GPlatesViewOperations::GeometryBuilder* geometry_builder)` | method | `void` | public | — |
| `d_point_index` | field | `GeometryBuilder::PointIndex` | public | — |
| `d_old_point` | field | `GPlatesMaths::PointOnSphere` | public | — |
| `d_secondary_geometries` | field | `std::vector<SecondaryGeometry>` | public | — |
| `d_secondary_points` | field | `std::vector<GPlatesMaths::PointOnSphere>` | public | — |

### `GPlatesViewOperations::GeometryBuilderInternal::SetGeometryTypeUndoImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SetGeometryTypeUndoImpl( GPlatesMaths::GeometryType::Value prev_geom_type)` | constructor | `None` | public | — |
| `accept_undo_visitor( GPlatesViewOperations::GeometryBuilder* geometry_builder)` | method | `void` | public | — |
| `d_prev_geom_type` | field | `GPlatesMaths::GeometryType::Value` | public | — |

### `GPlatesViewOperations::GeometryBuilderInternal::ClearAllGeometriesUndoImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ClearAllGeometriesUndoImpl( GeometryBuilder::GeometryIndex prev_current_geom_index)` | constructor | `None` | public | — |
| `accept_undo_visitor( GPlatesViewOperations::GeometryBuilder* geometry_builder)` | method | `void` | public | — |
| `geometry_seq_type` | typedef | `std::vector<InternalGeometryBuilder::point_seq_type>` | public | Typedef for a sequence of geometries. |
| `d_prev_current_geom_index` | field | `GeometryBuilder::GeometryIndex` | public | — |
| `d_geometry_seq` | field | `geometry_seq_type` | public | — |

### `GPlatesViewOperations::GeometryBuilderInternal::InsertGeometryUndoImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InsertGeometryUndoImpl( GeometryBuilder::GeometryIndex geom_index)` | constructor | `None` | public | — |
| `accept_undo_visitor( GPlatesViewOperations::GeometryBuilder* geometry_builder)` | method | `void` | public | — |
| `d_geom_index` | field | `GeometryBuilder::GeometryIndex` | public | — |

### `GPlatesViewOperations::GeometryBuilderInternal::CompositeUndoImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `undo_operation_seq_type` | typedef | `std::vector<GeometryBuilder::UndoOperation>` | public | Typedef for a sequence of UndoOperation objects. |
| `CompositeUndoImpl( undo_operation_seq_type undo_operation_seq)` | constructor | `None` | public | — |
| `accept_undo_visitor( GPlatesViewOperations::GeometryBuilder* geometry_builder)` | method | `void` | public | — |
| `d_undo_operation_seq` | field | `undo_operation_seq_type` | public | — |

### `GPlatesViewOperations::GeometryBuilderInternal::UndoImpl`

*None.*

### `GPlatesViewOperations::SecondaryGeometry`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SecondaryGeometry( GPlatesAppLogic::ReconstructedFeatureGeometry::non_null_ptr_to_const_type rfg, GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type geometry_on_sphere, unsigned int index_of_vertex)` | constructor | `None` | public | — |
| `d_rfg` | field | `GPlatesAppLogic::ReconstructedFeatureGeometry::non_null_ptr_to_const_type` | public | — |
| `d_geometry_on_sphere` | field | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | — |
| `d_index_of_vertex` | field | `unsigned int` | public | — |

### `GPlatesViewOperations::GeometryUpdater`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryUpdater( const GPlatesMaths::PointOnSphere &point_on_sphere, unsigned int index_of_vertex)` | constructor | `None` | public | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `geometry()` | method | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | — |
| `d_point_on_sphere` | field | `GPlatesMaths::PointOnSphere` | private | — |
| `d_index_of_vertex` | field | `unsigned int` | private | — |
| `d_validity` | field | `GPlatesUtils::GeometryConstruction::GeometryConstructionValidity` | private | — |
| `d_geometry` | field | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | private | — |

### `GPlatesViewOperations::GeometryVertexFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GeometryVertexFinder( unsigned int index)` | constructor | `None` | public | — |
| `visit_point_on_sphere( GPlatesMaths::PointGeometryOnSphere::non_null_ptr_to_const_type point_on_sphere)` | method | `void` | public | — |
| `visit_multi_point_on_sphere( GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type multi_point_on_sphere)` | method | `void` | public | — |
| `visit_polyline_on_sphere( GPlatesMaths::PolylineOnSphere::non_null_ptr_to_const_type polyline_on_sphere)` | method | `void` | public | — |
| `visit_polygon_on_sphere( GPlatesMaths::PolygonOnSphere::non_null_ptr_to_const_type polygon_on_sphere)` | method | `void` | public | — |
| `get_vertex()` | method | `boost::optional<GPlatesMaths::PointOnSphere>` | public | — |
| `d_index` | field | `unsigned int` | private | — |
| `d_vertex` | field | `boost::optional<GPlatesMaths::PointOnSphere>` | private | — |

### `GPlatesViewOperations::GeometryBuilder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `geometry_opt_ptr_type` | typedef | `boost::optional<GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type>` | public | This typedef is used wherever geometry (of some unknown type) is expected. |
| `GeometryIndex` | typedef | `unsigned int` | public | Geometry index. |
| `PointIndex` | typedef | `unsigned int` | public | Point index within a geometry. |
| `point_const_iterator_type` | typedef | `InternalGeometryBuilder::point_seq_const_iterator_type` | public | Const iterator over geometry points. |
| `UndoOperation` | typedef | `boost::any` | public | Opaque undo memento returned by public modifying operations. |
| `GeometryBuilder()` | constructor | `None` | public | — |
| `set_geometry_type_to_build( GPlatesMaths::GeometryType::Value geom_type)` | method | `UndoOperation` | public | Specifies the type of geometry the user wants to build. |
| `clear_all_geometries()` | method | `UndoOperation` | public | Clears and removes all geometry(s). |
| `set_geometry( GPlatesMaths::GeometryType::Value geom_type, ForwardPointIter geom_points_begin, ForwardPointIter geom_points_end)` | method | `UndoOperation` | public | Sets the geometry and type. |
| `insert_point_into_current_geometry( PointIndex point_index, const GPlatesMaths::PointOnSphere &oriented_pos_on_globe)` | method | `UndoOperation` | public | Insert a point into the current geometry. |
| `remove_point_from_current_geometry( PointIndex point_index)` | method | `UndoOperation` | public | Remove a point from the current geometry. |
| `move_point_in_current_geometry( PointIndex point_index, const GPlatesMaths::PointOnSphere &new_oriented_pos_on_globe, std::vector<SecondaryGeometry> &secondary_geometries, std::vector<GPlatesMaths::PointOnSphere> &secondary_points, bool is_intermediate_move = false)` | method | `UndoOperation` | public | Moves a point in the current geometry. |
| `undo( UndoOperation &undo_operation)` | method | `void` | public | Undo a previous operation. |
| `has_geometry()` | method | `bool` | public | Returns true if there are any internal geometries in this builder. |
| `get_num_geometries()` | method | `unsigned int` | public | The number of internal geometries. |
| `get_geometry_build_type()` | method | `GPlatesMaths::GeometryType::Value` | public | The type of geometry we're trying to build. |
| `get_actual_type_of_current_geometry()` | method | `GPlatesMaths::GeometryType::Value` | public | The actual type of the geometry at the current geometry index. |
| `get_actual_type_of_geometry( GeometryIndex geom_index)` | method | `GPlatesMaths::GeometryType::Value` | public | The actual type of the geometry at the specified geometry index. |
| `get_current_geometry_index()` | method | `GeometryIndex` | public | The current geometry that operations are being directed at. |
| `get_num_points_in_current_geometry()` | method | `unsigned int` | public | Number of points/vertices in the current geometry. |
| `get_num_points_in_geometry( GeometryIndex geom_index)` | method | `unsigned int` | public | Number of points/vertices in the geometry at index geom\_index. |
| `get_geometry_point_begin( GeometryIndex geom_index)` | method | `point_const_iterator_type` | public | Begin iterator to GPlatesMaths::PointOnSphere points/vertices of geometry at index geom\_index. |
| `get_geometry_point_end( GeometryIndex geom_index)` | method | `point_const_iterator_type` | public | End iterator to GPlatesMaths::PointOnSphere points/vertices of geometry at index geom\_index. |
| `get_geometry_point` | field | `GPlatesMaths::PointOnSphere` | public | Returns point/vertex of geometry at index geom\_index and point at index point\_index within that geometry. |
| `get_geometry_on_sphere()` | method | `geometry_opt_ptr_type` | public | Returns geometry built or NULL if no geometries currently in this builder. |
| `visit_undo_operation( GeometryBuilderInternal::InsertPointUndoImpl &)` | method | `void` | public | Only GeometryBuilder implementation classes call these methods. |
| `visit_undo_operation( GeometryBuilderInternal::RemovePointUndoImpl &)` | method | `void` | public | — |
| `visit_undo_operation( GeometryBuilderInternal::MovePointUndoImpl &)` | method | `void` | public | — |
| `visit_undo_operation( GeometryBuilderInternal::SetGeometryTypeUndoImpl &)` | method | `void` | public | — |
| `visit_undo_operation( GeometryBuilderInternal::ClearAllGeometriesUndoImpl &)` | method | `void` | public | — |
| `visit_undo_operation( GeometryBuilderInternal::InsertGeometryUndoImpl &)` | method | `void` | public | — |
| `clear_secondary_geometries()` | method | `void` | public | — |
| `add_secondary_geometry( GPlatesAppLogic::ReconstructionGeometry::non_null_ptr_to_const_type rfg, unsigned int index_of_vertex)` | method | `void` | public | — |
| `num_secondary_geometries()` | method | `int` | public | — |
| `get_secondary_geometry()` | method | `geometry_opt_ptr_type` | public | Returns the first of any secondary geometries. |
| `get_secondary_rfg()` | method | `boost::optional<GPlatesAppLogic::ReconstructedFeatureGeometry::non_null_ptr_to_const_type>` | public | Returns the rfg of the first of any secondary geometries. |
| `get_secondary_vertex()` | method | `boost::optional<GPlatesMaths::PointOnSphere>` | public | Returns a point representing the vertex of the first of any secondary geometries |
| `get_secondary_index()` | method | `boost::optional<unsigned int>` | public | Returns the index of the vertex of the first of any secondary geometry |
| `started_updating_geometry()` | method | `void` | public | Geometry modifications have started. |
| `started_updating_geometry_excluding_intermediate_moves()` | method | `void` | public | Geometry modifications have started. |
| `stopped_updating_geometry()` | method | `void` | public | Geometry modifications have stopped. |
| `stopped_updating_geometry_excluding_intermediate_moves()` | method | `void` | public | Geometry modifications have stopped. |
| `changed_actual_geometry_type( GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index, GPlatesMaths::GeometryType::Value geometry_type)` | method | `void` | public | The actual type of geometry at geometry\_index has changed to geometry\_type. |
| `inserted_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index)` | method | `void` | public | Geometry was inserted at geometry\_index. |
| `removed_geometry( GPlatesViewOperations::GeometryBuilder::GeometryIndex geometry_index)` | method | `void` | public | Geometry was removed at geometry\_index. |
| `changed_current_geometry_index( GPlatesViewOperations::GeometryBuilder::GeometryIndex current_geometry_index)` | method | `void` | public | The current geometry index, at which all operations are currently directed, has changed to current\_geometry\_index. |
| `inserted_point_into_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex point_index, const GPlatesMaths::PointOnSphere &inserted_point)` | method | `void` | public | The point inserted\_point was inserted into the current geometry at index point\_index. |
| `removed_point_from_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex point_index)` | method | `void` | public | The point at index point\_index was removed from the current geometry. |
| `moved_point_in_current_geometry( GPlatesViewOperations::GeometryBuilder::PointIndex point_index, const GPlatesMaths::PointOnSphere &new_point_position, bool is_intermediate_move)` | method | `void` | public | The point at index point\_index was removed from the current geometry. |
| `UpdateGuard` | struct | `None` | private | Convenience structure for ensuring matching begin/end\_update\_geometry calls. |
| `geometry_builder_ptr_type` | typedef | `boost::shared_ptr<InternalGeometryBuilder>` | private | Typedef for pointer to InternalGeometryBuilder. |
| `geometry_builder_seq_type` | typedef | `std::vector<geometry_builder_ptr_type>` | private | Typedef for sequence of InternalGeometryBuilder pointers. |
| `undo_operation_seq_type` | typedef | `std::vector<UndoOperation>` | private | Typedef for a sequence of UndoOperation objects. |
| `d_geometry_build_type` | field | `GPlatesMaths::GeometryType::Value` | private | Value of geometry we're trying to build. |
| `d_geometry_builder_seq` | field | `geometry_builder_seq_type` | private | Sequence of geometries. |
| `d_current_geometry_index` | field | `GeometryIndex` | private | Index of geometry that's currently being edited/built. |
| `d_update_geometry_depth` | field | `int` | private | Used by begin\_update\_geometry and end\_update\_geometry to keep track of the nested call depth. |
| `DEFAULT_GEOMETRY_INDEX` | field | `GeometryIndex` | private | — |
| `d_secondary_geometries` | field | `std::vector<SecondaryGeometry>` | private | — |
| `begin_update_geometry( bool is_intermedate_move)` | method | `void` | private | — |
| `end_update_geometry( bool is_intermedate_move)` | method | `void` | private | — |
| `get_current_geometry_builder` | field | `InternalGeometryBuilder` | private | — |
| `insert_geometry( GeometryIndex, ForwardPointIter geom_points_begin, ForwardPointIter geom_points_end)` | method | `UndoOperation` | private | — |
| `insert_geometry( GeometryIndex)` | method | `UndoOperation` | private | — |
| `insert_geometry( geometry_builder_ptr_type geometry_ptr, GeometryIndex geom_index)` | method | `UndoOperation` | private | — |
| `remove_geometry( GeometryIndex)` | method | `void` | private | — |
| `create_composite_undo_operation( undo_operation_seq_type undo_operations)` | method | `UndoOperation` | private | Combines multiple undo operations into one. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `fill_secondary_points( std::vector<GPlatesMaths::PointOnSphere> &secondary_points, const std::vector<GPlatesViewOperations::SecondaryGeometry> &secondary_geometries)` | function | `void` | — |
| `move_secondary_geometry_vertices( std::vector<GPlatesViewOperations::SecondaryGeometry> &secondary_geometries, std::vector<GPlatesMaths::PointOnSphere> &secondary_points)` | function | `void` | — |
| `GPLATES_VIEWOPERATIONS_GEOMETRYBUILDER_H` | macro | `None` | — |

## Notes

- **Signal bracketing.** Every public mutator opens an `UpdateGuard` on entry.
  The guard increments `d_update_geometry_depth`; `started_updating_geometry` is
  emitted only on the transition to depth 1 and `stopped_updating_geometry` only
  on the return to depth 0, so a nested call such as `set_geometry` (which itself
  calls `clear_all_geometries`, `set_geometry_type_to_build` and
  `insert_geometry`) produces exactly one begin/end pair. The dirty
  `InternalGeometryBuilder`s are only `update()`d, and
  `changed_actual_geometry_type` only emitted, in the outermost
  `end_update_geometry`. Any new mutator must open an `UpdateGuard` or observers
  will see point-level signals with no enclosing update bracket.
- **Intermediate moves.** The `*_excluding_intermediate_moves` signal pair exists
  purely as a volume control: `move_point_in_current_geometry` with
  `is_intermediate_move == true` (mouse still down) suppresses them. Expensive
  observers — table rebuilds, model writes — should connect to those, not to the
  plain pair, or dragging a vertex will re-run them per mouse sample.
- **Undo mementos are single-use.** `undo()` calls `reset()` on the client's
  `shared_ptr` after replaying it, so passing the same `UndoOperation` to `undo()`
  twice asserts. The nested `visit_undo_operation` handlers deliberately discard
  the `UndoOperation` returned by the inverse call, so undo does not build a redo
  memento; redo in `GeometryBuilderUndoCommands` works by re-issuing the original
  operation, not by inverting the undo.
- **Constructor emits nothing on purpose.** Signals are not yet connected at
  construction time, so no state set in the constructor may go through a
  signalling path.
- **Single-geometry invariant.** `d_geometry_builder_seq` never holds more than
  one entry in the current code; `get_geometry_on_sphere` asserts that.
  `d_current_geometry_index` is held at zero even when the sequence is empty, so
  that adding a point simply recreates geometry 0. The multi-geometry indexing in
  the interface is anticipatory.
- **Threading.** A `QObject` used only on the GUI thread with direct connections;
  observers run inside the mutator that emitted the signal, so re-entrant calls
  back into the builder from a slot land inside the same `UpdateGuard` scope.
- **Error handling is assertion-based, and the documentation understates it.**
  Several methods documented as throwing `PreconditionViolationError` actually
  raise `AssertionFailureException` (`insert_point_into_current_geometry`,
  `remove_point_from_current_geometry`, `move_point_in_current_geometry`,
  `get_current_geometry_builder`). `UpdateGuard::~UpdateGuard` swallows every
  exception from `end_update_geometry`, so a throwing observer slot silently
  aborts the rest of the end-of-update processing.
- **Known rough edges.** `get_actual_type_of_geometry` range-checks its
  `geom_index` argument and then reads `get_current_geometry_builder()` instead of
  that index — harmless only while there is at most one geometry.
  `move_point_in_current_geometry` asserts `point_index <= size()` where the
  remove path correctly asserts `<`. In the file-local
  `move_secondary_geometry_vertices`, the `secondary_points` iterator is never
  advanced, so with more than one secondary geometry every one is moved to the
  same point; and `fill_secondary_points` only appends when a vertex was found,
  so the two vectors are not guaranteed to stay index-aligned. `GeometryUpdater`
  rebuilds polygons from the exterior ring only, discarding interior rings, and
  its point case replaces the position regardless of the vertex index.
- **Silent no-op.** `add_secondary_geometry` takes a
  `ReconstructionGeometry` and does nothing at all if it does not down-cast to a
  `ReconstructedFeatureGeometry`.

## Used by

| Unit | Component | References |
|---|---|---|
| [view-operations/InsertVertexGeometryOperation](InsertVertexGeometryOperation.md) | view-operations | 93 |
| [view-operations/GeometryBuilderUndoCommands](GeometryBuilderUndoCommands.md) | view-operations | 76 |
| [view-operations/SplitFeatureGeometryOperation](SplitFeatureGeometryOperation.md) | view-operations | 75 |
| [view-operations/MoveVertexGeometryOperation](MoveVertexGeometryOperation.md) | view-operations | 67 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 65 |
| [view-operations/DeleteVertexGeometryOperation](DeleteVertexGeometryOperation.md) | view-operations | 39 |
| [view-operations/GeometryOperation](GeometryOperation.md) | view-operations | 33 |
| [view-operations/AddPointGeometryOperation](AddPointGeometryOperation.md) | view-operations | 31 |
| [canvas-tools/MeasureDistance](../canvas-tools/MeasureDistance.md) | canvas-tools | 26 |
| [canvas-tools/MeasureDistanceState](../canvas-tools/MeasureDistanceState.md) | canvas-tools | 13 |
| [view-operations/FocusedFeatureGeometryManipulator](FocusedFeatureGeometryManipulator.md) | view-operations | 10 |
| [view-operations/CloneOperation](CloneOperation.md) | view-operations | 9 |
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 6 |
| [view-operations/SplitFeatureUndoCommand](SplitFeatureUndoCommand.md) | view-operations | 6 |
| [opengl/GLReconstructedStaticPolygonMeshes](../opengl/GLReconstructedStaticPolygonMeshes.md) | opengl | 5 |
| [view-operations/GeometryOperationUndo](GeometryOperationUndo.md) | view-operations | 5 |
| [gui/DigitisationCanvasToolWorkflow](../gui/DigitisationCanvasToolWorkflow.md) | gui | 4 |
| [gui/FeatureInspectionCanvasToolWorkflow](../gui/FeatureInspectionCanvasToolWorkflow.md) | gui | 4 |
| [qt-widgets/KinematicGraphsDialog](../qt-widgets/KinematicGraphsDialog.md) | qt-widgets | 3 |
| [canvas-tools/DigitiseGeometry](../canvas-tools/DigitiseGeometry.md) | canvas-tools | 1 |

*... and 2 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/view-operations/GeometryBuilder.h
python scripts/gpq.py def GPlatesViewOperations::GeometryBuilder --body
python scripts/gpq.py uses GeometryBuilder --kind class
python scripts/gpq.py hier GeometryBuilder
```
