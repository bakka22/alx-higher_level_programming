#!/usr/bin/python3

def safe_function(fct, *args):

    import sys
    try:
        return fct(*args)
    except (ZeroDivisionError, IndexError) as er:
        print("Exception: {}".format(er), file=sys.stderr)
        return None
