"""
Implement the Python function dllc(listx) that returns the sum of the numeric values stored in the nodes 
of the doubly linked list. The structure must be traversed using the references, 
and the original structure must remain unchanged.
"""

dll = {
    'head': {'prev': None, 'next': 12},
    12: {'prev': 'head', 'next': 20},
    20: {'prev': 12, 'next': 15},
    15: {'prev': 20, 'next': 2},
    2: {'prev': 15, 'next': 'tail'},
    'tail': {'prev': 2, 'next': None}
}

def sum_dll(dll):
    current = dll["head"]["next"]  # Start from first actual node
    sum = 0  # Initialize sum

    while current != "tail": # Stop before reaching 'tail'
        sum += current  # Add the node value to sum
        current = dll[current]['next']  # Move to the next node
    return sum  # Return the sum
print(sum_dll(dll))  # Output should be 12 + 20 + 15 + 2 = 49