# Lockbox

Lockbox is a Python program that allows you to determine if all boxes can be opened based on their contents. Each box may contain keys to other boxes, and a key with the same number as a box can open that box. The program takes in a list of lists representing the boxes and returns True if all boxes can be opened, or False if at least one box cannot be opened.

## Installation
Make sure you have Python 3 installed on your machine.
Clone the repository to your local machine.
Navigate to the project directory.
Run the program using the following command: python lockbox.py

## Usage
The program takes in a list of lists called boxes. Each inner list represents a box, and contains the keys that are inside that box. You can assume that all the keys will be positive integers. The first box (i.e., boxes[0]) is already unlocked, but you need to check if it's possible to unlock all the other boxes. If it is possible, the program will return True. Otherwise, it will return False.

```
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes)) # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes)) # Output: False
```

## Contributing
If you would like to contribute to Lockbox, please fork the repository and submit a pull request. We welcome bug fixes, feature requests, and other contributions.

## License
Lockbox is licensed under the MIT License.
