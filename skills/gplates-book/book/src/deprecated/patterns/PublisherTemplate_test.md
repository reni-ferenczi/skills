# PublisherTemplate_test

[Book TOC](../../../TOC.md) · [deprecated](../../../components/deprecated.md) · cluster Community 339 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/deprecated/patterns/PublisherTemplate_test.cc` | C++ | 360 |

## Overview

[[[PROSE overview unit=deprecated/patterns/PublisherTemplate_test tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

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

[[[PROSE notes unit=deprecated/patterns/PublisherTemplate_test tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

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
