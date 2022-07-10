#!/usr/bin/python
def search_replace(my_list, search, replace):
    mynew_list = my_list.copy()
    for i in range(len(mynew_list)):
        if mynew_list[i] == 2:
            mynew_list[i] = 89
    return (mynew_list)

