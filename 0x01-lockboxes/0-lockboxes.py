def canUnlockAll(boxes):
    # set to keep track of visited boxes
    visited = set()

    # queue with the first box
    queue = [0]

    # While there are boxes in the queue
    while queue:
        # Get the next box
        current_box = queue.pop(0)
        
        # Mark current box as visited
        visited.add(current_box)

        # Check all keys in current box
        for key in boxes[current_box]:
            # If key opens a new box and that box hasn't been visited yet
            if key < len(boxes) and key not in visited:
                # Add the new box to the queue
                queue.append(key)

    # If all boxes have been visited, return True, otherwise return False
    return len(visited) == len(boxes)

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
