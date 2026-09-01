# Profile

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 791 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Profile.h` | C++ | 343 |
| `src/utils/Profile.cc` | C++ | 1676 |

## Overview

GPlates' own instrumenting CPU profiler — a hand-written gprof, compiled in only
when `GPLATES_PROFILE_CODE` is defined. That comes either from the CMake option
in `cmake/modules/ConfigDefault.cmake` or from the dedicated `ProfileGPlates`
build configuration in `CustomBuildConfigs.cmake`, which is release flags plus
that define. In any ordinary build every macro expands to nothing (`PROFILE_CODE`
expands to its code argument, so the program still works), which is why over a
hundred units can include this header for free. The header itself pulls in only
`<iosfwd>`, `<string>` and `global/config.h`.

What it records is a *call graph*, not a flat timer table. A profiled section is
identified by its name string, so every `PROFILE_BLOCK("foo")` anywhere in the
tree accumulates into one `ProfileNode`; a `ProfileLink` is created per
caller/callee pair, which is what lets the report attribute a node's cost
separately to each of its callers. The live state is a `std::stack<ProfileRun>`
in the `ProfileManager` singleton mirroring the real call stack, with each run
tracking self ticks and children ticks separately — time in a nested profile is
subtracted from its parent, as the long worked example at the top of the header
explains. A permanent `<root>` run sits at the bottom of that stack purely so
mismatched begin/end calls can be detected.

Note the shape of the boundary. Only `ProfileBlockEnd` and five free functions
are in `GPlatesUtils`; `ProfileNode`, `ProfileGraph`, `ProfileManager` and the
rest live in an anonymous namespace inside `Profile.cc` and are unreachable from
anywhere else — which is why the tables above show them as `(anonymous)::`. The
`void *` in `profile_get_cache`/`profile_begin` is a deliberately opaque
`ProfileNode *`, kept opaque so the header need not declare the type.
`PROFILE_BEGIN` stashes that pointer in a function-local `static`, so the
string-to-node map lookup happens once per call site rather than once per hit.
Overhead is engineered throughout: `g_ticks_taken_in_get_ticks_call` is
calibrated at static-initialisation time and subtracted from every measurement,
and `profile_begin`/`profile_end` deliberately call `get_ticks()` only once each,
because the file's own measurements attribute about 90% of profiling cost to
`QueryPerformanceCounter` alone. `PROFILE_EXCLUDE_NEW_DELETE` optionally goes
further and replaces global `operator new`/`delete` so allocation time is
suspended out of the enclosing run.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`(anonymous)::ticks_t`](#anonymousticks_t) | typedef | — | — | 0 | Stores platform-dependent tick count. |
| [`(anonymous)::calls_t`](#anonymouscalls_t) | typedef | — | — | 0 | Stores number of get\_calls to a profiled section of code. |
| [`(anonymous)::ProfileRun`](#anonymousprofilerun) | class | — | — | 0 | Responsible for profiling a running segment of code. |
| [`(anonymous)::ProfileLink`](#anonymousprofilelink) | class | — | — | 0 | Links between ProfileNode objects in the call graph. |
| [`(anonymous)::ProfileNode`](#anonymousprofilenode) | class | — | — | 0 | A node in the call graph that keeps track of time spent in code segments profiled with the same profile name. |
| [`(anonymous)::ProfileGraph`](#anonymousprofilegraph) | class | — | — | 0 | The call graph of profile nodes. |
| [`(anonymous)::ProfileManager`](#anonymousprofilemanager) | class | — | — | 0 | Keeps track of profiles on function call stack. |
| [`(anonymous)::ProfileApiGuard`](#anonymousprofileapiguard) | class | — | — | 0 | Used to set global variable when inside a PROFILE API function. |
| [`GPlatesUtils::ProfileBlockEnd`](#gplatesutilsprofileblockend) | class | — | — | 0 | Calls profile\_end when lifetime of object ends. |

## Members

### `(anonymous)::ticks_t`

*None.*

### `(anonymous)::calls_t`

*None.*

### `(anonymous)::ProfileRun`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ProfileRun( ProfileNode &profile_node)` | constructor | `None` | public | — |
| `ProfileRun( ProfileNode &profile_node, const ticks_t &start_ticks)` | constructor | `None` | public | — |
| `stop_profile( const ticks_t &stop_ticks)` | method | `void` | public | Update the self ticks between now and when the currently profiled object started profiling. |
| `finished_profiling( ProfileRun& parent_run)` | method | `void` | public | Transfer information to the ProfileNode that we're referencing - a parent ProfileRun is passed in if it exists. |
| `get_self_ticks()` | method | `ticks_t` | public | — |
| `get_children_ticks()` | method | `ticks_t` | public | — |
| `get_profile_node()` | method | `ProfileNode` | public | Returns node in call graph associated with this profile run. |
| `d_profile_node` | field | `ProfileNode` | private | — |
| `d_self_ticks` | field | `ticks_t` | private | — |
| `d_children_ticks` | field | `ticks_t` | private | — |
| `d_last_ticks` | field | `ticks_t` | private | — |

