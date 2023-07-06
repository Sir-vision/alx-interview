#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

    # Get the total number of boxes
    n = len(boxes)

    # Create a list to track the unlocked status of each box
    unlocked = [False] * n

    # The first box is unlocked
    unlocked[0] = True

    # Start with the first box
    stack = [0]

    # Explore the boxes using a stack-based approach
    while stack:
        # Take the topmost box from the stack
        box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[box]:
            # Check if the key corresponds to a valid box index
            if (0 <= key < n and not unlocked[key]):
                # Mark the box as unlocked
                unlocked[key] = True

                # Add the box to the stack for further exploration
                stack.append(key)

    # Check if all boxes are unlocked
    return all(unlocked)
