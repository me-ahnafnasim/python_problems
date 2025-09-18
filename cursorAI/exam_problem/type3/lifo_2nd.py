"""
Content: A stack is stored in a doubly linked list implemented using a dictionary of dictionaries like, for example:
{
    'head': {'prev': None, 'next': 21},
    21: {'prev': 'head', 'next': 13},
    13: {'prev': 21, 'next': 8},
    8: {'prev': 13, 'next': 17},
    17: {'prev': 8, 'next': 'tail'},
    'tail': {'prev': 17, 'next': None}
}.

Implement the Python function stack3(listx, v1) that:
1) creates an empty doubly linked list.
2) insert the (possibly many) elements contained in the listx in function argument so as to implement a stack.
3) inserts the argument v1 into the stack and removes two elements from the stack.
4) returns the doubly linked list.
"""

def stack3(listx, v1):
    new_node = {
        "head":{"prev":None, "next": "tail"},
        "tail":{"prev": "head", "next": None}
    }

    for value in listx:
        node_key = str(value)
        prev_node = new_node["tail"]["prev"]
        
        new_node[node_key] = {
            "prev": prev_node,
            "next": "tail",
            "value": value
        }
      
        new_node[prev_node]["next"] = node_key
        new_node["tail"]["prev"] = node_key


    # Insert v1 (push to stack)
    v1_key = str(v1)
    next_node = new_node["head"]["next"]
    new_node[v1_key] = {
    "prev": "head",
    "next": next_node,
    "value": v1
    }
    new_node["head"]["next"] = v1_key
    new_node[next_node]["prev"] = v1_key

    # Remove two elements from stack
    if len(listx) >= 2:
        first_node = new_node["tail"]["prev"]
        print("hi", first_node)
        second_node = new_node[first_node]["prev"]

        new_node["tail"]["prev"] = new_node[second_node]["prev"]
        new_node[new_node["tail"]["prev"]]["next"] = "tail"

        del new_node[first_node]
        del new_node[second_node]

    
    
    return new_node
    

test_list = [10, 20, 30, 40, 50]
v1 = 60
result = stack3(test_list, v1)
print(result)
    


   
    
    
    
        
        
 

