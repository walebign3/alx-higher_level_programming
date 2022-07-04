#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for i in range(len(my_string)):
        if my_list[i] == 'c' or my_list[i] == 'C':
            my_list[i] = ''
    my_string = ''.join(my_list)
    return my_string
