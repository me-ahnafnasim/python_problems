#Represent a binary tree as a dictionary

"""
        [root]         (Level 0)
        /    \
      [1]    [10]      (Level 1)
     / \     /  \
   [5] [3] [12] [13]   (Level 2)


btree = {
    # Root node (has no parent)
    'root': {
        'P': None,  # Parent (None for root)
        'L': 1,     # Left child is node 1
        'R': 10     # Right child is node 10
    },
    
    # Left subtree of root (node 1)
    1: {
        'P': 'root',  # Parent is root
        'L': 5,       # Left child is node 5
        'R': 3        # Right child is node 3
    },
    
    # Right subtree of root (node 10)
    10: {
        'P': 'root',  # Parent is root
        'L': 12,      # Left child is node 12
        'R': 13       # Right child is node 13
    },
    
    # Leaf nodes (no children)
    5: {
        'P': 1,       # Parent is node 1
        'L': None,    # No left child
        'R': None     # No right child
    },
    3: {
        'P': 1,       # Parent is node 1
        'L': None,
        'R': None
    },
    12: {
        'P': 10,      # Parent is node 10
        'L': None,
        'R': None
    },
    13: {
        'P': 10,      # Parent is node 10
        'L': None,
        'R': None
    }
}"""




##Represent a binary tree as a dictionary
"""    
       1
       / \
      2   3
     / \  /
    4  5 6
"""

btree = {
    'root': {  # Root container (like your example)
        'P': None,   # Parent (None for root container)
        'L': 1,      # Left child is node 1 (actual root)
        'R': None    # Right child is None (only one root node)
    },
    1: {  # Actual root node (value 1)
        'P': 'root', # Parent is the root container
        'L': 2,      # Left child is node 2
        'R': 3       # Right child is node 3
    },
    2: {
        'P': 1,      # Parent is node 1
        'L': 4,      # Left child is node 4
        'R': 5       # Right child is node 5
    },
    3: {
        'P': 1,      # Parent is node 1
        'L': 6,      # Left child is node 6
        'R': None    # No right child
    },
    4: {
        'P': 2,      # Parent is node 2
        'L': None,   # No left child (leaf)
        'R': None     # No right child (leaf)
    },
    5: {
        'P': 2,      # Parent is node 2
        'L': None,   # No left child (leaf)
        'R': None     # No right child (leaf)
    },
    6: {
        'P': 3,      # Parent is node 3
        'L': None,   # No left child (leaf)
        'R': None     # No right child (leaf)
    }
}


# Get root node
actual_root = btree['root']['L']  # Returns node 1
print('actual_root',actual_root)

# Get left subtree of node 2
left_of_2 = btree[btree[2]['L']]  # Returns node 4
print('left_of_2',left_of_2)

# Check if node is a leaf
def is_leaf(node_key):
    return btree[node_key]['L'] is None and btree[node_key]['R'] is None

print(is_leaf(4))  # True
print(is_leaf(3))  # False