#!/usr/bin/python3

import json

def from_json_string(my_str):
    """Converts a JSON string to its corresponding Python data structure"""
    return json.loads(my_str)
