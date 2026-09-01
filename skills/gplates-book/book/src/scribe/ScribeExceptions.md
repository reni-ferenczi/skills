# ScribeExceptions

[Book TOC](../../TOC.md) · [scribe](../../components/scribe.md) · cluster Community 8 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/scribe/ScribeExceptions.h` | C++ | 1254 |
| `src/scribe/ScribeExceptions.cc` | C++ | 337 |

## Overview

Every failure the scribe library can raise is declared here, in one namespace, under one
root: `BaseException`, itself a `GPlatesGlobal::Exception`. That is the point of the file —
a caller that wants to survive any serialisation failure catches `Exceptions::BaseException`
and nothing else, while a caller that cares about a specific contract violation can catch
the leaf. The classes are pure diagnostics: each captures whatever context it needs at
throw time (a type name, a class name, an XML element name) and turns it into text in a
`write_message()` override defined in the `.cc`. They carry no recovery information and
nothing catches them to make a decision.

The line these exceptions draw is the one worth remembering when reading the rest of the
library. **Compatibility problems are not exceptions.** A tag that is missing from an
archive, a primitive of the wrong kind, or an export-registered class name the running
binary does not know are reported as `TRANSCRIBE_INCOMPATIBLE` or `TRANSCRIBE_UNKNOWN_TYPE`
return codes, which the caller may recover from by supplying a default. Everything in this
header is a situation from which transcribing cannot continue: a corrupt or future archive,
a bug inside the library, or — most of them — the client using the library incorrectly.
Almost all the messages start with "Incorrect Scribe usage".

They fall into four rough families. Archive-level failures raised by the readers and
writers: `UnsupportedVersion`, `InvalidArchiveSignature`, `ArchiveStreamError` and the XML
trio. Catch-alls that separate blame: `ScribeLibraryError` for an internal inconsistency or
a corrupt transcription, `ScribeUserError` for a call made in the wrong direction (saving
when only loading is legal, and vice versa). Violations of the object-tracking and
relocation contract described in [Scribe](Scribe.md), which is the largest group —
`AlreadyTranscribedObject`, `UntrackingObjectWithReferences`,
`TranscribedUntrackedPointerBeforeReferencedObject`, the `Relocated*` set,
`TranscribedReferenceInsteadOfObject` and `ScribeTranscribeResultNotChecked`. And
registration failures, where a type was used in a way that needed a registration nobody
performed: `UnregisteredCast` and `AmbiguousCast` from `VoidCastRegistry`,
`UnregisteredClassType` and the two `ExportRegistered*` clashes from `ExportRegistry`,
`UnregisteredEnumValue` from the enum protocol, and `UnregisteredQVariantMetaType` from the
Qt bindings.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesScribe::Exceptions::BaseException`](#gplatesscribeexceptionsbaseexception) | class | [`GPlatesGlobal::Exception`](../global/GPlatesException.md) | — | 31 | The base exception class for all Scribe exceptions. |
| [`GPlatesScribe::Exceptions::UnsupportedVersion`](#gplatesscribeexceptionsunsupportedversion) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown if the archive stream (being read) was written using a future version of the scribe library and/or archive. |
| [`GPlatesScribe::Exceptions::InvalidArchiveSignature`](#gplatesscribeexceptionsinvalidarchivesignature) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown if the archive stream has an invalid signature. |
| [`GPlatesScribe::Exceptions::ArchiveStreamError`](#gplatesscribeexceptionsarchivestreamerror) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown due to failure to read or write to the archive stream. |
| [`GPlatesScribe::Exceptions::ScribeLibraryError`](#gplatesscribeexceptionsscribelibraryerror) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | A non-specific error internal to the Scribe library. |
| [`GPlatesScribe::Exceptions::ScribeUserError`](#gplatesscribeexceptionsscribeusererror) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | A non-specific error in the usage of the Scribe library (not a bug in the library itself). |
| [`GPlatesScribe::Exceptions::ScribeTranscribeResultNotChecked`](#gplatesscribeexceptionsscribetranscriberesultnotchecked) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | This exception is thrown when a transcribe result from class Scribe (eg, Scribe::transcribe()) has not been checked. |
| [`GPlatesScribe::Exceptions::ConstructNotAllowed`](#gplatesscribeexceptionsconstructnotallowed) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Use this exception when you don't want a class type to be save/load constructed (only transcribed). |
| [`GPlatesScribe::Exceptions::InvalidTranscribeOptions`](#gplatesscribeexceptionsinvalidtranscribeoptions) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | When invalid options are passed to Scribe::transcribe(). |
| [`GPlatesScribe::Exceptions::UnexpectedXmlElementName`](#gplatesscribeexceptionsunexpectedxmlelementname) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | When the start or end of an XML element with a specific element name is not encountered. |
| [`GPlatesScribe::Exceptions::InvalidXmlElementName`](#gplatesscribeexceptionsinvalidxmlelementname) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | An invalid XML element name (obtained via an object tag). |
| [`GPlatesScribe::Exceptions::XmlStreamParseError`](#gplatesscribeexceptionsxmlstreamparseerror) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when a parse error reading XML stream is encountered. |
| [`GPlatesScribe::Exceptions::TranscriptionIncomplete`](#gplatesscribeexceptionstranscriptionincomplete) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when a transcription is incomplete (eg, there are uninitialised transcribed objects after an archive has been saved or loaded). |
| [`GPlatesScribe::Exceptions::TranscriptionIncompatible`](#gplatesscribeexceptionstranscriptionincompatible) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when a transcription was not able to be transcribed because it was incompatible (this can happen due to breaking of backward/forward compatibility). |
| [`GPlatesScribe::Exceptions::TranscribedReferenceInsteadOfObject`](#gplatesscribeexceptionstranscribedreferenceinsteadofobject) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when transcribing a reference-to-an-object instead of the object directly and the object's actual (RTTI) type is different than the reference type. |
| [`GPlatesScribe::Exceptions::AlreadyTranscribedObject`](#gplatesscribeexceptionsalreadytranscribedobject) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown if a tracked object has already been saved at a particular memory address, or already been loaded (at same object tag location in transcription). |
| [`GPlatesScribe::Exceptions::AlreadyTranscribedObjectWithoutOwningPointer`](#gplatesscribeexceptionsalreadytranscribedobjectwithoutowningpointer) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown if an attempted to transcribe an object via an owning pointer but the object has already been transcribed without one. |
| [`GPlatesScribe::Exceptions::TranscribedUntrackedPointerBeforeReferencedObject`](#gplatesscribeexceptionstranscribeduntrackedpointerbeforereferencedobject) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when an untracked pointer is transcribed before the pointed-to object - because its untracked it won't get initialised properly later when the pointed-to object is transcribed. |
| [`GPlatesScribe::Exceptions::UntrackingObjectWithReferences`](#gplatesscribeexceptionsuntrackingobjectwithreferences) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when an object is untracked (or discarded) and it has transcribed pointers or references referencing it. |
| [`GPlatesScribe::Exceptions::TranscribedReferenceBeforeReferencedObject`](#gplatesscribeexceptionstranscribedreferencebeforereferencedobject) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when a reference-to-an-object cannot find the referenced object at the time when the reference is transcribed. |
| [`GPlatesScribe::Exceptions::RelocatedReferenceInsteadOfObject`](#gplatesscribeexceptionsrelocatedreferenceinsteadofobject) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when relocating a reference-to-an-object instead of the object directly and the object's actual (RTTI) type is different than the reference type. |
| [`GPlatesScribe::Exceptions::RelocatedUntrackedObject`](#gplatesscribeexceptionsrelocateduntrackedobject) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when a reference-to-an-object cannot find the referenced object at the time when the reference is transcribed. |
| [`GPlatesScribe::Exceptions::RelocatedObjectBoundToAReferenceOrUntrackedPointer`](#gplatesscribeexceptionsrelocatedobjectboundtoareferenceoruntrackedpointer) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when an attempt is made to relocate a transcribed object that already has a reference bound to it (the reference cannot be re-bound to the relocated object) or an untracked pointer (cannot be updated to point to relocated ... |
| [`GPlatesScribe::Exceptions::LoadedObjectTrackedButNotRelocated`](#gplatesscribeexceptionsloadedobjecttrackedbutnotrelocated) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when a tracked object is loaded (in Scribe::load()) but was not relocated. |
| [`GPlatesScribe::Exceptions::UnregisteredCast`](#gplatesscribeexceptionsunregisteredcast) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when unable to void cast between a derived and base class. |
| [`GPlatesScribe::Exceptions::AmbiguousCast`](#gplatesscribeexceptionsambiguouscast) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when there is more than one path between between a derived and a base class. |
| [`GPlatesScribe::Exceptions::UnregisteredEnumValue`](#gplatesscribeexceptionsunregisteredenumvalue) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when attempting to transcribe an enumeration value that is not registered. |
| [`GPlatesScribe::Exceptions::UnregisteredClassType`](#gplatesscribeexceptionsunregisteredclasstype) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when the class type is not explicitly registered or export registered. |
| [`GPlatesScribe::Exceptions::ExportRegisteredMultipleClassTypesWithSameClassName`](#gplatesscribeexceptionsexportregisteredmultipleclasstypeswithsameclassname) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when the same class name is used to export register different class types. |
| [`GPlatesScribe::Exceptions::ExportRegisteredMultipleClassNamesWithSameClassType`](#gplatesscribeexceptionsexportregisteredmultipleclassnameswithsameclasstype) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when multiple class names are used to export register the same class type. |
| [`GPlatesScribe::Exceptions::UnregisteredQVariantMetaType`](#gplatesscribeexceptionsunregisteredqvariantmetatype) | class | [`BaseException`](ScribeExceptions.md) | — | 0 | Exception thrown when the type stored in a transcribed QVariant is not registered with Qt using 'qRegisterMetaType()' and 'qRegisterMetaTypeStreamOperators()'. |

## Members

### `GPlatesScribe::Exceptions::BaseException`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~BaseException()` | destructor | `None` | public | — |
| `BaseException( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | protected | — |

### `GPlatesScribe::Exceptions::UnsupportedVersion`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnsupportedVersion( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~UnsupportedVersion()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesScribe::Exceptions::InvalidArchiveSignature`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidArchiveSignature( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~InvalidArchiveSignature()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesScribe::Exceptions::ArchiveStreamError`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ArchiveStreamError( const GPlatesUtils::CallStack::Trace &exception_source, const std::string &message)` | constructor | `None` | public | — |
| `~ArchiveStreamError()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_message` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::ScribeLibraryError`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ScribeLibraryError( const GPlatesUtils::CallStack::Trace &exception_source, const std::string &message)` | constructor | `None` | public | — |
| `~ScribeLibraryError()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_message` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::ScribeUserError`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ScribeUserError( const GPlatesUtils::CallStack::Trace &exception_source, const std::string &message)` | constructor | `None` | public | — |
| `~ScribeUserError()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_message` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::ScribeTranscribeResultNotChecked`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ScribeTranscribeResultNotChecked( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~ScribeTranscribeResultNotChecked()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesScribe::Exceptions::ConstructNotAllowed`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ConstructNotAllowed( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &object_type_info)` | constructor | `None` | public | — |
| `~ConstructNotAllowed()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_object_type_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::InvalidTranscribeOptions`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidTranscribeOptions( const GPlatesUtils::CallStack::Trace &exception_source, const std::string &message)` | constructor | `None` | public | — |
| `~InvalidTranscribeOptions()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_message` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::UnexpectedXmlElementName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnexpectedXmlElementName( const GPlatesUtils::CallStack::Trace &exception_source, const QString &element_name, bool is_start_element)` | constructor | `None` | public | — |
| `UnexpectedXmlElementName( const GPlatesUtils::CallStack::Trace &exception_source, const QStringList &element_names, bool is_start_element)` | constructor | `None` | public | — |
| `~UnexpectedXmlElementName()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_element_names` | field | `QStringList` | private | — |
| `d_is_start_element` | field | `bool` | private | — |

### `GPlatesScribe::Exceptions::InvalidXmlElementName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `InvalidXmlElementName( const GPlatesUtils::CallStack::Trace &exception_source, boost::optional<std::string> xml_element_name = boost::none)` | constructor | `None` | public | — |
| `~InvalidXmlElementName()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_xml_element_name` | field | `boost::optional<std::string>` | private | — |

### `GPlatesScribe::Exceptions::XmlStreamParseError`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `XmlStreamParseError( const GPlatesUtils::CallStack::Trace &exception_source, const QString &xml_error_message)` | constructor | `None` | public | — |
| `~XmlStreamParseError()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_xml_error_message` | field | `QString` | private | — |

### `GPlatesScribe::Exceptions::TranscriptionIncomplete`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscriptionIncomplete( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~TranscriptionIncomplete()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesScribe::Exceptions::TranscriptionIncompatible`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscriptionIncompatible( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~TranscriptionIncompatible()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesScribe::Exceptions::TranscribedReferenceInsteadOfObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscribedReferenceInsteadOfObject( const GPlatesUtils::CallStack::Trace &exception_source, const ObjectType &referenced_object)` | constructor | `None` | public | — |
| `~TranscribedReferenceInsteadOfObject()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_reference_type_name` | field | `std::string` | private | — |
| `d_object_type_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::AlreadyTranscribedObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AlreadyTranscribedObject( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &object_type_info, bool scribe_is_saving)` | constructor | `None` | public | — |
| `~AlreadyTranscribedObject()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_object_type_name` | field | `std::string` | private | — |
| `d_scribe_is_saving` | field | `bool` | private | — |

### `GPlatesScribe::Exceptions::AlreadyTranscribedObjectWithoutOwningPointer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AlreadyTranscribedObjectWithoutOwningPointer( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &object_type_info)` | constructor | `None` | public | — |
| `~AlreadyTranscribedObjectWithoutOwningPointer()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_object_type_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::TranscribedUntrackedPointerBeforeReferencedObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscribedUntrackedPointerBeforeReferencedObject( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &object_type_info)` | constructor | `None` | public | — |
| `~TranscribedUntrackedPointerBeforeReferencedObject()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_object_type_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::UntrackingObjectWithReferences`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UntrackingObjectWithReferences( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &object_type_info)` | constructor | `None` | public | — |
| `~UntrackingObjectWithReferences()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_object_type_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::TranscribedReferenceBeforeReferencedObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TranscribedReferenceBeforeReferencedObject( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &object_type_info)` | constructor | `None` | public | — |
| `~TranscribedReferenceBeforeReferencedObject()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_object_type_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::RelocatedReferenceInsteadOfObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RelocatedReferenceInsteadOfObject( const GPlatesUtils::CallStack::Trace &exception_source, const ObjectType &referenced_object)` | constructor | `None` | public | — |
| `~RelocatedReferenceInsteadOfObject()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_reference_type_name` | field | `std::string` | private | — |
| `d_object_type_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::RelocatedUntrackedObject`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RelocatedUntrackedObject( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~RelocatedUntrackedObject()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesScribe::Exceptions::RelocatedObjectBoundToAReferenceOrUntrackedPointer`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `RelocatedObjectBoundToAReferenceOrUntrackedPointer( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~RelocatedObjectBoundToAReferenceOrUntrackedPointer()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesScribe::Exceptions::LoadedObjectTrackedButNotRelocated`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `LoadedObjectTrackedButNotRelocated( const GPlatesUtils::CallStack::Trace &exception_source)` | constructor | `None` | public | — |
| `~LoadedObjectTrackedButNotRelocated()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |

### `GPlatesScribe::Exceptions::UnregisteredCast`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnregisteredCast( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &derived_class_type, const std::type_info &base_class_type)` | constructor | `None` | public | — |
| `~UnregisteredCast()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_derived_class_name` | field | `std::string` | private | — |
| `d_base_class_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::AmbiguousCast`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `AmbiguousCast( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &derived_class_type, const std::type_info &base_class_type)` | constructor | `None` | public | — |
| `~AmbiguousCast()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_derived_class_name` | field | `std::string` | private | — |
| `d_base_class_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::UnregisteredEnumValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnregisteredEnumValue( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &enum_type, int enum_value)` | constructor | `None` | public | — |
| `~UnregisteredEnumValue()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_enum_type` | field | `std::string` | private | — |
| `d_enum_value` | field | `int` | private | — |

### `GPlatesScribe::Exceptions::UnregisteredClassType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnregisteredClassType( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &class_type)` | constructor | `None` | public | — |
| `UnregisteredClassType( const GPlatesUtils::CallStack::Trace &exception_source, const std::string &class_name)` | constructor | `None` | public | — |
| `~UnregisteredClassType()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_class_name` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::ExportRegisteredMultipleClassTypesWithSameClassName`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportRegisteredMultipleClassTypesWithSameClassName( const GPlatesUtils::CallStack::Trace &exception_source, const std::string &class_name, const std::type_info &class_type1, const std::type_info &class_type2)` | constructor | `None` | public | — |
| `~ExportRegisteredMultipleClassTypesWithSameClassName()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_class_name` | field | `std::string` | private | — |
| `d_class_type1` | field | `std::string` | private | — |
| `d_class_type2` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::ExportRegisteredMultipleClassNamesWithSameClassType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `ExportRegisteredMultipleClassNamesWithSameClassType( const GPlatesUtils::CallStack::Trace &exception_source, const std::type_info &class_type, const std::string &class_name1, const std::string &class_name2)` | constructor | `None` | public | — |
| `~ExportRegisteredMultipleClassNamesWithSameClassType()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_class_type` | field | `std::string` | private | — |
| `d_class_name1` | field | `std::string` | private | — |
| `d_class_name2` | field | `std::string` | private | — |

### `GPlatesScribe::Exceptions::UnregisteredQVariantMetaType`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `UnregisteredQVariantMetaType( const GPlatesUtils::CallStack::Trace &exception_source, const QVariant &qvariant_object)` | constructor | `None` | public | — |
| `~UnregisteredQVariantMetaType()` | destructor | `None` | public | — |
| `exception_name()` | method | `char` | protected | — |
| `write_message( std::ostream &os)` | method | `void` | protected | — |
| `d_type_name` | field | `std::string` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_SCRIBE_SCRIBEEXCEPTIONS_H` | macro | `None` | — |

## Notes

**In a debug build these are not thrown at all.** Nearly every one is raised through
`GPlatesGlobal::Assert<ExceptionType>(condition, GPLATES_ASSERTION_SOURCE, args...)`, and
that template calls `GPlatesGlobal::Abort()` when `GPLATES_DEBUG` is defined, throwing only
in release builds. A debug run therefore dies at the assertion site with the call stack
printed, and no `catch` in the session or project code ever sees it. That is usually what
you want while debugging, but it means exception-handling paths in scribe clients are
exercised only by release builds.

**The constructor signature is fixed by that mechanism.** `Assert` always passes the
`GPlatesUtils::CallStack::Trace` first and forwards its remaining arguments verbatim, so
every class here must take the trace as its first constructor parameter and its extra
context after it. Adding a new exception means matching that shape, and matching the
`exception_name()` / `write_message()` pair inherited from `GPlatesGlobal::Exception`. All
destructors are declared `throw()`, as the base requires.

**Two of these are declared but never thrown.** `TranscriptionIncompatible` and
`LoadedObjectTrackedButNotRelocated` have full definitions and message text, and no throw
site anywhere in the tree — incompatibility is signalled by the `TRANSCRIBE_INCOMPATIBLE`
return code instead, and an unrelocated tracked load is handled by silently untracking the
object when its last `LoadRef` dies. Do not take their existence as evidence of a code path.

**`TranscriptionIncomplete` is mostly thrown by callers, not by the library.** `Scribe`'s
loading constructor raises it when handed an incomplete `Transcription`; the rest of the
throw sites are in `presentation/InternalSession.cc` and `presentation/ProjectSession.cc`,
which assert on `Scribe::is_transcription_complete()` after saving and after restoring.

**The `.cc` includes `Scribe.h`.** `AlreadyTranscribedObject` phrases its message
differently depending on whether the scribe was saving or loading, which is why the
implementation of a leaf exception depends on the main header — worth knowing before
assuming this file is free of the rest of the library.

**Messages name types with `std::type_info::name()`.** What reaches the user is therefore
the compiler's mangled or decorated spelling, which differs between MSVC and GCC and is not
something to parse.

## Used by

| Unit | Component | References |
|---|---|---|
| [scribe/Scribe](Scribe.md) | scribe | 127 |
| [scribe/Transcription](Transcription.md) | scribe | 113 |
| [scribe/TranscriptionScribeContext](TranscriptionScribeContext.md) | scribe | 62 |
| [scribe/ScribeXmlArchiveReader](ScribeXmlArchiveReader.md) | scribe | 39 |
| [scribe/ScribeObjectTag](ScribeObjectTag.md) | scribe | 33 |
| [data-mining/Types](../data-mining/Types.md) | data-mining | 26 |
| [app-logic/LayerInputChannelName](../app-logic/LayerInputChannelName.md) | app-logic | 24 |
| [scribe/ScribeTextArchiveReader](ScribeTextArchiveReader.md) | scribe | 23 |
| [scribe/ScribeBinaryArchiveReader](ScribeBinaryArchiveReader.md) | scribe | 21 |
| [unit-test/TranscribeTest](../unit-test/TranscribeTest.md) | unit-test | 21 |
| [presentation/SessionManagement](../presentation/SessionManagement.md) | presentation | 19 |
| [app-logic/LayerTaskType](../app-logic/LayerTaskType.md) | app-logic | 13 |
| [scribe/ScribeBinaryArchiveWriter](ScribeBinaryArchiveWriter.md) | scribe | 13 |
| [scribe/ScribeTextArchiveWriter](ScribeTextArchiveWriter.md) | scribe | 13 |
| [scribe/ScribeExportRegistry](ScribeExportRegistry.md) | scribe | 12 |
| [scribe/ScribeVoidCastRegistry](ScribeVoidCastRegistry.md) | scribe | 12 |
| [presentation/InternalSession](../presentation/InternalSession.md) | presentation | 11 |
| [presentation/ProjectSession](../presentation/ProjectSession.md) | presentation | 11 |
| [scribe/ScribeLoadRefImpl](ScribeLoadRefImpl.md) | scribe | 9 |
| [scribe/TranscribeQt](TranscribeQt.md) | scribe | 8 |

*... and 14 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/scribe/ScribeExceptions.h
python scripts/gpq.py def GPlatesScribe::Exceptions::UnexpectedXmlElementName --body
python scripts/gpq.py uses UnexpectedXmlElementName --kind class
python scripts/gpq.py hier UnexpectedXmlElementName
```
