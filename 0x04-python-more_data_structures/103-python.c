#include <stdio.h>
#include <Python.h>
/**
 * print_python_list - Prints information about a Python list.
 * @p: Pointer to the Python list object.
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size = PyList_Size(p);
Py_ssize_t i;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
}
/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: Pointer to the Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
PyBytesObject *bytes = (PyBytesObject *)p;
Py_ssize_t size = PyBytes_Size(p);
Py_ssize_t i;
char *str;

printf("[.] Bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  Size: %ld\n", size);
printf("  Trying string: %s\n", PyBytes_AsString(p));

if (size > 10)
{
size = 10;
}

str = bytes->ob_sval;
printf("  first %ld bytes: ", size);
for (i = 0; i < size; i++)
{
printf("%02hhx", str[i]);
if (i < size - 1)
{
printf(" ");
}
}
printf("\n");
}
