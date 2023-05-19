#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    n_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for num in data:
        num = num & 0xFF

        if n_bytes == 0:
            while mask1 & num:
                n_bytes += 1
                mask1 = mask1 >> 1
            if n_bytes == 0:
                continue
            if n_bytes > 4 or n_bytes == 1:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False

        n_bytes -= 1
    return n_bytes == 0
