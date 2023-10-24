#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    x = list_length
    ls = []
    y = 0
    for i in range(x):
        try:
            y = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            y = 0
        except (ValueError, TypeError):
            print("wrong type")
            y = 0
        except IndexError:
            print("out of range")
            y = 0
        finally:
            ls.append(y)
    return (ls)
