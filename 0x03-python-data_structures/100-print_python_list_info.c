#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints Python list info
 *
 * @p: PyObject representing the Python list
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
Py_ssize_t size = PyList_Size(p);
Py_ssize_t i;
PyListObject *list = (PyListObject *)p;

printf("[*] Size of the Python List = %ld\n", size);

printf("[*] Allocated = %ld\n", list->allocated);

for (i = 0; i < size; i++)
{

printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
}
