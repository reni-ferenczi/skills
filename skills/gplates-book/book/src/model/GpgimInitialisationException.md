# GpgimInitialisationException

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1271 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/GpgimInitialisationException.h` | C++ | 85 |
| `src/model/GpgimInitialisationException.cc` | C++ | 39 |

## Overview

`GpgimInitialisationException` is the `GPlatesGlobal::Exception` thrown when
`Gpgim` fails to read or parse `gpgim.xml` at startup. It carries the GPGIM
filename, the line number in that file, and a message describing what went
wrong, and formats them into a single diagnostic line in `write_message()`
("Error initialising GPGIM from file '...' at line '...': ..."). Since GPGIM
parsing happens once, early in startup, this exception exists to give that
one failure mode a precise, file-and-line error report rather than a generic
one.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::GpgimInitialisationException`](#gplatesmodelgpgiminitialisationexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 0 | An exception during initialisation of the GPGIM (reading/parsing GPGIM XML file). |

## Members

### `GPlatesModel::GpgimInitialisationException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `GpgimInitialisationException( const GPlatesUtils::CallStack::Trace &exception_source, const QString &gpgim_filename, const qint64 &line_number, const QString &msg)` | constructor | `None` | public | in which the problem occurs. |
| `~GpgimInitialisationException()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_gpgim_filename` | field | `QString` | private | — |
| `d_line_number` | field | `int` | private | — |
| `d_msg` | field | `QString` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_GPGIMINITIALISATIONEXCEPTION_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [model/Gpgim](Gpgim.md) | model | 40 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/GpgimInitialisationException.h
python scripts/gpq.py def GPlatesModel::GpgimInitialisationException --body
python scripts/gpq.py uses GpgimInitialisationException --kind class
python scripts/gpq.py hier GpgimInitialisationException
```
