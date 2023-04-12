#!/usr/bin/python3

import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Load the existing list from the file, or create an empty list if the file doesn't exist
try:
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []

# Add the command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, 'add_item.json')
