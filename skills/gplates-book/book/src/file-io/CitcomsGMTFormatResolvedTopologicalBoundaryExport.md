# CitcomsGMTFormatResolvedTopologicalBoundaryExport

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 96 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.h` | C++ | 86 |
| `src/file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.cc` | C++ | 943 |

## Overview

[[[PROSE overview unit=file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::TextStream`](#gplatesfileiocitcomsgmtformatresolvedtopologicalboundaryexportanonymoustextstream) | class | — | — | 0 | Convenience wrapper for opening a text file and attached QTextStream to it. |
| [`GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::GMTExportHeader`](#gplatesfileiocitcomsgmtformatresolvedtopologicalboundaryexportanonymousgmtexportheader) | class | — | — | 2 | Interface for formatting of a GMT feature header. |
| [`GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::ResolvedTopologyHeader`](#gplatesfileiocitcomsgmtformatresolvedtopologicalboundaryexportanonymousresolvedtopologyheader) | class | [`GMTExportHeader`](CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | — | 0 | Formats GMT header for Polygons (plate/slab/network) |
| [`GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::SubSegmentHeader`](#gplatesfileiocitcomsgmtformatresolvedtopologicalboundaryexportanonymoussubsegmentheader) | class | [`GMTExportHeader`](CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | — | 0 | Formats an export GMT header for subsegments: "\>sL # name: Trenched\_on NAP\_PAC\_1 # ... # polygon: NAM # use\_reverse: no # identity: GPlates-blah-blah-blah" TODO: Determine if CitcomS actually uses the 'polygon' field. |
| [`GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::GMTFeatureExporter`](#gplatesfileiocitcomsgmtformatresolvedtopologicalboundaryexportanonymousgmtfeatureexporter) | class | — | — | 0 | Handles exporting of a feature's geometry and header to GMT format. |
| [`GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::referenced_files_collection_type`](#gplatesfileiocitcomsgmtformatresolvedtopologicalboundaryexportreferenced_files_collection_type) | typedef | — | — | 0 | Typedef for a sequence of referenced files. |
| [`GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::resolved_topologies_seq_type`](#gplatesfileiocitcomsgmtformatresolvedtopologicalboundaryexportresolved_topologies_seq_type) | typedef | — | — | 0 | Typedef for a feature geometry group of resolved topological geometries. |
| [`GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::sub_segment_group_seq_type`](#gplatesfileiocitcomsgmtformatresolvedtopologicalboundaryexportsub_segment_group_seq_type) | typedef | — | — | 0 | Typedef for a sequence of SubSegmentGroup objects. |

## Members

### `GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::TextStream`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TextStream( const QFileInfo &file_info, bool open_file = true)` | constructor | `None` | public | — |
| `is_open()` | method | `bool` | public | — |
| `open()` | method | `void` | public | — |
| `d_file_info` | field | `QFileInfo` | private | — |
| `d_file` | field | `QFile` | private | — |
| `d_text_stream` | field | `QTextStream` | private | — |

### `GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::GMTExportHeader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~GMTExportHeader()` | destructor | `None` | public | — |
| `get_feature_header_lines( std::vector<QString>& header_lines)` | method | `void` | public | Format feature into a sequence of header lines (returned as strings). |

### `GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::ResolvedTopologyHeader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ResolvedTopologyHeader( const GPlatesModel::FeatureHandle::const_weak_ref &resolved_topology_feature, ResolvedTopologyType resolved_topology_type)` | constructor | `None` | public | — |
| `get_feature_header_lines( std::vector<QString>& header_lines)` | method | `void` | public | — |
| `d_header_line` | field | `QString` | private | — |

### `GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::SubSegmentHeader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `SubSegmentHeader( const GPlatesModel::FeatureHandle::const_weak_ref &sub_segment_feature, const GPlatesModel::FeatureHandle::const_weak_ref &resolved_topology_feature, const SubSegment &sub_segment, ResolvedTopologyType resolved_topology_type)` | constructor | `None` | public | — |
| `get_feature_header_lines( std::vector<QString>& header_lines)` | method | `void` | public | — |
| `d_header_line` | field | `QString` | private | — |

### `GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::GMTFeatureExporter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GMTFeatureExporter( const QFileInfo &file_info)` | constructor | `None` | public | Constructor. |
| `print_gmt_header_and_geometry( const GMTExportHeader &gmt_header, const GPlatesMaths::GeometryOnSphere::non_null_ptr_to_const_type &geometry)` | method | `void` | public | Write a feature's header and geometry to GMT format. |
| `d_output_stream` | field | `TextStream` | private | Does writing to file. |
| `d_gmt_header_printer` | field | `GPlatesFileIO::GMTHeaderPrinter` | private | Does the actual printing of GMT header to the output stream. |

### `GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::referenced_files_collection_type`

*None.*

### `GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::resolved_topologies_seq_type`

*None.*

### `GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::sub_segment_group_seq_type`

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_feature_id( QString &id, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "\<gpml:identity\>" property in feature otherwise returns false. |
| `get_feature_name( QString &name, const GPlatesModel::FeatureHandle::const_weak_ref &feature, const GPlatesPropertyValues::GpmlOldPlatesHeader *gpml_old_plates_header)` | function | `bool` | Looks for "gml:name" property in feature otherwise looks at GpmlOldPlatesHeader for geographic description (if non-null) otherwise returns false. |
| `get_feature_name( QString &name, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gml:name" property in feature otherwise returns false. |
| `get_feature_sz_age( QString &age, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gpml:subductionZoneAge" property in feature otherwise returns false. |
| `get_feature_sz_convergence( QString &age, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gpml:subductionZoneConvergence" property in feature otherwise returns false. |
| `get_feature_sz_dip( QString &dip, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gpml:subductionZoneDeepDip" property in feature otherwise returns false. |
| `get_feature_sz_depth( QString &depth, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gpml:subductionZoneDepth" property in feature otherwise returns false. |
| `get_feature_sz_system( QString &system, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gpml:subductionZoneSystem" property in feature otherwise returns false. |
| `get_feature_sz_system_order( QString &order, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gpml:subductionZoneSystemOrder" property in feature otherwise returns false. |
| `get_feature_rhea_fault( QString &rhea_fault, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gpml:rheaFault" property in feature otherwise returns false. |
| `get_feature_slab_flat_lying( QString &flat, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gpml:slabFlatLying" property in feature otherwise returns false. |
| `get_feature_slab_flat_lying_depth( QString &value, const GPlatesModel::FeatureHandle::const_weak_ref &feature)` | function | `bool` | Looks for "gpml:slabFlatLyingDepth" property in feature otherwise returns false. |
| `get_feature_type_code_2chars( const SubSegmentType sub_segment_type )` | function | `QString` | Get a two-letter PLATES data type code from the subsegment type if it's a subduction zone, otherwise get the data type code from a GpmlOldPlatesHeader if there is one, otherwise get the full gpml feature type. |
| `get_feature_type_code( const GPlatesModel::FeatureHandle::const_weak_ref &source_feature, const SubSegmentType sub_segment_type)` | function | `QString` | Get a two-letter PLATES data type code from the subsegment type if it's a subduction zone, otherwise get the data type code from a GpmlOldPlatesHeader if there is one, otherwise get the full gpml feature type. |
| `GPLATES_FILE_IO_CITCOMSGMTFORMATRESOLVEDTOPOLOGICALBOUNDARYEXPORT_H` | macro | `None` | — |
| `export_resolved_topological_boundaries( const resolved_topologies_seq_type &resolved_topologies, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_pla ...` | function | `void` | Exports ResolvedTopologicalBoundary and ResolvedTopologicalNetwork objects to GMT format. |
| `export_sub_segments( const sub_segment_group_seq_type &sub_segments, const QFileInfo& file_info, const referenced_files_collection_type &referenced_files, const referenced_files_collection_type &active_reconstruction_files, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id)` | function | `void` | Exports subsegments of resolved topological boundaries to GMT format. |

## Notes

[[[PROSE notes unit=file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/CitcomsResolvedTopologicalBoundaryExport](CitcomsResolvedTopologicalBoundaryExport.md) | file-io | 34 |
| [api/PyTopologyTools](../api/PyTopologyTools.md) | api | 2 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 2 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 2 |
| [qt-widgets/deprecated/CreateFeatureIdListDialog](../qt-widgets/deprecated/CreateFeatureIdListDialog.md) | qt-widgets | 2 |
| [gui/TopologySectionsTable](../gui/TopologySectionsTable.md) | gui | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.h
python scripts/gpq.py def GPlatesFileIO::CitcomsGMTFormatResolvedTopologicalBoundaryExport::(anonymous)::SubSegmentHeader --body
python scripts/gpq.py uses SubSegmentHeader --kind class
python scripts/gpq.py hier SubSegmentHeader
```
