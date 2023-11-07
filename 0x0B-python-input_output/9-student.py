#!/usr/bin/python3
# 9-student.py
# Juan Duque <3428@holbertonschool.com>
""" Define  a class Student that defines a student by
    first_name
    last_name
    age
    """


class Student:

    """ Instantiation the news attributes publics"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """ Declaration the new public method"""

    def to_json(self):
        """ Return obj in dict mode"""
        return self.__dict__
