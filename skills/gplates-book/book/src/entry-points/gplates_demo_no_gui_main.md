# gplates_demo_no_gui_main

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 743 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gplates_demo_no_gui_main.cc` | C++ | 606 |

## Overview

[[[PROSE overview unit=entry-points/gplates_demo_no_gui_main tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `create_isochron( GPlatesModel::ModelInterface &model, GPlatesModel::FeatureCollectionHandle::weak_ref &target_collection, const unsigned long &plate_id, const double *coords, unsigned num_coords, const GPlatesPropertyValues::GeoTimeInstant &geo_time_instant_begin, const GPlatesPropertyValues::GeoTimeInstant &geo_time_i ...` | function | `GPlatesModel::FeatureHandle::weak_ref` | — |
| `traverse_recon_tree_recursive( const GPlatesAppLogic::ReconstructionTree::Edge &edge)` | function | `void` | — |
| `traverse_recon_tree( const GPlatesAppLogic::ReconstructionTree &recon_tree)` | function | `void` | — |
| `populate_feature_store( GPlatesModel::ModelInterface &model)` | function | `std::pair<GPlatesModel::FeatureCollectionHandle::weak_ref, GPlatesModel::FeatureCollectionHandle::weak_ref>` | — |
| `output_as_gpml( const GPlatesModel::FeatureCollectionHandle::weak_ref &features)` | function | `void` | — |
| `output_reconstructions( GPlatesModel::FeatureCollectionHandle::weak_ref isochrons, GPlatesModel::FeatureCollectionHandle::weak_ref total_recon_seqs)` | function | `void` | — |
| `main(int argc, char *argv[])` | function | `int` | — |

## Notes

[[[PROSE notes unit=entry-points/gplates_demo_no_gui_main tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gplates_demo_no_gui_main.cc
```
