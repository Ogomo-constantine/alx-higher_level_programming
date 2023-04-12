#!/usr/bin/python3

import json

def load_from_json_file(filename):
    """Reads a JSON file and returns the corresponding Python data structure"""
    with open(filename, 'r') as f:
        return json.load(f)
