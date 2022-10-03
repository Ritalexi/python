#!/usr/bin/python3
"""
File:  1-write_file.py
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    and returns the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
