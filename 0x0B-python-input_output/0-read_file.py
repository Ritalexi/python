#!/usr/bin/python3
"""
File: 0-read_file.py
"""


def read_file(filename=""):
    """
    a function that reads a text file
    and prints it to stdout
    """

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
