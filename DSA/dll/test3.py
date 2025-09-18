# --- Node Helper ---
def _create_node(data):
    """Creates a new node dictionary."""
    return {'data': data, 'prev': None, 'next': None}

# --- List State Management ---
def create_list():
    """Creates and returns a new, empty list state dictionary."""
    return {'head': None, 'tail': None, 'size': 0}

def is_empty(list_state):
    """Checks if the list represented by list_state is empty."""
    return list_state['size'] == 0

def get_size(list_state):
    """Returns the number of nodes in the list."""
    return list_state['size']

# --- Insertion Functions ---

def add_first(list_state, data):
    """Adds data to the beginning (head) of the list."""
    new_node = _create_node(data)
    if is_empty(list_state):
        list_state['head'] = new_node
        list_state['tail'] = new_node
    else:
        new_node['next'] = list_state['head']
        list_state['head']['prev'] = new_node
        list_state['head'] = new_node
    list_state['size'] += 1
    # print(f"Added '{data}' to head.") # Optional: for verbosity

def add_last(list_state, data):
    """Adds data to the end (tail) of the list."""
    new_node = _create_node(data)
    if is_empty(list_state):
        list_state['head'] = new_node
        list_state['tail'] = new_node
    else:
        new_node['prev'] = list_state['tail']
        list_state['tail']['next'] = new_node
        list_state['tail'] = new_node
    list_state['size'] += 1
    # print(f"Added '{data}' to tail.") # Optional: for verbosity

def insert_after(list_state, target_data, new_data):
    """Inserts new_data after the first node containing target_data."""
    current = list_state['head']
    while current:
        if current['data'] == target_data:
            if current == list_state['tail']: # Target is the tail
                add_last(list_state, new_data)
            else:
                new_node = _create_node(new_data)
                next_node = current['next']

                # Link new_node
                new_node['prev'] = current
                new_node['next'] = next_node

                # Update surrounding nodes
                current['next'] = new_node
                if next_node:
                    next_node['prev'] = new_node

                list_state['size'] += 1
                # print(f"Inserted '{new_data}' after '{target_data}'.") # Optional
            return True # Indicate success
        current = current['next']
    # print(f"Target data '{target_data}' not found for insertion.") # Optional
    return False # Indicate target not found

def insert_before(list_state, target_data, new_data):
    """Inserts new_data before the first node containing target_data."""
    current = list_state['head']
    while current:
        if current['data'] == target_data:
            if current == list_state['head']: # Target is the head
                add_first(list_state, new_data)
            else:
                new_node = _create_node(new_data)
                prev_node = current['prev']

                # Link new_node
                new_node['prev'] = prev_node
                new_node['next'] = current

                # Update surrounding nodes
                if prev_node: # Should always be true if not head
                   prev_node['next'] = new_node
                current['prev'] = new_node

                list_state['size'] += 1
                # print(f"Inserted '{new_data}' before '{target_data}'.") # Optional
            return True # Indicate success
        current = current['next']
    # print(f"Target data '{target_data}' not found for insertion.") # Optional
    return False # Indicate target not found

# --- Deletion Functions ---

def remove_first(list_state):
    """Removes and returns data from the head of the list."""
    if is_empty(list_state):
        raise IndexError("Cannot remove from an empty list.")

    head_node = list_state['head']
    data_to_remove = head_node['data']
    # print(f"Removing head node with data: '{data_to_remove}'") # Optional

    if list_state['size'] == 1:
        list_state['head'] = None
        list_state['tail'] = None
    else:
        list_state['head'] = head_node['next']
        if list_state['head']: # Check if new head exists
            list_state['head']['prev'] = None

    list_state['size'] -= 1
    # Help garbage collection (optional, but good practice)
    head_node['prev'] = head_node['next'] = head_node['data'] = None
    return data_to_remove

def remove_last(list_state):
    """Removes and returns data from the tail of the list."""
    if is_empty(list_state):
        raise IndexError("Cannot remove from an empty list.")

    tail_node = list_state['tail']
    data_to_remove = tail_node['data']
    # print(f"Removing tail node with data: '{data_to_remove}'") # Optional

    if list_state['size'] == 1:
        list_state['head'] = None
        list_state['tail'] = None
    else:
        list_state['tail'] = tail_node['prev']
        if list_state['tail']: # Check if new tail exists
            list_state['tail']['next'] = None

    list_state['size'] -= 1
    # Help garbage collection
    tail_node['prev'] = tail_node['next'] = tail_node['data'] = None
    return data_to_remove

