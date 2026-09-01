# gplates_unit_test_main

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 863 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gplates_unit_test_main.cc` | C++ | 181 |

## Overview

[[[PROSE overview unit=entry-points/gplates_unit_test_main tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `TEST_TO_RUN_OPTION_NAME` | variable | `char` | — |
| `print_usage( std::ostream &os, const GPlatesUtils::CommandLineParser::InputOptions &input_options)` | function | `void` | — |
| `print_usage_and_exit( std::ostream &os, const GPlatesUtils::CommandLineParser::InputOptions &input_options)` | function | `void` | — |
| `get_test_to_run_option( int argc, char* argv[])` | function | `std::string` | — |
| `init_unit_test()` | function | `bool` | — |
| `main(int argc, char* argv[])` | function | `int` | We're using the dynamically-linked version of Boost unit test library (rather than statically linked) because we use dynamic linking for other Boost libraries (such as Boost python) and it is error prone to change the CMake variable ... |

## Notes

[[[PROSE notes unit=entry-points/gplates_unit_test_main tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gplates_unit_test_main.cc
```
