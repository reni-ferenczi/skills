# Macros

[Book TOC](../TOC.md)

Every in-tree definition of preprocessor macros, from the `gplates-code` index. 1484 entries.

1346 of them are include guards, listed at the end.

## A

| Name | Unit | Description |
|---|---|---|
| [`ADD_TESTCASE`](../src/unit-test/GPlatesTestSuite.md#free-functions-and-macros) | [unit-test/GPlatesTestSuite](../src/unit-test/GPlatesTestSuite.md) | Registers a member test case into d\_test\_cases\_map under its name |
| [`ADD_TESTSUITE`](../src/unit-test/GPlatesTestSuite.md#free-functions-and-macros) | [unit-test/GPlatesTestSuite](../src/unit-test/GPlatesTestSuite.md) | Instantiates a child test suite one level deeper and registers it into d\_test\_suites\_map |

## B

| Name | Unit | Description |
|---|---|---|
| [`BOOST_BIND_GLOBAL_PLACEHOLDERS`](../src/global/python.md#free-functions-and-macros) | [global/python](../src/global/python.md) | boost::python Note: Boost 1.73+ deprecated including \<boost/bind.hpp\> in favour of including \<boost/bind/bind.hpp\> in order to avoid importing the placeholders \_1, \_2, etc, into the global namespace. |
| [`BOOST_PYTHON_MAX_ARITY`](../src/qt-widgets/HellingerThread.md#free-functions-and-macros) | [qt-widgets/HellingerThread](../src/qt-widgets/HellingerThread.md) | This definition sets the maximum number of parameters that you can send to a boost python function. |
| [`BREAK_BETWEEN_POLYS`](../src/maths/deprecated/PolylineIntersections_test.md#free-functions-and-macros) | [maths/deprecated/PolylineIntersections_test](../src/maths/deprecated/PolylineIntersections_test.md) | — |

## C

| Name | Unit | Description |
|---|---|---|
| [`__CONVENTION__`](../src/opengl/OpenGL.md#free-functions-and-macros) | [opengl/OpenGL](../src/opengl/OpenGL.md) | Platform calling convention for OpenGL API calls (WINAPI on Windows, empty elsewhere) |
| [`CALL_STACK_MAGIC1`](../src/utils/CallStackTracker.md#free-functions-and-macros) | [utils/CallStackTracker](../src/utils/CallStackTracker.md) | Do not invoke this macro directly. |
| [`CALL_STACK_MAGIC2`](../src/utils/CallStackTracker.md#free-functions-and-macros) | [utils/CallStackTracker](../src/utils/CallStackTracker.md) | Do not invoke this macro directly. |
| [`CGAL_DT2_USE_RECURSIVE_PROPAGATE_CONFLICTS`](../src/app-logic/ResolvedTriangulationDelaunay2.md#free-functions-and-macros) | [app-logic/ResolvedTriangulationDelaunay2](../src/app-logic/ResolvedTriangulationDelaunay2.md) | — |
| [`copysign`](../src/app-logic/ResolvedTriangulationNetwork.md#free-functions-and-macros) | [app-logic/ResolvedTriangulationNetwork](../src/app-logic/ResolvedTriangulationNetwork.md) | — |
| [`copysign`](../src/app-logic/TopologyReconstruct.md#free-functions-and-macros) | [app-logic/TopologyReconstruct](../src/app-logic/TopologyReconstruct.md) | — |

## D

| Name | Unit | Description |
|---|---|---|
| [`_DEBUG`](../src/global/python.md#free-functions-and-macros) | [global/python](../src/global/python.md) | — |
| [`DECLARE_PROPERTY_VALUE_FINDER`](../src/feature-visitors/PropertyValueFinder.md#free-functions-and-macros) | [feature-visitors/PropertyValueFinder](../src/feature-visitors/PropertyValueFinder.md) | NOTE: DECLARE\_PROPERTY\_VALUE\_FINDER must be placed at the top of every derivation of GPlatesModel::PropertyValue in order for the get property functions in this file to work with that type of property value. |
| [`DECLARE_PROPERTY_VALUE_FINDER_CLASS`](../src/feature-visitors/PropertyValueFinder.md#free-functions-and-macros) | [feature-visitors/PropertyValueFinder](../src/feature-visitors/PropertyValueFinder.md) | Macro to declare a template specialisation of class PropertyValueFinder. |
| [`DEFINE_COLOUR`](../src/gui/Colour.md#free-functions-and-macros) | [gui/Colour](../src/gui/Colour.md) | Define a function (eg, "get\_black()") that creates a local static colour object and returns it. |
| [`DEFINE_FUNCTION_DEEP_CLONE_AS_INTERP_FUNC`](../src/property-values/GpmlInterpolationFunction.md#free-functions-and-macros) | [property-values/GpmlInterpolationFunction](../src/property-values/GpmlInterpolationFunction.md) | Emits the boilerplate deep\_clone\_as\_interp\_func override in each interpolation-function subclass |
| [`DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL`](../src/model/PropertyValue.md#free-functions-and-macros) | [model/PropertyValue](../src/model/PropertyValue.md) | This macro is used to define the virtual function 'deep\_clone\_as\_prop\_val' inside a class which derives from PropertyValue. |
| [`DEFINE_FUNCTION_DEEP_CLONE_AS_TOPO_SECTION`](../src/property-values/GpmlTopologicalSection.md#free-functions-and-macros) | [property-values/GpmlTopologicalSection](../src/property-values/GpmlTopologicalSection.md) | This macro is used to define the virtual function 'deep\_clone\_as\_topo\_section' inside a class which derives from TopologicalSection. |
| [`DISABLE_GCC_WARNING`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) | — |
| [`DISABLE_MSVC_WARNING`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) | — |
| [`DISPATCH_GUI_FUN`](../src/api/PythonUtils.md#free-functions-and-macros) | [api/PythonUtils](../src/api/PythonUtils.md) | — |

## E

| Name | Unit | Description |
|---|---|---|
| [`ENABLE_GCC_WARNING`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) | — |
| [`ENABLE_MSVC_WARNING`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) | — |
| [`END_OF_LIST`](../src/maths/deprecated/PolylineIntersections_test.md#free-functions-and-macros) | [maths/deprecated/PolylineIntersections_test](../src/maths/deprecated/PolylineIntersections_test.md) | — |
| [`EXCEPTION_SOURCE`](../src/file-io/GpmlPropertyStructuralTypeReaderUtils.md#free-functions-and-macros) | [file-io/GpmlPropertyStructuralTypeReaderUtils](../src/file-io/GpmlPropertyStructuralTypeReaderUtils.md) | — |
| [`EXCEPTION_SOURCE`](../src/file-io/GpmlStructuralTypeReaderUtils.md#free-functions-and-macros) | [file-io/GpmlStructuralTypeReaderUtils](../src/file-io/GpmlStructuralTypeReaderUtils.md) | — |

## G

| Name | Unit | Description |
|---|---|---|
| [`GET_PROP_VAL_NAME`](../src/file-io/deprecated/FeaturePropertiesMap.md#free-functions-and-macros) | [file-io/deprecated/FeaturePropertiesMap](../src/file-io/deprecated/FeaturePropertiesMap.md) | — |
| [`GPLATES_ACCESS_EXPORT_REGISTER_CLASS_TYPE`](../src/scribe/ScribeExportRegistration.md#free-functions-and-macros) | [scribe/ScribeExportRegistration](../src/scribe/ScribeExportRegistration.md) | Registers a single class type in the export registry with private access |
| [`GPLATES_ACCESS_EXPORT_REGISTER_CLASS_TYPE_MACRO`](../src/scribe/ScribeExportRegistration.md#free-functions-and-macros) | [scribe/ScribeExportRegistration](../src/scribe/ScribeExportRegistration.md) | Boost preprocessor macro that wraps single-class registration |
| [`GPLATES_ASSERTION_SOURCE`](../src/global/GPlatesAssert.md#free-functions-and-macros) | [global/GPlatesAssert](../src/global/GPlatesAssert.md) | — |
| [`GPLATES_DEFERRED_API_CALL`](../src/api/DeferredApiCall.md#free-functions-and-macros) | [api/DeferredApiCall](../src/api/DeferredApiCall.md) | Macro that creates a wrapper function for deferred execution on the main thread |
| [`GPLATES_EXCEPTION_SOURCE`](../src/global/GPlatesException.md#free-functions-and-macros) | [global/GPlatesException](../src/global/GPlatesException.md) | Note: we don't use BOOST\_CURRENT\_FUNCTION anymore since it can produce some pretty verbose output when a function has arguments that are template types. |
| [`GPLATES_GDAL_COMPUTE_VERSION`](../src/global/GdalVersion.md#free-functions-and-macros) | [global/GdalVersion](../src/global/GdalVersion.md) | Same as defined in GDAL \>= 1.10... |
| [`GPLATES_GDAL_VERSION_NUM`](../src/global/GdalVersion.md#free-functions-and-macros) | [global/GdalVersion](../src/global/GdalVersion.md) | Same as defined in GDAL \>= 1.10... |
| [`GPLATES_ICU_BOOL`](../src/utils/IdStringSet.md#free-functions-and-macros) | [utils/IdStringSet](../src/utils/IdStringSet.md) | — |
| [`GPLATES_ICU_BOOL`](../src/utils/StringSet.md#free-functions-and-macros) | [utils/StringSet](../src/utils/StringSet.md) | — |
| [`GPLATES_ICU_BOOL`](../src/utils/UnicodeString.md#free-functions-and-macros) | [utils/UnicodeString](../src/utils/UnicodeString.md) | The ICU UnicodeString binary comparison operators returned a UBool rather than a bool, which caused problems. |
| [`GPLATES_OPENGL_BOOL`](../src/opengl/OpenGL.md#free-functions-and-macros) | [opengl/OpenGL](../src/opengl/OpenGL.md) | Normalises a GLboolean value to a real C++ boolean test |
| [`GPLATES_OPENGL_BUFFER_OFFSET`](../src/opengl/OpenGL.md#free-functions-and-macros) | [opengl/OpenGL](../src/opengl/OpenGL.md) | Casts a byte offset into the void pointer expected by buffer-object drawing calls |
| [`GPLATES_PINCH_ZOOM_ENABLED`](../src/qt-widgets/GlobeAndMapWidget.md#free-functions-and-macros) | [qt-widgets/GlobeAndMapWidget](../src/qt-widgets/GlobeAndMapWidget.md) | — |
| [`GPLATES_QTWIDGETS_VelocityFieldCalculatorLayerOptionsWidget_H`](../src/qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/VelocityFieldCalculatorLayerOptionsWidget](../src/qt-widgets/VelocityFieldCalculatorLayerOptionsWidget.md) | — |
| [`GPLATES_SCRIBE_ACCESS_CONSTRUCT_MAX_CONSTRUCTOR_ARGS`](../src/scribe/ScribeAccess.md#free-functions-and-macros) | [scribe/ScribeAccess](../src/scribe/ScribeAccess.md) | The maximum number of object constructor arguments supported in Access::construct\_object(). |
| [`GPLATES_SCRIBE_ACCESS_CONSTRUCT_OBJECT`](../src/scribe/ScribeAccess.md#free-functions-and-macros) | [scribe/ScribeAccess](../src/scribe/ScribeAccess.md) | — |
| [`GPLATES_SCRIBE_ACCESS_CONSTRUCT_OBJECT_PARAM`](../src/scribe/ScribeAccess.md#free-functions-and-macros) | [scribe/ScribeAccess](../src/scribe/ScribeAccess.md) | The following preprocessor macros generate the following code: template \<typename ObjectType, typename A1\> static void construct\_object( ObjectType \*object, const A1 &a1); template \<typename ObjectType, typename A1, typename A2\> static ... |
| [`GPLATES_SCRIBE_ARRAY_INDICES_OP`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Increment array index and decrements predicate counter. |
| [`GPLATES_SCRIBE_ARRAY_INDICES_PRED`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Predicate tests if array dimension decremented to zero. |
| [`GPLATES_SCRIBE_ARRAY_TEMPLATE_INDICES`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Array template template indices (eg, '\[N1\] \[N2\] \[N3\]'). |
| [`GPLATES_SCRIBE_ARRAY_TEMPLATE_INDICES_MACRO`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Returns array template index as, eg, '\[N3\]'. |
| [`GPLATES_SCRIBE_ARRAY_TEMPLATE_PARAMETER_INDICES`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Array template parameter indices returned as a sequence (eg, '(int N1) (int N2) (int N3)'). |
| [`GPLATES_SCRIBE_ARRAY_TEMPLATE_PARAMETER_INDICES_MACRO`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Returns array template parameter index as, eg, '(int N3)'. |
| [`GPLATES_SCRIBE_CONSTRUCT_MAX_CONSTRUCTOR_ARGS`](../src/scribe/ScribeConstructObject.md#free-functions-and-macros) | [scribe/ScribeConstructObject](../src/scribe/ScribeConstructObject.md) | Maximum constructor argument count supported by ConstructObject::construct\_object() |
| [`GPLATES_SCRIBE_CONSTRUCT_OBJECT`](../src/scribe/ScribeConstructObject.md#free-functions-and-macros) | [scribe/ScribeConstructObject](../src/scribe/ScribeConstructObject.md) | Preprocessor helper generating one construct\_object() overload for N arguments |
| [`GPLATES_SCRIBE_CONSTRUCT_OBJECT_PARAM`](../src/scribe/ScribeConstructObject.md#free-functions-and-macros) | [scribe/ScribeConstructObject](../src/scribe/ScribeConstructObject.md) | Preprocessor helper emitting one 'const Ai &ai' constructor parameter |
| [`GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_FUNCTIONS_ARRAY_CALL`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates double argument function delegate overloads for native \*arrays\* for a specific multi-level pointer level. |
| [`GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_FUNCTIONS_NON_ARRAY_CALL`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates double argument function delegate overloads for \*non-arrays\* for a specific multi-level pointer level. |
| [`GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_NON_POINTER_FUNCTIONS`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Double \*non-pointer\* argument function delegates. |
| [`GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_NON_POINTER_FUNCTIONS_ARRAY`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates double \*non-pointer\* argument function delegate overloads for native \*arrays\*. |
| [`GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Double \*pointer\* argument function delegates. |
| [`GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS_ARRAY`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates double pointer argument function delegate overloads for native \*arrays\* for a specific multi-level pointer level. |
| [`GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS_CALL`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates double pointer argument function delegate overloads for a specific multi-level pointer level. |
| [`GPLATES_SCRIBE_DELEGATE_DOUBLE_ARG_POINTER_FUNCTIONS_INDEX`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates double argument pointer function delegate overloads for a multi-level pointer of dimension 'pointer\_level'. |
| [`GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Iterate over half-open range \[ 0, 2\*pow(2,pointer\_level) ) and generate all const/non-const multi-level pointer combinations for a particular pointer-level. |
| [`GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_ARRAY`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates single argument function delegate overloads for native \*arrays\* for a specific multi-level pointer level. |
| [`GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_ARRAY_CALL`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates single argument function delegate overloads for native \*arrays\* for a specific multi-level pointer level. |
| [`GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_CALL`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates single argument function delegate overloads for a specific multi-level pointer level. |
| [`GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_INDEX`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates single argument function delegate overloads for a multi-level pointer of dimension 'pointer\_level'. |
| [`GPLATES_SCRIBE_DELEGATE_SINGLE_ARG_FUNCTIONS_NON_ARRAY_CALL`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Generates single argument function delegate overloads for \*non-arrays\* for a specific multi-level pointer level. |
| [`GPLATES_SCRIBE_MAX_ARRAY_DIMENSION`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | The maximum dimension of transcribable native arrays. |
| [`GPLATES_SCRIBE_MAX_POINTER_DIMENSION`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | The maximum dimension of transcribable multi-level pointers. |
| [`GPLATES_SCRIBE_POW2`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | This is just pow(2,n) implemented as 1\*2\*2\*2\*, ie, repeated 'n' times... |
| [`GPLATES_SCRIBE_POW2_MUL_BY_2`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Operation for GPLATES\_SCRIBE\_POW2. |
| [`GPLATES_SCRIBE_POW2_PRED`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Predicate for GPLATES\_SCRIBE\_POW2. |
| [`GPLATES_SCRIBE_PRINT`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | / |
| [`GPLATES_SCRIBE_QUALIFIED_OBJECT`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Returns 'const' if least-significant bit of 'index' is set, otherwise nothing. |
| [`GPLATES_SCRIBE_QUALIFIED_POINTER`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Repeat '\*const' or '\*' character 'pointer\_level' times depending on 'pointer\_level' number of bit flags in 'index'. |
| [`GPLATES_SCRIBE_QUALIFIED_POINTER_MACRO`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Return '\*const' or '\*' depending on the state. |
| [`GPLATES_SCRIBE_QUALIFIED_POINTER_OP`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Right shifts by one bit and tests the least-significant bit (that was shifted out). |
| [`GPLATES_SCRIBE_QUALIFIED_POINTER_PRED`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Predicate tests if pointer-level counter is zero. |
| [`GPLATES_SCRIBE_UNQUALIFIED_POINTER`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | Repeat '\*' character 'pointer\_level' times. |
| [`GPLATES_SINGLETON_CONSTRUCTOR_DECL`](../src/utils/Singleton.md#free-functions-and-macros) | [utils/Singleton](../src/utils/Singleton.md) | Adds a default (protected) constructor and friend declaration. |
| [`GPLATES_SINGLETON_CONSTRUCTOR_DEF`](../src/utils/Singleton.md#free-functions-and-macros) | [utils/Singleton](../src/utils/Singleton.md) | Adds a default (protected) constructor implementation and friend declaration. |
| [`GPLATES_SINGLETON_PUBLIC_CONSTRUCTOR_DECL`](../src/utils/Singleton.md#free-functions-and-macros) | [utils/Singleton](../src/utils/Singleton.md) | Adds a default (public) constructor and friend declaration. |
| [`GPLATES_SINGLETON_PUBLIC_CONSTRUCTOR_DEF`](../src/utils/Singleton.md#free-functions-and-macros) | [utils/Singleton](../src/utils/Singleton.md) | Adds a default (public) constructor implementation and friend declaration. |
| [`GPLATES_USE_NATIVE_FILE_DIALOG`](../src/qt-widgets/SaveFileDialog.md#free-functions-and-macros) | [qt-widgets/SaveFileDialog](../src/qt-widgets/SaveFileDialog.md) | Compile-time switch selecting the native save dialog on Windows/macOS |

## H

| Name | Unit | Description |
|---|---|---|
| [`HAS_FUNCTION`](../src/utils/HasFunction.md#free-functions-and-macros) | [utils/HasFunction](../src/utils/HasFunction.md) | Macro generating a meta-function to detect global functions via SFINAE |
| [`HAS_MEMBER_FUNCTION`](../src/utils/HasFunction.md#free-functions-and-macros) | [utils/HasFunction](../src/utils/HasFunction.md) | Macro generating a meta-function to detect member functions via SFINAE |
| [`HAVE_SNPRINTF`](../src/global/python.md#free-functions-and-macros) | [global/python](../src/global/python.md) | — |
| [`HIDE_SHADER_TEST_VARIABLE_CONTROLS`](../src/qt-widgets/ScalarField3DLayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ScalarField3DLayerOptionsWidget](../src/qt-widgets/ScalarField3DLayerOptionsWidget.md) | Define this to hide the GUI controls that change the shader test variables. |

## I

| Name | Unit | Description |
|---|---|---|
| [`INTERTEC_MONOTONICALLY_DECREASING_LATITUDE_BEHAVIOUR`](../src/maths/GeometryInterpolation.md#free-functions-and-macros) | [maths/GeometryInterpolation](../src/maths/GeometryInterpolation.md) | Define this to make our monotonically decreasing latitudes behave like the original Intertec program. |

## L

| Name | Unit | Description |
|---|---|---|
| [`LOKI_ANONYMOUS_VARIABLE`](../src/system-fixes/loki/ScopeGuard.md#free-functions-and-macros) | [system-fixes/loki/ScopeGuard](../src/system-fixes/loki/ScopeGuard.md) | — |
| [`LOKI_CONCATENATE`](../src/system-fixes/loki/ScopeGuard.md#free-functions-and-macros) | [system-fixes/loki/ScopeGuard](../src/system-fixes/loki/ScopeGuard.md) | — |
| [`LOKI_CONCATENATE_DIRECT`](../src/system-fixes/loki/ScopeGuard.md#free-functions-and-macros) | [system-fixes/loki/ScopeGuard](../src/system-fixes/loki/ScopeGuard.md) | — |
| [`LOKI_ON_BLOCK_EXIT`](../src/system-fixes/loki/ScopeGuard.md#free-functions-and-macros) | [system-fixes/loki/ScopeGuard](../src/system-fixes/loki/ScopeGuard.md) | Macro declaring an anonymous ScopeGuard bound via MakeGuard, run at block exit |
| [`LOKI_ON_BLOCK_EXIT_OBJ`](../src/system-fixes/loki/ScopeGuard.md#free-functions-and-macros) | [system-fixes/loki/ScopeGuard](../src/system-fixes/loki/ScopeGuard.md) | Macro declaring an anonymous ScopeGuard bound via MakeObjGuard, run at block exit |

## M

| Name | Unit | Description |
|---|---|---|
| [`MaxConcurrentThreads`](../src/data-mining/deprecated/TaskQueue.md#free-functions-and-macros) | [data-mining/deprecated/TaskQueue](../src/data-mining/deprecated/TaskQueue.md) | — |

## N

| Name | Unit | Description |
|---|---|---|
| [`name`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | Starts profiling until the end of the current scope in which this PROFILE\_BLOCK call was made. |
| [`new`](../src/unit-test/FeatureHandleTest.md#free-functions-and-macros) | [unit-test/FeatureHandleTest](../src/unit-test/FeatureHandleTest.md) | Redefines new for the rest of the file to route through the pool-aware operator new(size\_t,bool) |
| [`NO_IMPORT_ARRAY`](../src/global/python.md#free-functions-and-macros) | [global/python](../src/global/python.md) | — |
| [`NOMINMAX`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | — |
| [`NON_NULL_INTRUSIVE_PTR_HPP_INCLUDED`](../src/utils/non_null_intrusive_ptr.md#free-functions-and-macros) | [utils/non_null_intrusive_ptr](../src/utils/non_null_intrusive_ptr.md) | — |
| [`NPY_NO_DEPRECATED_API`](../src/global/python.md#free-functions-and-macros) | [global/python](../src/global/python.md) | Avoid deprecation warnings. |
| [`NUM_ELEMS`](../src/file-io/ReadErrorMessages.md#free-functions-and-macros) | [file-io/ReadErrorMessages](../src/file-io/ReadErrorMessages.md) | — |
| [`NUM_ELEMS`](../src/gui/FeatureTableModel.md#free-functions-and-macros) | [gui/FeatureTableModel](../src/gui/FeatureTableModel.md) | — |
| [`NUM_ELEMS`](../src/maths/deprecated/PolylineIntersections_test.md#free-functions-and-macros) | [maths/deprecated/PolylineIntersections_test](../src/maths/deprecated/PolylineIntersections_test.md) | — |
| [`NUM_ELEMS`](../src/qt-widgets/KinematicGraphsDialog.md#free-functions-and-macros) | [qt-widgets/KinematicGraphsDialog](../src/qt-widgets/KinematicGraphsDialog.md) | — |
| [`NUM_ELEMS`](../src/qt-widgets/TotalReconstructionPolesDialog.md#free-functions-and-macros) | [qt-widgets/TotalReconstructionPolesDialog](../src/qt-widgets/TotalReconstructionPolesDialog.md) | — |

## P

| Name | Unit | Description |
|---|---|---|
| [`POINT`](../src/maths/deprecated/PolylineIntersections_test.md#free-functions-and-macros) | [maths/deprecated/PolylineIntersections_test](../src/maths/deprecated/PolylineIntersections_test.md) | — |
| [`POP_GCC_WARNINGS`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) | — |
| [`POP_MSVC_WARNINGS`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) | — |
| [`PROFILE_ANONYMOUS_VARIABLE`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | — |
| [`PROFILE_BEGIN`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | Starts profiling until the matching PROFILE\_END is reached or an exception is thrown or the function we're in returns early. name is a string of type "const char \*". |
| [`PROFILE_CODE`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | Starts profiling just before the source code expression code and stops profiling just after. profile\_tag is only used internally to match PROFILE\_BEGIN and PROFILE\_END calls. profile\_tag is an identifier and must use C++ naming rules. ... |
| [`PROFILE_CONCATENATE`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | — |
| [`PROFILE_CONCATENATE_DIRECT`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | — |
| [`PROFILE_END`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | Stops profiling the matching PROFILE\_BEGIN call. |
| [`PROFILE_FUNC`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | Same as PROFILE\_BLOCK except the name of the profile is the function that PROFILE\_BLOCK is called from. |
| [`PROFILE_REPORT_TO_FILE`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | Writes the profiling data as text to the file filename where filename is a std::string. |
| [`PROFILE_REPORT_TO_OSTREAM`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | Writes the profiling data as text to the output stream output\_stream where output\_stream is a std::ostream &. |
| [`PROFILE_SCOPE_VARIABLE`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | — |
| [`PROFILE_UNUSED`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) | — |
| [`PUSH_GCC_WARNINGS`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) | — |
| [`PUSH_MSVC_WARNINGS`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) | — |
| [`PY_ARRAY_UNIQUE_SYMBOL`](../src/global/python.md#free-functions-and-macros) | [global/python](../src/global/python.md) | This just needs to be something unique (that doesn't clash with boost::python::numpy for example). |

## S

| Name | Unit | Description |
|---|---|---|
| [`SAVE_LOAD_CLASS_DATA_USING_VARIANT`](../src/unit-test/TranscribeTest.md#free-functions-and-macros) | [unit-test/TranscribeTest](../src/unit-test/TranscribeTest.md) | Notes that Data can be constructed via either its int or variant constructor |
| [`SCRIBE_EXPORT_DATA_MINING`](../src/data-mining/ScribeExportDataMining.md#free-functions-and-macros) | [data-mining/ScribeExportDataMining](../src/data-mining/ScribeExportDataMining.md) | Macro that maps data-mining filter configs to stable string identifiers for serialization |
| [`SCRIBE_EXPORT_EXTERNAL`](../src/scribe/ScribeExportExternal.md#free-functions-and-macros) | [scribe/ScribeExportExternal](../src/scribe/ScribeExportExternal.md) | Registers fundamental types, Qt types, and standard library types for transcription |
| [`SCRIBE_EXPORT_GPLATES`](../src/entry-points/ScribeExportGPlates.md#free-functions-and-macros) | [entry-points/ScribeExportGPlates](../src/entry-points/ScribeExportGPlates.md) | Combines data-mining and external type groups for main application export registration |
| [`SCRIBE_EXPORT_GPLATES_DEMO_NO_GUI`](../src/entry-points/ScribeExportGPlatesDemoNoGui.md#free-functions-and-macros) | [entry-points/ScribeExportGPlatesDemoNoGui](../src/entry-points/ScribeExportGPlatesDemoNoGui.md) | Groups external types for demo application export registration |
| [`SCRIBE_EXPORT_GPLATES_UNIT_TEST`](../src/entry-points/ScribeExportGPlatesUnitTest.md#free-functions-and-macros) | [entry-points/ScribeExportGPlatesUnitTest](../src/entry-points/ScribeExportGPlatesUnitTest.md) | Combines unit-test and external type groups for test executable export registration |
| [`SCRIBE_EXPORT_PYGPLATES`](../src/entry-points/ScribeExportPyGPlates.md#free-functions-and-macros) | [entry-points/ScribeExportPyGPlates](../src/entry-points/ScribeExportPyGPlates.md) | Groups external types for pyGPlates extension module export registration |
| [`SCRIBE_EXPORT_REGISTRATION`](../src/scribe/ScribeExportRegistration.md#free-functions-and-macros) | [scribe/ScribeExportRegistration](../src/scribe/ScribeExportRegistration.md) | Registers a set of polymorphic class types for serialization at program startup |
| [`SCRIBE_EXPORT_UNIT_TEST`](../src/unit-test/ScribeExportUnitTest.md#free-functions-and-macros) | [unit-test/ScribeExportUnitTest](../src/unit-test/ScribeExportUnitTest.md) | Macro registering transcription test types for Scribe serialization |
| [`STRINGIFY_WARNING`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) | Used to support gcc's \_Pragma() preprocessor operator which expects a string literal. |

## T

| Name | Unit | Description |
|---|---|---|
| [`TEMPORARY_HACK_NO_DIRECTIONAL_LIGHT_FOR_NORMAL_MAPS`](../src/opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md#free-functions-and-macros) | [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../src/opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) | Standing workaround disabling directional lighting on normal maps until a light canvas tool exists |
| [`TRACK_CALL_STACK`](../src/utils/CallStackTracker.md#free-functions-and-macros) | [utils/CallStackTracker](../src/utils/CallStackTracker.md) | Track the call stack. |
| [`TRANSCRIBE_SOURCE`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) | — |
| [`TRANSCRIBE_SOURCE`](../src/scribe/TranscribeEnumProtocol.md#free-functions-and-macros) | [scribe/TranscribeEnumProtocol](../src/scribe/TranscribeEnumProtocol.md) | — |

## Z

| Name | Unit | Description |
|---|---|---|
| [`ZLIB_WINAPI`](../src/file-io/GzipFile.md#free-functions-and-macros) | [file-io/GzipFile](../src/file-io/GzipFile.md) | Note that, on Windows, ZLIB\_WINAPI should be defined before including "zlib.h". |

## Include guards

Header guards, one per header; they carry no meaning beyond protecting their own file.

| Name | Unit |
|---|---|
| [`_GPLATES_CONTROLS_ANIMATIONTIMER_H_`](../src/deprecated/controls/AnimationTimer.md#free-functions-and-macros) | [deprecated/controls/AnimationTimer](../src/deprecated/controls/AnimationTimer.md) |
| [`_GPLATES_CONTROLS_DIALOGS_H_`](../src/deprecated/controls/Dialogs.md#free-functions-and-macros) | [deprecated/controls/Dialogs](../src/deprecated/controls/Dialogs.md) |
| [`_GPLATES_CONTROLS_FILE_H_`](../src/deprecated/controls/File.md#free-functions-and-macros) | [deprecated/controls/File](../src/deprecated/controls/File.md) |
| [`_GPLATES_CONTROLS_GUICALLS_H_`](../src/deprecated/controls/GuiCalls.md#free-functions-and-macros) | [deprecated/controls/GuiCalls](../src/deprecated/controls/GuiCalls.md) |
| [`_GPLATES_CONTROLS_LIFETIME_H_`](../src/deprecated/controls/Lifetime.md#free-functions-and-macros) | [deprecated/controls/Lifetime](../src/deprecated/controls/Lifetime.md) |
| [`_GPLATES_CONTROLS_RECONSTRUCT_H_`](../src/deprecated/controls/Reconstruct.md#free-functions-and-macros) | [deprecated/controls/Reconstruct](../src/deprecated/controls/Reconstruct.md) |
| [`_GPLATES_CONTROLS_VIEW_H_`](../src/deprecated/controls/View.md#free-functions-and-macros) | [deprecated/controls/View](../src/deprecated/controls/View.md) |
| [`_GPLATES_FILEIO_GPLATESREADER_H_`](../src/file-io/deprecated/GPlatesReader.md#free-functions-and-macros) | [file-io/deprecated/GPlatesReader](../src/file-io/deprecated/GPlatesReader.md) |
| [`_GPLATES_FILEIO_NETCDFREADER_H_`](../src/file-io/deprecated/NetCDFReader.md#free-functions-and-macros) | [file-io/deprecated/NetCDFReader](../src/file-io/deprecated/NetCDFReader.md) |
| [`_GPLATES_FILEIO_NETCDFWRITER_H_`](../src/file-io/deprecated/NetCDFWriter.md#free-functions-and-macros) | [file-io/deprecated/NetCDFWriter](../src/file-io/deprecated/NetCDFWriter.md) |
| [`_GPLATES_FILEIO_XMLPARSER_H_`](../src/file-io/deprecated/XMLParser.md#free-functions-and-macros) | [file-io/deprecated/XMLParser](../src/file-io/deprecated/XMLParser.md) |
| [`_GPLATES_GLOBAL_ALREADYINITIALISEDSINGLETONEXCEPTION_H_`](../src/global/deprecated/AlreadyInitialisedSingletonException.md#free-functions-and-macros) | [global/deprecated/AlreadyInitialisedSingletonException](../src/global/deprecated/AlreadyInitialisedSingletonException.md) |
| [`_GPLATES_GLOBAL_ASSERT_H_`](../src/global/GPlatesAssert.md#free-functions-and-macros) | [global/GPlatesAssert](../src/global/GPlatesAssert.md) |
| [`_GPLATES_GLOBAL_CONTROLFLOWEXCEPTION_H_`](../src/global/ControlFlowException.md#free-functions-and-macros) | [global/ControlFlowException](../src/global/ControlFlowException.md) |
| [`_GPLATES_GLOBAL_ILLEGALPARAMETERSEXCEPTION_H_`](../src/global/IllegalParametersException.md#free-functions-and-macros) | [global/IllegalParametersException](../src/global/IllegalParametersException.md) |
| [`_GPLATES_GLOBAL_INTERNALRID_H_`](../src/global/deprecated/InternalRID.md#free-functions-and-macros) | [global/deprecated/InternalRID](../src/global/deprecated/InternalRID.md) |
| [`_GPLATES_GLOBAL_INVALIDPARAMETERSEXCEPTION_H_`](../src/global/InvalidParametersException.md#free-functions-and-macros) | [global/InvalidParametersException](../src/global/InvalidParametersException.md) |
| [`_GPLATES_GLOBAL_NOTYETIMPLEMENTEDEXCEPTION_H_`](../src/global/NotYetImplementedException.md#free-functions-and-macros) | [global/NotYetImplementedException](../src/global/NotYetImplementedException.md) |
| [`_GPLATES_GLOBAL_NULLPARAMETEREXCEPTION_H_`](../src/global/NullParameterException.md#free-functions-and-macros) | [global/NullParameterException](../src/global/NullParameterException.md) |
| [`_GPLATES_GLOBAL_UNINITIALISEDITERATOREXCEPTION_H_`](../src/global/UninitialisedIteratorException.md#free-functions-and-macros) | [global/UninitialisedIteratorException](../src/global/UninitialisedIteratorException.md) |
| [`_GPLATES_GLOBAL_UNINITIALISEDSINGLETONEXCEPTION_H_`](../src/global/deprecated/UninitialisedSingletonException.md#free-functions-and-macros) | [global/deprecated/UninitialisedSingletonException](../src/global/deprecated/UninitialisedSingletonException.md) |
| [`_GPLATES_GLOBAL_UNSUPPORTEDFUNCTIONEXCEPTION_H_`](../src/global/UnsupportedFunctionException.md#free-functions-and-macros) | [global/UnsupportedFunctionException](../src/global/UnsupportedFunctionException.md) |
| [`_GPLATES_GUI_GLCANVAS_H_`](../src/gui/deprecated/GLCanvas.md#free-functions-and-macros) | [gui/deprecated/GLCanvas](../src/gui/deprecated/GLCanvas.md) |
| [`_GPLATES_GUI_GUIEXCEPTION_H_`](../src/gui/GuiException.md#free-functions-and-macros) | [gui/GuiException](../src/gui/GuiException.md) |
| [`_GPLATES_GUI_MAINWINDOW_H_`](../src/gui/deprecated/MainWindow.md#free-functions-and-macros) | [gui/deprecated/MainWindow](../src/gui/deprecated/MainWindow.md) |
| [`_GPLATES_MATHS_CARTESIANCONVMATRIX3D_H_`](../src/maths/CartesianConvMatrix3D.md#free-functions-and-macros) | [maths/CartesianConvMatrix3D](../src/maths/CartesianConvMatrix3D.md) |
| [`_GPLATES_MATHS_CV_H_`](../src/maths/CalculateVelocity.md#free-functions-and-macros) | [maths/CalculateVelocity](../src/maths/CalculateVelocity.md) |
| [`_GPLATES_MATHS_FUNCTIONDOMAINEXCEPTION_H_`](../src/maths/FunctionDomainException.md#free-functions-and-macros) | [maths/FunctionDomainException](../src/maths/FunctionDomainException.md) |
| [`_GPLATES_MATHS_GRIDONSPHERE_H_`](../src/maths/deprecated/GridOnSphere.md#free-functions-and-macros) | [maths/deprecated/GridOnSphere](../src/maths/deprecated/GridOnSphere.md) |
| [`_GPLATES_MATHS_HIGHPRECISION_H_`](../src/maths/HighPrecision.md#free-functions-and-macros) | [maths/HighPrecision](../src/maths/HighPrecision.md) |
| [`_GPLATES_MATHS_INDETERMINATERESULTEXCEPTION_H_`](../src/maths/IndeterminateResultException.md#free-functions-and-macros) | [maths/IndeterminateResultException](../src/maths/IndeterminateResultException.md) |
| [`_GPLATES_MATHS_INVALIDGREATCIRCLEARCEXCEPTION_H_`](../src/maths/InvalidGreatCircleArcException.md#free-functions-and-macros) | [maths/InvalidGreatCircleArcException](../src/maths/InvalidGreatCircleArcException.md) |
| [`_GPLATES_MATHS_INVALIDGRIDEXCEPTION_H_`](../src/maths/InvalidGridException.md#free-functions-and-macros) | [maths/InvalidGridException](../src/maths/InvalidGridException.md) |
| [`_GPLATES_MATHS_INVALIDOPERATIONEXCEPTION_H_`](../src/maths/InvalidOperationException.md#free-functions-and-macros) | [maths/InvalidOperationException](../src/maths/InvalidOperationException.md) |
| [`_GPLATES_MATHS_MATHEMATICALEXCEPTION_H_`](../src/maths/MathematicalException.md#free-functions-and-macros) | [maths/MathematicalException](../src/maths/MathematicalException.md) |
| [`_GPLATES_MATHS_ROTATIONHISTORY_H_`](../src/maths/deprecated/RotationHistory.md#free-functions-and-macros) | [maths/deprecated/RotationHistory](../src/maths/deprecated/RotationHistory.md) |
| [`_GPLATES_MATHS_ROTATIONSEQUENCE_H_`](../src/maths/deprecated/RotationSequence.md#free-functions-and-macros) | [maths/deprecated/RotationSequence](../src/maths/deprecated/RotationSequence.md) |
| [`_GPLATES_MATHS_SMALLCIRCLE_H_`](../src/maths/SmallCircle.md#free-functions-and-macros) | [maths/SmallCircle](../src/maths/SmallCircle.md) |
| [`_GPLATES_MATHS_UNITVECTOR3D_H_`](../src/maths/UnitVector3D.md#free-functions-and-macros) | [maths/UnitVector3D](../src/maths/UnitVector3D.md) |
| [`_GPLATES_MATHS_VECTOR3D_H_`](../src/maths/Vector3D.md#free-functions-and-macros) | [maths/Vector3D](../src/maths/Vector3D.md) |
| [`_GPLATES_MATHS_VIOLATEDCLASSINVARIANTEXCEPTION_H_`](../src/maths/ViolatedClassInvariantException.md#free-functions-and-macros) | [maths/ViolatedClassInvariantException](../src/maths/ViolatedClassInvariantException.md) |
| [`_GPLATES_MATHS_VIOLATEDDIRVECTORINVARIANTEXCEPTION_H_`](../src/maths/ViolatedDirVectorInvariantException.md#free-functions-and-macros) | [maths/ViolatedDirVectorInvariantException](../src/maths/ViolatedDirVectorInvariantException.md) |
| [`_GPLATES_MATHS_VIOLATEDSMALLCIRCLEINVARIANTEXCEPTION_H_`](../src/maths/ViolatedSmallCircleInvariantException.md#free-functions-and-macros) | [maths/ViolatedSmallCircleInvariantException](../src/maths/ViolatedSmallCircleInvariantException.md) |
| [`_GPLATES_MATHS_VIOLATEDUNITVECTORINVARIANTEXCEPTION_H_`](../src/maths/ViolatedUnitVectorInvariantException.md#free-functions-and-macros) | [maths/ViolatedUnitVectorInvariantException](../src/maths/ViolatedUnitVectorInvariantException.md) |
| [`_GPLATES_OPENGL_OPENGLBADALLOCEXCEPTION_H_`](../src/opengl/OpenGLBadAllocException.md#free-functions-and-macros) | [opengl/OpenGLBadAllocException](../src/opengl/OpenGLBadAllocException.md) |
| [`_GPLATES_OPENGL_OPENGLEXCEPTION_H_`](../src/opengl/OpenGLException.md#free-functions-and-macros) | [opengl/OpenGLException](../src/opengl/OpenGLException.md) |
| [`AGEMODELREADER_H`](../src/file-io/AgeModelReader.md#free-functions-and-macros) | [file-io/AgeModelReader](../src/file-io/AgeModelReader.md) |
| [`DEBUG_UNDEFINED_FROM_GLOBAL_PYTHON_H`](../src/global/python.md#free-functions-and-macros) | [global/python](../src/global/python.md) |
| [`GENERATE_VELOCITY_DOMAIN_CITCOMS_DIALOG_H`](../src/qt-widgets/GenerateVelocityDomainCitcomsDialog.md#free-functions-and-macros) | [qt-widgets/GenerateVelocityDomainCitcomsDialog](../src/qt-widgets/GenerateVelocityDomainCitcomsDialog.md) |
| [`GENERATE_VELOCITY_DOMAIN_CITCOMS_H`](../src/app-logic/GenerateVelocityDomainCitcoms.md#free-functions-and-macros) | [app-logic/GenerateVelocityDomainCitcoms](../src/app-logic/GenerateVelocityDomainCitcoms.md) |
| [`GENERATE_VELOCITY_DOMAIN_CITCOMS_H`](../src/app-logic/GenerateVelocityDomainTerra.md#free-functions-and-macros) | [app-logic/GenerateVelocityDomainTerra](../src/app-logic/GenerateVelocityDomainTerra.md) |
| [`GENERATE_VELOCITY_DOMAIN_LATLON_DIALOG_H`](../src/qt-widgets/GenerateVelocityDomainLatLonDialog.md#free-functions-and-macros) | [qt-widgets/GenerateVelocityDomainLatLonDialog](../src/qt-widgets/GenerateVelocityDomainLatLonDialog.md) |
| [`GENERATE_VELOCITY_DOMAIN_TERRA_DIALOG_H`](../src/qt-widgets/GenerateVelocityDomainTerraDialog.md#free-functions-and-macros) | [qt-widgets/GenerateVelocityDomainTerraDialog](../src/qt-widgets/GenerateVelocityDomainTerraDialog.md) |
| [`GPLATES_API_ABSTRACTCONSOLE_H`](../src/api/AbstractConsole.md#free-functions-and-macros) | [api/AbstractConsole](../src/api/AbstractConsole.md) |
| [`GPLATES_API_ABSTRACTPYTHONRUNNER_H`](../src/api/AbstractPythonRunner.md#free-functions-and-macros) | [api/AbstractPythonRunner](../src/api/AbstractPythonRunner.md) |
| [`GPLATES_API_CONSOLEREADER_H`](../src/api/ConsoleReader.md#free-functions-and-macros) | [api/ConsoleReader](../src/api/ConsoleReader.md) |
| [`GPLATES_API_CONSOLEWRITER_H`](../src/api/ConsoleWriter.md#free-functions-and-macros) | [api/ConsoleWriter](../src/api/ConsoleWriter.md) |
| [`GPLATES_API_COREGISTRATIONPROXY_H`](../src/api/PyCoregistrationLayerProxy.md#free-functions-and-macros) | [api/PyCoregistrationLayerProxy](../src/api/PyCoregistrationLayerProxy.md) |
| [`GPLATES_API_DEFERREDAPICALL_H`](../src/api/DeferredApiCall.md#free-functions-and-macros) | [api/DeferredApiCall](../src/api/DeferredApiCall.md) |
| [`GPLATES_API_DEFERREDAPICALLIMPL_H`](../src/api/DeferredApiCallImpl.md#free-functions-and-macros) | [api/DeferredApiCallImpl](../src/api/DeferredApiCallImpl.md) |
| [`GPLATES_API_FEATURE_H`](../src/api/PyFeature.md#free-functions-and-macros) | [api/PyFeature](../src/api/PyFeature.md) |
| [`GPLATES_API_FEATURECOLLECTION_H`](../src/api/PyFeatureCollection.md#free-functions-and-macros) | [api/PyFeatureCollection](../src/api/PyFeatureCollection.md) |
| [`GPLATES_API_PYTHONEXECUTIONMONITOR_H`](../src/api/PythonExecutionMonitor.md#free-functions-and-macros) | [api/PythonExecutionMonitor](../src/api/PythonExecutionMonitor.md) |
| [`GPLATES_API_PYTHONEXECUTIONTHREAD_H`](../src/api/PythonExecutionThread.md#free-functions-and-macros) | [api/PythonExecutionThread](../src/api/PythonExecutionThread.md) |
| [`GPLATES_API_PYTHONINTERPRETERLOCKER_H`](../src/api/PythonInterpreterLocker.md#free-functions-and-macros) | [api/PythonInterpreterLocker](../src/api/PythonInterpreterLocker.md) |
| [`GPLATES_API_PYTHONINTERPRETERUNLOCKER_H`](../src/api/PythonInterpreterUnlocker.md#free-functions-and-macros) | [api/PythonInterpreterUnlocker](../src/api/PythonInterpreterUnlocker.md) |
| [`GPLATES_API_PYTHONRUNNER_H`](../src/api/PythonRunner.md#free-functions-and-macros) | [api/PythonRunner](../src/api/PythonRunner.md) |
| [`GPLATES_API_PYTHONUTILS_H`](../src/api/PythonUtils.md#free-functions-and-macros) | [api/PythonUtils](../src/api/PythonUtils.md) |
| [`GPLATES_API_SLEEPER_H`](../src/api/Sleeper.md#free-functions-and-macros) | [api/Sleeper](../src/api/Sleeper.md) |
| [`GPLATES_APP_LOGIC_AGEMODELCOLLECTION_H`](../src/app-logic/AgeModelCollection.md#free-functions-and-macros) | [app-logic/AgeModelCollection](../src/app-logic/AgeModelCollection.md) |
| [`GPLATES_APP_LOGIC_APPLICATIONSTATE_H`](../src/app-logic/ApplicationState.md#free-functions-and-macros) | [app-logic/ApplicationState](../src/app-logic/ApplicationState.md) |
| [`GPLATES_APP_LOGIC_APPLOGICUTILS_H`](../src/app-logic/AppLogicUtils.md#free-functions-and-macros) | [app-logic/AppLogicUtils](../src/app-logic/AppLogicUtils.md) |
| [`GPLATES_APP_LOGIC_ASSIGNPLATEIDS_H`](../src/app-logic/AssignPlateIds.md#free-functions-and-macros) | [app-logic/AssignPlateIds](../src/app-logic/AssignPlateIds.md) |
| [`GPLATES_APP_LOGIC_COREGISTRATIONDATA_H`](../src/app-logic/CoRegistrationData.md#free-functions-and-macros) | [app-logic/CoRegistrationData](../src/app-logic/CoRegistrationData.md) |
| [`GPLATES_APP_LOGIC_COREGISTRATIONLAYERPARAMS_H`](../src/app-logic/CoRegistrationLayerParams.md#free-functions-and-macros) | [app-logic/CoRegistrationLayerParams](../src/app-logic/CoRegistrationLayerParams.md) |
| [`GPLATES_APP_LOGIC_COREGISTRATIONLAYERPROXY_H`](../src/app-logic/CoRegistrationLayerProxy.md#free-functions-and-macros) | [app-logic/CoRegistrationLayerProxy](../src/app-logic/CoRegistrationLayerProxy.md) |
| [`GPLATES_APP_LOGIC_COREGISTRATIONLAYERTASK_H`](../src/app-logic/CoRegistrationLayerTask.md#free-functions-and-macros) | [app-logic/CoRegistrationLayerTask](../src/app-logic/CoRegistrationLayerTask.md) |
| [`GPLATES_APP_LOGIC_DEFORMATION_STRAIN_H`](../src/app-logic/DeformationStrain.md#free-functions-and-macros) | [app-logic/DeformationStrain](../src/app-logic/DeformationStrain.md) |
| [`GPLATES_APP_LOGIC_DEFORMATION_STRAIN_RATE_H`](../src/app-logic/DeformationStrainRate.md#free-functions-and-macros) | [app-logic/DeformationStrainRate](../src/app-logic/DeformationStrainRate.md) |
| [`GPLATES_APP_LOGIC_DEPENDENTTOPOLOGICALSECTIONLAYERS_H`](../src/app-logic/DependentTopologicalSectionLayers.md#free-functions-and-macros) | [app-logic/DependentTopologicalSectionLayers](../src/app-logic/DependentTopologicalSectionLayers.md) |
| [`GPLATES_APP_LOGIC_EXTRACTRASTERFEATUREPROPERTIES_H`](../src/app-logic/ExtractRasterFeatureProperties.md#free-functions-and-macros) | [app-logic/ExtractRasterFeatureProperties](../src/app-logic/ExtractRasterFeatureProperties.md) |
| [`GPLATES_APP_LOGIC_EXTRACTSCALARFIELD3DFEATUREPROPERTIES_H`](../src/app-logic/ExtractScalarField3DFeatureProperties.md#free-functions-and-macros) | [app-logic/ExtractScalarField3DFeatureProperties](../src/app-logic/ExtractScalarField3DFeatureProperties.md) |
| [`GPLATES_APP_LOGIC_FEATURECOLLECTIONFILEIO_H`](../src/app-logic/FeatureCollectionFileIO.md#free-functions-and-macros) | [app-logic/FeatureCollectionFileIO](../src/app-logic/FeatureCollectionFileIO.md) |
| [`GPLATES_APP_LOGIC_FEATURECOLLECTIONFILESTATE_H`](../src/app-logic/FeatureCollectionFileState.md#free-functions-and-macros) | [app-logic/FeatureCollectionFileState](../src/app-logic/FeatureCollectionFileState.md) |
| [`GPLATES_APP_LOGIC_FLOWLINEGEOMETRYPOPULATOR_H`](../src/app-logic/FlowlineGeometryPopulator.md#free-functions-and-macros) | [app-logic/FlowlineGeometryPopulator](../src/app-logic/FlowlineGeometryPopulator.md) |
| [`GPLATES_APP_LOGIC_GENERICPARTITIONFEATURETASK_H`](../src/app-logic/GenericPartitionFeatureTask.md#free-functions-and-macros) | [app-logic/GenericPartitionFeatureTask](../src/app-logic/GenericPartitionFeatureTask.md) |
| [`GPLATES_APP_LOGIC_GEOMETRY_UTILS_H`](../src/app-logic/GeometryUtils.md#free-functions-and-macros) | [app-logic/GeometryUtils](../src/app-logic/GeometryUtils.md) |
| [`GPLATES_APP_LOGIC_GEOMETRYCOOKIECUTTER_H`](../src/app-logic/GeometryCookieCutter.md#free-functions-and-macros) | [app-logic/GeometryCookieCutter](../src/app-logic/GeometryCookieCutter.md) |
| [`GPLATES_APP_LOGIC_GPLATESQTMSGHANDLER_H`](../src/app-logic/GPlatesQtMsgHandler.md#free-functions-and-macros) | [app-logic/GPlatesQtMsgHandler](../src/app-logic/GPlatesQtMsgHandler.md) |
| [`GPLATES_APP_LOGIC_LAYER_H`](../src/app-logic/Layer.md#free-functions-and-macros) | [app-logic/Layer](../src/app-logic/Layer.md) |
| [`GPLATES_APP_LOGIC_LAYERCONNECTIONTYPE_H`](../src/app-logic/LayerInputChannelType.md#free-functions-and-macros) | [app-logic/LayerInputChannelType](../src/app-logic/LayerInputChannelType.md) |
| [`GPLATES_APP_LOGIC_LAYERINPUTCHANNELNAME_H`](../src/app-logic/LayerInputChannelName.md#free-functions-and-macros) | [app-logic/LayerInputChannelName](../src/app-logic/LayerInputChannelName.md) |
| [`GPLATES_APP_LOGIC_LAYERPARAMS_H`](../src/app-logic/LayerParams.md#free-functions-and-macros) | [app-logic/LayerParams](../src/app-logic/LayerParams.md) |
| [`GPLATES_APP_LOGIC_LAYERPARAMSVISITOR_H`](../src/app-logic/LayerParamsVisitor.md#free-functions-and-macros) | [app-logic/LayerParamsVisitor](../src/app-logic/LayerParamsVisitor.md) |
| [`GPLATES_APP_LOGIC_LAYERPROXY_H`](../src/app-logic/LayerProxy.md#free-functions-and-macros) | [app-logic/LayerProxy](../src/app-logic/LayerProxy.md) |
| [`GPLATES_APP_LOGIC_LAYERPROXYUTILS_H`](../src/app-logic/LayerProxyUtils.md#free-functions-and-macros) | [app-logic/LayerProxyUtils](../src/app-logic/LayerProxyUtils.md) |
| [`GPLATES_APP_LOGIC_LAYERPROXYVISITOR_H`](../src/app-logic/LayerProxyVisitor.md#free-functions-and-macros) | [app-logic/LayerProxyVisitor](../src/app-logic/LayerProxyVisitor.md) |
| [`GPLATES_APP_LOGIC_LAYERTASK_H`](../src/app-logic/LayerTask.md#free-functions-and-macros) | [app-logic/LayerTask](../src/app-logic/LayerTask.md) |
| [`GPLATES_APP_LOGIC_LAYERTASKREGISTRY_H`](../src/app-logic/LayerTaskRegistry.md#free-functions-and-macros) | [app-logic/LayerTaskRegistry](../src/app-logic/LayerTaskRegistry.md) |
| [`GPLATES_APP_LOGIC_LAYERTASKTYPE_H`](../src/app-logic/LayerTaskType.md#free-functions-and-macros) | [app-logic/LayerTaskType](../src/app-logic/LayerTaskType.md) |
| [`GPLATES_APP_LOGIC_LOGMODEL_H`](../src/app-logic/LogModel.md#free-functions-and-macros) | [app-logic/LogModel](../src/app-logic/LogModel.md) |
| [`GPLATES_APP_LOGIC_LOGTOMODELHANDLER_H`](../src/app-logic/LogToModelHandler.md#free-functions-and-macros) | [app-logic/LogToModelHandler](../src/app-logic/LogToModelHandler.md) |
| [`GPLATES_APP_LOGIC_MOTIONPATHGEOMETRYPOPULATOR_H`](../src/app-logic/MotionPathGeometryPopulator.md#free-functions-and-macros) | [app-logic/MotionPathGeometryPopulator](../src/app-logic/MotionPathGeometryPopulator.md) |
| [`GPLATES_APP_LOGIC_MULTIPOINTVECTORFIELD_H`](../src/app-logic/MultiPointVectorField.md#free-functions-and-macros) | [app-logic/MultiPointVectorField](../src/app-logic/MultiPointVectorField.md) |
| [`GPLATES_APP_LOGIC_NETROTATIONUTILS_H`](../src/app-logic/NetRotationUtils.md#free-functions-and-macros) | [app-logic/NetRotationUtils](../src/app-logic/NetRotationUtils.md) |
| [`GPLATES_APP_LOGIC_PALAEOMAGUTILS_H`](../src/app-logic/PalaeomagUtils.md#free-functions-and-macros) | [app-logic/PalaeomagUtils](../src/app-logic/PalaeomagUtils.md) |
| [`GPLATES_APP_LOGIC_PALEOMAGUTILS_H`](../src/app-logic/deprecated/PaleomagUtils.md#free-functions-and-macros) | [app-logic/deprecated/PaleomagUtils](../src/app-logic/deprecated/PaleomagUtils.md) |
| [`GPLATES_APP_LOGIC_PALEOMAGWORKFLOW_H`](../src/app-logic/deprecated/PaleomagWorkflow.md#free-functions-and-macros) | [app-logic/deprecated/PaleomagWorkflow](../src/app-logic/deprecated/PaleomagWorkflow.md) |
| [`GPLATES_APP_LOGIC_PARTITIONFEATURETASK_H`](../src/app-logic/PartitionFeatureTask.md#free-functions-and-macros) | [app-logic/PartitionFeatureTask](../src/app-logic/PartitionFeatureTask.md) |
| [`GPLATES_APP_LOGIC_PARTITIONFEATUREUTILS_H`](../src/app-logic/PartitionFeatureUtils.md#free-functions-and-macros) | [app-logic/PartitionFeatureUtils](../src/app-logic/PartitionFeatureUtils.md) |
| [`GPLATES_APP_LOGIC_PLATEVELOCITYUTILS_H`](../src/app-logic/PlateVelocityUtils.md#free-functions-and-macros) | [app-logic/PlateVelocityUtils](../src/app-logic/PlateVelocityUtils.md) |
| [`GPLATES_APP_LOGIC_PLATEVELOCITYWORKFLOW_H`](../src/app-logic/deprecated/PlateVelocityWorkflow.md#free-functions-and-macros) | [app-logic/deprecated/PlateVelocityWorkflow](../src/app-logic/deprecated/PlateVelocityWorkflow.md) |
| [`GPLATES_APP_LOGIC_PROPERTYEXTRACTORS_H`](../src/app-logic/PropertyExtractors.md#free-functions-and-macros) | [app-logic/PropertyExtractors](../src/app-logic/PropertyExtractors.md) |
| [`GPLATES_APP_LOGIC_PROPERTYVALUEPROPOGATOR_H`](../src/app-logic/deprecated/PropertyValuePropogator.md#free-functions-and-macros) | [app-logic/deprecated/PropertyValuePropogator](../src/app-logic/deprecated/PropertyValuePropogator.md) |
| [`GPLATES_APP_LOGIC_RASTERLAYERPARAMS_H`](../src/app-logic/RasterLayerParams.md#free-functions-and-macros) | [app-logic/RasterLayerParams](../src/app-logic/RasterLayerParams.md) |
| [`GPLATES_APP_LOGIC_RASTERLAYERPROXY_H`](../src/app-logic/RasterLayerProxy.md#free-functions-and-macros) | [app-logic/RasterLayerProxy](../src/app-logic/RasterLayerProxy.md) |
| [`GPLATES_APP_LOGIC_RASTERLAYERTASK_H`](../src/app-logic/RasterLayerTask.md#free-functions-and-macros) | [app-logic/RasterLayerTask](../src/app-logic/RasterLayerTask.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTCONTEXT_H`](../src/app-logic/ReconstructContext.md#free-functions-and-macros) | [app-logic/ReconstructContext](../src/app-logic/ReconstructContext.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTEDFEATUREGEOMETRY_H`](../src/app-logic/ReconstructedFeatureGeometry.md#free-functions-and-macros) | [app-logic/ReconstructedFeatureGeometry](../src/app-logic/ReconstructedFeatureGeometry.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTEDFEATUREGEOMETRYFINDER_H`](../src/app-logic/ReconstructedFeatureGeometryFinder.md#free-functions-and-macros) | [app-logic/ReconstructedFeatureGeometryFinder](../src/app-logic/ReconstructedFeatureGeometryFinder.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTEDFLOWLINE_H`](../src/app-logic/ReconstructedFlowline.md#free-functions-and-macros) | [app-logic/ReconstructedFlowline](../src/app-logic/ReconstructedFlowline.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTEDMOTIONPATH_H`](../src/app-logic/ReconstructedMotionPath.md#free-functions-and-macros) | [app-logic/ReconstructedMotionPath](../src/app-logic/ReconstructedMotionPath.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTEDSCALARCOVERAGE_H`](../src/app-logic/ReconstructedScalarCoverage.md#free-functions-and-macros) | [app-logic/ReconstructedScalarCoverage](../src/app-logic/ReconstructedScalarCoverage.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTEDSMALLCIRCLE_H`](../src/app-logic/ReconstructedSmallCircle.md#free-functions-and-macros) | [app-logic/ReconstructedSmallCircle](../src/app-logic/ReconstructedSmallCircle.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTEDVIRTUALGEOMAGNETICPOLE_H`](../src/app-logic/ReconstructedVirtualGeomagneticPole.md#free-functions-and-macros) | [app-logic/ReconstructedVirtualGeomagneticPole](../src/app-logic/ReconstructedVirtualGeomagneticPole.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTGRAPH_H`](../src/app-logic/ReconstructGraph.md#free-functions-and-macros) | [app-logic/ReconstructGraph](../src/app-logic/ReconstructGraph.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTGRAPHIMPL_H`](../src/app-logic/ReconstructGraphImpl.md#free-functions-and-macros) | [app-logic/ReconstructGraphImpl](../src/app-logic/ReconstructGraphImpl.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTHANDLE_H`](../src/app-logic/ReconstructHandle.md#free-functions-and-macros) | [app-logic/ReconstructHandle](../src/app-logic/ReconstructHandle.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTION_H`](../src/app-logic/Reconstruction.md#free-functions-and-macros) | [app-logic/Reconstruction](../src/app-logic/Reconstruction.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONFEATUREPROPERTIES_H`](../src/app-logic/ReconstructionFeatureProperties.md#free-functions-and-macros) | [app-logic/ReconstructionFeatureProperties](../src/app-logic/ReconstructionFeatureProperties.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONGEOMETRY_H`](../src/app-logic/ReconstructionGeometry.md#free-functions-and-macros) | [app-logic/ReconstructionGeometry](../src/app-logic/ReconstructionGeometry.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONGEOMETRYFINDER_H`](../src/app-logic/ReconstructionGeometryFinder.md#free-functions-and-macros) | [app-logic/ReconstructionGeometryFinder](../src/app-logic/ReconstructionGeometryFinder.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONGEOMETRYVISITOR_H`](../src/app-logic/ReconstructionGeometryVisitor.md#free-functions-and-macros) | [app-logic/ReconstructionGeometryVisitor](../src/app-logic/ReconstructionGeometryVisitor.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONGRAPH_H`](../src/app-logic/ReconstructionGraph.md#free-functions-and-macros) | [app-logic/ReconstructionGraph](../src/app-logic/ReconstructionGraph.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONGRAPHBUILDER_H`](../src/app-logic/ReconstructionGraphBuilder.md#free-functions-and-macros) | [app-logic/ReconstructionGraphBuilder](../src/app-logic/ReconstructionGraphBuilder.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONLAYER_H`](../src/app-logic/ReconstructionLayerTask.md#free-functions-and-macros) | [app-logic/ReconstructionLayerTask](../src/app-logic/ReconstructionLayerTask.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONLAYERPARAMS_H`](../src/app-logic/ReconstructionLayerParams.md#free-functions-and-macros) | [app-logic/ReconstructionLayerParams](../src/app-logic/ReconstructionLayerParams.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONLAYERPROXY_H`](../src/app-logic/ReconstructionLayerProxy.md#free-functions-and-macros) | [app-logic/ReconstructionLayerProxy](../src/app-logic/ReconstructionLayerProxy.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONPARAMS_H`](../src/app-logic/ReconstructionParams.md#free-functions-and-macros) | [app-logic/ReconstructionParams](../src/app-logic/ReconstructionParams.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONTREE_H`](../src/app-logic/ReconstructionTree.md#free-functions-and-macros) | [app-logic/ReconstructionTree](../src/app-logic/ReconstructionTree.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONTREECREATOR_H`](../src/app-logic/ReconstructionTreeCreator.md#free-functions-and-macros) | [app-logic/ReconstructionTreeCreator](../src/app-logic/ReconstructionTreeCreator.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTIONTREEPOPULATOR_H`](../src/app-logic/ReconstructionGraphPopulator.md#free-functions-and-macros) | [app-logic/ReconstructionGraphPopulator](../src/app-logic/ReconstructionGraphPopulator.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTLAYERPARAMS_H`](../src/app-logic/ReconstructLayerParams.md#free-functions-and-macros) | [app-logic/ReconstructLayerParams](../src/app-logic/ReconstructLayerParams.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTLAYERPROXY_H`](../src/app-logic/ReconstructLayerProxy.md#free-functions-and-macros) | [app-logic/ReconstructLayerProxy](../src/app-logic/ReconstructLayerProxy.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTLAYERTASK_H`](../src/app-logic/ReconstructLayerTask.md#free-functions-and-macros) | [app-logic/ReconstructLayerTask](../src/app-logic/ReconstructLayerTask.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODBYPLATEID_H`](../src/app-logic/ReconstructMethodByPlateId.md#free-functions-and-macros) | [app-logic/ReconstructMethodByPlateId](../src/app-logic/ReconstructMethodByPlateId.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODFINITEROTATION_H`](../src/app-logic/ReconstructMethodFiniteRotation.md#free-functions-and-macros) | [app-logic/ReconstructMethodFiniteRotation](../src/app-logic/ReconstructMethodFiniteRotation.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODFLOWLINE_H`](../src/app-logic/ReconstructMethodFlowline.md#free-functions-and-macros) | [app-logic/ReconstructMethodFlowline](../src/app-logic/ReconstructMethodFlowline.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODHALFSTAGEROTATION_H`](../src/app-logic/ReconstructMethodHalfStageRotation.md#free-functions-and-macros) | [app-logic/ReconstructMethodHalfStageRotation](../src/app-logic/ReconstructMethodHalfStageRotation.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODINTERFACE_H`](../src/app-logic/ReconstructMethodInterface.md#free-functions-and-macros) | [app-logic/ReconstructMethodInterface](../src/app-logic/ReconstructMethodInterface.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODMOTIONPATH_H`](../src/app-logic/ReconstructMethodMotionPath.md#free-functions-and-macros) | [app-logic/ReconstructMethodMotionPath](../src/app-logic/ReconstructMethodMotionPath.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODREGISTRY_H`](../src/app-logic/ReconstructMethodRegistry.md#free-functions-and-macros) | [app-logic/ReconstructMethodRegistry](../src/app-logic/ReconstructMethodRegistry.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODSMALLCIRCLE_H`](../src/app-logic/ReconstructMethodSmallCircle.md#free-functions-and-macros) | [app-logic/ReconstructMethodSmallCircle](../src/app-logic/ReconstructMethodSmallCircle.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODTYPE_H`](../src/app-logic/ReconstructMethodType.md#free-functions-and-macros) | [app-logic/ReconstructMethodType](../src/app-logic/ReconstructMethodType.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTMETHODVIRTUALGEOMAGNETICPOLE_H`](../src/app-logic/ReconstructMethodVirtualGeomagneticPole.md#free-functions-and-macros) | [app-logic/ReconstructMethodVirtualGeomagneticPole](../src/app-logic/ReconstructMethodVirtualGeomagneticPole.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTPARAMS_H`](../src/app-logic/ReconstructParams.md#free-functions-and-macros) | [app-logic/ReconstructParams](../src/app-logic/ReconstructParams.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTSCALARCOVERAGELAYERPARAMS_H`](../src/app-logic/ReconstructScalarCoverageLayerParams.md#free-functions-and-macros) | [app-logic/ReconstructScalarCoverageLayerParams](../src/app-logic/ReconstructScalarCoverageLayerParams.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTSCALARCOVERAGELAYERPROXY_H`](../src/app-logic/ReconstructScalarCoverageLayerProxy.md#free-functions-and-macros) | [app-logic/ReconstructScalarCoverageLayerProxy](../src/app-logic/ReconstructScalarCoverageLayerProxy.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTSCALARCOVERAGELAYERTASK_H`](../src/app-logic/ReconstructScalarCoverageLayerTask.md#free-functions-and-macros) | [app-logic/ReconstructScalarCoverageLayerTask](../src/app-logic/ReconstructScalarCoverageLayerTask.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTSCALARCOVERAGEPARAMS_H`](../src/app-logic/ReconstructScalarCoverageParams.md#free-functions-and-macros) | [app-logic/ReconstructScalarCoverageParams](../src/app-logic/ReconstructScalarCoverageParams.md) |
| [`GPLATES_APP_LOGIC_RECONSTRUCTUTILS_H`](../src/app-logic/ReconstructUtils.md#free-functions-and-macros) | [app-logic/ReconstructUtils](../src/app-logic/ReconstructUtils.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDRASTER_H`](../src/app-logic/ResolvedRaster.md#free-functions-and-macros) | [app-logic/ResolvedRaster](../src/app-logic/ResolvedRaster.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDSCALARFIELD3D_H`](../src/app-logic/ResolvedScalarField3D.md#free-functions-and-macros) | [app-logic/ResolvedScalarField3D](../src/app-logic/ResolvedScalarField3D.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDSUBSEGMENTRANGEINSECTION_H`](../src/app-logic/ResolvedSubSegmentRangeInSection.md#free-functions-and-macros) | [app-logic/ResolvedSubSegmentRangeInSection](../src/app-logic/ResolvedSubSegmentRangeInSection.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALBOUNDARY_H`](../src/app-logic/ResolvedTopologicalBoundary.md#free-functions-and-macros) | [app-logic/ResolvedTopologicalBoundary](../src/app-logic/ResolvedTopologicalBoundary.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALGEOMETRY_H`](../src/app-logic/ResolvedTopologicalGeometry.md#free-functions-and-macros) | [app-logic/ResolvedTopologicalGeometry](../src/app-logic/ResolvedTopologicalGeometry.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALGEOMETRYSUBSEGMENT_H`](../src/app-logic/ResolvedTopologicalGeometrySubSegment.md#free-functions-and-macros) | [app-logic/ResolvedTopologicalGeometrySubSegment](../src/app-logic/ResolvedTopologicalGeometrySubSegment.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALLINE_H`](../src/app-logic/ResolvedTopologicalLine.md#free-functions-and-macros) | [app-logic/ResolvedTopologicalLine](../src/app-logic/ResolvedTopologicalLine.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALNETWORK_H`](../src/app-logic/ResolvedTopologicalNetwork.md#free-functions-and-macros) | [app-logic/ResolvedTopologicalNetwork](../src/app-logic/ResolvedTopologicalNetwork.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALSECTION_H`](../src/app-logic/ResolvedTopologicalSection.md#free-functions-and-macros) | [app-logic/ResolvedTopologicalSection](../src/app-logic/ResolvedTopologicalSection.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALSHAREDSUBSEGMENT_H`](../src/app-logic/ResolvedTopologicalSharedSubSegment.md#free-functions-and-macros) | [app-logic/ResolvedTopologicalSharedSubSegment](../src/app-logic/ResolvedTopologicalSharedSubSegment.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTOPOLOGICALSUBSEGMENTIMPL_H`](../src/app-logic/ResolvedTopologicalSubSegmentImpl.md#free-functions-and-macros) | [app-logic/ResolvedTopologicalSubSegmentImpl](../src/app-logic/ResolvedTopologicalSubSegmentImpl.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTRIANGULATIONDELAUNAY2_H`](../src/app-logic/ResolvedTriangulationDelaunay2.md#free-functions-and-macros) | [app-logic/ResolvedTriangulationDelaunay2](../src/app-logic/ResolvedTriangulationDelaunay2.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTRIANGULATIONNETWORK_H`](../src/app-logic/ResolvedTriangulationNetwork.md#free-functions-and-macros) | [app-logic/ResolvedTriangulationNetwork](../src/app-logic/ResolvedTriangulationNetwork.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDTRIANGULATIONUTILS_H`](../src/app-logic/ResolvedTriangulationUtils.md#free-functions-and-macros) | [app-logic/ResolvedTriangulationUtils](../src/app-logic/ResolvedTriangulationUtils.md) |
| [`GPLATES_APP_LOGIC_RESOLVEDVERTEXSOURCEINFO_H`](../src/app-logic/ResolvedVertexSourceInfo.md#free-functions-and-macros) | [app-logic/ResolvedVertexSourceInfo](../src/app-logic/ResolvedVertexSourceInfo.md) |
| [`GPLATES_APP_LOGIC_ROTATIONUTILS_H`](../src/app-logic/RotationUtils.md#free-functions-and-macros) | [app-logic/RotationUtils](../src/app-logic/RotationUtils.md) |
| [`GPLATES_APP_LOGIC_SCALARCOVERAGEEVOLUTION_H`](../src/app-logic/ScalarCoverageEvolution.md#free-functions-and-macros) | [app-logic/ScalarCoverageEvolution](../src/app-logic/ScalarCoverageEvolution.md) |
| [`GPLATES_APP_LOGIC_SCALARCOVERAGEFEATUREPROPERTIES_H`](../src/app-logic/ScalarCoverageFeatureProperties.md#free-functions-and-macros) | [app-logic/ScalarCoverageFeatureProperties](../src/app-logic/ScalarCoverageFeatureProperties.md) |
| [`GPLATES_APP_LOGIC_SCALARCOVERAGETIMESPAN_H`](../src/app-logic/ScalarCoverageTimeSpan.md#free-functions-and-macros) | [app-logic/ScalarCoverageTimeSpan](../src/app-logic/ScalarCoverageTimeSpan.md) |
| [`GPLATES_APP_LOGIC_SCALARFIELD3DLAYERPARAMS_H`](../src/app-logic/ScalarField3DLayerParams.md#free-functions-and-macros) | [app-logic/ScalarField3DLayerParams](../src/app-logic/ScalarField3DLayerParams.md) |
| [`GPLATES_APP_LOGIC_SCALARFIELD3DLAYERPROXY_H`](../src/app-logic/ScalarField3DLayerProxy.md#free-functions-and-macros) | [app-logic/ScalarField3DLayerProxy](../src/app-logic/ScalarField3DLayerProxy.md) |
| [`GPLATES_APP_LOGIC_SCALARFIELD3DLAYERTASK_H`](../src/app-logic/ScalarField3DLayerTask.md#free-functions-and-macros) | [app-logic/ScalarField3DLayerTask](../src/app-logic/ScalarField3DLayerTask.md) |
| [`GPLATES_APP_LOGIC_SMALLCIRCLEGEOMETRYPOPULATOR_H`](../src/app-logic/SmallCircleGeometryPopulator.md#free-functions-and-macros) | [app-logic/SmallCircleGeometryPopulator](../src/app-logic/SmallCircleGeometryPopulator.md) |
| [`GPLATES_APP_LOGIC_TIMESPANUTILS_H`](../src/app-logic/TimeSpanUtils.md#free-functions-and-macros) | [app-logic/TimeSpanUtils](../src/app-logic/TimeSpanUtils.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGY_GEOMETRY_RESOLVER_H`](../src/app-logic/TopologyGeometryResolver.md#free-functions-and-macros) | [app-logic/TopologyGeometryResolver](../src/app-logic/TopologyGeometryResolver.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGY_NETWORK_RESOLVER_H`](../src/app-logic/TopologyNetworkResolver.md#free-functions-and-macros) | [app-logic/TopologyNetworkResolver](../src/app-logic/TopologyNetworkResolver.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYBOUNDARYRESOLVERLAYERTASK_H`](../src/app-logic/TopologyNetworkResolverLayerTask.md#free-functions-and-macros) | [app-logic/TopologyNetworkResolverLayerTask](../src/app-logic/TopologyNetworkResolverLayerTask.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYGEOMETRYRESOLVERLAYERPROXY_H`](../src/app-logic/TopologyGeometryResolverLayerProxy.md#free-functions-and-macros) | [app-logic/TopologyGeometryResolverLayerProxy](../src/app-logic/TopologyGeometryResolverLayerProxy.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYGEOMETRYRESOLVERLAYERTASK_H`](../src/app-logic/TopologyGeometryResolverLayerTask.md#free-functions-and-macros) | [app-logic/TopologyGeometryResolverLayerTask](../src/app-logic/TopologyGeometryResolverLayerTask.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYGEOMETRYTYPE_H`](../src/app-logic/TopologyGeometryType.md#free-functions-and-macros) | [app-logic/TopologyGeometryType](../src/app-logic/TopologyGeometryType.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYINTERNALUTILS_H`](../src/app-logic/TopologyInternalUtils.md#free-functions-and-macros) | [app-logic/TopologyInternalUtils](../src/app-logic/TopologyInternalUtils.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYINTERSECTIONS_H`](../src/app-logic/TopologyIntersections.md#free-functions-and-macros) | [app-logic/TopologyIntersections](../src/app-logic/TopologyIntersections.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYNETWORKLAYERPARAMS_H`](../src/app-logic/TopologyNetworkLayerParams.md#free-functions-and-macros) | [app-logic/TopologyNetworkLayerParams](../src/app-logic/TopologyNetworkLayerParams.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYNETWORKPARAMS_H`](../src/app-logic/TopologyNetworkParams.md#free-functions-and-macros) | [app-logic/TopologyNetworkParams](../src/app-logic/TopologyNetworkParams.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYNETWORKRESOLVERLAYERPROXY_H`](../src/app-logic/TopologyNetworkResolverLayerProxy.md#free-functions-and-macros) | [app-logic/TopologyNetworkResolverLayerProxy](../src/app-logic/TopologyNetworkResolverLayerProxy.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYNETWORKRESOLVERLAYERTASK_H`](../src/app-logic/TopologyNetworkResolverLayerTask.md#free-functions-and-macros) | [app-logic/TopologyNetworkResolverLayerTask](../src/app-logic/TopologyNetworkResolverLayerTask.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYPOINTLOCATION_H`](../src/app-logic/TopologyPointLocation.md#free-functions-and-macros) | [app-logic/TopologyPointLocation](../src/app-logic/TopologyPointLocation.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYRECONSTRUCT_H`](../src/app-logic/TopologyReconstruct.md#free-functions-and-macros) | [app-logic/TopologyReconstruct](../src/app-logic/TopologyReconstruct.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYRECONSTRUCTEDFEATUREGEOMETRY_H`](../src/app-logic/TopologyReconstructedFeatureGeometry.md#free-functions-and-macros) | [app-logic/TopologyReconstructedFeatureGeometry](../src/app-logic/TopologyReconstructedFeatureGeometry.md) |
| [`GPLATES_APP_LOGIC_TOPOLOGYUTILS_H`](../src/app-logic/TopologyUtils.md#free-functions-and-macros) | [app-logic/TopologyUtils](../src/app-logic/TopologyUtils.md) |
| [`GPLATES_APP_LOGIC_USERPREFERENCES_H`](../src/app-logic/UserPreferences.md#free-functions-and-macros) | [app-logic/UserPreferences](../src/app-logic/UserPreferences.md) |
| [`GPLATES_APP_LOGIC_VELOCITYDELTATIME_H`](../src/app-logic/VelocityDeltaTime.md#free-functions-and-macros) | [app-logic/VelocityDeltaTime](../src/app-logic/VelocityDeltaTime.md) |
| [`GPLATES_APP_LOGIC_VELOCITYFIELDCALCULATORLAYERPARAMS_H`](../src/app-logic/VelocityFieldCalculatorLayerParams.md#free-functions-and-macros) | [app-logic/VelocityFieldCalculatorLayerParams](../src/app-logic/VelocityFieldCalculatorLayerParams.md) |
| [`GPLATES_APP_LOGIC_VELOCITYFIELDCALCULATORLAYERPROXY_H`](../src/app-logic/VelocityFieldCalculatorLayerProxy.md#free-functions-and-macros) | [app-logic/VelocityFieldCalculatorLayerProxy](../src/app-logic/VelocityFieldCalculatorLayerProxy.md) |
| [`GPLATES_APP_LOGIC_VELOCITYFIELDCALCULATORLAYERTASK_H`](../src/app-logic/VelocityFieldCalculatorLayerTask.md#free-functions-and-macros) | [app-logic/VelocityFieldCalculatorLayerTask](../src/app-logic/VelocityFieldCalculatorLayerTask.md) |
| [`GPLATES_APP_LOGIC_VELOCITYPARAMS_H`](../src/app-logic/VelocityParams.md#free-functions-and-macros) | [app-logic/VelocityParams](../src/app-logic/VelocityParams.md) |
| [`GPLATES_APP_LOGIC_VGPPARTITIONFEATURETASK_H`](../src/app-logic/VgpPartitionFeatureTask.md#free-functions-and-macros) | [app-logic/VgpPartitionFeatureTask](../src/app-logic/VgpPartitionFeatureTask.md) |
| [`GPLATES_APPLOGIC_FLOWLINEUTILS_H`](../src/app-logic/FlowlineUtils.md#free-functions-and-macros) | [app-logic/FlowlineUtils](../src/app-logic/FlowlineUtils.md) |
| [`GPLATES_APPLOGIC_MOTIONPATHUTILS_H`](../src/app-logic/MotionPathUtils.md#free-functions-and-macros) | [app-logic/MotionPathUtils](../src/app-logic/MotionPathUtils.md) |
| [`GPLATES_APPLOGIC_RECONSTRUCTIONGEOMETRYUTILS_H`](../src/app-logic/ReconstructionGeometryUtils.md#free-functions-and-macros) | [app-logic/ReconstructionGeometryUtils](../src/app-logic/ReconstructionGeometryUtils.md) |
| [`GPLATES_CANVAS_TOOLS_CHANGELIGHTINGGLOBE_H`](../src/canvas-tools/ChangeLightDirectionGlobe.md#free-functions-and-macros) | [canvas-tools/ChangeLightDirectionGlobe](../src/canvas-tools/ChangeLightDirectionGlobe.md) |
| [`GPLATES_CANVAS_TOOLS_CHANGELIGHTINGMAP_H`](../src/canvas-tools/ChangeLightDirectionMap.md#free-functions-and-macros) | [canvas-tools/ChangeLightDirectionMap](../src/canvas-tools/ChangeLightDirectionMap.md) |
| [`GPLATES_CANVAS_TOOLS_MOVEPOLEGLOBE_H`](../src/canvas-tools/MovePoleGlobe.md#free-functions-and-macros) | [canvas-tools/MovePoleGlobe](../src/canvas-tools/MovePoleGlobe.md) |
| [`GPLATES_CANVAS_TOOLS_MOVEPOLEMAP_H`](../src/canvas-tools/MovePoleMap.md#free-functions-and-macros) | [canvas-tools/MovePoleMap](../src/canvas-tools/MovePoleMap.md) |
| [`GPLATES_CANVASTOOLS_ADJUSTFITTEDPOLEESTIMATE_H`](../src/canvas-tools/AdjustFittedPoleEstimate.md#free-functions-and-macros) | [canvas-tools/AdjustFittedPoleEstimate](../src/canvas-tools/AdjustFittedPoleEstimate.md) |
| [`GPLATES_CANVASTOOLS_BUILD_TOPOLOGY_H`](../src/canvas-tools/BuildTopology.md#free-functions-and-macros) | [canvas-tools/BuildTopology](../src/canvas-tools/BuildTopology.md) |
| [`GPLATES_CANVASTOOLS_CANVASTOOL_H`](../src/canvas-tools/CanvasTool.md#free-functions-and-macros) | [canvas-tools/CanvasTool](../src/canvas-tools/CanvasTool.md) |
| [`GPLATES_CANVASTOOLS_CANVASTOOLADAPTERFORGLOBE_H`](../src/canvas-tools/CanvasToolAdapterForGlobe.md#free-functions-and-macros) | [canvas-tools/CanvasToolAdapterForGlobe](../src/canvas-tools/CanvasToolAdapterForGlobe.md) |
| [`GPLATES_CANVASTOOLS_CANVASTOOLADAPTERFORMAP_H`](../src/canvas-tools/CanvasToolAdapterForMap.md#free-functions-and-macros) | [canvas-tools/CanvasToolAdapterForMap](../src/canvas-tools/CanvasToolAdapterForMap.md) |
| [`GPLATES_CANVASTOOLS_CLICKGEOMETRY_H`](../src/canvas-tools/ClickGeometry.md#free-functions-and-macros) | [canvas-tools/ClickGeometry](../src/canvas-tools/ClickGeometry.md) |
| [`GPLATES_CANVASTOOLS_CREATESMALLCIRCLE_H`](../src/canvas-tools/CreateSmallCircle.md#free-functions-and-macros) | [canvas-tools/CreateSmallCircle](../src/canvas-tools/CreateSmallCircle.md) |
| [`GPLATES_CANVASTOOLS_DELETEVERTEX_H`](../src/canvas-tools/DeleteVertex.md#free-functions-and-macros) | [canvas-tools/DeleteVertex](../src/canvas-tools/DeleteVertex.md) |
| [`GPLATES_CANVASTOOLS_DIGITISATIONCANVASTOOLWORKFLOW_H`](../src/gui/DigitisationCanvasToolWorkflow.md#free-functions-and-macros) | [gui/DigitisationCanvasToolWorkflow](../src/gui/DigitisationCanvasToolWorkflow.md) |
| [`GPLATES_CANVASTOOLS_DIGITISEGEOMETRY_H`](../src/canvas-tools/DigitiseGeometry.md#free-functions-and-macros) | [canvas-tools/DigitiseGeometry](../src/canvas-tools/DigitiseGeometry.md) |
| [`GPLATES_CANVASTOOLS_EDIT_TOPOLOGY_H`](../src/canvas-tools/EditTopology.md#free-functions-and-macros) | [canvas-tools/EditTopology](../src/canvas-tools/EditTopology.md) |
| [`GPLATES_CANVASTOOLS_GEOMETRYOPERATIONSTATE_H`](../src/canvas-tools/GeometryOperationState.md#free-functions-and-macros) | [canvas-tools/GeometryOperationState](../src/canvas-tools/GeometryOperationState.md) |
| [`GPLATES_CANVASTOOLS_INSERTVERTEX_H`](../src/canvas-tools/InsertVertex.md#free-functions-and-macros) | [canvas-tools/InsertVertex](../src/canvas-tools/InsertVertex.md) |
| [`GPLATES_CANVASTOOLS_MANIPULATEPOLE_H`](../src/canvas-tools/ManipulatePole.md#free-functions-and-macros) | [canvas-tools/ManipulatePole](../src/canvas-tools/ManipulatePole.md) |
| [`GPLATES_CANVASTOOLS_MEASUREDISTANCE_H`](../src/canvas-tools/MeasureDistance.md#free-functions-and-macros) | [canvas-tools/MeasureDistance](../src/canvas-tools/MeasureDistance.md) |
| [`GPLATES_CANVASTOOLS_MEASUREDISTANCESTATE_H`](../src/canvas-tools/MeasureDistanceState.md#free-functions-and-macros) | [canvas-tools/MeasureDistanceState](../src/canvas-tools/MeasureDistanceState.md) |
| [`GPLATES_CANVASTOOLS_MODIFYGEOMETRYSTATE_H`](../src/canvas-tools/ModifyGeometryState.md#free-functions-and-macros) | [canvas-tools/ModifyGeometryState](../src/canvas-tools/ModifyGeometryState.md) |
| [`GPLATES_CANVASTOOLS_MOVEVERTEX_H`](../src/canvas-tools/MoveVertex.md#free-functions-and-macros) | [canvas-tools/MoveVertex](../src/canvas-tools/MoveVertex.md) |
| [`GPLATES_CANVASTOOLS_PANMAP_H`](../src/canvas-tools/PanMap.md#free-functions-and-macros) | [canvas-tools/PanMap](../src/canvas-tools/PanMap.md) |
| [`GPLATES_CANVASTOOLS_REORIENTGLOBE_H`](../src/canvas-tools/ReorientGlobe.md#free-functions-and-macros) | [canvas-tools/ReorientGlobe](../src/canvas-tools/ReorientGlobe.md) |
| [`GPLATES_CANVASTOOLS_SELECTHELLINGERGEOMETRIES_H`](../src/canvas-tools/SelectHellingerGeometries.md#free-functions-and-macros) | [canvas-tools/SelectHellingerGeometries](../src/canvas-tools/SelectHellingerGeometries.md) |
| [`GPLATES_CANVASTOOLS_SPLITFEATURE_H`](../src/canvas-tools/SplitFeature.md#free-functions-and-macros) | [canvas-tools/SplitFeature](../src/canvas-tools/SplitFeature.md) |
| [`GPLATES_CANVASTOOLS_ZOOMGLOBE_H`](../src/canvas-tools/ZoomGlobe.md#free-functions-and-macros) | [canvas-tools/ZoomGlobe](../src/canvas-tools/ZoomGlobe.md) |
| [`GPLATES_CANVASTOOLS_ZOOMMAP_H`](../src/canvas-tools/ZoomMap.md#free-functions-and-macros) | [canvas-tools/ZoomMap](../src/canvas-tools/ZoomMap.md) |
| [`GPLATES_CLI_CLICOMMANDREGISTRY_H`](../src/cli/CliCommandRegistry.md#free-functions-and-macros) | [cli/CliCommandRegistry](../src/cli/CliCommandRegistry.md) |
| [`GPLATES_CLI_CLICONVERTFILEFORMATCOMMAND_H`](../src/cli/CliConvertFileFormatCommand.md#free-functions-and-macros) | [cli/CliConvertFileFormatCommand](../src/cli/CliConvertFileFormatCommand.md) |
| [`GPLATES_CLI_CLIEQUIVALENTTOTALROTATION_H`](../src/cli/CliEquivalentTotalRotation.md#free-functions-and-macros) | [cli/CliEquivalentTotalRotation](../src/cli/CliEquivalentTotalRotation.md) |
| [`GPLATES_CLI_CLIINVALIDOPTIONVALUE_H`](../src/cli/CliInvalidOptionValue.md#free-functions-and-macros) | [cli/CliInvalidOptionValue](../src/cli/CliInvalidOptionValue.md) |
| [`GPLATES_CLI_CLILOADFEATURECOLLECTIONS_H`](../src/cli/CliFeatureCollectionFileIO.md#free-functions-and-macros) | [cli/CliFeatureCollectionFileIO](../src/cli/CliFeatureCollectionFileIO.md) |
| [`GPLATES_CLI_CLIRELATIVETOTALROTATION_H`](../src/cli/CliRelativeTotalRotation.md#free-functions-and-macros) | [cli/CliRelativeTotalRotation](../src/cli/CliRelativeTotalRotation.md) |
| [`GPLATES_CLI_CLIREQUIREDOPTIONNOTPRESENT_H`](../src/cli/CliRequiredOptionNotPresent.md#free-functions-and-macros) | [cli/CliRequiredOptionNotPresent](../src/cli/CliRequiredOptionNotPresent.md) |
| [`GPLATES_CLI_CLISTAGEROTATIONCOMMAND_H`](../src/cli/CliStageRotationCommand.md#free-functions-and-macros) | [cli/CliStageRotationCommand](../src/cli/CliStageRotationCommand.md) |
| [`GPLATES_DATA_MINING_SCRIBEEXPORTDATAMINING_H`](../src/data-mining/ScribeExportDataMining.md#free-functions-and-macros) | [data-mining/ScribeExportDataMining](../src/data-mining/ScribeExportDataMining.md) |
| [`GPLATES_FEATURE_VISITORS_GEOMETRYROTATOR_H`](../src/feature-visitors/GeometryRotator.md#free-functions-and-macros) | [feature-visitors/GeometryRotator](../src/feature-visitors/GeometryRotator.md) |
| [`GPLATES_FEATUREVISITORS_FEATURECLASSIFIER_H`](../src/feature-visitors/FeatureClassifier.md#free-functions-and-macros) | [feature-visitors/FeatureClassifier](../src/feature-visitors/FeatureClassifier.md) |
| [`GPLATES_FEATUREVISITORS_FROMQVARIANTCONVERTER_H`](../src/feature-visitors/FromQvariantConverter.md#free-functions-and-macros) | [feature-visitors/FromQvariantConverter](../src/feature-visitors/FromQvariantConverter.md) |
| [`GPLATES_FEATUREVISITORS_GEOMETRYFINDER_H`](../src/feature-visitors/GeometryFinder.md#free-functions-and-macros) | [feature-visitors/GeometryFinder](../src/feature-visitors/GeometryFinder.md) |
| [`GPLATES_FEATUREVISITORS_GEOMETRYSETTER_H`](../src/feature-visitors/GeometrySetter.md#free-functions-and-macros) | [feature-visitors/GeometrySetter](../src/feature-visitors/GeometrySetter.md) |
| [`GPLATES_FEATUREVISITORS_GEOMETRYTYPEFINDER_H`](../src/feature-visitors/GeometryTypeFinder.md#free-functions-and-macros) | [feature-visitors/GeometryTypeFinder](../src/feature-visitors/GeometryTypeFinder.md) |
| [`GPLATES_FEATUREVISITORS_GMLTIMEPERIODFINDER_H`](../src/feature-visitors/deprecated/GmlTimePeriodFinder.md#free-functions-and-macros) | [feature-visitors/deprecated/GmlTimePeriodFinder](../src/feature-visitors/deprecated/GmlTimePeriodFinder.md) |
| [`GPLATES_FEATUREVISITORS_KEYVALUEDICTIONARYFINDER_H`](../src/feature-visitors/KeyValueDictionaryFinder.md#free-functions-and-macros) | [feature-visitors/KeyValueDictionaryFinder](../src/feature-visitors/KeyValueDictionaryFinder.md) |
| [`GPLATES_FEATUREVISITORS_PLATEIDFINDER_H`](../src/feature-visitors/deprecated/PlateIdFinder.md#free-functions-and-macros) | [feature-visitors/deprecated/PlateIdFinder](../src/feature-visitors/deprecated/PlateIdFinder.md) |
| [`GPLATES_FEATUREVISITORS_POPULATESHAPEFILEATTRIBUTESVISITOR_H`](../src/data-mining/PopulateShapeFileAttributesVisitor.md#free-functions-and-macros) | [data-mining/PopulateShapeFileAttributesVisitor](../src/data-mining/PopulateShapeFileAttributesVisitor.md) |
| [`GPLATES_FEATUREVISITORS_PROPERTYVALUEFINDER_H`](../src/feature-visitors/PropertyValueFinder.md#free-functions-and-macros) | [feature-visitors/PropertyValueFinder](../src/feature-visitors/PropertyValueFinder.md) |
| [`GPLATES_FEATUREVISITORS_QUERYFEATUREPROPERTIESWIDGETPOPULATOR_H`](../src/feature-visitors/QueryFeaturePropertiesWidgetPopulator.md#free-functions-and-macros) | [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../src/feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) |
| [`GPLATES_FEATUREVISITORS_SHAPEFILEATTRIBUTEFINDER_H`](../src/feature-visitors/ShapefileAttributeFinder.md#free-functions-and-macros) | [feature-visitors/ShapefileAttributeFinder](../src/feature-visitors/ShapefileAttributeFinder.md) |
| [`GPLATES_FEATUREVISITORS_TOPOLOGY_SECTIONS_FINDER_H`](../src/feature-visitors/TopologySectionsFinder.md#free-functions-and-macros) | [feature-visitors/TopologySectionsFinder](../src/feature-visitors/TopologySectionsFinder.md) |
| [`GPLATES_FEATUREVISITORS_TOQVARIANTCONVERTER_H`](../src/feature-visitors/ToQvariantConverter.md#free-functions-and-macros) | [feature-visitors/ToQvariantConverter](../src/feature-visitors/ToQvariantConverter.md) |
| [`GPLATES_FEATUREVISITORS_TOTALRECONSTRUCTIONSEQUENCEPLATEIDFINDER_H`](../src/feature-visitors/TotalReconstructionSequencePlateIdFinder.md#free-functions-and-macros) | [feature-visitors/TotalReconstructionSequencePlateIdFinder](../src/feature-visitors/TotalReconstructionSequencePlateIdFinder.md) |
| [`GPLATES_FEATUREVISITORS_TOTALRECONSTRUCTIONSEQUENCEROTATIONINSERTER_H`](../src/feature-visitors/TotalReconstructionSequenceRotationInserter.md#free-functions-and-macros) | [feature-visitors/TotalReconstructionSequenceRotationInserter](../src/feature-visitors/TotalReconstructionSequenceRotationInserter.md) |
| [`GPLATES_FEATUREVISITORS_TOTALRECONSTRUCTIONSEQUENCEROTATIONINTERPOLATER_H`](../src/feature-visitors/TotalReconstructionSequenceRotationInterpolater.md#free-functions-and-macros) | [feature-visitors/TotalReconstructionSequenceRotationInterpolater](../src/feature-visitors/TotalReconstructionSequenceRotationInterpolater.md) |
| [`GPLATES_FEATUREVISITORS_TOTALRECONSTRUCTIONSEQUENCETIMEPERIODFINDER_H`](../src/feature-visitors/TotalReconstructionSequenceTimePeriodFinder.md#free-functions-and-macros) | [feature-visitors/TotalReconstructionSequenceTimePeriodFinder](../src/feature-visitors/TotalReconstructionSequenceTimePeriodFinder.md) |
| [`GPLATES_FEATUREVISITORS_VIEWFEATUREGEOMETRIESWIDGETPOPULATOR_H`](../src/feature-visitors/ViewFeatureGeometriesWidgetPopulator.md#free-functions-and-macros) | [feature-visitors/ViewFeatureGeometriesWidgetPopulator](../src/feature-visitors/ViewFeatureGeometriesWidgetPopulator.md) |
| [`GPLATES_FEATUREVISITORS_XSSTRINGFINDER_H`](../src/feature-visitors/deprecated/XsStringFinder.md#free-functions-and-macros) | [feature-visitors/deprecated/XsStringFinder](../src/feature-visitors/deprecated/XsStringFinder.md) |
| [`GPLATES_FILE_IO_CITCOMSFORMATVELOCITYVECTORFIELDEXPORT_H`](../src/file-io/CitcomsFormatVelocityVectorFieldExport.md#free-functions-and-macros) | [file-io/CitcomsFormatVelocityVectorFieldExport](../src/file-io/CitcomsFormatVelocityVectorFieldExport.md) |
| [`GPLATES_FILE_IO_CITCOMSGMTFORMATRESOLVEDTOPOLOGICALBOUNDARYEXPORT_H`](../src/file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md#free-functions-and-macros) | [file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport](../src/file-io/CitcomsGMTFormatResolvedTopologicalBoundaryExport.md) |
| [`GPLATES_FILE_IO_CITCOMSRESOLVEDTOPOLOGICALBOUNDARYEXPORT_H`](../src/file-io/CitcomsResolvedTopologicalBoundaryExport.md#free-functions-and-macros) | [file-io/CitcomsResolvedTopologicalBoundaryExport](../src/file-io/CitcomsResolvedTopologicalBoundaryExport.md) |
| [`GPLATES_FILE_IO_CITCOMSRESOLVEDTOPOLOGICALBOUNDARYEXPORTIMPL_H`](../src/file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md#free-functions-and-macros) | [file-io/CitcomsResolvedTopologicalBoundaryExportImpl](../src/file-io/CitcomsResolvedTopologicalBoundaryExportImpl.md) |
| [`GPLATES_FILE_IO_DEFORMATIONEXPORT_H`](../src/file-io/DeformationExport.md#free-functions-and-macros) | [file-io/DeformationExport](../src/file-io/DeformationExport.md) |
| [`GPLATES_FILE_IO_ERRORWRITINGFEATURECOLLECTIONTOFILEFORMATEXCEPTION_H`](../src/file-io/ErrorWritingFeatureCollectionToFileFormatException.md#free-functions-and-macros) | [file-io/ErrorWritingFeatureCollectionToFileFormatException](../src/file-io/ErrorWritingFeatureCollectionToFileFormatException.md) |
| [`GPLATES_FILE_IO_EXPORTTEMPLATEFILENAMESEQUENCE_H`](../src/file-io/ExportTemplateFilenameSequence.md#free-functions-and-macros) | [file-io/ExportTemplateFilenameSequence](../src/file-io/ExportTemplateFilenameSequence.md) |
| [`GPLATES_FILE_IO_EXPORTTEMPLATEFILENAMESEQUENCEFORMATS_H`](../src/file-io/ExportTemplateFilenameSequenceFormats.md#free-functions-and-macros) | [file-io/ExportTemplateFilenameSequenceFormats](../src/file-io/ExportTemplateFilenameSequenceFormats.md) |
| [`GPLATES_FILE_IO_EXPORTTEMPLATEFILENAMESEQUENCEIMPL_H`](../src/file-io/ExportTemplateFilenameSequenceImpl.md#free-functions-and-macros) | [file-io/ExportTemplateFilenameSequenceImpl](../src/file-io/ExportTemplateFilenameSequenceImpl.md) |
| [`GPLATES_FILE_IO_FEATURECOLLECTIONFILEFORMATCLASSIFY_H`](../src/file-io/FeatureCollectionFileFormatClassify.md#free-functions-and-macros) | [file-io/FeatureCollectionFileFormatClassify](../src/file-io/FeatureCollectionFileFormatClassify.md) |
| [`GPLATES_FILE_IO_FEATURECOLLECTIONFILEFORMATCONFIGURATION_H`](../src/file-io/FeatureCollectionFileFormatConfiguration.md#free-functions-and-macros) | [file-io/FeatureCollectionFileFormatConfiguration](../src/file-io/FeatureCollectionFileFormatConfiguration.md) |
| [`GPLATES_FILE_IO_FEATURECOLLECTIONFILEFORMATCONFIGURATIONS_H`](../src/file-io/FeatureCollectionFileFormatConfigurations.md#free-functions-and-macros) | [file-io/FeatureCollectionFileFormatConfigurations](../src/file-io/FeatureCollectionFileFormatConfigurations.md) |
| [`GPLATES_FILE_IO_FEATURECOLLECTIONFILEFORMATREGISTRY_H`](../src/file-io/FeatureCollectionFileFormatRegistry.md#free-functions-and-macros) | [file-io/FeatureCollectionFileFormatRegistry](../src/file-io/FeatureCollectionFileFormatRegistry.md) |
| [`GPLATES_FILE_IO_FILE_H`](../src/file-io/File.md#free-functions-and-macros) | [file-io/File](../src/file-io/File.md) |
| [`GPLATES_FILE_IO_FILEFORMATNOTSUPPORTEDEXCEPTION_H`](../src/file-io/FileFormatNotSupportedException.md#free-functions-and-macros) | [file-io/FileFormatNotSupportedException](../src/file-io/FileFormatNotSupportedException.md) |
| [`GPLATES_FILE_IO_FILELOADABORTEDEXCEPTION_H`](../src/file-io/FileLoadAbortedException.md#free-functions-and-macros) | [file-io/FileLoadAbortedException](../src/file-io/FileLoadAbortedException.md) |
| [`GPLATES_FILE_IO_GDALRASTERWRITER_H`](../src/file-io/GdalRasterWriter.md#free-functions-and-macros) | [file-io/GdalRasterWriter](../src/file-io/GdalRasterWriter.md) |
| [`GPLATES_FILE_IO_GMTFORMATDEFORMATIONEXPORT_H`](../src/file-io/GMTFormatDeformationExport.md#free-functions-and-macros) | [file-io/GMTFormatDeformationExport](../src/file-io/GMTFormatDeformationExport.md) |
| [`GPLATES_FILE_IO_GMTFORMATMULTIPOINTVECTORFIELDEXPORT_H`](../src/file-io/GMTFormatMultiPointVectorFieldExport.md#free-functions-and-macros) | [file-io/GMTFormatMultiPointVectorFieldExport](../src/file-io/GMTFormatMultiPointVectorFieldExport.md) |
| [`GPLATES_FILE_IO_GMTFORMATRECONSTRUCTEDSCALARCOVERAGEEXPORT_H`](../src/file-io/GMTFormatReconstructedScalarCoverageExport.md#free-functions-and-macros) | [file-io/GMTFormatReconstructedScalarCoverageExport](../src/file-io/GMTFormatReconstructedScalarCoverageExport.md) |
| [`GPLATES_FILE_IO_GMTFORMATRESOLVEDTOPOLOGICALGEOMETRYEXPORT_H`](../src/file-io/GMTFormatResolvedTopologicalGeometryExport.md#free-functions-and-macros) | [file-io/GMTFormatResolvedTopologicalGeometryExport](../src/file-io/GMTFormatResolvedTopologicalGeometryExport.md) |
| [`GPLATES_FILE_IO_GPMLFEATUREREADERFACTORY_H`](../src/file-io/GpmlFeatureReaderFactory.md#free-functions-and-macros) | [file-io/GpmlFeatureReaderFactory](../src/file-io/GpmlFeatureReaderFactory.md) |
| [`GPLATES_FILE_IO_GPMLFEATUREREADERIMPL_H`](../src/file-io/GpmlFeatureReaderImpl.md#free-functions-and-macros) | [file-io/GpmlFeatureReaderImpl](../src/file-io/GpmlFeatureReaderImpl.md) |
| [`GPLATES_FILE_IO_GPMLFEATUREREADERINTERFACE_H`](../src/file-io/GpmlFeatureReaderInterface.md#free-functions-and-macros) | [file-io/GpmlFeatureReaderInterface](../src/file-io/GpmlFeatureReaderInterface.md) |
| [`GPLATES_FILE_IO_GPMLFORMATDEFORMATIONEXPORT_H`](../src/file-io/GpmlFormatDeformationExport.md#free-functions-and-macros) | [file-io/GpmlFormatDeformationExport](../src/file-io/GpmlFormatDeformationExport.md) |
| [`GPLATES_FILE_IO_GPMLFORMATMULTIPOINTVECTORFIELDEXPORT_H`](../src/file-io/GpmlFormatMultiPointVectorFieldExport.md#free-functions-and-macros) | [file-io/GpmlFormatMultiPointVectorFieldExport](../src/file-io/GpmlFormatMultiPointVectorFieldExport.md) |
| [`GPLATES_FILE_IO_GPMLFORMATRECONSTRUCTEDSCALARCOVERAGEEXPORT_H`](../src/file-io/GpmlFormatReconstructedScalarCoverageExport.md#free-functions-and-macros) | [file-io/GpmlFormatReconstructedScalarCoverageExport](../src/file-io/GpmlFormatReconstructedScalarCoverageExport.md) |
| [`GPLATES_FILE_IO_GPMLPROPERTYREADER_H`](../src/file-io/GpmlPropertyReader.md#free-functions-and-macros) | [file-io/GpmlPropertyReader](../src/file-io/GpmlPropertyReader.md) |
| [`GPLATES_FILE_IO_GPMLREADEREXCEPTION_H`](../src/file-io/GpmlReaderException.md#free-functions-and-macros) | [file-io/GpmlReaderException](../src/file-io/GpmlReaderException.md) |
| [`GPLATES_FILE_IO_GPMLUPGRADEREADERUTILS_H`](../src/file-io/GpmlUpgradeReaderUtils.md#free-functions-and-macros) | [file-io/GpmlUpgradeReaderUtils](../src/file-io/GpmlUpgradeReaderUtils.md) |
| [`GPLATES_FILE_IO_GZIPFILE_H`](../src/file-io/GzipFile.md#free-functions-and-macros) | [file-io/GzipFile](../src/file-io/GzipFile.md) |
| [`GPLATES_FILE_IO_OGRFORMATRESOLVEDTOPOLOGICALGEOMETRYXPORT_H`](../src/file-io/OgrFormatResolvedTopologicalGeometryExport.md#free-functions-and-macros) | [file-io/OgrFormatResolvedTopologicalGeometryExport](../src/file-io/OgrFormatResolvedTopologicalGeometryExport.md) |
| [`GPLATES_FILE_IO_PLATESFORMATUTILS_H`](../src/file-io/PlatesFormatUtils.md#free-functions-and-macros) | [file-io/PlatesFormatUtils](../src/file-io/PlatesFormatUtils.md) |
| [`GPLATES_FILE_IO_RASTERFILECACHE_H`](../src/file-io/RasterFileCache.md#free-functions-and-macros) | [file-io/RasterFileCache](../src/file-io/RasterFileCache.md) |
| [`GPLATES_FILE_IO_RASTERFILECACHEFORMATREADER_H`](../src/file-io/RasterFileCacheFormatReader.md#free-functions-and-macros) | [file-io/RasterFileCacheFormatReader](../src/file-io/RasterFileCacheFormatReader.md) |
| [`GPLATES_FILE_IO_RASTERWRITER_H`](../src/file-io/RasterWriter.md#free-functions-and-macros) | [file-io/RasterWriter](../src/file-io/RasterWriter.md) |
| [`GPLATES_FILE_IO_READERRORMESSAGES_H`](../src/file-io/ReadErrorMessages.md#free-functions-and-macros) | [file-io/ReadErrorMessages](../src/file-io/ReadErrorMessages.md) |
| [`GPLATES_FILE_IO_READERRORUTILS_H`](../src/file-io/ReadErrorUtils.md#free-functions-and-macros) | [file-io/ReadErrorUtils](../src/file-io/ReadErrorUtils.md) |
| [`GPLATES_FILE_IO_RECONSTRUCTEDSCALARCOVERAGEEXPORT_H`](../src/file-io/ReconstructedScalarCoverageExport.md#free-functions-and-macros) | [file-io/ReconstructedScalarCoverageExport](../src/file-io/ReconstructedScalarCoverageExport.md) |
| [`GPLATES_FILE_IO_RECONSTRUCTIONGEOMETRYEXPORTIMPL_H`](../src/file-io/ReconstructionGeometryExportImpl.md#free-functions-and-macros) | [file-io/ReconstructionGeometryExportImpl](../src/file-io/ReconstructionGeometryExportImpl.md) |
| [`GPLATES_FILE_IO_RESOLVEDTOPOLOGICALGEOMETRYEXPORT_H`](../src/file-io/ResolvedTopologicalGeometryExport.md#free-functions-and-macros) | [file-io/ResolvedTopologicalGeometryExport](../src/file-io/ResolvedTopologicalGeometryExport.md) |
| [`GPLATES_FILE_IO_RGBARASTERWRITER_H`](../src/file-io/RgbaRasterWriter.md#free-functions-and-macros) | [file-io/RgbaRasterWriter](../src/file-io/RgbaRasterWriter.md) |
| [`GPLATES_FILE_IO_SOURCERASTERFILECACHEFORMATREADER_H`](../src/file-io/SourceRasterFileCacheFormatReader.md#free-functions-and-macros) | [file-io/SourceRasterFileCacheFormatReader](../src/file-io/SourceRasterFileCacheFormatReader.md) |
| [`GPLATES_FILE_IO_TERRAFORMATVELOCITYVECTORFIELDEXPORT_H`](../src/file-io/TerraFormatVelocityVectorFieldExport.md#free-functions-and-macros) | [file-io/TerraFormatVelocityVectorFieldExport](../src/file-io/TerraFormatVelocityVectorFieldExport.md) |
| [`GPLATES_FILEIO_ARBITRARYNODEPROCESSOR_H`](../src/file-io/ArbitraryNodeProcessor.md#free-functions-and-macros) | [file-io/ArbitraryNodeProcessor](../src/file-io/ArbitraryNodeProcessor.md) |
| [`GPLATES_FILEIO_ARBITRARYXMLPROFILE_H`](../src/file-io/ArbitraryXmlProfile.md#free-functions-and-macros) | [file-io/ArbitraryXmlProfile](../src/file-io/ArbitraryXmlProfile.md) |
| [`GPLATES_FILEIO_ARBITRARYXMLREADER_H`](../src/file-io/ArbitraryXmlReader.md#free-functions-and-macros) | [file-io/ArbitraryXmlReader](../src/file-io/ArbitraryXmlReader.md) |
| [`GPLATES_FILEIO_CPTREADER_H`](../src/file-io/CptReader.md#free-functions-and-macros) | [file-io/CptReader](../src/file-io/CptReader.md) |
| [`GPLATES_FILEIO_ERROROPENINGFILEFORREADINGEXCEPTION_H`](../src/file-io/ErrorOpeningFileForReadingException.md#free-functions-and-macros) | [file-io/ErrorOpeningFileForReadingException](../src/file-io/ErrorOpeningFileForReadingException.md) |
| [`GPLATES_FILEIO_ERROROPENINGFILEFORWRITINGEXCEPTION_H`](../src/file-io/ErrorOpeningFileForWritingException.md#free-functions-and-macros) | [file-io/ErrorOpeningFileForWritingException](../src/file-io/ErrorOpeningFileForWritingException.md) |
| [`GPLATES_FILEIO_ERROROPENINGPIPEFROMGZIPEXCEPTION_H`](../src/file-io/ErrorOpeningPipeFromGzipException.md#free-functions-and-macros) | [file-io/ErrorOpeningPipeFromGzipException](../src/file-io/ErrorOpeningPipeFromGzipException.md) |
| [`GPLATES_FILEIO_ERROROPENINGPIPETOGZIPEXCEPTION_H`](../src/file-io/ErrorOpeningPipeToGzipException.md#free-functions-and-macros) | [file-io/ErrorOpeningPipeToGzipException](../src/file-io/ErrorOpeningPipeToGzipException.md) |
| [`GPLATES_FILEIO_FEATURECOLLECTIONFILEFORMAT_H`](../src/file-io/FeatureCollectionFileFormat.md#free-functions-and-macros) | [file-io/FeatureCollectionFileFormat](../src/file-io/FeatureCollectionFileFormat.md) |
| [`GPLATES_FILEIO_FEATUREPROPERTIESMAP_H`](../src/file-io/deprecated/FeaturePropertiesMap.md#free-functions-and-macros) | [file-io/deprecated/FeaturePropertiesMap](../src/file-io/deprecated/FeaturePropertiesMap.md) |
| [`GPLATES_FILEIO_FILEFORMAT_H`](../src/file-io/deprecated/FileFormat.md#free-functions-and-macros) | [file-io/deprecated/FileFormat](../src/file-io/deprecated/FileFormat.md) |
| [`GPLATES_FILEIO_FILEINFO_H`](../src/file-io/FileInfo.md#free-functions-and-macros) | [file-io/FileInfo](../src/file-io/FileInfo.md) |
| [`GPLATES_FILEIO_GDAL_H`](../src/file-io/Gdal.md#free-functions-and-macros) | [file-io/Gdal](../src/file-io/Gdal.md) |
| [`GPLATES_FILEIO_GDALRASTERREADER_H`](../src/file-io/GdalRasterReader.md#free-functions-and-macros) | [file-io/GdalRasterReader](../src/file-io/GdalRasterReader.md) |
| [`GPLATES_FILEIO_GDALUTILS_H`](../src/file-io/GdalUtils.md#free-functions-and-macros) | [file-io/GdalUtils](../src/file-io/GdalUtils.md) |
| [`GPLATES_FILEIO_GEOMETRYEXPORTER_H`](../src/file-io/GeometryExporter.md#free-functions-and-macros) | [file-io/GeometryExporter](../src/file-io/GeometryExporter.md) |
| [`GPLATES_FILEIO_GEOSCIMLPROFILE_H`](../src/file-io/GeoscimlProfile.md#free-functions-and-macros) | [file-io/GeoscimlProfile](../src/file-io/GeoscimlProfile.md) |
| [`GPLATES_FILEIO_GMAPREADER_H`](../src/file-io/GmapReader.md#free-functions-and-macros) | [file-io/GmapReader](../src/file-io/GmapReader.md) |
| [`GPLATES_FILEIO_GMTFORMATFLOWLINESEXPORT_H`](../src/file-io/GMTFormatFlowlineExport.md#free-functions-and-macros) | [file-io/GMTFormatFlowlineExport](../src/file-io/GMTFormatFlowlineExport.md) |
| [`GPLATES_FILEIO_GMTFORMATGEOMETRYEXPORTER_H`](../src/file-io/GMTFormatGeometryExporter.md#free-functions-and-macros) | [file-io/GMTFormatGeometryExporter](../src/file-io/GMTFormatGeometryExporter.md) |
| [`GPLATES_FILEIO_GMTFORMATHEADER_H`](../src/file-io/GMTFormatHeader.md#free-functions-and-macros) | [file-io/GMTFormatHeader](../src/file-io/GMTFormatHeader.md) |
| [`GPLATES_FILEIO_GMTFORMATMOTIONPATHSEXPORT_H`](../src/file-io/GMTFormatMotionPathExport.md#free-functions-and-macros) | [file-io/GMTFormatMotionPathExport](../src/file-io/GMTFormatMotionPathExport.md) |
| [`GPLATES_FILEIO_GMTFORMATRECONSTRUCTEDFEATUREGEOMETRYEXPORT_H`](../src/file-io/GMTFormatReconstructedFeatureGeometryExport.md#free-functions-and-macros) | [file-io/GMTFormatReconstructedFeatureGeometryExport](../src/file-io/GMTFormatReconstructedFeatureGeometryExport.md) |
| [`GPLATES_FILEIO_GMTFORMATWRITER_H`](../src/file-io/GMTFormatWriter.md#free-functions-and-macros) | [file-io/GMTFormatWriter](../src/file-io/GMTFormatWriter.md) |
| [`GPLATES_FILEIO_GPMLONEPOINTFIVEOUTPUTVISITOR_H`](../src/file-io/deprecated/GpmlOnePointFiveOutputVisitor.md#free-functions-and-macros) | [file-io/deprecated/GpmlOnePointFiveOutputVisitor](../src/file-io/deprecated/GpmlOnePointFiveOutputVisitor.md) |
| [`GPLATES_FILEIO_GPMLOUTPUTVISITOR_H`](../src/file-io/GpmlOutputVisitor.md#free-functions-and-macros) | [file-io/GpmlOutputVisitor](../src/file-io/GpmlOutputVisitor.md) |
| [`GPLATES_FILEIO_GPMLPROPERTYSTRUCTURALTYPEREADER_H`](../src/file-io/GpmlPropertyStructuralTypeReader.md#free-functions-and-macros) | [file-io/GpmlPropertyStructuralTypeReader](../src/file-io/GpmlPropertyStructuralTypeReader.md) |
| [`GPLATES_FILEIO_GPMLPROPERTYSTRUCTURALTYPEREADERUTILS_H`](../src/file-io/GpmlPropertyStructuralTypeReaderUtils.md#free-functions-and-macros) | [file-io/GpmlPropertyStructuralTypeReaderUtils](../src/file-io/GpmlPropertyStructuralTypeReaderUtils.md) |
| [`GPLATES_FILEIO_GPMLREADER_H`](../src/file-io/GpmlReader.md#free-functions-and-macros) | [file-io/GpmlReader](../src/file-io/GpmlReader.md) |
| [`GPLATES_FILEIO_GPMLREADERUTILS_H`](../src/file-io/GpmlReaderUtils.md#free-functions-and-macros) | [file-io/GpmlReaderUtils](../src/file-io/GpmlReaderUtils.md) |
| [`GPLATES_FILEIO_GPMLSTRUCTURALTYPEREADERUTILS_H`](../src/file-io/GpmlStructuralTypeReaderUtils.md#free-functions-and-macros) | [file-io/GpmlStructuralTypeReaderUtils](../src/file-io/GpmlStructuralTypeReaderUtils.md) |
| [`GPLATES_FILEIO_GSMLCONST_H`](../src/file-io/GsmlConst.md#free-functions-and-macros) | [file-io/GsmlConst](../src/file-io/GsmlConst.md) |
| [`GPLATES_FILEIO_GSMLFEATUREHANDLERS_H`](../src/file-io/GsmlFeatureHandlers.md#free-functions-and-macros) | [file-io/GsmlFeatureHandlers](../src/file-io/GsmlFeatureHandlers.md) |
| [`GPLATES_FILEIO_GSMLFEATURESDEF_H`](../src/file-io/GsmlFeaturesDef.md#free-functions-and-macros) | [file-io/GsmlFeaturesDef](../src/file-io/GsmlFeaturesDef.md) |
| [`GPLATES_FILEIO_GSMLNODEPROCESSOR_H`](../src/file-io/GsmlNodeProcessor.md#free-functions-and-macros) | [file-io/GsmlNodeProcessor](../src/file-io/GsmlNodeProcessor.md) |
| [`GPLATES_FILEIO_GSMLPROPERTYDEF_H`](../src/file-io/GsmlPropertyDef.md#free-functions-and-macros) | [file-io/GsmlPropertyDef](../src/file-io/GsmlPropertyDef.md) |
| [`GPLATES_FILEIO_GSMLPROPERTYHANDLERS_H`](../src/file-io/GsmlPropertyHandlers.md#free-functions-and-macros) | [file-io/GsmlPropertyHandlers](../src/file-io/GsmlPropertyHandlers.md) |
| [`GPLATES_FILEIO_LINEREADER_H`](../src/file-io/LineReader.md#free-functions-and-macros) | [file-io/LineReader](../src/file-io/LineReader.md) |
| [`GPLATES_FILEIO_LOGTOFILEHANDLER_H`](../src/file-io/LogToFileHandler.md#free-functions-and-macros) | [file-io/LogToFileHandler](../src/file-io/LogToFileHandler.md) |
| [`GPLATES_FILEIO_MIPMAPPEDRASTERFORMATREADER_H`](../src/file-io/MipmappedRasterFormatReader.md#free-functions-and-macros) | [file-io/MipmappedRasterFormatReader](../src/file-io/MipmappedRasterFormatReader.md) |
| [`GPLATES_FILEIO_MIPMAPPEDRASTERFORMATWRITER_H`](../src/file-io/MipmappedRasterFormatWriter.md#free-functions-and-macros) | [file-io/MipmappedRasterFormatWriter](../src/file-io/MipmappedRasterFormatWriter.md) |
| [`GPLATES_FILEIO_MULTIPOINTVECTORFIELDEXPORT_H`](../src/file-io/MultiPointVectorFieldExport.md#free-functions-and-macros) | [file-io/MultiPointVectorFieldExport](../src/file-io/MultiPointVectorFieldExport.md) |
| [`GPLATES_FILEIO_OGR_H`](../src/file-io/Ogr.md#free-functions-and-macros) | [file-io/Ogr](../src/file-io/Ogr.md) |
| [`GPLATES_FILEIO_OGREXCEPTION_H`](../src/file-io/OgrException.md#free-functions-and-macros) | [file-io/OgrException](../src/file-io/OgrException.md) |
| [`GPLATES_FILEIO_OGRFEATURECOLLECTIONWRITER_H`](../src/file-io/OgrFeatureCollectionWriter.md#free-functions-and-macros) | [file-io/OgrFeatureCollectionWriter](../src/file-io/OgrFeatureCollectionWriter.md) |
| [`GPLATES_FILEIO_OGRREADER_H`](../src/file-io/OgrReader.md#free-functions-and-macros) | [file-io/OgrReader](../src/file-io/OgrReader.md) |
| [`GPLATES_FILEIO_OGRWRITER_H`](../src/file-io/OgrWriter.md#free-functions-and-macros) | [file-io/OgrWriter](../src/file-io/OgrWriter.md) |
| [`GPLATES_FILEIO_PICKFILEREADER_H`](../src/file-io/HellingerReader.md#free-functions-and-macros) | [file-io/HellingerReader](../src/file-io/HellingerReader.md) |
| [`GPLATES_FILEIO_PICKFILEWRITER_H`](../src/file-io/HellingerWriter.md#free-functions-and-macros) | [file-io/HellingerWriter](../src/file-io/HellingerWriter.md) |
| [`GPLATES_FILEIO_PLATESLINEFORMATGEOMETRYEXPORTER_H`](../src/file-io/PlatesLineFormatGeometryExporter.md#free-functions-and-macros) | [file-io/PlatesLineFormatGeometryExporter](../src/file-io/PlatesLineFormatGeometryExporter.md) |
| [`GPLATES_FILEIO_PLATESLINEFORMATHEADERVISITOR_H`](../src/file-io/PlatesLineFormatHeaderVisitor.md#free-functions-and-macros) | [file-io/PlatesLineFormatHeaderVisitor](../src/file-io/PlatesLineFormatHeaderVisitor.md) |
| [`GPLATES_FILEIO_PLATESLINEFORMATREADER_H`](../src/file-io/PlatesLineFormatReader.md#free-functions-and-macros) | [file-io/PlatesLineFormatReader](../src/file-io/PlatesLineFormatReader.md) |
| [`GPLATES_FILEIO_PLATESLINEFORMATWRITER_H`](../src/file-io/PlatesLineFormatWriter.md#free-functions-and-macros) | [file-io/PlatesLineFormatWriter](../src/file-io/PlatesLineFormatWriter.md) |
| [`GPLATES_FILEIO_PLATESROTATIONFILEPROXY_H`](../src/file-io/PlatesRotationFileProxy.md#free-functions-and-macros) | [file-io/PlatesRotationFileProxy](../src/file-io/PlatesRotationFileProxy.md) |
| [`GPLATES_FILEIO_PLATESROTATIONFORMATREADER_H`](../src/file-io/PlatesRotationFormatReader.md#free-functions-and-macros) | [file-io/PlatesRotationFormatReader](../src/file-io/PlatesRotationFormatReader.md) |
| [`GPLATES_FILEIO_PLATESROTATIONFORMATWRITER_H`](../src/file-io/PlatesRotationFormatWriter.md#free-functions-and-macros) | [file-io/PlatesRotationFormatWriter](../src/file-io/PlatesRotationFormatWriter.md) |
| [`GPLATES_FILEIO_PROJ_H`](../src/file-io/Proj.md#free-functions-and-macros) | [file-io/Proj](../src/file-io/Proj.md) |
| [`GPLATES_FILEIO_PROPERTYMAPPER_H`](../src/file-io/PropertyMapper.md#free-functions-and-macros) | [file-io/PropertyMapper](../src/file-io/PropertyMapper.md) |
| [`GPLATES_FILEIO_RASTERBANDREADER_H`](../src/file-io/RasterBandReader.md#free-functions-and-macros) | [file-io/RasterBandReader](../src/file-io/RasterBandReader.md) |
| [`GPLATES_FILEIO_RASTERBANDREADERHANDLE_H`](../src/file-io/RasterBandReaderHandle.md#free-functions-and-macros) | [file-io/RasterBandReaderHandle](../src/file-io/RasterBandReaderHandle.md) |
| [`GPLATES_FILEIO_RASTERFILECACHEFORMAT_H`](../src/file-io/RasterFileCacheFormat.md#free-functions-and-macros) | [file-io/RasterFileCacheFormat](../src/file-io/RasterFileCacheFormat.md) |
| [`GPLATES_FILEIO_RASTERREADER_H`](../src/file-io/RasterReader.md#free-functions-and-macros) | [file-io/RasterReader](../src/file-io/RasterReader.md) |
| [`GPLATES_FILEIO_READER_H`](../src/file-io/deprecated/Reader.md#free-functions-and-macros) | [file-io/deprecated/Reader](../src/file-io/deprecated/Reader.md) |
| [`GPLATES_FILEIO_READERRORACCUMULATION_H`](../src/file-io/ReadErrorAccumulation.md#free-functions-and-macros) | [file-io/ReadErrorAccumulation](../src/file-io/ReadErrorAccumulation.md) |
| [`GPLATES_FILEIO_READERROROCCURRENCE_H`](../src/file-io/ReadErrorOccurrence.md#free-functions-and-macros) | [file-io/ReadErrorOccurrence](../src/file-io/ReadErrorOccurrence.md) |
| [`GPLATES_FILEIO_READERRORS_H`](../src/file-io/ReadErrors.md#free-functions-and-macros) | [file-io/ReadErrors](../src/file-io/ReadErrors.md) |
| [`GPLATES_FILEIO_RECONSTRUCTEDFEATUREGEOMETRYEXPORT_H`](../src/file-io/ReconstructedFeatureGeometryExport.md#free-functions-and-macros) | [file-io/ReconstructedFeatureGeometryExport](../src/file-io/ReconstructedFeatureGeometryExport.md) |
| [`GPLATES_FILEIO_RECONSTRUCTEDFLOWLINEEXPORT_H`](../src/file-io/ReconstructedFlowlineExport.md#free-functions-and-macros) | [file-io/ReconstructedFlowlineExport](../src/file-io/ReconstructedFlowlineExport.md) |
| [`GPLATES_FILEIO_RECONSTRUCTEDMOTIONPATHEXPORT_H`](../src/file-io/ReconstructedMotionPathExport.md#free-functions-and-macros) | [file-io/ReconstructedMotionPathExport](../src/file-io/ReconstructedMotionPathExport.md) |
| [`GPLATES_FILEIO_RGBARASTERREADER_H`](../src/file-io/RgbaRasterReader.md#free-functions-and-macros) | [file-io/RgbaRasterReader](../src/file-io/RgbaRasterReader.md) |
| [`GPLATES_FILEIO_ROTATIONATTRIBUTESREGISTRY_H`](../src/file-io/RotationAttributesRegistry.md#free-functions-and-macros) | [file-io/RotationAttributesRegistry](../src/file-io/RotationAttributesRegistry.md) |
| [`GPLATES_FILEIO_SCALARFIELD3DFILEFORMAT_H`](../src/file-io/ScalarField3DFileFormat.md#free-functions-and-macros) | [file-io/ScalarField3DFileFormat](../src/file-io/ScalarField3DFileFormat.md) |
| [`GPLATES_FILEIO_SCALARFIELD3DFILEFORMATREADER_H`](../src/file-io/ScalarField3DFileFormatReader.md#free-functions-and-macros) | [file-io/ScalarField3DFileFormatReader](../src/file-io/ScalarField3DFileFormatReader.md) |
| [`GPLATES_FILEIO_SHAPEFILEFORMATFLOWLINEEXPORT_H`](../src/file-io/OgrFormatFlowlineExport.md#free-functions-and-macros) | [file-io/OgrFormatFlowlineExport](../src/file-io/OgrFormatFlowlineExport.md) |
| [`GPLATES_FILEIO_SHAPEFILEFORMATMOTIONPATHEXPORT_H`](../src/file-io/OgrFormatMotionPathExport.md#free-functions-and-macros) | [file-io/OgrFormatMotionPathExport](../src/file-io/OgrFormatMotionPathExport.md) |
| [`GPLATES_FILEIO_SHAPEFILEFORMATRECONSTRUCTEDFEATUREGEOMETRYEXPORT_H`](../src/file-io/OgrFormatReconstructedFeatureGeometryExport.md#free-functions-and-macros) | [file-io/OgrFormatReconstructedFeatureGeometryExport](../src/file-io/OgrFormatReconstructedFeatureGeometryExport.md) |
| [`GPLATES_FILEIO_SHAPEFILEGEOMETRYEXPORTER_H`](../src/file-io/OgrGeometryExporter.md#free-functions-and-macros) | [file-io/OgrGeometryExporter](../src/file-io/OgrGeometryExporter.md) |
| [`GPLATES_FILEIO_SHAPEFILEUTILS_H`](../src/file-io/OgrUtils.md#free-functions-and-macros) | [file-io/OgrUtils](../src/file-io/OgrUtils.md) |
| [`GPLATES_FILEIO_SHAPEFILEXMLREADER_H`](../src/file-io/ShapefileXmlReader.md#free-functions-and-macros) | [file-io/ShapefileXmlReader](../src/file-io/ShapefileXmlReader.md) |
| [`GPLATES_FILEIO_SHAPEFILEXMLWRITER_H`](../src/file-io/ShapefileXmlWriter.md#free-functions-and-macros) | [file-io/ShapefileXmlWriter](../src/file-io/ShapefileXmlWriter.md) |
| [`GPLATES_FILEIO_STANDALONEBUNDLE_H`](../src/file-io/StandaloneBundle.md#free-functions-and-macros) | [file-io/StandaloneBundle](../src/file-io/StandaloneBundle.md) |
| [`GPLATES_FILEIO_SYMBOLFILEREADER_H`](../src/file-io/SymbolFileReader.md#free-functions-and-macros) | [file-io/SymbolFileReader](../src/file-io/SymbolFileReader.md) |
| [`GPLATES_FILEIO_TEMPORARYFILEREGISTRY_H`](../src/file-io/TemporaryFileRegistry.md#free-functions-and-macros) | [file-io/TemporaryFileRegistry](../src/file-io/TemporaryFileRegistry.md) |
| [`GPLATES_FILEIO_WRITER_H`](../src/file-io/deprecated/Writer.md#free-functions-and-macros) | [file-io/deprecated/Writer](../src/file-io/deprecated/Writer.md) |
| [`GPLATES_FILEIO_XMLNODEPROCESSORFACTORY_H`](../src/file-io/GsmlNodeProcessorFactory.md#free-functions-and-macros) | [file-io/GsmlNodeProcessorFactory](../src/file-io/GsmlNodeProcessorFactory.md) |
| [`GPLATES_FILEIO_XMLOUTPUTINTERFACE_H`](../src/file-io/XmlOutputInterface.md#free-functions-and-macros) | [file-io/XmlOutputInterface](../src/file-io/XmlOutputInterface.md) |
| [`GPLATES_FILEIO_XMLWRITER_H`](../src/file-io/XmlWriter.md#free-functions-and-macros) | [file-io/XmlWriter](../src/file-io/XmlWriter.md) |
| [`GPLATES_GLOBAL_ABORTEXCEPTION_H`](../src/global/AbortException.md#free-functions-and-macros) | [global/AbortException](../src/global/AbortException.md) |
| [`GPLATES_GLOBAL_ASSERTIONFAILUREEXCEPTION_H`](../src/global/AssertionFailureException.md#free-functions-and-macros) | [global/AssertionFailureException](../src/global/AssertionFailureException.md) |
| [`GPLATES_GLOBAL_COMPILERWARNINGS_H`](../src/global/CompilerWarnings.md#free-functions-and-macros) | [global/CompilerWarnings](../src/global/CompilerWarnings.md) |
| [`GPLATES_GLOBAL_EXCEPTION_H`](../src/global/GPlatesException.md#free-functions-and-macros) | [global/GPlatesException](../src/global/GPlatesException.md) |
| [`GPLATES_GLOBAL_EXTERNALRESOURCEFAILUREEXCEPTION_H`](../src/global/ExternalResourceFailureException.md#free-functions-and-macros) | [global/ExternalResourceFailureException](../src/global/ExternalResourceFailureException.md) |
| [`GPLATES_GLOBAL_GDALVERSION_H`](../src/global/GdalVersion.md#free-functions-and-macros) | [global/GdalVersion](../src/global/GdalVersion.md) |
| [`GPLATES_GLOBAL_INTERNALINCONSISTENCYEXCEPTION_H`](../src/global/InternalInconsistencyException.md#free-functions-and-macros) | [global/InternalInconsistencyException](../src/global/InternalInconsistencyException.md) |
| [`GPLATES_GLOBAL_INTERNALOBJECTINCONSISTENCYEXCEPTION_H`](../src/global/InternalObjectInconsistencyException.md#free-functions-and-macros) | [global/InternalObjectInconsistencyException](../src/global/InternalObjectInconsistencyException.md) |
| [`GPLATES_GLOBAL_INTRUSIVEPOINTERZEROREFCOUNTEXCEPTION_H`](../src/global/IntrusivePointerZeroRefCountException.md#free-functions-and-macros) | [global/IntrusivePointerZeroRefCountException](../src/global/IntrusivePointerZeroRefCountException.md) |
| [`GPLATES_GLOBAL_INVALIDFEATURECOLLECTIONEXCEPTION_H`](../src/global/InvalidFeatureCollectionException.md#free-functions-and-macros) | [global/InvalidFeatureCollectionException](../src/global/InvalidFeatureCollectionException.md) |
| [`GPLATES_GLOBAL_LICENSE_H`](../src/global/License.md#free-functions-and-macros) | [global/License](../src/global/License.md) |
| [`GPLATES_GLOBAL_LOGEXCEPTION_H`](../src/global/LogException.md#free-functions-and-macros) | [global/LogException](../src/global/LogException.md) |
| [`GPLATES_GLOBAL_POINTERTRAITS_H`](../src/global/PointerTraits.md#free-functions-and-macros) | [global/PointerTraits](../src/global/PointerTraits.md) |
| [`GPLATES_GLOBAL_PRECONDITIONVIOLATIONERROR_H`](../src/global/PreconditionViolationError.md#free-functions-and-macros) | [global/PreconditionViolationError](../src/global/PreconditionViolationError.md) |
| [`GPLATES_GLOBAL_PYTHON_H`](../src/global/python.md#free-functions-and-macros) | [global/python](../src/global/python.md) |
| [`GPLATES_GLOBAL_RETRIEVALFROMEMPTYCONTAINEREXCEPTION_H`](../src/global/RetrievalFromEmptyContainerException.md#free-functions-and-macros) | [global/RetrievalFromEmptyContainerException](../src/global/RetrievalFromEmptyContainerException.md) |
| [`GPLATES_GLOBAL_TYPES_H`](../src/global/deprecated/types.md#free-functions-and-macros) | [global/deprecated/types](../src/global/deprecated/types.md) |
| [`GPLATES_GLOBAL_UNEXPECTEDEMPTYFEATURECOLLECTIONEXCEPTION_H`](../src/global/UnexpectedEmptyFeatureCollectionException.md#free-functions-and-macros) | [global/UnexpectedEmptyFeatureCollectionException](../src/global/UnexpectedEmptyFeatureCollectionException.md) |
| [`GPLATES_GLOBAL_UNICODE_H`](../src/global/unicode.md#free-functions-and-macros) | [global/unicode](../src/global/unicode.md) |
| [`GPLATES_GLOBAL_VERSION_H`](../src/global/Version.md#free-functions-and-macros) | [global/Version](../src/global/Version.md) |
| [`GPLATES_GUI_ADDCLICKEDGEOMETRIESTOFEATURETABLE_H`](../src/gui/AddClickedGeometriesToFeatureTable.md#free-functions-and-macros) | [gui/AddClickedGeometriesToFeatureTable](../src/gui/AddClickedGeometriesToFeatureTable.md) |
| [`GPLATES_GUI_AGECOLOURPALETTES_H`](../src/gui/AgeColourPalettes.md#free-functions-and-macros) | [gui/AgeColourPalettes](../src/gui/AgeColourPalettes.md) |
| [`GPLATES_GUI_ANIMATIONCONTROLLER_H`](../src/gui/AnimationController.md#free-functions-and-macros) | [gui/AnimationController](../src/gui/AnimationController.md) |
| [`GPLATES_GUI_BUILTINCOLOURPALETTES_H`](../src/gui/BuiltinColourPalettes.md#free-functions-and-macros) | [gui/BuiltinColourPalettes](../src/gui/BuiltinColourPalettes.md) |
| [`GPLATES_GUI_BUILTINCOLOURPALETTETYPE_H`](../src/gui/BuiltinColourPaletteType.md#free-functions-and-macros) | [gui/BuiltinColourPaletteType](../src/gui/BuiltinColourPaletteType.md) |
| [`GPLATES_GUI_CANVASTOOLWORKFLOW_H`](../src/gui/CanvasToolWorkflow.md#free-functions-and-macros) | [gui/CanvasToolWorkflow](../src/gui/CanvasToolWorkflow.md) |
| [`GPLATES_GUI_CANVASTOOLWORKFLOWS_H`](../src/gui/CanvasToolWorkflows.md#free-functions-and-macros) | [gui/CanvasToolWorkflows](../src/gui/CanvasToolWorkflows.md) |
| [`GPLATES_GUI_CHOOSECANVASTOOLUNDOCOMMAND_H`](../src/gui/ChooseCanvasToolUndoCommand.md#free-functions-and-macros) | [gui/ChooseCanvasToolUndoCommand](../src/gui/ChooseCanvasToolUndoCommand.md) |
| [`GPLATES_GUI_COLOUR_H`](../src/gui/Colour.md#free-functions-and-macros) | [gui/Colour](../src/gui/Colour.md) |
| [`GPLATES_GUI_COLOURFILTER_H`](../src/gui/ColourFilter.md#free-functions-and-macros) | [gui/ColourFilter](../src/gui/ColourFilter.md) |
| [`GPLATES_GUI_COLOURNAMESET_H`](../src/gui/ColourNameSet.md#free-functions-and-macros) | [gui/ColourNameSet](../src/gui/ColourNameSet.md) |
| [`GPLATES_GUI_COLOURPALETTE_H`](../src/gui/ColourPalette.md#free-functions-and-macros) | [gui/ColourPalette](../src/gui/ColourPalette.md) |
| [`GPLATES_GUI_COLOURPALETTEADAPTER_H`](../src/gui/ColourPaletteAdapter.md#free-functions-and-macros) | [gui/ColourPaletteAdapter](../src/gui/ColourPaletteAdapter.md) |
| [`GPLATES_GUI_COLOURPALETTERANGEREMAPPER_H`](../src/gui/ColourPaletteRangeRemapper.md#free-functions-and-macros) | [gui/ColourPaletteRangeRemapper](../src/gui/ColourPaletteRangeRemapper.md) |
| [`GPLATES_GUI_COLOURPALETTEUTILS_H`](../src/gui/ColourPaletteUtils.md#free-functions-and-macros) | [gui/ColourPaletteUtils](../src/gui/ColourPaletteUtils.md) |
| [`GPLATES_GUI_COLOURPALETTEVISITOR_H`](../src/gui/ColourPaletteVisitor.md#free-functions-and-macros) | [gui/ColourPaletteVisitor](../src/gui/ColourPaletteVisitor.md) |
| [`GPLATES_GUI_COLOURPROXY_H`](../src/gui/ColourProxy.md#free-functions-and-macros) | [gui/ColourProxy](../src/gui/ColourProxy.md) |
| [`GPLATES_GUI_COLOURRAWRASTER_H`](../src/gui/ColourRawRaster.md#free-functions-and-macros) | [gui/ColourRawRaster](../src/gui/ColourRawRaster.md) |
| [`GPLATES_GUI_COLOURSCALEGENERATOR_H`](../src/gui/ColourScaleGenerator.md#free-functions-and-macros) | [gui/ColourScaleGenerator](../src/gui/ColourScaleGenerator.md) |
| [`GPLATES_GUI_COLOURSCHEME_H`](../src/gui/ColourScheme.md#free-functions-and-macros) | [gui/ColourScheme](../src/gui/ColourScheme.md) |
| [`GPLATES_GUI_COLOURSCHEMECONTAINER_H`](../src/gui/ColourSchemeContainer.md#free-functions-and-macros) | [gui/ColourSchemeContainer](../src/gui/ColourSchemeContainer.md) |
| [`GPLATES_GUI_COLOURSCHEMEDELEGATOR_H`](../src/gui/ColourSchemeDelegator.md#free-functions-and-macros) | [gui/ColourSchemeDelegator](../src/gui/ColourSchemeDelegator.md) |
| [`GPLATES_GUI_COLOURSCHEMEINFO_H`](../src/gui/ColourSchemeInfo.md#free-functions-and-macros) | [gui/ColourSchemeInfo](../src/gui/ColourSchemeInfo.md) |
| [`GPLATES_GUI_COLOURSPECTRUM_H`](../src/gui/ColourSpectrum.md#free-functions-and-macros) | [gui/ColourSpectrum](../src/gui/ColourSpectrum.md) |
| [`GPLATES_GUI_COMMANDSERVER_H`](../src/gui/CommandServer.md#free-functions-and-macros) | [gui/CommandServer](../src/gui/CommandServer.md) |
| [`GPLATES_GUI_COMPLETIONIST_H`](../src/gui/Completionist.md#free-functions-and-macros) | [gui/Completionist](../src/gui/Completionist.md) |
| [`GPLATES_GUI_CONFIGGUIUTILS_H`](../src/gui/ConfigGuiUtils.md#free-functions-and-macros) | [gui/ConfigGuiUtils](../src/gui/ConfigGuiUtils.md) |
| [`GPLATES_GUI_CONFIGMODEL_H`](../src/gui/ConfigModel.md#free-functions-and-macros) | [gui/ConfigModel](../src/gui/ConfigModel.md) |
| [`GPLATES_GUI_CONFIGVALUEDELEGATE_H`](../src/gui/ConfigValueDelegate.md#free-functions-and-macros) | [gui/ConfigValueDelegate](../src/gui/ConfigValueDelegate.md) |
| [`GPLATES_GUI_CPTCOLOURPALETTE_H`](../src/gui/CptColourPalette.md#free-functions-and-macros) | [gui/CptColourPalette](../src/gui/CptColourPalette.md) |
| [`GPLATES_GUI_CSVEXPORT_H`](../src/gui/CsvExport.md#free-functions-and-macros) | [gui/CsvExport](../src/gui/CsvExport.md) |
| [`GPLATES_GUI_CUSTOMCOMPLETER_H`](../src/gui/CustomCompleter.md#free-functions-and-macros) | [gui/CustomCompleter](../src/gui/CustomCompleter.md) |
| [`GPLATES_GUI_DIALOGS_H`](../src/gui/Dialogs.md#free-functions-and-macros) | [gui/Dialogs](../src/gui/Dialogs.md) |
| [`GPLATES_GUI_DOCKSTATE_H`](../src/gui/DockState.md#free-functions-and-macros) | [gui/DockState](../src/gui/DockState.md) |
| [`GPLATES_GUI_DRAWSTYLEADAPTERS_H`](../src/gui/DrawStyleAdapters.md#free-functions-and-macros) | [gui/DrawStyleAdapters](../src/gui/DrawStyleAdapters.md) |
| [`GPLATES_GUI_DRAWSTYLEMANAGER_H`](../src/gui/DrawStyleManager.md#free-functions-and-macros) | [gui/DrawStyleManager](../src/gui/DrawStyleManager.md) |
| [`GPLATES_GUI_EVENTBLACKOUT_H`](../src/gui/EventBlackout.md#free-functions-and-macros) | [gui/EventBlackout](../src/gui/EventBlackout.md) |
| [`GPLATES_GUI_EXPORTANIMATIONCONTEXT_H`](../src/gui/ExportAnimationContext.md#free-functions-and-macros) | [gui/ExportAnimationContext](../src/gui/ExportAnimationContext.md) |
| [`GPLATES_GUI_EXPORTANIMATIONREGISTRY_H`](../src/gui/ExportAnimationRegistry.md#free-functions-and-macros) | [gui/ExportAnimationRegistry](../src/gui/ExportAnimationRegistry.md) |
| [`GPLATES_GUI_EXPORTANIMATIONSTRATEGY_H`](../src/gui/ExportAnimationStrategy.md#free-functions-and-macros) | [gui/ExportAnimationStrategy](../src/gui/ExportAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTANIMATIONTYPE_H`](../src/gui/ExportAnimationType.md#free-functions-and-macros) | [gui/ExportAnimationType](../src/gui/ExportAnimationType.md) |
| [`GPLATES_GUI_EXPORTCITCOMSRESOLVEDTOPOLOGYSTRATEGY_H`](../src/gui/ExportCitcomsResolvedTopologyAnimationStrategy.md#free-functions-and-macros) | [gui/ExportCitcomsResolvedTopologyAnimationStrategy](../src/gui/ExportCitcomsResolvedTopologyAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTCOREGISTRATIONANIMATIONSTRATEGY_H`](../src/gui/ExportCoRegistrationAnimationStrategy.md#free-functions-and-macros) | [gui/ExportCoRegistrationAnimationStrategy](../src/gui/ExportCoRegistrationAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTDEFORMATIONANIMATIONSTRATEGY_H`](../src/gui/ExportDeformationAnimationStrategy.md#free-functions-and-macros) | [gui/ExportDeformationAnimationStrategy](../src/gui/ExportDeformationAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTFILENAMETEMPLATEVALIDATIONUTILS_H`](../src/gui/ExportFileNameTemplateValidationUtils.md#free-functions-and-macros) | [gui/ExportFileNameTemplateValidationUtils](../src/gui/ExportFileNameTemplateValidationUtils.md) |
| [`GPLATES_GUI_EXPORTFLOWLINEANIMATIONSTRATEGY_H`](../src/gui/ExportFlowlineAnimationStrategy.md#free-functions-and-macros) | [gui/ExportFlowlineAnimationStrategy](../src/gui/ExportFlowlineAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTIMAGEANIMATIONSTRATEGY_H`](../src/gui/ExportImageAnimationStrategy.md#free-functions-and-macros) | [gui/ExportImageAnimationStrategy](../src/gui/ExportImageAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTMOTIONPATHANIMATIONSTRATEGY_H`](../src/gui/ExportMotionPathAnimationStrategy.md#free-functions-and-macros) | [gui/ExportMotionPathAnimationStrategy](../src/gui/ExportMotionPathAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTNETROTATIONANIMATIONSTRATEGY_H`](../src/gui/ExportNetRotationAnimationStrategy.md#free-functions-and-macros) | [gui/ExportNetRotationAnimationStrategy](../src/gui/ExportNetRotationAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTOPTIONSUTILS_H`](../src/gui/ExportOptionsUtils.md#free-functions-and-macros) | [gui/ExportOptionsUtils](../src/gui/ExportOptionsUtils.md) |
| [`GPLATES_GUI_EXPORTRASTERANIMATIONSTRATEGY_H`](../src/gui/ExportRasterAnimationStrategy.md#free-functions-and-macros) | [gui/ExportRasterAnimationStrategy](../src/gui/ExportRasterAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTRECONSTRUCTEDGEOMETRYANIMATIONSTRATEGY_H`](../src/gui/ExportReconstructedGeometryAnimationStrategy.md#free-functions-and-macros) | [gui/ExportReconstructedGeometryAnimationStrategy](../src/gui/ExportReconstructedGeometryAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTRESOLVEDTOPOLOGYANIMATIONSTRATEGY_H`](../src/gui/ExportResolvedTopologyAnimationStrategy.md#free-functions-and-macros) | [gui/ExportResolvedTopologyAnimationStrategy](../src/gui/ExportResolvedTopologyAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTSCALARCOVERAGEANIMATIONSTRATEGY_H`](../src/gui/ExportScalarCoverageAnimationStrategy.md#free-functions-and-macros) | [gui/ExportScalarCoverageAnimationStrategy](../src/gui/ExportScalarCoverageAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTSTAGEROTATIONSTRATEGY_H`](../src/gui/ExportStageRotationAnimationStrategy.md#free-functions-and-macros) | [gui/ExportStageRotationAnimationStrategy](../src/gui/ExportStageRotationAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTSVGANIMATIONSTRATEGY_H`](../src/gui/ExportSvgAnimationStrategy.md#free-functions-and-macros) | [gui/ExportSvgAnimationStrategy](../src/gui/ExportSvgAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTTOTALROTATIONANIMATIONSTRATEGY_H`](../src/gui/ExportTotalRotationAnimationStrategy.md#free-functions-and-macros) | [gui/ExportTotalRotationAnimationStrategy](../src/gui/ExportTotalRotationAnimationStrategy.md) |
| [`GPLATES_GUI_EXPORTVELOCITYANIMATIONSTRATEGY_H`](../src/gui/ExportVelocityAnimationStrategy.md#free-functions-and-macros) | [gui/ExportVelocityAnimationStrategy](../src/gui/ExportVelocityAnimationStrategy.md) |
| [`GPLATES_GUI_EXTERNALSYNCCONTROLLER_H`](../src/gui/ExternalSyncController.md#free-functions-and-macros) | [gui/ExternalSyncController](../src/gui/ExternalSyncController.md) |
| [`GPLATES_GUI_FEATURECOLOURPALETTE_H`](../src/gui/FeatureTypeColourPalette.md#free-functions-and-macros) | [gui/FeatureTypeColourPalette](../src/gui/FeatureTypeColourPalette.md) |
| [`GPLATES_GUI_FEATUREFOCUS_H`](../src/gui/FeatureFocus.md#free-functions-and-macros) | [gui/FeatureFocus](../src/gui/FeatureFocus.md) |
| [`GPLATES_GUI_FEATUREINSPECTIONCANVASTOOLWORKFLOW_H`](../src/gui/FeatureInspectionCanvasToolWorkflow.md#free-functions-and-macros) | [gui/FeatureInspectionCanvasToolWorkflow](../src/gui/FeatureInspectionCanvasToolWorkflow.md) |
| [`GPLATES_GUI_FEATUREPROPERTYTABLEMODEL_H`](../src/gui/FeaturePropertyTableModel.md#free-functions-and-macros) | [gui/FeaturePropertyTableModel](../src/gui/FeaturePropertyTableModel.md) |
| [`GPLATES_GUI_FEATURETABLEMODEL_H`](../src/gui/FeatureTableModel.md#free-functions-and-macros) | [gui/FeatureTableModel](../src/gui/FeatureTableModel.md) |
| [`GPLATES_GUI_FEATUREWEAKREFSEQUENCE_H`](../src/gui/deprecated/FeatureWeakRefSequence.md#free-functions-and-macros) | [gui/deprecated/FeatureWeakRefSequence](../src/gui/deprecated/FeatureWeakRefSequence.md) |
| [`GPLATES_GUI_FEEDBACKOPENGLTOQPAINTER_H`](../src/gui/FeedbackOpenGLToQPainter.md#free-functions-and-macros) | [gui/FeedbackOpenGLToQPainter](../src/gui/FeedbackOpenGLToQPainter.md) |
| [`GPLATES_GUI_FILE_IO_DIRECTORY_CONFIGURATIONS_H`](../src/gui/FileIODirectoryConfigurations.md#free-functions-and-macros) | [gui/FileIODirectoryConfigurations](../src/gui/FileIODirectoryConfigurations.md) |
| [`GPLATES_GUI_FILEIOFEEDBACK_H`](../src/gui/FileIOFeedback.md#free-functions-and-macros) | [gui/FileIOFeedback](../src/gui/FileIOFeedback.md) |
| [`GPLATES_GUI_FULLSCREENMODE_H`](../src/gui/FullScreenMode.md#free-functions-and-macros) | [gui/FullScreenMode](../src/gui/FullScreenMode.md) |
| [`GPLATES_GUI_GENERICCOLOURSCHEME_H`](../src/gui/GenericColourScheme.md#free-functions-and-macros) | [gui/GenericColourScheme](../src/gui/GenericColourScheme.md) |
| [`GPLATES_GUI_GEOMETRYFOCUSHIGHLIGHT_H`](../src/gui/GeometryFocusHighlight.md#free-functions-and-macros) | [gui/GeometryFocusHighlight](../src/gui/GeometryFocusHighlight.md) |
| [`GPLATES_GUI_GLOBE_H`](../src/gui/Globe.md#free-functions-and-macros) | [gui/Globe](../src/gui/Globe.md) |
| [`GPLATES_GUI_GLOBECANVASTOOL_H`](../src/gui/GlobeCanvasTool.md#free-functions-and-macros) | [gui/GlobeCanvasTool](../src/gui/GlobeCanvasTool.md) |
| [`GPLATES_GUI_GLOBECANVASTOOLADAPTER_H`](../src/gui/GlobeCanvasToolAdapter.md#free-functions-and-macros) | [gui/GlobeCanvasToolAdapter](../src/gui/GlobeCanvasToolAdapter.md) |
| [`GPLATES_GUI_GLOBEORIENTATION_H`](../src/gui/GlobeOrientation.md#free-functions-and-macros) | [gui/GlobeOrientation](../src/gui/GlobeOrientation.md) |
| [`GPLATES_GUI_GLOBERENDEREDGEOMETRYLAYERPAINTER_H`](../src/gui/GlobeRenderedGeometryLayerPainter.md#free-functions-and-macros) | [gui/GlobeRenderedGeometryLayerPainter](../src/gui/GlobeRenderedGeometryLayerPainter.md) |
| [`GPLATES_GUI_GLOBERENDEREDGEOMETRYPAINTER_H`](../src/gui/GlobeRenderedGeometryCollectionPainter.md#free-functions-and-macros) | [gui/GlobeRenderedGeometryCollectionPainter](../src/gui/GlobeRenderedGeometryCollectionPainter.md) |
| [`GPLATES_GUI_GLOBEVISIBILITYTESTER_H`](../src/gui/GlobeVisibilityTester.md#free-functions-and-macros) | [gui/GlobeVisibilityTester](../src/gui/GlobeVisibilityTester.md) |
| [`GPLATES_GUI_GMTCOLOURNAMES_H`](../src/gui/GMTColourNames.md#free-functions-and-macros) | [gui/GMTColourNames](../src/gui/GMTColourNames.md) |
| [`GPLATES_GUI_GPLATESAPP_H`](../src/gui/deprecated/GPlatesApp.md#free-functions-and-macros) | [gui/deprecated/GPlatesApp](../src/gui/deprecated/GPlatesApp.md) |
| [`GPLATES_GUI_GPLATESQAPPLICATION_H`](../src/gui/GPlatesQApplication.md#free-functions-and-macros) | [gui/GPlatesQApplication](../src/gui/GPlatesQApplication.md) |
| [`GPLATES_GUI_GRATICULESETTINGS_H`](../src/gui/GraticuleSettings.md#free-functions-and-macros) | [gui/GraticuleSettings](../src/gui/GraticuleSettings.md) |
| [`GPLATES_GUI_GUIDEBUG_H`](../src/gui/GuiDebug.md#free-functions-and-macros) | [gui/GuiDebug](../src/gui/GuiDebug.md) |
| [`GPLATES_GUI_HELLINGERCANVASTOOLWORKFLOW_H`](../src/gui/HellingerCanvasToolWorkflow.md#free-functions-and-macros) | [gui/HellingerCanvasToolWorkflow](../src/gui/HellingerCanvasToolWorkflow.md) |
| [`GPLATES_GUI_HTMLCOLOURNAMES_H`](../src/gui/HTMLColourNames.md#free-functions-and-macros) | [gui/HTMLColourNames](../src/gui/HTMLColourNames.md) |
| [`GPLATES_GUI_IMPORTMENU_H`](../src/gui/ImportMenu.md#free-functions-and-macros) | [gui/ImportMenu](../src/gui/ImportMenu.md) |
| [`GPLATES_GUI_LAYERPAINTER_H`](../src/gui/LayerPainter.md#free-functions-and-macros) | [gui/LayerPainter](../src/gui/LayerPainter.md) |
| [`GPLATES_GUI_LOGFILTERMODEL_H`](../src/gui/LogFilterModel.md#free-functions-and-macros) | [gui/LogFilterModel](../src/gui/LogFilterModel.md) |
| [`GPLATES_GUI_MANAGEFEATURECOLLECTIONSDIALOG_H`](../src/qt-widgets/ManageFeatureCollectionsDialog.md#free-functions-and-macros) | [qt-widgets/ManageFeatureCollectionsDialog](../src/qt-widgets/ManageFeatureCollectionsDialog.md) |
| [`GPLATES_GUI_MAP_H`](../src/gui/Map.md#free-functions-and-macros) | [gui/Map](../src/gui/Map.md) |
| [`GPLATES_GUI_MAPBACKGROUND_H`](../src/gui/MapBackground.md#free-functions-and-macros) | [gui/MapBackground](../src/gui/MapBackground.md) |
| [`GPLATES_GUI_MAPCANVASPAINTER_H`](../src/gui/MapRenderedGeometryLayerPainter.md#free-functions-and-macros) | [gui/MapRenderedGeometryLayerPainter](../src/gui/MapRenderedGeometryLayerPainter.md) |
| [`GPLATES_GUI_MAPCANVASTOOL_H`](../src/gui/MapCanvasTool.md#free-functions-and-macros) | [gui/MapCanvasTool](../src/gui/MapCanvasTool.md) |
| [`GPLATES_GUI_MAPCANVASTOOLADAPTER_H`](../src/gui/MapCanvasToolAdapter.md#free-functions-and-macros) | [gui/MapCanvasToolAdapter](../src/gui/MapCanvasToolAdapter.md) |
| [`GPLATES_GUI_MAPGRID_H`](../src/gui/MapGrid.md#free-functions-and-macros) | [gui/MapGrid](../src/gui/MapGrid.md) |
| [`GPLATES_GUI_MAPPROJECTION_H`](../src/gui/MapProjection.md#free-functions-and-macros) | [gui/MapProjection](../src/gui/MapProjection.md) |
| [`GPLATES_GUI_MAPRENDEREDGEOMETRYCOLLECTIONPAINTER_H`](../src/gui/MapRenderedGeometryCollectionPainter.md#free-functions-and-macros) | [gui/MapRenderedGeometryCollectionPainter](../src/gui/MapRenderedGeometryCollectionPainter.md) |
| [`GPLATES_GUI_MAPTRANSFORM_H`](../src/gui/MapTransform.md#free-functions-and-macros) | [gui/MapTransform](../src/gui/MapTransform.md) |
| [`GPLATES_GUI_MIPMAPPER_H`](../src/gui/Mipmapper.md#free-functions-and-macros) | [gui/Mipmapper](../src/gui/Mipmapper.md) |
| [`GPLATES_GUI_OPAQUESPHERE_H`](../src/gui/OpaqueSphere.md#free-functions-and-macros) | [gui/OpaqueSphere](../src/gui/OpaqueSphere.md) |
| [`GPLATES_GUI_PALETTE_H`](../src/gui/Palette.md#free-functions-and-macros) | [gui/Palette](../src/gui/Palette.md) |
| [`GPLATES_GUI_PLATEIDCOLOURPALETTES_H`](../src/gui/PlateIdColourPalettes.md#free-functions-and-macros) | [gui/PlateIdColourPalettes](../src/gui/PlateIdColourPalettes.md) |
| [`GPLATES_GUI_POLEMANIPULATIONCANVASTOOLWORKFLOW_H`](../src/gui/PoleManipulationCanvasToolWorkflow.md#free-functions-and-macros) | [gui/PoleManipulationCanvasToolWorkflow](../src/gui/PoleManipulationCanvasToolWorkflow.md) |
| [`GPLATES_GUI_PROJECTIONEXCEPTION_H`](../src/gui/ProjectionException.md#free-functions-and-macros) | [gui/ProjectionException](../src/gui/ProjectionException.md) |
| [`GPLATES_GUI_PYTHON_CONFIGURATION_H`](../src/gui/PythonConfiguration.md#free-functions-and-macros) | [gui/PythonConfiguration](../src/gui/PythonConfiguration.md) |
| [`GPLATES_GUI_PYTHON_MANAGER_H`](../src/gui/PythonManager.md#free-functions-and-macros) | [gui/PythonManager](../src/gui/PythonManager.md) |
| [`GPLATES_GUI_PYTHONCONSOLEHISTORY_H`](../src/gui/PythonConsoleHistory.md#free-functions-and-macros) | [gui/PythonConsoleHistory](../src/gui/PythonConsoleHistory.md) |
| [`GPLATES_GUI_RASTERCOLOURPALETTE_H`](../src/gui/RasterColourPalette.md#free-functions-and-macros) | [gui/RasterColourPalette](../src/gui/RasterColourPalette.md) |
| [`GPLATES_GUI_READERRORACCUMULATIONDIALOG_H`](../src/qt-widgets/ReadErrorAccumulationDialog.md#free-functions-and-macros) | [qt-widgets/ReadErrorAccumulationDialog](../src/qt-widgets/ReadErrorAccumulationDialog.md) |
| [`GPLATES_GUI_RENDEREDGEOMETRY_H`](../src/view-operations/RenderedGeometry.md#free-functions-and-macros) | [view-operations/RenderedGeometry](../src/view-operations/RenderedGeometry.md) |
| [`GPLATES_GUI_RENDERSETTINGS_H`](../src/gui/RenderSettings.md#free-functions-and-macros) | [gui/RenderSettings](../src/gui/RenderSettings.md) |
| [`GPLATES_GUI_SCENELIGHTINGPARAMETERS_H`](../src/gui/SceneLightingParameters.md#free-functions-and-macros) | [gui/SceneLightingParameters](../src/gui/SceneLightingParameters.md) |
| [`GPLATES_GUI_SESSIONMENU_H`](../src/gui/SessionMenu.md#free-functions-and-macros) | [gui/SessionMenu](../src/gui/SessionMenu.md) |
| [`GPLATES_GUI_SIMPLEGLOBEORIENTATION_H`](../src/gui/SimpleGlobeOrientation.md#free-functions-and-macros) | [gui/SimpleGlobeOrientation](../src/gui/SimpleGlobeOrientation.md) |
| [`GPLATES_GUI_SINGLECOLOURSCHEME_H`](../src/gui/SingleColourScheme.md#free-functions-and-macros) | [gui/SingleColourScheme](../src/gui/SingleColourScheme.md) |
| [`GPLATES_GUI_SMALLCIRCLECANVASTOOLWORKFLOW_H`](../src/gui/SmallCircleCanvasToolWorkflow.md#free-functions-and-macros) | [gui/SmallCircleCanvasToolWorkflow](../src/gui/SmallCircleCanvasToolWorkflow.md) |
| [`GPLATES_GUI_SPHERICALGRID_H`](../src/gui/SphericalGrid.md#free-functions-and-macros) | [gui/SphericalGrid](../src/gui/SphericalGrid.md) |
| [`GPLATES_GUI_STARS_H`](../src/gui/Stars.md#free-functions-and-macros) | [gui/Stars](../src/gui/Stars.md) |
| [`GPLATES_GUI_SYMBOL_H`](../src/gui/Symbol.md#free-functions-and-macros) | [gui/Symbol](../src/gui/Symbol.md) |
| [`GPLATES_GUI_TEXTOVERLAY_H`](../src/gui/TextOverlay.md#free-functions-and-macros) | [gui/TextOverlay](../src/gui/TextOverlay.md) |
| [`GPLATES_GUI_TEXTOVERLAYSETTINGS_H`](../src/gui/TextOverlaySettings.md#free-functions-and-macros) | [gui/TextOverlaySettings](../src/gui/TextOverlaySettings.md) |
| [`GPLATES_GUI_TOPOLOGY_TOOLS_H`](../src/gui/TopologyTools.md#free-functions-and-macros) | [gui/TopologyTools](../src/gui/TopologyTools.md) |
| [`GPLATES_GUI_TOPOLOGYCANVASTOOLWORKFLOW_H`](../src/gui/TopologyCanvasToolWorkflow.md#free-functions-and-macros) | [gui/TopologyCanvasToolWorkflow](../src/gui/TopologyCanvasToolWorkflow.md) |
| [`GPLATES_GUI_TOPOLOGYSECTIONSCONTAINER_H`](../src/gui/TopologySectionsContainer.md#free-functions-and-macros) | [gui/TopologySectionsContainer](../src/gui/TopologySectionsContainer.md) |
| [`GPLATES_GUI_TOPOLOGYSECTIONSTABLE_H`](../src/gui/TopologySectionsTable.md#free-functions-and-macros) | [gui/TopologySectionsTable](../src/gui/TopologySectionsTable.md) |
| [`GPLATES_GUI_TOPOLOGYSECTIONSTABLECOLUMNS_H`](../src/gui/TopologySectionsTableColumns.md#free-functions-and-macros) | [gui/TopologySectionsTableColumns](../src/gui/TopologySectionsTableColumns.md) |
| [`GPLATES_GUI_TREEWIDGETBUILDER_H`](../src/gui/TreeWidgetBuilder.md#free-functions-and-macros) | [gui/TreeWidgetBuilder](../src/gui/TreeWidgetBuilder.md) |
| [`GPLATES_GUI_TRINKETAREA_H`](../src/gui/TrinketArea.md#free-functions-and-macros) | [gui/TrinketArea](../src/gui/TrinketArea.md) |
| [`GPLATES_GUI_UNSAVEDCHANGESTRACKER_H`](../src/gui/UnsavedChangesTracker.md#free-functions-and-macros) | [gui/UnsavedChangesTracker](../src/gui/UnsavedChangesTracker.md) |
| [`GPLATES_GUI_UTILITIESMENU_H`](../src/gui/UtilitiesMenu.md#free-functions-and-macros) | [gui/UtilitiesMenu](../src/gui/UtilitiesMenu.md) |
| [`GPLATES_GUI_VELOCITYLEGENDOVERLAY_H`](../src/gui/VelocityLegendOverlay.md#free-functions-and-macros) | [gui/VelocityLegendOverlay](../src/gui/VelocityLegendOverlay.md) |
| [`GPLATES_GUI_VELOCITYLEGENDOVERLAYSETTINGS_H`](../src/gui/VelocityLegendOverlaySettings.md#free-functions-and-macros) | [gui/VelocityLegendOverlaySettings](../src/gui/VelocityLegendOverlaySettings.md) |
| [`GPLATES_GUI_VIEWCANVASTOOLWORKFLOW_H`](../src/gui/ViewCanvasToolWorkflow.md#free-functions-and-macros) | [gui/ViewCanvasToolWorkflow](../src/gui/ViewCanvasToolWorkflow.md) |
| [`GPLATES_GUI_VIEWPORTPROJECTION_H`](../src/gui/ViewportProjection.md#free-functions-and-macros) | [gui/ViewportProjection](../src/gui/ViewportProjection.md) |
| [`GPLATES_GUI_VIEWPORTZOOM_H`](../src/gui/ViewportZoom.md#free-functions-and-macros) | [gui/ViewportZoom](../src/gui/ViewportZoom.md) |
| [`GPLATES_GUI_VISUALLAYERSLISTMODEL_H`](../src/gui/VisualLayersListModel.md#free-functions-and-macros) | [gui/VisualLayersListModel](../src/gui/VisualLayersListModel.md) |
| [`GPLATES_GUI_VISUALLAYERSPROXY_H`](../src/gui/VisualLayersProxy.md#free-functions-and-macros) | [gui/VisualLayersProxy](../src/gui/VisualLayersProxy.md) |
| [`GPLATES_MATH_GEOMETRYCROSSING_H`](../src/maths/GeometryCrossing.md#free-functions-and-macros) | [maths/GeometryCrossing](../src/maths/GeometryCrossing.md) |
| [`GPLATES_MATHS_ANGULARDISTANCE_H`](../src/maths/AngularDistance.md#free-functions-and-macros) | [maths/AngularDistance](../src/maths/AngularDistance.md) |
| [`GPLATES_MATHS_ANGULAREXTENT_H`](../src/maths/AngularExtent.md#free-functions-and-macros) | [maths/AngularExtent](../src/maths/AngularExtent.md) |
| [`GPLATES_MATHS_AZIMUTHALEQUALAREAPROJECTION_H`](../src/maths/AzimuthalEqualAreaProjection.md#free-functions-and-macros) | [maths/AzimuthalEqualAreaProjection](../src/maths/AzimuthalEqualAreaProjection.md) |
| [`GPLATES_MATHS_CENTROID_H`](../src/maths/Centroid.md#free-functions-and-macros) | [maths/Centroid](../src/maths/Centroid.md) |
| [`GPLATES_MATHS_CONSTGEOMETRYONSPHEREVISITOR_H`](../src/maths/ConstGeometryOnSphereVisitor.md#free-functions-and-macros) | [maths/ConstGeometryOnSphereVisitor](../src/maths/ConstGeometryOnSphereVisitor.md) |
| [`GPLATES_MATHS_CUBECOORDINATEFRAME_H`](../src/maths/CubeCoordinateFrame.md#free-functions-and-macros) | [maths/CubeCoordinateFrame](../src/maths/CubeCoordinateFrame.md) |
| [`GPLATES_MATHS_CUBEQUADTREE_H`](../src/maths/CubeQuadTree.md#free-functions-and-macros) | [maths/CubeQuadTree](../src/maths/CubeQuadTree.md) |
| [`GPLATES_MATHS_CUBEQUADTREELOCATION_H`](../src/maths/CubeQuadTreeLocation.md#free-functions-and-macros) | [maths/CubeQuadTreeLocation](../src/maths/CubeQuadTreeLocation.md) |
| [`GPLATES_MATHS_CUBEQUADTREEPARTITION_H`](../src/maths/CubeQuadTreePartition.md#free-functions-and-macros) | [maths/CubeQuadTreePartition](../src/maths/CubeQuadTreePartition.md) |
| [`GPLATES_MATHS_CUBEQUADTREEPARTITIONUTILS_H`](../src/maths/CubeQuadTreePartitionUtils.md#free-functions-and-macros) | [maths/CubeQuadTreePartitionUtils](../src/maths/CubeQuadTreePartitionUtils.md) |
| [`GPLATES_MATHS_DATELINEWRAPPER_H`](../src/maths/DateLineWrapper.md#free-functions-and-macros) | [maths/DateLineWrapper](../src/maths/DateLineWrapper.md) |
| [`GPLATES_MATHS_ELLIPSEGENERATOR_H`](../src/maths/EllipseGenerator.md#free-functions-and-macros) | [maths/EllipseGenerator](../src/maths/EllipseGenerator.md) |
| [`GPLATES_MATHS_FINITEROTATION_H`](../src/maths/FiniteRotation.md#free-functions-and-macros) | [maths/FiniteRotation](../src/maths/FiniteRotation.md) |
| [`GPLATES_MATHS_FINITEROTATIONSNAPSHOTTABLE_H`](../src/maths/FiniteRotationSnapshotTable.md#free-functions-and-macros) | [maths/FiniteRotationSnapshotTable](../src/maths/FiniteRotationSnapshotTable.md) |
| [`GPLATES_MATHS_GENERATEPOINTS_H`](../src/maths/GeneratePoints.md#free-functions-and-macros) | [maths/GeneratePoints](../src/maths/GeneratePoints.md) |
| [`GPLATES_MATHS_GENERICVECTOROPS3D_H`](../src/maths/GenericVectorOps3D.md#free-functions-and-macros) | [maths/GenericVectorOps3D](../src/maths/GenericVectorOps3D.md) |
| [`GPLATES_MATHS_GEOMETRYDISTANCE_H`](../src/maths/GeometryDistance.md#free-functions-and-macros) | [maths/GeometryDistance](../src/maths/GeometryDistance.md) |
| [`GPLATES_MATHS_GEOMETRYFORWARDDECLARATIONS_H`](../src/maths/GeometryForwardDeclarations.md#free-functions-and-macros) | [maths/GeometryForwardDeclarations](../src/maths/GeometryForwardDeclarations.md) |
| [`GPLATES_MATHS_GEOMETRYINTERPOLATION_H`](../src/maths/GeometryInterpolation.md#free-functions-and-macros) | [maths/GeometryInterpolation](../src/maths/GeometryInterpolation.md) |
| [`GPLATES_MATHS_GEOMETRYINTERSECT_H`](../src/maths/GeometryIntersect.md#free-functions-and-macros) | [maths/GeometryIntersect](../src/maths/GeometryIntersect.md) |
| [`GPLATES_MATHS_GEOMETRYONSPHERE_H`](../src/maths/GeometryOnSphere.md#free-functions-and-macros) | [maths/GeometryOnSphere](../src/maths/GeometryOnSphere.md) |
| [`GPLATES_MATHS_GEOMETRYTYPE_H`](../src/maths/GeometryType.md#free-functions-and-macros) | [maths/GeometryType](../src/maths/GeometryType.md) |
| [`GPLATES_MATHS_GNOMONICPROJECTION_H`](../src/maths/GnomonicProjection.md#free-functions-and-macros) | [maths/GnomonicProjection](../src/maths/GnomonicProjection.md) |
| [`GPLATES_MATHS_GREATCIRCLE_H`](../src/maths/GreatCircle.md#free-functions-and-macros) | [maths/GreatCircle](../src/maths/GreatCircle.md) |
| [`GPLATES_MATHS_GREATCIRCLEARC_H`](../src/maths/GreatCircleArc.md#free-functions-and-macros) | [maths/GreatCircleArc](../src/maths/GreatCircleArc.md) |
| [`GPLATES_MATHS_INDETERMINATEARCROTATIONAXISEXCEPTION_H`](../src/maths/IndeterminateArcRotationAxisException.md#free-functions-and-macros) | [maths/IndeterminateArcRotationAxisException](../src/maths/IndeterminateArcRotationAxisException.md) |
| [`GPLATES_MATHS_INVALIDLATLONCOORDINATEEXCEPTION_H`](../src/maths/InvalidLatLonCoordinateException.md#free-functions-and-macros) | [maths/InvalidLatLonCoordinateException](../src/maths/InvalidLatLonCoordinateException.md) |
| [`GPLATES_MATHS_INVALIDLATLONEXCEPTION_H`](../src/maths/InvalidLatLonException.md#free-functions-and-macros) | [maths/InvalidLatLonException](../src/maths/InvalidLatLonException.md) |
| [`GPLATES_MATHS_INVALIDPOLYLINECONTAINSONLYONEPOINTEXCEPTION_H`](../src/maths/InvalidPolylineContainsOnlyOnePointException.md#free-functions-and-macros) | [maths/InvalidPolylineContainsOnlyOnePointException](../src/maths/InvalidPolylineContainsOnlyOnePointException.md) |
| [`GPLATES_MATHS_INVALIDPOLYLINECONTAINSZEROPOINTSEXCEPTION_H`](../src/maths/InvalidPolylineContainsZeroPointsException.md#free-functions-and-macros) | [maths/InvalidPolylineContainsZeroPointsException](../src/maths/InvalidPolylineContainsZeroPointsException.md) |
| [`GPLATES_MATHS_LATLONPOINT_H`](../src/maths/LatLonPoint.md#free-functions-and-macros) | [maths/LatLonPoint](../src/maths/LatLonPoint.md) |
| [`GPLATES_MATHS_MATHUTILS_H`](../src/maths/MathsUtils.md#free-functions-and-macros) | [maths/MathsUtils](../src/maths/MathsUtils.md) |
| [`GPLATES_MATHS_MULTIPOINTONSPHERE_H`](../src/maths/MultiPointOnSphere.md#free-functions-and-macros) | [maths/MultiPointOnSphere](../src/maths/MultiPointOnSphere.md) |
| [`GPLATES_MATHS_MULTIPOINTPROXIMITYHITDETAIL_H`](../src/maths/MultiPointProximityHitDetail.md#free-functions-and-macros) | [maths/MultiPointProximityHitDetail](../src/maths/MultiPointProximityHitDetail.md) |
| [`GPLATES_MATHS_POINTINPOLYGON_H`](../src/maths/PointInPolygon.md#free-functions-and-macros) | [maths/PointInPolygon](../src/maths/PointInPolygon.md) |
| [`GPLATES_MATHS_POINTLIESONGREATCIRCLEARC_H`](../src/maths/PointLiesOnGreatCircleArc.md#free-functions-and-macros) | [maths/PointLiesOnGreatCircleArc](../src/maths/PointLiesOnGreatCircleArc.md) |
| [`GPLATES_MATHS_POINTONSPHERE_H`](../src/maths/PointOnSphere.md#free-functions-and-macros) | [maths/PointOnSphere](../src/maths/PointOnSphere.md) |
| [`GPLATES_MATHS_POINTPROXIMITYHITDETAIL_H`](../src/maths/PointProximityHitDetail.md#free-functions-and-macros) | [maths/PointProximityHitDetail](../src/maths/PointProximityHitDetail.md) |
| [`GPLATES_MATHS_POLYGONFAN_H`](../src/maths/PolygonFan.md#free-functions-and-macros) | [maths/PolygonFan](../src/maths/PolygonFan.md) |
| [`GPLATES_MATHS_POLYGONINTERSECTIONS_H`](../src/maths/PolygonPartitioner.md#free-functions-and-macros) | [maths/PolygonPartitioner](../src/maths/PolygonPartitioner.md) |
| [`GPLATES_MATHS_POLYGONMESH_H`](../src/maths/PolygonMesh.md#free-functions-and-macros) | [maths/PolygonMesh](../src/maths/PolygonMesh.md) |
| [`GPLATES_MATHS_POLYGONONSPHERE_H`](../src/maths/PolygonOnSphere.md#free-functions-and-macros) | [maths/PolygonOnSphere](../src/maths/PolygonOnSphere.md) |
| [`GPLATES_MATHS_POLYGONORIENTATION_H`](../src/maths/PolygonOrientation.md#free-functions-and-macros) | [maths/PolygonOrientation](../src/maths/PolygonOrientation.md) |
| [`GPLATES_MATHS_POLYGONPROXIMITYHITDETAIL_H`](../src/maths/PolygonProximityHitDetail.md#free-functions-and-macros) | [maths/PolygonProximityHitDetail](../src/maths/PolygonProximityHitDetail.md) |
| [`GPLATES_MATHS_POLYGREATCIRCLEARCBOUNDINGTREE_H`](../src/maths/PolyGreatCircleArcBoundingTree.md#free-functions-and-macros) | [maths/PolyGreatCircleArcBoundingTree](../src/maths/PolyGreatCircleArcBoundingTree.md) |
| [`GPLATES_MATHS_POLYLINEEQUIVALENCEPREDICATES_H`](../src/maths/PolylineEquivalencePredicates.md#free-functions-and-macros) | [maths/PolylineEquivalencePredicates](../src/maths/PolylineEquivalencePredicates.md) |
| [`GPLATES_MATHS_POLYLINEINTERSECTIONS_H`](../src/maths/PolylineIntersections.md#free-functions-and-macros) | [maths/PolylineIntersections](../src/maths/PolylineIntersections.md) |
| [`GPLATES_MATHS_POLYLINEONSPHERE_H`](../src/maths/PolylineOnSphere.md#free-functions-and-macros) | [maths/PolylineOnSphere](../src/maths/PolylineOnSphere.md) |
| [`GPLATES_MATHS_POLYLINEPROXIMITYHITDETAIL_H`](../src/maths/PolylineProximityHitDetail.md#free-functions-and-macros) | [maths/PolylineProximityHitDetail](../src/maths/PolylineProximityHitDetail.md) |
| [`GPLATES_MATHS_PROXIMITYCRITERIA_H`](../src/maths/ProximityCriteria.md#free-functions-and-macros) | [maths/ProximityCriteria](../src/maths/ProximityCriteria.md) |
| [`GPLATES_MATHS_PROXIMITYHITDETAIL_H`](../src/maths/ProximityHitDetail.md#free-functions-and-macros) | [maths/ProximityHitDetail](../src/maths/ProximityHitDetail.md) |
| [`GPLATES_MATHS_PROXIMITYHITDETAILVISITOR_H`](../src/maths/ProximityHitDetailVisitor.md#free-functions-and-macros) | [maths/ProximityHitDetailVisitor](../src/maths/ProximityHitDetailVisitor.md) |
| [`GPLATES_MATHS_REAL_H`](../src/maths/Real.md#free-functions-and-macros) | [maths/Real](../src/maths/Real.md) |
| [`GPLATES_MATHS_ROTATION_H`](../src/maths/Rotation.md#free-functions-and-macros) | [maths/Rotation](../src/maths/Rotation.md) |
| [`GPLATES_MATHS_SMALLCIRCLEARC_H`](../src/maths/SmallCircleArc.md#free-functions-and-macros) | [maths/SmallCircleArc](../src/maths/SmallCircleArc.md) |
| [`GPLATES_MATHS_SMALLCIRCLEBOUNDS_H`](../src/maths/SmallCircleBounds.md#free-functions-and-macros) | [maths/SmallCircleBounds](../src/maths/SmallCircleBounds.md) |
| [`GPLATES_MATHS_SMALLCIRCLECOVERAGEMESH_H`](../src/maths/SmallCircleCoverageMesh.md#free-functions-and-macros) | [maths/SmallCircleCoverageMesh](../src/maths/SmallCircleCoverageMesh.md) |
| [`GPLATES_MATHS_SMALLCIRCLEPROXIMITYHITDETAIL_H`](../src/maths/SmallCircleProximityHitDetail.md#free-functions-and-macros) | [maths/SmallCircleProximityHitDetail](../src/maths/SmallCircleProximityHitDetail.md) |
| [`GPLATES_MATHS_SPHERICALAREA_H`](../src/maths/SphericalArea.md#free-functions-and-macros) | [maths/SphericalArea](../src/maths/SphericalArea.md) |
| [`GPLATES_MATHS_SPHERICALSUBDIVISION_H`](../src/maths/SphericalSubdivision.md#free-functions-and-macros) | [maths/SphericalSubdivision](../src/maths/SphericalSubdivision.md) |
| [`GPLATES_MATHS_STAGEROTATION_H`](../src/maths/deprecated/StageRotation.md#free-functions-and-macros) | [maths/deprecated/StageRotation](../src/maths/deprecated/StageRotation.md) |
| [`GPLATES_MATHS_TRAILINGLATLONCOORDINATEEXCEPTION_H`](../src/maths/TrailingLatLonCoordinateException.md#free-functions-and-macros) | [maths/TrailingLatLonCoordinateException](../src/maths/TrailingLatLonCoordinateException.md) |
| [`GPLATES_MATHS_TYPES_H`](../src/maths/types.md#free-functions-and-macros) | [maths/types](../src/maths/types.md) |
| [`GPLATES_MATHS_UNABLETOEXTENDPOINTLIKEARCEXCEPTION_H`](../src/maths/UnableToExtendPointlikeArcException.md#free-functions-and-macros) | [maths/UnableToExtendPointlikeArcException](../src/maths/UnableToExtendPointlikeArcException.md) |
| [`GPLATES_MATHS_UNABLETOINTERSECTEQUIVALENTGREATCIRCLESEXCEPTION_H`](../src/maths/UnableToIntersectEquivalentGreatCirclesException.md#free-functions-and-macros) | [maths/UnableToIntersectEquivalentGreatCirclesException](../src/maths/UnableToIntersectEquivalentGreatCirclesException.md) |
| [`GPLATES_MATHS_UNABLETONORMALILEZEROVECTOREXCEPTION_H`](../src/maths/UnableToNormaliseZeroVectorException.md#free-functions-and-macros) | [maths/UnableToNormaliseZeroVectorException](../src/maths/UnableToNormaliseZeroVectorException.md) |
| [`GPLATES_MATHS_UNITQUATERNION3D_H`](../src/maths/UnitQuaternion3D.md#free-functions-and-macros) | [maths/UnitQuaternion3D](../src/maths/UnitQuaternion3D.md) |
| [`GPLATES_MODEL_BASICHANDLE_H`](../src/model/BasicHandle.md#free-functions-and-macros) | [model/BasicHandle](../src/model/BasicHandle.md) |
| [`GPLATES_MODEL_BASICREVISION_H`](../src/model/BasicRevision.md#free-functions-and-macros) | [model/BasicRevision](../src/model/BasicRevision.md) |
| [`GPLATES_MODEL_CHANGESETHANDLE_H`](../src/model/ChangesetHandle.md#free-functions-and-macros) | [model/ChangesetHandle](../src/model/ChangesetHandle.md) |
| [`GPLATES_MODEL_DCMETADATA_H`](../src/model/Metadata.md#free-functions-and-macros) | [model/Metadata](../src/model/Metadata.md) |
| [`GPLATES_MODEL_FEATURECOLLECTIONHANDLE_H`](../src/model/FeatureCollectionHandle.md#free-functions-and-macros) | [model/FeatureCollectionHandle](../src/model/FeatureCollectionHandle.md) |
| [`GPLATES_MODEL_FEATURECOLLECTIONREVISION_H`](../src/model/FeatureCollectionRevision.md#free-functions-and-macros) | [model/FeatureCollectionRevision](../src/model/FeatureCollectionRevision.md) |
| [`GPLATES_MODEL_FEATUREHANDLE_H`](../src/model/FeatureHandle.md#free-functions-and-macros) | [model/FeatureHandle](../src/model/FeatureHandle.md) |
| [`GPLATES_MODEL_FEATUREHANDLEWEAKREFBACKINSERTER_H`](../src/model/FeatureHandleWeakRefBackInserter.md#free-functions-and-macros) | [model/FeatureHandleWeakRefBackInserter](../src/model/FeatureHandleWeakRefBackInserter.md) |
| [`GPLATES_MODEL_FEATUREID_H`](../src/model/FeatureId.md#free-functions-and-macros) | [model/FeatureId](../src/model/FeatureId.md) |
| [`GPLATES_MODEL_FEATUREREVISION_H`](../src/model/FeatureRevision.md#free-functions-and-macros) | [model/FeatureRevision](../src/model/FeatureRevision.md) |
| [`GPLATES_MODEL_FEATURESTOREROOTHANDLE_H`](../src/model/FeatureStoreRootHandle.md#free-functions-and-macros) | [model/FeatureStoreRootHandle](../src/model/FeatureStoreRootHandle.md) |
| [`GPLATES_MODEL_FEATURESTOREROOTREVISION_H`](../src/model/FeatureStoreRootRevision.md#free-functions-and-macros) | [model/FeatureStoreRootRevision](../src/model/FeatureStoreRootRevision.md) |
| [`GPLATES_MODEL_FEATURETYPE_H`](../src/model/FeatureType.md#free-functions-and-macros) | [model/FeatureType](../src/model/FeatureType.md) |
| [`GPLATES_MODEL_FEATUREVISITOR_H`](../src/model/FeatureVisitor.md#free-functions-and-macros) | [model/FeatureVisitor](../src/model/FeatureVisitor.md) |
| [`GPLATES_MODEL_GPGIM_H`](../src/model/Gpgim.md#free-functions-and-macros) | [model/Gpgim](../src/model/Gpgim.md) |
| [`GPLATES_MODEL_GPGIMENUMERATIONTYPE_H`](../src/model/GpgimEnumerationType.md#free-functions-and-macros) | [model/GpgimEnumerationType](../src/model/GpgimEnumerationType.md) |
| [`GPLATES_MODEL_GPGIMFEATURECLASS_H`](../src/model/GpgimFeatureClass.md#free-functions-and-macros) | [model/GpgimFeatureClass](../src/model/GpgimFeatureClass.md) |
| [`GPLATES_MODEL_GPGIMINITIALISATIONEXCEPTION_H`](../src/model/GpgimInitialisationException.md#free-functions-and-macros) | [model/GpgimInitialisationException](../src/model/GpgimInitialisationException.md) |
| [`GPLATES_MODEL_GPGIMPROPERTY_H`](../src/model/GpgimProperty.md#free-functions-and-macros) | [model/GpgimProperty](../src/model/GpgimProperty.md) |
| [`GPLATES_MODEL_GPGIMSTRUCTURALTYPE_H`](../src/model/GpgimStructuralType.md#free-functions-and-macros) | [model/GpgimStructuralType](../src/model/GpgimStructuralType.md) |
| [`GPLATES_MODEL_GPGIMTEMPLATESTRUCTURALTYPE_H`](../src/model/GpgimTemplateStructuralType.md#free-functions-and-macros) | [model/GpgimTemplateStructuralType](../src/model/GpgimTemplateStructuralType.md) |
| [`GPLATES_MODEL_GPGIMVERSION_H`](../src/model/GpgimVersion.md#free-functions-and-macros) | [model/GpgimVersion](../src/model/GpgimVersion.md) |
| [`GPLATES_MODEL_HANDLETRAITS_H`](../src/model/HandleTraits.md#free-functions-and-macros) | [model/HandleTraits](../src/model/HandleTraits.md) |
| [`GPLATES_MODEL_IDTYPEGENERATOR_H`](../src/model/IdTypeGenerator.md#free-functions-and-macros) | [model/IdTypeGenerator](../src/model/IdTypeGenerator.md) |
| [`GPLATES_MODEL_MODEL_H`](../src/model/Model.md#free-functions-and-macros) | [model/Model](../src/model/Model.md) |
| [`GPLATES_MODEL_MODELINTERFACE_H`](../src/model/ModelInterface.md#free-functions-and-macros) | [model/ModelInterface](../src/model/ModelInterface.md) |
| [`GPLATES_MODEL_MODELUTILS_H`](../src/model/ModelUtils.md#free-functions-and-macros) | [model/ModelUtils](../src/model/ModelUtils.md) |
| [`GPLATES_MODEL_NOTIFICATIONGUARD_H`](../src/model/NotificationGuard.md#free-functions-and-macros) | [model/NotificationGuard](../src/model/NotificationGuard.md) |
| [`GPLATES_MODEL_PROPERTYNAME_H`](../src/model/PropertyName.md#free-functions-and-macros) | [model/PropertyName](../src/model/PropertyName.md) |
| [`GPLATES_MODEL_PROPERTYVALUE_H`](../src/model/PropertyValue.md#free-functions-and-macros) | [model/PropertyValue](../src/model/PropertyValue.md) |
| [`GPLATES_MODEL_QUALIFIEDXMLNAME_H`](../src/model/QualifiedXmlName.md#free-functions-and-macros) | [model/QualifiedXmlName](../src/model/QualifiedXmlName.md) |
| [`GPLATES_MODEL_REVISIONAWAREITERATOR_H`](../src/model/RevisionAwareIterator.md#free-functions-and-macros) | [model/RevisionAwareIterator](../src/model/RevisionAwareIterator.md) |
| [`GPLATES_MODEL_REVISIONID_H`](../src/model/RevisionId.md#free-functions-and-macros) | [model/RevisionId](../src/model/RevisionId.md) |
| [`GPLATES_MODEL_STRINGCONTENTTYPEGENERATOR_H`](../src/model/StringContentTypeGenerator.md#free-functions-and-macros) | [model/StringContentTypeGenerator](../src/model/StringContentTypeGenerator.md) |
| [`GPLATES_MODEL_STRINGSETSINGLETONS_H`](../src/model/StringSetSingletons.md#free-functions-and-macros) | [model/StringSetSingletons](../src/model/StringSetSingletons.md) |
| [`GPLATES_MODEL_TOPLEVELPROPERTY_H`](../src/model/TopLevelProperty.md#free-functions-and-macros) | [model/TopLevelProperty](../src/model/TopLevelProperty.md) |
| [`GPLATES_MODEL_TOPLEVELPROPERTYINLINE_H`](../src/model/TopLevelPropertyInline.md#free-functions-and-macros) | [model/TopLevelPropertyInline](../src/model/TopLevelPropertyInline.md) |
| [`GPLATES_MODEL_TOPLEVELPROPERTYREF_H`](../src/model/TopLevelPropertyRef.md#free-functions-and-macros) | [model/TopLevelPropertyRef](../src/model/TopLevelPropertyRef.md) |
| [`GPLATES_MODEL_TRANSCRIBEQUALIFIEDXMLNAME_H`](../src/model/TranscribeQualifiedXmlName.md#free-functions-and-macros) | [model/TranscribeQualifiedXmlName](../src/model/TranscribeQualifiedXmlName.md) |
| [`GPLATES_MODEL_TRANSCRIBESTRINGCONTENTTYPEGENERATOR_H`](../src/model/TranscribeStringContentTypeGenerator.md#free-functions-and-macros) | [model/TranscribeStringContentTypeGenerator](../src/model/TranscribeStringContentTypeGenerator.md) |
| [`GPLATES_MODEL_TYPES_H`](../src/model/types.md#free-functions-and-macros) | [model/types](../src/model/types.md) |
| [`GPLATES_MODEL_WEAKOBSERVER_H`](../src/model/WeakObserver.md#free-functions-and-macros) | [model/WeakObserver](../src/model/WeakObserver.md) |
| [`GPLATES_MODEL_WEAKOBSERVERPUBLISHER_H`](../src/model/WeakObserverPublisher.md#free-functions-and-macros) | [model/WeakObserverPublisher](../src/model/WeakObserverPublisher.md) |
| [`GPLATES_MODEL_WEAKOBSERVERVISITOR_H`](../src/model/WeakObserverVisitor.md#free-functions-and-macros) | [model/WeakObserverVisitor](../src/model/WeakObserverVisitor.md) |
| [`GPLATES_MODEL_WEAKREFERENCE_H`](../src/model/WeakReference.md#free-functions-and-macros) | [model/WeakReference](../src/model/WeakReference.md) |
| [`GPLATES_MODEL_WEAKREFERENCECALLBACK_H`](../src/model/WeakReferenceCallback.md#free-functions-and-macros) | [model/WeakReferenceCallback](../src/model/WeakReferenceCallback.md) |
| [`GPLATES_MODEL_WEAKREFERENCEVISITOR_H`](../src/model/WeakReferenceVisitors.md#free-functions-and-macros) | [model/WeakReferenceVisitors](../src/model/WeakReferenceVisitors.md) |
| [`GPLATES_MODEL_XMLATTRIBUTENAME_H`](../src/model/XmlAttributeName.md#free-functions-and-macros) | [model/XmlAttributeName](../src/model/XmlAttributeName.md) |
| [`GPLATES_MODEL_XMLATTRIBUTEVALUE_H`](../src/model/XmlAttributeValue.md#free-functions-and-macros) | [model/XmlAttributeValue](../src/model/XmlAttributeValue.md) |
| [`GPLATES_MODEL_XMLELEMENTNAME_H`](../src/model/XmlElementName.md#free-functions-and-macros) | [model/XmlElementName](../src/model/XmlElementName.md) |
| [`GPLATES_MODEL_XMLNODE_H`](../src/model/XmlNode.md#free-functions-and-macros) | [model/XmlNode](../src/model/XmlNode.md) |
| [`GPLATES_MODEL_XMLNODEUTILS_H`](../src/model/XmlNodeUtils.md#free-functions-and-macros) | [model/XmlNodeUtils](../src/model/XmlNodeUtils.md) |
| [`GPLATES_OPENGL_GLAGEGRIDMASKSOURCE_H`](../src/opengl/GLAgeGridMaskSource.md#free-functions-and-macros) | [opengl/GLAgeGridMaskSource](../src/opengl/GLAgeGridMaskSource.md) |
| [`GPLATES_OPENGL_GLBUFFER_H`](../src/opengl/GLBuffer.md#free-functions-and-macros) | [opengl/GLBuffer](../src/opengl/GLBuffer.md) |
| [`GPLATES_OPENGL_GLBUFFERIMPL_H`](../src/opengl/GLBufferImpl.md#free-functions-and-macros) | [opengl/GLBufferImpl](../src/opengl/GLBufferImpl.md) |
| [`GPLATES_OPENGL_GLBUFFEROBJECT_H`](../src/opengl/GLBufferObject.md#free-functions-and-macros) | [opengl/GLBufferObject](../src/opengl/GLBufferObject.md) |
| [`GPLATES_OPENGL_GLCAPABILITIES_H`](../src/opengl/GLCapabilities.md#free-functions-and-macros) | [opengl/GLCapabilities](../src/opengl/GLCapabilities.md) |
| [`GPLATES_OPENGL_GLCOMPILEDDRAWSTATE_H`](../src/opengl/GLCompiledDrawState.md#free-functions-and-macros) | [opengl/GLCompiledDrawState](../src/opengl/GLCompiledDrawState.md) |
| [`GPLATES_OPENGL_GLCONTEXT_H`](../src/opengl/GLContext.md#free-functions-and-macros) | [opengl/GLContext](../src/opengl/GLContext.md) |
| [`GPLATES_OPENGL_GLCONTEXTIMPL_H`](../src/opengl/GLContextImpl.md#free-functions-and-macros) | [opengl/GLContextImpl](../src/opengl/GLContextImpl.md) |
| [`GPLATES_OPENGL_GLCUBEMESHGENERATOR_H`](../src/opengl/GLCubeMeshGenerator.md#free-functions-and-macros) | [opengl/GLCubeMeshGenerator](../src/opengl/GLCubeMeshGenerator.md) |
| [`GPLATES_OPENGL_GLCUBESUBDIVISION_H`](../src/opengl/GLCubeSubdivision.md#free-functions-and-macros) | [opengl/GLCubeSubdivision](../src/opengl/GLCubeSubdivision.md) |
| [`GPLATES_OPENGL_GLCUBESUBDIVISIONCACHE_H`](../src/opengl/GLCubeSubdivisionCache.md#free-functions-and-macros) | [opengl/GLCubeSubdivisionCache](../src/opengl/GLCubeSubdivisionCache.md) |
| [`GPLATES_OPENGL_GLDATARASTERSOURCE_H`](../src/opengl/GLDataRasterSource.md#free-functions-and-macros) | [opengl/GLDataRasterSource](../src/opengl/GLDataRasterSource.md) |
| [`GPLATES_OPENGL_GLDEPTHRANGE_H`](../src/opengl/GLDepthRange.md#free-functions-and-macros) | [opengl/GLDepthRange](../src/opengl/GLDepthRange.md) |
| [`GPLATES_OPENGL_GLFILLEDPOLYGONSGLOBEVIEW_H`](../src/opengl/GLFilledPolygonsGlobeView.md#free-functions-and-macros) | [opengl/GLFilledPolygonsGlobeView](../src/opengl/GLFilledPolygonsGlobeView.md) |
| [`GPLATES_OPENGL_GLFILLEDPOLYGONSMAPVIEW_H`](../src/opengl/GLFilledPolygonsMapView.md#free-functions-and-macros) | [opengl/GLFilledPolygonsMapView](../src/opengl/GLFilledPolygonsMapView.md) |
| [`GPLATES_OPENGL_GLFRAMEBUFFEROBJECT_H`](../src/opengl/GLFrameBufferObject.md#free-functions-and-macros) | [opengl/GLFrameBufferObject](../src/opengl/GLFrameBufferObject.md) |
| [`GPLATES_OPENGL_GLFRUSTUM_H`](../src/opengl/GLFrustum.md#free-functions-and-macros) | [opengl/GLFrustum](../src/opengl/GLFrustum.md) |
| [`GPLATES_OPENGL_GLIMAGEUTILS_H`](../src/opengl/GLImageUtils.md#free-functions-and-macros) | [opengl/GLImageUtils](../src/opengl/GLImageUtils.md) |
| [`GPLATES_OPENGL_GLINTERSECT_H`](../src/opengl/GLIntersect.md#free-functions-and-macros) | [opengl/GLIntersect](../src/opengl/GLIntersect.md) |
| [`GPLATES_OPENGL_GLINTERSECTPRIMITIVES_H`](../src/opengl/GLIntersectPrimitives.md#free-functions-and-macros) | [opengl/GLIntersectPrimitives](../src/opengl/GLIntersectPrimitives.md) |
| [`GPLATES_OPENGL_GLLIGHT_H`](../src/opengl/GLLight.md#free-functions-and-macros) | [opengl/GLLight](../src/opengl/GLLight.md) |
| [`GPLATES_OPENGL_GLMAPCUBEMESHGENERATOR_H`](../src/opengl/GLMapCubeMeshGenerator.md#free-functions-and-macros) | [opengl/GLMapCubeMeshGenerator](../src/opengl/GLMapCubeMeshGenerator.md) |
| [`GPLATES_OPENGL_GLMATRIX_H`](../src/opengl/GLMatrix.md#free-functions-and-macros) | [opengl/GLMatrix](../src/opengl/GLMatrix.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONCUBEMESH_H`](../src/opengl/GLMultiResolutionCubeMesh.md#free-functions-and-macros) | [opengl/GLMultiResolutionCubeMesh](../src/opengl/GLMultiResolutionCubeMesh.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONCUBERASTER_H`](../src/opengl/GLMultiResolutionCubeRaster.md#free-functions-and-macros) | [opengl/GLMultiResolutionCubeRaster](../src/opengl/GLMultiResolutionCubeRaster.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONCUBERASTERINTERFACE_H`](../src/opengl/GLMultiResolutionCubeRasterInterface.md#free-functions-and-macros) | [opengl/GLMultiResolutionCubeRasterInterface](../src/opengl/GLMultiResolutionCubeRasterInterface.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONCUBERECONSTRUCTEDRASTER_H`](../src/opengl/GLMultiResolutionCubeReconstructedRaster.md#free-functions-and-macros) | [opengl/GLMultiResolutionCubeReconstructedRaster](../src/opengl/GLMultiResolutionCubeReconstructedRaster.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONMAPCUBEMESH_H`](../src/opengl/GLMultiResolutionMapCubeMesh.md#free-functions-and-macros) | [opengl/GLMultiResolutionMapCubeMesh](../src/opengl/GLMultiResolutionMapCubeMesh.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONRASTER_H`](../src/opengl/GLMultiResolutionRaster.md#free-functions-and-macros) | [opengl/GLMultiResolutionRaster](../src/opengl/GLMultiResolutionRaster.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONRASTERINTERFACE_H`](../src/opengl/GLMultiResolutionRasterInterface.md#free-functions-and-macros) | [opengl/GLMultiResolutionRasterInterface](../src/opengl/GLMultiResolutionRasterInterface.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONRASTERMAPVIEW_H`](../src/opengl/GLMultiResolutionRasterMapView.md#free-functions-and-macros) | [opengl/GLMultiResolutionRasterMapView](../src/opengl/GLMultiResolutionRasterMapView.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONRASTERSOURCE_H`](../src/opengl/GLMultiResolutionRasterSource.md#free-functions-and-macros) | [opengl/GLMultiResolutionRasterSource](../src/opengl/GLMultiResolutionRasterSource.md) |
| [`GPLATES_OPENGL_GLMULTIRESOLUTIONSTATICPOLYGONRECONSTRUCTEDRASTER_H`](../src/opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md#free-functions-and-macros) | [opengl/GLMultiResolutionStaticPolygonReconstructedRaster](../src/opengl/GLMultiResolutionStaticPolygonReconstructedRaster.md) |
| [`GPLATES_OPENGL_GLNORMALMAPSOURCE_H`](../src/opengl/GLNormalMapSource.md#free-functions-and-macros) | [opengl/GLNormalMapSource](../src/opengl/GLNormalMapSource.md) |
| [`GPLATES_OPENGL_GLOBJECT_H`](../src/opengl/GLObject.md#free-functions-and-macros) | [opengl/GLObject](../src/opengl/GLObject.md) |
| [`GPLATES_OPENGL_GLOBJECTRESOURCE_H`](../src/opengl/GLObjectResource.md#free-functions-and-macros) | [opengl/GLObjectResource](../src/opengl/GLObjectResource.md) |
| [`GPLATES_OPENGL_GLOBJECTRESOURCEMANAGER_H`](../src/opengl/GLObjectResourceManager.md#free-functions-and-macros) | [opengl/GLObjectResourceManager](../src/opengl/GLObjectResourceManager.md) |
| [`GPLATES_OPENGL_GLOFFSCREENCONTEXT_H`](../src/opengl/GLOffScreenContext.md#free-functions-and-macros) | [opengl/GLOffScreenContext](../src/opengl/GLOffScreenContext.md) |
| [`GPLATES_OPENGL_GLPIXELBUFFER_H`](../src/opengl/GLPixelBuffer.md#free-functions-and-macros) | [opengl/GLPixelBuffer](../src/opengl/GLPixelBuffer.md) |
| [`GPLATES_OPENGL_GLPIXELBUFFERIMPL_H`](../src/opengl/GLPixelBufferImpl.md#free-functions-and-macros) | [opengl/GLPixelBufferImpl](../src/opengl/GLPixelBufferImpl.md) |
| [`GPLATES_OPENGL_GLPIXELBUFFEROBJECT_H`](../src/opengl/GLPixelBufferObject.md#free-functions-and-macros) | [opengl/GLPixelBufferObject](../src/opengl/GLPixelBufferObject.md) |
| [`GPLATES_OPENGL_GLPROGRAMOBJECT_H`](../src/opengl/GLProgramObject.md#free-functions-and-macros) | [opengl/GLProgramObject](../src/opengl/GLProgramObject.md) |
| [`GPLATES_OPENGL_GLPROJECTIONUTILS_H`](../src/opengl/GLProjectionUtils.md#free-functions-and-macros) | [opengl/GLProjectionUtils](../src/opengl/GLProjectionUtils.md) |
| [`GPLATES_OPENGL_GLRASTERCOREGISTRATION_H`](../src/opengl/GLRasterCoRegistration.md#free-functions-and-macros) | [opengl/GLRasterCoRegistration](../src/opengl/GLRasterCoRegistration.md) |
| [`GPLATES_OPENGL_GLRECONSTRUCTEDSTATICPOLYGONMESHES_H`](../src/opengl/GLReconstructedStaticPolygonMeshes.md#free-functions-and-macros) | [opengl/GLReconstructedStaticPolygonMeshes](../src/opengl/GLReconstructedStaticPolygonMeshes.md) |
| [`GPLATES_OPENGL_GLRENDERBUFFEROBJECT_H`](../src/opengl/GLRenderBufferObject.md#free-functions-and-macros) | [opengl/GLRenderBufferObject](../src/opengl/GLRenderBufferObject.md) |
| [`GPLATES_OPENGL_GLRENDERER_H`](../src/opengl/GLRenderer.md#free-functions-and-macros) | [opengl/GLRenderer](../src/opengl/GLRenderer.md) |
| [`GPLATES_OPENGL_GLRENDERERIMPL_H`](../src/opengl/GLRendererImpl.md#free-functions-and-macros) | [opengl/GLRendererImpl](../src/opengl/GLRendererImpl.md) |
| [`GPLATES_OPENGL_GLRENDERTARGET_H`](../src/opengl/GLRenderTarget.md#free-functions-and-macros) | [opengl/GLRenderTarget](../src/opengl/GLRenderTarget.md) |
| [`GPLATES_OPENGL_GLRENDERTARGETIMPL_H`](../src/opengl/GLRenderTargetImpl.md#free-functions-and-macros) | [opengl/GLRenderTargetImpl](../src/opengl/GLRenderTargetImpl.md) |
| [`GPLATES_OPENGL_GLSAVERESTOREFRAMEBUFFER_H`](../src/opengl/GLSaveRestoreFrameBuffer.md#free-functions-and-macros) | [opengl/GLSaveRestoreFrameBuffer](../src/opengl/GLSaveRestoreFrameBuffer.md) |
| [`GPLATES_OPENGL_GLSCALARFIELD3D_H`](../src/opengl/GLScalarField3D.md#free-functions-and-macros) | [opengl/GLScalarField3D](../src/opengl/GLScalarField3D.md) |
| [`GPLATES_OPENGL_GLSCALARFIELD3DGENERATOR_H`](../src/opengl/GLScalarField3DGenerator.md#free-functions-and-macros) | [opengl/GLScalarField3DGenerator](../src/opengl/GLScalarField3DGenerator.md) |
| [`GPLATES_OPENGL_GLSCALARFIELDDEPTHLAYERSSOURCE_H`](../src/opengl/GLScalarFieldDepthLayersSource.md#free-functions-and-macros) | [opengl/GLScalarFieldDepthLayersSource](../src/opengl/GLScalarFieldDepthLayersSource.md) |
| [`GPLATES_OPENGL_GLSCREENRENDERTARGET_H`](../src/opengl/GLScreenRenderTarget.md#free-functions-and-macros) | [opengl/GLScreenRenderTarget](../src/opengl/GLScreenRenderTarget.md) |
| [`GPLATES_OPENGL_GLSHADEROBJECT_H`](../src/opengl/GLShaderObject.md#free-functions-and-macros) | [opengl/GLShaderObject](../src/opengl/GLShaderObject.md) |
| [`GPLATES_OPENGL_GLSHADERPROGRAMUTILS_H`](../src/opengl/GLShaderProgramUtils.md#free-functions-and-macros) | [opengl/GLShaderProgramUtils](../src/opengl/GLShaderProgramUtils.md) |
| [`GPLATES_OPENGL_GLSHADERSOURCE_H`](../src/opengl/GLShaderSource.md#free-functions-and-macros) | [opengl/GLShaderSource](../src/opengl/GLShaderSource.md) |
| [`GPLATES_OPENGL_GLSTATE_H`](../src/opengl/GLState.md#free-functions-and-macros) | [opengl/GLState](../src/opengl/GLState.md) |
| [`GPLATES_OPENGL_GLSTATESET_H`](../src/opengl/GLStateSet.md#free-functions-and-macros) | [opengl/GLStateSet](../src/opengl/GLStateSet.md) |
| [`GPLATES_OPENGL_GLSTATESETKEYS_H`](../src/opengl/GLStateSetKeys.md#free-functions-and-macros) | [opengl/GLStateSetKeys](../src/opengl/GLStateSetKeys.md) |
| [`GPLATES_OPENGL_GLSTATESETS_H`](../src/opengl/GLStateSets.md#free-functions-and-macros) | [opengl/GLStateSets](../src/opengl/GLStateSets.md) |
| [`GPLATES_OPENGL_GLSTATESETSTORE_H`](../src/opengl/GLStateSetStore.md#free-functions-and-macros) | [opengl/GLStateSetStore](../src/opengl/GLStateSetStore.md) |
| [`GPLATES_OPENGL_GLSTATESTORE_H`](../src/opengl/GLStateStore.md#free-functions-and-macros) | [opengl/GLStateStore](../src/opengl/GLStateStore.md) |
| [`GPLATES_OPENGL_GLSTREAMPRIMITIVES_H`](../src/opengl/GLStreamPrimitives.md#free-functions-and-macros) | [opengl/GLStreamPrimitives](../src/opengl/GLStreamPrimitives.md) |
| [`GPLATES_OPENGL_GLSTREAMPRIMITIVEWRITERS_H`](../src/opengl/GLStreamPrimitiveWriters.md#free-functions-and-macros) | [opengl/GLStreamPrimitiveWriters](../src/opengl/GLStreamPrimitiveWriters.md) |
| [`GPLATES_OPENGL_GLTEXT2DDRAWABLE_H`](../src/opengl/GLText.md#free-functions-and-macros) | [opengl/GLText](../src/opengl/GLText.md) |
| [`GPLATES_OPENGL_GLTEXTURE_H`](../src/opengl/GLTexture.md#free-functions-and-macros) | [opengl/GLTexture](../src/opengl/GLTexture.md) |
| [`GPLATES_OPENGL_GLTEXTUREUTILS_H`](../src/opengl/GLTextureUtils.md#free-functions-and-macros) | [opengl/GLTextureUtils](../src/opengl/GLTextureUtils.md) |
| [`GPLATES_OPENGL_GLTILERENDER_H`](../src/opengl/GLTileRender.md#free-functions-and-macros) | [opengl/GLTileRender](../src/opengl/GLTileRender.md) |
| [`GPLATES_OPENGL_GLTRANSFORM_H`](../src/opengl/GLTransform.md#free-functions-and-macros) | [opengl/GLTransform](../src/opengl/GLTransform.md) |
| [`GPLATES_OPENGL_GLUTILS_H`](../src/opengl/GLUtils.md#free-functions-and-macros) | [opengl/GLUtils](../src/opengl/GLUtils.md) |
| [`GPLATES_OPENGL_GLVERTEXARRAY_H`](../src/opengl/GLVertexArray.md#free-functions-and-macros) | [opengl/GLVertexArray](../src/opengl/GLVertexArray.md) |
| [`GPLATES_OPENGL_GLVERTEXARRAYIMPL_H`](../src/opengl/GLVertexArrayImpl.md#free-functions-and-macros) | [opengl/GLVertexArrayImpl](../src/opengl/GLVertexArrayImpl.md) |
| [`GPLATES_OPENGL_GLVERTEXARRAYOBJECT_H`](../src/opengl/GLVertexArrayObject.md#free-functions-and-macros) | [opengl/GLVertexArrayObject](../src/opengl/GLVertexArrayObject.md) |
| [`GPLATES_OPENGL_GLVERTEXBUFFER_H`](../src/opengl/GLVertexBuffer.md#free-functions-and-macros) | [opengl/GLVertexBuffer](../src/opengl/GLVertexBuffer.md) |
| [`GPLATES_OPENGL_GLVERTEXBUFFERIMPL_H`](../src/opengl/GLVertexBufferImpl.md#free-functions-and-macros) | [opengl/GLVertexBufferImpl](../src/opengl/GLVertexBufferImpl.md) |
| [`GPLATES_OPENGL_GLVERTEXBUFFEROBJECT_H`](../src/opengl/GLVertexBufferObject.md#free-functions-and-macros) | [opengl/GLVertexBufferObject](../src/opengl/GLVertexBufferObject.md) |
| [`GPLATES_OPENGL_GLVERTEXELEMENTBUFFER_H`](../src/opengl/GLVertexElementBuffer.md#free-functions-and-macros) | [opengl/GLVertexElementBuffer](../src/opengl/GLVertexElementBuffer.md) |
| [`GPLATES_OPENGL_GLVERTEXELEMENTBUFFERIMPL_H`](../src/opengl/GLVertexElementBufferImpl.md#free-functions-and-macros) | [opengl/GLVertexElementBufferImpl](../src/opengl/GLVertexElementBufferImpl.md) |
| [`GPLATES_OPENGL_GLVERTEXELEMENTBUFFEROBJECT_H`](../src/opengl/GLVertexElementBufferObject.md#free-functions-and-macros) | [opengl/GLVertexElementBufferObject](../src/opengl/GLVertexElementBufferObject.md) |
| [`GPLATES_OPENGL_GLVIEWPORT_H`](../src/opengl/GLViewport.md#free-functions-and-macros) | [opengl/GLViewport](../src/opengl/GLViewport.md) |
| [`GPLATES_OPENGL_GLVISUALLAYERS_H`](../src/opengl/GLVisualLayers.md#free-functions-and-macros) | [opengl/GLVisualLayers](../src/opengl/GLVisualLayers.md) |
| [`GPLATES_OPENGL_GLVISUALRASTERSOURCE_H`](../src/opengl/GLVisualRasterSource.md#free-functions-and-macros) | [opengl/GLVisualRasterSource](../src/opengl/GLVisualRasterSource.md) |
| [`GPLATES_OPENGL_OPENGL_H`](../src/opengl/OpenGL.md#free-functions-and-macros) | [opengl/OpenGL](../src/opengl/OpenGL.md) |
| [`GPLATES_OPENGL_VERTEX_H`](../src/opengl/GLVertex.md#free-functions-and-macros) | [opengl/GLVertex](../src/opengl/GLVertex.md) |
| [`GPLATES_PATTERNS_PUBLISHERTEMPLATE_H`](../src/deprecated/patterns/PublisherTemplate.md#free-functions-and-macros) | [deprecated/patterns/PublisherTemplate](../src/deprecated/patterns/PublisherTemplate.md) |
| [`GPLATES_PRESENTATION_APPLICATION_H`](../src/presentation/Application.md#free-functions-and-macros) | [presentation/Application](../src/presentation/Application.md) |
| [`GPLATES_PRESENTATION_DEPRECATEDSESSIONRESTORE_H`](../src/presentation/DeprecatedSessionRestore.md#free-functions-and-macros) | [presentation/DeprecatedSessionRestore](../src/presentation/DeprecatedSessionRestore.md) |
| [`GPLATES_PRESENTATION_INTERNALSESSION_H`](../src/presentation/InternalSession.md#free-functions-and-macros) | [presentation/InternalSession](../src/presentation/InternalSession.md) |
| [`GPLATES_PRESENTATION_LAYEROUTPUTRENDERER_H`](../src/presentation/LayerOutputRenderer.md#free-functions-and-macros) | [presentation/LayerOutputRenderer](../src/presentation/LayerOutputRenderer.md) |
| [`GPLATES_PRESENTATION_PROJECTSESSION_H`](../src/presentation/ProjectSession.md#free-functions-and-macros) | [presentation/ProjectSession](../src/presentation/ProjectSession.md) |
| [`GPLATES_PRESENTATION_RASTERVISUALLAYERPARAMS_H`](../src/presentation/RasterVisualLayerParams.md#free-functions-and-macros) | [presentation/RasterVisualLayerParams](../src/presentation/RasterVisualLayerParams.md) |
| [`GPLATES_PRESENTATION_RECONSTRUCTION_GEOMETRY_RENDERER_H`](../src/presentation/ReconstructionGeometryRenderer.md#free-functions-and-macros) | [presentation/ReconstructionGeometryRenderer](../src/presentation/ReconstructionGeometryRenderer.md) |
| [`GPLATES_PRESENTATION_RECONSTRUCTSCALARCOVERAGEVISUALLAYERPARAMS_H`](../src/presentation/ReconstructScalarCoverageVisualLayerParams.md#free-functions-and-macros) | [presentation/ReconstructScalarCoverageVisualLayerParams](../src/presentation/ReconstructScalarCoverageVisualLayerParams.md) |
| [`GPLATES_PRESENTATION_RECONSTRUCTVISUALLAYERPARAMS_H`](../src/presentation/ReconstructVisualLayerParams.md#free-functions-and-macros) | [presentation/ReconstructVisualLayerParams](../src/presentation/ReconstructVisualLayerParams.md) |
| [`GPLATES_PRESENTATION_REMAPPEDCOLOURPALETTEPARAMETERS_H`](../src/presentation/RemappedColourPaletteParameters.md#free-functions-and-macros) | [presentation/RemappedColourPaletteParameters](../src/presentation/RemappedColourPaletteParameters.md) |
| [`GPLATES_PRESENTATION_SCALARFIELD3DVISUALLAYERPARAMS_H`](../src/presentation/ScalarField3DVisualLayerParams.md#free-functions-and-macros) | [presentation/ScalarField3DVisualLayerParams](../src/presentation/ScalarField3DVisualLayerParams.md) |
| [`GPLATES_PRESENTATION_SESSION_H`](../src/presentation/Session.md#free-functions-and-macros) | [presentation/Session](../src/presentation/Session.md) |
| [`GPLATES_PRESENTATION_SESSIONMANAGEMENT_H`](../src/presentation/SessionManagement.md#free-functions-and-macros) | [presentation/SessionManagement](../src/presentation/SessionManagement.md) |
| [`GPLATES_PRESENTATION_TOPOLOGYGEOMETRYVISUALLAYERPARAMS_H`](../src/presentation/TopologyGeometryVisualLayerParams.md#free-functions-and-macros) | [presentation/TopologyGeometryVisualLayerParams](../src/presentation/TopologyGeometryVisualLayerParams.md) |
| [`GPLATES_PRESENTATION_TOPOLOGYNETWORKVISUALLAYERPARAMS_H`](../src/presentation/TopologyNetworkVisualLayerParams.md#free-functions-and-macros) | [presentation/TopologyNetworkVisualLayerParams](../src/presentation/TopologyNetworkVisualLayerParams.md) |
| [`GPLATES_PRESENTATION_TRANSCRIBESESSION_H`](../src/presentation/TranscribeSession.md#free-functions-and-macros) | [presentation/TranscribeSession](../src/presentation/TranscribeSession.md) |
| [`GPLATES_PRESENTATION_VELOCITYFIELDCALCULATORVISAULLAYERPARAMS_H`](../src/presentation/VelocityFieldCalculatorVisualLayerParams.md#free-functions-and-macros) | [presentation/VelocityFieldCalculatorVisualLayerParams](../src/presentation/VelocityFieldCalculatorVisualLayerParams.md) |
| [`GPLATES_PRESENTATION_VIEWSTATE_H`](../src/presentation/ViewState.md#free-functions-and-macros) | [presentation/ViewState](../src/presentation/ViewState.md) |
| [`GPLATES_PRESENTATION_VISUALLAYER_H`](../src/presentation/VisualLayer.md#free-functions-and-macros) | [presentation/VisualLayer](../src/presentation/VisualLayer.md) |
| [`GPLATES_PRESENTATION_VISUALLAYERGROUP_H`](../src/presentation/VisualLayerGroup.md#free-functions-and-macros) | [presentation/VisualLayerGroup](../src/presentation/VisualLayerGroup.md) |
| [`GPLATES_PRESENTATION_VISUALLAYERINPUTCHANNELNAME_H`](../src/presentation/VisualLayerInputChannelName.md#free-functions-and-macros) | [presentation/VisualLayerInputChannelName](../src/presentation/VisualLayerInputChannelName.md) |
| [`GPLATES_PRESENTATION_VISUALLAYERPARAMS_H`](../src/presentation/VisualLayerParams.md#free-functions-and-macros) | [presentation/VisualLayerParams](../src/presentation/VisualLayerParams.md) |
| [`GPLATES_PRESENTATION_VISUALLAYERPARAMSVISITOR_H`](../src/presentation/VisualLayerParamsVisitor.md#free-functions-and-macros) | [presentation/VisualLayerParamsVisitor](../src/presentation/VisualLayerParamsVisitor.md) |
| [`GPLATES_PRESENTATION_VISUALLAYERREGISTRY_H`](../src/presentation/VisualLayerRegistry.md#free-functions-and-macros) | [presentation/VisualLayerRegistry](../src/presentation/VisualLayerRegistry.md) |
| [`GPLATES_PRESENTATION_VISUALLAYERS_H`](../src/presentation/VisualLayers.md#free-functions-and-macros) | [presentation/VisualLayers](../src/presentation/VisualLayers.md) |
| [`GPLATES_PRESENTATION_VISUALLAYERTYPE_H`](../src/presentation/VisualLayerType.md#free-functions-and-macros) | [presentation/VisualLayerType](../src/presentation/VisualLayerType.md) |
| [`GPLATES_PRESENTER_EXPOSEDPRESENTEROBJECT_H`](../src/deprecated/presenter/ExposedPresenterObject.md#free-functions-and-macros) | [deprecated/presenter/ExposedPresenterObject](../src/deprecated/presenter/ExposedPresenterObject.md) |
| [`GPLATES_PRESENTER_RECONSTRUCTIONCONTEXT_H`](../src/deprecated/presenter/ReconstructionContext.md#free-functions-and-macros) | [deprecated/presenter/ReconstructionContext](../src/deprecated/presenter/ReconstructionContext.md) |
| [`GPLATES_PROPERTY_VALUES_COORDINATETRANSFORMATION_H`](../src/property-values/CoordinateTransformation.md#free-functions-and-macros) | [property-values/CoordinateTransformation](../src/property-values/CoordinateTransformation.md) |
| [`GPLATES_PROPERTY_VALUES_GPMLSCALARFIELD3DFILE_H`](../src/property-values/GpmlScalarField3DFile.md#free-functions-and-macros) | [property-values/GpmlScalarField3DFile](../src/property-values/GpmlScalarField3DFile.md) |
| [`GPLATES_PROPERTY_VALUES_GPMLTOPOLOGICALNETWORK_H`](../src/property-values/GpmlTopologicalNetwork.md#free-functions-and-macros) | [property-values/GpmlTopologicalNetwork](../src/property-values/GpmlTopologicalNetwork.md) |
| [`GPLATES_PROPERTY_VALUES_OLDVERSIONPROPERTYVALUE_H`](../src/property-values/OldVersionPropertyValue.md#free-functions-and-macros) | [property-values/OldVersionPropertyValue](../src/property-values/OldVersionPropertyValue.md) |
| [`GPLATES_PROPERTY_VALUES_SPATIALREFERENCESYSTEM_H`](../src/property-values/SpatialReferenceSystem.md#free-functions-and-macros) | [property-values/SpatialReferenceSystem](../src/property-values/SpatialReferenceSystem.md) |
| [`GPLATES_PROPERTYVALUES_ENUMERATION_H`](../src/property-values/Enumeration.md#free-functions-and-macros) | [property-values/Enumeration](../src/property-values/Enumeration.md) |
| [`GPLATES_PROPERTYVALUES_ENUMERATIONCONTENT_H`](../src/property-values/EnumerationContent.md#free-functions-and-macros) | [property-values/EnumerationContent](../src/property-values/EnumerationContent.md) |
| [`GPLATES_PROPERTYVALUES_ENUMERATIONTYPE_H`](../src/property-values/EnumerationType.md#free-functions-and-macros) | [property-values/EnumerationType](../src/property-values/EnumerationType.md) |
| [`GPLATES_PROPERTYVALUES_GEOREFERENCING_H`](../src/property-values/Georeferencing.md#free-functions-and-macros) | [property-values/Georeferencing](../src/property-values/Georeferencing.md) |
| [`GPLATES_PROPERTYVALUES_GEOTIMEINSTANT_H`](../src/property-values/GeoTimeInstant.md#free-functions-and-macros) | [property-values/GeoTimeInstant](../src/property-values/GeoTimeInstant.md) |
| [`GPLATES_PROPERTYVALUES_GMLDATABLOCK_H`](../src/property-values/GmlDataBlock.md#free-functions-and-macros) | [property-values/GmlDataBlock](../src/property-values/GmlDataBlock.md) |
| [`GPLATES_PROPERTYVALUES_GMLDATABLOCKCOORDINATELIST_H`](../src/property-values/GmlDataBlockCoordinateList.md#free-functions-and-macros) | [property-values/GmlDataBlockCoordinateList](../src/property-values/GmlDataBlockCoordinateList.md) |
| [`GPLATES_PROPERTYVALUES_GMLFILE_H`](../src/property-values/GmlFile.md#free-functions-and-macros) | [property-values/GmlFile](../src/property-values/GmlFile.md) |
| [`GPLATES_PROPERTYVALUES_GMLGRIDENVELOPE_H`](../src/property-values/GmlGridEnvelope.md#free-functions-and-macros) | [property-values/GmlGridEnvelope](../src/property-values/GmlGridEnvelope.md) |
| [`GPLATES_PROPERTYVALUES_GMLLINESTRING_H`](../src/property-values/GmlLineString.md#free-functions-and-macros) | [property-values/GmlLineString](../src/property-values/GmlLineString.md) |
| [`GPLATES_PROPERTYVALUES_GMLMULTIPOINT_H`](../src/property-values/GmlMultiPoint.md#free-functions-and-macros) | [property-values/GmlMultiPoint](../src/property-values/GmlMultiPoint.md) |
| [`GPLATES_PROPERTYVALUES_GMLORIENTABLECURVE_H`](../src/property-values/GmlOrientableCurve.md#free-functions-and-macros) | [property-values/GmlOrientableCurve](../src/property-values/GmlOrientableCurve.md) |
| [`GPLATES_PROPERTYVALUES_GMLPOINT_H`](../src/property-values/GmlPoint.md#free-functions-and-macros) | [property-values/GmlPoint](../src/property-values/GmlPoint.md) |
| [`GPLATES_PROPERTYVALUES_GMLPOLYGON_H`](../src/property-values/GmlPolygon.md#free-functions-and-macros) | [property-values/GmlPolygon](../src/property-values/GmlPolygon.md) |
| [`GPLATES_PROPERTYVALUES_GMLRECTIFIEDGRID_H`](../src/property-values/GmlRectifiedGrid.md#free-functions-and-macros) | [property-values/GmlRectifiedGrid](../src/property-values/GmlRectifiedGrid.md) |
| [`GPLATES_PROPERTYVALUES_GMLTIMEINSTANT_H`](../src/property-values/GmlTimeInstant.md#free-functions-and-macros) | [property-values/GmlTimeInstant](../src/property-values/GmlTimeInstant.md) |
| [`GPLATES_PROPERTYVALUES_GMLTIMEPERIOD_H`](../src/property-values/GmlTimePeriod.md#free-functions-and-macros) | [property-values/GmlTimePeriod](../src/property-values/GmlTimePeriod.md) |
| [`GPLATES_PROPERTYVALUES_GPMLAGE_H`](../src/property-values/GpmlAge.md#free-functions-and-macros) | [property-values/GpmlAge](../src/property-values/GpmlAge.md) |
| [`GPLATES_PROPERTYVALUES_GPMLARRAY_H`](../src/property-values/GpmlArray.md#free-functions-and-macros) | [property-values/GpmlArray](../src/property-values/GpmlArray.md) |
| [`GPLATES_PROPERTYVALUES_GPMLCONSTANTVALUE_H`](../src/property-values/GpmlConstantValue.md#free-functions-and-macros) | [property-values/GpmlConstantValue](../src/property-values/GpmlConstantValue.md) |
| [`GPLATES_PROPERTYVALUES_GPMLFEATUREREFERENCE_H`](../src/property-values/GpmlFeatureReference.md#free-functions-and-macros) | [property-values/GpmlFeatureReference](../src/property-values/GpmlFeatureReference.md) |
| [`GPLATES_PROPERTYVALUES_GPMLFEATURESNAPSHOTREFERENCE_H`](../src/property-values/GpmlFeatureSnapshotReference.md#free-functions-and-macros) | [property-values/GpmlFeatureSnapshotReference](../src/property-values/GpmlFeatureSnapshotReference.md) |
| [`GPLATES_PROPERTYVALUES_GPMLFINITEROTATION_H`](../src/property-values/GpmlFiniteRotation.md#free-functions-and-macros) | [property-values/GpmlFiniteRotation](../src/property-values/GpmlFiniteRotation.md) |
| [`GPLATES_PROPERTYVALUES_GPMLFINITEROTATIONSLERP_H`](../src/property-values/GpmlFiniteRotationSlerp.md#free-functions-and-macros) | [property-values/GpmlFiniteRotationSlerp](../src/property-values/GpmlFiniteRotationSlerp.md) |
| [`GPLATES_PROPERTYVALUES_GPMLHOTSPOTTRAILMARK_H`](../src/property-values/GpmlHotSpotTrailMark.md#free-functions-and-macros) | [property-values/GpmlHotSpotTrailMark](../src/property-values/GpmlHotSpotTrailMark.md) |
| [`GPLATES_PROPERTYVALUES_GPMLINTERPOLATIONFUNCTION_H`](../src/property-values/GpmlInterpolationFunction.md#free-functions-and-macros) | [property-values/GpmlInterpolationFunction](../src/property-values/GpmlInterpolationFunction.md) |
| [`GPLATES_PROPERTYVALUES_GPMLIRREGULARSAMPLING_H`](../src/property-values/GpmlIrregularSampling.md#free-functions-and-macros) | [property-values/GpmlIrregularSampling](../src/property-values/GpmlIrregularSampling.md) |
| [`GPLATES_PROPERTYVALUES_GPMLKEYVALUEDICTIONARY_H`](../src/property-values/GpmlKeyValueDictionary.md#free-functions-and-macros) | [property-values/GpmlKeyValueDictionary](../src/property-values/GpmlKeyValueDictionary.md) |
| [`GPLATES_PROPERTYVALUES_GPMLKEYVALUEDICTIONARYELEMENT_H`](../src/property-values/GpmlKeyValueDictionaryElement.md#free-functions-and-macros) | [property-values/GpmlKeyValueDictionaryElement](../src/property-values/GpmlKeyValueDictionaryElement.md) |
| [`GPLATES_PROPERTYVALUES_GPMLMEASURE_H`](../src/property-values/GpmlMeasure.md#free-functions-and-macros) | [property-values/GpmlMeasure](../src/property-values/GpmlMeasure.md) |
| [`GPLATES_PROPERTYVALUES_GPMLMETADATA_H`](../src/property-values/GpmlMetadata.md#free-functions-and-macros) | [property-values/GpmlMetadata](../src/property-values/GpmlMetadata.md) |
| [`GPLATES_PROPERTYVALUES_GPMLOLDPLATESHEADER_H`](../src/property-values/GpmlOldPlatesHeader.md#free-functions-and-macros) | [property-values/GpmlOldPlatesHeader](../src/property-values/GpmlOldPlatesHeader.md) |
| [`GPLATES_PROPERTYVALUES_GPMLPIECEWISEAGGREGATION_H`](../src/property-values/GpmlPiecewiseAggregation.md#free-functions-and-macros) | [property-values/GpmlPiecewiseAggregation](../src/property-values/GpmlPiecewiseAggregation.md) |
| [`GPLATES_PROPERTYVALUES_GPMLPLATEID_H`](../src/property-values/GpmlPlateId.md#free-functions-and-macros) | [property-values/GpmlPlateId](../src/property-values/GpmlPlateId.md) |
| [`GPLATES_PROPERTYVALUES_GPMLPOLARITYCHRONID_H`](../src/property-values/GpmlPolarityChronId.md#free-functions-and-macros) | [property-values/GpmlPolarityChronId](../src/property-values/GpmlPolarityChronId.md) |
| [`GPLATES_PROPERTYVALUES_GPMLPROPERTYDELEGATE_H`](../src/property-values/GpmlPropertyDelegate.md#free-functions-and-macros) | [property-values/GpmlPropertyDelegate](../src/property-values/GpmlPropertyDelegate.md) |
| [`GPLATES_PROPERTYVALUES_GPMLRASTERBANDNAMES_H`](../src/property-values/GpmlRasterBandNames.md#free-functions-and-macros) | [property-values/GpmlRasterBandNames](../src/property-values/GpmlRasterBandNames.md) |
| [`GPLATES_PROPERTYVALUES_GPMLREVISIONID_H`](../src/property-values/GpmlRevisionId.md#free-functions-and-macros) | [property-values/GpmlRevisionId](../src/property-values/GpmlRevisionId.md) |
| [`GPLATES_PROPERTYVALUES_GPMLSTRINGLIST_H`](../src/property-values/GpmlStringList.md#free-functions-and-macros) | [property-values/GpmlStringList](../src/property-values/GpmlStringList.md) |
| [`GPLATES_PROPERTYVALUES_GPMLTIMESAMPLE_H`](../src/property-values/GpmlTimeSample.md#free-functions-and-macros) | [property-values/GpmlTimeSample](../src/property-values/GpmlTimeSample.md) |
| [`GPLATES_PROPERTYVALUES_GPMLTIMEWINDOW_H`](../src/property-values/GpmlTimeWindow.md#free-functions-and-macros) | [property-values/GpmlTimeWindow](../src/property-values/GpmlTimeWindow.md) |
| [`GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALLINE_H`](../src/property-values/GpmlTopologicalLine.md#free-functions-and-macros) | [property-values/GpmlTopologicalLine](../src/property-values/GpmlTopologicalLine.md) |
| [`GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALLINESECTION_H`](../src/property-values/GpmlTopologicalLineSection.md#free-functions-and-macros) | [property-values/GpmlTopologicalLineSection](../src/property-values/GpmlTopologicalLineSection.md) |
| [`GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALPOINT_H`](../src/property-values/GpmlTopologicalPoint.md#free-functions-and-macros) | [property-values/GpmlTopologicalPoint](../src/property-values/GpmlTopologicalPoint.md) |
| [`GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALPOLYGON_H`](../src/property-values/GpmlTopologicalPolygon.md#free-functions-and-macros) | [property-values/GpmlTopologicalPolygon](../src/property-values/GpmlTopologicalPolygon.md) |
| [`GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALSECTION_H`](../src/property-values/GpmlTopologicalSection.md#free-functions-and-macros) | [property-values/GpmlTopologicalSection](../src/property-values/GpmlTopologicalSection.md) |
| [`GPLATES_PROPERTYVALUES_PROXIEDRASTERCACHE_H`](../src/property-values/ProxiedRasterCache.md#free-functions-and-macros) | [property-values/ProxiedRasterCache](../src/property-values/ProxiedRasterCache.md) |
| [`GPLATES_PROPERTYVALUES_PROXIEDRASTERRESOLVER_H`](../src/property-values/ProxiedRasterResolver.md#free-functions-and-macros) | [property-values/ProxiedRasterResolver](../src/property-values/ProxiedRasterResolver.md) |
| [`GPLATES_PROPERTYVALUES_RASTERSTATISTICS_H`](../src/property-values/RasterStatistics.md#free-functions-and-macros) | [property-values/RasterStatistics](../src/property-values/RasterStatistics.md) |
| [`GPLATES_PROPERTYVALUES_RASTERTYPE_H`](../src/property-values/RasterType.md#free-functions-and-macros) | [property-values/RasterType](../src/property-values/RasterType.md) |
| [`GPLATES_PROPERTYVALUES_RAWRASTER_H`](../src/property-values/RawRaster.md#free-functions-and-macros) | [property-values/RawRaster](../src/property-values/RawRaster.md) |
| [`GPLATES_PROPERTYVALUES_RAWRASTERUTILS_H`](../src/property-values/RawRasterUtils.md#free-functions-and-macros) | [property-values/RawRasterUtils](../src/property-values/RawRasterUtils.md) |
| [`GPLATES_PROPERTYVALUES_SCALARCOVERAGESTATISTICS_H`](../src/property-values/ScalarCoverageStatistics.md#free-functions-and-macros) | [property-values/ScalarCoverageStatistics](../src/property-values/ScalarCoverageStatistics.md) |
| [`GPLATES_PROPERTYVALUES_STRUCTURALTYPE_H`](../src/property-values/StructuralType.md#free-functions-and-macros) | [property-values/StructuralType](../src/property-values/StructuralType.md) |
| [`GPLATES_PROPERTYVALUES_TEXTCONTENT_H`](../src/property-values/TextContent.md#free-functions-and-macros) | [property-values/TextContent](../src/property-values/TextContent.md) |
| [`GPLATES_PROPERTYVALUES_TIMESCALEBAND_H`](../src/property-values/TimescaleBand.md#free-functions-and-macros) | [property-values/TimescaleBand](../src/property-values/TimescaleBand.md) |
| [`GPLATES_PROPERTYVALUES_TIMESCALENAME_H`](../src/property-values/TimescaleName.md#free-functions-and-macros) | [property-values/TimescaleName](../src/property-values/TimescaleName.md) |
| [`GPLATES_PROPERTYVALUES_UNINTERPRETEDPROPERTYVALUE_H`](../src/property-values/UninterpretedPropertyValue.md#free-functions-and-macros) | [property-values/UninterpretedPropertyValue](../src/property-values/UninterpretedPropertyValue.md) |
| [`GPLATES_PROPERTYVALUES_VALUEOBJECTTYPE_H`](../src/property-values/ValueObjectType.md#free-functions-and-macros) | [property-values/ValueObjectType](../src/property-values/ValueObjectType.md) |
| [`GPLATES_PROPERTYVALUES_XSBOOLEAN_H`](../src/property-values/XsBoolean.md#free-functions-and-macros) | [property-values/XsBoolean](../src/property-values/XsBoolean.md) |
| [`GPLATES_PROPERTYVALUES_XSDOUBLE_H`](../src/property-values/XsDouble.md#free-functions-and-macros) | [property-values/XsDouble](../src/property-values/XsDouble.md) |
| [`GPLATES_PROPERTYVALUES_XSINTEGER_H`](../src/property-values/XsInteger.md#free-functions-and-macros) | [property-values/XsInteger](../src/property-values/XsInteger.md) |
| [`GPLATES_PROPERTYVALUES_XSSTRING_H`](../src/property-values/XsString.md#free-functions-and-macros) | [property-values/XsString](../src/property-values/XsString.md) |
| [`GPLATES_QT_WIDGETS_ASSIGNRECONSTRUCTIONPLATEIDSDIALOG_H`](../src/qt-widgets/AssignReconstructionPlateIdsDialog.md#free-functions-and-macros) | [qt-widgets/AssignReconstructionPlateIdsDialog](../src/qt-widgets/AssignReconstructionPlateIdsDialog.md) |
| [`GPLATES_QT_WIDGETS_CANVASTOOLBARDOCKWIDGET_H`](../src/qt-widgets/CanvasToolBarDockWidget.md#free-functions-and-macros) | [qt-widgets/CanvasToolBarDockWidget](../src/qt-widgets/CanvasToolBarDockWidget.md) |
| [`GPLATES_QT_WIDGETS_CHOOSEBUILTINPALETTEDIALOG_H`](../src/qt-widgets/ChooseBuiltinPaletteDialog.md#free-functions-and-macros) | [qt-widgets/ChooseBuiltinPaletteDialog](../src/qt-widgets/ChooseBuiltinPaletteDialog.md) |
| [`GPLATES_QT_WIDGETS_COLOURSCALEBUTTON_H`](../src/qt-widgets/ColourScaleButton.md#free-functions-and-macros) | [qt-widgets/ColourScaleButton](../src/qt-widgets/ColourScaleButton.md) |
| [`GPLATES_QT_WIDGETS_COREGISTRATIONLAYERCONFIGURATIONDIALOG_H`](../src/qt-widgets/CoRegistrationLayerConfigurationDialog.md#free-functions-and-macros) | [qt-widgets/CoRegistrationLayerConfigurationDialog](../src/qt-widgets/CoRegistrationLayerConfigurationDialog.md) |
| [`GPLATES_QT_WIDGETS_DATELINEWRAPOPTIONSWIDGET_H`](../src/qt-widgets/DatelineWrapOptionsWidget.md#free-functions-and-macros) | [qt-widgets/DatelineWrapOptionsWidget](../src/qt-widgets/DatelineWrapOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTCITCOMSRESOLVEDTOPOLOGYOPTIONSWIDGET_H`](../src/qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget](../src/qt-widgets/ExportCitcomsResolvedTopologyOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTDEFORMATIONOPTIONSWIDGET_H`](../src/qt-widgets/ExportDeformationOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportDeformationOptionsWidget](../src/qt-widgets/ExportDeformationOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTFILEOPTIONSWIDGET_H`](../src/qt-widgets/ExportFileOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportFileOptionsWidget](../src/qt-widgets/ExportFileOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTFLOWLINEOPTIONSWIDGET_H`](../src/qt-widgets/ExportFlowlineOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportFlowlineOptionsWidget](../src/qt-widgets/ExportFlowlineOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTIMAGEOPTIONSWIDGET_H`](../src/qt-widgets/ExportImageOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportImageOptionsWidget](../src/qt-widgets/ExportImageOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTIMAGERESOLUTIONOPTIONSWIDGET_H`](../src/qt-widgets/ExportImageResolutionOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportImageResolutionOptionsWidget](../src/qt-widgets/ExportImageResolutionOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTMOTIONPATHOPTIONSWIDGET_H`](../src/qt-widgets/ExportMotionPathOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportMotionPathOptionsWidget](../src/qt-widgets/ExportMotionPathOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTNETROTATIONOPTIONSWIDGET_H`](../src/qt-widgets/ExportNetRotationOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportNetRotationOptionsWidget](../src/qt-widgets/ExportNetRotationOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTOPTIONSWIDGET_H`](../src/qt-widgets/ExportOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportOptionsWidget](../src/qt-widgets/ExportOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTRASTEROPTIONSWIDGET_H`](../src/qt-widgets/ExportRasterOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportRasterOptionsWidget](../src/qt-widgets/ExportRasterOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTRECONSTRUCTEDGEOMETRYOPTIONSWIDGET_H`](../src/qt-widgets/ExportReconstructedGeometryOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportReconstructedGeometryOptionsWidget](../src/qt-widgets/ExportReconstructedGeometryOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTRESOLVEDTOPOLOGYOPTIONSWIDGET_H`](../src/qt-widgets/ExportResolvedTopologyOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportResolvedTopologyOptionsWidget](../src/qt-widgets/ExportResolvedTopologyOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTROTATIONOPTIONSWIDGET_H`](../src/qt-widgets/ExportRotationOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportRotationOptionsWidget](../src/qt-widgets/ExportRotationOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTSCALARCOVERAGEOPTIONSWIDGET_H`](../src/qt-widgets/ExportScalarCoverageOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportScalarCoverageOptionsWidget](../src/qt-widgets/ExportScalarCoverageOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTSTAGEROTATIONONLYOPTIONSWIDGET_H`](../src/qt-widgets/ExportStageRotationOnlyOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportStageRotationOnlyOptionsWidget](../src/qt-widgets/ExportStageRotationOnlyOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTSTAGEROTATIONOPTIONSWIDGET_H`](../src/qt-widgets/ExportStageRotationOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportStageRotationOptionsWidget](../src/qt-widgets/ExportStageRotationOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTSVGOPTIONSWIDGET_H`](../src/qt-widgets/ExportSvgOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportSvgOptionsWidget](../src/qt-widgets/ExportSvgOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTTOTALROTATIONOPTIONSWIDGET_H`](../src/qt-widgets/ExportTotalRotationOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportTotalRotationOptionsWidget](../src/qt-widgets/ExportTotalRotationOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTVELOCITYCALCULATIONOPTIONSWIDGET_H`](../src/qt-widgets/ExportVelocityCalculationOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportVelocityCalculationOptionsWidget](../src/qt-widgets/ExportVelocityCalculationOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_EXPORTVELOCITYOPTIONSWIDGET_H`](../src/qt-widgets/ExportVelocityOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ExportVelocityOptionsWidget](../src/qt-widgets/ExportVelocityOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_IMPORTSCALARFIELD3DDIALOG_H`](../src/qt-widgets/ImportScalarField3DDialog.md#free-functions-and-macros) | [qt-widgets/ImportScalarField3DDialog](../src/qt-widgets/ImportScalarField3DDialog.md) |
| [`GPLATES_QT_WIDGETS_LIGHTINGWIDGET_H`](../src/qt-widgets/LightingWidget.md#free-functions-and-macros) | [qt-widgets/LightingWidget](../src/qt-widgets/LightingWidget.md) |
| [`GPLATES_QT_WIDGETS_MANAGEFEATURECOLLECTIONSEDITCONFIGURATIONS_H`](../src/qt-widgets/ManageFeatureCollectionsEditConfigurations.md#free-functions-and-macros) | [qt-widgets/ManageFeatureCollectionsEditConfigurations](../src/qt-widgets/ManageFeatureCollectionsEditConfigurations.md) |
| [`GPLATES_QT_WIDGETS_MOVEPOLEWIDGET_H`](../src/qt-widgets/MovePoleWidget.md#free-functions-and-macros) | [qt-widgets/MovePoleWidget](../src/qt-widgets/MovePoleWidget.md) |
| [`GPLATES_QT_WIDGETS_RECONSTRUCTSCALARCOVERAGELAYEROPTIONSWIDGET_H`](../src/qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ReconstructScalarCoverageLayerOptionsWidget](../src/qt-widgets/ReconstructScalarCoverageLayerOptionsWidget.md) |
| [`GPLATES_QT_WIDGETS_REMAPPEDCOLOURPALETTEWIDGET_H`](../src/qt-widgets/RemappedColourPaletteWidget.md#free-functions-and-macros) | [qt-widgets/RemappedColourPaletteWidget](../src/qt-widgets/RemappedColourPaletteWidget.md) |
| [`GPLATES_QT_WIDGETS_RESIZETOCONTENTSTEXTEDIT_H`](../src/qt-widgets/ResizeToContentsTextEdit.md#free-functions-and-macros) | [qt-widgets/ResizeToContentsTextEdit](../src/qt-widgets/ResizeToContentsTextEdit.md) |
| [`GPLATES_QT_WIDGETS_SEARCHRESULTSDOCKWIDGET_H`](../src/qt-widgets/SearchResultsDockWidget.md#free-functions-and-macros) | [qt-widgets/SearchResultsDockWidget](../src/qt-widgets/SearchResultsDockWidget.md) |
| [`GPLATES_QT_WIDGETS_TOPOLOGYGEOMETRYRESOLVERLAYEROPTIONSWIDGET_H`](../src/qt-widgets/TopologyGeometryResolverLayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/TopologyGeometryResolverLayerOptionsWidget](../src/qt-widgets/TopologyGeometryResolverLayerOptionsWidget.md) |
| [`GPLATES_QTWIDGETS_ABOUTDIALOG_H`](../src/qt-widgets/AboutDialog.md#free-functions-and-macros) | [qt-widgets/AboutDialog](../src/qt-widgets/AboutDialog.md) |
| [`GPLATES_QTWIDGETS_ABSTRACTCUSTOMPROPERTIESWIDGET_H`](../src/qt-widgets/AbstractCustomPropertiesWidget.md#free-functions-and-macros) | [qt-widgets/AbstractCustomPropertiesWidget](../src/qt-widgets/AbstractCustomPropertiesWidget.md) |
| [`GPLATES_QTWIDGETS_ABSTRACTEDITWIDGET_H`](../src/qt-widgets/AbstractEditWidget.md#free-functions-and-macros) | [qt-widgets/AbstractEditWidget](../src/qt-widgets/AbstractEditWidget.md) |
| [`GPLATES_QTWIDGETS_ACTIONBUTTONBOX_H`](../src/qt-widgets/ActionButtonBox.md#free-functions-and-macros) | [qt-widgets/ActionButtonBox](../src/qt-widgets/ActionButtonBox.md) |
| [`GPLATES_QTWIDGETS_ADDNEWLAYERDIALOG_H`](../src/qt-widgets/AddNewLayerDialog.md#free-functions-and-macros) | [qt-widgets/AddNewLayerDialog](../src/qt-widgets/AddNewLayerDialog.md) |
| [`GPLATES_QTWIDGETS_ADDPROPERTYDIALOG_H`](../src/qt-widgets/AddPropertyDialog.md#free-functions-and-macros) | [qt-widgets/AddPropertyDialog](../src/qt-widgets/AddPropertyDialog.md) |
| [`GPLATES_QTWIDGETS_AGEMODELMANAGERDIALOG_H`](../src/qt-widgets/AgeModelManagerDialog.md#free-functions-and-macros) | [qt-widgets/AgeModelManagerDialog](../src/qt-widgets/AgeModelManagerDialog.md) |
| [`GPLATES_QTWIDGETS_ANIMATECONTROLWIDGET_H`](../src/qt-widgets/AnimateControlWidget.md#free-functions-and-macros) | [qt-widgets/AnimateControlWidget](../src/qt-widgets/AnimateControlWidget.md) |
| [`GPLATES_QTWIDGETS_ANIMATEDIALOG_H`](../src/qt-widgets/AnimateDialog.md#free-functions-and-macros) | [qt-widgets/AnimateDialog](../src/qt-widgets/AnimateDialog.md) |
| [`GPLATES_QTWIDGETS_APPLYRECONSTRUCTIONPOLEADJUSTMENTDIALOG_H`](../src/qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md#free-functions-and-macros) | [qt-widgets/ApplyReconstructionPoleAdjustmentDialog](../src/qt-widgets/ApplyReconstructionPoleAdjustmentDialog.md) |
| [`GPLATES_QTWIDGETS_CALCULATERECONSTRUCTIONPOLEDIALOG_H`](../src/qt-widgets/CalculateReconstructionPoleDialog.md#free-functions-and-macros) | [qt-widgets/CalculateReconstructionPoleDialog](../src/qt-widgets/CalculateReconstructionPoleDialog.md) |
| [`GPLATES_QTWIDGETS_CALCULATESTAGEPOLEDIALOG_H`](../src/qt-widgets/deprecated/CalculateStagePoleDialog.md#free-functions-and-macros) | [qt-widgets/deprecated/CalculateStagePoleDialog](../src/qt-widgets/deprecated/CalculateStagePoleDialog.md) |
| [`GPLATES_QTWIDGETS_CHANGEFEATURETYPEDIALOG_H`](../src/qt-widgets/ChangeFeatureTypeDialog.md#free-functions-and-macros) | [qt-widgets/ChangeFeatureTypeDialog](../src/qt-widgets/ChangeFeatureTypeDialog.md) |
| [`GPLATES_QTWIDGETS_CHANGEPROPERTYWIDGET_H`](../src/qt-widgets/ChangePropertyWidget.md#free-functions-and-macros) | [qt-widgets/ChangePropertyWidget](../src/qt-widgets/ChangePropertyWidget.md) |
| [`GPLATES_QTWIDGETS_CHOOSECOLOURBUTTON_H`](../src/qt-widgets/ChooseColourButton.md#free-functions-and-macros) | [qt-widgets/ChooseColourButton](../src/qt-widgets/ChooseColourButton.md) |
| [`GPLATES_QTWIDGETS_CHOOSEFEATURECOLLECTIONDIALOG_H`](../src/qt-widgets/ChooseFeatureCollectionDialog.md#free-functions-and-macros) | [qt-widgets/ChooseFeatureCollectionDialog](../src/qt-widgets/ChooseFeatureCollectionDialog.md) |
| [`GPLATES_QTWIDGETS_CHOOSEFEATURECOLLECTIONWIDGET_H`](../src/qt-widgets/ChooseFeatureCollectionWidget.md#free-functions-and-macros) | [qt-widgets/ChooseFeatureCollectionWidget](../src/qt-widgets/ChooseFeatureCollectionWidget.md) |
| [`GPLATES_QTWIDGETS_CHOOSEFEATURETYPEWIDGET_H`](../src/qt-widgets/ChooseFeatureTypeWidget.md#free-functions-and-macros) | [qt-widgets/ChooseFeatureTypeWidget](../src/qt-widgets/ChooseFeatureTypeWidget.md) |
| [`GPLATES_QTWIDGETS_CHOOSEFONTBUTTON_H`](../src/qt-widgets/ChooseFontButton.md#free-functions-and-macros) | [qt-widgets/ChooseFontButton](../src/qt-widgets/ChooseFontButton.md) |
| [`GPLATES_QTWIDGETS_CHOOSEPROPERTYWIDGET_H`](../src/qt-widgets/ChoosePropertyWidget.md#free-functions-and-macros) | [qt-widgets/ChoosePropertyWidget](../src/qt-widgets/ChoosePropertyWidget.md) |
| [`GPLATES_QTWIDGETS_COLOURINGDIALOG_H`](../src/qt-widgets/ColouringDialog.md#free-functions-and-macros) | [qt-widgets/ColouringDialog](../src/qt-widgets/ColouringDialog.md) |
| [`GPLATES_QTWIDGETS_COLOURSCALEWIDGET_H`](../src/qt-widgets/ColourScaleWidget.md#free-functions-and-macros) | [qt-widgets/ColourScaleWidget](../src/qt-widgets/ColourScaleWidget.md) |
| [`GPLATES_QTWIDGETS_CONFIGURECANVASTOOLGEOMETRYRENDERPARAMETERSDIALOG_H`](../src/qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog.md#free-functions-and-macros) | [qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog](../src/qt-widgets/ConfigureCanvasToolGeometryRenderParametersDialog.md) |
| [`GPLATES_QTWIDGETS_CONFIGUREEXPORTPARAMETERSDIALOG_H`](../src/qt-widgets/ConfigureExportParametersDialog.md#free-functions-and-macros) | [qt-widgets/ConfigureExportParametersDialog](../src/qt-widgets/ConfigureExportParametersDialog.md) |
| [`GPLATES_QTWIDGETS_CONFIGUREGRATICULESDIALOG_H`](../src/qt-widgets/ConfigureGraticulesDialog.md#free-functions-and-macros) | [qt-widgets/ConfigureGraticulesDialog](../src/qt-widgets/ConfigureGraticulesDialog.md) |
| [`GPLATES_QTWIDGETS_CONFIGURETEXTOVERLAYDIALOG_H`](../src/qt-widgets/ConfigureTextOverlayDialog.md#free-functions-and-macros) | [qt-widgets/ConfigureTextOverlayDialog](../src/qt-widgets/ConfigureTextOverlayDialog.md) |
| [`GPLATES_QTWIDGETS_CONFIGUREVELOCITYLEGENDOVERLAYDIALOG_H`](../src/qt-widgets/ConfigureVelocityLegendOverlayDialog.md#free-functions-and-macros) | [qt-widgets/ConfigureVelocityLegendOverlayDialog](../src/qt-widgets/ConfigureVelocityLegendOverlayDialog.md) |
| [`GPLATES_QTWIDGETS_CONFIGVALUEEDITORWIDGET_H`](../src/qt-widgets/ConfigValueEditorWidget.md#free-functions-and-macros) | [qt-widgets/ConfigValueEditorWidget](../src/qt-widgets/ConfigValueEditorWidget.md) |
| [`GPLATES_QTWIDGETS_CONNECTWFSDIALOG_H`](../src/qt-widgets/ConnectWFSDialog.md#free-functions-and-macros) | [qt-widgets/ConnectWFSDialog](../src/qt-widgets/ConnectWFSDialog.md) |
| [`GPLATES_QTWIDGETS_COREGISTRATIONOPTIONSWIDGET_H`](../src/qt-widgets/CoRegistrationOptionsWidget.md#free-functions-and-macros) | [qt-widgets/CoRegistrationOptionsWidget](../src/qt-widgets/CoRegistrationOptionsWidget.md) |
| [`GPLATES_QTWIDGETS_COREGISTRATIONRESULTTABLEDIALOG_H`](../src/qt-widgets/CoRegistrationResultTableDialog.md#free-functions-and-macros) | [qt-widgets/CoRegistrationResultTableDialog](../src/qt-widgets/CoRegistrationResultTableDialog.md) |
| [`GPLATES_QTWIDGETS_CREATEFEATUREADDOREDITPROPERTYDIALOG_H`](../src/qt-widgets/CreateFeatureAddOrEditPropertyDialog.md#free-functions-and-macros) | [qt-widgets/CreateFeatureAddOrEditPropertyDialog](../src/qt-widgets/CreateFeatureAddOrEditPropertyDialog.md) |
| [`GPLATES_QTWIDGETS_CREATEFEATUREDIALOG_H`](../src/qt-widgets/CreateFeatureDialog.md#free-functions-and-macros) | [qt-widgets/CreateFeatureDialog](../src/qt-widgets/CreateFeatureDialog.md) |
| [`GPLATES_QTWIDGETS_CREATEFEATUREPROPERTIESPAGE_H`](../src/qt-widgets/CreateFeaturePropertiesPage.md#free-functions-and-macros) | [qt-widgets/CreateFeaturePropertiesPage](../src/qt-widgets/CreateFeaturePropertiesPage.md) |
| [`GPLATES_QTWIDGETS_CREATESMALLCIRCLEDIALOG_H`](../src/qt-widgets/CreateSmallCircleDialog.md#free-functions-and-macros) | [qt-widgets/CreateSmallCircleDialog](../src/qt-widgets/CreateSmallCircleDialog.md) |
| [`GPLATES_QTWIDGETS_CREATESMALLCIRCLEFEATUREDIALOG_H`](../src/qt-widgets/CreateSmallCircleFeatureDialog.md#free-functions-and-macros) | [qt-widgets/CreateSmallCircleFeatureDialog](../src/qt-widgets/CreateSmallCircleFeatureDialog.md) |
| [`GPLATES_QTWIDGETS_CREATETOPOLOGYWIDGET_H`](../src/qt-widgets/deprecated/CreateTopologyWidget.md#free-functions-and-macros) | [qt-widgets/deprecated/CreateTopologyWidget](../src/qt-widgets/deprecated/CreateTopologyWidget.md) |
| [`GPLATES_QTWIDGETS_CREATETOTALRECONSTRUCTIONSEQUENCEDIALOG_H`](../src/qt-widgets/CreateTotalReconstructionSequenceDialog.md#free-functions-and-macros) | [qt-widgets/CreateTotalReconstructionSequenceDialog](../src/qt-widgets/CreateTotalReconstructionSequenceDialog.md) |
| [`GPLATES_QTWIDGETS_CREATEVGPDIALOG_H`](../src/qt-widgets/CreateVGPDialog.md#free-functions-and-macros) | [qt-widgets/CreateVGPDialog](../src/qt-widgets/CreateVGPDialog.md) |
| [`GPLATES_QTWIDGETS_DIGITISATIONUNDOPARADOXEXCEPTION_H`](../src/qt-widgets/deprecated/DigitisationUndoParadoxException.md#free-functions-and-macros) | [qt-widgets/deprecated/DigitisationUndoParadoxException](../src/qt-widgets/deprecated/DigitisationUndoParadoxException.md) |
| [`GPLATES_QTWIDGETS_DIGITISATIONWIDGET_H`](../src/qt-widgets/DigitisationWidget.md#free-functions-and-macros) | [qt-widgets/DigitisationWidget](../src/qt-widgets/DigitisationWidget.md) |
| [`GPLATES_QTWIDGETS_DOCKWIDGET_H`](../src/qt-widgets/DockWidget.md#free-functions-and-macros) | [qt-widgets/DockWidget](../src/qt-widgets/DockWidget.md) |
| [`GPLATES_QTWIDGETS_DRAWSTYLEDIALOG_H`](../src/qt-widgets/DrawStyleDialog.md#free-functions-and-macros) | [qt-widgets/DrawStyleDialog](../src/qt-widgets/DrawStyleDialog.md) |
| [`GPLATES_QTWIDGETS_EDITAFFINETRANSFORMGEOREFERENCINGWIDGET_H`](../src/qt-widgets/EditAffineTransformGeoreferencingWidget.md#free-functions-and-macros) | [qt-widgets/EditAffineTransformGeoreferencingWidget](../src/qt-widgets/EditAffineTransformGeoreferencingWidget.md) |
| [`GPLATES_QTWIDGETS_EDITAGEWIDGET_H`](../src/qt-widgets/EditAgeWidget.md#free-functions-and-macros) | [qt-widgets/EditAgeWidget](../src/qt-widgets/EditAgeWidget.md) |
| [`GPLATES_QTWIDGETS_EDITANGLEWIDGET_H`](../src/qt-widgets/EditAngleWidget.md#free-functions-and-macros) | [qt-widgets/EditAngleWidget](../src/qt-widgets/EditAngleWidget.md) |
| [`GPLATES_QTWIDGETS_EDITBOOLEANWIDGET_H`](../src/qt-widgets/EditBooleanWidget.md#free-functions-and-macros) | [qt-widgets/EditBooleanWidget](../src/qt-widgets/EditBooleanWidget.md) |
| [`GPLATES_QTWIDGETS_EDITDOUBLEWIDGET_H`](../src/qt-widgets/EditDoubleWidget.md#free-functions-and-macros) | [qt-widgets/EditDoubleWidget](../src/qt-widgets/EditDoubleWidget.md) |
| [`GPLATES_QTWIDGETS_EDITENUMERATIONWIDGET_H`](../src/qt-widgets/EditEnumerationWidget.md#free-functions-and-macros) | [qt-widgets/EditEnumerationWidget](../src/qt-widgets/EditEnumerationWidget.md) |
| [`GPLATES_QTWIDGETS_EDITEXPORTPARAMETERSDIALOG_H`](../src/qt-widgets/EditExportParametersDialog.md#free-functions-and-macros) | [qt-widgets/EditExportParametersDialog](../src/qt-widgets/EditExportParametersDialog.md) |
| [`GPLATES_QTWIDGETS_EDITFEATUREPROPERTIESWIDGET_H`](../src/qt-widgets/EditFeaturePropertiesWidget.md#free-functions-and-macros) | [qt-widgets/EditFeaturePropertiesWidget](../src/qt-widgets/EditFeaturePropertiesWidget.md) |
| [`GPLATES_QTWIDGETS_EDITGEOMETRYWIDGET_H`](../src/qt-widgets/EditGeometryWidget.md#free-functions-and-macros) | [qt-widgets/EditGeometryWidget](../src/qt-widgets/EditGeometryWidget.md) |
| [`GPLATES_QTWIDGETS_EDITINTEGERWIDGET_H`](../src/qt-widgets/EditIntegerWidget.md#free-functions-and-macros) | [qt-widgets/EditIntegerWidget](../src/qt-widgets/EditIntegerWidget.md) |
| [`GPLATES_QTWIDGETS_EDITOLDPLATESHEADERWIDGET_H`](../src/qt-widgets/EditOldPlatesHeaderWidget.md#free-functions-and-macros) | [qt-widgets/EditOldPlatesHeaderWidget](../src/qt-widgets/EditOldPlatesHeaderWidget.md) |
| [`GPLATES_QTWIDGETS_EDITPLATEIDWIDGET_H`](../src/qt-widgets/EditPlateIdWidget.md#free-functions-and-macros) | [qt-widgets/EditPlateIdWidget](../src/qt-widgets/EditPlateIdWidget.md) |
| [`GPLATES_QTWIDGETS_EDITPOLARITYCHRONIDWIDGET_H`](../src/qt-widgets/EditPolarityChronIdWidget.md#free-functions-and-macros) | [qt-widgets/EditPolarityChronIdWidget](../src/qt-widgets/EditPolarityChronIdWidget.md) |
| [`GPLATES_QTWIDGETS_EDITSHAPEFILEATTRIBUTESWIDGET_H`](../src/qt-widgets/EditShapefileAttributesWidget.md#free-functions-and-macros) | [qt-widgets/EditShapefileAttributesWidget](../src/qt-widgets/EditShapefileAttributesWidget.md) |
| [`GPLATES_QTWIDGETS_EDITSTRINGLIST_H`](../src/qt-widgets/EditStringListWidget.md#free-functions-and-macros) | [qt-widgets/EditStringListWidget](../src/qt-widgets/EditStringListWidget.md) |
| [`GPLATES_QTWIDGETS_EDITSTRINGWIDGET_H`](../src/qt-widgets/EditStringWidget.md#free-functions-and-macros) | [qt-widgets/EditStringWidget](../src/qt-widgets/EditStringWidget.md) |
| [`GPLATES_QTWIDGETS_EDITTABLEACTIONWIDGET_H`](../src/qt-widgets/EditTableActionWidget.md#free-functions-and-macros) | [qt-widgets/EditTableActionWidget](../src/qt-widgets/EditTableActionWidget.md) |
| [`GPLATES_QTWIDGETS_EDITTABLEWIDGET_H`](../src/qt-widgets/EditTableWidget.md#free-functions-and-macros) | [qt-widgets/EditTableWidget](../src/qt-widgets/EditTableWidget.md) |
| [`GPLATES_QTWIDGETS_EDITTIMEINSTANTWIDGET_H`](../src/qt-widgets/EditTimeInstantWidget.md#free-functions-and-macros) | [qt-widgets/EditTimeInstantWidget](../src/qt-widgets/EditTimeInstantWidget.md) |
| [`GPLATES_QTWIDGETS_EDITTIMEPERIODWIDGET_H`](../src/qt-widgets/EditTimePeriodWidget.md#free-functions-and-macros) | [qt-widgets/EditTimePeriodWidget](../src/qt-widgets/EditTimePeriodWidget.md) |
| [`GPLATES_QTWIDGETS_EDITTIMESEQUENCE_H`](../src/qt-widgets/EditTimeSequenceWidget.md#free-functions-and-macros) | [qt-widgets/EditTimeSequenceWidget](../src/qt-widgets/EditTimeSequenceWidget.md) |
| [`GPLATES_QTWIDGETS_EDITTOTALRECONSTRUCTIONSEQUENCEDIALOG_H`](../src/qt-widgets/EditTotalReconstructionSequenceDialog.md#free-functions-and-macros) | [qt-widgets/EditTotalReconstructionSequenceDialog](../src/qt-widgets/EditTotalReconstructionSequenceDialog.md) |
| [`GPLATES_QTWIDGETS_EDITTOTALRECONSTRUCTIONSEQUENCEWIDGET_H`](../src/qt-widgets/EditTotalReconstructionSequenceWidget.md#free-functions-and-macros) | [qt-widgets/EditTotalReconstructionSequenceWidget](../src/qt-widgets/EditTotalReconstructionSequenceWidget.md) |
| [`GPLATES_QTWIDGETS_EDITWIDGETCHOOSER_H`](../src/qt-widgets/EditWidgetChooser.md#free-functions-and-macros) | [qt-widgets/EditWidgetChooser](../src/qt-widgets/EditWidgetChooser.md) |
| [`GPLATES_QTWIDGETS_EDITWIDGETGROUPBOX_H`](../src/qt-widgets/EditWidgetGroupBox.md#free-functions-and-macros) | [qt-widgets/EditWidgetGroupBox](../src/qt-widgets/EditWidgetGroupBox.md) |
| [`GPLATES_QTWIDGETS_ELIDEDLABEL_H`](../src/qt-widgets/ElidedLabel.md#free-functions-and-macros) | [qt-widgets/ElidedLabel](../src/qt-widgets/ElidedLabel.md) |
| [`GPLATES_QTWIDGETS_EXPORTANIMATIONDIALOG_H`](../src/qt-widgets/ExportAnimationDialog.md#free-functions-and-macros) | [qt-widgets/ExportAnimationDialog](../src/qt-widgets/ExportAnimationDialog.md) |
| [`GPLATES_QTWIDGETS_EXPORTCOORDINATESDIALOG_H`](../src/qt-widgets/ExportCoordinatesDialog.md#free-functions-and-macros) | [qt-widgets/ExportCoordinatesDialog](../src/qt-widgets/ExportCoordinatesDialog.md) |
| [`GPLATES_QTWIDGETS_EXPORTFILENAMETEMPLATEWIDGET_H`](../src/qt-widgets/ExportFileNameTemplateWidget.md#free-functions-and-macros) | [qt-widgets/ExportFileNameTemplateWidget](../src/qt-widgets/ExportFileNameTemplateWidget.md) |
| [`GPLATES_QTWIDGETS_FEATUREPROPERTIESDIALOG_H`](../src/qt-widgets/FeaturePropertiesDialog.md#free-functions-and-macros) | [qt-widgets/FeaturePropertiesDialog](../src/qt-widgets/FeaturePropertiesDialog.md) |
| [`GPLATES_QTWIDGETS_FEATURESUMMARYWIDGET_H`](../src/qt-widgets/FeatureSummaryWidget.md#free-functions-and-macros) | [qt-widgets/FeatureSummaryWidget](../src/qt-widgets/FeatureSummaryWidget.md) |
| [`GPLATES_QTWIDGETS_FILEDIALOGFILTER_H`](../src/qt-widgets/FileDialogFilter.md#free-functions-and-macros) | [qt-widgets/FileDialogFilter](../src/qt-widgets/FileDialogFilter.md) |
| [`GPLATES_QTWIDGETS_FINITEROTATIONCALCULATORDIALOG_H`](../src/qt-widgets/FiniteRotationCalculatorDialog.md#free-functions-and-macros) | [qt-widgets/FiniteRotationCalculatorDialog](../src/qt-widgets/FiniteRotationCalculatorDialog.md) |
| [`GPLATES_QTWIDGETS_FLOWLINEPROPERTIESWIDGET_H`](../src/qt-widgets/FlowlinePropertiesWidget.md#free-functions-and-macros) | [qt-widgets/FlowlinePropertiesWidget](../src/qt-widgets/FlowlinePropertiesWidget.md) |
| [`GPLATES_QTWIDGETS_FRIENDLYLINEEDIT_H`](../src/qt-widgets/FriendlyLineEdit.md#free-functions-and-macros) | [qt-widgets/FriendlyLineEdit](../src/qt-widgets/FriendlyLineEdit.md) |
| [`GPLATES_QTWIDGETS_GENERATEDEFORMINGMESHPOINTSDIALOG_H`](../src/qt-widgets/GenerateDeformingMeshPointsDialog.md#free-functions-and-macros) | [qt-widgets/GenerateDeformingMeshPointsDialog](../src/qt-widgets/GenerateDeformingMeshPointsDialog.md) |
| [`GPLATES_QTWIDGETS_GLOBEANDMAPWIDGET_H`](../src/qt-widgets/GlobeAndMapWidget.md#free-functions-and-macros) | [qt-widgets/GlobeAndMapWidget](../src/qt-widgets/GlobeAndMapWidget.md) |
| [`GPLATES_QTWIDGETS_GLOBECANVAS_H`](../src/qt-widgets/GlobeCanvas.md#free-functions-and-macros) | [qt-widgets/GlobeCanvas](../src/qt-widgets/GlobeCanvas.md) |
| [`GPLATES_QTWIDGETS_GMENUBUTTON_H`](../src/qt-widgets/GMenuButton.md#free-functions-and-macros) | [qt-widgets/GMenuButton](../src/qt-widgets/GMenuButton.md) |
| [`GPLATES_QTWIDGETS_GMTFILEFORMATCONFIGURATIONDIALOG_H`](../src/qt-widgets/GMTFileFormatConfigurationDialog.md#free-functions-and-macros) | [qt-widgets/GMTFileFormatConfigurationDialog](../src/qt-widgets/GMTFileFormatConfigurationDialog.md) |
| [`GPLATES_QTWIDGETS_GPGIMVERSIONWARNINGDIALOG_H`](../src/qt-widgets/GpgimVersionWarningDialog.md#free-functions-and-macros) | [qt-widgets/GpgimVersionWarningDialog](../src/qt-widgets/GpgimVersionWarningDialog.md) |
| [`GPLATES_QTWIDGETS_GPLATESDIALOG_H`](../src/qt-widgets/GPlatesDialog.md#free-functions-and-macros) | [qt-widgets/GPlatesDialog](../src/qt-widgets/GPlatesDialog.md) |
| [`GPLATES_QTWIDGETS_HELLINGERDIALOG_H`](../src/qt-widgets/HellingerDialog.md#free-functions-and-macros) | [qt-widgets/HellingerDialog](../src/qt-widgets/HellingerDialog.md) |
| [`GPLATES_QTWIDGETS_HELLINGERFITWIDGET_H`](../src/qt-widgets/HellingerFitWidget.md#free-functions-and-macros) | [qt-widgets/HellingerFitWidget](../src/qt-widgets/HellingerFitWidget.md) |
| [`GPLATES_QTWIDGETS_HELLINGERMODEL_H`](../src/qt-widgets/HellingerModel.md#free-functions-and-macros) | [qt-widgets/HellingerModel](../src/qt-widgets/HellingerModel.md) |
| [`GPLATES_QTWIDGETS_HELLINGERNEWSEGMENTWARNING_H`](../src/qt-widgets/HellingerNewSegmentWarning.md#free-functions-and-macros) | [qt-widgets/HellingerNewSegmentWarning](../src/qt-widgets/HellingerNewSegmentWarning.md) |
| [`GPLATES_QTWIDGETS_HELLINGERPICKWIDGET_H`](../src/qt-widgets/HellingerPickWidget.md#free-functions-and-macros) | [qt-widgets/HellingerPickWidget](../src/qt-widgets/HellingerPickWidget.md) |
| [`GPLATES_QTWIDGETS_HELLINGERPOINTDIALOG_H`](../src/qt-widgets/HellingerPointDialog.md#free-functions-and-macros) | [qt-widgets/HellingerPointDialog](../src/qt-widgets/HellingerPointDialog.md) |
| [`GPLATES_QTWIDGETS_HELLINGERSEGMENTDIALOG_H`](../src/qt-widgets/HellingerSegmentDialog.md#free-functions-and-macros) | [qt-widgets/HellingerSegmentDialog](../src/qt-widgets/HellingerSegmentDialog.md) |
| [`GPLATES_QTWIDGETS_HELLINGERSTATSDIALOG_H`](../src/qt-widgets/HellingerStatsDialog.md#free-functions-and-macros) | [qt-widgets/HellingerStatsDialog](../src/qt-widgets/HellingerStatsDialog.md) |
| [`GPLATES_QTWIDGETS_HELLINGERTHREAD_H`](../src/qt-widgets/HellingerThread.md#free-functions-and-macros) | [qt-widgets/HellingerThread](../src/qt-widgets/HellingerThread.md) |
| [`GPLATES_QTWIDGETS_IMPORTRASTERDIALOG_H`](../src/qt-widgets/ImportRasterDialog.md#free-functions-and-macros) | [qt-widgets/ImportRasterDialog](../src/qt-widgets/ImportRasterDialog.md) |
| [`GPLATES_QTWIDGETS_INFORMATIONDIALOG_H`](../src/qt-widgets/InformationDialog.md#free-functions-and-macros) | [qt-widgets/InformationDialog](../src/qt-widgets/InformationDialog.md) |
| [`GPLATES_QTWIDGETS_INSERTIONPOINTWIDGET_H`](../src/qt-widgets/InsertionPointWidget.md#free-functions-and-macros) | [qt-widgets/InsertionPointWidget](../src/qt-widgets/InsertionPointWidget.md) |
| [`GPLATES_QTWIDGETS_INSERTVGPRECONSTRUCTIONPOLEDIALOG_H`](../src/qt-widgets/InsertVGPReconstructionPoleDialog.md#free-functions-and-macros) | [qt-widgets/InsertVGPReconstructionPoleDialog](../src/qt-widgets/InsertVGPReconstructionPoleDialog.md) |
| [`GPLATES_QTWIDGETS_INVALIDPROPERTYVALUEEXCEPTION_H`](../src/qt-widgets/InvalidPropertyValueException.md#free-functions-and-macros) | [qt-widgets/InvalidPropertyValueException](../src/qt-widgets/InvalidPropertyValueException.md) |
| [`GPLATES_QTWIDGETS_KINEMATICGRAPHSCONFIGURATIONDIALOG_H`](../src/qt-widgets/KinematicGraphsConfigurationDialog.md#free-functions-and-macros) | [qt-widgets/KinematicGraphsConfigurationDialog](../src/qt-widgets/KinematicGraphsConfigurationDialog.md) |
| [`GPLATES_QTWIDGETS_KINEMATICGRAPHSCONFIGURATIONWIDGET_H`](../src/qt-widgets/KinematicGraphsConfigurationWidget.md#free-functions-and-macros) | [qt-widgets/KinematicGraphsConfigurationWidget](../src/qt-widgets/KinematicGraphsConfigurationWidget.md) |
| [`GPLATES_QTWIDGETS_KINEMATICGRAPHSDIALOG_H`](../src/qt-widgets/KinematicGraphsDialog.md#free-functions-and-macros) | [qt-widgets/KinematicGraphsDialog](../src/qt-widgets/KinematicGraphsDialog.md) |
| [`GPLATES_QTWIDGETS_LATLONCOORDINATESTABLE_H`](../src/qt-widgets/LatLonCoordinatesTable.md#free-functions-and-macros) | [qt-widgets/LatLonCoordinatesTable](../src/qt-widgets/LatLonCoordinatesTable.md) |
| [`GPLATES_QTWIDGETS_LAYEROPTIONSWIDGET_H`](../src/qt-widgets/LayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/LayerOptionsWidget](../src/qt-widgets/LayerOptionsWidget.md) |
| [`GPLATES_QTWIDGETS_LEAVEFULLSCREENBUTTON_H`](../src/qt-widgets/LeaveFullScreenButton.md#free-functions-and-macros) | [qt-widgets/LeaveFullScreenButton](../src/qt-widgets/LeaveFullScreenButton.md) |
| [`GPLATES_QTWIDGETS_LICENSEDIALOG_H`](../src/qt-widgets/LicenseDialog.md#free-functions-and-macros) | [qt-widgets/LicenseDialog](../src/qt-widgets/LicenseDialog.md) |
| [`GPLATES_QTWIDGETS_LINKWIDGET_H`](../src/qt-widgets/LinkWidget.md#free-functions-and-macros) | [qt-widgets/LinkWidget](../src/qt-widgets/LinkWidget.md) |
| [`GPLATES_QTWIDGETS_LOGDIALOG_H`](../src/qt-widgets/LogDialog.md#free-functions-and-macros) | [qt-widgets/LogDialog](../src/qt-widgets/LogDialog.md) |
| [`GPLATES_QTWIDGETS_MANAGEFEATURECOLLECTIONSACTIONWIDGET_H`](../src/qt-widgets/ManageFeatureCollectionsActionWidget.md#free-functions-and-macros) | [qt-widgets/ManageFeatureCollectionsActionWidget](../src/qt-widgets/ManageFeatureCollectionsActionWidget.md) |
| [`GPLATES_QTWIDGETS_MAPCANVAS_H`](../src/qt-widgets/MapCanvas.md#free-functions-and-macros) | [qt-widgets/MapCanvas](../src/qt-widgets/MapCanvas.md) |
| [`GPLATES_QTWIDGETS_MAPVIEW_H`](../src/qt-widgets/MapView.md#free-functions-and-macros) | [qt-widgets/MapView](../src/qt-widgets/MapView.md) |
| [`GPLATES_QTWIDGETS_MEASUREDISTANCEWIDGET_H`](../src/qt-widgets/MeasureDistanceWidget.md#free-functions-and-macros) | [qt-widgets/MeasureDistanceWidget](../src/qt-widgets/MeasureDistanceWidget.md) |
| [`GPLATES_QTWIDGETS_MERGERECONSTRUCTIONLAYERSDIALOG_H`](../src/qt-widgets/MergeReconstructionLayersDialog.md#free-functions-and-macros) | [qt-widgets/MergeReconstructionLayersDialog](../src/qt-widgets/MergeReconstructionLayersDialog.md) |
| [`GPLATES_QTWIDGETS_MISSINGSESSIONFILESDIALOG_H`](../src/qt-widgets/MissingSessionFilesDialog.md#free-functions-and-macros) | [qt-widgets/MissingSessionFilesDialog](../src/qt-widgets/MissingSessionFilesDialog.md) |
| [`GPLATES_QTWIDGETS_MODIFYGEOMETRYWIDGET_H`](../src/qt-widgets/ModifyGeometryWidget.md#free-functions-and-macros) | [qt-widgets/ModifyGeometryWidget](../src/qt-widgets/ModifyGeometryWidget.md) |
| [`GPLATES_QTWIDGETS_MODIFYRECONSTRUCTIONPOLEWIDGET_H`](../src/qt-widgets/ModifyReconstructionPoleWidget.md#free-functions-and-macros) | [qt-widgets/ModifyReconstructionPoleWidget](../src/qt-widgets/ModifyReconstructionPoleWidget.md) |
| [`GPLATES_QTWIDGETS_NOACTIVEEDITWIDGETEXCEPTION_H`](../src/qt-widgets/NoActiveEditWidgetException.md#free-functions-and-macros) | [qt-widgets/NoActiveEditWidgetException](../src/qt-widgets/NoActiveEditWidgetException.md) |
| [`GPLATES_QTWIDGETS_OGRSRSWRITEOPTIONDIALOG_H`](../src/qt-widgets/OgrSrsWriteOptionDialog.md#free-functions-and-macros) | [qt-widgets/OgrSrsWriteOptionDialog](../src/qt-widgets/OgrSrsWriteOptionDialog.md) |
| [`GPLATES_QTWIDGETS_OPENDIRECTORYDIALOG_H`](../src/qt-widgets/OpenDirectoryDialog.md#free-functions-and-macros) | [qt-widgets/OpenDirectoryDialog](../src/qt-widgets/OpenDirectoryDialog.md) |
| [`GPLATES_QTWIDGETS_OPENFILEDIALOG_H`](../src/qt-widgets/OpenFileDialog.md#free-functions-and-macros) | [qt-widgets/OpenFileDialog](../src/qt-widgets/OpenFileDialog.md) |
| [`GPLATES_QTWIDGETS_OPENPROJECTRELATIVEORABSOLUTEDIALOG_H`](../src/qt-widgets/OpenProjectRelativeOrAbsoluteDialog.md#free-functions-and-macros) | [qt-widgets/OpenProjectRelativeOrAbsoluteDialog](../src/qt-widgets/OpenProjectRelativeOrAbsoluteDialog.md) |
| [`GPLATES_QTWIDGETS_POLESEQUENCETABLEWIDGET_H`](../src/qt-widgets/PoleSequenceTableWidget.md#free-functions-and-macros) | [qt-widgets/PoleSequenceTableWidget](../src/qt-widgets/PoleSequenceTableWidget.md) |
| [`GPLATES_QTWIDGETS_PREFERENCESDIALOG_H`](../src/qt-widgets/PreferencesDialog.md#free-functions-and-macros) | [qt-widgets/PreferencesDialog](../src/qt-widgets/PreferencesDialog.md) |
| [`GPLATES_QTWIDGETS_PREFERENCESPANEFILES_H`](../src/qt-widgets/PreferencesPaneFiles.md#free-functions-and-macros) | [qt-widgets/PreferencesPaneFiles](../src/qt-widgets/PreferencesPaneFiles.md) |
| [`GPLATES_QTWIDGETS_PREFERENCESPANEKINEMATICGRAPHS_H`](../src/qt-widgets/PreferencesPaneKinematicGraphs.md#free-functions-and-macros) | [qt-widgets/PreferencesPaneKinematicGraphs](../src/qt-widgets/PreferencesPaneKinematicGraphs.md) |
| [`GPLATES_QTWIDGETS_PREFERENCESPANENETWORK_H`](../src/qt-widgets/PreferencesPaneNetwork.md#free-functions-and-macros) | [qt-widgets/PreferencesPaneNetwork](../src/qt-widgets/PreferencesPaneNetwork.md) |
| [`GPLATES_QTWIDGETS_PREFERENCESPANEVIEW_H`](../src/qt-widgets/PreferencesPaneView.md#free-functions-and-macros) | [qt-widgets/PreferencesPaneView](../src/qt-widgets/PreferencesPaneView.md) |
| [`GPLATES_QTWIDGETS_PREFERENCESPYTHONPANE_H`](../src/qt-widgets/PreferencesPanePython.md#free-functions-and-macros) | [qt-widgets/PreferencesPanePython](../src/qt-widgets/PreferencesPanePython.md) |
| [`GPLATES_QTWIDGETS_PROJECTIONCONTROLWIDGET_H`](../src/qt-widgets/ProjectionControlWidget.md#free-functions-and-macros) | [qt-widgets/ProjectionControlWidget](../src/qt-widgets/ProjectionControlWidget.md) |
| [`GPLATES_QTWIDGETS_PROPERTYVALUENOTSUPPORTEDEXCEPTION_H`](../src/qt-widgets/PropertyValueNotSupportedException.md#free-functions-and-macros) | [qt-widgets/PropertyValueNotSupportedException](../src/qt-widgets/PropertyValueNotSupportedException.md) |
| [`GPLATES_QTWIDGETS_PYTHONARGUMENTWIDGET_H`](../src/qt-widgets/PythonArgumentWidget.md#free-functions-and-macros) | [qt-widgets/PythonArgumentWidget](../src/qt-widgets/PythonArgumentWidget.md) |
| [`GPLATES_QTWIDGETS_PYTHONCONSOLEDIALOG_H`](../src/qt-widgets/PythonConsoleDialog.md#free-functions-and-macros) | [qt-widgets/PythonConsoleDialog](../src/qt-widgets/PythonConsoleDialog.md) |
| [`GPLATES_QTWIDGETS_PYTHONEXECUTIONMONITORWIDGET_H`](../src/qt-widgets/PythonExecutionMonitorWidget.md#free-functions-and-macros) | [qt-widgets/PythonExecutionMonitorWidget](../src/qt-widgets/PythonExecutionMonitorWidget.md) |
| [`GPLATES_QTWIDGETS_PYTHONINITFAILEDDIALOG_H`](../src/qt-widgets/PythonInitFailedDialog.md#free-functions-and-macros) | [qt-widgets/PythonInitFailedDialog](../src/qt-widgets/PythonInitFailedDialog.md) |
| [`GPLATES_QTWIDGETS_PYTHONREADLINEDIALOG_H`](../src/qt-widgets/PythonReadlineDialog.md#free-functions-and-macros) | [qt-widgets/PythonReadlineDialog](../src/qt-widgets/PythonReadlineDialog.md) |
| [`GPLATES_QTWIDGETS_QTWIDGETUTILS_H`](../src/qt-widgets/QtWidgetUtils.md#free-functions-and-macros) | [qt-widgets/QtWidgetUtils](../src/qt-widgets/QtWidgetUtils.md) |
| [`GPLATES_QTWIDGETS_QUERYFEATUREPROPERTIESWIDGET_H`](../src/qt-widgets/QueryFeaturePropertiesWidget.md#free-functions-and-macros) | [qt-widgets/QueryFeaturePropertiesWidget](../src/qt-widgets/QueryFeaturePropertiesWidget.md) |
| [`GPLATES_QTWIDGETS_RASTERBANDPAGE_H`](../src/qt-widgets/RasterBandPage.md#free-functions-and-macros) | [qt-widgets/RasterBandPage](../src/qt-widgets/RasterBandPage.md) |
| [`GPLATES_QTWIDGETS_RASTERFEATURECOLLECTIONPAGE_H`](../src/qt-widgets/RasterFeatureCollectionPage.md#free-functions-and-macros) | [qt-widgets/RasterFeatureCollectionPage](../src/qt-widgets/RasterFeatureCollectionPage.md) |
| [`GPLATES_QTWIDGETS_RASTERGEOREFERENCINGPAGE_H`](../src/qt-widgets/RasterGeoreferencingPage.md#free-functions-and-macros) | [qt-widgets/RasterGeoreferencingPage](../src/qt-widgets/RasterGeoreferencingPage.md) |
| [`GPLATES_QTWIDGETS_RASTERLAYEROPTIONSWIDGET_H`](../src/qt-widgets/RasterLayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/RasterLayerOptionsWidget](../src/qt-widgets/RasterLayerOptionsWidget.md) |
| [`GPLATES_QTWIDGETS_RASTERPROPERTIESDIALOG_H`](../src/qt-widgets/RasterPropertiesDialog.md#free-functions-and-macros) | [qt-widgets/RasterPropertiesDialog](../src/qt-widgets/RasterPropertiesDialog.md) |
| [`GPLATES_QTWIDGETS_RECONSTRUCTIONLAYEROPTIONSWIDGET_H`](../src/qt-widgets/ReconstructionLayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ReconstructionLayerOptionsWidget](../src/qt-widgets/ReconstructionLayerOptionsWidget.md) |
| [`GPLATES_QTWIDGETS_RECONSTRUCTIONPOLEWIDGET_H`](../src/qt-widgets/ReconstructionPoleWidget.md#free-functions-and-macros) | [qt-widgets/ReconstructionPoleWidget](../src/qt-widgets/ReconstructionPoleWidget.md) |
| [`GPLATES_QTWIDGETS_RECONSTRUCTIONVIEWWIDGET_H`](../src/qt-widgets/ReconstructionViewWidget.md#free-functions-and-macros) | [qt-widgets/ReconstructionViewWidget](../src/qt-widgets/ReconstructionViewWidget.md) |
| [`GPLATES_QTWIDGETS_RECONSTRUCTLAYEROPTIONSWIDGET_H`](../src/qt-widgets/ReconstructLayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ReconstructLayerOptionsWidget](../src/qt-widgets/ReconstructLayerOptionsWidget.md) |
| [`GPLATES_QTWIDGETS_SAVEFILEDIALOG_H`](../src/qt-widgets/SaveFileDialog.md#free-functions-and-macros) | [qt-widgets/SaveFileDialog](../src/qt-widgets/SaveFileDialog.md) |
| [`GPLATES_QTWIDGETS_SAVEFILEDIALOGIMPL_H`](../src/qt-widgets/SaveFileDialogImpl.md#free-functions-and-macros) | [qt-widgets/SaveFileDialogImpl](../src/qt-widgets/SaveFileDialogImpl.md) |
| [`GPLATES_QTWIDGETS_SCALARFIELD3DDEPTHLAYERSPAGE_H`](../src/qt-widgets/ScalarField3DDepthLayersPage.md#free-functions-and-macros) | [qt-widgets/ScalarField3DDepthLayersPage](../src/qt-widgets/ScalarField3DDepthLayersPage.md) |
| [`GPLATES_QTWIDGETS_SCALARFIELD3DFEATURECOLLECTIONPAGE_H`](../src/qt-widgets/ScalarField3DFeatureCollectionPage.md#free-functions-and-macros) | [qt-widgets/ScalarField3DFeatureCollectionPage](../src/qt-widgets/ScalarField3DFeatureCollectionPage.md) |
| [`GPLATES_QTWIDGETS_SCALARFIELD3DGEOREFERENCINGPAGE_H`](../src/qt-widgets/ScalarField3DGeoreferencingPage.md#free-functions-and-macros) | [qt-widgets/ScalarField3DGeoreferencingPage](../src/qt-widgets/ScalarField3DGeoreferencingPage.md) |
| [`GPLATES_QTWIDGETS_SCALARFIELD3DLAYEROPTIONSWIDGET_H`](../src/qt-widgets/ScalarField3DLayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/ScalarField3DLayerOptionsWidget](../src/qt-widgets/ScalarField3DLayerOptionsWidget.md) |
| [`GPLATES_QTWIDGETS_SCENEVIEW_H`](../src/qt-widgets/SceneView.md#free-functions-and-macros) | [qt-widgets/SceneView](../src/qt-widgets/SceneView.md) |
| [`GPLATES_QTWIDGETS_SELECTIONWIDGET_H`](../src/qt-widgets/SelectionWidget.md#free-functions-and-macros) | [qt-widgets/SelectionWidget](../src/qt-widgets/SelectionWidget.md) |
| [`GPLATES_QTWIDGETS_SETCAMERAVIEWPOINTDIALOG_H`](../src/qt-widgets/SetCameraViewpointDialog.md#free-functions-and-macros) | [qt-widgets/SetCameraViewpointDialog](../src/qt-widgets/SetCameraViewpointDialog.md) |
| [`GPLATES_QTWIDGETS_SETPROJECTIONDIALOG_H`](../src/qt-widgets/SetProjectionDialog.md#free-functions-and-macros) | [qt-widgets/SetProjectionDialog](../src/qt-widgets/SetProjectionDialog.md) |
| [`GPLATES_QTWIDGETS_SETTOPOLOGYRECONSTRUCTIONPARAMETERSDIALOG_H`](../src/qt-widgets/SetTopologyReconstructionParametersDialog.md#free-functions-and-macros) | [qt-widgets/SetTopologyReconstructionParametersDialog](../src/qt-widgets/SetTopologyReconstructionParametersDialog.md) |
| [`GPLATES_QTWIDGETS_SETVGPVISIBILITYDIALOG_H`](../src/qt-widgets/SetVGPVisibilityDialog.md#free-functions-and-macros) | [qt-widgets/SetVGPVisibilityDialog](../src/qt-widgets/SetVGPVisibilityDialog.md) |
| [`GPLATES_QTWIDGETS_SHAPEFILEATTRIBUTEMAPPERDIALOG_H`](../src/qt-widgets/ShapefileAttributeMapperDialog.md#free-functions-and-macros) | [qt-widgets/ShapefileAttributeMapperDialog](../src/qt-widgets/ShapefileAttributeMapperDialog.md) |
| [`GPLATES_QTWIDGETS_SHAPEFILEATTRIBUTEREMAPPERDIALOG_H`](../src/qt-widgets/ShapefileAttributeRemapperDialog.md#free-functions-and-macros) | [qt-widgets/ShapefileAttributeRemapperDialog](../src/qt-widgets/ShapefileAttributeRemapperDialog.md) |
| [`GPLATES_QTWIDGETS_SHAPEFILEATTRIBUTEVIEWERDIALOG_H`](../src/qt-widgets/ShapefileAttributeViewerDialog.md#free-functions-and-macros) | [qt-widgets/ShapefileAttributeViewerDialog](../src/qt-widgets/ShapefileAttributeViewerDialog.md) |
| [`GPLATES_QTWIDGETS_SHAPEFILEATTRIBUTEWIDGET_H`](../src/qt-widgets/ShapefileAttributeWidget.md#free-functions-and-macros) | [qt-widgets/ShapefileAttributeWidget](../src/qt-widgets/ShapefileAttributeWidget.md) |
| [`GPLATES_QTWIDGETS_SHAPEFILEFILEFORMATCONFIGURATIONDIALOG_H`](../src/qt-widgets/ShapefileFileFormatConfigurationDialog.md#free-functions-and-macros) | [qt-widgets/ShapefileFileFormatConfigurationDialog](../src/qt-widgets/ShapefileFileFormatConfigurationDialog.md) |
| [`GPLATES_QTWIDGETS_SHAPEFILEPROPERTYMAPPER_H`](../src/qt-widgets/ShapefilePropertyMapper.md#free-functions-and-macros) | [qt-widgets/ShapefilePropertyMapper](../src/qt-widgets/ShapefilePropertyMapper.md) |
| [`GPLATES_QTWIDGETS_SMALLCIRCLEMANAGER_H`](../src/qt-widgets/deprecated/SmallCircleManager.md#free-functions-and-macros) | [qt-widgets/deprecated/SmallCircleManager](../src/qt-widgets/deprecated/SmallCircleManager.md) |
| [`GPLATES_QTWIDGETS_SMALLCIRCLEWIDGET_H`](../src/qt-widgets/SmallCircleWidget.md#free-functions-and-macros) | [qt-widgets/SmallCircleWidget](../src/qt-widgets/SmallCircleWidget.md) |
| [`GPLATES_QTWIDGETS_SNAPNEARBYVERTICESWIDGET_H`](../src/qt-widgets/SnapNearbyVerticesWidget.md#free-functions-and-macros) | [qt-widgets/SnapNearbyVerticesWidget](../src/qt-widgets/SnapNearbyVerticesWidget.md) |
| [`GPLATES_QTWIDGETS_SPECIFYANCHOREDPLATEIDDIALOG_H`](../src/qt-widgets/SpecifyAnchoredPlateIdDialog.md#free-functions-and-macros) | [qt-widgets/SpecifyAnchoredPlateIdDialog](../src/qt-widgets/SpecifyAnchoredPlateIdDialog.md) |
| [`GPLATES_QTWIDGETS_SYMBOLMANAGERDIALOG_H`](../src/qt-widgets/SymbolManagerDialog.md#free-functions-and-macros) | [qt-widgets/SymbolManagerDialog](../src/qt-widgets/SymbolManagerDialog.md) |
| [`GPLATES_QTWIDGETS_TASKPANEL_H`](../src/qt-widgets/TaskPanel.md#free-functions-and-macros) | [qt-widgets/TaskPanel](../src/qt-widgets/TaskPanel.md) |
| [`GPLATES_QTWIDGETS_TASKPANELWIDGET_H`](../src/qt-widgets/TaskPanelWidget.md#free-functions-and-macros) | [qt-widgets/TaskPanelWidget](../src/qt-widgets/TaskPanelWidget.md) |
| [`GPLATES_QTWIDGETS_TIMECONTROLWIDGET_H`](../src/qt-widgets/TimeControlWidget.md#free-functions-and-macros) | [qt-widgets/TimeControlWidget](../src/qt-widgets/TimeControlWidget.md) |
| [`GPLATES_QTWIDGETS_TIMEDEPENDENTRASTERPAGE_H`](../src/qt-widgets/TimeDependentRasterPage.md#free-functions-and-macros) | [qt-widgets/TimeDependentRasterPage](../src/qt-widgets/TimeDependentRasterPage.md) |
| [`GPLATES_QTWIDGETS_TOPOLOGYNETWORKRESOLVERLAYEROPTIONSWIDGET_H`](../src/qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md#free-functions-and-macros) | [qt-widgets/TopologyNetworkResolverLayerOptionsWidget](../src/qt-widgets/TopologyNetworkResolverLayerOptionsWidget.md) |
| [`GPLATES_QTWIDGETS_TOPOLOGYTOOLSWIDGET_H`](../src/qt-widgets/TopologyToolsWidget.md#free-functions-and-macros) | [qt-widgets/TopologyToolsWidget](../src/qt-widgets/TopologyToolsWidget.md) |
| [`GPLATES_QTWIDGETS_TOTALRECONSTRUCTIONPOLESDIALOG_H`](../src/qt-widgets/TotalReconstructionPolesDialog.md#free-functions-and-macros) | [qt-widgets/TotalReconstructionPolesDialog](../src/qt-widgets/TotalReconstructionPolesDialog.md) |
| [`GPLATES_QTWIDGETS_TOTALRECONSTRUCTIONSEQUENCESDIALOG_H`](../src/qt-widgets/TotalReconstructionSequencesDialog.md#free-functions-and-macros) | [qt-widgets/TotalReconstructionSequencesDialog](../src/qt-widgets/TotalReconstructionSequencesDialog.md) |
| [`GPLATES_QTWIDGETS_TRINKETICON_H`](../src/qt-widgets/TrinketIcon.md#free-functions-and-macros) | [qt-widgets/TrinketIcon](../src/qt-widgets/TrinketIcon.md) |
| [`GPLATES_QTWIDGETS_UNINITIALISEDEDITWIDGETEXCEPTION_H`](../src/qt-widgets/UninitialisedEditWidgetException.md#free-functions-and-macros) | [qt-widgets/UninitialisedEditWidgetException](../src/qt-widgets/UninitialisedEditWidgetException.md) |
| [`GPLATES_QTWIDGETS_UNSAVEDCHANGESWARNINGDIALOG_H`](../src/qt-widgets/UnsavedChangesWarningDialog.md#free-functions-and-macros) | [qt-widgets/UnsavedChangesWarningDialog](../src/qt-widgets/UnsavedChangesWarningDialog.md) |
| [`GPLATES_QTWIDGETS_VELOCITYMETHODWIDGET_H`](../src/qt-widgets/VelocityMethodWidget.md#free-functions-and-macros) | [qt-widgets/VelocityMethodWidget](../src/qt-widgets/VelocityMethodWidget.md) |
| [`GPLATES_QTWIDGETS_VIEWFEATUREGEOMETRIESWIDGET_H`](../src/qt-widgets/ViewFeatureGeometriesWidget.md#free-functions-and-macros) | [qt-widgets/ViewFeatureGeometriesWidget](../src/qt-widgets/ViewFeatureGeometriesWidget.md) |
| [`GPLATES_QTWIDGETS_VIEWPORTWINDOW_H`](../src/qt-widgets/ViewportWindow.md#free-functions-and-macros) | [qt-widgets/ViewportWindow](../src/qt-widgets/ViewportWindow.md) |
| [`GPLATES_QTWIDGETS_VISUALLAYERSCOMBOBOX_H`](../src/qt-widgets/VisualLayersComboBox.md#free-functions-and-macros) | [qt-widgets/VisualLayersComboBox](../src/qt-widgets/VisualLayersComboBox.md) |
| [`GPLATES_QTWIDGETS_VISUALLAYERSDELEGATE_H`](../src/qt-widgets/VisualLayersDelegate.md#free-functions-and-macros) | [qt-widgets/VisualLayersDelegate](../src/qt-widgets/VisualLayersDelegate.md) |
| [`GPLATES_QTWIDGETS_VISUALLAYERSDIALOG_H`](../src/qt-widgets/VisualLayersDialog.md#free-functions-and-macros) | [qt-widgets/VisualLayersDialog](../src/qt-widgets/VisualLayersDialog.md) |
| [`GPLATES_QTWIDGETS_VISUALLAYERSLISTVIEW_H`](../src/qt-widgets/VisualLayersListView.md#free-functions-and-macros) | [qt-widgets/VisualLayersListView](../src/qt-widgets/VisualLayersListView.md) |
| [`GPLATES_QTWIDGETS_VISUALLAYERSWIDGET_H`](../src/qt-widgets/VisualLayersWidget.md#free-functions-and-macros) | [qt-widgets/VisualLayersWidget](../src/qt-widgets/VisualLayersWidget.md) |
| [`GPLATES_QTWIDGETS_VISUALLAYERWIDGET_H`](../src/qt-widgets/VisualLayerWidget.md#free-functions-and-macros) | [qt-widgets/VisualLayerWidget](../src/qt-widgets/VisualLayerWidget.md) |
| [`GPLATES_QTWIDGETS_ZOOMCONTROLWIDGET_H`](../src/qt-widgets/ZoomControlWidget.md#free-functions-and-macros) | [qt-widgets/ZoomControlWidget](../src/qt-widgets/ZoomControlWidget.md) |
| [`GPLATES_QTWIDGETS_ZOOMSLIDERWIDGET_H`](../src/qt-widgets/ZoomSliderWidget.md#free-functions-and-macros) | [qt-widgets/ZoomSliderWidget](../src/qt-widgets/ZoomSliderWidget.md) |
| [`GPLATES_SCRIBE_SCRIBE_H`](../src/scribe/Scribe.md#free-functions-and-macros) | [scribe/Scribe](../src/scribe/Scribe.md) |
| [`GPLATES_SCRIBE_SCRIBEACCESS_H`](../src/scribe/ScribeAccess.md#free-functions-and-macros) | [scribe/ScribeAccess](../src/scribe/ScribeAccess.md) |
| [`GPLATES_SCRIBE_SCRIBEARCHIVECOMMON_H`](../src/scribe/ScribeArchiveCommon.md#free-functions-and-macros) | [scribe/ScribeArchiveCommon](../src/scribe/ScribeArchiveCommon.md) |
| [`GPLATES_SCRIBE_SCRIBEARCHIVEREADER_H`](../src/scribe/ScribeArchiveReader.md#free-functions-and-macros) | [scribe/ScribeArchiveReader](../src/scribe/ScribeArchiveReader.md) |
| [`GPLATES_SCRIBE_SCRIBEARCHIVEWRITER_H`](../src/scribe/ScribeArchiveWriter.md#free-functions-and-macros) | [scribe/ScribeArchiveWriter](../src/scribe/ScribeArchiveWriter.md) |
| [`GPLATES_SCRIBE_SCRIBEBINARYARCHIVEREADER_H`](../src/scribe/ScribeBinaryArchiveReader.md#free-functions-and-macros) | [scribe/ScribeBinaryArchiveReader](../src/scribe/ScribeBinaryArchiveReader.md) |
| [`GPLATES_SCRIBE_SCRIBEBINARYARCHIVEWRITER_H`](../src/scribe/ScribeBinaryArchiveWriter.md#free-functions-and-macros) | [scribe/ScribeBinaryArchiveWriter](../src/scribe/ScribeBinaryArchiveWriter.md) |
| [`GPLATES_SCRIBE_SCRIBECONSTRUCTOBJECT_H`](../src/scribe/ScribeConstructObject.md#free-functions-and-macros) | [scribe/ScribeConstructObject](../src/scribe/ScribeConstructObject.md) |
| [`GPLATES_SCRIBE_SCRIBEEXCEPTIONS_H`](../src/scribe/ScribeExceptions.md#free-functions-and-macros) | [scribe/ScribeExceptions](../src/scribe/ScribeExceptions.md) |
| [`GPLATES_SCRIBE_SCRIBEEXPORTEXTERNAL_H`](../src/scribe/ScribeExportExternal.md#free-functions-and-macros) | [scribe/ScribeExportExternal](../src/scribe/ScribeExportExternal.md) |
| [`GPLATES_SCRIBE_SCRIBEEXPORTREGISTRATION_H`](../src/scribe/ScribeExportRegistration.md#free-functions-and-macros) | [scribe/ScribeExportRegistration](../src/scribe/ScribeExportRegistration.md) |
| [`GPLATES_SCRIBE_SCRIBEEXPORTREGISTRY_H`](../src/scribe/ScribeExportRegistry.md#free-functions-and-macros) | [scribe/ScribeExportRegistry](../src/scribe/ScribeExportRegistry.md) |
| [`GPLATES_SCRIBE_SCRIBEINTERNALACCESS_H`](../src/scribe/ScribeInternalAccess.md#free-functions-and-macros) | [scribe/ScribeInternalAccess](../src/scribe/ScribeInternalAccess.md) |
| [`GPLATES_SCRIBE_SCRIBEINTERNALUTILS_H`](../src/scribe/ScribeInternalUtils.md#free-functions-and-macros) | [scribe/ScribeInternalUtils](../src/scribe/ScribeInternalUtils.md) |
| [`GPLATES_SCRIBE_SCRIBEINTERNALUTILSIMPL_H`](../src/scribe/ScribeInternalUtilsImpl.md#free-functions-and-macros) | [scribe/ScribeInternalUtilsImpl](../src/scribe/ScribeInternalUtilsImpl.md) |
| [`GPLATES_SCRIBE_SCRIBELOADREF_H`](../src/scribe/ScribeLoadRef.md#free-functions-and-macros) | [scribe/ScribeLoadRef](../src/scribe/ScribeLoadRef.md) |
| [`GPLATES_SCRIBE_SCRIBELOADREFIMPL_H`](../src/scribe/ScribeLoadRefImpl.md#free-functions-and-macros) | [scribe/ScribeLoadRefImpl](../src/scribe/ScribeLoadRefImpl.md) |
| [`GPLATES_SCRIBE_SCRIBEOBJECTTAG_H`](../src/scribe/ScribeObjectTag.md#free-functions-and-macros) | [scribe/ScribeObjectTag](../src/scribe/ScribeObjectTag.md) |
| [`GPLATES_SCRIBE_SCRIBEOPTIONS_H`](../src/scribe/ScribeOptions.md#free-functions-and-macros) | [scribe/ScribeOptions](../src/scribe/ScribeOptions.md) |
| [`GPLATES_SCRIBE_SCRIBESAVELOADCONSTRUCTOBJECT_H`](../src/scribe/ScribeSaveLoadConstructObject.md#free-functions-and-macros) | [scribe/ScribeSaveLoadConstructObject](../src/scribe/ScribeSaveLoadConstructObject.md) |
| [`GPLATES_SCRIBE_SCRIBETEXTARCHIVEREADER_H`](../src/scribe/ScribeTextArchiveReader.md#free-functions-and-macros) | [scribe/ScribeTextArchiveReader](../src/scribe/ScribeTextArchiveReader.md) |
| [`GPLATES_SCRIBE_SCRIBETEXTARCHIVEWRITER_H`](../src/scribe/ScribeTextArchiveWriter.md#free-functions-and-macros) | [scribe/ScribeTextArchiveWriter](../src/scribe/ScribeTextArchiveWriter.md) |
| [`GPLATES_SCRIBE_SCRIBEVOIDCASTREGISTRY_H`](../src/scribe/ScribeVoidCastRegistry.md#free-functions-and-macros) | [scribe/ScribeVoidCastRegistry](../src/scribe/ScribeVoidCastRegistry.md) |
| [`GPLATES_SCRIBE_SCRIBEXMLARCHIVEREADER_H`](../src/scribe/ScribeXmlArchiveReader.md#free-functions-and-macros) | [scribe/ScribeXmlArchiveReader](../src/scribe/ScribeXmlArchiveReader.md) |
| [`GPLATES_SCRIBE_SCRIBEXMLARCHIVEWRITER_H`](../src/scribe/ScribeXmlArchiveWriter.md#free-functions-and-macros) | [scribe/ScribeXmlArchiveWriter](../src/scribe/ScribeXmlArchiveWriter.md) |
| [`GPLATES_SCRIBE_TRANSCRIBE_H`](../src/scribe/Transcribe.md#free-functions-and-macros) | [scribe/Transcribe](../src/scribe/Transcribe.md) |
| [`GPLATES_SCRIBE_TRANSCRIBEARRAY_H`](../src/scribe/TranscribeArray.md#free-functions-and-macros) | [scribe/TranscribeArray](../src/scribe/TranscribeArray.md) |
| [`GPLATES_SCRIBE_TRANSCRIBEBOOST_H`](../src/scribe/TranscribeBoost.md#free-functions-and-macros) | [scribe/TranscribeBoost](../src/scribe/TranscribeBoost.md) |
| [`GPLATES_SCRIBE_TRANSCRIBECONTEXT_H`](../src/scribe/TranscribeContext.md#free-functions-and-macros) | [scribe/TranscribeContext](../src/scribe/TranscribeContext.md) |
| [`GPLATES_SCRIBE_TRANSCRIBEDELEGATEPROTOCOL_H`](../src/scribe/TranscribeDelegateProtocol.md#free-functions-and-macros) | [scribe/TranscribeDelegateProtocol](../src/scribe/TranscribeDelegateProtocol.md) |
| [`GPLATES_SCRIBE_TRANSCRIBEENUMPROTOCOL_H`](../src/scribe/TranscribeEnumProtocol.md#free-functions-and-macros) | [scribe/TranscribeEnumProtocol](../src/scribe/TranscribeEnumProtocol.md) |
| [`GPLATES_SCRIBE_TRANSCRIBEEXTERNAL_H`](../src/scribe/TranscribeExternal.md#free-functions-and-macros) | [scribe/TranscribeExternal](../src/scribe/TranscribeExternal.md) |
| [`GPLATES_SCRIBE_TRANSCRIBEIMPL_H`](../src/scribe/TranscribeImpl.md#free-functions-and-macros) | [scribe/TranscribeImpl](../src/scribe/TranscribeImpl.md) |
| [`GPLATES_SCRIBE_TRANSCRIBEMAPPINGPROTOCOL_H`](../src/scribe/TranscribeMappingProtocol.md#free-functions-and-macros) | [scribe/TranscribeMappingProtocol](../src/scribe/TranscribeMappingProtocol.md) |
| [`GPLATES_SCRIBE_TRANSCRIBENONNULLINTRUSIVEPTR_H`](../src/scribe/TranscribeNonNullIntrusivePtr.md#free-functions-and-macros) | [scribe/TranscribeNonNullIntrusivePtr](../src/scribe/TranscribeNonNullIntrusivePtr.md) |
| [`GPLATES_SCRIBE_TRANSCRIBEQT_H`](../src/scribe/TranscribeQt.md#free-functions-and-macros) | [scribe/TranscribeQt](../src/scribe/TranscribeQt.md) |
| [`GPLATES_SCRIBE_TRANSCRIBERESULT_H`](../src/scribe/TranscribeResult.md#free-functions-and-macros) | [scribe/TranscribeResult](../src/scribe/TranscribeResult.md) |
| [`GPLATES_SCRIBE_TRANSCRIBESEQUENCEPROTOCOL_H`](../src/scribe/TranscribeSequenceProtocol.md#free-functions-and-macros) | [scribe/TranscribeSequenceProtocol](../src/scribe/TranscribeSequenceProtocol.md) |
| [`GPLATES_SCRIBE_TRANSCRIBESMARTPOINTERPROTOCOL_H`](../src/scribe/TranscribeSmartPointerProtocol.md#free-functions-and-macros) | [scribe/TranscribeSmartPointerProtocol](../src/scribe/TranscribeSmartPointerProtocol.md) |
| [`GPLATES_SCRIBE_TRANSCRIBESTD_H`](../src/scribe/TranscribeStd.md#free-functions-and-macros) | [scribe/TranscribeStd](../src/scribe/TranscribeStd.md) |
| [`GPLATES_SCRIBE_TRANSCRIBEUTILS_H`](../src/scribe/TranscribeUtils.md#free-functions-and-macros) | [scribe/TranscribeUtils](../src/scribe/TranscribeUtils.md) |
| [`GPLATES_SCRIBE_TRANSCRIPTION_H`](../src/scribe/Transcription.md#free-functions-and-macros) | [scribe/Transcription](../src/scribe/Transcription.md) |
| [`GPLATES_SCRIBE_TRANSCRIPTIONSCRIBECONTEXT_H`](../src/scribe/TranscriptionScribeContext.md#free-functions-and-macros) | [scribe/TranscriptionScribeContext](../src/scribe/TranscriptionScribeContext.md) |
| [`GPLATES_SRC_CLI_ASSIGN_PLATE_IDS_COMMAND_H`](../src/cli/CliAssignPlateIdsCommand.md#free-functions-and-macros) | [cli/CliAssignPlateIdsCommand](../src/cli/CliAssignPlateIdsCommand.md) |
| [`GPLATES_SRC_CLI_COMMAND_DISPATCHER_H`](../src/cli/CliCommandDispatcher.md#free-functions-and-macros) | [cli/CliCommandDispatcher](../src/cli/CliCommandDispatcher.md) |
| [`GPLATES_SRC_CLI_COMMAND_H`](../src/cli/CliCommand.md#free-functions-and-macros) | [cli/CliCommand](../src/cli/CliCommand.md) |
| [`GPLATES_SRC_CLI_RECONSTRUCT_COMMAND_H`](../src/cli/CliReconstructCommand.md#free-functions-and-macros) | [cli/CliReconstructCommand](../src/cli/CliReconstructCommand.md) |
| [`GPLATES_SYSTEMFIXES_BOOST_CSTDINT_HPP`](../src/system-fixes/boost/cstdint.md#free-functions-and-macros) | [system-fixes/boost/cstdint](../src/system-fixes/boost/cstdint.md) |
| [`GPLATES_UNIT_PRESENTATION_TEST_SUITE_H`](../src/unit-test/PresentationTestSuite.md#free-functions-and-macros) | [unit-test/PresentationTestSuite](../src/unit-test/PresentationTestSuite.md) |
| [`GPLATES_UNIT_TEST_APP_LOGIC_TEST_SUITE_H`](../src/unit-test/AppLogicTestSuite.md#free-functions-and-macros) | [unit-test/AppLogicTestSuite](../src/unit-test/AppLogicTestSuite.md) |
| [`GPLATES_UNIT_TEST_APPLICATIONSTATE_TEST_H`](../src/unit-test/ApplicationStateTest.md#free-functions-and-macros) | [unit-test/ApplicationStateTest](../src/unit-test/ApplicationStateTest.md) |
| [`GPLATES_UNIT_TEST_CANVAS_TOOLS_TEST_SUITE_H`](../src/unit-test/CanvasToolsTestSuite.md#free-functions-and-macros) | [unit-test/CanvasToolsTestSuite](../src/unit-test/CanvasToolsTestSuite.md) |
| [`GPLATES_UNIT_TEST_COREG_TEST_H`](../src/unit-test/CoregTest.md#free-functions-and-macros) | [unit-test/CoregTest](../src/unit-test/CoregTest.md) |
| [`GPLATES_UNIT_TEST_CPTPALETTE_TEST_H`](../src/unit-test/CptPaletteTest.md#free-functions-and-macros) | [unit-test/CptPaletteTest](../src/unit-test/CptPaletteTest.md) |
| [`GPLATES_UNIT_TEST_DA_DATATABLE_H`](../src/unit-test/DataAssociationDataTableTest.md#free-functions-and-macros) | [unit-test/DataAssociationDataTableTest](../src/unit-test/DataAssociationDataTableTest.md) |
| [`GPLATES_UNIT_TEST_DATA_MINING_TEST_SUITE_H`](../src/unit-test/DataMiningTestSuite.md#free-functions-and-macros) | [unit-test/DataMiningTestSuite](../src/unit-test/DataMiningTestSuite.md) |
| [`GPLATES_UNIT_TEST_FEATURE_VISITORS_TEST_SUITE_H`](../src/unit-test/FeatureVisitorsTestSuite.md#free-functions-and-macros) | [unit-test/FeatureVisitorsTestSuite](../src/unit-test/FeatureVisitorsTestSuite.md) |
| [`GPLATES_UNIT_TEST_FEATUREHANDLE_TEST_H`](../src/unit-test/FeatureHandleTest.md#free-functions-and-macros) | [unit-test/FeatureHandleTest](../src/unit-test/FeatureHandleTest.md) |
| [`GPLATES_UNIT_TEST_FILE_IO_TEST_SUITE_H`](../src/unit-test/FileIoTestSuite.md#free-functions-and-macros) | [unit-test/FileIoTestSuite](../src/unit-test/FileIoTestSuite.md) |
| [`GPLATES_UNIT_TEST_FILTER_TEST_H`](../src/unit-test/FilterTest.md#free-functions-and-macros) | [unit-test/FilterTest](../src/unit-test/FilterTest.md) |
| [`GPLATES_UNIT_TEST_GENERATE_VELOCITY_DOMAIN_CITCOMS_TEST_H`](../src/unit-test/GenerateVelocityDomainCitcomsTest.md#free-functions-and-macros) | [unit-test/GenerateVelocityDomainCitcomsTest](../src/unit-test/GenerateVelocityDomainCitcomsTest.md) |
| [`GPLATES_UNIT_TEST_GEOMETRY_VISITORS_APP_LOGIC_TEST_SUITE_H`](../src/unit-test/GeometryVisitorsTestSuite.md#free-functions-and-macros) | [unit-test/GeometryVisitorsTestSuite](../src/unit-test/GeometryVisitorsTestSuite.md) |
| [`GPLATES_UNIT_TEST_GLOBAL_TEST_SUITE_H`](../src/unit-test/GlobalTestSuite.md#free-functions-and-macros) | [unit-test/GlobalTestSuite](../src/unit-test/GlobalTestSuite.md) |
| [`GPLATES_UNIT_TEST_GLOBALFIXTURE_H`](../src/unit-test/GPlatesGlobalFixture.md#free-functions-and-macros) | [unit-test/GPlatesGlobalFixture](../src/unit-test/GPlatesGlobalFixture.md) |
| [`GPLATES_UNIT_TEST_GPLATESTESTSUITE_H`](../src/unit-test/GPlatesTestSuite.md#free-functions-and-macros) | [unit-test/GPlatesTestSuite](../src/unit-test/GPlatesTestSuite.md) |
| [`GPLATES_UNIT_TEST_GUI_TEST_SUITE_H`](../src/unit-test/GuiTestSuite.md#free-functions-and-macros) | [unit-test/GuiTestSuite](../src/unit-test/GuiTestSuite.md) |
| [`GPLATES_UNIT_TEST_MAINTESTSUITE_H`](../src/unit-test/MainTestSuite.md#free-functions-and-macros) | [unit-test/MainTestSuite](../src/unit-test/MainTestSuite.md) |
| [`GPLATES_UNIT_TEST_MATHS_TEST_SUITE_H`](../src/unit-test/MathsTestSuite.md#free-functions-and-macros) | [unit-test/MathsTestSuite](../src/unit-test/MathsTestSuite.md) |
| [`GPLATES_UNIT_TEST_MODEL_TEST_SUITE_H`](../src/unit-test/ModelTestSuite.md#free-functions-and-macros) | [unit-test/ModelTestSuite](../src/unit-test/ModelTestSuite.md) |
| [`GPLATES_UNIT_TEST_MULTITHREAD_TEST_H`](../src/unit-test/MultiThreadTest.md#free-functions-and-macros) | [unit-test/MultiThreadTest](../src/unit-test/MultiThreadTest.md) |
| [`GPLATES_UNIT_TEST_PROPERTYVALUES_TEST_SUITE_H`](../src/unit-test/PropertyValuesTestSuite.md#free-functions-and-macros) | [unit-test/PropertyValuesTestSuite](../src/unit-test/PropertyValuesTestSuite.md) |
| [`GPLATES_UNIT_TEST_REAL_TEST_H`](../src/unit-test/MipmapperTest.md#free-functions-and-macros) | [unit-test/MipmapperTest](../src/unit-test/MipmapperTest.md) |
| [`GPLATES_UNIT_TEST_REAL_TEST_H`](../src/unit-test/RealTest.md#free-functions-and-macros) | [unit-test/RealTest](../src/unit-test/RealTest.md) |
| [`GPLATES_UNIT_TEST_SCRIBEEXPORTUNITTEST_H`](../src/unit-test/ScribeExportUnitTest.md#free-functions-and-macros) | [unit-test/ScribeExportUnitTest](../src/unit-test/ScribeExportUnitTest.md) |
| [`GPLATES_UNIT_TEST_SCRIBETESTSUITE_H`](../src/unit-test/ScribeTestSuite.md#free-functions-and-macros) | [unit-test/ScribeTestSuite](../src/unit-test/ScribeTestSuite.md) |
| [`GPLATES_UNIT_TEST_SMARTNODELINKEDLIST_TEST_H`](../src/unit-test/SmartNodeLinkedListTest.md#free-functions-and-macros) | [unit-test/SmartNodeLinkedListTest](../src/unit-test/SmartNodeLinkedListTest.md) |
| [`GPLATES_UNIT_TEST_STRINGSET_TEST_H`](../src/unit-test/StringSetTest.md#free-functions-and-macros) | [unit-test/StringSetTest](../src/unit-test/StringSetTest.md) |
| [`GPLATES_UNIT_TEST_TESTSUITEFILTER_H`](../src/unit-test/TestSuiteFilter.md#free-functions-and-macros) | [unit-test/TestSuiteFilter](../src/unit-test/TestSuiteFilter.md) |
| [`GPLATES_UNIT_TEST_TESTSUITEFILTER_TEST_H`](../src/unit-test/TestSuiteFilterTest.md#free-functions-and-macros) | [unit-test/TestSuiteFilterTest](../src/unit-test/TestSuiteFilterTest.md) |
| [`GPLATES_UNIT_TEST_TRANSCRIBE_TEST_H`](../src/unit-test/TranscribeTest.md#free-functions-and-macros) | [unit-test/TranscribeTest](../src/unit-test/TranscribeTest.md) |
| [`GPLATES_UNIT_TEST_UNIT_TEST_TEST_SUITE_H`](../src/unit-test/UnitTestTestSuite.md#free-functions-and-macros) | [unit-test/UnitTestTestSuite](../src/unit-test/UnitTestTestSuite.md) |
| [`GPLATES_UNIT_TEST_UTILS_TEST_SUITE_H`](../src/unit-test/UtilsTestSuite.md#free-functions-and-macros) | [unit-test/UtilsTestSuite](../src/unit-test/UtilsTestSuite.md) |
| [`GPLATES_UNIT_TEST_VIEW_OPERATIONS_TEST_SUITE_H`](../src/unit-test/ViewOperationsTestSuite.md#free-functions-and-macros) | [unit-test/ViewOperationsTestSuite](../src/unit-test/ViewOperationsTestSuite.md) |
| [`GPLATES_UTILS_ANIMATIONSEQUENCEUTILS_H`](../src/utils/AnimationSequenceUtils.md#free-functions-and-macros) | [utils/AnimationSequenceUtils](../src/utils/AnimationSequenceUtils.md) |
| [`GPLATES_UTILS_BASE2UTILS_H`](../src/utils/Base2Utils.md#free-functions-and-macros) | [utils/Base2Utils](../src/utils/Base2Utils.md) |
| [`GPLATES_UTILS_BINARYREDUCER_H`](../src/utils/deprecated/BinaryReducer.md#free-functions-and-macros) | [utils/deprecated/BinaryReducer](../src/utils/deprecated/BinaryReducer.md) |
| [`GPLATES_UTILS_CALLSTACKTRACKER_H`](../src/utils/CallStackTracker.md#free-functions-and-macros) | [utils/CallStackTracker](../src/utils/CallStackTracker.md) |
| [`GPLATES_UTILS_COMMAND_LINE_PARSER_H`](../src/utils/CommandLineParser.md#free-functions-and-macros) | [utils/CommandLineParser](../src/utils/CommandLineParser.md) |
| [`GPLATES_UTILS_COMPONENT_MANAGER_H`](../src/utils/ComponentManager.md#free-functions-and-macros) | [utils/ComponentManager](../src/utils/ComponentManager.md) |
| [`GPLATES_UTILS_CONFIGBUNDLE_H`](../src/utils/ConfigBundle.md#free-functions-and-macros) | [utils/ConfigBundle](../src/utils/ConfigBundle.md) |
| [`GPLATES_UTILS_CONFIGBUNDLEUTILS_H`](../src/utils/ConfigBundleUtils.md#free-functions-and-macros) | [utils/ConfigBundleUtils](../src/utils/ConfigBundleUtils.md) |
| [`GPLATES_UTILS_CONFIGINTERFACE_H`](../src/utils/ConfigInterface.md#free-functions-and-macros) | [utils/ConfigInterface](../src/utils/ConfigInterface.md) |
| [`GPLATES_UTILS_COPYCONST_H`](../src/utils/CopyConst.md#free-functions-and-macros) | [utils/CopyConst](../src/utils/CopyConst.md) |
| [`GPLATES_UTILS_COPYONWRITEPOINTER_H`](../src/utils/CopyOnWrite.md#free-functions-and-macros) | [utils/CopyOnWrite](../src/utils/CopyOnWrite.md) |
| [`GPLATES_UTILS_COUNTER64_H`](../src/utils/Counter64.md#free-functions-and-macros) | [utils/Counter64](../src/utils/Counter64.md) |
| [`GPLATES_UTILS_DEFERREDCALLEVENT_H`](../src/utils/DeferredCallEvent.md#free-functions-and-macros) | [utils/DeferredCallEvent](../src/utils/DeferredCallEvent.md) |
| [`GPLATES_UTILS_EARTH_H`](../src/utils/Earth.md#free-functions-and-macros) | [utils/Earth](../src/utils/Earth.md) |
| [`GPLATES_UTILS_ENDIAN_H`](../src/utils/Endian.md#free-functions-and-macros) | [utils/Endian](../src/utils/Endian.md) |
| [`GPLATES_UTILS_ENVIRONMENT_H`](../src/utils/Environment.md#free-functions-and-macros) | [utils/Environment](../src/utils/Environment.md) |
| [`GPLATES_UTILS_FEATUREHANDLETOOLDID_H`](../src/utils/deprecated/FeatureHandleToOldId.md#free-functions-and-macros) | [utils/deprecated/FeatureHandleToOldId](../src/utils/deprecated/FeatureHandleToOldId.md) |
| [`GPLATES_UTILS_FEATUREUTILS_H`](../src/utils/FeatureUtils.md#free-functions-and-macros) | [utils/FeatureUtils](../src/utils/FeatureUtils.md) |
| [`GPLATES_UTILS_FILTER_H`](../src/utils/deprecated/Filter.md#free-functions-and-macros) | [utils/deprecated/Filter](../src/utils/deprecated/Filter.md) |
| [`GPLATES_UTILS_FILTERMAPOUTPUTHANDLER_H`](../src/utils/deprecated/FilterMapOutputHandler.md#free-functions-and-macros) | [utils/deprecated/FilterMapOutputHandler](../src/utils/deprecated/FilterMapOutputHandler.md) |
| [`GPLATES_UTILS_FILTERMAPREDUCEWORKFLOW_H`](../src/utils/deprecated/FilterMapReduceWorkFlow.md#free-functions-and-macros) | [utils/deprecated/FilterMapReduceWorkFlow](../src/utils/deprecated/FilterMapReduceWorkFlow.md) |
| [`GPLATES_UTILS_FUNCTIONTYPES_H`](../src/utils/FunctionTypes.md#free-functions-and-macros) | [utils/FunctionTypes](../src/utils/FunctionTypes.md) |
| [`GPLATES_UTILS_GENERICFILTER_H`](../src/utils/deprecated/GenericFilter.md#free-functions-and-macros) | [utils/deprecated/GenericFilter](../src/utils/deprecated/GenericFilter.md) |
| [`GPLATES_UTILS_GENERICREDUCER_H`](../src/utils/deprecated/GenericReducer.md#free-functions-and-macros) | [utils/deprecated/GenericReducer](../src/utils/deprecated/GenericReducer.md) |
| [`GPLATES_UTILS_GENERICREDUCERIMPL_H`](../src/utils/deprecated/GenericReducerImpl.md#free-functions-and-macros) | [utils/deprecated/GenericReducerImpl](../src/utils/deprecated/GenericReducerImpl.md) |
| [`GPLATES_UTILS_GENERICTRANSFORMER_H`](../src/utils/deprecated/GenericMapper.md#free-functions-and-macros) | [utils/deprecated/GenericMapper](../src/utils/deprecated/GenericMapper.md) |
| [`GPLATES_UTILS_GENERICTRANSFORMERIMPL_H`](../src/utils/deprecated/GenericMapperImpl.md#free-functions-and-macros) | [utils/deprecated/GenericMapperImpl](../src/utils/deprecated/GenericMapperImpl.md) |
| [`GPLATES_UTILS_GEOMETRYCREATIONUTILS_H`](../src/utils/GeometryCreationUtils.md#free-functions-and-macros) | [utils/GeometryCreationUtils](../src/utils/GeometryCreationUtils.md) |
| [`GPLATES_UTILS_HASFUNCTION_H`](../src/utils/HasFunction.md#free-functions-and-macros) | [utils/HasFunction](../src/utils/HasFunction.md) |
| [`GPLATES_UTILS_IDSTRINGSET_H`](../src/utils/IdStringSet.md#free-functions-and-macros) | [utils/IdStringSet](../src/utils/IdStringSet.md) |
| [`GPLATES_UTILS_INTRUSIVESINGLYLINKEDLIST_H`](../src/utils/IntrusiveSinglyLinkedList.md#free-functions-and-macros) | [utils/IntrusiveSinglyLinkedList](../src/utils/IntrusiveSinglyLinkedList.md) |
| [`GPLATES_UTILS_KEYVALUECACHE_H`](../src/utils/KeyValueCache.md#free-functions-and-macros) | [utils/KeyValueCache](../src/utils/KeyValueCache.md) |
| [`GPLATES_UTILS_LATLONAREASAMPLING_H`](../src/utils/LatLonAreaSampling.md#free-functions-and-macros) | [utils/LatLonAreaSampling](../src/utils/LatLonAreaSampling.md) |
| [`GPLATES_UTILS_NETWORKUTILS_H`](../src/utils/NetworkUtils.md#free-functions-and-macros) | [utils/NetworkUtils](../src/utils/NetworkUtils.md) |
| [`GPLATES_UTILS_NULLINTRUSIVEPOINTERHANDLER_H`](../src/utils/NullIntrusivePointerHandler.md#free-functions-and-macros) | [utils/NullIntrusivePointerHandler](../src/utils/NullIntrusivePointerHandler.md) |
| [`GPLATES_UTILS_NULLNONNULLINTRUSIVEPOINTEREXCEPTION_H`](../src/utils/NullNonNullIntrusivePointerException.md#free-functions-and-macros) | [utils/NullNonNullIntrusivePointerException](../src/utils/NullNonNullIntrusivePointerException.md) |
| [`GPLATES_UTILS_OBJECTCACHE_H`](../src/utils/ObjectCache.md#free-functions-and-macros) | [utils/ObjectCache](../src/utils/ObjectCache.md) |
| [`GPLATES_UTILS_OBJECTPOOL_H`](../src/utils/ObjectPool.md#free-functions-and-macros) | [utils/ObjectPool](../src/utils/ObjectPool.md) |
| [`GPLATES_UTILS_OVERLOADRESOLUTION_H`](../src/utils/OverloadResolution.md#free-functions-and-macros) | [utils/OverloadResolution](../src/utils/OverloadResolution.md) |
| [`GPLATES_UTILS_PARSE_H`](../src/utils/Parse.md#free-functions-and-macros) | [utils/Parse](../src/utils/Parse.md) |
| [`GPLATES_UTILS_PREDICATEFILTER_H`](../src/utils/deprecated/PredicateFilter.md#free-functions-and-macros) | [utils/deprecated/PredicateFilter](../src/utils/deprecated/PredicateFilter.md) |
| [`GPLATES_UTILS_PROFILE_H`](../src/utils/Profile.md#free-functions-and-macros) | [utils/Profile](../src/utils/Profile.md) |
| [`GPLATES_UTILS_QTFORMATTINGUTILS_H`](../src/utils/QtFormattingUtils.md#free-functions-and-macros) | [utils/QtFormattingUtils](../src/utils/QtFormattingUtils.md) |
| [`GPLATES_UTILS_QTSTREAMABLE_H`](../src/utils/QtStreamable.md#free-functions-and-macros) | [utils/QtStreamable](../src/utils/QtStreamable.md) |
| [`GPLATES_UTILS_REDUCER_H`](../src/utils/Reducer.md#free-functions-and-macros) | [utils/Reducer](../src/utils/Reducer.md) |
| [`GPLATES_UTILS_REFERENCECOUNT_H`](../src/utils/ReferenceCount.md#free-functions-and-macros) | [utils/ReferenceCount](../src/utils/ReferenceCount.md) |
| [`GPLATES_UTILS_SAFEBOOL_H`](../src/utils/SafeBool.md#free-functions-and-macros) | [utils/SafeBool](../src/utils/SafeBool.md) |
| [`GPLATES_UTILS_SELECT_H`](../src/utils/Select.md#free-functions-and-macros) | [utils/Select](../src/utils/Select.md) |
| [`GPLATES_UTILS_SETCONST_H`](../src/utils/SetConst.md#free-functions-and-macros) | [utils/SetConst](../src/utils/SetConst.md) |
| [`GPLATES_UTILS_SINGLETON_H`](../src/utils/Singleton.md#free-functions-and-macros) | [utils/Singleton](../src/utils/Singleton.md) |
| [`GPLATES_UTILS_SMARTNODELINKEDLIST_H`](../src/utils/SmartNodeLinkedList.md#free-functions-and-macros) | [utils/SmartNodeLinkedList](../src/utils/SmartNodeLinkedList.md) |
| [`GPLATES_UTILS_STRINGFORMATTINGUTILS_H`](../src/utils/StringFormattingUtils.md#free-functions-and-macros) | [utils/StringFormattingUtils](../src/utils/StringFormattingUtils.md) |
| [`GPLATES_UTILS_STRINGSET_H`](../src/utils/StringSet.md#free-functions-and-macros) | [utils/StringSet](../src/utils/StringSet.md) |
| [`GPLATES_UTILS_STRINGUTILS_H`](../src/utils/StringUtils.md#free-functions-and-macros) | [utils/StringUtils](../src/utils/StringUtils.md) |
| [`GPLATES_UTILS_SUBJECTOBSERVERTOKEN_H`](../src/utils/SubjectObserverToken.md#free-functions-and-macros) | [utils/SubjectObserverToken](../src/utils/SubjectObserverToken.md) |
| [`GPLATES_UTILS_TRANSFORMER_H`](../src/utils/Mapper.md#free-functions-and-macros) | [utils/Mapper](../src/utils/Mapper.md) |
| [`GPLATES_UTILS_TYPETRAITS_H`](../src/utils/TypeTraits.md#free-functions-and-macros) | [utils/TypeTraits](../src/utils/TypeTraits.md) |
| [`GPLATES_UTILS_UNARYTRANSFORMER_H`](../src/utils/deprecated/UnaryMapper.md#free-functions-and-macros) | [utils/deprecated/UnaryMapper](../src/utils/deprecated/UnaryMapper.md) |
| [`GPLATES_UTILS_UNICODESTRING_H`](../src/utils/UnicodeString.md#free-functions-and-macros) | [utils/UnicodeString](../src/utils/UnicodeString.md) |
| [`GPLATES_UTILS_UNICODESTRINGUTILS_H`](../src/utils/UnicodeStringUtils.md#free-functions-and-macros) | [utils/UnicodeStringUtils](../src/utils/UnicodeStringUtils.md) |
| [`GPLATES_UTILS_UNIQUEID_H`](../src/utils/UniqueId.md#free-functions-and-macros) | [utils/UniqueId](../src/utils/UniqueId.md) |
| [`GPLATES_UTILS_VIRTUALPROXY_H`](../src/utils/VirtualProxy.md#free-functions-and-macros) | [utils/VirtualProxy](../src/utils/VirtualProxy.md) |
| [`GPLATES_UTILS_XMLNAMESPACES_H`](../src/utils/XmlNamespaces.md#free-functions-and-macros) | [utils/XmlNamespaces](../src/utils/XmlNamespaces.md) |
| [`GPLATES_UTILS_XPATH_H`](../src/utils/XPath.md#free-functions-and-macros) | [utils/XPath](../src/utils/XPath.md) |
| [`GPLATES_UTILS_XQUERYUTILS_H`](../src/utils/XQueryUtils.md#free-functions-and-macros) | [utils/XQueryUtils](../src/utils/XQueryUtils.md) |
| [`GPLATES_VIEW_OPERATIONS_CHANGELIGHTDIRECTIONOPERATION_H`](../src/view-operations/ChangeLightDirectionOperation.md#free-functions-and-macros) | [view-operations/ChangeLightDirectionOperation](../src/view-operations/ChangeLightDirectionOperation.md) |
| [`GPLATES_VIEW_OPERATIONS_MOVEPOLEOPERATION_H`](../src/view-operations/MovePoleOperation.md#free-functions-and-macros) | [view-operations/MovePoleOperation](../src/view-operations/MovePoleOperation.md) |
| [`GPLATES_VIEW_OPERATIONS_RENDEREDRESOLVEDSCALARFIELD3D_H`](../src/view-operations/RenderedResolvedScalarField3D.md#free-functions-and-macros) | [view-operations/RenderedResolvedScalarField3D](../src/view-operations/RenderedResolvedScalarField3D.md) |
| [`GPLATES_VIEW_OPERATIONS_SCALARFIELD3DRENDERPARAMETERS_H`](../src/view-operations/ScalarField3DRenderParameters.md#free-functions-and-macros) | [view-operations/ScalarField3DRenderParameters](../src/view-operations/ScalarField3DRenderParameters.md) |
| [`GPLATES_VIEWOPERATIONS_ADDPOINTGEOMETRYOPERATION_H`](../src/view-operations/AddPointGeometryOperation.md#free-functions-and-macros) | [view-operations/AddPointGeometryOperation](../src/view-operations/AddPointGeometryOperation.md) |
| [`GPLATES_VIEWOPERATIONS_CLONEOPERATION_H`](../src/view-operations/CloneOperation.md#free-functions-and-macros) | [view-operations/CloneOperation](../src/view-operations/CloneOperation.md) |
| [`GPLATES_VIEWOPERATIONS_DELETEFEATUREOPERATION_H`](../src/view-operations/DeleteFeatureOperation.md#free-functions-and-macros) | [view-operations/DeleteFeatureOperation](../src/view-operations/DeleteFeatureOperation.md) |
| [`GPLATES_VIEWOPERATIONS_DELETEVERTEXGEOMETRYOPERATION_H`](../src/view-operations/DeleteVertexGeometryOperation.md#free-functions-and-macros) | [view-operations/DeleteVertexGeometryOperation](../src/view-operations/DeleteVertexGeometryOperation.md) |
| [`GPLATES_VIEWOPERATIONS_FOCUSEDFEATUREGEOMETRYMANIPULATOR_H`](../src/view-operations/FocusedFeatureGeometryManipulator.md#free-functions-and-macros) | [view-operations/FocusedFeatureGeometryManipulator](../src/view-operations/FocusedFeatureGeometryManipulator.md) |
| [`GPLATES_VIEWOPERATIONS_GEOMETRYBUILDER_H`](../src/view-operations/GeometryBuilder.md#free-functions-and-macros) | [view-operations/GeometryBuilder](../src/view-operations/GeometryBuilder.md) |
| [`GPLATES_VIEWOPERATIONS_GEOMETRYBUILDERUNDOCOMMANDS_H`](../src/view-operations/GeometryBuilderUndoCommands.md#free-functions-and-macros) | [view-operations/GeometryBuilderUndoCommands](../src/view-operations/GeometryBuilderUndoCommands.md) |
| [`GPLATES_VIEWOPERATIONS_GEOMETRYOPERATION_H`](../src/view-operations/GeometryOperation.md#free-functions-and-macros) | [view-operations/GeometryOperation](../src/view-operations/GeometryOperation.md) |
| [`GPLATES_VIEWOPERATIONS_GEOMETRYOPERATIONUNDO_H`](../src/view-operations/GeometryOperationUndo.md#free-functions-and-macros) | [view-operations/GeometryOperationUndo](../src/view-operations/GeometryOperationUndo.md) |
| [`GPLATES_VIEWOPERATIONS_INSERTVERTEXGEOMETRYOPERATION_H`](../src/view-operations/InsertVertexGeometryOperation.md#free-functions-and-macros) | [view-operations/InsertVertexGeometryOperation](../src/view-operations/InsertVertexGeometryOperation.md) |
| [`GPLATES_VIEWOPERATIONS_INTERNALGEOMETRYBUILDER_H`](../src/view-operations/InternalGeometryBuilder.md#free-functions-and-macros) | [view-operations/InternalGeometryBuilder](../src/view-operations/InternalGeometryBuilder.md) |
| [`GPLATES_VIEWOPERATIONS_MOVEVERTEXGEOMETRYOPERATION_H`](../src/view-operations/MoveVertexGeometryOperation.md#free-functions-and-macros) | [view-operations/MoveVertexGeometryOperation](../src/view-operations/MoveVertexGeometryOperation.md) |
| [`GPLATES_VIEWOPERATIONS_QUERYPROXIMITYTHRESHOLD_H`](../src/view-operations/QueryProximityThreshold.md#free-functions-and-macros) | [view-operations/QueryProximityThreshold](../src/view-operations/QueryProximityThreshold.md) |
| [`GPLATES_VIEWOPERATIONS_RENDERED_SUBDUCTION_TEETH_POLYLINE_H`](../src/view-operations/RenderedSubductionTeethPolyline.md#free-functions-and-macros) | [view-operations/RenderedSubductionTeethPolyline](../src/view-operations/RenderedSubductionTeethPolyline.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDARROWEDPOLYLINE_H`](../src/view-operations/RenderedArrowedPolyline.md#free-functions-and-macros) | [view-operations/RenderedArrowedPolyline](../src/view-operations/RenderedArrowedPolyline.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDCIRCLESYMBOL_H`](../src/view-operations/RenderedCircleSymbol.md#free-functions-and-macros) | [view-operations/RenderedCircleSymbol](../src/view-operations/RenderedCircleSymbol.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDEDGESURFACEMESH_H`](../src/view-operations/RenderedColouredEdgeSurfaceMesh.md#free-functions-and-macros) | [view-operations/RenderedColouredEdgeSurfaceMesh](../src/view-operations/RenderedColouredEdgeSurfaceMesh.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDMULTIPOINTONSPHERE_H`](../src/view-operations/RenderedColouredMultiPointOnSphere.md#free-functions-and-macros) | [view-operations/RenderedColouredMultiPointOnSphere](../src/view-operations/RenderedColouredMultiPointOnSphere.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDPOLYGONONSPHERE_H`](../src/view-operations/RenderedColouredPolygonOnSphere.md#free-functions-and-macros) | [view-operations/RenderedColouredPolygonOnSphere](../src/view-operations/RenderedColouredPolygonOnSphere.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDPOLYLINEONSPHERE_H`](../src/view-operations/RenderedColouredPolylineOnSphere.md#free-functions-and-macros) | [view-operations/RenderedColouredPolylineOnSphere](../src/view-operations/RenderedColouredPolylineOnSphere.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDCOLOUREDTRIANGLESURFACEMESH_H`](../src/view-operations/RenderedColouredTriangleSurfaceMesh.md#free-functions-and-macros) | [view-operations/RenderedColouredTriangleSurfaceMesh](../src/view-operations/RenderedColouredTriangleSurfaceMesh.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDCROSSSYMBOL_H`](../src/view-operations/RenderedCrossSymbol.md#free-functions-and-macros) | [view-operations/RenderedCrossSymbol](../src/view-operations/RenderedCrossSymbol.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDELLIPSE_H`](../src/view-operations/RenderedEllipse.md#free-functions-and-macros) | [view-operations/RenderedEllipse](../src/view-operations/RenderedEllipse.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYCOLLECTION_H`](../src/view-operations/RenderedGeometryCollection.md#free-functions-and-macros) | [view-operations/RenderedGeometryCollection](../src/view-operations/RenderedGeometryCollection.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYCOLLECTIONUTILS_H`](../src/view-operations/RenderedGeometryUtils.md#free-functions-and-macros) | [view-operations/RenderedGeometryUtils](../src/view-operations/RenderedGeometryUtils.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYCOLLECTIONVISITOR_H`](../src/view-operations/RenderedGeometryCollectionVisitor.md#free-functions-and-macros) | [view-operations/RenderedGeometryCollectionVisitor](../src/view-operations/RenderedGeometryCollectionVisitor.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYFACTORY_H`](../src/view-operations/RenderedGeometryFactory.md#free-functions-and-macros) | [view-operations/RenderedGeometryFactory](../src/view-operations/RenderedGeometryFactory.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYIMPL_H`](../src/view-operations/RenderedGeometryImpl.md#free-functions-and-macros) | [view-operations/RenderedGeometryImpl](../src/view-operations/RenderedGeometryImpl.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYLAYER_H`](../src/view-operations/RenderedGeometryLayer.md#free-functions-and-macros) | [view-operations/RenderedGeometryLayer](../src/view-operations/RenderedGeometryLayer.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYLAYERVISITOR_H`](../src/view-operations/RenderedGeometryLayerVisitor.md#free-functions-and-macros) | [view-operations/RenderedGeometryLayerVisitor](../src/view-operations/RenderedGeometryLayerVisitor.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYPARAMETERS_H`](../src/view-operations/RenderedGeometryParameters.md#free-functions-and-macros) | [view-operations/RenderedGeometryParameters](../src/view-operations/RenderedGeometryParameters.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYPROXIMITY_H`](../src/view-operations/RenderedGeometryProximity.md#free-functions-and-macros) | [view-operations/RenderedGeometryProximity](../src/view-operations/RenderedGeometryProximity.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDGEOMETRYVISITOR_H`](../src/view-operations/RenderedGeometryVisitor.md#free-functions-and-macros) | [view-operations/RenderedGeometryVisitor](../src/view-operations/RenderedGeometryVisitor.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDMULTIPOINTONSPHERE_H`](../src/view-operations/RenderedMultiPointOnSphere.md#free-functions-and-macros) | [view-operations/RenderedMultiPointOnSphere](../src/view-operations/RenderedMultiPointOnSphere.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDMULTIRECONSTRUCTIONGEOMETRY_H`](../src/view-operations/RenderedMultiReconstructionGeometry.md#free-functions-and-macros) | [view-operations/RenderedMultiReconstructionGeometry](../src/view-operations/RenderedMultiReconstructionGeometry.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDPOINTONSPHERE_H`](../src/view-operations/RenderedPointOnSphere.md#free-functions-and-macros) | [view-operations/RenderedPointOnSphere](../src/view-operations/RenderedPointOnSphere.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDPOLYGONONSPHERE_H`](../src/view-operations/RenderedPolygonOnSphere.md#free-functions-and-macros) | [view-operations/RenderedPolygonOnSphere](../src/view-operations/RenderedPolygonOnSphere.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDPOLYLINEONSPHERE_H`](../src/view-operations/RenderedPolylineOnSphere.md#free-functions-and-macros) | [view-operations/RenderedPolylineOnSphere](../src/view-operations/RenderedPolylineOnSphere.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDRADIALARROW_H`](../src/view-operations/RenderedRadialArrow.md#free-functions-and-macros) | [view-operations/RenderedRadialArrow](../src/view-operations/RenderedRadialArrow.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDRECONSTRUCTIONGEOMETRY_H`](../src/view-operations/RenderedReconstructionGeometry.md#free-functions-and-macros) | [view-operations/RenderedReconstructionGeometry](../src/view-operations/RenderedReconstructionGeometry.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDRESOLVEDRASTER_H`](../src/view-operations/RenderedResolvedRaster.md#free-functions-and-macros) | [view-operations/RenderedResolvedRaster](../src/view-operations/RenderedResolvedRaster.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDSMALLCIRCLE_H`](../src/view-operations/RenderedSmallCircle.md#free-functions-and-macros) | [view-operations/RenderedSmallCircle](../src/view-operations/RenderedSmallCircle.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDSMALLCIRCLEARC_H`](../src/view-operations/RenderedSmallCircleArc.md#free-functions-and-macros) | [view-operations/RenderedSmallCircleArc](../src/view-operations/RenderedSmallCircleArc.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDSQUARESYMBOL_H`](../src/view-operations/RenderedSquareSymbol.md#free-functions-and-macros) | [view-operations/RenderedSquareSymbol](../src/view-operations/RenderedSquareSymbol.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDSTRAINMARKERSYMBOL_H`](../src/view-operations/RenderedStrainMarkerSymbol.md#free-functions-and-macros) | [view-operations/RenderedStrainMarkerSymbol](../src/view-operations/RenderedStrainMarkerSymbol.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDSTRING_H`](../src/view-operations/RenderedString.md#free-functions-and-macros) | [view-operations/RenderedString](../src/view-operations/RenderedString.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDTANGENTIALARROW_H`](../src/view-operations/RenderedTangentialArrow.md#free-functions-and-macros) | [view-operations/RenderedTangentialArrow](../src/view-operations/RenderedTangentialArrow.md) |
| [`GPLATES_VIEWOPERATIONS_RENDEREDTRIANGLESYMBOL_H`](../src/view-operations/RenderedTriangleSymbol.md#free-functions-and-macros) | [view-operations/RenderedTriangleSymbol](../src/view-operations/RenderedTriangleSymbol.md) |
| [`GPLATES_VIEWOPERATIONS_SPLITFEATUREGEOMETRYOPERATION_H`](../src/view-operations/SplitFeatureGeometryOperation.md#free-functions-and-macros) | [view-operations/SplitFeatureGeometryOperation](../src/view-operations/SplitFeatureGeometryOperation.md) |
| [`GPLATES_VIEWOPERATIONS_SPLITFEATUREUNDOCOMMAND_H`](../src/view-operations/SplitFeatureUndoCommand.md#free-functions-and-macros) | [view-operations/SplitFeatureUndoCommand](../src/view-operations/SplitFeatureUndoCommand.md) |
| [`GPLATES_VIEWOPERATIONS_UNDOREDO_H`](../src/view-operations/UndoRedo.md#free-functions-and-macros) | [view-operations/UndoRedo](../src/view-operations/UndoRedo.md) |
| [`GPLATES_VIEWOPERATIONS_VISIBLERECONSTRUCTIONGEOMETRYEXPORT_H`](../src/view-operations/VisibleReconstructionGeometryExport.md#free-functions-and-macros) | [view-operations/VisibleReconstructionGeometryExport](../src/view-operations/VisibleReconstructionGeometryExport.md) |
| [`GPLATES_WIDGETS_CREATEFEATUREIDLISTDIALOG_H`](../src/qt-widgets/deprecated/CreateFeatureIdListDialog.md#free-functions-and-macros) | [qt-widgets/deprecated/CreateFeatureIdListDialog](../src/qt-widgets/deprecated/CreateFeatureIdListDialog.md) |
| [`GPLATES_WIDGETS_CREATEFEATUREIDLISTMODEL_H`](../src/qt-widgets/deprecated/CreateFeatureIdListModel.md#free-functions-and-macros) | [qt-widgets/deprecated/CreateFeatureIdListModel](../src/qt-widgets/deprecated/CreateFeatureIdListModel.md) |
| [`GPLATESAPPLOGIC_TRSUTILS_H`](../src/app-logic/TRSUtils.md#free-functions-and-macros) | [app-logic/TRSUtils](../src/app-logic/TRSUtils.md) |
| [`GPLATESDATAMINING_ASSOCIATIONOPERATORFACTORY_H`](../src/data-mining/deprecated/AssociationOperatorFactory.md#free-functions-and-macros) | [data-mining/deprecated/AssociationOperatorFactory](../src/data-mining/deprecated/AssociationOperatorFactory.md) |
| [`GPLATESDATAMINING_CHECKATTRTYPEVISITOR_H`](../src/data-mining/CheckAttrTypeVisitor.md#free-functions-and-macros) | [data-mining/CheckAttrTypeVisitor](../src/data-mining/CheckAttrTypeVisitor.md) |
| [`GPLATESDATAMINING_COREGCONFIGURATIONTABLE_H`](../src/data-mining/CoRegConfigurationTable.md#free-functions-and-macros) | [data-mining/CoRegConfigurationTable](../src/data-mining/CoRegConfigurationTable.md) |
| [`GPLATESDATAMINING_COREGFILTER_H`](../src/data-mining/CoRegFilter.md#free-functions-and-macros) | [data-mining/CoRegFilter](../src/data-mining/CoRegFilter.md) |
| [`GPLATESDATAMINING_COREGFILTERCACHE_H`](../src/data-mining/CoRegFilterCache.md#free-functions-and-macros) | [data-mining/CoRegFilterCache](../src/data-mining/CoRegFilterCache.md) |
| [`GPLATESDATAMINING_COREGFILTERMAPREDUCEFACTORY_H`](../src/data-mining/CoRegFilterMapReduceFactory.md#free-functions-and-macros) | [data-mining/CoRegFilterMapReduceFactory](../src/data-mining/CoRegFilterMapReduceFactory.md) |
| [`GPLATESDATAMINING_COREGMAPPER_H`](../src/data-mining/CoRegMapper.md#free-functions-and-macros) | [data-mining/CoRegMapper](../src/data-mining/CoRegMapper.md) |
| [`GPLATESDATAMINING_COREGREDUCER_H`](../src/data-mining/CoRegReducer.md#free-functions-and-macros) | [data-mining/CoRegReducer](../src/data-mining/CoRegReducer.md) |
| [`GPLATESDATAMINING_DATAASSOCIATIONFACTORY_H`](../src/data-mining/deprecated/DataOperatorFactory.md#free-functions-and-macros) | [data-mining/deprecated/DataOperatorFactory](../src/data-mining/deprecated/DataOperatorFactory.md) |
| [`GPLATESDATAMINING_DATAMININGCACHE_H`](../src/data-mining/DataMiningCache.md#free-functions-and-macros) | [data-mining/DataMiningCache](../src/data-mining/DataMiningCache.md) |
| [`GPLATESDATAMINING_DATAMININGUTILS_H`](../src/data-mining/DataMiningUtils.md#free-functions-and-macros) | [data-mining/DataMiningUtils](../src/data-mining/DataMiningUtils.md) |
| [`GPLATESDATAMINING_DATAOPERATOR_H`](../src/data-mining/deprecated/DataOperator.md#free-functions-and-macros) | [data-mining/deprecated/DataOperator](../src/data-mining/deprecated/DataOperator.md) |
| [`GPLATESDATAMINING_DATASELECTOR_H`](../src/data-mining/DataSelector.md#free-functions-and-macros) | [data-mining/DataSelector](../src/data-mining/DataSelector.md) |
| [`GPLATESDATAMINING_DATATABLE_H`](../src/data-mining/DataTable.md#free-functions-and-macros) | [data-mining/DataTable](../src/data-mining/DataTable.md) |
| [`GPLATESDATAMINING_DISTANCEDATAOPERATOR_H`](../src/data-mining/deprecated/DistanceDataOperator.md#free-functions-and-macros) | [data-mining/deprecated/DistanceDataOperator](../src/data-mining/deprecated/DistanceDataOperator.md) |
| [`GPLATESDATAMINING_GETPROPERTYASPYTHONOBJVISITOR_H`](../src/utils/GetPropertyAsPythonObjVisitor.md#free-functions-and-macros) | [utils/GetPropertyAsPythonObjVisitor](../src/utils/GetPropertyAsPythonObjVisitor.md) |
| [`GPLATESDATAMINING_GETVALUEFROMPROPERTYVISITOR_H`](../src/data-mining/GetValueFromPropertyVisitor.md#free-functions-and-macros) | [data-mining/GetValueFromPropertyVisitor](../src/data-mining/GetValueFromPropertyVisitor.md) |
| [`GPLATESDATAMINING_ISINREGIONOFINTERESTVISITOR_H`](../src/data-mining/deprecated/IsInRegionOfInterestVisitor.md#free-functions-and-macros) | [data-mining/deprecated/IsInRegionOfInterestVisitor](../src/data-mining/deprecated/IsInRegionOfInterestVisitor.md) |
| [`GPLATESDATAMINING_LOOKUPDATAOPERATOR_H`](../src/data-mining/deprecated/LookupDataOperator.md#free-functions-and-macros) | [data-mining/deprecated/LookupDataOperator](../src/data-mining/deprecated/LookupDataOperator.md) |
| [`GPLATESDATAMINING_LOOKUPREDUCER_H`](../src/data-mining/LookupReducer.md#free-functions-and-macros) | [data-mining/LookupReducer](../src/data-mining/LookupReducer.md) |
| [`GPLATESDATAMINING_MAXDISTANCEDATAOPERATOR_H`](../src/data-mining/deprecated/MaxDistanceDataOperator.md#free-functions-and-macros) | [data-mining/deprecated/MaxDistanceDataOperator](../src/data-mining/deprecated/MaxDistanceDataOperator.md) |
| [`GPLATESDATAMINING_MAXREDUCER_H`](../src/data-mining/MaxReducer.md#free-functions-and-macros) | [data-mining/MaxReducer](../src/data-mining/MaxReducer.md) |
| [`GPLATESDATAMINING_MEANDISTANCEDATAOPERATOR_H`](../src/data-mining/deprecated/MeanDistanceDataOperator.md#free-functions-and-macros) | [data-mining/deprecated/MeanDistanceDataOperator](../src/data-mining/deprecated/MeanDistanceDataOperator.md) |
| [`GPLATESDATAMINING_MEANREDUCER_H`](../src/data-mining/MeanReducer.md#free-functions-and-macros) | [data-mining/MeanReducer](../src/data-mining/MeanReducer.md) |
| [`GPLATESDATAMINING_MEDIANDISTANCEDATAOPERATOR_H`](../src/data-mining/deprecated/MedianDistanceDataOperator.md#free-functions-and-macros) | [data-mining/deprecated/MedianDistanceDataOperator](../src/data-mining/deprecated/MedianDistanceDataOperator.md) |
| [`GPLATESDATAMINING_MEDIANREDUCER_H`](../src/data-mining/MedianReducer.md#free-functions-and-macros) | [data-mining/MedianReducer](../src/data-mining/MedianReducer.md) |
| [`GPLATESDATAMINING_MINDATAOPERATOR_H`](../src/data-mining/deprecated/MinDataOperator.md#free-functions-and-macros) | [data-mining/deprecated/MinDataOperator](../src/data-mining/deprecated/MinDataOperator.md) |
| [`GPLATESDATAMINING_MINDISTANCEDATAOPERATOR_H`](../src/data-mining/deprecated/MinDistanceDataOperator.md#free-functions-and-macros) | [data-mining/deprecated/MinDistanceDataOperator](../src/data-mining/deprecated/MinDistanceDataOperator.md) |
| [`GPLATESDATAMINING_MINREDUCER_H`](../src/data-mining/MinReducer.md#free-functions-and-macros) | [data-mining/MinReducer](../src/data-mining/MinReducer.md) |
| [`GPLATESDATAMINING_NUMINROIDATAOPERATOR_H`](../src/data-mining/deprecated/NumInROIDataOperator.md#free-functions-and-macros) | [data-mining/deprecated/NumInROIDataOperator](../src/data-mining/deprecated/NumInROIDataOperator.md) |
| [`GPLATESDATAMINING_OPAQUEDATA_H`](../src/data-mining/OpaqueData.md#free-functions-and-macros) | [data-mining/OpaqueData](../src/data-mining/OpaqueData.md) |
| [`GPLATESDATAMINING_OPAQUEDATATODOUBLE_H`](../src/data-mining/OpaqueDataToDouble.md#free-functions-and-macros) | [data-mining/OpaqueDataToDouble](../src/data-mining/OpaqueDataToDouble.md) |
| [`GPLATESDATAMINING_OPAQUEDATAVISITORS_H`](../src/data-mining/OpaqueDataToQString.md#free-functions-and-macros) | [data-mining/OpaqueDataToQString](../src/data-mining/OpaqueDataToQString.md) |
| [`GPLATESDATAMINING_PERCENTILEREDUCER_H`](../src/data-mining/PercentileReducer.md#free-functions-and-macros) | [data-mining/PercentileReducer](../src/data-mining/PercentileReducer.md) |
| [`GPLATESDATAMINING_PRESENCEDATAOPERATOR_H`](../src/data-mining/deprecated/PresenceDataOperator.md#free-functions-and-macros) | [data-mining/deprecated/PresenceDataOperator](../src/data-mining/deprecated/PresenceDataOperator.md) |
| [`GPLATESDATAMINING_PROSPECTOR_H`](../src/data-mining/deprecated/Prospector.md#free-functions-and-macros) | [data-mining/deprecated/Prospector](../src/data-mining/deprecated/Prospector.md) |
| [`GPLATESDATAMINING_REDUCERTYPES_H`](../src/data-mining/Types.md#free-functions-and-macros) | [data-mining/Types](../src/data-mining/Types.md) |
| [`GPLATESDATAMINING_REGIONOFINTERESTASSOCIATIONOPERATOR_H`](../src/data-mining/deprecated/RegionOfInterestAssociationOperator.md#free-functions-and-macros) | [data-mining/deprecated/RegionOfInterestAssociationOperator](../src/data-mining/deprecated/RegionOfInterestAssociationOperator.md) |
| [`GPLATESDATAMINING_REGIONOFINTERESTFILTER_H`](../src/data-mining/RegionOfInterestFilter.md#free-functions-and-macros) | [data-mining/RegionOfInterestFilter](../src/data-mining/RegionOfInterestFilter.md) |
| [`GPLATESDATAMINING_RFGTOPROPERTYVALUEMAPPER_H`](../src/data-mining/RFGToPropertyValueMapper.md#free-functions-and-macros) | [data-mining/RFGToPropertyValueMapper](../src/data-mining/RFGToPropertyValueMapper.md) |
| [`GPLATESDATAMINING_RFGTORELATIONALPROPERTYMAPPER_H`](../src/data-mining/RFGToRelationalPropertyMapper.md#free-functions-and-macros) | [data-mining/RFGToRelationalPropertyMapper](../src/data-mining/RFGToRelationalPropertyMapper.md) |
| [`GPLATESDATAMINING_SEEDSELFFILTER_H`](../src/data-mining/SeedSelfFilter.md#free-functions-and-macros) | [data-mining/SeedSelfFilter](../src/data-mining/SeedSelfFilter.md) |
| [`GPLATESDATAMINING_SUBDATASELECTOR_H`](../src/data-mining/deprecated/SubDataSelector.md#free-functions-and-macros) | [data-mining/deprecated/SubDataSelector](../src/data-mining/deprecated/SubDataSelector.md) |
| [`GPLATESDATAMINING_TASKQUEUE_H`](../src/data-mining/deprecated/TaskQueue.md#free-functions-and-macros) | [data-mining/deprecated/TaskQueue](../src/data-mining/deprecated/TaskQueue.md) |
| [`GPLATESDATAMINING_VOTEREDUCER_H`](../src/data-mining/VoteReducer.md#free-functions-and-macros) | [data-mining/VoteReducer](../src/data-mining/VoteReducer.md) |
| [`GPLATESDATAMINING_WEIGHTEDMEANREDUCER_H`](../src/data-mining/WeightedMeanReducer.md#free-functions-and-macros) | [data-mining/WeightedMeanReducer](../src/data-mining/WeightedMeanReducer.md) |
| [`HELLINGERCONFIGURATIONDIALOG_H`](../src/qt-widgets/HellingerConfigurationDialog.md#free-functions-and-macros) | [qt-widgets/HellingerConfigurationDialog](../src/qt-widgets/HellingerConfigurationDialog.md) |
| [`HELLINGERCONFIGURATIONWIDGET_H`](../src/qt-widgets/HellingerConfigurationWidget.md#free-functions-and-macros) | [qt-widgets/HellingerConfigurationWidget](../src/qt-widgets/HellingerConfigurationWidget.md) |
| [`KINEMATICGRAPHPICKER_H`](../src/qt-widgets/KinematicGraphPicker.md#free-functions-and-macros) | [qt-widgets/KinematicGraphPicker](../src/qt-widgets/KinematicGraphPicker.md) |
| [`LOKI_REFTOVALUE_H`](../src/system-fixes/loki/RefToValue.md#free-functions-and-macros) | [system-fixes/loki/RefToValue](../src/system-fixes/loki/RefToValue.md) |
| [`LOKI_SCOPEGUARD_H_`](../src/system-fixes/loki/ScopeGuard.md#free-functions-and-macros) | [system-fixes/loki/ScopeGuard](../src/system-fixes/loki/ScopeGuard.md) |
| [`METADATA_DIALOG_H`](../src/qt-widgets/MetadataDialog.md#free-functions-and-macros) | [qt-widgets/MetadataDialog](../src/qt-widgets/MetadataDialog.md) |
| [`PROGRESS_DIALOG_H`](../src/qt-widgets/ProgressDialog.md#free-functions-and-macros) | [qt-widgets/ProgressDialog](../src/qt-widgets/ProgressDialog.md) |
