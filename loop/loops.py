"""

def remfiras(listx):

    # Step 1: Get the node after head
    node_after_head = listx['head']['next']
    print("hi", node_after_head)
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

listx = { 'head': {'prev': None, 'next': 12}, 
          12: {'prev': 'head', 'next': 20}, 
          20: {'prev': 12, 'next': 15}, 
          15: {'prev': 20, 'next': 2}, 
          2: {'prev': 15, 'next': 'tail'}, 
          'tail': {'prev': 2, 'next': None}
          }

call = remfiras(listx)
print(call)



"""


"""
listx = { 'head': {'prev': None, 'next': 12}, 
          12: {'prev': 'head', 'next': 20}, 
          20: {'prev': 12, 'next': 15}, 
          15: {'prev': 20, 'next': 2}, 
          2: {'prev': 15, 'next': 'tail'}, 
          'tail': {'prev': 2, 'next': None}
          }"""



