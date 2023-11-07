#!/usr/bin/python3
# 1-write_file.py

""" Define function to read new file"""


def write_file(filename="", text=""):
    """"Writing in to fle with statement
        Return - 29

    """
    with open(filename, mode='w', encoding="utf-8") as file:
        value = file.write(text)
    return(value)
