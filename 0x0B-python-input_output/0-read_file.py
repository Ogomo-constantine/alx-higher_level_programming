#!/usr/bin/python3

class filename(UTF8):

    def read_file(filename=""):
    with open(filename, "r", encoding="utf8") as f:
        print(f.read())
