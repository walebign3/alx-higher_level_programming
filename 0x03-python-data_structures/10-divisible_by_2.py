#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_mylist = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_mylist.append(True)
        else:
            new_mylist.append(False)
    return (new_mylist)
