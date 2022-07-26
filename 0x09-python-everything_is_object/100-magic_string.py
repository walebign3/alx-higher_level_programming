#!/usr/bin/python3
def magic_string(h={'counter': 0}):
    h['counter'] += 1
    return (', '.join(['BestSchool'] * (h['counter'])))
