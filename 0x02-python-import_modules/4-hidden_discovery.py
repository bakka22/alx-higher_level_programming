#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    y = dir(hidden_4)
    x = len(y)
    for i in range(x):
        if y[i][1] != '_':
            print(y[i])
