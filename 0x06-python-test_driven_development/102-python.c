#include <Python.h>
#include <stdio.h>
#include <listobject.h>
#include <object.h>
#include <string.h>
#include <wchar.h>

#define TYPE(ob) (((PyObject*)(ob))->ob_type)
#define SIZE(ob) (((PyVarObject*)(ob))->ob_size)
#define ASCII(op) (((PyASCIIObject*)op)->state.ascii)
#define COMPACT(op) (((PyASCIIObject*)(op))->state.compact)
#define DATA(op)                     \
	(ASCII(op) ?                   \
	 ((void*)((PyASCIIObject*)(op) + 1)) :		\
	 ((void*)((PyCompactUnicodeObject*)(op) + 1)))



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
 * print_python_string - print strings in python
 * @p: pyObject
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t size;
	int nb_bytes;

/*	printf("%s\n", p->ob_type->tp_name);*/
	puts("[.] string object info");
	if (is_type(TYPE(p)->tp_name, "str"))
	{
		nb_bytes = PyUnicode_KIND(p);
		size = PyUnicode_GET_LENGTH(p);
/*		printf("kind: %d size: %lu\n", nb_bytes, size);*/
		if (ASCII(p) && COMPACT(p))
		{
			puts("  type: compact ascii");
			printf("  length: %lu\n", size);
			printf("  value: %s\n", (char *)(DATA(p)));
		}
		else
		{
			puts("  type: compact unicode object");
			printf("  length: %lu\n", size);
			printf("  value: ");
			if (nb_bytes == 1)
			{
				printf("%s\n", (char *)(DATA(p)));
				printf("HERE\n");
				printf( "%s\n", "\u00E9");
			}
			else
			{
				printf("%s\n", (unsigned short *)(DATA(p)));
			}
		}

	}
	else
	{
		puts("  [ERROR] Invalid String Object");
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
