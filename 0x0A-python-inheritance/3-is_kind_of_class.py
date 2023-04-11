#!/usr/bin/python3
class object:
    def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of a_class,
    otherwise return False.
    """
    return isinstance(obj, a_class)
