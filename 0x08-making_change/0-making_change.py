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
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
