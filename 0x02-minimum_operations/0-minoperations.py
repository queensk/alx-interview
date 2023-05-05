#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n: int) -> int:
    """
    Minimum Operations
    """
    if n <= 1:
        return 0
    i = 2
    while i <= n:
        if n % i == 0:
            return minOperations(n // i) + i
        i += 1
