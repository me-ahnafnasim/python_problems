"""
{
    'head': {'prev': None, 'next': first_key},
    key1: {'prev': 'head', 'next': key2},
    key2: {'prev': key1, 'next': key3},
    ...
    'tail': {'prev': last_key, 'next': None}
}
"""



"""

def ds5(elements):
    # Step 1: Initialize the doubly linked list
    dll = {
        'head': {'prev': None, 'next': None},
        'tail': {'prev': None, 'next': None}
    }
    
    # Initially, head and tail are connected
    dll['head']['next'] = 'tail'
    dll['tail']['prev'] = 'head'

    # Helper function to insert an element at the end
    def insert_at_end(key):
        # New node structure
        new_node = {'prev': None, 'next': None}
        
        # Get the current last node (before 'tail')
        last_node_key = dll['tail']['prev']
        
        # Update pointers for the new node
        new_node['prev'] = last_node_key
        new_node['next'] = 'tail'
        
        # Update pointers for the last node and 'tail'
        dll[last_node_key]['next'] = key
        dll['tail']['prev'] = key
        
        # Add the new node to the dictionary
        dll[key] = new_node

    # Step 2: Insert all elements into the queue
    for elem in elements:
        insert_at_end(elem)

    # Helper function to remove the first element
    def remove_from_front():
        # Get the first node after 'head'
        first_node_key = dll['head']['next']
        
        if first_node_key == 'tail':  # Empty queue
            return
        
        # Get the second node
        second_node_key = dll[first_node_key]['next']
        
        # Update pointers to remove the first node
        dll['head']['next'] = second_node_key
        dll[second_node_key]['prev'] = 'head'
        
        # Remove the first node from the dictionary
        del dll[first_node_key]

    # Step 3: Remove two elements from the front
    remove_from_front()
    remove_from_front()

    # Step 4: Return the resulting doubly linked list
    return dll


# Example Execution
if __name__ == "__main__":
    # Input list
    input_list = [10, 20, 30]
    
    # Call the function
    result = ds5(input_list)
    
    # Print the resulting doubly linked list
    print("Resulting Doubly Linked List:")
    print(result)"""















dll = {'head': {'prev': None, 'next': 12}, 
       12: {'prev': 'head', 'next': 20}, 
       20: {'prev': 12, 'next': 15}, 
       15: {'prev': 20, 'next': 2},
        2: {'prev': 15, 'next': 'tail'},
       'tail': {'prev': 2, 'next': None}}

