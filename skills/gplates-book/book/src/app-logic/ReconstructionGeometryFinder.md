# ReconstructionGeometryFinder

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 736 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructionGeometryFinder.h` | C++ | 198 |
| `src/app-logic/ReconstructionGeometryFinder.cc` | C++ | 155 |

## Overview

[[[PROSE overview unit=app-logic/ReconstructionGeometryFinder tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/ReconstructionGeometryFinder tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
