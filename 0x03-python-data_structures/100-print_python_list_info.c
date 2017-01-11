#include <Python.h>
#include <stdio.h>
#include <listobject.h>
#include <object.h>
#include <string.h>

/**
 * is_list - check if string is list
 * @s: a string
 * Return: 1 if true 0 otherwise
 */
int is_list(const char *s)
{
	int i;
	const char *l = "list";

	if (strlen(s) != 4)
		return (0);
	for(i = 0; *(s + i) && *(s + i) == *(l + i); ++i)
		;
	if (i == 4)
		return (1);
	return (0);
}

/**
 * print_python_list_info - print info about python lists
 * @p: a python object
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;

	if (is_list((Py_TYPE(p))->tp_name))
	{
/*		printf("%s\n", (Py_TYPE(p))->tp_name);*/
		size = PyList_Size(p);
		printf("[*] Size of the Python List = %lu\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < size; ++i)
		{
			printf("Element %lu: %s\n",i ,
			       (Py_TYPE(PyList_GetItem(p, i)))->tp_name);
		}
	}
}
