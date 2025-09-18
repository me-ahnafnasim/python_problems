#Top -> 60 → 50 → 40 → 30 → 20 → 10
#Then we remove 2 elements: 60 and 50
#final result-->Top -> 40 → 30 → 20 → 10



def stack3(listx, v1):
    dll = {
        "head": {"prev": None, "next": "tail"},
        "tail": {"prev": "head", "next": None}
    }

    # Insert elements from listx into the stack
    for value in listx:
        node_key = str(value)
        prev_node = dll["tail"]["prev"]
        
        dll[node_key] = {
            "prev": prev_node,
            "next": "tail"
        }
      
        dll[prev_node]["next"] = node_key
        dll["tail"]["prev"] = node_key

    # Insert v1 (push to stack)
    v1_key = str(v1)
    #prev_node = dll["tail"]["prev"]
    
    dll[v1_key] = {
        "prev": prev_node,
        "next": "tail"
    }
    dll[prev_node]["next"] = v1_key
    dll["tail"]["prev"] = v1_key

    # Remove two elements from the stack
    if len(listx)>2:
        for _ in range(2):
            node_before_tail = dll["tail"]["prev"]
            prev = dll[node_before_tail]["prev"]
            dll["tail"]["prev"] = prev
            dll[prev]["next"] = "tail"
            del dll[node_before_tail]
    return dll

test_list = [10, 20, 30, 40, 50]
v1 = 60
result = stack3(test_list, v1)
print(result)