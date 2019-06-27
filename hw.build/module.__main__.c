/* Generated code for Python module '__main__'
 * created by Nuitka version 0.6.3.1
 *
 * This code is in part copyright 2019 Kay Hayen.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "nuitka/prelude.h"

#include "__helpers.h"

/* The "_module___main__" is a Python object pointer of module type.
 *
 * Note: For full compatibility with CPython, every module variable access
 * needs to go through it except for cases where the module cannot possibly
 * have changed in the mean time.
 */

PyObject *module___main__;
PyDictObject *moduledict___main__;

/* The declarations of module constants used, if any. */
static PyObject *const_str_plain_main;
static PyObject *const_str_digest_af09b5465318a1dbcf049fc5d56a3d48;
extern PyObject *const_str_plain___file__;
static PyObject *const_str_digest_c2e08a163d3eb76cb8e2fac825f44837;
extern PyObject *const_int_0;
extern PyObject *const_str_plain_print;
extern PyObject *const_str_plain_site;
static PyObject *const_str_plain_talk;
static PyObject *const_str_digest_2c872ba3691aed37a9f4d19e29288a31;
static PyObject *const_str_plain_message;
static PyObject *const_str_angle_module;
static PyObject *const_tuple_str_plain_message_tuple;
extern PyObject *const_tuple_empty;
extern PyObject *const_str_plain___main__;
static PyObject *const_str_plain___annotations__;
extern PyObject *const_str_plain___doc__;
extern PyObject *const_str_plain___cached__;
static PyObject *const_tuple_str_digest_af09b5465318a1dbcf049fc5d56a3d48_tuple;
static PyObject *module_filename_obj;

/* Indicator if this modules private constants were created yet. */
static bool constants_created = false;

/* Function to create module private constants. */
static void createModuleConstants( void )
{
    const_str_plain_main = UNSTREAM_STRING_ASCII( &constant_bin[ 0 ], 4, 1 );
    const_str_digest_af09b5465318a1dbcf049fc5d56a3d48 = UNSTREAM_STRING_ASCII( &constant_bin[ 4 ], 11, 0 );
    const_str_digest_c2e08a163d3eb76cb8e2fac825f44837 = UNSTREAM_STRING_ASCII( &constant_bin[ 15 ], 5, 0 );
    const_str_plain_talk = UNSTREAM_STRING_ASCII( &constant_bin[ 20 ], 4, 1 );
    const_str_digest_2c872ba3691aed37a9f4d19e29288a31 = UNSTREAM_STRING_ASCII( &constant_bin[ 24 ], 5, 0 );
    const_str_plain_message = UNSTREAM_STRING_ASCII( &constant_bin[ 29 ], 7, 1 );
    const_str_angle_module = UNSTREAM_STRING_ASCII( &constant_bin[ 36 ], 8, 0 );
    const_tuple_str_plain_message_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_plain_message_tuple, 0, const_str_plain_message ); Py_INCREF( const_str_plain_message );
    const_str_plain___annotations__ = UNSTREAM_STRING_ASCII( &constant_bin[ 44 ], 15, 1 );
    const_tuple_str_digest_af09b5465318a1dbcf049fc5d56a3d48_tuple = PyTuple_New( 1 );
    PyTuple_SET_ITEM( const_tuple_str_digest_af09b5465318a1dbcf049fc5d56a3d48_tuple, 0, const_str_digest_af09b5465318a1dbcf049fc5d56a3d48 ); Py_INCREF( const_str_digest_af09b5465318a1dbcf049fc5d56a3d48 );

    constants_created = true;
}

/* Function to verify module private constants for non-corruption. */
#ifndef __NUITKA_NO_ASSERT__
void checkModuleConstants___main__( void )
{
    // The module may not have been used at all, then ignore this.
    if (constants_created == false) return;


}
#endif

// The module code objects.
static PyCodeObject *codeobj_6c565e902b4e680a75ba298785b20d24;
static PyCodeObject *codeobj_aab6665c7d7da82ddfd6d5e961ab4869;
static PyCodeObject *codeobj_50320aa795b05b9fb9f611b975852c56;
/* For use in "MainProgram.c". */
PyCodeObject *codeobj_main = NULL;

