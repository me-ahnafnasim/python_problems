"""A doubly linked list is implemented using a dictionary of dictionaries such as, for example:

listx = { 'head': {'prev': None, 'next': 12}, 
          12: {'prev': 'head', 'next': 20}, 
          20: {'prev': 12, 'next': 15}, 
          15: {'prev': 20, 'next': 2}, 
          2: {'prev': 15, 'next': 'tail'}, 
          'tail': {'prev': 2, 'next': None}
          }
with two sentinel nodes (head and tail) and a collection of nodes 12, 20, 15, 2.

Implement the Python function `remfiras(listx)` that removes the node immediately following the head and
 the node immediately preceding the tail. The doubly linked list after removals has to be returned. 
 **The structure must be traversed using the references.**

This text describes the structure of a doubly linked list implemented as a dictionary of dictionaries
 and provides instructions for implementing a function to remove specific nodes from the list.
"""



def remfiras(listx):
    # Make a copy to avoid modifying the original directly (optional)
    listx = dict(listx)

    # Step 1: Get the node after head
    node_after_head = listx['head']['next']
    # Step 2: Get the node before tail
    node_before_tail = listx['tail']['prev']

    # Step 3: Remove node_after_head
    if node_after_head != 'tail':  # Ensure there is a node to remove
        next_node = listx[node_after_head]['next']
        listx['head']['next'] = next_node
        listx[next_node]['prev'] = 'head'
        del listx[node_after_head]

    # Step 4: Remove node_before_tail
    if node_before_tail != 'head':  # Ensure there is a node to remove
        prev_node = listx[node_before_tail]['prev']
        listx['tail']['prev'] = prev_node
        listx[prev_node]['next'] = 'tail'
        del listx[node_before_tail]

    return listx







"""
#remove the element after head and befor tail and return the rest

def remelement(listx):
    node_after_head = listx["head"]["next"]
    node_before_tail = listx["tail"]["prev"]

    if node_after_head != "tail":
        next_node = listx[node_after_head]["next"]
        listx["head"]["next"] = next_node
        listx[next_node]["prev"] = "head"
        del [node_after_head]
    
    if node_before_tail != "head":
        prev_node = listx[node_before_tail]["prev"]
        listx["tail"]["prev"] = prev_node
        listx[prev_node]["next"] = "tail"
        del [node_before_tail]

    return listx


listx = { 'head': {'prev': None, 'next': 12}, 
          12: {'prev': 'head', 'next': 20}, 
          20: {'prev': 12, 'next': 15}, 
          15: {'prev': 20, 'next': 2}, 
          2: {'prev': 15, 'next': 'tail'}, 
          'tail': {'prev': 2, 'next': None}
          }

call = remelement(listx)
print(call)


"""




