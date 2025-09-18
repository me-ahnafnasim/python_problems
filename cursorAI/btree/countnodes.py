def countnodes(tree, root):
    if root is None:
        return 0
    else:
        node = tree.get(root)
        if node is None:
            return 0
        else:
            left_node = node["L"]
            right_node = node["R"]
            
            if left_node is None and right_node is None:
                return 0
            else:
                return 1+countnodes(tree, left_node)+countnodes(tree, right_node)


btree = {'root':{'p': None, 'L': 1, 'R': 10},
1: {'P': 'root', 'L': 5, 'R': 3},
10: {'P': 'root', 'L': 12, 'R': 13},
5: {'P': 1, 'L': None, 'R': None},
3: {'P': 1, 'L': None, 'R': None},
12: {'P': 10, 'L': None, 'R': None},
13: {'P': 10, 'L': None, 'R': None}
}

print(countnodes(btree, 'root'))
