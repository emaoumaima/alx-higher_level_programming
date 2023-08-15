#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - list info
 * @p: PyObj
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p), i;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
