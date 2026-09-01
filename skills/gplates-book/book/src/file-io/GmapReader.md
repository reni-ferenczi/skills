# GmapReader

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 415 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/GmapReader.h` | C++ | 52 |
| `src/file-io/GmapReader.cc` | C++ | 551 |

## Overview

[[[PROSE overview unit=file-io/GmapReader tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::VirtualGeomagneticPole`](#anonymousvirtualgeomagneticpole) | struct | — | — | 0 | — |
| [`GPlatesFileIO::GmapReader`](#gplatesfileiogmapreader) | class | — | — | 0 | — |

## Members

### `(anonymous)::VirtualGeomagneticPole`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `header` | field | `QString` | public | — |
| `inclination` | field | `float` | public | — |
| `declination` | field | `float` | public | — |
| `a95` | field | `float` | public | — |
| `site_latitude` | field | `float` | public | — |
| `site_longitude` | field | `float` | public | — |
| `vgp_latitude` | field | `float` | public | — |
| `vgp_longitude` | field | `float` | public | — |
| `dp` | field | `float` | public | — |
| `plate_id` | field | `boost::optional<GPlatesModel::integer_plate_id_type>` | public | — |
| `age` | field | `float` | public | — |

### `GPlatesFileIO::GmapReader`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `read_file( File::Reference &file, ReadErrorAccumulation &read_errors, bool &contains_unsaved_changes)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DELTA_AGE` | variable | `float` | The initial time-of-apperance, time-of-disappearance may be set to be the sample age +/- DELTA\_AGE. |
| `display_vgp( const VirtualGeomagneticPole &vgp)` | function | `void` | — |
| `append_name_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const QString &description)` | function | `void` | — |
| `append_site_geometry_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &latitude, const float &longitude)` | function | `void` | — |
| `append_inclination_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &inclination)` | function | `void` | — |
| `append_declination_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &declination)` | function | `void` | — |
| `append_a95_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &a95)` | function | `void` | — |
| `append_age_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &age)` | function | `void` | — |
| `append_vgp_position_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &vgp_latitude, const float &vgp_longitude)` | function | `void` | — |
| `append_plate_id_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const GPlatesModel::integer_plate_id_type &plate_id)` | function | `void` | — |
| `append_dm_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &dm)` | function | `void` | — |
| `append_dp_to_feature( const GPlatesModel::FeatureHandle::weak_ref &feature, const float &dp)` | function | `void` | — |
| `create_vgp_feature( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, const VirtualGeomagneticPole &vgp)` | function | `void` | — |
| `check_format_and_return_value( QString &line)` | function | `boost::optional<float>` | Returns a non-empty boost::optional\<float\> if line, after trimming of white-space, begins and ends in the double-quote character, and if the string contained between the quotes can be converted to a float |
| `line_is_header( const QString &line)` | function | `bool` | Returns true if the line is identified as a GMAP vgp header line. |
| `read_feature( GPlatesModel::FeatureCollectionHandle::weak_ref &collection, const QString &header_line, QTextStream &input, const boost::shared_ptr<GPlatesFileIO::DataSource> &source, unsigned int &line_number, GPlatesFileIO::ReadErrorAccumulation &errors)` | function | `void` | — |
| `GPLATES_FILEIO_GMAPREADER_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=file-io/GmapReader tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [gui/CustomCompleter](../gui/CustomCompleter.md) | gui | 5 |
| [qt-widgets/HellingerPickWidget](../qt-widgets/HellingerPickWidget.md) | qt-widgets | 5 |
| [qt-widgets/SearchResultsDockWidget](../qt-widgets/SearchResultsDockWidget.md) | qt-widgets | 3 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 3 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 3 |
| [file-io/FeatureCollectionFileFormatRegistry](FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [qt-widgets/TotalReconstructionPolesDialog](../qt-widgets/TotalReconstructionPolesDialog.md) | qt-widgets | 2 |
| [maths/GreatCircleArc](../maths/GreatCircleArc.md) | maths | 1 |
| [qt-widgets/DigitisationWidget](../qt-widgets/DigitisationWidget.md) | qt-widgets | 1 |
| [qt-widgets/ExportFileNameTemplateWidget](../qt-widgets/ExportFileNameTemplateWidget.md) | qt-widgets | 1 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 1 |
| [qt-widgets/ModifyGeometryWidget](../qt-widgets/ModifyGeometryWidget.md) | qt-widgets | 1 |
| [qt-widgets/RasterPropertiesDialog](../qt-widgets/RasterPropertiesDialog.md) | qt-widgets | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/GmapReader.h
python scripts/gpq.py def (anonymous)::VirtualGeomagneticPole --body
python scripts/gpq.py uses VirtualGeomagneticPole --kind struct
python scripts/gpq.py hier VirtualGeomagneticPole
```
