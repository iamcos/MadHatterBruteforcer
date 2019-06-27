// This file contains helper functions that are automatically created from
// templates.

#include "nuitka/prelude.h"

extern PyObject *callPythonFunction( PyObject *func, PyObject **args, int count );


PyObject *CALL_FUNCTION_WITH_ARGS1( PyObject *called, PyObject **args )
{
    CHECK_OBJECT( called );

    // Check if arguments are valid objects in debug mode.
#ifndef __NUITKA_NO_ASSERT__
    for( size_t i = 0; i < 1; i++ )
    {
        CHECK_OBJECT( args[ i ] );
    }
#endif

    if ( Nuitka_Function_Check( called ) )
    {
        if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
        {
            return NULL;
        }

        struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)called;
        PyObject *result;

        if ( function->m_args_simple && 1 == function->m_args_positional_count )
        {
            for( Py_ssize_t i = 0; i < 1; i++ )
            {
                Py_INCREF( args[ i ] );
            }

            result = function->m_c_code( function, args );
        }
        else if ( function->m_args_simple && 1 + function->m_defaults_given == function->m_args_positional_count )
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
            PyObject *python_pars[ function->m_args_positional_count ];
#endif
            memcpy( python_pars, args, 1 * sizeof(PyObject *) );
            memcpy( python_pars + 1, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

            for( Py_ssize_t i = 0; i < function->m_args_positional_count; i++ )
            {
                Py_INCREF( python_pars[ i ] );
            }

            result = function->m_c_code( function, python_pars );
        }
        else
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
            PyObject *python_pars[ function->m_args_overall_count ];
#endif
            memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

            if ( parseArgumentsPos( function, python_pars, args, 1 ))
            {
                result = function->m_c_code( function, python_pars );
            }
            else
            {
                result = NULL;
            }
        }

        Py_LeaveRecursiveCall();

        return result;
    }
    else if ( Nuitka_Method_Check( called ) )
    {
        struct Nuitka_MethodObject *method = (struct Nuitka_MethodObject *)called;

        // Unbound method without arguments, let the error path be slow.
        if ( method->m_object != NULL )
        {
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }

            struct Nuitka_FunctionObject *function = method->m_function;

            PyObject *result;

            if ( function->m_args_simple && 1 + 1 == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                for( Py_ssize_t i = 0; i < 1; i++ )
                {
                    python_pars[ i + 1 ] = args[ i ];
                    Py_INCREF( args[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else if ( function->m_args_simple && 1 + 1 + function->m_defaults_given == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                memcpy( python_pars+1, args, 1 * sizeof(PyObject *) );
                memcpy( python_pars+1 + 1, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

                for( Py_ssize_t i = 1; i < function->m_args_overall_count; i++ )
                {
                    Py_INCREF( python_pars[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
                PyObject *python_pars[ function->m_args_overall_count ];
#endif
                memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

                if ( parseArgumentsMethodPos( function, python_pars, method->m_object, args, 1 ) )
                {
                    result = function->m_c_code( function, python_pars );
                }
                else
                {
                    result = NULL;
                }
            }

            Py_LeaveRecursiveCall();

            return result;
        }
    }
    else if ( PyCFunction_Check( called ) )
    {
        // Try to be fast about wrapping the arguments.
        int flags = PyCFunction_GET_FLAGS( called ) & ~(METH_CLASS | METH_STATIC | METH_COEXIST);

        if ( flags & METH_NOARGS )
        {
#if 1 == 0
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, NULL );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(
                PyExc_TypeError,
                "%s() takes no arguments (1 given)",
                ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_O )
        {
#if 1 == 1
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, args[0] );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(PyExc_TypeError,
                "%s() takes exactly one argument (1 given)",
                 ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_VARARGS )
        {
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            PyObject *pos_args = MAKE_TUPLE( args, 1 );

            PyObject *result;

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

#if PYTHON_VERSION < 360
            if ( flags & METH_KEYWORDS )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#else
            if ( flags == ( METH_VARARGS | METH_KEYWORDS ) )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else if ( flags == METH_FASTCALL )
            {
#if PYTHON_VERSION < 370
                result = (*(_PyCFunctionFast)method)( self, &PyTuple_GET_ITEM( pos_args, 0 ), 1, NULL );;
#else
                result = (*(_PyCFunctionFast)method)( self, &pos_args, 1 );;
#endif
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#endif

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
                // Some buggy C functions do set an error, but do not indicate it
                // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                Py_DECREF( pos_args );
                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                Py_DECREF( pos_args );
                return NULL;
            }
        }
    }
    else if ( PyFunction_Check( called ) )
    {
        return callPythonFunction(
            called,
            args,
            1
        );
    }

    PyObject *pos_args = MAKE_TUPLE( args, 1 );

    PyObject *result = CALL_FUNCTION(
        called,
        pos_args,
        NULL
    );

    Py_DECREF( pos_args );

    return result;
}

PyObject *CALL_FUNCTION_WITH_ARGS2( PyObject *called, PyObject **args )
{
    CHECK_OBJECT( called );

    // Check if arguments are valid objects in debug mode.
#ifndef __NUITKA_NO_ASSERT__
    for( size_t i = 0; i < 2; i++ )
    {
        CHECK_OBJECT( args[ i ] );
    }
#endif

    if ( Nuitka_Function_Check( called ) )
    {
        if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
        {
            return NULL;
        }

        struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)called;
        PyObject *result;

        if ( function->m_args_simple && 2 == function->m_args_positional_count )
        {
            for( Py_ssize_t i = 0; i < 2; i++ )
            {
                Py_INCREF( args[ i ] );
            }

            result = function->m_c_code( function, args );
        }
        else if ( function->m_args_simple && 2 + function->m_defaults_given == function->m_args_positional_count )
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
            PyObject *python_pars[ function->m_args_positional_count ];
#endif
            memcpy( python_pars, args, 2 * sizeof(PyObject *) );
            memcpy( python_pars + 2, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

            for( Py_ssize_t i = 0; i < function->m_args_positional_count; i++ )
            {
                Py_INCREF( python_pars[ i ] );
            }

            result = function->m_c_code( function, python_pars );
        }
        else
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
            PyObject *python_pars[ function->m_args_overall_count ];
#endif
            memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

            if ( parseArgumentsPos( function, python_pars, args, 2 ))
            {
                result = function->m_c_code( function, python_pars );
            }
            else
            {
                result = NULL;
            }
        }

        Py_LeaveRecursiveCall();

        return result;
    }
    else if ( Nuitka_Method_Check( called ) )
    {
        struct Nuitka_MethodObject *method = (struct Nuitka_MethodObject *)called;

        // Unbound method without arguments, let the error path be slow.
        if ( method->m_object != NULL )
        {
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }

            struct Nuitka_FunctionObject *function = method->m_function;

            PyObject *result;

            if ( function->m_args_simple && 2 + 1 == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                for( Py_ssize_t i = 0; i < 2; i++ )
                {
                    python_pars[ i + 1 ] = args[ i ];
                    Py_INCREF( args[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else if ( function->m_args_simple && 2 + 1 + function->m_defaults_given == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                memcpy( python_pars+1, args, 2 * sizeof(PyObject *) );
                memcpy( python_pars+1 + 2, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

                for( Py_ssize_t i = 1; i < function->m_args_overall_count; i++ )
                {
                    Py_INCREF( python_pars[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
                PyObject *python_pars[ function->m_args_overall_count ];
#endif
                memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

                if ( parseArgumentsMethodPos( function, python_pars, method->m_object, args, 2 ) )
                {
                    result = function->m_c_code( function, python_pars );
                }
                else
                {
                    result = NULL;
                }
            }

            Py_LeaveRecursiveCall();

            return result;
        }
    }
    else if ( PyCFunction_Check( called ) )
    {
        // Try to be fast about wrapping the arguments.
        int flags = PyCFunction_GET_FLAGS( called ) & ~(METH_CLASS | METH_STATIC | METH_COEXIST);

        if ( flags & METH_NOARGS )
        {
#if 2 == 0
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, NULL );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(
                PyExc_TypeError,
                "%s() takes no arguments (2 given)",
                ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_O )
        {
#if 2 == 1
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, args[0] );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(PyExc_TypeError,
                "%s() takes exactly one argument (2 given)",
                 ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_VARARGS )
        {
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            PyObject *pos_args = MAKE_TUPLE( args, 2 );

            PyObject *result;

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

#if PYTHON_VERSION < 360
            if ( flags & METH_KEYWORDS )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#else
            if ( flags == ( METH_VARARGS | METH_KEYWORDS ) )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else if ( flags == METH_FASTCALL )
            {
#if PYTHON_VERSION < 370
                result = (*(_PyCFunctionFast)method)( self, &PyTuple_GET_ITEM( pos_args, 0 ), 2, NULL );;
#else
                result = (*(_PyCFunctionFast)method)( self, &pos_args, 2 );;
#endif
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#endif

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
                // Some buggy C functions do set an error, but do not indicate it
                // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                Py_DECREF( pos_args );
                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                Py_DECREF( pos_args );
                return NULL;
            }
        }
    }
    else if ( PyFunction_Check( called ) )
    {
        return callPythonFunction(
            called,
            args,
            2
        );
    }

    PyObject *pos_args = MAKE_TUPLE( args, 2 );

    PyObject *result = CALL_FUNCTION(
        called,
        pos_args,
        NULL
    );

    Py_DECREF( pos_args );

    return result;
}

PyObject *CALL_FUNCTION_WITH_ARGS3( PyObject *called, PyObject **args )
{
    CHECK_OBJECT( called );

    // Check if arguments are valid objects in debug mode.
#ifndef __NUITKA_NO_ASSERT__
    for( size_t i = 0; i < 3; i++ )
    {
        CHECK_OBJECT( args[ i ] );
    }
#endif

    if ( Nuitka_Function_Check( called ) )
    {
        if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
        {
            return NULL;
        }

        struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)called;
        PyObject *result;

        if ( function->m_args_simple && 3 == function->m_args_positional_count )
        {
            for( Py_ssize_t i = 0; i < 3; i++ )
            {
                Py_INCREF( args[ i ] );
            }

            result = function->m_c_code( function, args );
        }
        else if ( function->m_args_simple && 3 + function->m_defaults_given == function->m_args_positional_count )
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
            PyObject *python_pars[ function->m_args_positional_count ];
#endif
            memcpy( python_pars, args, 3 * sizeof(PyObject *) );
            memcpy( python_pars + 3, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

            for( Py_ssize_t i = 0; i < function->m_args_positional_count; i++ )
            {
                Py_INCREF( python_pars[ i ] );
            }

            result = function->m_c_code( function, python_pars );
        }
        else
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
            PyObject *python_pars[ function->m_args_overall_count ];
#endif
            memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

            if ( parseArgumentsPos( function, python_pars, args, 3 ))
            {
                result = function->m_c_code( function, python_pars );
            }
            else
            {
                result = NULL;
            }
        }

        Py_LeaveRecursiveCall();

        return result;
    }
    else if ( Nuitka_Method_Check( called ) )
    {
        struct Nuitka_MethodObject *method = (struct Nuitka_MethodObject *)called;

        // Unbound method without arguments, let the error path be slow.
        if ( method->m_object != NULL )
        {
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }

            struct Nuitka_FunctionObject *function = method->m_function;

            PyObject *result;

            if ( function->m_args_simple && 3 + 1 == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                for( Py_ssize_t i = 0; i < 3; i++ )
                {
                    python_pars[ i + 1 ] = args[ i ];
                    Py_INCREF( args[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else if ( function->m_args_simple && 3 + 1 + function->m_defaults_given == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                memcpy( python_pars+1, args, 3 * sizeof(PyObject *) );
                memcpy( python_pars+1 + 3, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

                for( Py_ssize_t i = 1; i < function->m_args_overall_count; i++ )
                {
                    Py_INCREF( python_pars[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
                PyObject *python_pars[ function->m_args_overall_count ];
#endif
                memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

                if ( parseArgumentsMethodPos( function, python_pars, method->m_object, args, 3 ) )
                {
                    result = function->m_c_code( function, python_pars );
                }
                else
                {
                    result = NULL;
                }
            }

            Py_LeaveRecursiveCall();

            return result;
        }
    }
    else if ( PyCFunction_Check( called ) )
    {
        // Try to be fast about wrapping the arguments.
        int flags = PyCFunction_GET_FLAGS( called ) & ~(METH_CLASS | METH_STATIC | METH_COEXIST);

        if ( flags & METH_NOARGS )
        {
#if 3 == 0
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, NULL );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(
                PyExc_TypeError,
                "%s() takes no arguments (3 given)",
                ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_O )
        {
#if 3 == 1
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, args[0] );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(PyExc_TypeError,
                "%s() takes exactly one argument (3 given)",
                 ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_VARARGS )
        {
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            PyObject *pos_args = MAKE_TUPLE( args, 3 );

            PyObject *result;

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

#if PYTHON_VERSION < 360
            if ( flags & METH_KEYWORDS )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#else
            if ( flags == ( METH_VARARGS | METH_KEYWORDS ) )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else if ( flags == METH_FASTCALL )
            {
#if PYTHON_VERSION < 370
                result = (*(_PyCFunctionFast)method)( self, &PyTuple_GET_ITEM( pos_args, 0 ), 3, NULL );;
#else
                result = (*(_PyCFunctionFast)method)( self, &pos_args, 3 );;
#endif
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#endif

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
                // Some buggy C functions do set an error, but do not indicate it
                // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                Py_DECREF( pos_args );
                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                Py_DECREF( pos_args );
                return NULL;
            }
        }
    }
    else if ( PyFunction_Check( called ) )
    {
        return callPythonFunction(
            called,
            args,
            3
        );
    }

    PyObject *pos_args = MAKE_TUPLE( args, 3 );

    PyObject *result = CALL_FUNCTION(
        called,
        pos_args,
        NULL
    );

    Py_DECREF( pos_args );

    return result;
}

PyObject *CALL_FUNCTION_WITH_ARGS4( PyObject *called, PyObject **args )
{
    CHECK_OBJECT( called );

    // Check if arguments are valid objects in debug mode.
#ifndef __NUITKA_NO_ASSERT__
    for( size_t i = 0; i < 4; i++ )
    {
        CHECK_OBJECT( args[ i ] );
    }
#endif

    if ( Nuitka_Function_Check( called ) )
    {
        if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
        {
            return NULL;
        }

        struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)called;
        PyObject *result;

        if ( function->m_args_simple && 4 == function->m_args_positional_count )
        {
            for( Py_ssize_t i = 0; i < 4; i++ )
            {
                Py_INCREF( args[ i ] );
            }

            result = function->m_c_code( function, args );
        }
        else if ( function->m_args_simple && 4 + function->m_defaults_given == function->m_args_positional_count )
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
            PyObject *python_pars[ function->m_args_positional_count ];
#endif
            memcpy( python_pars, args, 4 * sizeof(PyObject *) );
            memcpy( python_pars + 4, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

            for( Py_ssize_t i = 0; i < function->m_args_positional_count; i++ )
            {
                Py_INCREF( python_pars[ i ] );
            }

            result = function->m_c_code( function, python_pars );
        }
        else
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
            PyObject *python_pars[ function->m_args_overall_count ];
#endif
            memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

            if ( parseArgumentsPos( function, python_pars, args, 4 ))
            {
                result = function->m_c_code( function, python_pars );
            }
            else
            {
                result = NULL;
            }
        }

        Py_LeaveRecursiveCall();

        return result;
    }
    else if ( Nuitka_Method_Check( called ) )
    {
        struct Nuitka_MethodObject *method = (struct Nuitka_MethodObject *)called;

        // Unbound method without arguments, let the error path be slow.
        if ( method->m_object != NULL )
        {
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }

            struct Nuitka_FunctionObject *function = method->m_function;

            PyObject *result;

            if ( function->m_args_simple && 4 + 1 == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                for( Py_ssize_t i = 0; i < 4; i++ )
                {
                    python_pars[ i + 1 ] = args[ i ];
                    Py_INCREF( args[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else if ( function->m_args_simple && 4 + 1 + function->m_defaults_given == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                memcpy( python_pars+1, args, 4 * sizeof(PyObject *) );
                memcpy( python_pars+1 + 4, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

                for( Py_ssize_t i = 1; i < function->m_args_overall_count; i++ )
                {
                    Py_INCREF( python_pars[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
                PyObject *python_pars[ function->m_args_overall_count ];
#endif
                memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

                if ( parseArgumentsMethodPos( function, python_pars, method->m_object, args, 4 ) )
                {
                    result = function->m_c_code( function, python_pars );
                }
                else
                {
                    result = NULL;
                }
            }

            Py_LeaveRecursiveCall();

            return result;
        }
    }
    else if ( PyCFunction_Check( called ) )
    {
        // Try to be fast about wrapping the arguments.
        int flags = PyCFunction_GET_FLAGS( called ) & ~(METH_CLASS | METH_STATIC | METH_COEXIST);

        if ( flags & METH_NOARGS )
        {
#if 4 == 0
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, NULL );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(
                PyExc_TypeError,
                "%s() takes no arguments (4 given)",
                ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_O )
        {
#if 4 == 1
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, args[0] );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(PyExc_TypeError,
                "%s() takes exactly one argument (4 given)",
                 ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_VARARGS )
        {
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            PyObject *pos_args = MAKE_TUPLE( args, 4 );

            PyObject *result;

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

#if PYTHON_VERSION < 360
            if ( flags & METH_KEYWORDS )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#else
            if ( flags == ( METH_VARARGS | METH_KEYWORDS ) )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else if ( flags == METH_FASTCALL )
            {
#if PYTHON_VERSION < 370
                result = (*(_PyCFunctionFast)method)( self, &PyTuple_GET_ITEM( pos_args, 0 ), 4, NULL );;
#else
                result = (*(_PyCFunctionFast)method)( self, &pos_args, 4 );;
#endif
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#endif

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
                // Some buggy C functions do set an error, but do not indicate it
                // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                Py_DECREF( pos_args );
                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                Py_DECREF( pos_args );
                return NULL;
            }
        }
    }
    else if ( PyFunction_Check( called ) )
    {
        return callPythonFunction(
            called,
            args,
            4
        );
    }

    PyObject *pos_args = MAKE_TUPLE( args, 4 );

    PyObject *result = CALL_FUNCTION(
        called,
        pos_args,
        NULL
    );

    Py_DECREF( pos_args );

    return result;
}

PyObject *CALL_FUNCTION_WITH_ARGS5( PyObject *called, PyObject **args )
{
    CHECK_OBJECT( called );

    // Check if arguments are valid objects in debug mode.
#ifndef __NUITKA_NO_ASSERT__
    for( size_t i = 0; i < 5; i++ )
    {
        CHECK_OBJECT( args[ i ] );
    }
#endif

    if ( Nuitka_Function_Check( called ) )
    {
        if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
        {
            return NULL;
        }

        struct Nuitka_FunctionObject *function = (struct Nuitka_FunctionObject *)called;
        PyObject *result;

        if ( function->m_args_simple && 5 == function->m_args_positional_count )
        {
            for( Py_ssize_t i = 0; i < 5; i++ )
            {
                Py_INCREF( args[ i ] );
            }

            result = function->m_c_code( function, args );
        }
        else if ( function->m_args_simple && 5 + function->m_defaults_given == function->m_args_positional_count )
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
            PyObject *python_pars[ function->m_args_positional_count ];
#endif
            memcpy( python_pars, args, 5 * sizeof(PyObject *) );
            memcpy( python_pars + 5, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

            for( Py_ssize_t i = 0; i < function->m_args_positional_count; i++ )
            {
                Py_INCREF( python_pars[ i ] );
            }

            result = function->m_c_code( function, python_pars );
        }
        else
        {
#ifdef _MSC_VER
            PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
            PyObject *python_pars[ function->m_args_overall_count ];
#endif
            memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

            if ( parseArgumentsPos( function, python_pars, args, 5 ))
            {
                result = function->m_c_code( function, python_pars );
            }
            else
            {
                result = NULL;
            }
        }

        Py_LeaveRecursiveCall();

        return result;
    }
    else if ( Nuitka_Method_Check( called ) )
    {
        struct Nuitka_MethodObject *method = (struct Nuitka_MethodObject *)called;

        // Unbound method without arguments, let the error path be slow.
        if ( method->m_object != NULL )
        {
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }

            struct Nuitka_FunctionObject *function = method->m_function;

            PyObject *result;

            if ( function->m_args_simple && 5 + 1 == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                for( Py_ssize_t i = 0; i < 5; i++ )
                {
                    python_pars[ i + 1 ] = args[ i ];
                    Py_INCREF( args[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else if ( function->m_args_simple && 5 + 1 + function->m_defaults_given == function->m_args_positional_count )
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_positional_count );
#else
                PyObject *python_pars[ function->m_args_positional_count ];
#endif
                python_pars[ 0 ] = method->m_object;
                Py_INCREF( method->m_object );

                memcpy( python_pars+1, args, 5 * sizeof(PyObject *) );
                memcpy( python_pars+1 + 5, &PyTuple_GET_ITEM( function->m_defaults, 0 ), function->m_defaults_given * sizeof(PyObject *) );

                for( Py_ssize_t i = 1; i < function->m_args_overall_count; i++ )
                {
                    Py_INCREF( python_pars[ i ] );
                }

                result = function->m_c_code( function, python_pars );
            }
            else
            {
#ifdef _MSC_VER
                PyObject **python_pars = (PyObject **)_alloca( sizeof( PyObject * ) * function->m_args_overall_count );
#else
                PyObject *python_pars[ function->m_args_overall_count ];
#endif
                memset( python_pars, 0, function->m_args_overall_count * sizeof(PyObject *) );

                if ( parseArgumentsMethodPos( function, python_pars, method->m_object, args, 5 ) )
                {
                    result = function->m_c_code( function, python_pars );
                }
                else
                {
                    result = NULL;
                }
            }

            Py_LeaveRecursiveCall();

            return result;
        }
    }
    else if ( PyCFunction_Check( called ) )
    {
        // Try to be fast about wrapping the arguments.
        int flags = PyCFunction_GET_FLAGS( called ) & ~(METH_CLASS | METH_STATIC | METH_COEXIST);

        if ( flags & METH_NOARGS )
        {
#if 5 == 0
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, NULL );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(
                PyExc_TypeError,
                "%s() takes no arguments (5 given)",
                ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_O )
        {
#if 5 == 1
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

            PyObject *result = (*method)( self, args[0] );

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
            // Some buggy C functions do set an error, but do not indicate it
            // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                return NULL;
            }
#else
            PyErr_Format(PyExc_TypeError,
                "%s() takes exactly one argument (5 given)",
                 ((PyCFunctionObject *)called)->m_ml->ml_name
            );
            return NULL;
#endif
        }
        else if ( flags & METH_VARARGS )
        {
            PyCFunction method = PyCFunction_GET_FUNCTION( called );
            PyObject *self = PyCFunction_GET_SELF( called );

            PyObject *pos_args = MAKE_TUPLE( args, 5 );

            PyObject *result;

            // Recursion guard is not strictly necessary, as we already have
            // one on our way to here.
#ifdef _NUITKA_FULL_COMPAT
            if (unlikely( Py_EnterRecursiveCall( (char *)" while calling a Python object" ) ))
            {
                return NULL;
            }
#endif

#if PYTHON_VERSION < 360
            if ( flags & METH_KEYWORDS )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#else
            if ( flags == ( METH_VARARGS | METH_KEYWORDS ) )
            {
                result = (*(PyCFunctionWithKeywords)method)( self, pos_args, NULL );
            }
            else if ( flags == METH_FASTCALL )
            {
#if PYTHON_VERSION < 370
                result = (*(_PyCFunctionFast)method)( self, &PyTuple_GET_ITEM( pos_args, 0 ), 5, NULL );;
#else
                result = (*(_PyCFunctionFast)method)( self, &pos_args, 5 );;
#endif
            }
            else
            {
                result = (*method)( self, pos_args );
            }
#endif

#ifdef _NUITKA_FULL_COMPAT
            Py_LeaveRecursiveCall();
#endif

            if ( result != NULL )
            {
                // Some buggy C functions do set an error, but do not indicate it
                // and Nuitka inner workings can get upset/confused from it.
                DROP_ERROR_OCCURRED();

                Py_DECREF( pos_args );
                return result;
            }
            else
            {
                // Other buggy C functions do this, return NULL, but with
                // no error set, not allowed.
                if (unlikely( !ERROR_OCCURRED() ))
                {
                    PyErr_Format(
                        PyExc_SystemError,
                        "NULL result without error in PyObject_Call"
                    );
                }

                Py_DECREF( pos_args );
                return NULL;
            }
        }
    }
    else if ( PyFunction_Check( called ) )
    {
        return callPythonFunction(
            called,
            args,
            5
        );
    }

    PyObject *pos_args = MAKE_TUPLE( args, 5 );

    PyObject *result = CALL_FUNCTION(
        called,
        pos_args,
        NULL
    );

    Py_DECREF( pos_args );

    return result;
}
/* Code to register embedded modules for meta path based loading if any. */

#include "nuitka/unfreezing.h"

/* Table for lookup to find compiled or bytecode modules included in this
 * binary or module, or put along this binary as extension modules. We do
 * our own loading for each of these.
 */
MOD_INIT_DECL( __main__ );
static struct Nuitka_MetaPathBasedLoaderEntry meta_path_loader_entries[] =
{
    { "__main__", MOD_INIT_NAME( __main__ ), 0, 0, NUITKA_COMPILED_MODULE },
    { "_asyncio", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_bisect", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_blake2", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_bz2", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_codecs_cn", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_codecs_hk", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_codecs_iso2022", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_codecs_jp", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_codecs_kr", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_codecs_tw", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_contextvars", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_crypt", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_csv", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_ctypes", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_curses", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_curses_panel", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_datetime", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_dbm", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_decimal", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_elementtree", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_gdbm", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_hashlib", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_heapq", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_json", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_lsprof", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_lzma", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_multibytecodec", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_multiprocessing", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_opcode", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_pickle", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_posixsubprocess", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_queue", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_random", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_scproxy", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_sha3", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_socket", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_sqlite3", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_ssl", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_struct", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "_uuid", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "array", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "audioop", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "binascii", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "fcntl", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "grp", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "math", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "mmap", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "pyexpat", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "readline", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "select", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "site", NULL, 558, 17467, NUITKA_BYTECODE_FLAG },
    { "termios", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "unicodedata", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "zlib", NULL, 0, 0, NUITKA_SHLIB_FLAG },
    { "__future__", NULL, 18025, 4132, NUITKA_BYTECODE_FLAG },
    { "_bootlocale", NULL, 22157, 1249, NUITKA_BYTECODE_FLAG },
    { "_compat_pickle", NULL, 23406, 5819, NUITKA_BYTECODE_FLAG },
    { "_dummy_thread", NULL, 29225, 4853, NUITKA_BYTECODE_FLAG },
    { "_markupbase", NULL, 34078, 7796, NUITKA_BYTECODE_FLAG },
    { "_osx_support", NULL, 41874, 9589, NUITKA_BYTECODE_FLAG },
    { "_py_abc", NULL, 51463, 4665, NUITKA_BYTECODE_FLAG },
    { "_pyio", NULL, 56128, 72829, NUITKA_BYTECODE_FLAG },
    { "_sitebuiltins", NULL, 128957, 3476, NUITKA_BYTECODE_FLAG },
    { "_strptime", NULL, 132433, 16115, NUITKA_BYTECODE_FLAG },
    { "_sysconfigdata_m_darwin_darwin", NULL, 148548, 19311, NUITKA_BYTECODE_FLAG },
    { "_threading_local", NULL, 167859, 6423, NUITKA_BYTECODE_FLAG },
    { "_virtualenv_distutils", NULL, 174282, 409, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "aifc", NULL, 174691, 26154, NUITKA_BYTECODE_FLAG },
    { "argparse", NULL, 200845, 61924, NUITKA_BYTECODE_FLAG },
    { "ast", NULL, 262769, 12091, NUITKA_BYTECODE_FLAG },
    { "asynchat", NULL, 274860, 6845, NUITKA_BYTECODE_FLAG },
    { "asyncio", NULL, 281705, 701, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "asyncio.base_events", NULL, 282406, 47789, NUITKA_BYTECODE_FLAG },
    { "asyncio.base_futures", NULL, 330195, 2113, NUITKA_BYTECODE_FLAG },
    { "asyncio.base_subprocess", NULL, 332308, 9202, NUITKA_BYTECODE_FLAG },
    { "asyncio.base_tasks", NULL, 341510, 1877, NUITKA_BYTECODE_FLAG },
    { "asyncio.constants", NULL, 343387, 602, NUITKA_BYTECODE_FLAG },
    { "asyncio.coroutines", NULL, 343989, 6389, NUITKA_BYTECODE_FLAG },
    { "asyncio.events", NULL, 350378, 27866, NUITKA_BYTECODE_FLAG },
    { "asyncio.format_helpers", NULL, 378244, 2328, NUITKA_BYTECODE_FLAG },
    { "asyncio.futures", NULL, 380572, 10756, NUITKA_BYTECODE_FLAG },
    { "asyncio.locks", NULL, 391328, 15924, NUITKA_BYTECODE_FLAG },
    { "asyncio.log", NULL, 407252, 251, NUITKA_BYTECODE_FLAG },
    { "asyncio.proactor_events", NULL, 407503, 19728, NUITKA_BYTECODE_FLAG },
    { "asyncio.protocols", NULL, 427231, 8739, NUITKA_BYTECODE_FLAG },
    { "asyncio.queues", NULL, 435970, 8184, NUITKA_BYTECODE_FLAG },
    { "asyncio.runners", NULL, 444154, 1925, NUITKA_BYTECODE_FLAG },
    { "asyncio.selector_events", NULL, 446079, 28491, NUITKA_BYTECODE_FLAG },
    { "asyncio.sslproto", NULL, 474570, 21222, NUITKA_BYTECODE_FLAG },
    { "asyncio.streams", NULL, 495792, 20299, NUITKA_BYTECODE_FLAG },
    { "asyncio.subprocess", NULL, 516091, 6763, NUITKA_BYTECODE_FLAG },
    { "asyncio.tasks", NULL, 522854, 21877, NUITKA_BYTECODE_FLAG },
    { "asyncio.transports", NULL, 544731, 12222, NUITKA_BYTECODE_FLAG },
    { "asyncio.unix_events", NULL, 556953, 32117, NUITKA_BYTECODE_FLAG },
    { "asyncore", NULL, 589070, 15855, NUITKA_BYTECODE_FLAG },
    { "bdb", NULL, 604925, 24405, NUITKA_BYTECODE_FLAG },
    { "binhex", NULL, 629330, 12070, NUITKA_BYTECODE_FLAG },
    { "bisect", NULL, 641400, 2698, NUITKA_BYTECODE_FLAG },
    { "cProfile", NULL, 644098, 4468, NUITKA_BYTECODE_FLAG },
    { "calendar", NULL, 648566, 27435, NUITKA_BYTECODE_FLAG },
    { "cgi", NULL, 676001, 26596, NUITKA_BYTECODE_FLAG },
    { "cgitb", NULL, 702597, 10123, NUITKA_BYTECODE_FLAG },
    { "chunk", NULL, 712720, 4930, NUITKA_BYTECODE_FLAG },
    { "cmd", NULL, 717650, 12601, NUITKA_BYTECODE_FLAG },
    { "code", NULL, 730251, 9869, NUITKA_BYTECODE_FLAG },
    { "codeop", NULL, 740120, 6301, NUITKA_BYTECODE_FLAG },
    { "colorsys", NULL, 746421, 3308, NUITKA_BYTECODE_FLAG },
    { "compileall", NULL, 749729, 9010, NUITKA_BYTECODE_FLAG },
    { "concurrent", NULL, 758739, 157, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "concurrent.futures", NULL, 758896, 1097, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "concurrent.futures._base", NULL, 759993, 20894, NUITKA_BYTECODE_FLAG },
    { "concurrent.futures.process", NULL, 780887, 19572, NUITKA_BYTECODE_FLAG },
    { "concurrent.futures.thread", NULL, 800459, 5184, NUITKA_BYTECODE_FLAG },
    { "configparser", NULL, 805643, 45891, NUITKA_BYTECODE_FLAG },
    { "contextlib", NULL, 851534, 19911, NUITKA_BYTECODE_FLAG },
    { "contextvars", NULL, 871445, 268, NUITKA_BYTECODE_FLAG },
    { "copy", NULL, 871713, 7101, NUITKA_BYTECODE_FLAG },
    { "crypt", NULL, 878814, 3145, NUITKA_BYTECODE_FLAG },
    { "csv", NULL, 881959, 11843, NUITKA_BYTECODE_FLAG },
    { "ctypes", NULL, 893802, 16160, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "ctypes._aix", NULL, 909962, 9834, NUITKA_BYTECODE_FLAG },
    { "ctypes._endian", NULL, 919796, 1967, NUITKA_BYTECODE_FLAG },
    { "ctypes.macholib", NULL, 921763, 324, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "ctypes.macholib.dyld", NULL, 922087, 4357, NUITKA_BYTECODE_FLAG },
    { "ctypes.macholib.dylib", NULL, 926444, 1951, NUITKA_BYTECODE_FLAG },
    { "ctypes.macholib.framework", NULL, 928395, 2231, NUITKA_BYTECODE_FLAG },
    { "ctypes.util", NULL, 930626, 7760, NUITKA_BYTECODE_FLAG },
    { "curses", NULL, 938386, 1806, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "curses.ascii", NULL, 940192, 3914, NUITKA_BYTECODE_FLAG },
    { "curses.has_key", NULL, 944106, 4278, NUITKA_BYTECODE_FLAG },
    { "curses.panel", NULL, 948384, 248, NUITKA_BYTECODE_FLAG },
    { "curses.textpad", NULL, 948632, 5917, NUITKA_BYTECODE_FLAG },
    { "dataclasses", NULL, 954549, 22006, NUITKA_BYTECODE_FLAG },
    { "datetime", NULL, 976555, 56557, NUITKA_BYTECODE_FLAG },
    { "dbm", NULL, 1033112, 4177, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "dbm.dumb", NULL, 1037289, 8411, NUITKA_BYTECODE_FLAG },
    { "dbm.gnu", NULL, 1045700, 228, NUITKA_BYTECODE_FLAG },
    { "dbm.ndbm", NULL, 1045928, 227, NUITKA_BYTECODE_FLAG },
    { "decimal", NULL, 1046155, 162183, NUITKA_BYTECODE_FLAG },
    { "difflib", NULL, 1208338, 59449, NUITKA_BYTECODE_FLAG },
    { "distutils", NULL, 1267787, 2831, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "distutils.archive_util", NULL, 1270618, 6389, NUITKA_BYTECODE_FLAG },
    { "distutils.bcppcompiler", NULL, 1277007, 6512, NUITKA_BYTECODE_FLAG },
    { "distutils.ccompiler", NULL, 1283519, 33227, NUITKA_BYTECODE_FLAG },
    { "distutils.cmd", NULL, 1316746, 13919, NUITKA_BYTECODE_FLAG },
    { "distutils.command", NULL, 1330665, 566, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "distutils.command.bdist", NULL, 1331231, 3665, NUITKA_BYTECODE_FLAG },
    { "distutils.command.bdist_dumb", NULL, 1334896, 3579, NUITKA_BYTECODE_FLAG },
    { "distutils.command.bdist_rpm", NULL, 1338475, 12504, NUITKA_BYTECODE_FLAG },
    { "distutils.command.bdist_wininst", NULL, 1350979, 8018, NUITKA_BYTECODE_FLAG },
    { "distutils.command.build", NULL, 1358997, 3846, NUITKA_BYTECODE_FLAG },
    { "distutils.command.build_clib", NULL, 1362843, 4896, NUITKA_BYTECODE_FLAG },
    { "distutils.command.build_ext", NULL, 1367739, 15773, NUITKA_BYTECODE_FLAG },
    { "distutils.command.build_py", NULL, 1383512, 10402, NUITKA_BYTECODE_FLAG },
    { "distutils.command.build_scripts", NULL, 1393914, 4301, NUITKA_BYTECODE_FLAG },
    { "distutils.command.check", NULL, 1398215, 4821, NUITKA_BYTECODE_FLAG },
    { "distutils.command.clean", NULL, 1403036, 2103, NUITKA_BYTECODE_FLAG },
    { "distutils.command.config", NULL, 1405139, 10207, NUITKA_BYTECODE_FLAG },
    { "distutils.command.install", NULL, 1415346, 13530, NUITKA_BYTECODE_FLAG },
    { "distutils.command.install_data", NULL, 1428876, 2296, NUITKA_BYTECODE_FLAG },
    { "distutils.command.install_egg_info", NULL, 1431172, 2994, NUITKA_BYTECODE_FLAG },
    { "distutils.command.install_headers", NULL, 1434166, 1711, NUITKA_BYTECODE_FLAG },
    { "distutils.command.install_lib", NULL, 1435877, 5089, NUITKA_BYTECODE_FLAG },
    { "distutils.command.install_scripts", NULL, 1440966, 2153, NUITKA_BYTECODE_FLAG },
    { "distutils.command.register", NULL, 1443119, 8488, NUITKA_BYTECODE_FLAG },
    { "distutils.command.sdist", NULL, 1451607, 14519, NUITKA_BYTECODE_FLAG },
    { "distutils.command.upload", NULL, 1466126, 5101, NUITKA_BYTECODE_FLAG },
    { "distutils.config", NULL, 1471227, 3496, NUITKA_BYTECODE_FLAG },
    { "distutils.core", NULL, 1474723, 6621, NUITKA_BYTECODE_FLAG },
    { "distutils.cygwinccompiler", NULL, 1481344, 8539, NUITKA_BYTECODE_FLAG },
    { "distutils.debug", NULL, 1489883, 219, NUITKA_BYTECODE_FLAG },
    { "distutils.dep_util", NULL, 1490102, 2735, NUITKA_BYTECODE_FLAG },
    { "distutils.dir_util", NULL, 1492837, 5829, NUITKA_BYTECODE_FLAG },
    { "distutils.dist", NULL, 1498666, 34450, NUITKA_BYTECODE_FLAG },
    { "distutils.errors", NULL, 1533116, 5505, NUITKA_BYTECODE_FLAG },
    { "distutils.extension", NULL, 1538621, 6916, NUITKA_BYTECODE_FLAG },
    { "distutils.fancy_getopt", NULL, 1545537, 10628, NUITKA_BYTECODE_FLAG },
    { "distutils.file_util", NULL, 1556165, 5914, NUITKA_BYTECODE_FLAG },
    { "distutils.filelist", NULL, 1562079, 9849, NUITKA_BYTECODE_FLAG },
    { "distutils.log", NULL, 1571928, 2330, NUITKA_BYTECODE_FLAG },
    { "distutils.msvccompiler", NULL, 1574258, 14582, NUITKA_BYTECODE_FLAG },
    { "distutils.spawn", NULL, 1588840, 5020, NUITKA_BYTECODE_FLAG },
    { "distutils.sysconfig", NULL, 1593860, 11869, NUITKA_BYTECODE_FLAG },
    { "distutils.text_file", NULL, 1605729, 8456, NUITKA_BYTECODE_FLAG },
    { "distutils.unixccompiler", NULL, 1614185, 6490, NUITKA_BYTECODE_FLAG },
    { "distutils.util", NULL, 1620675, 15066, NUITKA_BYTECODE_FLAG },
    { "distutils.version", NULL, 1635741, 7367, NUITKA_BYTECODE_FLAG },
    { "distutils.versionpredicate", NULL, 1643108, 5114, NUITKA_BYTECODE_FLAG },
    { "doctest", NULL, 1648222, 75621, NUITKA_BYTECODE_FLAG },
    { "dummy_threading", NULL, 1723843, 1135, NUITKA_BYTECODE_FLAG },
    { "email", NULL, 1724978, 1702, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "email._encoded_words", NULL, 1726680, 5619, NUITKA_BYTECODE_FLAG },
    { "email._header_value_parser", NULL, 1732299, 75638, NUITKA_BYTECODE_FLAG },
    { "email._parseaddr", NULL, 1807937, 12359, NUITKA_BYTECODE_FLAG },
    { "email._policybase", NULL, 1820296, 14861, NUITKA_BYTECODE_FLAG },
    { "email.base64mime", NULL, 1835157, 3246, NUITKA_BYTECODE_FLAG },
    { "email.charset", NULL, 1838403, 11540, NUITKA_BYTECODE_FLAG },
    { "email.contentmanager", NULL, 1849943, 7306, NUITKA_BYTECODE_FLAG },
    { "email.encoders", NULL, 1857249, 1675, NUITKA_BYTECODE_FLAG },
    { "email.errors", NULL, 1858924, 6202, NUITKA_BYTECODE_FLAG },
    { "email.feedparser", NULL, 1865126, 10636, NUITKA_BYTECODE_FLAG },
    { "email.generator", NULL, 1875762, 12511, NUITKA_BYTECODE_FLAG },
    { "email.header", NULL, 1888273, 16391, NUITKA_BYTECODE_FLAG },
    { "email.headerregistry", NULL, 1904664, 21308, NUITKA_BYTECODE_FLAG },
    { "email.iterators", NULL, 1925972, 1943, NUITKA_BYTECODE_FLAG },
    { "email.message", NULL, 1927915, 37951, NUITKA_BYTECODE_FLAG },
    { "email.mime", NULL, 1965866, 157, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "email.mime.application", NULL, 1966023, 1468, NUITKA_BYTECODE_FLAG },
    { "email.mime.audio", NULL, 1967491, 2627, NUITKA_BYTECODE_FLAG },
    { "email.mime.base", NULL, 1970118, 1093, NUITKA_BYTECODE_FLAG },
    { "email.mime.image", NULL, 1971211, 1913, NUITKA_BYTECODE_FLAG },
    { "email.mime.message", NULL, 1973124, 1342, NUITKA_BYTECODE_FLAG },
    { "email.mime.multipart", NULL, 1974466, 1564, NUITKA_BYTECODE_FLAG },
    { "email.mime.nonmultipart", NULL, 1976030, 779, NUITKA_BYTECODE_FLAG },
    { "email.mime.text", NULL, 1976809, 1326, NUITKA_BYTECODE_FLAG },
    { "email.parser", NULL, 1978135, 5758, NUITKA_BYTECODE_FLAG },
    { "email.policy", NULL, 1983893, 9651, NUITKA_BYTECODE_FLAG },
    { "email.quoprimime", NULL, 1993544, 7675, NUITKA_BYTECODE_FLAG },
    { "email.utils", NULL, 2001219, 9478, NUITKA_BYTECODE_FLAG },
    { "filecmp", NULL, 2010697, 8318, NUITKA_BYTECODE_FLAG },
    { "fileinput", NULL, 2019015, 13209, NUITKA_BYTECODE_FLAG },
    { "fnmatch", NULL, 2032224, 3337, NUITKA_BYTECODE_FLAG },
    { "formatter", NULL, 2035561, 17564, NUITKA_BYTECODE_FLAG },
    { "fractions", NULL, 2053125, 18439, NUITKA_BYTECODE_FLAG },
    { "ftplib", NULL, 2071564, 28077, NUITKA_BYTECODE_FLAG },
    { "getopt", NULL, 2099641, 6250, NUITKA_BYTECODE_FLAG },
    { "getpass", NULL, 2105891, 4175, NUITKA_BYTECODE_FLAG },
    { "gettext", NULL, 2110066, 14179, NUITKA_BYTECODE_FLAG },
    { "glob", NULL, 2124245, 4270, NUITKA_BYTECODE_FLAG },
    { "gzip", NULL, 2128515, 17196, NUITKA_BYTECODE_FLAG },
    { "hashlib", NULL, 2145711, 6591, NUITKA_BYTECODE_FLAG },
    { "hmac", NULL, 2152302, 6113, NUITKA_BYTECODE_FLAG },
    { "html", NULL, 2158415, 3408, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "html.entities", NULL, 2161823, 50480, NUITKA_BYTECODE_FLAG },
    { "html.parser", NULL, 2212303, 11118, NUITKA_BYTECODE_FLAG },
    { "http", NULL, 2223421, 5933, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "http.client", NULL, 2229354, 34059, NUITKA_BYTECODE_FLAG },
    { "http.cookiejar", NULL, 2263413, 53418, NUITKA_BYTECODE_FLAG },
    { "http.cookies", NULL, 2316831, 15255, NUITKA_BYTECODE_FLAG },
    { "http.server", NULL, 2332086, 33378, NUITKA_BYTECODE_FLAG },
    { "imaplib", NULL, 2365464, 41440, NUITKA_BYTECODE_FLAG },
    { "imghdr", NULL, 2406904, 4153, NUITKA_BYTECODE_FLAG },
    { "imp", NULL, 2411057, 9753, NUITKA_BYTECODE_FLAG },
    { "importlib.abc", NULL, 2420810, 13486, NUITKA_BYTECODE_FLAG },
    { "importlib.resources", NULL, 2434296, 8339, NUITKA_BYTECODE_FLAG },
    { "importlib.util", NULL, 2442635, 9356, NUITKA_BYTECODE_FLAG },
    { "ipaddress", NULL, 2451991, 63005, NUITKA_BYTECODE_FLAG },
    { "json", NULL, 2514996, 12349, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "json.decoder", NULL, 2527345, 9835, NUITKA_BYTECODE_FLAG },
    { "json.encoder", NULL, 2537180, 11317, NUITKA_BYTECODE_FLAG },
    { "json.scanner", NULL, 2548497, 2007, NUITKA_BYTECODE_FLAG },
    { "json.tool", NULL, 2550504, 1488, NUITKA_BYTECODE_FLAG },
    { "lib2to3", NULL, 2551992, 154, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "lib2to3.btm_matcher", NULL, 2552146, 4904, NUITKA_BYTECODE_FLAG },
    { "lib2to3.btm_utils", NULL, 2557050, 6154, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixer_base", NULL, 2563204, 6246, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixer_util", NULL, 2569450, 12057, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes", NULL, 2581507, 160, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "lib2to3.fixes.fix_apply", NULL, 2581667, 1698, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_asserts", NULL, 2583365, 1283, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_basestring", NULL, 2584648, 673, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_buffer", NULL, 2585321, 818, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_dict", NULL, 2586139, 3326, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_except", NULL, 2589465, 2828, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_exec", NULL, 2592293, 1159, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_execfile", NULL, 2593452, 1683, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_exitfunc", NULL, 2595135, 2306, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_filter", NULL, 2597441, 2371, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_funcattrs", NULL, 2599812, 984, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_future", NULL, 2600796, 794, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_getcwdu", NULL, 2601590, 798, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_has_key", NULL, 2602388, 2928, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_idioms", NULL, 2605316, 3913, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_import", NULL, 2609229, 2795, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_imports", NULL, 2612024, 4359, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_imports2", NULL, 2616383, 558, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_input", NULL, 2616941, 960, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_intern", NULL, 2617901, 1167, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_isinstance", NULL, 2619068, 1565, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_itertools", NULL, 2620633, 1554, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_itertools_imports", NULL, 2622187, 1590, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_long", NULL, 2623777, 715, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_map", NULL, 2624492, 3103, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_metaclass", NULL, 2627595, 5356, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_methodattrs", NULL, 2632951, 946, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_ne", NULL, 2633897, 817, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_next", NULL, 2634714, 3070, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_nonzero", NULL, 2637784, 933, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_numliterals", NULL, 2638717, 1029, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_operator", NULL, 2639746, 4246, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_paren", NULL, 2643992, 1400, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_print", NULL, 2645392, 2335, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_raise", NULL, 2647727, 2259, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_raw_input", NULL, 2649986, 805, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_reduce", NULL, 2650791, 1140, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_reload", NULL, 2651931, 1179, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_renames", NULL, 2653110, 2003, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_repr", NULL, 2655113, 855, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_set_literal", NULL, 2655968, 1687, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_standarderror", NULL, 2657655, 730, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_sys_exc", NULL, 2658385, 1411, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_throw", NULL, 2659796, 1812, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_tuple_params", NULL, 2661608, 4606, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_types", NULL, 2666214, 1839, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_unicode", NULL, 2668053, 1551, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_urllib", NULL, 2669604, 5971, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_ws_comma", NULL, 2675575, 1133, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_xrange", NULL, 2676708, 2546, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_xreadlines", NULL, 2679254, 1127, NUITKA_BYTECODE_FLAG },
    { "lib2to3.fixes.fix_zip", NULL, 2680381, 1591, NUITKA_BYTECODE_FLAG },
    { "lib2to3.main", NULL, 2681972, 8547, NUITKA_BYTECODE_FLAG },
    { "lib2to3.patcomp", NULL, 2690519, 5622, NUITKA_BYTECODE_FLAG },
    { "lib2to3.pgen2", NULL, 2696141, 190, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "lib2to3.pgen2.driver", NULL, 2696331, 5151, NUITKA_BYTECODE_FLAG },
    { "lib2to3.pgen2.grammar", NULL, 2701482, 7027, NUITKA_BYTECODE_FLAG },
    { "lib2to3.pgen2.literals", NULL, 2708509, 1569, NUITKA_BYTECODE_FLAG },
    { "lib2to3.pgen2.parse", NULL, 2710078, 6315, NUITKA_BYTECODE_FLAG },
    { "lib2to3.pgen2.pgen", NULL, 2716393, 9791, NUITKA_BYTECODE_FLAG },
    { "lib2to3.pgen2.token", NULL, 2726184, 1883, NUITKA_BYTECODE_FLAG },
    { "lib2to3.pgen2.tokenize", NULL, 2728067, 15151, NUITKA_BYTECODE_FLAG },
    { "lib2to3.pygram", NULL, 2743218, 1209, NUITKA_BYTECODE_FLAG },
    { "lib2to3.pytree", NULL, 2744427, 25014, NUITKA_BYTECODE_FLAG },
    { "lib2to3.refactor", NULL, 2769441, 20415, NUITKA_BYTECODE_FLAG },
    { "logging", NULL, 2789856, 62577, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "logging.config", NULL, 2852433, 23026, NUITKA_BYTECODE_FLAG },
    { "logging.handlers", NULL, 2875459, 42994, NUITKA_BYTECODE_FLAG },
    { "lzma", NULL, 2918453, 11950, NUITKA_BYTECODE_FLAG },
    { "macpath", NULL, 2930403, 5818, NUITKA_BYTECODE_FLAG },
    { "mailbox", NULL, 2936221, 63659, NUITKA_BYTECODE_FLAG },
    { "mailcap", NULL, 2999880, 6495, NUITKA_BYTECODE_FLAG },
    { "mimetypes", NULL, 3006375, 15479, NUITKA_BYTECODE_FLAG },
    { "modulefinder", NULL, 3021854, 15363, NUITKA_BYTECODE_FLAG },
    { "multiprocessing", NULL, 3037217, 538, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "multiprocessing.connection", NULL, 3037755, 24943, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.context", NULL, 3062698, 13124, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.dummy", NULL, 3075822, 3816, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "multiprocessing.dummy.connection", NULL, 3079638, 2524, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.forkserver", NULL, 3082162, 7775, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.heap", NULL, 3089937, 6435, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.managers", NULL, 3096372, 34024, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.pool", NULL, 3130396, 21693, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.popen_fork", NULL, 3152089, 2537, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.popen_forkserver", NULL, 3154626, 2370, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.popen_spawn_posix", NULL, 3156996, 2152, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.process", NULL, 3159148, 9437, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.queues", NULL, 3168585, 9448, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.reduction", NULL, 3178033, 8029, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.resource_sharer", NULL, 3186062, 5214, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.semaphore_tracker", NULL, 3191276, 3751, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.sharedctypes", NULL, 3195027, 6928, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.spawn", NULL, 3201955, 6489, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.synchronize", NULL, 3208444, 11194, NUITKA_BYTECODE_FLAG },
    { "multiprocessing.util", NULL, 3219638, 9958, NUITKA_BYTECODE_FLAG },
    { "netrc", NULL, 3229596, 3774, NUITKA_BYTECODE_FLAG },
    { "nntplib", NULL, 3233370, 33762, NUITKA_BYTECODE_FLAG },
    { "ntpath", NULL, 3267132, 12986, NUITKA_BYTECODE_FLAG },
    { "nturl2path", NULL, 3280118, 1626, NUITKA_BYTECODE_FLAG },
    { "numbers", NULL, 3281744, 12203, NUITKA_BYTECODE_FLAG },
    { "optparse", NULL, 3293947, 47904, NUITKA_BYTECODE_FLAG },
    { "pathlib", NULL, 3341851, 41474, NUITKA_BYTECODE_FLAG },
    { "pdb", NULL, 3383325, 46773, NUITKA_BYTECODE_FLAG },
    { "pickle", NULL, 3430098, 42977, NUITKA_BYTECODE_FLAG },
    { "pickletools", NULL, 3473075, 65342, NUITKA_BYTECODE_FLAG },
    { "pipes", NULL, 3538417, 7814, NUITKA_BYTECODE_FLAG },
    { "pkgutil", NULL, 3546231, 16371, NUITKA_BYTECODE_FLAG },
    { "platform", NULL, 3562602, 28186, NUITKA_BYTECODE_FLAG },
    { "plistlib", NULL, 3590788, 25106, NUITKA_BYTECODE_FLAG },
    { "poplib", NULL, 3615894, 13346, NUITKA_BYTECODE_FLAG },
    { "pprint", NULL, 3629240, 15830, NUITKA_BYTECODE_FLAG },
    { "profile", NULL, 3645070, 13852, NUITKA_BYTECODE_FLAG },
    { "pstats", NULL, 3658922, 22305, NUITKA_BYTECODE_FLAG },
    { "pty", NULL, 3681227, 3894, NUITKA_BYTECODE_FLAG },
    { "py_compile", NULL, 3685121, 7041, NUITKA_BYTECODE_FLAG },
    { "pyclbr", NULL, 3692162, 10384, NUITKA_BYTECODE_FLAG },
    { "pydoc", NULL, 3702546, 84436, NUITKA_BYTECODE_FLAG },
    { "pydoc_data", NULL, 3786982, 157, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "pydoc_data.topics", NULL, 3787139, 411666, NUITKA_BYTECODE_FLAG },
    { "queue", NULL, 4198805, 11483, NUITKA_BYTECODE_FLAG },
    { "random", NULL, 4210288, 19394, NUITKA_BYTECODE_FLAG },
    { "rlcompleter", NULL, 4229682, 5747, NUITKA_BYTECODE_FLAG },
    { "runpy", NULL, 4235429, 7956, NUITKA_BYTECODE_FLAG },
    { "sched", NULL, 4243385, 6532, NUITKA_BYTECODE_FLAG },
    { "secrets", NULL, 4249917, 2195, NUITKA_BYTECODE_FLAG },
    { "selectors", NULL, 4252112, 16959, NUITKA_BYTECODE_FLAG },
    { "shelve", NULL, 4269071, 9517, NUITKA_BYTECODE_FLAG },
    { "shlex", NULL, 4278588, 7001, NUITKA_BYTECODE_FLAG },
    { "shutil", NULL, 4285589, 30545, NUITKA_BYTECODE_FLAG },
    { "signal", NULL, 4316134, 2523, NUITKA_BYTECODE_FLAG },
    { "site", NULL, 558, 17467, NUITKA_BYTECODE_FLAG },
    { "smtpd", NULL, 4318657, 26615, NUITKA_BYTECODE_FLAG },
    { "smtplib", NULL, 4345272, 35359, NUITKA_BYTECODE_FLAG },
    { "sndhdr", NULL, 4380631, 6914, NUITKA_BYTECODE_FLAG },
    { "socket", NULL, 4387545, 22032, NUITKA_BYTECODE_FLAG },
    { "socketserver", NULL, 4409577, 24197, NUITKA_BYTECODE_FLAG },
    { "sqlite3", NULL, 4433774, 185, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "sqlite3.dbapi2", NULL, 4433959, 2504, NUITKA_BYTECODE_FLAG },
    { "sqlite3.dump", NULL, 4436463, 1947, NUITKA_BYTECODE_FLAG },
    { "ssl", NULL, 4438410, 39793, NUITKA_BYTECODE_FLAG },
    { "statistics", NULL, 4478203, 18175, NUITKA_BYTECODE_FLAG },
    { "string", NULL, 4496378, 7846, NUITKA_BYTECODE_FLAG },
    { "subprocess", NULL, 4504224, 38694, NUITKA_BYTECODE_FLAG },
    { "sunau", NULL, 4542918, 17222, NUITKA_BYTECODE_FLAG },
    { "symbol", NULL, 4560140, 2576, NUITKA_BYTECODE_FLAG },
    { "symtable", NULL, 4562716, 10456, NUITKA_BYTECODE_FLAG },
    { "sysconfig", NULL, 4573172, 15285, NUITKA_BYTECODE_FLAG },
    { "tabnanny", NULL, 4588457, 6989, NUITKA_BYTECODE_FLAG },
    { "tarfile", NULL, 4595446, 61841, NUITKA_BYTECODE_FLAG },
    { "telnetlib", NULL, 4657287, 18113, NUITKA_BYTECODE_FLAG },
    { "tempfile", NULL, 4675400, 22145, NUITKA_BYTECODE_FLAG },
    { "textwrap", NULL, 4697545, 13623, NUITKA_BYTECODE_FLAG },
    { "this", NULL, 4711168, 1288, NUITKA_BYTECODE_FLAG },
    { "timeit", NULL, 4712456, 11658, NUITKA_BYTECODE_FLAG },
    { "trace", NULL, 4724114, 19156, NUITKA_BYTECODE_FLAG },
    { "tracemalloc", NULL, 4743270, 17287, NUITKA_BYTECODE_FLAG },
    { "tty", NULL, 4760557, 1105, NUITKA_BYTECODE_FLAG },
    { "typing", NULL, 4761662, 49937, NUITKA_BYTECODE_FLAG },
    { "unittest", NULL, 4811599, 3022, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "unittest.case", NULL, 4814621, 48094, NUITKA_BYTECODE_FLAG },
    { "unittest.loader", NULL, 4862715, 14280, NUITKA_BYTECODE_FLAG },
    { "unittest.main", NULL, 4876995, 7449, NUITKA_BYTECODE_FLAG },
    { "unittest.mock", NULL, 4884444, 63004, NUITKA_BYTECODE_FLAG },
    { "unittest.result", NULL, 4947448, 7263, NUITKA_BYTECODE_FLAG },
    { "unittest.runner", NULL, 4954711, 6992, NUITKA_BYTECODE_FLAG },
    { "unittest.signals", NULL, 4961703, 2205, NUITKA_BYTECODE_FLAG },
    { "unittest.suite", NULL, 4963908, 9214, NUITKA_BYTECODE_FLAG },
    { "unittest.util", NULL, 4973122, 4532, NUITKA_BYTECODE_FLAG },
    { "urllib", NULL, 4977654, 153, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "urllib.error", NULL, 4977807, 2787, NUITKA_BYTECODE_FLAG },
    { "urllib.parse", NULL, 4980594, 29630, NUITKA_BYTECODE_FLAG },
    { "urllib.request", NULL, 5010224, 72314, NUITKA_BYTECODE_FLAG },
    { "urllib.response", NULL, 5082538, 3260, NUITKA_BYTECODE_FLAG },
    { "urllib.robotparser", NULL, 5085798, 7072, NUITKA_BYTECODE_FLAG },
    { "uu", NULL, 5092870, 3624, NUITKA_BYTECODE_FLAG },
    { "uuid", NULL, 5096494, 23210, NUITKA_BYTECODE_FLAG },
    { "venv", NULL, 5119704, 13639, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "wave", NULL, 5133343, 18299, NUITKA_BYTECODE_FLAG },
    { "weakref", NULL, 5151642, 19110, NUITKA_BYTECODE_FLAG },
    { "webbrowser", NULL, 5170752, 16386, NUITKA_BYTECODE_FLAG },
    { "wsgiref", NULL, 5187138, 749, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "wsgiref.handlers", NULL, 5187887, 16158, NUITKA_BYTECODE_FLAG },
    { "wsgiref.headers", NULL, 5204045, 7770, NUITKA_BYTECODE_FLAG },
    { "wsgiref.simple_server", NULL, 5211815, 5216, NUITKA_BYTECODE_FLAG },
    { "wsgiref.util", NULL, 5217031, 5191, NUITKA_BYTECODE_FLAG },
    { "wsgiref.validate", NULL, 5222222, 14687, NUITKA_BYTECODE_FLAG },
    { "xdrlib", NULL, 5236909, 8335, NUITKA_BYTECODE_FLAG },
    { "xml", NULL, 5245244, 717, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "xml.dom", NULL, 5245961, 5469, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "xml.dom.NodeFilter", NULL, 5251430, 984, NUITKA_BYTECODE_FLAG },
    { "xml.dom.domreg", NULL, 5252414, 2801, NUITKA_BYTECODE_FLAG },
    { "xml.dom.expatbuilder", NULL, 5255215, 27031, NUITKA_BYTECODE_FLAG },
    { "xml.dom.minicompat", NULL, 5282246, 2830, NUITKA_BYTECODE_FLAG },
    { "xml.dom.minidom", NULL, 5285076, 55630, NUITKA_BYTECODE_FLAG },
    { "xml.dom.pulldom", NULL, 5340706, 10503, NUITKA_BYTECODE_FLAG },
    { "xml.dom.xmlbuilder", NULL, 5351209, 12450, NUITKA_BYTECODE_FLAG },
    { "xml.etree", NULL, 5363659, 156, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "xml.etree.ElementInclude", NULL, 5363815, 1592, NUITKA_BYTECODE_FLAG },
    { "xml.etree.ElementPath", NULL, 5365407, 6360, NUITKA_BYTECODE_FLAG },
    { "xml.etree.ElementTree", NULL, 5371767, 44824, NUITKA_BYTECODE_FLAG },
    { "xml.etree.cElementTree", NULL, 5416591, 198, NUITKA_BYTECODE_FLAG },
    { "xml.parsers", NULL, 5416789, 330, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "xml.parsers.expat", NULL, 5417119, 359, NUITKA_BYTECODE_FLAG },
    { "xml.sax", NULL, 5417478, 3154, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "xml.sax._exceptions", NULL, 5420632, 5498, NUITKA_BYTECODE_FLAG },
    { "xml.sax.expatreader", NULL, 5426130, 12401, NUITKA_BYTECODE_FLAG },
    { "xml.sax.handler", NULL, 5438531, 12374, NUITKA_BYTECODE_FLAG },
    { "xml.sax.saxutils", NULL, 5450905, 12827, NUITKA_BYTECODE_FLAG },
    { "xml.sax.xmlreader", NULL, 5463732, 16935, NUITKA_BYTECODE_FLAG },
    { "xmlrpc", NULL, 5480667, 153, NUITKA_BYTECODE_FLAG | NUITKA_PACKAGE_FLAG },
    { "xmlrpc.client", NULL, 5480820, 34559, NUITKA_BYTECODE_FLAG },
    { "xmlrpc.server", NULL, 5515379, 29401, NUITKA_BYTECODE_FLAG },
    { "zipapp", NULL, 5544780, 5814, NUITKA_BYTECODE_FLAG },
    { "zipfile", NULL, 5550594, 49891, NUITKA_BYTECODE_FLAG },
    { NULL, NULL, 0, 0, 0 }
};

void setupMetaPathBasedLoader( void )
{
    static bool init_done = false;

    if ( init_done == false )
    {
        registerMetaPathBasedUnfreezer( meta_path_loader_entries );
        init_done = true;
    }
}
