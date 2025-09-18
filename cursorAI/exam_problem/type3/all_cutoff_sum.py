
#Given a doubly linked list represented as a dictionary (listx) and a numeric threshold (cutoff),
#  write a function dllc(listx, cutoff) that returns the sum of all node keys (converted to integers)
#  that are less than the cutoff value . 

def dllc(listx, cutoff):
    current = listx['head']['next']  # Start at the first actual node
    total = 0
    
    while current != 'tail':
        node_value = int(current)
        if node_value < cutoff:
            total += node_value
        current = listx[current]['next']  # Move to next node
    
    return total

dll = {
    'head': {'prev': None, 'next': 12},
    12: {'prev': 'head', 'next': 20},
    20: {'prev': 12, 'next': 15},
    15: {'prev': 20, 'next': 2},
    2: {'prev': 15, 'next': 'tail'},
    'tail': {'prev': 2, 'next': None}
}