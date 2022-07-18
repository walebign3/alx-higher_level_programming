#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0

    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            num = num + 1

    print()
    return (num)
