#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == "+":
        print("{} {} {} = {}".format(sys.argv[1],sys.argv[2],sys.argv[3], add(int(sys.argv[1]),int(sys.argv[3]))))
    elif sys.argv[2] == "-":
        print("{} {} {} = {}".format(sys.argv[1],sys.argv[2],sys.argv[3], sub(sys.argv[1],sys.argv[3])))
    elif sys.argv[2] == "*":
        print("{} {} {} = {}".format(sys.argv[1],sys.argv[2],sys.argv[3], mul(sys.argv[1],sys.argv[3])))
    elif sys.argv[2] == "/":
        print("{} {} {} = {}".format(sys.argv[1],sys.argv[2],sys.argv[3], div(sys.argv[1],sys.argv[3])))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
