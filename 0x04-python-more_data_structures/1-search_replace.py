#!/usr/bin/python
def search_replace(my_list, search, replace):
    n = 0
    mynew_list = my_list.copy()
    for i in range(len(mynew_list)):
        c = mynew_list.count(mynew_list[i])
        if c == search:
            n = mynew_list[i]
            for j in range(len(mynew_list)):
                if c == mynew_list[j]:
                    mynew_list[j] = replace
    return (mynew_list)

