#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    x = len(argv)
    print(f"{x} ", end="")
    if x == 1:
        print("argument:")
    elif x == 0:
        print("arguments.")
        sys.exit(0)
    else:
        print("arguments:")
    for i in range(x):
        print(f"{i}: {argv[i]}")
