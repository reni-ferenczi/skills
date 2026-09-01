# FeatureId

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 138 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/FeatureId.h` | C++ | 69 |

## Overview

`FeatureId` is the persistent, string-based identifier that lets one feature
reference another — for example a `GpmlFeatureReference` or
`GpmlPropertyDelegate` pointing at the `FeatureHandle` it targets. It is not a
class of its own but a typedef, `IdTypeGenerator<FeatureIdFactory, FeatureHandle>`:
`IdTypeGenerator` supplies the actual ID machinery (unique-string storage,
comparison, and an optional back-reference to the defining `FeatureHandle`), and
`FeatureIdFactory` supplies the process-wide `GPlatesUtils::IdStringSet` — reached
through `StringSetSingletons::feature_id_instance()` — that all `FeatureId`
strings are interned into. `FeatureIdFactory` itself is uninstantiable (its
constructor is private); it exists purely to give `IdTypeGenerator` a distinct
singleton to key off, so feature IDs and other ID kinds (built the same way from
different factories) do not collide in the same string set.

Because IDs are meant to double as XML IDs, feature ID strings must conform to
the XML `NCName` production, per the class comment's cited W3C references. The
header itself only wires the typedef together; the ID comparison and
back-reference behaviour live in `IdTypeGenerator`.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureIdFactory`](#gplatesmodelfeatureidfactory) | class | — | — | 0 | A feature ID acts as a persistent unique identifier for a feature. |
| [`GPlatesModel::FeatureId`](#gplatesmodelfeatureid) | typedef | — | — | 0 | — |

## Members

### `GPlatesModel::FeatureIdFactory`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `FeatureIdFactory()` | constructor | `None` | private | — |

### `GPlatesModel::FeatureId`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_FEATUREID_H` | macro | `None` | — |

## Notes

- Uniqueness is "reasonably unique" only, per the class comment — `FeatureId`
  values are not guaranteed globally unique, just interned so equal strings
  compare equal cheaply.
- A `FeatureId` string must be a valid XML `NCName`; constructing one from an
  arbitrary string can violate that if the caller does not check it.

## Used by

| Unit | Component | References |
|---|---|---|
| [model/FeatureHandle](FeatureHandle.md) | model | 13 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 12 |
| [gui/TopologySectionsContainer](../gui/TopologySectionsContainer.md) | gui | 11 |
| [app-logic/TopologyGeometryResolverLayerProxy](../app-logic/TopologyGeometryResolverLayerProxy.md) | app-logic | 10 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 9 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 9 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 7 |
| [property-values/GpmlFeatureReference](../property-values/GpmlFeatureReference.md) | property-values | 7 |
| [app-logic/ReconstructLayerProxy](../app-logic/ReconstructLayerProxy.md) | app-logic | 6 |
| [app-logic/ApplicationState](../app-logic/ApplicationState.md) | app-logic | 5 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 5 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 5 |
| [presentation/ReconstructionGeometryRenderer](../presentation/ReconstructionGeometryRenderer.md) | presentation | 5 |
| [property-values/GpmlFeatureSnapshotReference](../property-values/GpmlFeatureSnapshotReference.md) | property-values | 5 |
| [property-values/GpmlPropertyDelegate](../property-values/GpmlPropertyDelegate.md) | property-values | 5 |
| [app-logic/ReconstructContext](../app-logic/ReconstructContext.md) | app-logic | 4 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 4 |
| [model/ModelUtils](ModelUtils.md) | model | 4 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 3 |
| [app-logic/DependentTopologicalSectionLayers](../app-logic/DependentTopologicalSectionLayers.md) | app-logic | 3 |

*... and 13 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/FeatureId.h
python scripts/gpq.py def GPlatesModel::FeatureIdFactory --body
python scripts/gpq.py uses FeatureIdFactory --kind class
python scripts/gpq.py hier FeatureIdFactory
```