static void createModuleCodeObjects(void)
{
    module_filename_obj = MAKE_RELATIVE_PATH( const_str_digest_2c872ba3691aed37a9f4d19e29288a31 );
    codeobj_6c565e902b4e680a75ba298785b20d24 = MAKE_CODEOBJ( module_filename_obj, const_str_angle_module, 1, const_tuple_empty, 0, 0, CO_NOFREE );
    codeobj_main = codeobj_6c565e902b4e680a75ba298785b20d24;
    codeobj_aab6665c7d7da82ddfd6d5e961ab4869 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_main, 4, const_tuple_empty, 0, 0, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
    codeobj_50320aa795b05b9fb9f611b975852c56 = MAKE_CODEOBJ( module_filename_obj, const_str_plain_talk, 1, const_tuple_str_plain_message_tuple, 1, 0, CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE );
}

// The module function declarations.
static PyObject *MAKE_FUNCTION___main__$$$function_1_talk(  );


static PyObject *MAKE_FUNCTION___main__$$$function_2_main(  );


// The module function definitions.
static PyObject *impl___main__$$$function_1_talk( struct Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    PyObject *par_message = python_pars[ 0 ];
    struct Nuitka_FrameObject *frame_50320aa795b05b9fb9f611b975852c56;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *tmp_return_value = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_50320aa795b05b9fb9f611b975852c56 = NULL;
    PyObject *exception_keeper_type_1;
    PyObject *exception_keeper_value_1;
    PyTracebackObject *exception_keeper_tb_1;
    NUITKA_MAY_BE_UNUSED int exception_keeper_lineno_1;

    // Actual function body.
    // Tried code:
    MAKE_OR_REUSE_FRAME( cache_frame_50320aa795b05b9fb9f611b975852c56, codeobj_50320aa795b05b9fb9f611b975852c56, module___main__, sizeof(void *) );
    frame_50320aa795b05b9fb9f611b975852c56 = cache_frame_50320aa795b05b9fb9f611b975852c56;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_50320aa795b05b9fb9f611b975852c56 );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert( Py_REFCNT( frame_50320aa795b05b9fb9f611b975852c56 ) == 2 ); // Frame stack

    // Framed code:
    {
        PyObject *tmp_left_name_1;
        PyObject *tmp_right_name_1;
        tmp_left_name_1 = const_str_digest_c2e08a163d3eb76cb8e2fac825f44837;
        CHECK_OBJECT( par_message );
        tmp_right_name_1 = par_message;
        tmp_return_value = BINARY_OPERATION_ADD_UNICODE_OBJECT( tmp_left_name_1, tmp_right_name_1 );
        if ( tmp_return_value == NULL )
        {
            assert( ERROR_OCCURRED() );

            FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


            exception_lineno = 2;
            type_description_1 = "o";
            goto frame_exception_exit_1;
        }
        goto frame_return_exit_1;
    }

#if 0
    RESTORE_FRAME_EXCEPTION( frame_50320aa795b05b9fb9f611b975852c56 );
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_return_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_50320aa795b05b9fb9f611b975852c56 );
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto try_return_handler_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION( frame_50320aa795b05b9fb9f611b975852c56 );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_50320aa795b05b9fb9f611b975852c56, exception_lineno );
    }
    else if ( exception_tb->tb_frame != &frame_50320aa795b05b9fb9f611b975852c56->m_frame )
    {
        exception_tb = ADD_TRACEBACK( exception_tb, frame_50320aa795b05b9fb9f611b975852c56, exception_lineno );
    }

    // Attachs locals to frame if any.
    Nuitka_Frame_AttachLocals(
        (struct Nuitka_FrameObject *)frame_50320aa795b05b9fb9f611b975852c56,
        type_description_1,
        par_message
    );


    // Release cached frame.
    if ( frame_50320aa795b05b9fb9f611b975852c56 == cache_frame_50320aa795b05b9fb9f611b975852c56 )
    {
        Py_DECREF( frame_50320aa795b05b9fb9f611b975852c56 );
    }
    cache_frame_50320aa795b05b9fb9f611b975852c56 = NULL;

    assertFrameObject( frame_50320aa795b05b9fb9f611b975852c56 );

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto try_except_handler_1;

    frame_no_exception_1:;
    // tried codes exits in all cases
    NUITKA_CANNOT_GET_HERE( __main__$$$function_1_talk );
    return NULL;
    // Return handler code:
    try_return_handler_1:;
    CHECK_OBJECT( (PyObject *)par_message );
    Py_DECREF( par_message );
    par_message = NULL;

    goto function_return_exit;
    // Exception handler code:
    try_except_handler_1:;
    exception_keeper_type_1 = exception_type;
    exception_keeper_value_1 = exception_value;
    exception_keeper_tb_1 = exception_tb;
    exception_keeper_lineno_1 = exception_lineno;
    exception_type = NULL;
    exception_value = NULL;
    exception_tb = NULL;
    exception_lineno = 0;

    CHECK_OBJECT( (PyObject *)par_message );
    Py_DECREF( par_message );
    par_message = NULL;

    // Re-raise.
    exception_type = exception_keeper_type_1;
    exception_value = exception_keeper_value_1;
    exception_tb = exception_keeper_tb_1;
    exception_lineno = exception_keeper_lineno_1;

    goto function_exception_exit;
    // End of try:

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( __main__$$$function_1_talk );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT( tmp_return_value );
   assert( had_error || !ERROR_OCCURRED() );
   return tmp_return_value;
}


