# UnicodeString

[Book TOC](../../TOC.md) · [utils](../../components/utils.md) · cluster Community 116 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/utils/UnicodeString.h` | C++ | 219 |
| `src/utils/UnicodeString.cc` | C++ | 155 |

## Overview

A compatibility shim, not a string implementation. GPlates once used ICU's
`icu::UnicodeString` throughout; when the dependency was dropped, rather than
rewriting several hundred call sites the class was replaced by a thin wrapper
holding a single `QString` and exposing just the slice of the ICU interface that
the tree actually called — `length()`, `isEmpty()`, `indexOf()`,
`extractBetween()`, `removeBetween()`, `operator+=`. Every method in the `.cc`
is a one-liner forwarding to the corresponding `QString` call, each with a
comment naming the ICU page it implements and the `QString` page it implements
it with. There is no behaviour of its own to understand: read the `QString`
documentation for the semantics.

`qstring()` is the escape hatch, and the header says so — it is the only member
that breaks the ICU illusion. Because the wrapper's surface is so narrow, most
code that needs to do real string work calls `qstring()` and works in Qt, which
is why the class shows up in a hundred and forty units without any of them
depending on much of it. New code should use `QString` directly; this type exists
to keep the old call sites compiling and to be the element type of
`GPlatesUtils::StringSet` and `GPlatesUtils::IdStringSet`, where its `operator<`
supplies the strict weak ordering for the interning `std::set` and its
`operator==` the string comparison.

Two pieces of integration are worth knowing about. Deriving from
`GPlatesUtils::QtStreamable<UnicodeString>` (a Barton-Nackman friend-injection
template) means that defining the `std::ostream` inserter in the `.cc` is enough
to also get `qDebug()`, `qWarning()` and `QTextStream` output for free. And the
private `transcribe()`, befriended to `GPlatesScribe::Access`, uses
`transcribe_delegate_protocol` on the wrapped `d_qstring`, which makes
`UnicodeString` and `QString` interchangeable in saved sessions and projects —
either may be transcribed and read back as the other.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUtils::UnicodeString`](#gplatesutilsunicodestring) | class | [`GPlatesUtils::QtStreamable<UnicodeString>`](QtStreamable.md) | — | 0 | A wrapper class around QString which mirrors the interface of ICU's UnicodeString as needed. http://icu-project.org/apiref/icu4c/classUnicodeString.html |

## Members

### `GPlatesUtils::UnicodeString`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnicodeString()` | constructor | `None` | public | — |
| `UnicodeString( const QString &qs)` | constructor | `None` | public | — |
| `UnicodeString( const char *s)` | constructor | `None` | public | Construct a UnicodeString instance from a null-terminated array of chars. http://icu-project.org/apiref/icu4c/classUnicodeString.html#2e81e482db97eb362b6d0d62ff331ca3 It seems that this constructor is not explicit in ICU UnicodeString. |
| `isEmpty()` | method | `bool` | public | Determine if this string is empty. http://icu-project.org/apiref/icu4c/classUnicodeString.html#4004ef18a48eafbefc4bbc67cb12dcdf |
| `length()` | method | `boost::int32_t` | public | Return the length of the UnicodeString object. |
| `indexOf( const UnicodeString &text)` | method | `boost::int32_t` | public | Locate in this the first occurrence of the characters in text, using bitwise comparison. http://icu-project.org/apiref/icu4c/classUnicodeString.html#8f3956140af1d4d9d255e5da837b297c |
| `indexOf( const UnicodeString &text, boost::int32_t start)` | method | `boost::int32_t` | public | Locate in this the first occurrence of the characters in text starting at offset start, using bitwise comparison. http://icu-project.org/apiref/icu4c/classUnicodeString.html#81248ae2f8f2700f808c3fdf14a2ee67 |
| `extractBetween( boost::int32_t start, boost::int32_t limit, UnicodeString &target)` | method | `void` | public | Copy the characters in the range \[start, limit) into the UnicodeString target. http://icu-project.org/apiref/icu4c/classUnicodeString.html#d8946e6ca397f9b37a60a6a3c1a2ab93 |
| `removeBetween` | field | `UnicodeString` | public | Remove the characters in the range \[start, limit) from the UnicodeString object. http://icu-project.org/apiref/icu4c/classUnicodeString.html#46ca3daa10b0bcbcc4d75da6b7496f4e |
| `d_qstring` | field | `QString` | private | — |
| `transcribe( GPlatesScribe::Scribe &scribe, bool transcribed_construct_data)` | method | `GPlatesScribe::TranscribeResult` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_UTILS_UNICODESTRING_H` | macro | `None` | — |
| `GPLATES_ICU_BOOL` | macro_function | `(b)` | The ICU UnicodeString binary comparison operators returned a UBool rather than a bool, which caused problems. |
| `operator==( const UnicodeString &us1, const UnicodeString &us2)` | operator | `bool` | — |
| `operator<( const UnicodeString &us1, const UnicodeString &us2)` | operator | `bool` | — |
| `operator+( const UnicodeString &us1, const UnicodeString &us2)` | operator | `UnicodeString` | — |
| `operator<<` | variable | `ostream` | — |

## Notes

- **Units are UTF-16 code units, not code points.** `length()` returns
  `QString::length()`, which counts 16-bit `QChar`s; the `.cc` comment spells
  this out, and the header's ICU-inherited advice to "use `countChar32()`" points
  at a function this wrapper does not provide. Every offset taken by `indexOf()`,
  `extractBetween()` and `removeBetween()` is in the same units, so a surrogate
  pair can be split by an unlucky index.
- **`const char *` conversion is implicit and assumes ASCII.** The comment on
  that constructor warns not to pass local-code-page data. Because it is not
  explicit, a stray string literal silently becomes a `UnicodeString`; the
  `QString` constructor is explicit, so only the char-pointer path has this
  hazard.
- **`GPLATES_ICU_BOOL` has two different definitions in the tree.** This header
  defines it as the identity `(b)` — the ICU version returning `UBool` is
  commented out and the macro is kept only because it still pervades the code —
  while `StringSet.h` defines it as `((b) != 0)` *before* including this header.
  Both are guarded by `#ifndef`, so which one a translation unit gets depends on
  include order. The two agree for a `bool` operand, but do not add a definition
  that does not.
- **`extractBetween()` and `removeBetween()` do not validate their range.** They
  compute `limit - start` and hand it to `QString::mid()` / `QString::remove()`,
  so out-of-range or inverted arguments give whatever `QString` gives, not the
  ICU clamping behaviour the linked documentation describes.
- **The `std::ostream` inserter writes UTF-8 via `ostream::write`,** deliberately
  passing an explicit byte count rather than treating the buffer as
  NUL-terminated, so embedded zero bytes survive. Do not simplify it to a
  `const char *` insertion.
- **Copy is `QString` copy.** Implicitly shared and cheap, but with `QString`'s
  copy-on-write, which means the usual Qt rule applies: a `UnicodeString` is not
  safe to share across threads while any copy of it may be mutated.
- **No inheritance is intended.** There is no virtual destructor; the
  `QtStreamable` base exists only to inject the streaming operators.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesFormatUtils](../file-io/PlatesFormatUtils.md) | file-io | 99 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 54 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 48 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 46 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 37 |
