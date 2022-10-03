#!/usr/bin/python3
"""
File: 5-save_to_json_file.py
"""

import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        ans = json.dumps(my_obj)
        return file.write(ans)
