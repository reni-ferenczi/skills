# AppLogicUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 7 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/AppLogicUtils.h` | C++ | 170 |
| `src/app-logic/AppLogicUtils.cc` | C++ | 90 |

## Overview

The single adapter between the model's containers and the model's visitor
protocol. `GPlatesModel::FeatureVisitorBase` knows how to visit *one* feature —
`visit_feature` takes either a weak-ref or a feature-collection iterator, checks
that it still resolves, and dispatches into `visit_feature_handle`. It has no
notion of a collection, and `GPlatesModel::FeatureCollectionHandle` has no notion
of a visitor. Everything in app-logic that wants "run this visitor over these
features" would otherwise write the same three-line loop plus the same validity
check, so that loop lives here instead, in a namespace of free functions with no
state of its own.

That is why the fan-in is so wide and so flat. The layer tasks
(`ReconstructLayerTask`, `TopologyGeometryResolverLayerTask`,
`VelocityFieldCalculatorLayerTask` and their peers) call
`visit_feature_collection` to run a `FeatureVisitor` subclass over the collections
wired into a layer; the `file-io` exporters and the `gui` export-animation
strategies call it to walk the collections they are about to write out;
`FeatureCollectionFileFormatClassify` calls it to decide what a just-loaded file
contains. Each caller supplies the interesting part — the visitor — and this unit
supplies only the traversal.

