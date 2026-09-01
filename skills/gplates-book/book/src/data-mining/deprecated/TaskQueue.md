# TaskQueue

[Book TOC](../../../TOC.md) · [data-mining](../../../components/data-mining.md) · cluster Community 397 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/data-mining/deprecated/TaskQueue.h` | C++ | 189 |

## Overview

[[[PROSE overview unit=data-mining/deprecated/TaskQueue tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesDataMining::TaskScheduler`](#gplatesdataminingtaskscheduler) | class | — | — | 0 | — |
| [`GPlatesDataMining::TaskQueue`](#gplatesdataminingtaskqueue) | class | — | — | 0 | — |

## Members

### `GPlatesDataMining::TaskScheduler`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TaskScheduler(TaskQueue*)` | constructor | `None` | public | — |
| `operator()()` | operator | `void` | public | — |
| `d_task_queue` | field | `TaskQueue` | private | — |

### `GPlatesDataMining::TaskQueue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TaskQueue()` | constructor | `None` | public | — |
| `~TaskQueue()` | destructor | `None` | public | — |
| `init()` | method | `void` | public | — |
| `add(Prospector* r)` | method | `void` | public | — |
| `fetch()` | method | `Prospector` | public | — |
| `shutdown()` | method | `void` | public | — |
| `shutdown_flag()` | method | `bool` | public | — |
| `d_wait_queue_mux` | field | `boost::mutex` | private | — |
| `d_shutdown_mux` | field | `boost::mutex` | private | — |
| `d_done_queue_mux` | field | `boost::mutex` | private | — |
| `d_queue_empty_cond` | field | `boost::condition` | private | — |
| `d_wait_task_cond` | field | `boost::condition` | private | — |
| `d_shutdown` | field | `bool` | private | — |
| `d_wait_queue` | field | `std::queue < Prospector* >` | private | — |
| `d_done_queue` | field | `std::queue < Prospector* >` | private | — |
| `d_threads` | field | `std::vector <boost::thread* >` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATESDATAMINING_TASKQUEUE_H` | macro | `None` | — |
| `MaxConcurrentThreads` | macro | `4` | — |
| `operator()()` | operator | `void` | — |

## Notes

[[[PROSE notes unit=data-mining/deprecated/TaskQueue tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/data-mining/deprecated/TaskQueue.h
python scripts/gpq.py def GPlatesDataMining::TaskQueue --body
python scripts/gpq.py uses TaskQueue --kind class
python scripts/gpq.py hier TaskQueue
```
