"""
A stack is stored in a doubly linked list implemented using a dictionary of dictionaries like, for example,

dll = {
    'head': {'prev': None, 'next': 12},
    12: {'prev': 'head', 'next': 20},
    20: {'prev': 12, 'next': 15},
    15: {'prev': 20, 'next': 2},
    2: {'prev': 15, 'next': 'tail'},
    'tail': {'prev': 2, 'next': None}
}

Implement the Python function `ds1(listx)` that:  
1. Creates an empty doubly linked list,  
2. Inserts the (possibly many) elements contained in the function argument `listx` so as to implement a stack,  
3. Extracts two elements from the stack, and  
4. Returns the doubly linked list. 

#note: The function adds new nodes at the back (end) of the doubly linked list, just before the tail sentinel node

"""


"""def ds1(listx):
    dll = {
        "head":{"prev":None, "next":"tail"},
        "tail":{"prev":"head", "next":None}
    }

    for value in listx:
        node_key = str(value)
        prev_node = dll["tail"]["prev"]

        dll[node_key] = {
            "prev": prev_node,
            "next": "tail",
            "value": value
        }

        dll[prev_node]["next"] = node_key
        dll["tail"]["prev"] = node_key

    if len(listx)>2:
        for _ in range(2):

            node_before_tail = dll["tail"]["prev"]
            prev_node = dll[node_before_tail]["prev"]
            dll["tail"]["prev"] = prev_node
            del dll[node_before_tail]
    return dll
test_list = [10, 20, 30, 40, 50]
result = ds1(test_list)
print(result)"""





def ds1(listx):
    dll ={
        "head": {"prev":None, "next":"tail"},
        "tail":{"prev":"head", "next": None}
    }

    for value in listx:
        node_key = str(value)

        prev_node = dll["tail"]["prev"]

        dll[node_key] ={
            "prev": prev_node,
            "next":"tail",
            "value":value
        }
        dll[prev_node]["next"] = node_key
        dll["tail"]["prev"] = node_key

    if len(listx)>2:
        for _ in range(2):
            node_before_tail = dll["tail"]["prev"]
            prev_node = dll[node_before_tail]["prev"]
            dll["tail"]["prev"] = prev_node
            del dll[node_before_tail]
    return dll


test_list = [10, 20, 30, 40, 50]
result = ds1(test_list)
print(result)






"""#this is a stack follow lifo
def ds1(listx):
    # Step 1: Create an empty doubly linked list
    dll = {
        'head': {'prev': None, 'next': 'tail'},  # Head points to tail initially
        'tail': {'prev': 'head', 'next': None}   # Tail points to head initially
    }
    # Step 2: Insert elements from listx into the stack
    for value in listx:
        # Create a unique key for the new node (using the value itself)
        
        node_key = str(value)  # Using the value as the key
       
        # Insert the new node before the tail
        prev_node = dll['tail']['prev'] # Node currently before the tail
        # Add the new node to the dictionary
        dll[node_key] = {
            'prev': prev_node,  # Previous node
            'next': 'tail',     # Next node (always 'tail')
            'value': value      # Store the value in the node
        }
        # Update connections
        dll[prev_node]['next'] = node_key  # ei code dll[head][next] = 10 ba prothom value ke set kore dei
         # Update the 'next' pointer of the previous node
        dll["tail"]["prev"]= node_key    # Update the 'prev' pointer of the tail
    
  # Step 3: Extract two elements from the stack
    if len(listx) >= 2:
        # Get the top two nodes (closest to the tail)
        first_node = dll['tail']['prev']       # First node to remove
        print("1node",first_node)
        second_node = dll[first_node]['prev']  # Second node to remove
        print("2node",second_node)
        
        # Update connections to bypass the two nodes
        dll['tail']['prev'] = dll[second_node]['prev']  # Tail's 'prev' now points to the node before second_node
        dll[dll[second_node]['prev']]['next'] = 'tail'  # The node before second_node points to 'tail'
        
        # Remove the extracted nodes from the dictionary
        del dll[first_node]
        del dll[second_node]
    
    # Step 4: Return the modified doubly linked list
    return dll



"""