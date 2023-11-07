#!/usr/bin/python3
# 6-load_from_json_file.py
# Juan Duque <3428@holbertonschool.com>
""" Import librarie necesary to json manage"""
import json


def load_from_json_file(filename):
    """ With statement for read and charge new file"""
    with open(filename, 'r') as file:
        return json.load(file)
