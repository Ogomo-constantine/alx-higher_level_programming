#!/usr/bin/python3

def class_to_json(obj):
    """Returns a dictionary description with a simple data structure for JSON serialization"""
    # Get the dictionary representation of the object's attributes
    attr_dict = obj.__dict__

    # Convert each attribute to a serializable type
    for key, value in attr_dict.items():
        if isinstance(value, list):
            # Convert each item in the list to a serializable type
            attr_dict[key] = [class_to_json(item) if isinstance(item, object) else item for item in value]
        elif isinstance(value, dict):
            # Convert each value in the dictionary to a serializable type
            attr_dict[key] = {k: class_to_json(v) if isinstance(v, object) else v for k, v in value.items()}
        elif isinstance(value, bool) or isinstance(value, int) or isinstance(value, str):
            # Attribute is already a serializable type
            pass
        elif isinstance(value, object):
            # Convert the nested object to a dictionary description with a simple data structure
            attr_dict[key] = class_to_json(value)
        else:
            # Attribute is not serializable, raise an exception
            raise TypeError(f"Attribute '{key}' of type '{type(value)}' is not serializable")

    return attr_dict
