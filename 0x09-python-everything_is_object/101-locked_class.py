#!/usr/bin/python3

class LockedClass:
    __slots__ = 'first_name'

    def __init__(self, first_name):
        self.first_name = first_name

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError(f"{self.__class__.__name__} does not allow setting new attributes")
        super().__setattr__(name, value)
