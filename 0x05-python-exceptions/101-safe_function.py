#!/usr/bin/python3

def safe_function(fct, *args):

    import sys
    try:
        return fct(args[0], args[1])
    except Exception as er:
        print("Exception: {}".format(er), file=sys.stderr)
        return None
