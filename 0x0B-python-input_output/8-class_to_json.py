#!/usr/bin/python3
# 8-class_to_json.py
# Juan Duque <3428@holbertonschool.com>
""" Declare the new function return new dict to json"""


def class_to_json(obj):
    """ Return obj in dict mode"""
    return obj.__dict__
