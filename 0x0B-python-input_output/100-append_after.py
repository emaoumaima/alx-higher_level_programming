#!/usr/bin/python3
# 100-append_after.py
# Juan Duque <3428@holbertonschool.com>
""" Define function for append_after list"""


def append_after(filename="", search_string="", new_string=""):
    """ Structure of the new function """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
