#!/usr/bin/python3
def multiple_returns(sentence):
    tup = len(sentence), \
        (sentence[0] if len(sentence) != 0 else None)
    return tup