### `(anonymous)::ProfileLink`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `profile_link_pool_type` | typedef | `GPlatesUtils::ObjectPool<ProfileLink>` | public | Typedef for pool allocator used to allocate ProfileLink objects. |
| `pointer_type` | typedef | `profile_link_pool_type::shared_object_ptr_type` | public | Shared pointer to ProfileLink object. |
| `create_profile_link( ProfileNode *parent, ProfileNode *child)` | method | `pointer_type` | public | Creates a ProfileLink and connects it between 'parent' and 'child'. |
| `update( const ProfileRun &child_run)` | method | `void` | public | Update with info from a get\_child ProfileRun. |
| `get_calls()` | method | `calls_t` | public | — |
| `get_child()` | method | `ProfileNode` | public | — |
| `get_parent()` | method | `ProfileNode` | public | — |
| `get_ticks_in_child()` | method | `ticks_t` | public | — |
| `get_ticks_in_childs_children()` | method | `ticks_t` | public | — |
| `ProfileLink( const ProfileNode *parent, const ProfileNode *child)` | constructor | `None` | private | — |
| `d_child` | field | `ProfileNode` | private | — |
| `d_parent` | field | `ProfileNode` | private | — |
| `d_ticks_in_child` | field | `ticks_t` | private | — |
| `d_ticks_in_childs_children` | field | `ticks_t` | private | — |
| `d_calls` | field | `calls_t` | private | — |
| `s_profile_link_pool` | field | `profile_link_pool_type` | private | Used to efficiently allocate memory for ProfileLink objects. |

### `(anonymous)::ProfileNode`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `profile_link_map_type` | typedef | `std::map<const ProfileNode *, ProfileLink::pointer_type>` | public | Typedef for a sequence of ProfileNode objects. |
| `profile_link_map_const_iterator` | typedef | `profile_link_map_type::const_iterator` | public | Typedef for a const iterator to a sequence of ProfileNode objects. |
| `ProfileLinkIterator` | class | `None` | public | Iterator links in the call graph eminating from a ProfileNode object. |
| `profile_count_const_iterator` | typedef | `ProfileLinkIterator` | public | Iterator over sequence of ProfileNode objects. |
| `ProfileNode( const std::string &profileName)` | constructor | `None` | public | — |
| `update( const ProfileRun &run, ProfileNode &parent)` | method | `void` | public | Updates this profile node with profile counts in run and updates link to parent node. |
| `get_self_ticks()` | method | `ticks_t` | public | The number of ticks counted - not including children. |
| `parent_profiles_begin()` | method | `profile_count_const_iterator` | public | — |
| `parent_profiles_end()` | method | `profile_count_const_iterator` | public | — |
| `child_profiles_begin()` | method | `profile_count_const_iterator` | public | — |
| `child_profiles_end()` | method | `profile_count_const_iterator` | public | — |
| `d_name` | field | `std::string` | private | — |
| `d_self_ticks` | field | `ticks_t` | private | — |
| `d_parent_profiles` | field | `profile_link_map_type` | private | — |
| `d_child_profiles` | field | `profile_link_map_type` | private | — |
| `d_most_recent_parent` | field | `ProfileNode` | private | Used for speed optimisation purposes to try and avoid searching d\_parent\_profiles. |
| `d_most_recent_parent_link` | field | `ProfileLink` | private | Used for speed optimisation purposes to try and avoid searching d\_parent\_profiles. |
| `get_parent_link( ProfileNode *parent_node)` | method | `ProfileLink` | private | Returns reference to parent link corresponding to parent\_node. |
| `create_call_graph_link( ProfileNode *parent, ProfileNode *child)` | method | `void` | private | Creates a ProfileLink and connects it between 'parent' and 'child'. |

### `(anonymous)::ProfileGraph`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `profile_node_seq_type` | typedef | `std::vector<const ProfileNode *>` | public | Sequence of ProfileNode objects. |
| `get_or_create_profile_node_by_name` | field | `ProfileNode` | public | Returns a ProfileNode object for 'profile\_name' - creates one if necessary. |
| `get_call_graph()` | method | `profile_node_seq_type` | public | Returns the sequence of all ProfileNode objects in the call graph. |
| `profile_node_map_type` | typedef | `std::map<std::string, ProfileNode>` | private | Maps profile name to ProfileNode object. |
| `d_profile_node_map` | field | `profile_node_map_type` | private | — |

