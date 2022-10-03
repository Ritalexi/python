#!/usr/bin/python3
"""
File: 2-append_write.py
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file
    and returns the number of characters added:
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