| [property-values/GpmlOldPlatesHeader](../property-values/GpmlOldPlatesHeader.md) | property-values | 29 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 23 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 20 |
| [file-io/XmlOutputInterface](../file-io/XmlOutputInterface.md) | file-io | 18 |
| [file-io/OgrFeatureCollectionWriter](../file-io/OgrFeatureCollectionWriter.md) | file-io | 17 |
| [file-io/PlatesLineFormatHeaderVisitor](../file-io/PlatesLineFormatHeaderVisitor.md) | file-io | 15 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 14 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 12 |
| [file-io/PlatesRotationFormatWriter](../file-io/PlatesRotationFormatWriter.md) | file-io | 11 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 10 |
| [utils/XmlNamespaces](XmlNamespaces.md) | utils | 10 |
| [presentation/TopologyNetworkVisualLayerParams](../presentation/TopologyNetworkVisualLayerParams.md) | presentation | 8 |
| [qt-widgets/PythonConsoleDialog](../qt-widgets/PythonConsoleDialog.md) | qt-widgets | 8 |
| [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) | qt-widgets | 8 |
| [presentation/TranscribeSession](../presentation/TranscribeSession.md) | presentation | 7 |

*... and 119 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/utils/UnicodeString.h
python scripts/gpq.py def GPlatesUtils::UnicodeString --body
python scripts/gpq.py uses UnicodeString --kind class
python scripts/gpq.py hier UnicodeString
```
