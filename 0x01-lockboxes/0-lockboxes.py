#!/usr/bin/python3
""" canunlock all function"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes: A list of lists representing boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is unlocked

    keys = [0]  # Start with the keys in the first box

    while keys:
        box_index = keys.pop()  # Get the box index from the keys list

        for key in boxes[box_index]:
            if 0 <= key < len(boxes) and not unlocked[key]:
                unlocked[key] = True  # Mark the box as unlocked
                keys.append(key)  # Add keys found in the box to the keys list

    return all(unlocked)
