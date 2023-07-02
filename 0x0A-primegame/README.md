# 0x0A. Prime Game

## Description

This project is about creating a game where two players take turns to pick prime numbers from a list of consecutive integers. The player who is left with no prime numbers to pick loses the game.

## Learning Objectives

- How to use the Sieve of Eratosthenes algorithm
- How to optimize code performance
- How to write unit tests for Python functions

## Requirements

- Python 3.4 or higher
- PEP 8 style

## Files

- `0-is_prime.py`: A function that checks if a given integer is a prime number.
- `0-main.py`: A main file that tests the `is_prime` function.
- `1-prime_game.py`: A function that simulates the prime game and returns the name of the winner.
- `1-main.py`: A main file that tests the `prime_game` function.

## Usage

To run the tests, execute:

```bash
python3 0-main.py
python3 1-main.py
```

To play the game, import the `prime_game` function and pass the names of the players and the maximum number as arguments. For example:

```python
from 1-prime_game import prime_game

player1 = "Alice"
player2 = "Bob"
max_num = 10

winner = prime_game(player1, player2, max_num)
print(winner)
```


```bash
Alice
```

## Author

[Queens Kisivuli](https://github.com/queensk/)