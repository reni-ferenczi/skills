# TestCase

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/TestCase.template_cc` | C++ | 109 |
| `src/unit-test/TestCase.template_h` | C++ | 79 |

## Overview

Template files for generating new test case classes. These files provide a boilerplate structure with placeholder variables ($TESTCLASS$) that developers substitute to create test classes and their associated Boost.Test suites. The template includes seven empty test case methods and standard constructor and suite-construction code ready for customization.

## Declared types

*None.*

## Members

*None.*

## Free functions and macros

*None.*

## Notes

*None.*

## Used by

*Nothing in the tree references this unit.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/TestCase.template_cc
```
