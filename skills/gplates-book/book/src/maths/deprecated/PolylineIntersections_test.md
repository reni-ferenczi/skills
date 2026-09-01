# PolylineIntersections_test

[Book TOC](../../../TOC.md) · [maths](../../../components/maths.md) · cluster Community 99 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/maths/deprecated/PolylineIntersections_test.cc` | C++ | 3999 |

## Overview

Automated regression test suite for the `PolylineIntersections::partition_intersecting_polylines` function, which finds intersection points between two polylines on a sphere and partitions them accordingly. The test file contains helper utilities for comparing polylines, constructing test data in lat/lon format, and running a comprehensive suite of test cases covering scenarios like coincident endpoints, no intersections, tangential intersections, and cases where Euclidean geometry would give different results than spherical geometry. Was originally designed to run by replacing `GPlatesApp.cc` directly.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`PointIsCoincident`](#pointiscoincident) | class | `std::unary_function< GPlatesMaths::PointOnSphere, bool >` | — | 0 | — |
| [`PointListType`](#pointlisttype) | enum | — | — | 0 | — |
| [`Point`](#point) | struct | — | — | 0 | — |
| [`PointOnSphereOstreamIterator`](#pointonsphereostreamiterator) | class | [`std::iterator< std::output_iterator_tag, GPlatesMaths::PointOnSphere >`](../../app-logic/LayerProxyUtils.md) | — | 0 | — |
| [`PointOnSphereAppender`](#pointonsphereappender) | class | — | `< typename C >` | 0 | — |
| [`TestResults::TestResult`](#testresultstestresult) | enum | — | — | 0 | — |

## Members

### `PointIsCoincident`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PointIsCoincident( const GPlatesMaths::PointOnSphere &p)` | constructor | `None` | public | — |
| `operator()( const GPlatesMaths::PointOnSphere &other_p)` | operator | `bool` | public | — |
| `d_p` | field | `GPlatesMaths::PointOnSphere` | private | — |

### `PointListType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `POINT_TYPE` | enumerator | `None` | — | — |
| `EOP_TYPE` | enumerator | `None` | — | — |
| `EOL_TYPE` | enumerator | `None` | — | — |

### `Point`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `lat` | field | `GPlatesMaths::real_t` | public | — |
| `lon` | field | `GPlatesMaths::real_t` | public | — |
| `point_list_type` | field | `PointListType` | public | — |

### `PointOnSphereOstreamIterator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PointOnSphereOstreamIterator( std::ostream &os, const char *delim = "")` | constructor | `None` | public | — |
| `operator=( const GPlatesMaths::PointOnSphere &p)` | operator | `void` | public | — |
| `operator++(int)` | operator | `PointOnSphereOstreamIterator` | public | — |
| `d_os_ptr` | field | `std::ostream` | private | — |
| `d_delim` | field | `std::string` | private | — |

### `PointOnSphereAppender`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PointOnSphereAppender( C &coll)` | constructor | `None` | public | — |
| `operator()( const Point &p)` | operator | `void` | public | — |
| `d_coll_ptr` | field | `C` | private | — |

