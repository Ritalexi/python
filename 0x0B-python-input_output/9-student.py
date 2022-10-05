#!/usr/bin/python3
"""
Module of class Student
"""


class Student:
    """
    A class Studet
    """

    def __init__(self, first_name, last_name, age):
        """
        Public Instantiation with
        first_name, last_name and age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dictionary representation with simple data structure.
        """
       return self.__dict__
