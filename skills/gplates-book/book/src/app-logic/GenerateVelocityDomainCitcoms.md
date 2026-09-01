# GenerateVelocityDomainCitcoms

[Book TOC](../../TOC.md) · [app-logic](../../components/app-logic.md) · cluster Community 573 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/app-logic/GenerateVelocityDomainCitcoms.h` | C++ | 57 |
| `src/app-logic/GenerateVelocityDomainCitcoms.cc` | C++ | 423 |

## Overview

[[[PROSE overview unit=app-logic/GenerateVelocityDomainCitcoms tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::Mesh`](#anonymousmesh) | class | — | — | 0 | — |

## Members

### `(anonymous)::Mesh`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Mesh( int node_x=1)` | constructor | `None` | public | — |
| `get_diamonds_points( unsigned index, std::vector<GPlatesMaths::PointOnSphere> &points)` | method | `void` | public | Given the index of the diamond, return all the points |
| `CapDiamond` | class | `None` | private | — |
| `d_node_x` | field | `int` | private | — |
| `d_cap_diamonds` | field | `std::vector<CapDiamond>` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `MY_PI` | variable | `double` | — |
| `OFFSET` | variable | `double` | — |
| `DIAMONDS_MUNBER` | variable | `int` | — |
| `even_divide_arc( int elx, double x1, double y1, double z1, double x2, double y2, double z2, std::vector<double> &theta, std::vector<double> &fi)` | function | `void` | — |
| `convert_coord( const double &theta, const double &fi, double &x, double &y, double &z)` | function | `void` | — |
| `create_vertex( double theta, double fi)` | function | `GPlatesMaths::PointOnSphere` | — |
| `GENERATE_VELOCITY_DOMAIN_CITCOMS_H` | macro | `None` | — |
| `generate_velocity_domains( int node_x, std::vector<GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type> &geometries)` | function | `void` | Given the resolution, return the mesh diamond geometries There are 12 MultiPoint Geometries in this case. |
| `generate_velocity_domain( int node_x, unsigned index)` | function | `GPlatesMaths::MultiPointOnSphere::non_null_ptr_to_const_type` | Given the resolution and index number, return the mesh diamond geometry |

## Notes

[[[PROSE notes unit=app-logic/GenerateVelocityDomainCitcoms tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [unit-test/GenerateVelocityDomainCitcomsTest](../unit-test/GenerateVelocityDomainCitcomsTest.md) | unit-test | 4 |
| [qt-widgets/GenerateVelocityDomainCitcomsDialog](../qt-widgets/GenerateVelocityDomainCitcomsDialog.md) | qt-widgets | 3 |
| [unit-test/AppLogicTestSuite](../unit-test/AppLogicTestSuite.md) | unit-test | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/app-logic/GenerateVelocityDomainCitcoms.h
python scripts/gpq.py def (anonymous)::Mesh --body
python scripts/gpq.py uses Mesh --kind class
python scripts/gpq.py hier Mesh
```
