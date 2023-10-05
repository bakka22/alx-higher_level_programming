#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    y = 0
    x = len(argv) - 1
    for i in range(1, x + 1):
        y += int(argv[i])

    print(f"{y}")
