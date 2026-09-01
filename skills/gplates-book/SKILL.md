---
name: gplates-book
description: Developer's reference manual for the GPlates 2.5+ C++ source — a generated, navigable book with per-component and per-unit pages plus by-name indexes of components, types, free functions and preprocessor macros. Use to understand what a GPlates class, file, module or macro is for, how a subsystem is designed, or where to start before diving into the code; complements gplates-code, which answers symbol-level where/who-uses questions against the raw source index.
license: MIT
---

# GPlates Book

A developer's reference manual for GPlates, generated from the code index built
by the `gplates-code` skill.

- **Read the book:** start at [book/TOC.md](book/TOC.md) — project overview,
  component list, and links to all the indexes:
  [Components](book/indexes/Components.md) ·
  [Classes](book/indexes/Classes.md) ·
  [Structs](book/indexes/Structs.md) ·
  [Enums](book/indexes/Enums.md) ·
  [Typedefs](book/indexes/Typedefs.md) ·
  [Functions](book/indexes/Functions.md) ·
  [Macros](book/indexes/Macros.md).
  Navigate TOC → component page → unit page; use the indexes for direct by-name lookup.
- **Every source file is reachable** from the TOC via its component page; if a
  page seems missing, run `scripts/verify_book.py` to check coverage and links.
- **Build or refresh the book:** follow the plan in [Writer.md](Writer.md).
  Requires the `gplates-code` index (`../gplates-code/data/gplates.db`) to exist.
- **Symbol-level questions** (declarations, usages, hierarchy, signals, GPGIM)
  belong to the `gplates-code` skill, not this book.
