#!/usr/bin/python3
def weight_average(my_list=[]):
    y = []
    e = []
    for x in my_list:
        y.append(x[0] * x[1])
        e.append(x[1])
    a = 0
    b = 0
    for i in range(len(y)):
        a += y[i]
        b += e[i]
    return (a / b)
