#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculate(a, op, b):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    elif op == "/":
        return div(a, b)
    else:
        return None


if __name__ == "__main__":
    args_len = len(sys.argv) - 1
    if args_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op not in ("+", "-", "*", "/"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    result = calculate(a, op, b)
    print("{} {} {} = {}".format(a, op, b, result))
