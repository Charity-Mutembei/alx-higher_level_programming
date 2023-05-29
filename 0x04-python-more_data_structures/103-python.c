#include <Python.h>
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
int list_size, list_alloc, i;
const char *element_type;
PyListObject *list_obj = (PyListObject *)p;
PyVarObject *var_obj = (PyVarObject *)p;

list_size = var_obj->ob_size;
list_alloc = list_obj->allocated;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %d\n", list_size);
printf("[*] Allocated = %d\n", list_alloc);

for (i = 0; i < list_size; i++)
{
element_type = list_obj->ob_item[i]->ob_type->tp_name;
printf("Element %d: %s\n", i, element_type);
if (strcmp(element_type, "bytes") == 0)
print_python_bytes(list_obj->ob_item[i]);
}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
unsigned char byte, max_bytes;
PyBytesObject *bytes_obj = (PyBytesObject *)p;

printf("[.] Bytes object info\n");
if (strcmp(p->ob_type->tp_name, "bytes") != 0)
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

printf("  Size: %ld\n", ((PyVarObject *)p)->ob_size);
printf("  Trying string: %s\n", bytes_obj->ob_sval);

if (((PyVarObject *)p)->ob_size > 10)
max_bytes = 10;
else
max_bytes = ((PyVarObject *)p)->ob_size + 1;

printf("  First %d bytes: ", max_bytes);
for (byte = 0; byte < max_bytes; byte++)
{
printf("%02hhx", bytes_obj->ob_sval[byte]);
if (byte == (max_bytes - 1))
printf("\n");
else
printf(" ");
}
}
