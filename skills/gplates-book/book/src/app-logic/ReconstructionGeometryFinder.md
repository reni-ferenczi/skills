# ReconstructionGeometryFinder

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 736 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGeometryFinder.h` | C++ | 198 |
| `src/app-logic/ReconstructionGeometryFinder.cc` | C++ | 155 |

## Overview

`ReconstructionGeometryFinder` walks the weak-observer list attached to a `GPlatesModel::FeatureHandle` and collects every `ReconstructionGeometry` currently observing it — the reverse lookup from a feature to the `ReconstructedFeatureGeometry`, `ResolvedTopologicalGeometry` and `ResolvedTopologicalNetwork` instances that were derived from it. Because a feature can be reconstructed many times (once per property, once per reconstruction, or across successive `reconstruct()` calls whose stale results have not yet been discarded), the three constructors let a caller narrow the search: to RGs built from one property (`GPlatesModel::PropertyName`), to the RG built from one specific property iterator (at most one match, since a `FeatureHandle::iterator` names a single property), or to RGs carrying a reconstruct handle from a given `ReconstructHandle::type` set — the last of these is how a caller restricts results to the most recent reconstruction pass rather than picking up stale RGs left over from an earlier one.

The visitor dispatches all three RG kinds through a single private template, `visit_reconstruction_geometry_derived_type`, which applies the property-name, properties-iterator and reconstruct-handle filters in sequence before appending the geometry to `d_found_rgs`. The free functions in the anonymous namespace of the `.cc` (`property_name_matches`, `properties_iterator_matches`, `reconstruct_handle_matches`) implement those three filters and are templated or overloaded purely to work uniformly across the three RG-derived types.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructionGeometryFinder`](#gplatesapplogicreconstructiongeometryfinder) | class | [`GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle>`](../model/WeakObserverVisitor.md) | — | 0 | This weak observer visitor finds all the reconstruction geometries (RGs) which are observing a given feature (eg, ReconstructedFeatureGeometry and ResolvedTopologicalGeometry). |

## Members

### `GPlatesAppLogic::ReconstructionGeometryFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `rg_container_type` | typedef | `std::vector<ReconstructionGeometry::non_null_ptr_type>` | public | — |
| `const_iterator` | typedef | `rg_container_type::const_iterator` | public | — |
| `ReconstructionGeometryFinder( boost::optional<const std::vector<ReconstructHandle::type> &> reconstruct_handles_to_match = boost::none)` | constructor | `None` | public | Constructor. |
| `ReconstructionGeometryFinder( const GPlatesModel::PropertyName &property_name_to_match, boost::optional<const std::vector<ReconstructHandle::type> &> reconstruct_handles_to_match = boost::none)` | constructor | `None` | public | Constructor. |
| `ReconstructionGeometryFinder( const GPlatesModel::FeatureHandle::iterator &properties_iterator_to_match, boost::optional<const std::vector<ReconstructHandle::type> &> reconstruct_handles_to_match = boost::none)` | constructor | `None` | public | Constructor. |
| `~ReconstructionGeometryFinder()` | destructor | `None` | public | Destructor. |
| `num_rgs_found()` | method | `rg_container_type::size_type` | public | — |
| `found_rgs_begin()` | method | `const_iterator` | public | — |
| `found_rgs_end()` | method | `const_iterator` | public | — |
| `find_rgs_of_feature( GPlatesModel::FeatureHandle::weak_ref ref)` | method | `void` | public | Find the RGs of the feature referenced by ref. |
| `find_rgs_of_feature( GPlatesModel::FeatureHandle *ptr)` | method | `void` | public | Find the RGs of the feature pointed-to by ptr. |
| `clear_found_rgs()` | method | `void` | public | — |
| `visit_reconstructed_feature_geometry( ReconstructedFeatureGeometry &rfg)` | method | `void` | protected | Handles ReconstructedFeatureGeometry and its derived classes. |
| `visit_resolved_topological_geometry( ResolvedTopologicalGeometry &rtg)` | method | `void` | protected | — |
| `visit_resolved_topological_network( ResolvedTopologicalNetwork &rtn)` | method | `void` | protected | — |
| `d_property_name_to_match` | field | `boost::optional<GPlatesModel::PropertyName>` | private | — |
| `d_properties_iterator_to_match` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `d_reconstruct_handles_to_match` | field | `boost::optional<std::vector<ReconstructHandle::type> >` | private | — |
| `d_found_rgs` | field | `rg_container_type` | private | — |
| `visit_reconstruction_geometry_derived_type( ReconstructionGeometryDerivedType &recon_geom_derived_obj)` | method | `void` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `property_name_matches( const ReconstructionGeometryDerivedType &rg, const GPlatesModel::PropertyName &property_name_to_match)` | function | `bool` | — |
| `properties_iterator_matches( const ReconstructionGeometryDerivedType &rg, const GPlatesModel::FeatureHandle::iterator &properties_iterator_to_match)` | function | `bool` | — |
| `reconstruct_handle_matches( const GPlatesAppLogic::ReconstructionGeometry &rg, const std::vector<GPlatesAppLogic::ReconstructHandle::type> &reconstruct_handles_to_match)` | function | `bool` | Returns true if the reconstruct handle of rg matches any of the handles in reconstruct\_handles\_to\_match. |
| `GPLATES_APP_LOGIC_RECONSTRUCTIONGEOMETRYFINDER_H` | macro | `None` | — |

## Notes

- `property_name_to_match` and `properties_iterator_to_match` are mutually exclusive in practice: only one constructor sets either, never both, though the class does not enforce this.
- `find_rgs_of_feature` is a no-op on an invalid `weak_ref` or a null pointer rather than asserting — callers do not need to check validity first.
- The finder accumulates into `d_found_rgs` across repeated calls; call `clear_found_rgs()` between searches if reusing the same instance.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 18 |
| [app-logic/ReconstructionGeometryUtils](ReconstructionGeometryUtils.md) | app-logic | 10 |
| [gui/FeatureFocus](../gui/FeatureFocus.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructionGeometryFinder.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructionGeometryFinder --body
python scripts/gpq.py uses ReconstructionGeometryFinder --kind class
python scripts/gpq.py hier ReconstructionGeometryFinder
```
