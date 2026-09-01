# python-examples

[Book TOC](../TOC.md)

Stand-alone pyGPlates demo and utility scripts.

1 unit page(s), 7 source file(s) documented here, 26 further file(s) listed below.

## Overview

This component is a grab-bag of standalone scripts written against the embedded `pygplates` scripting API rather than part of the compiled application: nothing under `scripts/` is referenced from any CMakeLists, so these files ship as examples and utilities a user runs, not code the reconstruction pipeline links against. That isolation shows up directly in the dependency tables — no incoming or outgoing edges — because the scripts talk only to the Python bindings surface (`pygplates.reconstruct()`, `pygplates.Application()`, `pygplates.MainWindow()`, `pygplates.CoRegistration()`), never to the C++ internals those bindings wrap.

The single `python-examples` unit groups seven scripts spanning the range of what the API exposes. `reconstruct.py` and `interpolation_test.py` are minimal drivers that call the top-level `pygplates.reconstruct()` function to reconstruct feature collections against rotation files at a given time and anchor plate, writing `.xy`/`.gmt` output — the simplest possible use of the module outside a running GPlates session. `camera_demo.py` and `feature_collection_demo.py` instead require a live GPlates instance: they use `pygplates.MainWindow()` to script camera pans/zooms and `pygplates.Application()` to walk the currently loaded feature collections, features and properties, illustrating the introspection side of the embedded interpreter. `CoRegDemo.py` drives `pygplates.CoRegistration()` across a range of reconstruction times using a multiprocessing pool, configuring co-registration rows (region of interest, presence, distance, number-in-region lookups) the same way the co-registration layer would. The pair `hellinger.py` and `hellinger_maths.py` — together the bulk of this component's line count — are a Python port of the FORTRAN Hellinger method for estimating finite rotations from ship-track magnetic crossing data, implementing quaternion algebra, matrix decomposition and minimisation routines independently of the rest of GPlates.

The listed "Other files" are a deprecated Orange Data Mining widget set (`scripts/deprecated/orange-widget/`) that wrapped GPlates co-registration output for use inside Orange Canvas workflows: widgets such as `OWReadDataSingleTime`, `OWAttributeAtTime`, `OWBirthTime`, `OWBirthAttribute`, `OWTimeSeries`, `OWOrdinalSignature`, `OWMergeRowAligned` and `OWStringToNum` let a user load per-time-step co-registration data, look up attribute values at arbitrary reconstruction times, compute when a feature's attribute first appears, merge aligned rows and derive ordinal signatures for time-series analysis — with `gplates.py` supplying shared XML-association parsing and `.ui` files defining the Qt Designer forms Orange rendered for each widget. `orange_demo.py` at the top of `scripts/` shows the intended entry point into that workflow. Because the whole component sits outside the dependency graph, it has no neighbours to lean on or be leaned on by: it is consumer-facing scaffolding around the Python bindings rather than infrastructure any other component depends on.

## Units

| Unit | Tier | Lines | Fan-in | Description |
|---|---|---|---|---|
| [python-examples](../src/scripts/python-examples.md) | 3 | 3876 | 0 | example scripts demonstrating the pygplates API for reconstruction, interpolation, camera control, co-registration and plate motion analysis |

## Other files

| File | Kind | Lines |
|---|---|---|
| `scripts/deprecated/orange-widget/CombineDomains.py` | Python | 47 |
| `scripts/deprecated/orange-widget/LoadCoregFileSelectTime.py` | Python | 213 |
| `scripts/deprecated/orange-widget/OWAttributeAtTime.py` | Python | 143 |
| `scripts/deprecated/orange-widget/OWBirthAttribute.py` | Python | 154 |
| `scripts/deprecated/orange-widget/OWBirthTime.py` | Python | 113 |
| `scripts/deprecated/orange-widget/OWMergeRowAligned.py` | Python | 80 |
| `scripts/deprecated/orange-widget/OWOrdinalSignature.py` | Python | 229 |
| `scripts/deprecated/orange-widget/OWReadDataSingleTime.py` | Python | 160 |
| `scripts/deprecated/orange-widget/OWStringToNum.py` | Python | 106 |
| `scripts/deprecated/orange-widget/OWTimeSeries.py` | Python | 207 |
| `scripts/deprecated/orange-widget/__init__.py` | Python | 22 |
| `scripts/deprecated/orange-widget/attr_at_time.ui` | Qt form | 124 |
| `scripts/deprecated/orange-widget/birth_attr.ui` | Qt form | 101 |
| `scripts/deprecated/orange-widget/birth_time.ui` | Qt form | 68 |
| `scripts/deprecated/orange-widget/example.py` | Python | 78 |
| `scripts/deprecated/orange-widget/gplates.py` | Python | 398 |
| `scripts/deprecated/orange-widget/icons/combine_data.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/compute_attrib_at_time.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/compute_birth_attribute.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/compute_birth_time.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/load_data_select_time.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/merge_timedepdata.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/ordinal_signature.png` | other | 0 |
| `scripts/deprecated/orange-widget/icons/string_to_num.png` | other | 0 |
| `scripts/deprecated/orange-widget/time_series.ui` | Qt form | 261 |
| `scripts/deprecated/orange_demo.py` | Python | 66 |

## Depends on

*None.*

## Used by

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py tree scripts
python scripts/gpq.py sym . --mode sub --path scripts --defs-only
```
