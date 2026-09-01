# PyFunctions

[Book TOC](../../TOC.md) · [api](../../components/api.md) · cluster Community 1516 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/api/PyFunctions.cc` | C++ | 303 |

## Overview

This module exports Python bindings for two core reconstruction workflows. `reconstruct` takes feature files and rotation files at a specified time and generates reconstructed geometries, exported to a chosen format (GMT, Shapefile, GeoJSON or OGRGMT). `reverse_reconstruct` is the inverse operation: it takes feature files whose geometries are already reconstructed at a given time and reconstructs them back to present day, then writes the result to new files. Helper functions adapt Python types to C++ (`to_str_vector`) and infer the output format from file extension (`get_format`).

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `to_str_vector(const bp::list& objs)` | function | `std::vector<QString>` | — |
| `get_format(QString file_name)` | function | `GPlatesFileIO::ReconstructedFeatureGeometryExport::Format` | — |
| `reconstruct( bp::list recon_files, bp::list rot_files, bp::object time, bp::object anchor_plate_id, bp::object export_file_name)` | function | `void` | — |
| `reverse_reconstruct( bp::list python_reconstructable_filenames, bp::list python_reconstruction_filenames, bp::object python_time, bp::object python_anchor_plate_id, bp::object python_output_file_basename_suffix, bp::object python_output_file_format)` | function | `void` | Loads reconstructable features from files python\_reconstructable\_filenames and assumes each feature geometry is \*not\* present day geometry but instead is the reconstructed geometry for the specified time python\_time. |
| `export_functions()` | function | `void` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

**Python bindings**

| Python name | Kind | Owner | C++ |
|---|---|---|---|
| `reconstruct` | function | — | `&reconstruct` |
| `reverse_reconstruct` | function | — | `&reverse_reconstruct` |


## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/api/PyFunctions.cc
```