static PyObject *impl___main__$$$function_2_main( struct Nuitka_FunctionObject const *self, PyObject **python_pars )
{
    // Preserve error status for checks
#ifndef __NUITKA_NO_ASSERT__
    NUITKA_MAY_BE_UNUSED bool had_error = ERROR_OCCURRED();
#endif

    // Local variable declarations.
    struct Nuitka_FrameObject *frame_aab6665c7d7da82ddfd6d5e961ab4869;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;
    static struct Nuitka_FrameObject *cache_frame_aab6665c7d7da82ddfd6d5e961ab4869 = NULL;
    PyObject *tmp_return_value = NULL;

    // Actual function body.
    MAKE_OR_REUSE_FRAME( cache_frame_aab6665c7d7da82ddfd6d5e961ab4869, codeobj_aab6665c7d7da82ddfd6d5e961ab4869, module___main__, 0 );
    frame_aab6665c7d7da82ddfd6d5e961ab4869 = cache_frame_aab6665c7d7da82ddfd6d5e961ab4869;

    // Push the new frame as the currently active one.
    pushFrameStack( frame_aab6665c7d7da82ddfd6d5e961ab4869 );

    // Mark the frame object as in use, ref count 1 will be up for reuse.
    assert( Py_REFCNT( frame_aab6665c7d7da82ddfd6d5e961ab4869 ) == 2 ); // Frame stack

    // Framed code:
    {
        PyObject *tmp_called_name_1;
        PyObject *tmp_call_result_1;
        PyObject *tmp_args_element_name_1;
        PyObject *tmp_called_name_2;
        PyObject *tmp_mvar_value_1;
        tmp_called_name_1 = LOOKUP_BUILTIN( const_str_plain_print );
        assert( tmp_called_name_1 != NULL );
        tmp_mvar_value_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_talk );

        if (unlikely( tmp_mvar_value_1 == NULL ))
        {
            tmp_mvar_value_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_talk );
        }

        if ( tmp_mvar_value_1 == NULL )
        {

            exception_type = PyExc_NameError;
            Py_INCREF( exception_type );
            exception_value = PyUnicode_FromFormat( "name '%s' is not defined", "talk" );
            exception_tb = NULL;
            NORMALIZE_EXCEPTION( &exception_type, &exception_value, &exception_tb );
            CHAIN_EXCEPTION( exception_value );

            exception_lineno = 5;

            goto frame_exception_exit_1;
        }

        tmp_called_name_2 = tmp_mvar_value_1;
        frame_aab6665c7d7da82ddfd6d5e961ab4869->m_frame.f_lineno = 5;
        tmp_args_element_name_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_2, &PyTuple_GET_ITEM( const_tuple_str_digest_af09b5465318a1dbcf049fc5d56a3d48_tuple, 0 ) );

        if ( tmp_args_element_name_1 == NULL )
        {
            assert( ERROR_OCCURRED() );

            FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


            exception_lineno = 5;

            goto frame_exception_exit_1;
        }
        frame_aab6665c7d7da82ddfd6d5e961ab4869->m_frame.f_lineno = 5;
        {
            PyObject *call_args[] = { tmp_args_element_name_1 };
            tmp_call_result_1 = CALL_FUNCTION_WITH_ARGS1( tmp_called_name_1, call_args );
        }

        Py_DECREF( tmp_args_element_name_1 );
        if ( tmp_call_result_1 == NULL )
        {
            assert( ERROR_OCCURRED() );

            FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


            exception_lineno = 5;

            goto frame_exception_exit_1;
        }
        Py_DECREF( tmp_call_result_1 );
    }

