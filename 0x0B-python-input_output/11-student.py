#!/usr/bin/python3
# 11-student.py
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

    def to_json(self, attrs=None):
        """ Return obj in dict mode"""
        if type(attrs) == list and all(type(index) == str for index in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        for h, k in json.items():
            setattr(self, h, k)
