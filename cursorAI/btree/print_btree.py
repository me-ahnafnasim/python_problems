def preorder_with_parent(node, tree, parent=None, direction=""):
    if node is None:
        return
    print(f"Node: {node}, Parent: {parent}, Direction: {direction}")
    preorder_with_parent(tree[node]['L'], tree, node, "L")
    preorder_with_parent(tree[node]['R'], tree, node, "R")


# Your tree
btree = {
    'root': {'P': None, 'L': 1, 'R': 10},
    1: {'P': 'root', 'L': 5, 'R': 3},
    10: {'P': 'root', 'L': 12, 'R': 13},
    5: {'P': 1, 'L': None, 'R': None},
    3: {'P': 1, 'L': None, 'R': None},
    12: {'P': 10, 'L': None, 'R': None},
    13: {'P': 10, 'L': None, 'R': None}
}


preorder_with_parent('root', btree)