def remove_node(list_state, data_to_remove):
    """Removes the first node containing the specified data. Returns True if removed, False otherwise."""
    if is_empty(list_state):
        # print("List is empty, cannot remove.") # Optional
        return False

    current = list_state['head']
    while current:
        if current['data'] == data_to_remove:
            # Case 1: Removing the head node
            if current == list_state['head']:
                remove_first(list_state) # This already decrements size
                return True
            # Case 2: Removing the tail node
            elif current == list_state['tail']:
                remove_last(list_state) # This already decrements size
                return True
            # Case 3: Removing a middle node
            else:
                prev_node = current['prev']
                next_node = current['next']
                if prev_node:
                    prev_node['next'] = next_node
                if next_node:
                    next_node['prev'] = prev_node

                list_state['size'] -= 1
                # print(f"Removed node with data: '{data_to_remove}'.") # Optional
                # Help garbage collector
                current['prev'] = current['next'] = current['data'] = None
                return True
        current = current['next']

    # print(f"Data '{data_to_remove}' not found in the list.") # Optional
    return False

# --- Traversal and Utility Functions ---

def find(list_state, data_to_find):
    """Finds the first node containing the specified data. Returns the node dict or None."""
    current = list_state['head']
    while current:
        if current['data'] == data_to_find:
            return current # Return the node dictionary
        current = current['next']
    return None # Data not found

def display_forward(list_state):
    """Prints the list elements from head to tail."""
    if is_empty(list_state):
        print("List is empty.")
        return
    elements = []
    current = list_state['head']
    while current:
        elements.append(str(current['data']))
        current = current['next']
    print("List (forward): " + " <-> ".join(elements))

def display_backward(list_state):
    """Prints the list elements from tail to head."""
    if is_empty(list_state):
        print("List is empty.")
        return
    elements = []
    current = list_state['tail']
    while current:
        elements.append(str(current['data']))
        current = current['prev']
    print("List (backward): " + " <-> ".join(elements))

def iterate_list(list_state):
    """Generator to iterate over the list data from head to tail."""
    current = list_state['head']
    while current:
        yield current['data']
        current = current['next']
        print("print the raw data:")
        print(current)

def list_to_string(list_state):
    """Returns a user-friendly string representation of the list."""
    if is_empty(list_state):
        return "[]"
    # Use the generator to get elements
    elements = [str(item) for item in iterate_list(list_state)]
    return "[" + " <-> ".join(elements) + "]"

# --- Example Usage ---
if __name__ == "__main__":
    # Create the list state dictionary
    my_list_data = create_list()

    print(f"Is empty? {is_empty(my_list_data)}")
    print(f"Length: {get_size(my_list_data)}")
    print(f"List string: {list_to_string(my_list_data)}")
    print("-" * 20)

    # Use functions, always passing the list_state
    add_last(my_list_data, "B")
    add_first(my_list_data, "A")
    add_last(my_list_data, "C")

    print(f"Is empty? {is_empty(my_list_data)}")
    print(f"Length: {get_size(my_list_data)}")
    display_forward(my_list_data)
    display_backward(my_list_data)
    print(f"List string: {list_to_string(my_list_data)}")
    print("-" * 20)

    insert_after(my_list_data, "B", "B.5")
    display_forward(my_list_data)
    insert_before(my_list_data, "A", "START")
    display_forward(my_list_data)
    insert_after(my_list_data, "C", "END")
    display_forward(my_list_data)
    print(f"Length: {get_size(my_list_data)}")
    print("-" * 20)

    node_b = find(my_list_data, "B")
    if node_b:
        # Accessing node data directly (be careful with None checks)
        prev_data = node_b['prev']['data'] if node_b.get('prev') else 'None'
        next_data = node_b['next']['data'] if node_b.get('next') else 'None'
        print(f"Found node B: Data={node_b['data']}, Prev={prev_data}, Next={next_data}")
    else:
        print("Node B not found.")

    node_x = find(my_list_data, "X")
    print(f"Found node X: {node_x}")
    print("-" * 20)

    print("Iterating through list:")
    for item in iterate_list(my_list_data):
        print(f" - {item}")
    print("-" * 20)

    remove_node(my_list_data, "B.5")
    display_forward(my_list_data)
    print(f"Length: {get_size(my_list_data)}")

    removed_head = remove_first(my_list_data)
    print(f"Removed head: {removed_head}")
    display_forward(my_list_data)

    removed_tail = remove_last(my_list_data)
    print(f"Removed tail: {removed_tail}")
    display_forward(my_list_data)

    remove_node(my_list_data, "A")
    display_forward(my_list_data)

    remove_node(my_list_data, "C") # Remove last remaining
    display_forward(my_list_data)
    print(f"Length: {get_size(my_list_data)}")
    print(f"List string: {list_to_string(my_list_data)}")

    # Test removing from empty list (will raise IndexError)
    try:
        remove_first(my_list_data)
    except IndexError as e:
        print(f"\nCaught expected error: {e}")

    # You can create multiple independent lists
    list2_data = create_list()
    add_first(list2_data, 100)
    add_last(list2_data, 200)
    print("\nList 1:", list_to_string(my_list_data))
    print("List 2:", list_to_string(list2_data))