#if 0
    RESTORE_FRAME_EXCEPTION( frame_aab6665c7d7da82ddfd6d5e961ab4869 );
#endif

    // Put the previous frame back on top.
    popFrameStack();

    goto frame_no_exception_1;

    frame_exception_exit_1:;

#if 0
    RESTORE_FRAME_EXCEPTION( frame_aab6665c7d7da82ddfd6d5e961ab4869 );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_aab6665c7d7da82ddfd6d5e961ab4869, exception_lineno );
    }
    else if ( exception_tb->tb_frame != &frame_aab6665c7d7da82ddfd6d5e961ab4869->m_frame )
    {
        exception_tb = ADD_TRACEBACK( exception_tb, frame_aab6665c7d7da82ddfd6d5e961ab4869, exception_lineno );
    }

    // Attachs locals to frame if any.
    Nuitka_Frame_AttachLocals(
        (struct Nuitka_FrameObject *)frame_aab6665c7d7da82ddfd6d5e961ab4869,
        type_description_1
    );


    // Release cached frame.
    if ( frame_aab6665c7d7da82ddfd6d5e961ab4869 == cache_frame_aab6665c7d7da82ddfd6d5e961ab4869 )
    {
        Py_DECREF( frame_aab6665c7d7da82ddfd6d5e961ab4869 );
    }
    cache_frame_aab6665c7d7da82ddfd6d5e961ab4869 = NULL;

    assertFrameObject( frame_aab6665c7d7da82ddfd6d5e961ab4869 );

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto function_exception_exit;

    frame_no_exception_1:;
    tmp_return_value = Py_None;
    Py_INCREF( tmp_return_value );
    goto function_return_exit;

    // Return statement must have exited already.
    NUITKA_CANNOT_GET_HERE( __main__$$$function_2_main );
    return NULL;

function_exception_exit:
    assert( exception_type );
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );

    return NULL;

function_return_exit:
   // Function cleanup code if any.


   // Actual function exit with return value, making sure we did not make
   // the error status worse despite non-NULL return.
   CHECK_OBJECT( tmp_return_value );
   assert( had_error || !ERROR_OCCURRED() );
   return tmp_return_value;
}



static PyObject *MAKE_FUNCTION___main__$$$function_1_talk(  )
{
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl___main__$$$function_1_talk,
        const_str_plain_talk,
#if PYTHON_VERSION >= 300
        NULL,
#endif
        codeobj_50320aa795b05b9fb9f611b975852c56,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        NULL,
#endif
        module___main__,
        NULL,
        0
    );

    return (PyObject *)result;
}



static PyObject *MAKE_FUNCTION___main__$$$function_2_main(  )
{
    struct Nuitka_FunctionObject *result = Nuitka_Function_New(
        impl___main__$$$function_2_main,
        const_str_plain_main,
#if PYTHON_VERSION >= 300
        NULL,
#endif
        codeobj_aab6665c7d7da82ddfd6d5e961ab4869,
        NULL,
#if PYTHON_VERSION >= 300
        NULL,
        NULL,
#endif
        module___main__,
        NULL,
        0
    );

    return (PyObject *)result;
}



