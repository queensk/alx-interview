#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        coin_count += total // coin
        total %= coin

    if total != 0:
        return -1

    return coin_count
