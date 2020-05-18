#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elem = 0  # counter of elements in the list
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")  # only print integers
            elem += 1
        except (ValueError, TypeError):
            # argument the right type, or right type but an inappropriate value
            pass
    print()
    return elem
