#!/usr/bin/python3
""" LockedClass
"""


class LockedClass:
    def __setattr__(self, attr, value):
        if not hasattr(self, attr) and attr != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(attr)
            )
        super().__setattr__(attr, value)
