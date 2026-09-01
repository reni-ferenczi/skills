# ReconstructedFeatureGeometryFinder

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 735 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ReconstructedFeatureGeometryFinder.h` | C++ | 199 |
| `src/app-logic/ReconstructedFeatureGeometryFinder.cc` | C++ | 151 |

## Overview

`ReconstructedFeatureGeometryFinder` walks the weak observers of a `GPlatesModel::FeatureHandle` to collect the `ReconstructedFeatureGeometry` instances currently observing that feature. Since RFGs are produced fresh by each reconstruction pass and only weakly reference the feature they came from, this finder is the standard way to go from a feature back to its most recent reconstructed geometries, rather than every caller re-deriving that link by hand.

Each constructor narrows the search: by the `ReconstructionTree` the RFG must have been reconstructed with, by the `GPlatesModel::PropertyName` of the source geometry property, or by a specific `GPlatesModel::FeatureHandle::iterator` (which can match at most one RFG). The `reconstruct_handles_to_match` parameter further restricts results to RFGs produced by one of a given set of `ReconstructHandle` values, letting a caller isolate the output of one particular reconstruction call.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ReconstructedFeatureGeometryFinder`](#gplatesapplogicreconstructedfeaturegeometryfinder) | class | [`GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureHandle>`](../model/WeakObserverVisitor.md) | — | 0 | This weak observer visitor finds all the reconstructed feature geometries (RFGs) which are observing a given feature. |

## Members

### `GPlatesAppLogic::ReconstructedFeatureGeometryFinder`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `rfg_container_type` | typedef | `std::vector< GPlatesGlobal::PointerTraits<ReconstructedFeatureGeometry>::non_null_ptr_type>` | public | — |
| `const_iterator` | typedef | `rfg_container_type::const_iterator` | public | — |
| `ReconstructedFeatureGeometryFinder( boost::optional<ReconstructionTree::non_null_ptr_to_const_type> reconstruction_tree_to_match = boost::none, boost::optional<const std::vector<ReconstructHandle::type> &> reconstruct_handles_to_match = boost::none)` | constructor | `None` | public | Constructor. |
| `ReconstructedFeatureGeometryFinder( const GPlatesModel::PropertyName &property_name_to_match, boost::optional<ReconstructionTree::non_null_ptr_to_const_type> reconstruction_tree_to_match = boost::none, boost::optional<const std::vector<ReconstructHandle::type> &> reconstruct_handles_to_match = boost::none)` | constructor | `None` | public | Constructor. |
| `ReconstructedFeatureGeometryFinder( const GPlatesModel::FeatureHandle::iterator &properties_iterator_to_match, boost::optional<ReconstructionTree::non_null_ptr_to_const_type> reconstruction_tree_to_match = boost::none, boost::optional<const std::vector<ReconstructHandle::type> &> reconstruct_handles_to_match = boost::n ...` | constructor | `None` | public | Constructor. |
| `~ReconstructedFeatureGeometryFinder()` | destructor | `None` | public | Destructor. |
| `num_rfgs_found()` | method | `rfg_container_type::size_type` | public | — |
| `found_rfgs_begin()` | method | `const_iterator` | public | — |
| `found_rfgs_end()` | method | `const_iterator` | public | — |
| `find_rfgs_of_feature( GPlatesModel::FeatureHandle::weak_ref ref)` | method | `void` | public | Find the RFGs of the feature referenced by ref. |
| `find_rfgs_of_feature( GPlatesModel::FeatureHandle *ptr)` | method | `void` | public | Find the RFGs of the feature pointed-to by ptr. |
| `clear_found_rfgs()` | method | `void` | public | — |
| `visit_reconstructed_feature_geometry( ReconstructedFeatureGeometry &rfg)` | method | `void` | protected | Handles ReconstructedFeatureGeometry and its derived classes. |
| `d_property_name_to_match` | field | `boost::optional<GPlatesModel::PropertyName>` | private | — |
| `d_properties_iterator_to_match` | field | `boost::optional<GPlatesModel::FeatureHandle::iterator>` | private | — |
| `d_reconstruction_tree_to_match` | field | `boost::optional<ReconstructionTree::non_null_ptr_to_const_type>` | private | — |
| `d_reconstruct_handles_to_match` | field | `boost::optional<std::vector<ReconstructHandle::type> >` | private | — |
| `d_found_rfgs` | field | `rfg_container_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `reconstruction_tree_matches( const GPlatesAppLogic::ReconstructedFeatureGeometry &rfg, const GPlatesAppLogic::ReconstructionTree::non_null_ptr_to_const_type &reconstruction_tree_to_match)` | function | `bool` | — |
| `property_name_matches( const GPlatesAppLogic::ReconstructedFeatureGeometry &rfg, const GPlatesModel::PropertyName &property_name_to_match)` | function | `bool` | — |
| `properties_iterator_matches( const GPlatesAppLogic::ReconstructedFeatureGeometry &rfg, const GPlatesModel::FeatureHandle::iterator &properties_iterator_to_match)` | function | `bool` | — |
| `reconstruct_handle_matches( const GPlatesAppLogic::ReconstructedFeatureGeometry &rfg, const std::vector<GPlatesAppLogic::ReconstructHandle::type> &reconstruct_handles_to_match)` | function | `bool` | Returns true if the reconstruct handle of rfg matches any of the handles in reconstruct\_handles\_to\_match. |
| `GPLATES_APP_LOGIC_RECONSTRUCTEDFEATUREGEOMETRYFINDER_H` | macro | `None` | — |

## Notes

Reconstruction-tree matching compares trees by `created_from_same_graph_with_same_parameters`, not by pointer or object equality: reconstruction-tree caches can evict and recreate an equivalent tree as a new instance, so pointer comparison would silently miss matches.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/GeometryUtils](GeometryUtils.md) | app-logic | 5 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 5 |
| [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) | feature-visitors | 3 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ReconstructedFeatureGeometryFinder.h
python scripts/gpq.py def GPlatesAppLogic::ReconstructedFeatureGeometryFinder --body
python scripts/gpq.py uses ReconstructedFeatureGeometryFinder --kind class
python scripts/gpq.py hier ReconstructedFeatureGeometryFinder
```