### `(anonymous)::ProfileManager`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~ProfileManager()` | destructor | `None` | public | — |
| `get_profile_cache( const char *profile_name)` | method | `void` | public | An optimisation to avoid repeated lookups of the profile\_name string to find the ProfileNode each time the same segment of source code is profiled. |
| `start_profile` | field | `ticks_t` | public | Called when starting a profile run for 'profile\_cache'. suspend\_profile\_time is the time just when profile is first started. |
| `stop_profile` | field | `ticks_t` | public | Called when stopping a profile run. suspend\_profile\_time is the time just when profile is first stopped. |
| `start_current_profile` | field | `ticks_t` | public | Called when restarting the current profile run after a call to stop\_current\_profile. |
| `stop_current_profile( const ticks_t &suspend_time)` | method | `void` | public | Called when stopping the current profile run. |
| `have_all_profile_runs_finished()` | method | `bool` | public | Returns true if all profile runs have finished. |
| `does_profile_manager_exist()` | method | `bool` | public | Is true if ProfileManager singleton object is constructed and not yet destructed. |
| `ProfileManager()` | constructor | `None` | private | — |
| `d_root_profile_node` | field | `ProfileNode` | private | Root profile node. |
| `d_profile_graph` | field | `ProfileGraph` | private | Contains profile call graph. |
| `d_profile_run_stack` | field | `std::stack<ProfileRun>` | private | Stack of profile runs that are currently following the call stack. |
| `s_does_profile_manager_exist` | field | `bool` | private | Is true if ProfileManager singleton object is constructed and not yet destructed. |

### `(anonymous)::ProfileApiGuard`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ProfileApiGuard()` | constructor | `None` | public | — |
| `~ProfileApiGuard()` | destructor | `None` | public | — |
| `is_inside_profile_api()` | method | `bool` | public | Returns true if we're currently inside a PROFILE API function. |
| `s_inside_profile_api` | field | `bool` | private | Is true if we're currently inside a PROFILE API function. |
| `s_profile_api_nested_depth` | field | `int` | private | Nested call depth inside a PROFILE API function. |

