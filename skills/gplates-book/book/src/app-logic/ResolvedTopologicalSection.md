# ResolvedTopologicalSection

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1417 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/ResolvedTopologicalSection.h` | C++ | 133 |

## Overview

`ResolvedTopologicalSection` groups, per topological-section feature, every
`ResolvedTopologicalSharedSubSegment` derived from it across all the
topologies (`ResolvedTopologicalBoundary` and `ResolvedTopologicalNetwork`)
that reuse that section as part of their boundary. It exists because
multiple resolved topologies can share the same section feature — a plate
boundary segment shared by two adjacent plates, for example — and callers
such as export code want to enumerate contributions per section feature
rather than per resolved topology.

The class is a thin, immutable aggregate: the source feature's reconstruction
geometry (a reconstructed feature geometry or a `ResolvedTopologicalLine`),
a weak reference to the section feature itself, and the sequence of shared
sub-segments contributed by it, all fixed at construction via the templated
`create()` factory.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::ResolvedTopologicalSection`](#gplatesapplogicresolvedtopologicalsection) | class | [`GPlatesUtils::ReferenceCount<ResolvedTopologicalSection>`](../utils/ReferenceCount.md) | — | 0 | A sequence of all sub-segments of a topological section feature used as part of the \*boundary\* of resolved topologies (ResolvedTopologicalBoundary and ResolvedTopologicalNetwork). |

## Members

### `GPlatesAppLogic::ResolvedTopologicalSection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<ResolvedTopologicalSection>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const ResolvedTopologicalSection>` | public | — |
| `create( ResolvedTopologicalSharedSubSegmentIter shared_sub_segments_begin, ResolvedTopologicalSharedSubSegmentIter shared_sub_segments_end, const ReconstructionGeometry::non_null_ptr_to_const_type &topological_section_reconstruction_geometry, const GPlatesModel::FeatureHandle::const_weak_ref &topological_section_featur ...` | method | `non_null_ptr_type` | public | — |
| `d_shared_sub_segments` | field | `shared_sub_segment_seq_type` | private | The shared sub-segments that reference the ReconstructionGeometry of this topological section. |
| `d_topological_section_reconstruction_geometry` | field | `ReconstructionGeometry::non_null_ptr_to_const_type` | private | The reconstruction geometry of the topological section feature. |
| `d_topological_section_feature_ref` | field | `GPlatesModel::FeatureHandle::const_weak_ref` | private | Reference to the source feature handle of the topological section. |
| `ResolvedTopologicalSection( ResolvedTopologicalSharedSubSegmentIter shared_sub_segments_begin, ResolvedTopologicalSharedSubSegmentIter shared_sub_segments_end, const ReconstructionGeometry::non_null_ptr_to_const_type &topological_section_reconstruction_geometry, const GPlatesModel::FeatureHandle::const_weak_ref &topolo ...` | constructor | `None` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALSECTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ResolvedTopologicalGeometryExport](../file-io/ResolvedTopologicalGeometryExport.md) | file-io | 9 |
| [app-logic/TopologyUtils](TopologyUtils.md) | app-logic | 6 |
| [app-logic/Reconstruction](Reconstruction.md) | app-logic | 5 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 4 |
| [view-operations/VisibleReconstructionGeometryExport](../view-operations/VisibleReconstructionGeometryExport.md) | view-operations | 4 |
| [app-logic/LayerProxyUtils](LayerProxyUtils.md) | app-logic | 3 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](../file-io/OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 3 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/ResolvedTopologicalSection.h
python scripts/gpq.py def GPlatesAppLogic::ResolvedTopologicalSection --body
python scripts/gpq.py uses ResolvedTopologicalSection --kind class
python scripts/gpq.py hier ResolvedTopologicalSection
```
