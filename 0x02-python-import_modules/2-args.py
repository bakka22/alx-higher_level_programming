#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    x = len(argv) - 1
    print(f"{x} ", end="")
    if x == 1:
        print("argument:")
    elif x == 0:
        print("arguments.")
        sys.exit(0)
    else:
        print("arguments:")
    for i in range(1, x + 1):
        print(f"{i}: {argv[i]}")
