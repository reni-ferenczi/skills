# HellingerWriter

[Book TOC](../../TOC.md) · [file-io](../../components/file-io.md) · cluster Community 1757 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/HellingerWriter.h` | C++ | 61 |
| `src/file-io/HellingerWriter.cc` | C++ | 233 |

## Overview

`HellingerWriter` is the counterpart to `file-io/HellingerReader`: it
serialises a `GPlatesQtWidgets::HellingerModel` back out to the same
`.pick`/`.com` text formats used by the Hellinger plate-fitting tool.
`write_pick_file` walks the model's picks and writes one line per pick as
`<plate index> <segment> <lat> <lon> <uncertainty>`, using `get_plate_index`
to fold each pick's enabled/disabled state into the plate-index value the
legacy format expects (a disabled pick is written with its
`DISABLED_PLATE_*_PICK_TYPE` index rather than a separate flag column).
`write_com_file` writes the fit configuration held in the model's
`HellingerComFileStructure` in the fixed line order the original FORTRAN
Hellinger tool requires — pick filename, initial-guess lat/lon/rho, search
radius, grid-search and kappa-estimation flags, and the associated `.dat`
filenames.

Both writers default the caller-supplied filename's extension: `write_pick_file`
only does so when `add_missing_pick_extension` is set, while `write_com_file`
always forces a `.com` extension. A comment on `write_com_file` records that
the output layout is deliberately kept identical to the legacy format so
existing user FORTRAN routines keep working, deferring any richer GPlates-native
`.com` format to a possible future export path.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesFileIO::HellingerWriter`](#gplatesfileiohellingerwriter) | class | — | — | 0 | — |

## Members

### `GPlatesFileIO::HellingerWriter`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `HellingerWriter()` | constructor | `None` | public | — |
| `write_pick_file(QString &filename, GPlatesQtWidgets::HellingerModel& hellinger_model, bool export_disabled_picks = true, bool add_missing_pick_extension = false)` | method | `void` | public | — |
| `write_com_file( QString &filename, GPlatesQtWidgets::HellingerModel& hellinger_model)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_plate_index( const GPlatesQtWidgets::HellingerPlateIndex index, bool enabled)` | function | `GPlatesQtWidgets::HellingerPlateIndex` | — |
| `GPLATES_FILEIO_PICKFILEWRITER_H` | macro | `None` | — |

## Notes

Neither writer takes a `ReadErrorAccumulation`; a failure to open the output
file is only reported via `qWarning()`, not surfaced to the caller as a
return value or exception. `write_com_file` writes the pick filename found in
`com_struct->d_pick_file` as-is (falling back to the `.com` file's base name
only if that field is empty) even though the format expects a path relative
to the `.com` file's own location — the code does not enforce that
relationship, as the surrounding `TODO` comments note.

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/HellingerDialog](../qt-widgets/HellingerDialog.md) | qt-widgets | 138 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/HellingerWriter.h
python scripts/gpq.py def GPlatesFileIO::HellingerWriter --body
python scripts/gpq.py uses HellingerWriter --kind class
python scripts/gpq.py hier HellingerWriter
```
