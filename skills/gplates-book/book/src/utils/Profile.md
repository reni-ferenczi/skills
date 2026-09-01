# Profile

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 791 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/Profile.h` | C++ | 343 |
| `src/utils/Profile.cc` | C++ | 1676 |

## Overview

[[[PROSE overview unit=utils/Profile tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=utils/Profile tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
