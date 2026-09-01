# CitcomsResolvedTopologicalBoundaryExportImpl

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 483 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/CitcomsResolvedTopologicalBoundaryExportImpl.h` | C++ | 156 |
| `src/file-io/CitcomsResolvedTopologicalBoundaryExportImpl.cc` | C++ | 461 |

## Overview

This unit supplies the data types and classification logic shared by the CitcomS resolved-topology exporters (`CitcomsResolvedTopologicalBoundaryExport` and its GMT/OGR format backends). `ResolvedTopology` pairs a resolved `ReconstructionGeometry` with a `ResolvedTopologyType` (plate, slab or network polygon); `SubSegment` pairs a `ResolvedTopologicalGeometrySubSegment` with a `SubSegmentType`; `SubSegmentGroup` bundles one `ResolvedTopology` with only the subset of its subsegments relevant to a given output file, since a single polygon's boundary is split across several export files (for example, ridge-transform boundaries versus left/right subduction boundaries).

`get_sub_segment_type` and `get_slab_sub_segment_type` classify a subsegment's source feature into a `SubSegmentType` (subduction zone left/right/unknown, or one of the slab-edge categories), and each is implemented as a `ConstFeatureVisitor` — `DetermineSubSegmentFeatureType` and `DetermineSlabSubSegmentFeatureType` respectively — because the polarity or feature-type information can be buried inside a time-dependent property value (`GpmlConstantValue`, `GpmlIrregularSampling`, `GpmlPiecewiseAggregation`) that must be evaluated at the given reconstruction time rather than read directly off the feature.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::DetermineSubSegmentFeatureType`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimpldeterminesubsegmentfeaturetype) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Determines feature type of subsegment source feature referenced by a resolved topological geometry at a specific reconstruction time. |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::DetermineSlabSubSegmentFeatureType`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimpldetermineslabsubsegmentfeaturetype) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | Determines feature type of subsegment source feature referenced by Slab Polygon at a specific reconstruction time. |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::SubSegmentType`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimplsubsegmenttype) | enum | — | — | 0 | Sub segment feature type. |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::ResolvedTopologyType`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimplresolvedtopologytype) | enum | — | — | 0 | Resolved topology feature type (plate/slab/network). |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::SubSegment`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimplsubsegment) | struct | — | — | 0 | A boundary subsegment and the subsegment type. |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::sub_segment_seq_type`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimplsub_segment_seq_type) | typedef | — | — | 0 | Typedef for a sequence of subsegments of resolved topological boundaries. |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::ResolvedTopology`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimplresolvedtopology) | struct | — | — | 0 | A resolved topology and its type (plate/slab/network). |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::resolved_topologies_seq_type`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimplresolved_topologies_seq_type) | typedef | — | — | 0 | Typedef for a sequence of resolved topologies. |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::SubSegmentGroup`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimplsubsegmentgroup) | struct | — | — | 0 | Groups a resolved topology with a subset of its boundary subsegments. |
| [`GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::sub_segment_group_seq_type`](#gplatesfileiocitcomsresolvedtopologicalboundaryexportimplsub_segment_group_seq_type) | typedef | — | — | 0 | Typedef for a sequence of SubSegmentGroup objects. |

## Members

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::DetermineSubSegmentFeatureType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DetermineSubSegmentFeatureType( const double &recon_time)` | constructor | `None` | public | — |
| `get_sub_segment_feature_type( const GPlatesModel::FeatureHandle::const_weak_ref &sub_segment_feature_ref)` | method | `SubSegmentType` | public | — |
| `d_recon_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | — |
| `d_sub_segment_type` | field | `SubSegmentType` | private | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &)` | method | `bool` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | Need this since "SubductionPolarityEnumeration" is in a time-dependent property value. |
| `visit_gpml_irregular_sampling( const GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | private | Need this since "SubductionPolarityEnumeration" is in a time-dependent property value. |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | private | Need this since "SubductionPolarityEnumeration" is in a time-dependent property value. |
| `visit_enumeration( const GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | private | — |
| `get_sub_segment_feature_type_from_old_plates_header( const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | method | `void` | private | — |
| `reverse_orientation()` | method | `void` | private | — |

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::DetermineSlabSubSegmentFeatureType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `DetermineSlabSubSegmentFeatureType( const double &recon_time)` | constructor | `None` | public | — |
| `get_slab_sub_segment_feature_type( const GPlatesModel::FeatureHandle::const_weak_ref &sub_segment_feature_ref)` | method | `SubSegmentType` | public | — |
| `d_recon_time` | field | `GPlatesPropertyValues::GeoTimeInstant` | private | — |
| `d_sub_segment_type` | field | `SubSegmentType` | private | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | private | — |
| `initialise_pre_property_values( const GPlatesModel::TopLevelPropertyInline &)` | method | `bool` | private | — |
| `visit_gpml_constant_value( const GPlatesPropertyValues::GpmlConstantValue &gpml_constant_value)` | method | `void` | private | Need this since "SubductionPolarityEnumeration" is in a time-dependent property value. |
| `visit_gpml_irregular_sampling( const GPlatesPropertyValues::GpmlIrregularSampling &gpml_irregular_sampling)` | method | `void` | private | Need this since "SubductionPolarityEnumeration" is in a time-dependent property value. |
| `visit_gpml_piecewise_aggregation( const GPlatesPropertyValues::GpmlPiecewiseAggregation &gpml_piecewise_aggregation)` | method | `void` | private | Need this since "SubductionPolarityEnumeration" is in a time-dependent property value. |
| `visit_enumeration( const GPlatesPropertyValues::Enumeration &enumeration)` | method | `void` | private | — |

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::SubSegmentType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SUB_SEGMENT_TYPE_SUBDUCTION_ZONE_LEFT` | enumerator | `None` | — | — |
| `SUB_SEGMENT_TYPE_SUBDUCTION_ZONE_RIGHT` | enumerator | `None` | — | — |
| `SUB_SEGMENT_TYPE_SUBDUCTION_ZONE_UNKNOWN` | enumerator | `None` | — | — |
| `SUB_SEGMENT_TYPE_SLAB_EDGE_LEADING_UNKNOWN` | enumerator | `None` | — | — |
| `SUB_SEGMENT_TYPE_SLAB_EDGE_LEADING_LEFT` | enumerator | `None` | — | — |
| `SUB_SEGMENT_TYPE_SLAB_EDGE_LEADING_RIGHT` | enumerator | `None` | — | — |
| `SUB_SEGMENT_TYPE_SLAB_EDGE_TRENCH` | enumerator | `None` | — | — |
| `SUB_SEGMENT_TYPE_SLAB_EDGE_SIDE` | enumerator | `None` | — | — |
| `SUB_SEGMENT_TYPE_OTHER` | enumerator | `None` | — | — |

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::ResolvedTopologyType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PLATE_POLYGON_TYPE` | enumerator | `None` | — | — |
| `SLAB_POLYGON_TYPE` | enumerator | `None` | — | — |
| `NETWORK_POLYGON_TYPE` | enumerator | `None` | — | — |

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::SubSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SubSegment( const GPlatesAppLogic::ResolvedTopologicalGeometrySubSegment* sub_segment_, SubSegmentType sub_segment_type_)` | constructor | `None` | public | — |
| `sub_segment` | field | `GPlatesAppLogic::ResolvedTopologicalGeometrySubSegment` | public | — |
| `sub_segment_type` | field | `SubSegmentType` | public | — |

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::sub_segment_seq_type`

*None.*

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::ResolvedTopology`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ResolvedTopology( const GPlatesAppLogic::ReconstructionGeometry* resolved_geom_, ResolvedTopologyType resolved_topology_type_)` | constructor | `None` | public | — |
| `resolved_geom` | field | `GPlatesAppLogic::ReconstructionGeometry` | public | — |
| `resolved_topology_type` | field | `ResolvedTopologyType` | public | — |

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::resolved_topologies_seq_type`

*None.*

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::SubSegmentGroup`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SubSegmentGroup( const ResolvedTopology &resolved_topology_)` | constructor | `None` | public | — |
| `resolved_topology` | field | `ResolvedTopology` | public | — |
| `sub_segments` | field | `sub_segment_seq_type` | public | — |

### `GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::sub_segment_group_seq_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_FILE_IO_CITCOMSRESOLVEDTOPOLOGICALBOUNDARYEXPORTIMPL_H` | macro | `None` | — |
| `get_sub_segment_type( const GPlatesModel::FeatureHandle::const_weak_ref &sub_segment_feature_ref, const double &recon_time)` | function | `SubSegmentType` | Determines feature type of subsegment source feature referenced by a plate polygon. |
| `get_slab_sub_segment_type( const GPlatesModel::FeatureHandle::const_weak_ref &sub_segment_feature_ref, const double &recon_time)` | function | `SubSegmentType` | Determines feature type of subsegment source feature referenced by a slab polygon. |

## Notes

- If a subduction-zone subsegment's polarity enumeration is absent or `"Unknown"`, `DetermineSubSegmentFeatureType` falls back to reading the `sL`/`sR` data-type code out of the feature's `oldPlatesHeader` property before giving up and returning `SUB_SEGMENT_TYPE_SUBDUCTION_ZONE_UNKNOWN`.
- `SubSegment`, `ResolvedTopology` and `SubSegmentGroup` hold raw, non-owning pointers into `GPlatesAppLogic` objects (a `ReconstructionGeometry` and a `ResolvedTopologicalGeometrySubSegment`); callers must keep the underlying resolved topology alive for as long as these structs are used.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/CitcomsResolvedTopologicalBoundaryExport](CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 218 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 42 |
| [file-io/OgrFormatResolvedTopologicalGeometryExport](OgrFormatResolvedTopologicalGeometryExport.md) | file-io | 29 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 5 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/CitcomsResolvedTopologicalBoundaryExportImpl.h
python scripts/gpq.py def GPlatesFileIO::CitcomsResolvedTopologicalBoundaryExportImpl::DetermineSubSegmentFeatureType --body
python scripts/gpq.py uses DetermineSubSegmentFeatureType --kind class
python scripts/gpq.py hier DetermineSubSegmentFeatureType
```
