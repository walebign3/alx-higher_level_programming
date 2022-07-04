#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if length == 0:
        n_tuple = (length, None)
    else:
        n_tuple = (length, sentence[0])

    return (n_tuple)
