#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    argv = sys.argv
    x = len(argv)
    oplist = ["+", "-", "*", "/"]
    op = calculator_1.add
    if x != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] not in oplist:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if argv[2] == "-":
        op = calculator_1.sub
    elif argv[2] == "*":
        op = calculator_1.mul
    elif argv[2] == "/":
        op = calculator_1.div
    result = op(a, b)
    print(f"{a} {argv[2]} {b} = {result}")
