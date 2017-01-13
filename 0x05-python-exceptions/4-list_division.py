#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    divides one list per another, element by element
    exercise to handle exceptions

    my_list_1: a list of anything
    my_list_2: another list, similar
    list_length: number of elements to divide

    Result: a list containing the result
    """
    result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            result.append(div)

    return (result)
