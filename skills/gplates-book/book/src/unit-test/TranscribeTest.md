# TranscribeTest

[Book TOC](../../TOC.md) · [unit-test](../../components/unit-test.md) · cluster Community 49 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/unit-test/TranscribeTest.h` | C++ | 846 |
| `src/unit-test/TranscribeTest.cc` | C++ | 2529 |

## Overview

This unit is the test suite for the `GPlatesScribe` serialisation framework (`Scribe`, `ArchiveWriter`/`ArchiveReader` and the `transcribe()` protocol), organised as four fixtures under `TranscribeTestSuite`: `TranscribePrimitivesTest` for built-in types, pointers, C-style arrays and STL/Qt containers; `TranscribeUntrackedTest` for the tracking rules around pointers and shared objects; `TranscribeInheritanceTest` for polymorphic base-class pointers, multiple inheritance and reconstructing objects via `TranscribeContext`/`ConstructObject`; and `TranscribeCompatibilityTest` for interchanging different smart-pointer wrapper types over the same transcribed data. Every test case follows the same shape: write a populated object graph out through a `_write` helper, then read it back through a matching `_read` helper, and each of these is run three times, once per archive backend (`TextArchiveWriter`/`Reader`, `BinaryArchiveWriter`/`Reader`, `XmlArchiveWriter`/`Reader`), so a bug specific to one archive format is caught even when the others pass.

`TranscribeCompatibilityTest::SmartPtrData::transcribe()` is the clearest illustration of what "compatibility" means here: on load it deliberately reads a `boost::scoped_ptr` under the object tag that was written for a `GPlatesUtils::non_null_intrusive_ptr`, a `boost::shared_ptr` under a tag written for a `std::unique_ptr`, and so on, to prove the smart-pointer transcribe protocol does not depend on the specific pointer type used at either end. The helper types with `friend class GPlatesScribe::Access` (`Data`, `B`, `A`, `D`, `Derived`, …) exist purely as fixtures for this: their private `transcribe()`/`transcribe_construct_data()` members and the free `transcribe_construct_data()` overloads at file scope are the very code paths under test, not incidental plumbing.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesUnitTest::TranscribePrimitivesTest`](#gplatesunittesttranscribeprimitivestest) | class | — | — | 0 | Test transcribing of primitives and pointers to them. |
| [`GPlatesUnitTest::TranscribeUntrackedTest`](#gplatesunittesttranscribeuntrackedtest) | class | — | — | 0 | Test transcribing untracked objects. |
| [`GPlatesUnitTest::TranscribeInheritanceTest`](#gplatesunittesttranscribeinheritancetest) | class | — | — | 0 | Test transcribing of base class pointers to derived class objects. |
| [`GPlatesUnitTest::TranscribeCompatibilityTest`](#gplatesunittesttranscribecompatibilitytest) | class | — | — | 0 | Test backward/forward compatibility. |
| [`GPlatesUnitTest::TranscribeTestSuite`](#gplatesunittesttranscribetestsuite) | class | [`GPlatesUnitTest::GPlatesTestSuite`](GPlatesTestSuite.md) | — | 0 | To run only Transcribe test suite: gplates-unit-test.exe --G\_test\_to\_run=\*/Transcribe |
| [`GPlatesScribe::TranscribeContext<GPlatesUnitTest::TranscribeInheritanceTest::A>`](#gplatesscribetranscribecontextgplatesunittesttranscribeinheritancetesta) | class | — | `<>` | 0 | — |

## Members

### `GPlatesUnitTest::TranscribePrimitivesTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscribePrimitivesTest()` | constructor | `None` | public | — |
| `test_case_primitives_1()` | method | `void` | public | — |
| `Data` | class | `None` | public | — |
| `test_case_1_write( const GPlatesScribe::ArchiveWriter::non_null_ptr_type &archive_writer, boost::scoped_ptr<Data> &before_data_scoped_ptr, Data &before_data, const std::string (&before_string_array)[2], const char (&before_char_array)[1][2][6], const Data::NonDefaultConstructable (&before_non_default_constructable_arra ...` | method | `void` | private | — |
| `test_case_1_read( const GPlatesScribe::ArchiveReader::non_null_ptr_type &archive_reader, boost::scoped_ptr<Data> &before_data_scoped_ptr, Data &before_data, const std::string (&before_string_array)[2], const char (&before_char_array)[1][2][6], const Data::NonDefaultConstructable (&before_non_default_constructable_array ...` | method | `void` | private | — |

### `GPlatesUnitTest::TranscribeUntrackedTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `variant_type` | typedef | `boost::variant<int, std::string>` | public | — |
| `test_case_untracked_exception()` | method | `void` | public | — |
| `test_case_untracked_1()` | method | `void` | public | — |
| `test_case_untracked_1_write( const GPlatesScribe::ArchiveWriter::non_null_ptr_type &archive_writer, variant_type &before_variant)` | method | `void` | private | — |
| `test_case_untracked_1_read( const GPlatesScribe::ArchiveReader::non_null_ptr_type &archive_reader, variant_type &before_variant)` | method | `void` | private | — |

### `GPlatesUnitTest::TranscribeInheritanceTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscribeInheritanceTest()` | constructor | `None` | public | — |
| `test_case_inheritance_1()` | method | `void` | public | — |
| `test_case_inheritance_2()` | method | `void` | public | — |
| `UntranscribedClass` | struct | `None` | public | A class that is not transcribed but will be referenced by a transcribed class. |
| `int_pair_type` | typedef | `std::pair<TranscribePrimitivesTest::Data::NonDefaultConstructable, int>` | public | — |
| `B` | class | `None` | public | — |
| `A` | class | `None` | public | — |
| `D` | class | `None` | public | — |
| `E` | class | `None` | public | — |
| `test_case_inheritance_1_write( const GPlatesScribe::ArchiveWriter::non_null_ptr_type &archive_writer, UntranscribedClass &untranscribed_object, boost::optional<int> &before_d, D &before_data, B *&before_data_ptr, int *&before_x_ptr, D &before_data2, E &before_e)` | method | `void` | private | — |
| `test_case_inheritance_1_read( const GPlatesScribe::ArchiveReader::non_null_ptr_type &archive_reader, UntranscribedClass &untranscribed_object, boost::optional<int> &before_d, D &before_data, B *&before_data_ptr, int *&before_x_ptr, D &before_data2, E &before_e)` | method | `void` | private | — |
| `test_case_inheritance_2_write( const GPlatesScribe::ArchiveWriter::non_null_ptr_type &archive_writer, UntranscribedClass &untranscribed_object, boost::scoped_ptr<int> &before_d, boost::shared_ptr<B> &before_data_ptr, boost::weak_ptr<B> &before_data_weak_ptr, boost::shared_ptr<D> &before_data_ptr2, GPlatesUtils::non_nul ...` | method | `void` | private | — |
| `test_case_inheritance_2_read( const GPlatesScribe::ArchiveReader::non_null_ptr_type &archive_reader, UntranscribedClass &untranscribed_object, boost::scoped_ptr<int> &before_d, boost::shared_ptr<B> &before_data_ptr, boost::weak_ptr<B> &before_data_weak_ptr, boost::shared_ptr<D> &before_data_ptr2, GPlatesUtils::non_null ...` | method | `void` | private | — |

### `GPlatesUnitTest::TranscribeCompatibilityTest`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscribeCompatibilityTest()` | constructor | `None` | public | — |
| `test_case_compatibility_1()` | method | `void` | public | — |
| `UntranscribedClass` | struct | `None` | public | A class that is not transcribed but will be referenced by a transcribed class. |
| `int_pair_type` | typedef | `std::pair<TranscribePrimitivesTest::Data::NonDefaultConstructable, int>` | public | — |
| `Base` | class | `None` | public | — |
| `Derived` | class | `None` | public | — |
| `SmartPtrData` | class | `None` | public | — |
| `test_case_compatibility_1_write( const GPlatesScribe::ArchiveWriter::non_null_ptr_type &archive_writer, SmartPtrData &before_smart_ptr_data)` | method | `void` | private | — |
| `test_case_compatibility_1_read( const GPlatesScribe::ArchiveReader::non_null_ptr_type &archive_reader, SmartPtrData &before_smart_ptr_data)` | method | `void` | private | — |

### `GPlatesUnitTest::TranscribeTestSuite`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscribeTestSuite( unsigned depth)` | constructor | `None` | public | — |
| `construct_maps()` | method | `void` | protected | — |
| `construct_transcribe_primitives_test()` | method | `void` | private | — |
| `construct_transcribe_untracked_test()` | method | `void` | private | — |
| `construct_transcribe_inheritance_test()` | method | `void` | private | — |
| `construct_transcribe_compatibility_test()` | method | `void` | private | — |

### `GPlatesScribe::TranscribeContext<GPlatesUnitTest::TranscribeInheritanceTest::A>`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscribeContext( const GPlatesUnitTest::TranscribeInheritanceTest::UntranscribedClass &untranscribed_object_)` | method | `None` | public | — |
| `untranscribed_object` | field | `GPlatesUnitTest::TranscribeInheritanceTest::UntranscribedClass` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `SAVE_LOAD_CLASS_DATA_USING_VARIANT` | macro | `None` | There's two ways to construct class Data (one using 'int' constructor and one using 'variant' constructor). |
| `GPLATES_UNIT_TEST_TRANSCRIBE_TEST_H` | macro | `None` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, TranscribePrimitivesTest::Data::Enum &e, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, TranscribePrimitivesTest::Data::NonDefaultConstructable &ndc, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | — |
| `transcribe_construct_data( GPlatesScribe::Scribe &scribe, GPlatesScribe::ConstructObject<TranscribePrimitivesTest::Data::NonDefaultConstructable> &ndc)` | function | `GPlatesScribe::TranscribeResult` | — |
| `transcribe_construct_data( GPlatesScribe::Scribe &scribe, GPlatesScribe::ConstructObject<TranscribeInheritanceTest::B> &b)` | function | `GPlatesScribe::TranscribeResult` | — |
| `transcribe_construct_data( GPlatesScribe::Scribe &scribe, GPlatesScribe::ConstructObject<TranscribeInheritanceTest::D> &d)` | function | `GPlatesScribe::TranscribeResult` | — |
| `transcribe( GPlatesScribe::Scribe &scribe, TranscribeInheritanceTest::E &e, bool transcribed_construct_data)` | function | `GPlatesScribe::TranscribeResult` | — |
| `transcribe_construct_data( GPlatesScribe::Scribe &scribe, GPlatesScribe::ConstructObject<TranscribeInheritanceTest::E> &e)` | function | `GPlatesScribe::TranscribeResult` | — |

## Notes

Several `BOOST_CHECK_THROW` assertions in `TranscribeUntrackedTest::test_case_untracked_exception()` (pointer-before-object and unreferencing-a-tracked-object checks) are compiled out under `#ifndef GPLATES_DEBUG`, because in a debug build the same violations are caught by `GPlatesGlobal::Assert()` aborting the process rather than throwing — so this test only exercises those exception paths in a release build. `D::relocated()` and the `boost::optional<int> y` comment ("Test relocation") mark the one place this suite checks the Scribe relocation callback, which fires when a tracked object's address changes between save and load (e.g. a value moved out of a `boost::optional`); get this wrong in `GPlatesScribe` and this is the test that will catch it. To run only this suite: `gplates-unit-test.exe --G_test_to_run=*/Transcribe`, as noted in the header above `TranscribeTestSuite`.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 7 |
| [qt-widgets/VisualLayerWidget](../qt-widgets/VisualLayerWidget.md) | qt-widgets | 6 |
| [deprecated/controls/File](../deprecated/controls/File.md) | deprecated | 5 |
| [opengl/GLMatrix](../opengl/GLMatrix.md) | opengl | 5 |
| [api/PyCoregistrationLayerProxy](../api/PyCoregistrationLayerProxy.md) | api | 4 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 4 |
| [app-logic/ResolvedTriangulationUtils](../app-logic/ResolvedTriangulationUtils.md) | app-logic | 3 |
| [gui/deprecated/GLCanvas](../gui/deprecated/GLCanvas.md) | gui | 3 |
| [qt-widgets/DrawStyleDialog](../qt-widgets/DrawStyleDialog.md) | qt-widgets | 3 |
| [qt-widgets/TotalReconstructionSequencesDialog](../qt-widgets/TotalReconstructionSequencesDialog.md) | qt-widgets | 3 |
| [app-logic/CoRegistrationLayerProxy](../app-logic/CoRegistrationLayerProxy.md) | app-logic | 2 |
| [file-io/CptReader](../file-io/CptReader.md) | file-io | 2 |
| [file-io/FeatureCollectionFileFormatRegistry](../file-io/FeatureCollectionFileFormatRegistry.md) | file-io | 2 |
| [gui/CommandServer](../gui/CommandServer.md) | gui | 2 |
| [gui/deprecated/GPlatesApp](../gui/deprecated/GPlatesApp.md) | gui | 2 |
| [qt-widgets/MapView](../qt-widgets/MapView.md) | qt-widgets | 2 |
| [api/CoReg](../api/CoReg.md) | api | 1 |
| [app-logic/GPlatesQtMsgHandler](../app-logic/GPlatesQtMsgHandler.md) | app-logic | 1 |
| [app-logic/NetRotationUtils](../app-logic/NetRotationUtils.md) | app-logic | 1 |
| [data-mining/LookupReducer](../data-mining/LookupReducer.md) | data-mining | 1 |

*... and 13 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/unit-test/TranscribeTest.h
python scripts/gpq.py def GPlatesUnitTest::TranscribePrimitivesTest --body
python scripts/gpq.py uses TranscribePrimitivesTest --kind class
python scripts/gpq.py hier TranscribePrimitivesTest
```
