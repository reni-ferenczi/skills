# GenerateVelocityDomainTerra

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 1191 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/GenerateVelocityDomainTerra.h` | C++ | 168 |
| `src/app-logic/GenerateVelocityDomainTerra.cc` | C++ | 244 |

## Overview

[[[PROSE overview unit=app-logic/GenerateVelocityDomainTerra tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesAppLogic::GenerateVelocityDomainTerra::Grid`](#gplatesapplogicgeneratevelocitydomainterragrid) | class | `boost::noncopyable` | — | 0 | An entire Terra grid of point locations (stored in memory) at which to calculate velocity. |

## Members

### `GPlatesAppLogic::GenerateVelocityDomainTerra::Grid`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Grid( unsigned int mt, unsigned int nt, unsigned int nd)` | constructor | `None` | public | Generates the positions at which to calculate velocities for Terra. mt, nt and nd are Terra parameters (by the same name). |
| `get_num_processors()` | method | `unsigned int` | public | Returns the number of Terra processors (determined by the constructor parameters). |
| `get_processor_sub_domain( unsigned int processor_number)` | method | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | public | Retrieve the sub-domain for the specified Terra local processor number. processor\_number is the local processor number (also defined by Terra). |
| `Diamond` | class | `None` | private | A single icosahedral diamond. |
| `d_mt` | field | `unsigned int` | private | — |
| `d_nt` | field | `unsigned int` | private | — |
| `d_nd` | field | `unsigned int` | private | — |
| `d_num_processors` | field | `unsigned int` | private | — |
| `d_diamond` | field | `Diamond` | private | The multi-dimensional array containing the entire grid of points. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `midpoint( const GPlatesMaths::UnitVector3D &v1, const GPlatesMaths::UnitVector3D &v2)` | function | `GPlatesMaths::UnitVector3D` | Subdivides the two specified vectors and returns the midpoint on the sphere. |
| `GENERATE_VELOCITY_DOMAIN_CITCOMS_H` | macro | `None` | — |
| `calculate_num_processors( unsigned int mt, unsigned int nt, unsigned int nd)` | function | `unsigned int` | Calculates the number of processors given the Terra parameters 'mt', 'nt' and 'nd'. mt, nt and nd are Terra parameters (by the same name). |

## Notes

[[[PROSE notes unit=app-logic/GenerateVelocityDomainTerra tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [qt-widgets/GenerateVelocityDomainTerraDialog](../qt-widgets/GenerateVelocityDomainTerraDialog.md) | qt-widgets | 35 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/GenerateVelocityDomainTerra.h
python scripts/gpq.py def GPlatesAppLogic::GenerateVelocityDomainTerra::Grid --body
python scripts/gpq.py uses Grid --kind class
python scripts/gpq.py hier Grid
```
