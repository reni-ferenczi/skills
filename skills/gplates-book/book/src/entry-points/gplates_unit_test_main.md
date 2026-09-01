# gplates_unit_test_main

[Book TOC](../../TOC.md) · [entry-points](../../components/entry-points.md) · cluster Community 863 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/gplates_unit_test_main.cc` | C++ | 181 |

## Overview

The entry point for the unit test executable that uses the Boost.Test framework. Initializes Qt resources needed by tests (OpenGL, Python, GPGIM, and widgets), checks for floating-point infinity and NaN support, sets up the Qt message handler, creates and registers the test suite hierarchy, and supports filtering tests by name via command-line options. Uses dynamic linking to Boost.Test to maintain consistency with other dynamically-linked Boost libraries.

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

The `init_unit_test()` function creates `MainTestSuite` with `new` (not on the stack); the memory is intentionally managed by the Boost.Test framework, not by C++ scope. Uses dynamic linking (`BOOST_TEST_DYN_LINK`) to avoid conflicts with static linking of other Boost libraries. Tests can be listed with `--list_content` and filtered by name with `--run_test=SuiteName,*/*/TestName`.

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/gplates_unit_test_main.cc
```
