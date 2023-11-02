#include <Python.h>

/**
 * print_python_string - Print information about a Python string object
 * @p: Pointer to the Python string object
 * Return : none
 */
void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p)) {
        printf("[ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t size;
    const char *string = PyUnicode_AsUTF8AndSize(p, &size);

    if (string == NULL) {
        printf("[ERROR] Can't convert String to UTF8\n");
        return;
    }

    printf("  length: %ld\n", size);
    printf("  value: %s\n", string);
}
