"""def ds1(listx):
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
        dll[prev_node]['next'] = node_key  # Update the 'next' pointer of the previous node
        dll['tail']['prev'] = node_key    # Update the 'prev' pointer of the tail
    # Step 4: Return the modified doubly linked list
    return dll

# Test the function
if __name__ == "__main__":
    # Test with a list of numbers
    test_list = [10, 20, 30, 40, 50, 60]
    result = ds1(test_list)
    print(result)"""
    
    
"""
dll = {
    'head': {'prev': None, 'next': 'tail'},  # Head points to tail initially
    'tail': {'prev': 'head', 'next': None}   # Tail points to head initially
}

# New node to insert
node_key = 'A'
dll[node_key] = {'prev': None, 'next': None}  # Initialize the new node

# Insert the new node before 'tail' (i.e., at the end of the list)
prev_node = dll['tail']['prev']  # prev_node is 'head'
dll[prev_node]['next'] = node_key  # head's 'next' is now 'A'
dll[node_key]['prev'] = prev_node  # A's 'prev' is 'head'
dll[node_key]['next'] = 'tail'     # A's 'next' is 'tail'
dll['tail']['prev'] = node_key     # tail's 'prev' is now 'A'"""