The three `visit_feature_collection` overloads exist to cover the const/non-const
cross product that the model's weak-ref types would otherwise force on callers.
The third one, taking a mutable `weak_ref` but a `ConstFeatureVisitor`, converts
to a `const_weak_ref` internally, so a caller holding a writable collection can
still hand it to a read-only visitor without a cast at the call site. The
`visit_features` and `visit_feature_collections` templates are the range forms,
parameterised on the iterator rather than the container so they work over any
sequence of weak-refs — a `std::vector`, a layer's input list — and are const-agnostic
for the same reason.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_APPLOGICUTILS_H` | macro | `None` | — |
| `visit_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, GPlatesModel::FeatureVisitor &visitor)` | function | `void` | A convenience function for iterating over a the features in a GPlatesModel::FeatureCollectionHandle::weak\_ref and visiting them with a GPlatesModel::FeatureVisitor. |
| `visit_feature_collection( const GPlatesModel::FeatureCollectionHandle::const_weak_ref &feature_collection, GPlatesModel::ConstFeatureVisitor &visitor)` | function | `void` | A convenience function for iterating over a the features in a GPlatesModel::FeatureCollectionHandle::const\_weak\_ref and visiting them with a GPlatesModel::ConstFeatureVisitor. |
| `visit_feature_collection( const GPlatesModel::FeatureCollectionHandle::weak_ref &feature_collection, GPlatesModel::ConstFeatureVisitor &visitor)` | function | `void` | A convenience function for iterating over a the features in a GPlatesModel::FeatureCollectionHandle::weak\_ref and visiting them with a GPlatesModel::ConstFeatureVisitor. |
| `visit_features( FeatureWeakRefIterator features_begin, FeatureWeakRefIterator features_end, GPlatesModel::FeatureVisitor &visitor)` | function | `void` | A convenience function for iterating over a sequence of GPlatesModel::FeatureHandle::weak\_ref visiting them with a GPlatesModel::FeatureVisitor. |
| `visit_features( FeatureWeakRefIterator features_begin, FeatureWeakRefIterator features_end, GPlatesModel::ConstFeatureVisitor &visitor)` | function | `void` | A convenience function for iterating over a sequence of GPlatesModel::FeatureHandle::weak\_ref or GPlatesModel::FeatureHandle::const\_weak\_ref objects and visiting them with a GPlatesModel::ConstFeatureVisitor. |
| `visit_feature_collections( FeatureCollectionWeakRefIterator collections_begin, FeatureCollectionWeakRefIterator collections_end, GPlatesModel::FeatureVisitor &visitor)` | function | `void` | A convenience function for iterating over a sequence of GPlatesModel::FeatureCollectionHandle::weak\_ref objects and visiting them with a GPlatesModel::FeatureVisitor. |
| `visit_feature_collections( FeatureCollectionWeakRefIterator collections_begin, FeatureCollectionWeakRefIterator collections_end, GPlatesModel::ConstFeatureVisitor &visitor)` | function | `void` | A convenience function for iterating over a sequence of GPlatesModel::FeatureCollectionHandle::weak\_ref or GPlatesModel::FeatureCollectionHandle::const\_weak\_ref objects and visiting them with a GPlatesModel::ConstFeatureVisitor. |

## Notes

**Invalid input is silently a no-op.** Every entry point tolerates a dead
weak-ref: `visit_feature_collection` tests `is_valid()` before dereferencing and
just returns if it fails, and `visit_feature` returns `false` for a stale
iterator, a result these helpers discard. So a caller cannot distinguish "the
collection was unloaded" from "the collection was empty" — nothing is thrown and
nothing is returned. If you need that distinction, check the weak-ref yourself
before calling.

**The collection must not grow while the visitor runs.** `visit_feature_collection`
captures `begin()` and `end()` once, before the loop, and
`GPlatesModel::RevisionAwareIterator` is an index into the current revision.
Features appended by the visitor sit past the captured `end` and are not visited;
features removed by the visitor leave a hole that `is_still_valid()` detects, so
`visit_feature` skips them rather than crashing. Mutating visitors that only edit
property values in place are fine; ones that add or remove features from the
collection they are walking are not.

**No ownership, no state.** These are free functions over borrowed references —
nothing here extends the lifetime of a collection, a feature or a visitor, and
the visitor's own accumulated state is the caller's problem. Re-entrancy and
threading are likewise entirely the visitor's business; there is nothing shared
in this unit to protect.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyInternalUtils](TopologyInternalUtils.md) | app-logic | 43 |
| [app-logic/FlowlineUtils](FlowlineUtils.md) | app-logic | 31 |
| [app-logic/ReconstructLayerTask](ReconstructLayerTask.md) | app-logic | 20 |
| [app-logic/ReconstructUtils](ReconstructUtils.md) | app-logic | 20 |
| [app-logic/TopologyNetworkResolverLayerTask](TopologyNetworkResolverLayerTask.md) | app-logic | 18 |
| [app-logic/VelocityFieldCalculatorLayerTask](VelocityFieldCalculatorLayerTask.md) | app-logic | 18 |
| [gui/ExportCitcomsResolvedTopologyAnimationStrategy](../gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) | gui | 18 |
| [app-logic/TopologyGeometryResolverLayerTask](TopologyGeometryResolverLayerTask.md) | app-logic | 17 |
| [file-io/FeatureCollectionFileFormatRegistry](../file-io/FeatureCollectionFileFormatRegistry.md) | file-io | 17 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 17 |
| [app-logic/ReconstructScalarCoverageLayerTask](ReconstructScalarCoverageLayerTask.md) | app-logic | 16 |
| [gui/ExportVelocityAnimationStrategy](../gui/ExportVelocityAnimationStrategy.md) | gui | 16 |
| [gui/ExportScalarCoverageAnimationStrategy](../gui/ExportScalarCoverageAnimationStrategy.md) | gui | 15 |
| [app-logic/CoRegistrationLayerTask](CoRegistrationLayerTask.md) | app-logic | 14 |
| [file-io/FeatureCollectionFileFormatClassify](../file-io/FeatureCollectionFileFormatClassify.md) | file-io | 14 |
| [gui/ExportDeformationAnimationStrategy](../gui/ExportDeformationAnimationStrategy.md) | gui | 14 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 13 |
| [app-logic/deprecated/PaleomagUtils](deprecated/PaleomagUtils.md) | app-logic | 12 |
| [app-logic/deprecated/PaleomagWorkflow](deprecated/PaleomagWorkflow.md) | app-logic | 11 |
| [gui/ExportFlowlineAnimationStrategy](../gui/ExportFlowlineAnimationStrategy.md) | gui | 11 |

*... and 9 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/AppLogicUtils.h
```
