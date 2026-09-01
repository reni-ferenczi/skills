# PublisherTemplate_test

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 339 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/patterns/PublisherTemplate_test.cc` | C++ | 360 |

## Overview

Test and demonstration file for `PublisherTemplate<T>`, instantiated with a concrete `TestPublisher` and `TestSubscriber` pair. The file exercises all operations on the publisher-subscriber pattern: subscription, unsubscription, notification, copy construction, and assignment, as well as lifetime and cleanup scenarios. It is not compiled into the GPlates executable; instead it serves as a standalone reference implementation showing correct usage of the template.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`TestPublisher`](#testpublisher) | class | [`GPlatesPatterns::PublisherTemplate< TestPublisher >`](PublisherTemplate.md) | — | 0 | — |
| [`TestSubscriber`](#testsubscriber) | class | [`GPlatesPatterns::PublisherTemplate< TestPublisher >::Subscriber`](PublisherTemplate.md) | — | 0 | — |

## Members

### `TestPublisher`

*None.*

### `TestSubscriber`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `receive_notification()` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `main()` | function | `int` | — |
| `describe_subscriber( const TestSubscriber &ts)` | function | `void` | — |
| `describe_publisher( const TestPublisher &tp)` | function | `void` | — |

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/deprecated/patterns/PublisherTemplate_test.cc
python scripts/gpq.py def TestSubscriber --body
python scripts/gpq.py uses TestSubscriber --kind class
python scripts/gpq.py hier TestSubscriber
```
