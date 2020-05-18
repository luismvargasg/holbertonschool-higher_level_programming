#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except (ZeroDivisionError, IndexError) as ZIE:
        print("Exception: {}".format(ZIE), file=sys.stderr)
        return None
