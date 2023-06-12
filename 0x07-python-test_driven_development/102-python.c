#include <Python.h>
/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to the Python object
 *
 * Description: This function prints the type, length, and value of a Python string object.
 * If the object is not a valid string, it prints an error message.
 */
void print_python_string(PyObject *p)
{
Py_ssize_t length;
Py_ssize_t i;

printf("[.] string object info\n");

if (!PyUnicode_Check(p))
{
printf("  [ERROR] Invalid String Object\n");
return;
}

length = PyUnicode_GET_LENGTH(p);
const char *value = PyUnicode_AsUTF8AndSize(p, &length);

printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
printf("  length: %ld\n", length);
printf("  value: %s\n", value);
}
