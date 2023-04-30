#!/usr/bin/env python3
"""

"""


def canUnlockAll(boxes):
    """

    """
    open_boxes = [False] * len(boxes)
    open_boxes[0] = True

    keys = [0]
    while keys:
        key = keys.pop()

        for box in boxes[key]:
            if not open_boxes[box]:
                open_boxes[box] = True
                keys.append(box)

    if all(open_boxes):
        return True
    else:
        return False
