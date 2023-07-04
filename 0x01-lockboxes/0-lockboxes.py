#!/usr/bin/python3

"""
Problem: You have n number of locked boxes in front of you.
         Each box is numbered sequentially from 0 to n - 1
         and each box may contain keys to the other boxes.
Task: Write a method that determines if all the boxes can be opened.
"""


def can_unlock_all(boxes):
    """
    Determines whether all the boxes can be unlocked.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # First box is unlocked by default
    keys_stack = boxes[0]

    while keys_stack:
        key = keys_stack.pop()
        if key < num_boxes and not unlocked_boxes[key]:
            # Unlock the box and add its keys to the stack
            unlocked_boxes[key] = True
            keys_stack.extend(boxes[key])

    return all(unlocked_boxes)

