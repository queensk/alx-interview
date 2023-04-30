#!/usr/bin/python3
"""
Lockbox
"""


def canUnlockAll(boxes):
    """
    Lockbox
    """
    open_boxes = [False] * len(boxes)
    open_boxes[0] = True

    keys = boxes[0]
    while keys:
        key = keys.pop()

        if not open_boxes[key]:
            open_boxes[key] = True
            keys.extend(boxes[key])

    if all(open_boxes):
        return True
    else:
        return False
