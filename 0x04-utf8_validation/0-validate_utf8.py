#!/usr/bin/python3
"""
Defines a method that determines if a given data set
represents valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents valid UTF-8 encoding

    parameters:
        data [list of ints]:
            each integer represents 1 byte of data
            data set can contain multiple characters
            each character in UTF-8 can be 1 to 4 bytes long

    returns:
        True if data is valid UTF-8 encoding, False otherwise
    """
    if type(data) is not list:
        return False
    for i in data:
        if type(i) is not int:
            return False
    return True
