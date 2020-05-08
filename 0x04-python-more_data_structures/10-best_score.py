#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        winner = max(list(a_dictionary))
        return winner
    else:
        return None
