#!/usr/bin/python3
"""
File:
6-load_from_json_file.py
"""

import json


def load_from_json_file(filename):
    """
    a function that creates an Object from av JSON fie
    """

    with open(filename, mode="r") as file:
        return json.load(file)
