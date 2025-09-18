"""def lower(tree, root, low):
    smaller = []
    if root is None:
        return 0
    else:
        node = tree.get(root)
        if node is None:
            return 0
        else:
            left_node = node["L"]
            right_node = node["R"]

            if left_node < low and right_node < low:
                smaller.append(left_node, right_node)

            else: 
                return lower(tree, left_node, low) , lower(tree, right_node, low)
    return smaller

root = 'root'
low = 6
btree = {
    'root': {'P': None, 'L': 1, 'R': 10},
    1: {'P': 'root', 'L': 5, 'R': 3},
    10: {'P': 'root', 'L': 12, 'R': 13},
    5: {'P': 1, 'L': None, 'R': None},
    3: {'P': 1, 'L': None, 'R': None},
    12: {'P': 10, 'L': None, 'R': None},
    13: {'P': 10, 'L': None, 'R': None}
}

print(lower(btree, root, low))"""





def lower(tree, root, low):
    if root is None:
        return []
    
    node = tree.get(root)
    if node is None:
        return []
    
    smaller = []
    left_child = node["L"]
    right_child = node["R"]
    
    # Check current node's value (assuming root is the value)
    if root != 'root' and root < low:  # Exclude the 'root' string from comparison
        smaller.append(root)
    
    # Recursively check left and right subtrees
    return smaller + lower(tree, left_child, low) + lower(tree, right_child, low)

root = 'root'
low = 15
btree = {
    'root': {'P': None, 'L': 1, 'R': 10},
    1: {'P': 'root', 'L': 5, 'R': 3},
    10: {'P': 'root', 'L': 12, 'R': 13},
    5: {'P': 1, 'L': None, 'R': None},
    3: {'P': 1, 'L': None, 'R': None},
    12: {'P': 10, 'L': None, 'R': None},
    13: {'P': 10, 'L': None, 'R': None}
}

print(lower(btree, root, low))