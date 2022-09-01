#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_key = list(a_dictionary.keys())
    max_value = list(a_dictionary.values())
    return (max_key[max_value.index(max(max_value))])
