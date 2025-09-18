"""
A binary tree is implemented using a dictionary of dictionaries such as in the example above. Implement the Python 
function btc(tree, root) that returns the sum of the odd values stored in the nodes of the binary tree. 
Only numeric values must be considered. The structure must be traversed using the references.
"""

def sum_odd_nodes(tree, root):
    if root is None:
        return 0
    
    node = tree.get(root)
    if node is None:
        return 0
    
    current_value = root if type(root) is int else 0
    left_child = node["L"]
    right_child = node["R"]

    current_sum = current_value if current_value % 2 !=0 else 0

    return current_sum + sum_odd_nodes(tree, left_child) + sum_odd_nodes(tree, right_child )



# Given tree
btree = {
    'root': {'P': None, 'L': 1, 'R': 10},  # 1 (odd), 10 (even)
    1: {'P': 'root', 'L': 5, 'R': 3},      # 5 (odd), 3 (odd)
    10: {'P': 'root', 'L': 7, 'R': 12},    # 7 (odd), 12 (even)
    5: {'P': 1, 'L': None, 'R': None},     # Leaf (odd)
    3: {'P': 1, 'L': None, 'R': None},     # Leaf (odd)
    7: {'P': 10, 'L': None, 'R': None},    # Leaf (odd)
    12: {'P': 10, 'L': 11, 'R': 13},       # 11 (odd), 13 (odd)
    11: {'P': 12, 'L': None, 'R': None},   # Leaf (odd)
    13: {'P': 12, 'L': None, 'R': None}    # Leaf (odd)
}
root = 'root'
print(sum_odd_nodes(btree, root))  # Output should be sum of all odd nodes