#if PYTHON_VERSION >= 300
static struct PyModuleDef mdef___main__ =
{
    PyModuleDef_HEAD_INIT,
    "__main__",
    NULL,                /* m_doc */
    -1,                  /* m_size */
    NULL,                /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#endif

extern PyObject *const_str_plain___compiled__;

extern PyObject *const_str_plain___package__;

#if PYTHON_VERSION >= 300
extern PyObject *const_str_dot;
extern PyObject *const_str_plain___loader__;
#endif

#if PYTHON_VERSION >= 340
extern PyObject *const_str_plain___spec__;
extern PyObject *const_str_plain__initializing;
extern PyObject *const_str_plain_submodule_search_locations;
#endif

extern void _initCompiledCellType();
extern void _initCompiledGeneratorType();
extern void _initCompiledFunctionType();
extern void _initCompiledMethodType();
extern void _initCompiledFrameType();
#if PYTHON_VERSION >= 350
extern void _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
extern void _initCompiledAsyncgenTypes();
#endif

extern PyTypeObject Nuitka_Loader_Type;

// The exported interface to CPython. On import of the module, this function
// gets called. It has to have an exact function name, in cases it's a shared
// library export. This is hidden behind the MOD_INIT_DECL.

MOD_INIT_DECL( __main__ )
{
#if defined(_NUITKA_EXE) || PYTHON_VERSION >= 300
    static bool _init_done = false;

    // Modules might be imported repeatedly, which is to be ignored.
    if ( _init_done )
    {
        return MOD_RETURN_VALUE( module___main__ );
    }
    else
    {
        _init_done = true;
    }
#endif

#ifdef _NUITKA_MODULE
    // In case of a stand alone extension module, need to call initialization
    // the init here because that's the first and only time we are going to get
    // called here.

    // Initialize the constant values used.
    _initBuiltinModule();
    createGlobalConstants();

    /* Initialize the compiled types of Nuitka. */
    _initCompiledCellType();
    _initCompiledGeneratorType();
    _initCompiledFunctionType();
    _initCompiledMethodType();
    _initCompiledFrameType();
#if PYTHON_VERSION >= 350
    _initCompiledCoroutineTypes();
#endif
#if PYTHON_VERSION >= 360
    _initCompiledAsyncgenTypes();
#endif

#if PYTHON_VERSION < 300
    _initSlotCompare();
#endif
#if PYTHON_VERSION >= 270
    _initSlotIternext();
#endif

    patchBuiltinModule();
    patchTypeComparison();

    // Enable meta path based loader if not already done.
#ifdef _NUITKA_TRACE
    puts("__main__: Calling setupMetaPathBasedLoader().");
#endif
    setupMetaPathBasedLoader();

#if PYTHON_VERSION >= 300
    patchInspectModule();
#endif

#endif

    /* The constants only used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleConstants().");
#endif
    createModuleConstants();

    /* The code objects used by this module are created now. */
#ifdef _NUITKA_TRACE
    puts("__main__: Calling createModuleCodeObjects().");
#endif
    createModuleCodeObjects();

    // puts( "in init__main__" );

    // Create the module object first. There are no methods initially, all are
    // added dynamically in actual code only.  Also no "__doc__" is initially
    // set at this time, as it could not contain NUL characters this way, they
    // are instead set in early module code.  No "self" for modules, we have no
    // use for it.
#if PYTHON_VERSION < 300
    module___main__ = Py_InitModule4(
        "__main__",       // Module Name
        NULL,                    // No methods initially, all are added
                                 // dynamically in actual module code only.
        NULL,                    // No "__doc__" is initially set, as it could
                                 // not contain NUL this way, added early in
                                 // actual code.
        NULL,                    // No self for modules, we don't use it.
        PYTHON_API_VERSION
    );
#else

    module___main__ = PyModule_Create( &mdef___main__ );
#endif

    moduledict___main__ = MODULE_DICT( module___main__ );

    // Set __compiled__ to what it we know.
    UPDATE_STRING_DICT1(
        moduledict___main__,
        (Nuitka_StringObject *)const_str_plain___compiled__,
        Nuitka_dunder_compiled_value
    );

    // Update "__package__" value to what it ought to be.
    {
#if 0
        PyObject *module_name = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__ );

        UPDATE_STRING_DICT1(
            moduledict___main__,
            (Nuitka_StringObject *)const_str_plain___package__,
            module_name
        );
#else

#if PYTHON_VERSION < 300
        PyObject *module_name = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__ );
        char const *module_name_cstr = PyString_AS_STRING( module_name );

        char const *last_dot = strrchr( module_name_cstr, '.' );

        if ( last_dot != NULL )
        {
            UPDATE_STRING_DICT1(
                moduledict___main__,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyString_FromStringAndSize( module_name_cstr, last_dot - module_name_cstr )
            );
        }
#else
        PyObject *module_name = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__ );
        Py_ssize_t dot_index = PyUnicode_Find( module_name, const_str_dot, 0, PyUnicode_GetLength( module_name ), -1 );

        if ( dot_index != -1 )
        {
            UPDATE_STRING_DICT1(
                moduledict___main__,
                (Nuitka_StringObject *)const_str_plain___package__,
                PyUnicode_Substring( module_name, 0, dot_index )
            );
        }
