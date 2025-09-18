
def poplast2(listx):
    for _ in range(2):
        node_before_tail = listx["tail"]["prev"]
        prev_node = listx[node_before_tail]["prev"]
        listx["tail"]["prev"] = prev_node
        listx[prev_node]["next"] = 'tail'
    return listx



listx = { 
    'head': {'prev': None, 'next': 12}, 
    12: {'prev': 'head', 'next': 20}, 
    20: {'prev': 12, 'next': 15}, 
    15: {'prev': 20, 'next': 2}, 
    2: {'prev': 15, 'next': 'tail'}, 
    'tail': {'prev': 2, 'next': None}
}

call = poplast2(listx)
print(call)

