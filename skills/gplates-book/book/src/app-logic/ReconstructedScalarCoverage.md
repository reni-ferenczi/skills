# ReconstructedScalarCoverage

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 636 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructedScalarCoverage.h` | C++ | 306 |
| `src/app-logic/ReconstructedScalarCoverage.cc` | C++ | 113 |

## Overview

`ReconstructedScalarCoverage` pairs a domain `ReconstructedFeatureGeometry` (the reconstructed, possibly deformed, points/polyline/polygon) with a range of per-point scalar values, whose evolution over time is delegated to a `ScalarCoverageTimeSpan`. It deliberately inherits from `ReconstructionGeometry` and `GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>` directly rather than from `ReconstructedFeatureGeometry`, because the domain geometry is already an RFG in its own right — making this class an RFG too would cause code that collects "all RFGs" (for example export) to see the domain geometry twice.

`get_reconstructed_points` dispatches on whether the domain geometry is actually a `TopologyReconstructedFeatureGeometry`: when it is, it asks that class directly for its reconstructed points (cheaper for large point counts than extracting them from the assembled geometry), and otherwise falls back to `GeometryUtils::get_geometry_exterior_points` on the plain reconstructed geometry. `get_reconstructed_point_scalar_values` and `get_reconstructed_points` are guaranteed to return values indexed the same way, one scalar per point.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructedScalarCoverage`](#gplatesapplogicreconstructedscalarcoverage) | class | [`ReconstructionGeometry`](ReconstructionGeometry.md)<br>[`GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>`](../model/WeakObserver.md) | — | 0 | A coverage of scalar values associated with points in a domain geometry. |

## Members

### `GPlatesAppLogic::ReconstructedScalarCoverage`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ReconstructedScalarCoverage>` | public | A convenience typedef for a non-null shared pointer to a non-const ReconstructedScalarCoverage. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ReconstructedScalarCoverage>` | public | A convenience typedef for a non-null shared pointer to a const ReconstructedScalarCoverage. |
| `WeakObserverType` | typedef | `GPlatesModel::WeakObserver<GPlatesModel::FeatureHandle>` | public | Typedef for the WeakObserver base class of this class. |
| `point_seq_type` | typedef | `std::vector<GPlatesMaths::PointOnSphere>` | public | Typedef for a sequence of points. |
| `point_scalar_value_seq_type` | typedef | `std::vector<double>` | public | Typedef for a sequence of per-geometry-point scalar values. |
| `create( const ReconstructedFeatureGeometry::non_null_ptr_type &reconstructed_domain_geometry, GPlatesModel::FeatureHandle::iterator range_property_iterator, const GPlatesPropertyValues::ValueObjectType &scalar_type, const ScalarCoverageTimeSpan::non_null_ptr_type &scalar_coverage_time_span, boost::optional<ReconstructH ...` | method | `non_null_ptr_type` | public | Create a ReconstructedScalarCoverage instance. |
| `get_reconstructed_feature_geometry()` | method | `ReconstructedFeatureGeometry::non_null_ptr_type` | public | Returns the domain reconstructed feature geometry. |
| `get_reconstructed_geometry()` | method | `GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type` | public | Returns the reconstructed domain geometry. |
| `get_reconstructed_points( point_seq_type &points)` | method | `void` | public | Returns the reconstructed geometry points. |
| `get_reconstructed_point_scalar_values( point_scalar_value_seq_type &scalar_values)` | method | `void` | public | Returns the per-geometry-point scalar values. |
| `get_domain_property()` | method | `GPlatesModel::FeatureHandle::iterator` | public | Access the feature property which contained the reconstructed domain geometry. |
| `get_range_property()` | method | `GPlatesModel::FeatureHandle::iterator` | public | Access the feature property from which the scalar values were reconstructed. |
| `get_non_null_pointer_to_const()` | method | `non_null_ptr_to_const_type` | public | Get a non-null pointer to const. |
| `get_non_null_pointer()` | method | `non_null_ptr_type` | public | Get a non-null pointer to non-const. |
| `references( const GPlatesModel::FeatureHandle &that_feature_handle)` | method | `bool` | public | Return whether this RG references that\_feature\_handle. |
| `feature_handle_ptr()` | method | `GPlatesModel::FeatureHandle` | public | Return the pointer to the FeatureHandle. |
| `is_valid()` | method | `bool` | public | Return whether this pointer is valid to be dereferenced (to obtain a FeatureHandle). |
| `get_feature_ref()` | method | `GPlatesModel::FeatureHandle::weak_ref` | public | Return a weak-ref to the \*domain\* feature used for the domain of the vector field. |
| `accept_visitor( ConstReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ConstReconstructionGeometryVisitor instance. |
| `accept_visitor( ReconstructionGeometryVisitor &visitor)` | method | `void` | public | Accept a ReconstructionGeometryVisitor instance. |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle> &visitor)` | method | `void` | public | Accept a WeakObserverVisitor instance. |
| `d_domain_reconstructed_feature_geometry` | field | `ReconstructedFeatureGeometry::non_null_ptr_type` | private | The domain reconstructed feature geometry. |
| `d_range_property_iterator` | field | `GPlatesModel::FeatureHandle::iterator` | private | The range property that the scalar values came from. |
| `d_scalar_type` | field | `GPlatesPropertyValues::ValueObjectType` | private | The type of the scalar values. |
| `d_scalar_coverage_time_span` | field | `ScalarCoverageTimeSpan::non_null_ptr_type` | private | Used to obtain the per-geometry-point scalar values when requested. |
| `ReconstructedScalarCoverage( const ReconstructedFeatureGeometry::non_null_ptr_type &reconstructed_domain_geometry, GPlatesModel::FeatureHandle::iterator range_property_iterator, const GPlatesPropertyValues::ValueObjectType &scalar_type, const ScalarCoverageTimeSpan::non_null_ptr_type &scalar_coverage_time_span, boost:: ...` | constructor | `None` | private | Instantiate a reconstructed scalar coverage. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RECONSTRUCTEDSCALARCOVERAGE_H` | macro | `None` | — |

## Notes

`get_reconstructed_point_scalar_values` asserts (`PreconditionViolationError`) that `d_scalar_coverage_time_span` has valid scalar values at the current reconstruction time; a coverage is expected never to be constructed for a time at which its scalar time span is invalid, so hitting this assertion indicates a bug in the caller that built the coverage, not a normal runtime condition to guard against.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructScalarCoverageLayerProxy](ReconstructScalarCoverageLayerProxy.md) | app-logic | 16 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 14 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 9 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 7 |
| [file-io/ReconstructedScalarCoverageExport](../file-io/ReconstructedScalarCoverageExport.md) | file-io | 5 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 5 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 5 |
| [presentation/LayerOutputRenderer](../presentation/LayerOutputRenderer.md) | presentation | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructedScalarCoverage.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructedScalarCoverage --body
python scripts/gpq.py uses ReconstructedScalarCoverage --kind class
python scripts/gpq.py hier ReconstructedScalarCoverage
```
