# 0x02. Minimum Operations

## Overview
The goal of this project is to create a Python function called minOperations(n) that calculates the fewest number of operations needed to result in exactly n H characters in a text file. The only two allowed operations are "Copy All" and "Paste".

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.)
- All your functions and coroutines must be type-annotated.

## Files
`0-minoperations.py`: Contains the Python `function minOperations(n)`.
`0-main.py`: Contains examples of how to use the `minOperations(n) function`.

## Function Signature
```
def minOperations(n: int) -> int
```
## Example Usage

```
n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n))) # Output: Min # of operations to reach 9 char: 6

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n))) # Output: Min # of operations to reach 12 char: 7
```
## Author
[Queens Kisivuli](https://github.com/queensk)