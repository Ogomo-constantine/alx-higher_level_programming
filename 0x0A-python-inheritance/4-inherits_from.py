#!/usr/bin/python3
class object:
    def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited (directly or indirectly) from a_class.
    Otherwise, returns False.
    """
    # Check if obj is an instance of a_class
    if isinstance(obj, a_class):
        return True
    # Check if obj's class inherits from a_class
    if issubclass(type(obj), a_class):
        return True
    # If neither case is true, return False
    return False
