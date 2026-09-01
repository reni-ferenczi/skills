# PlatesRotationFileProxy

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 229 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/PlatesRotationFileProxy.h` | C++ | 1081 |
| `src/file-io/PlatesRotationFileProxy.cc` | C++ | 1846 |

## Overview

[[[PROSE overview unit=file-io/PlatesRotationFileProxy tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::GetGpmlFiniteRotations`](#anonymousgetgpmlfiniterotations) | class | [`GPlatesModel::ConstFeatureVisitor`](../model/FeatureVisitor.md) | — | 0 | — |
| [`(anonymous)::Modifications`](#anonymousmodifications) | struct | — | — | 0 | — |
| [`GPlatesFileIO::RotationPoleData`](#gplatesfileiorotationpoledata) | struct | — | — | 0 | — |
| [`GPlatesFileIO::RotationFileSegment`](#gplatesfileiorotationfilesegment) | class | — | — | 7 | — |
| [`GPlatesFileIO::RotationFileSegmentContainer`](#gplatesfileiorotationfilesegmentcontainer) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::LineSegment`](#gplatesfileiolinesegment) | class | [`RotationFileSegment`](PlatesRotationFileProxy.md) | — | 1 | — |
| [`GPlatesFileIO::TextSegment`](#gplatesfileiotextsegment) | class | [`RotationFileSegment`](PlatesRotationFileProxy.md) | — | 0 | — |
| [`GPlatesFileIO::CommentSegment`](#gplatesfileiocommentsegment) | class | [`RotationFileSegment`](PlatesRotationFileProxy.md) | — | 0 | — |
| [`GPlatesFileIO::AttributeSegment`](#gplatesfileioattributesegment) | class | [`RotationFileSegment`](PlatesRotationFileProxy.md) | — | 0 | — |
| [`GPlatesFileIO::MPRSHeaderLineSegment`](#gplatesfileiomprsheaderlinesegment) | class | [`RotationFileSegment`](PlatesRotationFileProxy.md) | — | 0 | — |
| [`GPlatesFileIO::RotationPoleSegment`](#gplatesfileiorotationpolesegment) | class | [`RotationFileSegment`](PlatesRotationFileProxy.md) | — | 0 | — |
| [`GPlatesFileIO::RotationPoleLine`](#gplatesfileiorotationpoleline) | class | [`LineSegment`](PlatesRotationFileProxy.md) | — | 0 | — |
| [`GPlatesFileIO::RotationFileSegmentVisitor`](#gplatesfileiorotationfilesegmentvisitor) | class | — | — | 1 | — |
| [`GPlatesFileIO::PopulateReconstructionFeatureCollection`](#gplatesfileiopopulatereconstructionfeaturecollection) | class | [`RotationFileSegmentVisitor`](PlatesRotationFileProxy.md) | — | 0 | — |
| [`GPlatesFileIO::RotationFileReader`](#gplatesfileiorotationfilereader) | class | — | — | 1 | — |
| [`GPlatesFileIO::RotationFileReaderV2`](#gplatesfileiorotationfilereaderv2) | class | [`RotationFileReader`](PlatesRotationFileProxy.md) | — | 0 | — |
| [`GPlatesFileIO::GrotWriterWithCfg`](#gplatesfileiogrotwriterwithcfg) | class | [`PlatesRotationFormatWriter`](PlatesRotationFormatWriter.md) | — | 0 | — |
| [`GPlatesFileIO::GrotWriterWithoutCfg`](#gplatesfileiogrotwriterwithoutcfg) | class | [`PlatesRotationFormatWriter`](PlatesRotationFormatWriter.md) | — | 0 | — |
| [`GPlatesFileIO::PlatesRotationFileProxy`](#gplatesfileioplatesrotationfileproxy) | class | [`GPlatesModel::WeakObserver<GPlatesModel::FeatureCollectionHandle>`](../model/WeakObserver.md) | — | 0 | — |
| [`GPlatesFileIO::FeatureCollectionFileFormat::RotationFileConfiguration`](#gplatesfileiofeaturecollectionfileformatrotationfileconfiguration) | class | [`Configuration`](FeatureCollectionFileFormatConfiguration.md) | — | 0 | — |

## Members

### `(anonymous)::GetGpmlFiniteRotations`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit_gpml_irregular_sampling( gpml_irregular_sampling_type &gpml_irregular_sampling)` | method | `void` | public | — |
| `gpml_finite_rotations()` | method | `std::vector<const GpmlFiniteRotation*>` | public | — |
| `d_finite_rotations` | field | `std::vector<const GpmlFiniteRotation*>` | private | — |

### `(anonymous)::Modifications`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `deleted` | field | `std::vector<RotationPoleSegment*>` | public | — |
| `added` | field | `std::vector<const GpmlFiniteRotation*>` | public | — |
| `modified` | field | `std::vector<RotationPoleSegment*>` | public | — |

### `GPlatesFileIO::RotationPoleData`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RotationPoleData()` | constructor | `None` | public | — |
| `RotationPoleData( const GPlatesMaths::FiniteRotation &fr, int m_plate_id, int f_plate_id, double time_, bool disabled_ = false, const QString& comment="")` | constructor | `None` | public | — |
| `operator==( const RotationPoleData& r_data)` | operator | `bool` | public | — |
| `to_string()` | method | `QString` | public | — |
| `moving_plate_id` | field | `int` | public | — |
| `fix_plate_id` | field | `int` | public | — |
| `time` | field | `double` | public | — |
| `lat` | field | `double` | public | — |
| `lon` | field | `double` | public | — |
| `angle` | field | `double` | public | — |
| `disabled` | field | `bool` | public | — |
| `text` | field | `QString` | public | — |

### `GPlatesFileIO::RotationFileSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `accept_visitor( RotationFileSegmentVisitor&)` | method | `void` | public | — |
| `to_qstring()` | method | `QString` | public | — |
| `~RotationFileSegment()` | destructor | `None` | public | — |

### `GPlatesFileIO::RotationFileSegmentContainer`

*None.*

### `GPlatesFileIO::LineSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LineSegment( const RotationFileSegmentContainer& segs)` | constructor | `None` | public | — |
| `LineSegment( boost::shared_ptr<RotationFileSegment> seg)` | constructor | `None` | public | — |
| `accept_visitor( RotationFileSegmentVisitor& v)` | method | `void` | public | — |
| `to_qstring()` | method | `QString` | public | — |
| `d_sub_segments` | field | `RotationFileSegmentContainer` | protected | — |

### `GPlatesFileIO::TextSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TextSegment( const QString& txt, bool is_sep = false, bool visible = true)` | constructor | `None` | public | — |
| `accept_visitor( RotationFileSegmentVisitor& v)` | method | `void` | public | — |
| `is_separator()` | method | `bool` | public | — |
| `to_qstring()` | method | `QString` | public | — |
| `d_txt` | field | `QString` | private | — |
| `d_is_separator` | field | `bool` | private | — |
| `d_visible` | field | `bool` | private | — |

### `GPlatesFileIO::CommentSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `CommentSegment( const QString& str)` | constructor | `None` | public | — |
| `accept_visitor( RotationFileSegmentVisitor& v)` | method | `void` | public | — |
| `to_qstring()` | method | `QString` | public | — |
| `d_text` | field | `QString` | protected | — |

### `GPlatesFileIO::AttributeSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AttributeSegment( const QString& name, const QString& value, bool is_multiple_lines = false, bool end_with_new_line = false, const QString& leading_char = "@", const QString& name_sep = ":", const QString& value_sep = "\"", const QString& multilines_sep = "\"\"\"", const QString& sub_value_sep = "\|")` | constructor | `None` | public | — |
| `accept_visitor( RotationFileSegmentVisitor& v)` | method | `void` | public | — |
| `to_qstring()` | method | `QString` | public | — |
| `get_name()` | method | `QString` | public | — |
| `get_value()` | method | `QString` | public | — |
| `d_sub_names` | field | `QStringList` | private | — |
| `d_sub_values` | field | `QStringList` | private | — |
| `d_name` | field | `QString` | private | — |
| `d_value` | field | `QString` | private | — |
| `d_is_multilines` | field | `bool` | private | — |
| `d_end_with_new_line` | field | `bool` | private | — |
| `d_leading_char` | field | `QString` | private | — |
| `d_name_sep` | field | `QString` | private | — |
| `d_value_sep` | field | `QString` | private | — |
| `d_multilines_sep` | field | `QString` | private | — |
| `d_sub_value_sep` | field | `QString` | private | — |

### `GPlatesFileIO::MPRSHeaderLineSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `MPRSHeaderLineSegment( const RotationFileSegmentContainer& segs, bool end_with_new_line = false, const QString& leading_char = ">")` | constructor | `None` | public | — |
| `accept_visitor( RotationFileSegmentVisitor&)` | method | `void` | public | — |
| `to_qstring()` | method | `QString` | public | — |
| `get_pid()` | method | `int` | public | — |
| `d_end_with_new_line` | field | `bool` | private | — |
| `d_leading_char` | field | `QString` | private | — |
| `d_sub_segs` | field | `RotationFileSegmentContainer` | private | — |

### `GPlatesFileIO::RotationPoleSegment`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RotationPoleSegment( const RotationPoleData& _data, int plate_id_len = 3, int double_precision = 4)` | constructor | `None` | public | — |
| `accept_visitor( RotationFileSegmentVisitor& v)` | method | `void` | public | — |
| `to_qstring()` | method | `QString` | public | — |
| `data()` | method | `RotationPoleData` | public | — |
| `finite_rotation()` | method | `GPlatesModel::PropertyValue` | public | — |
| `set_finite_rotation( GPlatesModel::PropertyValue* fr)` | method | `void` | public | — |
| `pad_string( const QString& str, QChar pad, int len, bool pad_tail = true)` | method | `QString` | protected | — |
| `d_data` | field | `RotationPoleData` | protected | — |
| `d_plate_id_len` | field | `int` | protected | — |
| `d_double_precision` | field | `int` | protected | — |
| `d_associated_finite_rotation` | field | `GPlatesModel::PropertyValue` | protected | — |

### `GPlatesFileIO::RotationPoleLine`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RotationPoleLine( const RotationFileSegmentContainer& segs)` | constructor | `None` | public | — |
| `accept_visitor( RotationFileSegmentVisitor& v)` | method | `void` | public | — |
| `get_rotation_pole_data()` | method | `RotationPoleData` | public | — |
| `get_rotation_pole_data` | field | `RotationPoleData` | public | — |
| `update_attributes( const GPlatesModel::MetadataContainer &metadata)` | method | `GPlatesModel::MetadataContainer` | public | — |

### `GPlatesFileIO::RotationFileSegmentVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `visit( LineSegment&)` | method | `void` | public | — |
| `visit( TextSegment&)` | method | `void` | public | — |
| `visit( CommentSegment&)` | method | `void` | public | — |
| `visit( AttributeSegment&)` | method | `void` | public | — |
| `visit( RotationPoleSegment&)` | method | `void` | public | — |
| `visit( MPRSHeaderLineSegment&)` | method | `void` | public | — |
| `visit( RotationPoleLine&)` | method | `void` | public | — |
| `~RotationFileSegmentVisitor()` | destructor | `None` | public | — |

### `GPlatesFileIO::PopulateReconstructionFeatureCollection`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PopulateReconstructionFeatureCollection( GPlatesModel::FeatureCollectionHandle::weak_ref fc)` | constructor | `None` | public | — |
| `visit( LineSegment& s)` | method | `void` | public | — |
| `visit( TextSegment& s)` | method | `void` | public | — |
| `visit( CommentSegment& s)` | method | `void` | public | — |
| `visit( AttributeSegment& s)` | method | `void` | public | — |
| `visit( MPRSHeaderLineSegment& s)` | method | `void` | public | — |
| `visit( RotationPoleSegment& s)` | method | `void` | public | — |
| `visit( RotationPoleLine& s)` | method | `void` | public | — |
| `finalize()` | method | `void` | public | — |
| `validate_pole( const RotationPoleData&, boost::optional<const RotationPoleData&> = boost::none)` | method | `bool` | protected | — |
| `create_time_sample( const RotationPoleData&)` | method | `GPlatesPropertyValues::GpmlTimeSample` | protected | — |
| `create_new_trs_feature( const GPlatesModel::integer_plate_id_type &moving_plate_id, const GPlatesModel::integer_plate_id_type &fix_plate_id)` | method | `void` | protected | — |
| `is_new_trs( const RotationPoleData& pre, const RotationPoleData& current)` | method | `bool` | protected | — |
| `d_fc` | field | `GPlatesModel::FeatureCollectionHandle::weak_ref` | protected | — |
| `d_current_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | protected | — |
| `d_fc_metadata_feature` | field | `GPlatesModel::FeatureHandle::weak_ref` | protected | — |
| `DCMeta` | field | `std::map<QString,QString>` | protected | — |
| `d_current_sampling` | field | `boost::optional<GPlatesPropertyValues::GpmlIrregularSampling::non_null_ptr_type>` | protected | — |
| `d_current_sample` | field | `boost::optional<GPlatesPropertyValues::GpmlTimeSample>` | protected | — |
| `d_last_pole` | field | `RotationPoleData` | protected | — |
| `d_mprs_attrs` | field | `std::vector<GPlatesPropertyValues::GpmlKeyValueDictionaryElement>` | protected | — |
| `d_last_mprs` | field | `std::vector<GPlatesPropertyValues::GpmlKeyValueDictionaryElement>` | protected | — |
| `d_attrs` | field | `std::vector<AttributeSegment>` | protected | — |
| `d_fc_metadata` | field | `GPlatesModel::FeatureCollectionMetadata` | protected | — |

### `GPlatesFileIO::RotationFileReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_file( File::Reference &file, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | method | `void` | public | — |
| `read( const QFileInfo&, GPlatesModel::FeatureCollectionHandle::weak_ref)` | method | `void` | public | — |
| `~RotationFileReader()` | destructor | `None` | public | — |
| `d_segmetns` | field | `RotationFileSegmentContainer` | protected | — |

### `GPlatesFileIO::RotationFileReaderV2`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RotationFileReaderV2()` | constructor | `None` | public | — |
| `read( const QFileInfo&, GPlatesModel::FeatureCollectionHandle::weak_ref)` | method | `void` | public | — |
| `COMMENT_LEADING_CHARACTER` | field | `char` | public | — |
| `ATTRIBUTE_LEADING_CHARACTER` | field | `char` | public | — |
| `MPRS_HEADER_LEADING_CHARACTER` | field | `char` | public | — |
| `ATTR_VALUE_SEPARATOR` | field | `char` | public | — |
| `SUB_ATTR_VALUE_SEPARATOR` | field | `char` | public | — |
| `ATTR_LONG_VALUE_SEPARATOR` | field | `QString` | public | — |
| `COMMENT_LINE_REGEXP` | field | `QString` | public | — |
| `ROTATION_POLE_REGEXP` | field | `QString` | public | — |
| `ATTRIBUTE_REGEXP` | field | `QString` | public | — |
| `ATTRIBUTE_LINE_REGEXP` | field | `QString` | public | — |
| `MULTI_LINE_ATTR_REGEXP` | field | `QString` | public | — |
| `MPRS_HEADER_REGEXP` | field | `QString` | public | — |
| `process_comment( QIODevice&, RotationFileSegmentContainer&)` | method | `void` | protected | — |
| `process_attribute_line( QIODevice&, RotationFileSegmentContainer&)` | method | `void` | protected | — |
| `process_mprs_header_line( QIODevice&, RotationFileSegmentContainer&)` | method | `void` | protected | — |
| `process_rotation_pole_line( QIODevice&, RotationFileSegmentContainer&)` | method | `void` | protected | — |
| `process_arbitrary_text( QIODevice&, RotationFileSegmentContainer&)` | method | `void` | protected | — |
| `peek_next_line( QIODevice&)` | method | `QString` | protected | — |
| `is_valid_rotation_pole_line( const QString&)` | method | `bool` | protected | — |
| `parse_rotation_pole_line( const QString&, RotationPoleData&)` | method | `bool` | protected | — |
| `d_commnet_line_rx` | field | `QRegExp` | protected | — |
| `d_pole_rx` | field | `QRegExp` | protected | — |
| `d_attr_rx` | field | `QRegExp` | protected | — |
| `d_multi_line_attr_rx` | field | `QRegExp` | protected | — |
| `d_disabled_pole_rx` | field | `QRegExp` | protected | — |
| `d_mprs_header_rx` | field | `QRegExp` | protected | — |
| `FunctionMap` | typedef | `std::map<QRegExp*, function>` | protected | — |
| `RegExpVector` | typedef | `std::vector<QRegExp*>` | protected | — |
| `d_function_map` | field | `FunctionMap` | protected | — |
| `d_regexp_vec` | field | `RegExpVector` | protected | — |
| `d_last_moving_pid` | field | `int` | protected | — |
| `d_processing_mprs` | field | `bool` | protected | — |

### `GPlatesFileIO::GrotWriterWithCfg`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GrotWriterWithCfg( File::Reference &file_ref)` | constructor | `None` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `finalise_post_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `void` | public | — |
| `d_file_ref` | field | `File::Reference` | private | — |

### `GPlatesFileIO::GrotWriterWithoutCfg`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GrotWriterWithoutCfg( File::Reference &file_ref)` | constructor | `None` | public | — |
| `initialise_pre_feature_properties( const GPlatesModel::FeatureHandle &feature_handle)` | method | `bool` | public | — |
| `visit_gpml_metadata( const GPlatesPropertyValues::GpmlMetadata &gpml_metadata)` | method | `void` | public | — |
| `visit_gpml_key_value_dictionary( const GPlatesPropertyValues::GpmlKeyValueDictionary &gpml_key_value_dictionary)` | method | `void` | public | — |
| `d_file_ref` | field | `File::Reference` | private | — |
| `d_mprs_id` | field | `unsigned` | private | — |

### `GPlatesFileIO::PlatesRotationFileProxy`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ROTATION_FORMAT_VERSION` | enum | `None` | private | — |
| `PlatesRotationFileProxy()` | constructor | `None` | public | — |
| `init( File::Reference &file_ref)` | method | `void` | public | — |
| `get_segments` | field | `RotationFileSegmentContainer` | public | — |
| `accept_weak_observer_visitor( GPlatesModel::WeakObserverVisitor<GPlatesModel::FeatureCollectionHandle> &visitor)` | method | `void` | public | — |
| `create_file_writer( File::Reference &file_ref)` | method | `boost::shared_ptr<GrotWriterWithCfg>` | public | — |
| `save_file( File::Reference &file_ref)` | method | `void` | public | — |
| `save_feature( const GPlatesModel::FeatureHandle &feature_handle, File::Reference &file_ref)` | method | `void` | public | — |
| `update_header_metadata( GPlatesModel::FeatureCollectionMetadata fc_meta)` | method | `void` | public | — |
| `update_MPRS_metadata( GPlatesModel::MetadataContainer mprs_only_data, GPlatesModel::MetadataContainer default_pole_data, const QString& moving_plate_id)` | method | `void` | public | — |
| `get_mprs_range( const QString& moving_plate_id)` | method | `boost::tuple< RotationFileSegmentContainer::iterator, RotationFileSegmentContainer::iterator>` | public | — |
| `update_pole_metadata( const GPlatesModel::MetadataContainer &metadata, const RotationPoleData &pole_data)` | method | `void` | public | — |
| `insert_pole( const RotationPoleData&)` | method | `void` | public | — |
| `update_pole( const RotationPoleData& old_pole, const RotationPoleData& new_pole)` | method | `void` | public | — |
| `delete_pole( const RotationPoleData&)` | method | `void` | public | — |
| `remove_dangling_mprs_header()` | method | `void` | public | Remove any dangling MPRS header(not associated with any pole data). |
| `version()` | method | `ROTATION_FORMAT_VERSION` | protected | — |
| `check_version()` | method | `void` | protected | — |
| `create_file_reader()` | method | `void` | protected | — |
| `d_reader_ptr` | field | `boost::shared_ptr<RotationFileReader>` | protected | — |
| `d_writer_ptr` | field | `boost::shared_ptr<GrotWriterWithCfg>` | protected | — |
| `d_init` | field | `bool` | private | — |
| `d_feature_count` | field | `int` | private | — |
| `d_version` | field | `ROTATION_FORMAT_VERSION` | private | — |
| `d_feature_collection` | field | `GPlatesModel::FeatureCollectionHandle::weak_ref` | private | — |
| `d_file_info` | field | `FileInfo` | private | — |
| `PlatesRotationFileProxy( const PlatesRotationFileProxy&)` | constructor | `None` | private | — |
| `operator=` | field | `PlatesRotationFileProxy` | private | — |
| `ROTATION_EPSILON` | field | `double` | private | — |

### `GPlatesFileIO::FeatureCollectionFileFormat::RotationFileConfiguration`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `shared_ptr_to_const_type` | typedef | `boost::shared_ptr<const RotationFileConfiguration>` | public | — |
| `shared_ptr_type` | typedef | `boost::shared_ptr<RotationFileConfiguration>` | public | — |
| `RotationFileConfiguration()` | constructor | `None` | public | — |
| `d_proxy_ptr` | field | `boost::scoped_ptr<PlatesRotationFileProxy>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `COMMENT_LEADING_CHARACTER` | variable | `char` | — |
| `ATTRIBUTE_LEADING_CHARACTER` | variable | `char` | — |
| `MPRS_HEADER_LEADING_CHARACTER` | variable | `char` | — |
| `ATTR_VALUE_SEPARATOR` | variable | `char` | — |
| `SUB_ATTR_VALUE_SEPARATOR` | variable | `char` | — |
| `ATTR_LONG_VALUE_SEPARATOR` | variable | `QString` | — |
| `COMMENT_LINE_REGEXP` | variable | `QString` | — |
| `ROTATION_POLE_REGEXP` | variable | `QString` | — |
| `ATTRIBUTE_LINE_REGEXP` | variable | `QString` | — |
| `ATTRIBUTE_REGEXP` | variable | `QString` | — |
| `MULTI_LINE_ATTR_REGEXP` | variable | `QString` | — |
| `MPRS_HEADER_REGEXP` | variable | `QString` | — |
| `get_finite_rotations( FeatureCollectionHandle::weak_ref fc)` | function | `std::vector<const GpmlFiniteRotation*>` | — |
| `filter( const RotationFileSegmentContainer& segs)` | function | `std::vector<SegmentType*>` | — |
| `operator==( const RotationPoleSegment& pole_seg, const GpmlFiniteRotation& gpml_rot)` | operator | `bool` | — |
| `operator!=( const RotationPoleSegment& pole_seg, const GpmlFiniteRotation& gpml_rot)` | operator | `bool` | — |
| `operator!=( const GpmlFiniteRotation& gpml_rot, const RotationPoleSegment& pole_seg)` | operator | `bool` | — |
| `find( const std::vector<RotationPoleSegment*>& segs, const GpmlFiniteRotation* gpml_fr)` | function | `int` | — |
| `find( const std::vector<const GpmlFiniteRotation*>& gpml_frs, const RotationPoleSegment* rotation_seg)` | function | `int` | — |
| `check_modification( const RotationFileSegmentContainer& segs, FeatureCollectionHandle::weak_ref fc)` | function | `Modifications` | — |
| `ROTATION_EPSILON` | variable | `double` | — |
| `GPLATES_FILEIO_PLATESROTATIONFILEPROXY_H` | macro | `None` | — |
| `sep_length( const SeparatorType&)` | function | `int` | — |
| `sep_length( const char&)` | function | `int` | — |
| `sep_length( const QString& str)` | function | `int` | — |
| `update_attributes_and_return_new( const GPlatesModel::MetadataContainer &new_data, const RotationFileSegmentContainer &file_segs)` | function | `GPlatesModel::MetadataContainer` | — |
| `update_or_delete_attribute( GPlatesModel::MetadataContainer &new_data, AttributeSegment &attr)` | function | `void` | — |

## Notes

[[[PROSE notes unit=file-io/PlatesRotationFileProxy tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 90 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 46 |
| [qt-widgets/EditTotalReconstructionSequenceWidget](../qt-widgets/EditTotalReconstructionSequenceWidget.md) | qt-widgets | 18 |
| [feature-visitors/TotalReconstructionSequenceRotationInserter](../feature-visitors/TotalReconstructionSequenceRotationInserter.md) | feature-visitors | 14 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 13 |
| [file-io/PlatesRotationFormatReader](PlatesRotationFormatReader.md) | file-io | 5 |
| [data-mining/DataSelector](../data-mining/DataSelector.md) | data-mining | 4 |
| [qt-widgets/SaveFileDialogImpl](../qt-widgets/SaveFileDialogImpl.md) | qt-widgets | 2 |
| [qt-widgets/CreateTotalReconstructionSequenceDialog](../qt-widgets/CreateTotalReconstructionSequenceDialog.md) | qt-widgets | 1 |
| [qt-widgets/EditTotalReconstructionSequenceDialog](../qt-widgets/EditTotalReconstructionSequenceDialog.md) | qt-widgets | 1 |
| [unit-test/FilterTest](../unit-test/FilterTest.md) | unit-test | 1 |
| [utils/ConfigBundleUtils](../utils/ConfigBundleUtils.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/PlatesRotationFileProxy.h
python scripts/gpq.py def GPlatesFileIO::PlatesRotationFileProxy --body
python scripts/gpq.py uses PlatesRotationFileProxy --kind class
python scripts/gpq.py hier PlatesRotationFileProxy
```