### `GPlatesUtils::ProfileBlockEnd`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ProfileBlockEnd()` | constructor | `None` | public | — |
| `dismiss()` | method | `void` | public | — |
| `~ProfileBlockEnd()` | destructor | `None` | public | — |
| `d_dismiss` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `NOMINMAX` | macro | `None` | — |
| `convert_ticks_to_seconds( ticks_t)` | function | `double` | Converts ticks to seconds. |
| `convert_seconds_to_ticks( double)` | function | `ticks_t` | Converts seconds to ticks. |
| `s_profile_link_pool` | variable | `ProfileLink::profile_link_pool_type` | — |
| `get_ticks( const ProfileLink *profile_link)` | function | `ticks_t` | — |
| `calc_total_calls_from_parents( const ProfileNode *profile_node)` | function | `calls_t` | — |
| `calc_ticks_in_all_children( const ProfileNode *profile_node)` | function | `ticks_t` | — |
| `calc_ticks_in_profile_node_and_all_its_children( const ProfileNode *profile_node)` | function | `ticks_t` | — |
| `s_does_profile_manager_exist` | variable | `bool` | — |
| `print_accurate_time(double seconds, std::ostream &output_stream, int field_width)` | function | `void` | Printing of profiling statistics |
| `report_flat_profile( std::ostream &output_stream, const ProfileGraph &profile_graph, const ticks_t total_ticks)` | function | `void` | — |
| `report_call_graph_profile( std::ostream &output_stream, const ProfileGraph &profile_graph, const ticks_t total_ticks)` | function | `void` | — |
| `report( const ProfileGraph &profile_graph, std::ostream &output_stream)` | function | `void` | Prints out a report of this call graph to output\_stream (if any profiling has been done). |
| `get_ticks()` | function | `ticks_t` | — |
| `get_seconds_per_tick()` | function | `double` | — |
| `convert_ticks_to_seconds( ticks_t ticks)` | function | `double` | Converts ticks to seconds. |
| `convert_seconds_to_ticks( double seconds)` | function | `ticks_t` | Converts seconds to ticks. |
| `calc_ticks_taken_in_get_ticks_call()` | function | `ticks_t` | Calculates the time taken to execute a call to 'get\_ticks()' in ticks. |
| `g_ticks_taken_in_get_ticks_call` | variable | `ticks_t` | Actual time taken in 'get\_ticks()' call in ticks. |
| `s_inside_profile_api` | variable | `bool` | — |
| `s_profile_api_nested_depth` | variable | `int` | — |
| `g_inside_new_count` | variable | `int` | — |
| `g_inside_delete_count` | variable | `int` | — |
| `operator new( size_t bytes)` | operator | `void` | FIXME: This is not really thread-safe. |
| `operator delete( void *ptr)` | operator | `void` | — |
| `operator new []( size_t bytes)` | operator | `void` | — |
| `operator delete []( void *ptr)` | operator | `void` | — |
| `profile_get_cache( const char *profile_name)` | function | `void` | — |
| `profile_begin( void *profile_cache)` | function | `void` | — |
| `profile_end()` | function | `void` | — |
| `profile_report_to_ostream( std::ostream &output_stream)` | function | `void` | — |
| `profile_report_to_file( const std::string &filename)` | function | `void` | — |
| `GPLATES_UTILS_PROFILE_H` | macro | `None` | — |
| `PROFILE_BEGIN` | macro_function | `static void *PROFILE_ANONYMOUS_VARIABLE(gplates_profile_cache) = \ GPlatesUtils::profile_get_cache(name); \` | Starts profiling until the matching PROFILE\_END is reached or an exception is thrown or the function we're in returns early. name is a string of type "const char \*". |
| `PROFILE_SCOPE_VARIABLE(profile_tag)` | function | `GPlatesUtils::ProfileBlockEnd` | Make sure PROFILE\_END() is called if it is not reached - \*/ \\ this can happen if an exception is thrown or function 'return's early. \*/ \\ |
| `PROFILE_END` | macro_function | `PROFILE_SCOPE_VARIABLE(profile_tag).dismiss(); \` | Stops profiling the matching PROFILE\_BEGIN call. |
| `name` | macro | `);` | Starts profiling until the end of the current scope in which this PROFILE\_BLOCK call was made. |
| `PROFILE_FUNC` | macro_function | `PROFILE_BLOCK(__FUNCTION__);` | Same as PROFILE\_BLOCK except the name of the profile is the function that PROFILE\_BLOCK is called from. |
| `PROFILE_CODE` | macro_function | `PROFILE_BEGIN(PROFILE_CONCATENATE(code_, profile_tag), #code); \ { \ code; \ } \ PROFILE_END(PROFILE_CONCATENATE(code_, profile_tag));` | Starts profiling just before the source code expression code and stops profiling just after. profile\_tag is only used internally to match PROFILE\_BEGIN and PROFILE\_END calls. profile\_tag is an identifier and must use C++ naming rules. ... |
| `PROFILE_REPORT_TO_OSTREAM` | macro_function | `GPlatesUtils::profile_report_to_ostream(output_stream);` | Writes the profiling data as text to the output stream output\_stream where output\_stream is a std::ostream &. |
| `PROFILE_REPORT_TO_FILE` | macro_function | `GPlatesUtils::profile_report_to_file(filename);` | Writes the profiling data as text to the file filename where filename is a std::string. |
| `PROFILE_CONCATENATE_DIRECT` | macro_function | `s1##s2` | — |
| `PROFILE_CONCATENATE` | macro_function | `PROFILE_CONCATENATE_DIRECT(s1, s2)` | — |
| `PROFILE_SCOPE_VARIABLE` | macro_function | `PROFILE_CONCATENATE(gplates_profile_scope_, name)` | — |
| `PROFILE_ANONYMOUS_VARIABLE` | macro_function | `PROFILE_CONCATENATE(name, __LINE__)` | — |
| `PROFILE_UNUSED` | macro | `__attribute__ ((unused))` | — |
| `profile_get_cache( const char *name)` | function | `void` | — |
| `profile_report_to_ostream( std::ostream &)` | function | `void` | — |

## Notes

- **Single-threaded by construction.** One global `ProfileManager` with one
  `std::stack<ProfileRun>` models one call stack. Profiling code that runs on
  more than one thread interleaves runs from different threads into the same
  stack and produces nonsense. The `operator new` override carries an explicit
  FIXME saying it is not thread-safe either, and that a mutex was rejected as
  costing more than the feature is worth.
- **Begin/end must balance exactly.** An extra `PROFILE_END` empties the stack
  past the `<root>` sentinel and throws `AssertionFailureException` after writing
  to `std::cerr`; a missing one is caught later, when `profile_report_to_ostream`
  finds runs still open and throws for the same reason. `ProfileBlockEnd` covers
  the normal escapes — an exception or an early `return` between `PROFILE_BEGIN`
  and `PROFILE_END` still ends the run, because `PROFILE_END` merely `dismiss()`es
  a scope guard the begin macro already declared.
- **`profile_tag` must be unique within a scope.** `PROFILE_BLOCK` and
  `PROFILE_FUNC` use `__LINE__` as the tag *and* `__LINE__` to suffix the cache
  variable, so two of them on the same source line collide at compile time.
- **Ticks are platform-defined and not comparable.** Windows returns raw
  `QueryPerformanceCounter` counts; elsewhere a tick is fixed at 0.1 microseconds
  derived from `gettimeofday`. Only seconds, via `convert_ticks_to_seconds`, mean
  anything across platforms.
- **Calibration runs at static-init time.** `g_ticks_taken_in_get_ticks_call` is
  a namespace-scope constant whose initialiser times up to ten loops of a
  thousand `get_ticks()` calls, retrying if a context switch makes a loop look
  too slow. In a profile build that cost is paid at startup whether or not
  anything is ever profiled.
- **`s_does_profile_manager_exist` guards shutdown.** The `new`/`delete` hooks
  are global and outlive the singleton, so they check that flag before touching
  `ProfileManager::instance()`.
- **Measurement floor.** The file comment is blunt: each begin/end pair costs
  roughly 1.2 microseconds, so a section of that order is unmeasurable and
  profiling it can halve the program's speed. And any other CPU-consuming process
  on the machine is charged to whatever section was running.
- **A backwards or equal clock silently drops the sample.** `ProfileRun::stop_profile`
  only accumulates when `d_last_ticks < stop_ticks`, avoiding unsigned underflow
  at the cost of losing the measurement.
- `ProfileLink` objects come from a file-static `GPlatesUtils::ObjectPool` and are
  held by `shared_ptr` from *both* the parent's and the child's link map, so an
  edge lives as long as either endpoint's map entry.
- `ProfileNode::get_parent_link` caches the most recent parent to skip the
  `std::map` lookup, which is the case that matters for a profiled tight loop.
- **`PROFILE_EXCLUDE_NEW_DELETE` needs linker help on Windows** — the header notes
  that `/FORCE:MULTIPLE` is required to get past duplicate `operator new`/`delete`
  symbols. Only the four basic forms are overridden; the file flags the rest as a
  FIXME.

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/ReconstructContext](../app-logic/ReconstructContext.md) | app-logic | 8 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 8 |
| [opengl/GLNormalMapSource](../opengl/GLNormalMapSource.md) | opengl | 8 |
| [opengl/GLVisualLayers](../opengl/GLVisualLayers.md) | opengl | 8 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 7 |
| [app-logic/TopologyUtils](../app-logic/TopologyUtils.md) | app-logic | 7 |
| [file-io/MipmappedRasterFormatWriter](../file-io/MipmappedRasterFormatWriter.md) | file-io | 7 |
| [opengl/GLAgeGridMaskSource](../opengl/GLAgeGridMaskSource.md) | opengl | 7 |
| [opengl/GLScalarFieldDepthLayersSource](../opengl/GLScalarFieldDepthLayersSource.md) | opengl | 7 |
| [file-io/RgbaRasterReader](../file-io/RgbaRasterReader.md) | file-io | 6 |
| [opengl/GLState](../opengl/GLState.md) | opengl | 6 |
| [unit-test/MultiThreadTest](../unit-test/MultiThreadTest.md) | unit-test | 6 |
| [file-io/GdalRasterReader](../file-io/GdalRasterReader.md) | file-io | 5 |
| [gui/Mipmapper](../gui/Mipmapper.md) | gui | 5 |
| [opengl/GLDataRasterSource](../opengl/GLDataRasterSource.md) | opengl | 5 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 5 |
| [app-logic/DependentTopologicalSectionLayers](../app-logic/DependentTopologicalSectionLayers.md) | app-logic | 4 |
| [app-logic/ScalarCoverageEvolution](../app-logic/ScalarCoverageEvolution.md) | app-logic | 4 |
| [app-logic/TopologyReconstruct](../app-logic/TopologyReconstruct.md) | app-logic | 4 |
| [opengl/GLMultiResolutionRaster](../opengl/GLMultiResolutionRaster.md) | opengl | 4 |

*... and 80 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/Profile.h
python scripts/gpq.py def (anonymous)::ProfileNode --body
python scripts/gpq.py uses ProfileNode --kind class
python scripts/gpq.py hier ProfileNode
```
