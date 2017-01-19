#include <Python.h>
#include <stdio.h>
#include <listobject.h>
#include <object.h>
#include <string.h>

#define TYPE(ob) (((PyObject*)(ob))->ob_type)
#define SIZE(ob) (((PyVarObject*)(ob))->ob_size)

/**
 * is_type - check if string is list
 * @s: a string
 * @type: type to check for
 * Return: 1 if true 0 otherwise
 */
int is_type(const char *s, const char *type)
{
	unsigned int i;

	if (strlen(s) != strlen(type))
		return (0);
	for(i = 0; *(s + i) && *(s + i) == *(type + i); ++i)
		;
	if (i == strlen(s))
		return (1);
	return (0);
}


/**
 * print_python_bytes - print strings in python
 * @p: pyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, max_v, i;

/*	printf("%s\n", p->ob_type->tp_name);*/
	puts("[.] bytes object info");
	if (is_type(TYPE(p)->tp_name, "bytes"))
	{
		size = SIZE(p);
		printf("  size: %lu\n", size);
		printf("  trying string: %s\n",((PyBytesObject *)p)->ob_sval);
		max_v = (size >= 10 ) ? 10 : size + 1;
		printf("  first %lu bytes:", max_v);
		for (i = 0; i < max_v; i += 1)
			printf(" %02x",
			       (((PyBytesObject *)p)->ob_sval[i]) & 0xff);
		puts("");
	}
	else
	{
		puts("  [ERROR] Invalid Bytes Object");
	}
}


/**
 * print_python_float - print info about floats
 * @p: a python object
 */
void print_python_float(PyObject *p)
{
	PyObject* str_exc_type;
	PyObject* pyStr;

	puts("[.] float object info");
/*	printf("%s\n", p->ob_type->tp_name);*/
	if (is_type(TYPE(p)->tp_name, "float"))
	{
		str_exc_type = PyObject_Repr(p);
		pyStr = PyUnicode_AsEncodedString(str_exc_type,
							    "utf-8", "Error ~");
		printf("  value: %s\n",((PyBytesObject *)pyStr)->ob_sval);
	}
	else
	{
		puts("  [ERROR] Invalid Float Object");
	}
}

/* thanks to https://mail.python.org/pipermail/python-list/2009-March/527813.
 * html
 */


/**
 * print_python_list_info - print info about python lists
 * @p: a python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *o;

	puts("[*] Python list info");
/*	printf("%s\n", p->ob_type->tp_name);*/
	if (is_type(TYPE(p)->tp_name, "list"))
	{
		size = SIZE(p);
		printf("[*] Size of the Python List = %lu\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; ++i)
		{
			o = ((PyListObject *)(p))->ob_item[i];
			printf("Element %lu: %s\n",i ,
			       (TYPE(o))->tp_name);
			if (is_type(TYPE(o)->tp_name, "bytes"))
				print_python_bytes(o);
			if (is_type(TYPE(o)->tp_name, "float"))
				print_python_float(o);
		}
	}
	else
	{
		puts("  [ERROR] Invalid List Object");
	}
}
