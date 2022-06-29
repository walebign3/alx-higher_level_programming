#!/usr/bin/python3
def remove_char_at(str, n):
    replace = ""
    for i in range(len(str)):
        if i != n:
            replace = replace + str[i]
    return (replace)
