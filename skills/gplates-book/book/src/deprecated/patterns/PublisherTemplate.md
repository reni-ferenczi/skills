# PublisherTemplate

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 339 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/patterns/PublisherTemplate.h` | C++ | 685 |

## Overview

[[[PROSE overview unit=deprecated/patterns/PublisherTemplate tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPatterns::PublisherTemplate`](#gplatespatternspublishertemplate) | class | — | `< typename T >` | 1 | @attention Note that a class may be both a publisher and a subscriber to a different publisher. @section details Details - Publishers do not advertise an explicit ordering of their subscribers. - There are no automatic actions triggered ... |

## Members

### `GPlatesPatterns::PublisherTemplate`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `PublisherType` | typedef | `T` | public | — |
| `PublisherBaseType` | typedef | `PublisherTemplate< T >` | public | — |
| `Subscriber` | class | `None` | public | This class is the abstract base class of all subscribers to publishers of type PublisherTemplate\< X \>. |
| `Subscribers` | typedef | `std::list< Subscriber * >` | public | — |
| `size_type` | typedef | `typename Subscribers::size_type` | public | — |
| `PublisherTemplate()` | constructor | `None` | public | This function is strongly exception-safe and exception-neutral. |
| `~PublisherTemplate()` | destructor | `None` | public | This function will not throw. |
| `num_subscribers()` | method | `size_type` | public | Return the current number of subscribers. |
| `notify_subscribers()` | method | `void` | public | Notify all subscribers that an event has occurred. |
| `append_subscriber( Subscriber &s)` | method | `void` | public | Subscribe the subscriber s to this publisher. |
| `remove_subscriber( Subscriber &s)` | method | `void` | public | Unsubscribe the subscriber s from this publisher. |
| `remove_all_subscribers()` | method | `void` | public | Unsubscribe all subscribers from this publisher. |
| `m_subscribers` | field | `Subscribers` | private | The current subscribers to this publisher. |
| `remove( Subscriber &s)` | method | `void` | private | Remove subscriber s from m\_subscribers. |
| `splice_out( const Subscriber &s, Subscribers &into_this)` | method | `void` | private | Splice subscriber s out of m\_subscribers, into the list of subscribers into\_this. |
| `splice_in( Subscribers &from_this)` | method | `void` | private | Splice the contents of the list of subscribers from\_this into m\_subscribers. |
| `PublisherTemplate( const PublisherTemplate &)` | constructor | `None` | private | Declare the copy-constructor private, because copy-construction doesn't make sense for publishers. |
| `operator=` | field | `PublisherTemplate` | private | Declare the assignment operator private, because assignment doesn't make sense for publishers. |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PATTERNS_PUBLISHERTEMPLATE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=deprecated/patterns/PublisherTemplate tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [deprecated/patterns/PublisherTemplate_test](PublisherTemplate_test.md) | deprecated | 28 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/patterns/PublisherTemplate.h
python scripts/gpq.py def GPlatesPatterns::PublisherTemplate --body
python scripts/gpq.py uses PublisherTemplate --kind class
python scripts/gpq.py hier PublisherTemplate
```
