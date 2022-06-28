#!/usr/bin/python3
for n in range(0, 10):
    for m in range(0, 10):
        if n<m:
            if n+m != 17:
                print("{}{}".format(n,m), end=", ")
            else:
                print("{}{}".format(n,m))
