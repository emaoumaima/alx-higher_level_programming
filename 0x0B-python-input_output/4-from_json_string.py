#!/usr/bin/python3
# 4-from_json_string.py
# Juan Duque <3428@holbertonschool.com>
""" Import librarie to management of json files"""
import json


def from_json_string(my_str):
    """ Return - one string charging in to json format"""
    return json.loads(my_str)