#endif
#endif
    }

    CHECK_OBJECT( module___main__ );

// Seems to work for Python2.7 out of the box, but for Python3, the module
// doesn't automatically enter "sys.modules", so do it manually.
#if PYTHON_VERSION >= 300
    {
        int r = PyObject_SetItem( PyImport_GetModuleDict(), const_str_plain___main__, module___main__ );

        assert( r != -1 );
    }
#endif

    // For deep importing of a module we need to have "__builtins__", so we set
    // it ourselves in the same way than CPython does. Note: This must be done
    // before the frame object is allocated, or else it may fail.

    if ( GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___builtins__ ) == NULL )
    {
        PyObject *value = (PyObject *)builtin_module;

        // Check if main module, not a dict then but the module itself.
#if !defined(_NUITKA_EXE) || !1
        value = PyModule_GetDict( value );
#endif

        UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___builtins__, value );
    }

#if PYTHON_VERSION >= 300
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___loader__, (PyObject *)&Nuitka_Loader_Type );
#endif

#if PYTHON_VERSION >= 340
// Set the "__spec__" value

#if 1
    // Main modules just get "None" as spec.
    UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___spec__, Py_None );
#else
    // Other modules get a "ModuleSpec" from the standard mechanism.
    {
        PyObject *bootstrap_module = PyImport_ImportModule("importlib._bootstrap");
        CHECK_OBJECT( bootstrap_module );
        PyObject *module_spec_class = PyObject_GetAttrString( bootstrap_module, "ModuleSpec" );
        Py_DECREF( bootstrap_module );

        PyObject *args[] = {
            GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___name__ ),
            (PyObject *)&Nuitka_Loader_Type
        };

        PyObject *spec_value = CALL_FUNCTION_WITH_ARGS2(
            module_spec_class,
            args
        );
        Py_DECREF( module_spec_class );

        // We can assume this to never fail, or else we are in trouble anyway.
        CHECK_OBJECT( spec_value );

// For packages set the submodule search locations as well, even if to empty
// list, so investigating code will consider it a package.
#if 0
        SET_ATTRIBUTE( spec_value, const_str_plain_submodule_search_locations, PyList_New(0) );
#endif

// Mark the execution in the "__spec__" value.
        SET_ATTRIBUTE( spec_value, const_str_plain__initializing, Py_True );

        UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain___spec__, spec_value );
    }
