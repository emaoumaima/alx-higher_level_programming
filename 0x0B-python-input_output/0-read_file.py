#!/usr/bin/python3
# 0-read_file.py
# Juan Duque <3428@holbertonschool.com>
""" Define the new function to read with statement with"""


def read_file(filename=""):
    """ Reference to statement with """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
