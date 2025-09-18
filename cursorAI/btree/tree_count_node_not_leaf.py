
"""
implement a Python function countnodes(tree, root) that counts the number of nodes in a binary tree 
(represented as a dictionary of dictionaries) except for the leaf nodes. The function will traverse the tree using the references 
(parent, left, and right pointers)
"""


def countnodes(tree, root):
    if root is None:
        return 0
    else:
        node = tree.get(root)
        #print("node:",node)
        if node is None:
            return 0
        else:
            left_child = node['L']
            right_child = node['R']
            # Current node is a leaf (no children), don't count it
            if left_child is None and right_child is None:
             return 0
            else:
            # Current node is internal (has at least one child), count it and recurse
             return 1 + countnodes(tree, left_child) + countnodes(tree, right_child)


btree = {
    'root': {'P': None, 'L': 1, 'R': 10},
    1: {'P': 'root', 'L': 5, 'R': 3},
    10: {'P': 'root', 'L': 12, 'R': 13},
    5: {'P': 1, 'L': None, 'R': None},
    3: {'P': 1, 'L': None, 'R': None},
    12: {'P': 10, 'L': None, 'R': None},
    13: {'P': 10, 'L': None, 'R': None}
}

print(countnodes(btree, 'root'))




"""def countnodes(tree, root):
    # Helper function to recursively count non-leaf nodes
    def count_non_leaf_nodes(node_key):
        # Base case: if the node does not exist, return 0
        if node_key is None:
            return 0
        
        # Get the current node's dictionary
        node = tree[node_key]
        
        # Check if the node is a non-leaf node
        is_non_leaf = node['L'] is not None or node['R'] is not None
        
        # Count this node if it is a non-leaf node
        count = 1 if is_non_leaf else 0
        
        # Recursively count non-leaf nodes in the left and right subtrees
        count += count_non_leaf_nodes(node['L'])
        count += count_non_leaf_nodes(node['R'])
        
        return count
    
    # Start the traversal from the given root
    return count_non_leaf_nodes(root)

# Example usage
btree = {
    'root': {'P': None, 'L': 1, 'R': 10},
    1: {'P': 'root', 'L': 5, 'R': 3},
    10: {'P': 'root', 'L': 12, 'R': 13},
    5: {'P': 1, 'L': None, 'R': None},
    3: {'P': 1, 'L': None, 'R': None},
    12: {'P': 10, 'L': None, 'R': None},
    13: {'P': 10, 'L': None, 'R': None}
}

# Count non-leaf nodes starting from the root
result = countnodes(btree, 'root')
print("Number of non-leaf nodes:", result)"""