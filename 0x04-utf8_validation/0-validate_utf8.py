#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    data = iter(data)
    for leading_byte in data:
        leading_ones = _count_leading_ones(leading_byte)
        if leading_ones in [1, 7, 8]:
            return False
        for _ in range(leading_ones - 1):
            trailing_byte = next(data, None)
            if trailing_byte is None or trailing_byte >> 6 != 0b10:
                return False
    return True


def _count_leading_ones(byte):
    """
    Counts the leading ones.
    """

    for i in range(8):
        if byte >> 7 - i == 0b11111111 >> 7 - i & ~1:
            return i
    return 8
