#!/usr/bin/python3
# 2-append_write.py
# Juan Duque <3428@holbertonschool.com>
""" Funtion what append new text in file"""


def append_write(filename="", text=""):
    """ Read file with function of the append new text
        Return - 29"""
    with open(filename, 'a') as file:
        value = file.write(text)
    return (value)
