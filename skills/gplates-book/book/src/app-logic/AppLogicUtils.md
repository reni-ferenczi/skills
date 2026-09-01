# AppLogicUtils

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 7 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/AppLogicUtils.h` | C++ | 170 |
| `src/app-logic/AppLogicUtils.cc` | C++ | 90 |

## Overview

[[[PROSE overview unit=app-logic/AppLogicUtils tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=app-logic/AppLogicUtils tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
