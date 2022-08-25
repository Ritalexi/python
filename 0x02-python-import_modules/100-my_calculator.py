#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    len = len(sys.argv)
    if ((len - 1) != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    for i in range(1, len):
        a = int(i[1])
        b = int(i[len])
        if (i[2] != "+"):
            print("Unknown operator. Available operators: +, -, * and /")
            return 1
        else:
            print("{}".format(a), "{}".format(i[2]), "{}".format(a),\
            "=", "{}".format(add(a, b))
            return 0
        if (i[2] != "-"):
            print("Unknown operator. Available operators: +, -, * and /")
            return 1
        else:
            print("{}".format(a), "{}".format(i[2]), "{}".format(a),\
            "=", "{}".format(sub(a, b))
            return 0
        if (i[2] != "*"):
            print("Unknown operator. Available operators: +, -, * and /")
            return 1
        else:
            print("{}".format(a), "{}".format(i[2]), "{}".format(a),\
            "=", "{}".format(mul(a, b))
            return 0
        if (i[2] != "/"):
            print("Unknown operator. Available operators: +, -, * and /")
            return 1
        else:
            print("{}".format(a), "{}".format(i[2]), "{}".format(a),\
            "=", "{}".format(add(a, b))
            return 0
