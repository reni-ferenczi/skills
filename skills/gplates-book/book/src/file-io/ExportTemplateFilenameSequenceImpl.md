# ExportTemplateFilenameSequenceImpl

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 337 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/ExportTemplateFilenameSequenceImpl.h` | C++ | 313 |
| `src/file-io/ExportTemplateFilenameSequenceImpl.cc` | C++ | 496 |

## Overview

Generates sequences of filenames from templates containing format placeholders. Recognizes format codes such as frame number (%f), reconstruction time (printf-style), anchor plate ID (%a), datetime, and layer name, extracting them from the template and substituting values from the reconstruction sequence. Validates that templates produce varied filenames (differ with reconstruction time) and throws exceptions for unrecognized formats.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::ExportTemplateFilenameSequenceImpl`](#gplatesfileioexporttemplatefilenamesequenceimpl) | class | `boost::noncopyable` | — | 0 | Implementation of ExportTemplateFilenameSequence. |

## Members

### `GPlatesFileIO::ExportTemplateFilenameSequenceImpl`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `validate_filename_template( const QString &filename_template, bool check_filename_variation)` | method | `void` | public | Tests for validity of parameters in the filename template. |
| `ExportTemplateFilenameSequenceImpl( const QString &filename_template, const GPlatesModel::integer_plate_id_type &reconstruction_anchor_plate_id, const QString &default_recon_tree_layer_name, const double &begin_reconstruction_time, const double &reconstruction_time_increment, const GPlatesUtils::AnimationSequence::Sequ ...` | constructor | `None` | public | Constructor. |
| `size()` | method | `std::size_t` | public | Returns number of filenames in the sequence. |
| `get_filename( const std::size_t sequence_index, const QDateTime &date_time)` | method | `QString` | public | Gets the filename at index sequence\_index in the sequence. |
| `format_ptr_type` | typedef | `boost::shared_ptr<ExportTemplateFilename::Format>` | private | Typedef for memory-managed pointer to Format. |
| `format_seq_type` | typedef | `std::vector<format_ptr_type>` | private | Typedef for sequence of Format objects. |
| `d_filename_template` | field | `QString` | private | Filename template string containing placeholders %1, %2, etc for each format. |
| `d_begin_reconstruction_time` | field | `double` | private | — |
| `d_reconstruction_time_increment` | field | `double` | private | — |
| `d_sequence_info` | field | `GPlatesUtils::AnimationSequence::SequenceInfo` | private | — |
| `d_format_seq` | field | `format_seq_type` | private | — |
| `FormatExtractor` | class | `None` | private | Used to extract ExportTemplateFilename::Format from filename template. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `operator()( Wrap<FormatType>)` | operator | `void` | — |
| `operator()( Wrap<FormatType>)` | operator | `void` | — |
| `GPLATES_FILE_IO_EXPORTTEMPLATEFILENAMESEQUENCEIMPL_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/ExportTemplateFilenameSequence](ExportTemplateFilenameSequence.md) | file-io | 2 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/ExportTemplateFilenameSequenceImpl.h
python scripts/gpq.py def GPlatesFileIO::ExportTemplateFilenameSequenceImpl --body
python scripts/gpq.py uses ExportTemplateFilenameSequenceImpl --kind class
python scripts/gpq.py hier ExportTemplateFilenameSequenceImpl
```
