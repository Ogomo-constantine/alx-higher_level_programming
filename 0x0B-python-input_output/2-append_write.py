#!/usr/bin/python3

class filename(UTF8):
    def append_write(filename="", text=""):
    """
    Appends a given string to a text file and returns the number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        chars_added = f.write(text)
        return chars_addedi
