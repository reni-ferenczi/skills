# PublisherTemplate

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 339 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/patterns/PublisherTemplate.h` | C++ | 685 |

## Overview

A template-based implementation of the Observer/Publisher-Subscriber pattern that makes event notification type-safe through inheritance-based mixin style base classes. Classes become publishers by inheriting from `PublisherTemplate<T>`, while subscriber types inherit from `PublisherTemplate<T>::Subscriber` and define `receive_notification()`. The pattern handles automatic cleanup: publishers automatically unsubscribe all subscribers upon destruction, and subscribers automatically unsubscribe themselves before being destroyed.

The implementation provides subscription and unsubscription operations callable from either the publisher or subscriber side, with idempotent semantics (attempting to subscribe an already-subscribed subscriber or unsubscribe a non-subscribed one are safe no-ops). All operations are strongly exception-safe and exception-neutral. A single class can be both a publisher and subscriber to different publishers simultaneously, though the type system prevents a class from inheriting from multiple publisher or multiple subscriber base classes.

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

Copy-construction and copy-assignment are disabled for `PublisherTemplate` itself because they violate the invariant that a subscriber can only be subscribed to one publisher: copying a publisher would require copying its subscriber list, but those subscribers would still be subscribed to the original publisher. Subscribers' copy-constructor and assignment operator are protected and update subscription state to match the source; derived classes must explicitly invoke them in their own copy operations. All methods safely handle NULL state: `Subscriber::unsubscribe()` is a no-op if not subscribed, `append_subscriber()` is a no-op if already subscribed, and `remove_subscriber()` is a no-op if not subscribed to this publisher. Subscriber destruction automatically unsubscribes to prevent dangling pointers, and publisher destruction automatically calls `unsubscribe()` on all subscribers.

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