#endif
#endif

    // Temp variables if any
    struct Nuitka_FrameObject *frame_6c565e902b4e680a75ba298785b20d24;
    NUITKA_MAY_BE_UNUSED char const *type_description_1 = NULL;
    PyObject *exception_type = NULL;
    PyObject *exception_value = NULL;
    PyTracebackObject *exception_tb = NULL;
    NUITKA_MAY_BE_UNUSED int exception_lineno = 0;

    // Module code.
    // Frame without reuse.
    frame_6c565e902b4e680a75ba298785b20d24 = MAKE_MODULE_FRAME( codeobj_6c565e902b4e680a75ba298785b20d24, module___main__ );

    // Push the new frame as the currently active one, and we should be exclusively
    // owning it.
    pushFrameStack( frame_6c565e902b4e680a75ba298785b20d24 );
    assert( Py_REFCNT( frame_6c565e902b4e680a75ba298785b20d24 ) == 2 );

    // Framed code:
    {
        PyObject *tmp_name_name_1;
        PyObject *tmp_level_name_1;
        PyObject *tmp_imported_value_1;
        tmp_name_name_1 = const_str_plain_site;
        tmp_level_name_1 = const_int_0;
        frame_6c565e902b4e680a75ba298785b20d24->m_frame.f_lineno = 1;
        tmp_imported_value_1 = IMPORT_MODULE_KW( tmp_name_name_1, NULL, NULL, NULL, tmp_level_name_1 );
        if ( tmp_imported_value_1 == NULL )
        {
            assert( ERROR_OCCURRED() );

            FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


            exception_lineno = 1;

            goto frame_exception_exit_1;
        }
        Py_DECREF( tmp_imported_value_1 );
    }
    {
        PyObject *tmp_assign_source_1;
        tmp_assign_source_1 = Py_None;
        UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___doc__, tmp_assign_source_1 );
    }
    {
        PyObject *tmp_assign_source_2;
        tmp_assign_source_2 = module_filename_obj;
        UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___file__, tmp_assign_source_2 );
    }
    {
        PyObject *tmp_assign_source_3;
        tmp_assign_source_3 = Py_None;
        UPDATE_STRING_DICT0( moduledict___main__, (Nuitka_StringObject *)const_str_plain___cached__, tmp_assign_source_3 );
    }
    {
        PyObject *tmp_assign_source_4;
        tmp_assign_source_4 = PyDict_New();
        UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain___annotations__, tmp_assign_source_4 );
    }
    {
        PyObject *tmp_assign_source_5;
        tmp_assign_source_5 = MAKE_FUNCTION___main__$$$function_1_talk(  );



        UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_talk, tmp_assign_source_5 );
    }
    {
        PyObject *tmp_assign_source_6;
        tmp_assign_source_6 = MAKE_FUNCTION___main__$$$function_2_main(  );



        UPDATE_STRING_DICT1( moduledict___main__, (Nuitka_StringObject *)const_str_plain_main, tmp_assign_source_6 );
    }
    {
        PyObject *tmp_called_name_1;
        PyObject *tmp_mvar_value_1;
        PyObject *tmp_call_result_1;
        tmp_mvar_value_1 = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain_main );

        if (unlikely( tmp_mvar_value_1 == NULL ))
        {
            tmp_mvar_value_1 = GET_STRING_DICT_VALUE( dict_builtin, (Nuitka_StringObject *)const_str_plain_main );
        }

        CHECK_OBJECT( tmp_mvar_value_1 );
        tmp_called_name_1 = tmp_mvar_value_1;
        frame_6c565e902b4e680a75ba298785b20d24->m_frame.f_lineno = 8;
        tmp_call_result_1 = CALL_FUNCTION_NO_ARGS( tmp_called_name_1 );
        if ( tmp_call_result_1 == NULL )
        {
            assert( ERROR_OCCURRED() );

            FETCH_ERROR_OCCURRED( &exception_type, &exception_value, &exception_tb );


            exception_lineno = 8;

            goto frame_exception_exit_1;
        }
        Py_DECREF( tmp_call_result_1 );
    }

    // Restore frame exception if necessary.
#if 0
    RESTORE_FRAME_EXCEPTION( frame_6c565e902b4e680a75ba298785b20d24 );
#endif
    popFrameStack();

    assertFrameObject( frame_6c565e902b4e680a75ba298785b20d24 );

    goto frame_no_exception_1;

    frame_exception_exit_1:;
#if 0
    RESTORE_FRAME_EXCEPTION( frame_6c565e902b4e680a75ba298785b20d24 );
#endif

    if ( exception_tb == NULL )
    {
        exception_tb = MAKE_TRACEBACK( frame_6c565e902b4e680a75ba298785b20d24, exception_lineno );
    }
    else if ( exception_tb->tb_frame != &frame_6c565e902b4e680a75ba298785b20d24->m_frame )
    {
        exception_tb = ADD_TRACEBACK( exception_tb, frame_6c565e902b4e680a75ba298785b20d24, exception_lineno );
    }

    // Put the previous frame back on top.
    popFrameStack();

    // Return the error.
    goto module_exception_exit;

    frame_no_exception_1:;

#if _NUITKA_EXPERIMENTAL_PKGUTIL_ITERMODULES
#if 0 && 1
    {
        PyObject *path_value = GET_STRING_DICT_VALUE( moduledict___main__, (Nuitka_StringObject *)const_str_plain___path__ );

        if (path_value && PyList_CheckExact(path_value) && PyList_Size(path_value) > 0)
        {
            PyObject *path_element = PyList_GetItem( path_value, 0 );

            PyObject *path_importer_cache = PySys_GetObject((char *)"path_importer_cache");
            CHECK_OBJECT( path_importer_cache );

            int res = PyDict_SetItem( path_importer_cache, path_element, (PyObject *)&Nuitka_Loader_Type );
            assert( res == 0 );
        }
    }
#endif
#endif

    return MOD_RETURN_VALUE( module___main__ );
    module_exception_exit:
    RESTORE_ERROR_OCCURRED( exception_type, exception_value, exception_tb );
    return MOD_RETURN_VALUE( NULL );
}
