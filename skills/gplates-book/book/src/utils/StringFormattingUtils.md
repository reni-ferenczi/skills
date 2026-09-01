# StringFormattingUtils

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 1280 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/StringFormattingUtils.h` | C++ | 102 |
| `src/utils/StringFormattingUtils.cc` | C++ | 153 |

## Overview

[[[PROSE overview unit=utils/StringFormattingUtils tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::InvalidFormattingParametersException`](#gplatesutilsinvalidformattingparametersexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | — |

## Members

### `GPlatesUtils::InvalidFormattingParametersException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidFormattingParametersException( const GPlatesUtils::CallStack::Trace &exception_source, const std::string &message)` | constructor | `None` | public | — |
| `~InvalidFormattingParametersException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_message` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `remove_trailing_zeroes( const std::string &s)` | function | `std::string` | Remove any unnecessary zero digits after the decimal place. |
| `GPLATES_UTILS_STRINGFORMATTINGUTILS_H` | macro | `None` | — |
| `IGNORE_PRECISION` | variable | `int` | Tell 'formatted\_double\_to\_string()' to ignore precision. |
| `formatted_double_to_string( const double &val, unsigned width, int prec = IGNORE_PRECISION, bool elide_trailing_zeroes = false)` | function | `std::string` | Print a real number in a space of 'width' characters, right-justified, with exactly 'prec' digits to the right of the decimal place. |
| `formatted_int_to_string( int val, unsigned width, char fill_char = ' ')` | function | `std::string` | — |

## Notes

[[[PROSE notes unit=utils/StringFormattingUtils tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GMTFormatMultiPointVectorFieldExport](../file-io/GMTFormatMultiPointVectorFieldExport.md) | file-io | 13 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 11 |
| [file-io/PlatesLineFormatWriter](../file-io/PlatesLineFormatWriter.md) | file-io | 11 |
| [file-io/CitcomsFormatVelocityVectorFieldExport](../file-io/CitcomsFormatVelocityVectorFieldExport.md) | file-io | 7 |
| [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](../file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) | file-io | 7 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 7 |
| [file-io/GMTFormatFlowlineExport](../file-io/GMTFormatFlowlineExport.md) | file-io | 5 |
| [file-io/GMTFormatMotionPathExport](../file-io/GMTFormatMotionPathExport.md) | file-io | 5 |
| [file-io/PlatesLineFormatGeometryExporter](../file-io/PlatesLineFormatGeometryExporter.md) | file-io | 5 |
| [file-io/GMTFormatGeometryExporter](../file-io/GMTFormatGeometryExporter.md) | file-io | 4 |
| [file-io/TerraFormatVelocityVectorFieldExport](../file-io/TerraFormatVelocityVectorFieldExport.md) | file-io | 4 |
| [file-io/GMTFormatDeformationExport](../file-io/GMTFormatDeformationExport.md) | file-io | 3 |
| [file-io/GMTFormatReconstructedScalarCoverageExport](../file-io/GMTFormatReconstructedScalarCoverageExport.md) | file-io | 3 |
| [qt-widgets/LatLonCoordinatesTable](../qt-widgets/LatLonCoordinatesTable.md) | qt-widgets | 3 |
| [file-io/GMTFormatReconstructedFeatureGeometryExport](../file-io/GMTFormatReconstructedFeatureGeometryExport.md) | file-io | 1 |
| [file-io/GMTFormatResolvedTopologicalGeometryExport](../file-io/GMTFormatResolvedTopologicalGeometryExport.md) | file-io | 1 |
| [file-io/GMTFormatWriter](../file-io/GMTFormatWriter.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/StringFormattingUtils.h
python scripts/gpq.py def GPlatesUtils::InvalidFormattingParametersException --body
python scripts/gpq.py uses InvalidFormattingParametersException --kind class
python scripts/gpq.py hier InvalidFormattingParametersException
```
