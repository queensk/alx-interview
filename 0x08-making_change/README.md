# 0x08-making_change

This repository contains the implementation of a solution to the "Making Change" problem. The problem involves determining the fewest number of coins needed to meet a given total amount, given a pile of coins of different values.

## Problem Description

Given a pile of coins with different values and a total amount, the task is to find the fewest number of coins needed to meet the total amount. The requirements for the problem are as follows:

- Prototype: `def makeChange(coins, total)`
- Return: Fewest number of coins needed to meet the total
- If the total is 0 or less, return 0
- If the total cannot be met by any number of coins you have, return -1
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- It is assumed that you have an infinite number of each denomination of coin in the list

## Usage

To use the `makeChange` function, follow the steps below:

1. Import the `makeChange` function from the `0-making_change` module:

```python
from makeChange import makeChange
```

2. Call the `makeChange` function with the list of coins and the total amount:

```python
result = makeChange([1, 2, 25], 37)
print(result)  # Output: 7
```

## Test Cases

The repository includes a `main.py` file that demonstrates the usage of the `makeChange` function with example test cases. Run the `main.py` file to see the output:

```bash
$ python main.py
7
-1
```

## Implementation Details

The implementation of the `makeChange` function utilizes dynamic programming to solve the problem efficiently. It follows the following steps:

1. If the total amount is 0 or less, return 0.
2. Create an array `dp` of size `total + 1` and initialize all elements to infinity except `dp[0] = 0` since it requires 0 coins to make a total of 0.
3. Iterate over each coin value in the `coins` list.
4. For each coin value, iterate over the possible amounts from the coin value to the total amount.
5. Calculate the minimum number of coins required to make the current amount using the current coin. Update `dp[amount]` if the calculated number of coins is smaller than the current value of `dp[amount]`.
6. Finally, check if the minimum number of coins required to make the total amount is still infinity. If so, return -1 to indicate that it is not possible to make the total amount with the given coins.
7. Return `dp[total]`, which represents the fewest number of coins needed to meet the total amount.

## License

This project is licensed under the MIT License. Feel free to use and modify the code as per the license terms.