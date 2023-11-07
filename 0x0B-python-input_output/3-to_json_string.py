#!/usr/bin/python3
# 3-to_json_string.py
# Juan Duque <3428@holbertonschool.com>
"""Import librarie json"""
import json


def to_json_string(my_obj):
    """ Return the str in to format json for you
        can append, writin or saving data"""
    return json.dumps(my_obj)