### `TestResults::TestResult`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PASS` | enumerator | `None` | — | — |
| `FAIL` | enumerator | `None` | — | — |
| `ERROR` | enumerator | `None` | — | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `sets_of_polyline_are_undirected_equivalent( const std::list< GPlatesMaths::PolylineOnSphere > &s1, const std::list< GPlatesMaths::PolylineOnSphere > &s2)` | function | `bool` | — |
| `sets_of_T_are_equivalent_by_predicate( const std::list< T > &s1, const std::list< T > &s2)` | function | `bool` | — |
| `Point_to_PointOnSphere( const Point &p)` | function | `GPlatesMaths::PointOnSphere` | — |
| `operator=( const GPlatesMaths::PointOnSphere &p)` | operator | `void` | — |
| `make_poly( const Point *array)` | function | `GPlatesMaths::PolylineOnSphere` | — |
| `make_polys( std::list< GPlatesMaths::PolylineOnSphere > &polys, const Point *array)` | function | `void` | — |
| `make_points( std::list< GPlatesMaths::PointOnSphere > &points, const Point *array)` | function | `void` | — |
| `NUM_ELEMS` | macro_function | `(sizeof(a) / sizeof((a)[0]))` | — |
| `POINT` | macro_function | `{ (lat), (lon), POINT_TYPE }` | — |
| `BREAK_BETWEEN_POLYS` | macro | `{ 0, 0, EOP_TYPE }` | — |
| `END_OF_LIST` | macro | `{ 0, 0, EOL_TYPE }` | — |
| `partition_and_verify( const Point input_polyline1_point_array[], const Point input_polyline2_point_array[], const Point expected_intersection_points_point_array[], const Point expected_partitioned_polylines_point_array[], const char funcname[])` | function | `TestResults::TestResult` | — |
| `test_no_intersection_both_of_length_one()` | function | `TestResults::TestResult` | — |
| `test_no_intersection_both_of_length_one_on_same_great_circle_1()` | function | `TestResults::TestResult` | — |
| `test_no_intersection_both_of_length_one_on_same_great_circle_2()` | function | `TestResults::TestResult` | — |
| `test_no_intersection_due_to_spherical_geometry()` | function | `TestResults::TestResult` | If we were working in a 2-D plane, the middle segments of polyline1 and polyline2 would overlap, but because we're working on the surface of the sphere, there is no intersection. |
| `test_intersection_both_of_length_one()` | function | `TestResults::TestResult` | — |
| `test_intersection_coincident_with_one_vertex_lengths_one_two()` | function | `TestResults::TestResult` | — |
| `test_intersection_coincident_with_two_vertices_both_of_length_two()` | function | `TestResults::TestResult` | — |
| `test_intersection_coincident_with_two_vertices_both_of_length_four()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_end_no_intersection_both_of_length_one()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_start_no_intersection_both_of_length_one()` | function | `TestResults::TestResult` | — |
| `test_touching_start_to_end_no_intersection_both_of_length_one()` | function | `TestResults::TestResult` | — |
| `test_touching_start_to_start_no_intersection_both_of_length_one()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_end_no_intersection_both_of_length_two()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_start_no_intersection_both_of_length_two()` | function | `TestResults::TestResult` | — |
| `test_touching_start_to_end_no_intersection_both_of_length_two()` | function | `TestResults::TestResult` | — |
| `test_touching_start_to_start_no_intersection_both_of_length_two()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_mid_intersection_both_of_length_one()` | function | `TestResults::TestResult` | — |
| `test_touching_start_to_mid_intersection_both_of_length_one()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_mid_intersection_both_of_length_one_meet_perp()` | function | `TestResults::TestResult` | — |
| `test_touching_start_to_mid_intersection_both_of_length_one_meet_perp()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_mid_intersection_both_of_length_two_1()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_mid_intersection_both_of_length_two_2()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_mid_intersection_both_of_length_two_3()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_mid_intersection_both_of_length_two_4()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_mid_intersection_lengths_two_three()` | function | `TestResults::TestResult` | — |
| `test_touching_end_to_vertex_intersection_both_of_length_two()` | function | `TestResults::TestResult` | — |
| `test_overlap_defined_by_polyline1_parallel_arcs()` | function | `TestResults::TestResult` | — |
| `test_overlap_defined_by_polyline1_antiparallel_arcs()` | function | `TestResults::TestResult` | — |
| `test_overlap_defined_by_polyline2_parallel_arcs()` | function | `TestResults::TestResult` | — |
| `test_overlap_defined_by_polyline2_antiparallel_arcs()` | function | `TestResults::TestResult` | — |
| `test_same_polyline()` | function | `TestResults::TestResult` | Test that the intersection function does indeed handle duplicate polyline arguments in the way it says it will: partitioning the two overlapping polylines at every vertex and breaking the polylines down into their component segments. |
| `test_overlap_partial_both_of_length_one_1()` | function | `TestResults::TestResult` | Test that the intersection function correctly handles the situation when a segment of one polyline partially overlaps with the other. |
| `test_overlap_partial_both_of_length_one_2()` | function | `TestResults::TestResult` | Test that the intersection function correctly handles the situation when a segment of one polyline partially overlaps with the other. |
| `test_overlap_partial_both_of_length_one_3()` | function | `TestResults::TestResult` | Test that the intersection function correctly handles the situation when a segment of one polyline partially overlaps with the other. |
| `test_overlap_partial_both_of_length_one_4()` | function | `TestResults::TestResult` | Test that the intersection function correctly handles the situation when a segment of one polyline partially overlaps with the other. |
| `test_overlap_partial_both_of_length_three_middle_segment_to_middle_1()` | function | `TestResults::TestResult` | Test that the intersection function correctly handles the situation when the middle segment of one three-segment polyline partially overlaps with the middle segment of the other. |
| `test_overlap_partial_both_of_length_three_middle_segment_to_middle_2()` | function | `TestResults::TestResult` | Test that the intersection function correctly handles the situation when the middle segment of one three-segment polyline partially overlaps with the middle segment of the other. |
| `test_overlap_partial_both_of_length_three_middle_segment_to_middle_3()` | function | `TestResults::TestResult` | Test that the intersection function correctly handles the situation when the middle segment of one three-segment polyline partially overlaps with the middle segment of the other. |
| `test_overlap_partial_both_of_length_three_middle_segment_to_middle_4()` | function | `TestResults::TestResult` | Test that the intersection function correctly handles the situation when the middle segment of one three-segment polyline partially overlaps with the middle segment of the other. |
| `test_multi_intersection_4()` | function | `TestResults::TestResult` | — |
| `test_multi_intersection_5()` | function | `TestResults::TestResult` | — |
| `test_multi_intersection_6()` | function | `TestResults::TestResult` | — |
| `test_multi_intersection_7()` | function | `TestResults::TestResult` | Test that the intersection function correctly handles the situation when one polyline intersects multiple times with a single segment of the other. |
| `test_multi_intersection_8()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_intersection\_7 except that the direction of polyline1 has been reversed. |
| `test_multi_intersection_9()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_intersection\_7 except that the geometries of polyline1 and polyline2 have been swapped. |
| `test_multi_intersection_10()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_intersection\_9 except that the direction of polyline1 has been reversed. |
| `test_multi_intersection_11()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_intersection\_7 except that the third point of intersection is now between the first two. |
| `test_multi_intersection_12()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_intersection\_11 except that the direction of polyline1 has been reversed. |
| `test_multi_intersection_13()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_intersection\_11 except that the geometries of polyline1 and polyline2 have been swapped. |
| `test_multi_intersection_14()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_intersection\_13 except that the direction of polyline1 has been reversed. |
| `test_multi_overlap_1()` | function | `TestResults::TestResult` | This case tests two different configurations of overlap between two polylines: one overlap of identical segments and one overlap of a smaller segment contained within a larger segment. |
| `test_multi_overlap_2()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_overlap\_1 except that the geometries of polyline1 and polyline2 have been swapped. |
| `test_multi_overlap_3()` | function | `TestResults::TestResult` | This case tests the situation when polyline1 overlaps twice with a single segment of polyline2. |
| `test_multi_overlap_4()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_overlap\_4 except that the direction of polyline1 has been reversed. |
| `test_multi_overlap_5()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_overlap\_3 except that the geometries of polyline1 and polyline2 have been swapped. |
| `test_multi_overlap_6()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_overlap\_5 except that the direction of polyline1 has been reversed. |
| `test_multi_overlap_7()` | function | `TestResults::TestResult` | This case tests the situation when a single segment of polyline1 overlaps partially with two adjacent, parallel segments of polyline2. |
| `test_multi_overlap_8()` | function | `TestResults::TestResult` | This test case is the same as test\_multi\_overlap\_7 except that the geometries of polyline1 and polyline2 have been swapped. |
| `test_multi_overlap_and_intersection_1()` | function | `TestResults::TestResult` | — |
| `test_multi_overlap_and_intersection_2()` | function | `TestResults::TestResult` | — |
| `test_multi_overlap_and_intersection_3()` | function | `TestResults::TestResult` | — |
| `ALL_TESTS` | variable | `test_fn_t` | — |
| `run_test( test_fn_t f)` | function | `TestResults::TestResult` | — |
| `run_tests()` | function | `void` | — |

## Notes

This test file is deprecated and was designed to run as a replacement for `GPlatesApp.cc`, which was an early testing mechanism. It should not be compiled into GPlates unless explicitly running these regression tests. The tests use a custom `Point` structure with lat/lon coordinates for test data specification and include helper functors and iterators for comparing polyline sets and constructing test fixtures.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/maths/deprecated/PolylineIntersections_test.cc
python scripts/gpq.py def PointOnSphereOstreamIterator --body
python scripts/gpq.py uses PointOnSphereOstreamIterator --kind class
python scripts/gpq.py hier PointOnSphereOstreamIterator
```
